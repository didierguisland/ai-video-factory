#!/usr/bin/env node
// render.mjs <archivo.html> <audio.wav|mp4> <salida.mp4> [--fps 30] [--segundos N]
// Renderiza un HTML de canvas (con window.seek(t) y, de preferencia, window.DURATION) cuadro por cuadro a MP4:
// H.264 crf 18, yuv420p, AAC 192k, +faststart. Usa puppeteer y ffmpeg-static de node_modules en la raíz del repo (npm install).
// Duración: window.DURATION; si no hay, la del audio. --segundos limita para pruebas. Canvas: #c, #cv o el primer <canvas>.
// Audio: ruta a un wav/mp4, o la palabra 'ninguno' para renderizar con silencio (demo sin voz).
// Ejemplo (desde la raíz del repo): node engine/render.mjs examples/dessert-reel/bocetos/animacion.html ninguno out/demo.mp4 --segundos 3
import { createRequire } from 'node:module';
import { spawn, spawnSync } from 'node:child_process';
import { pathToFileURL, fileURLToPath } from 'node:url';
import path from 'node:path';
import fs from 'node:fs';

const aqui = path.dirname(fileURLToPath(import.meta.url));
const renderDir = process.env.HUMANIFY_RENDER_DIR || path.resolve(aqui, '..');  // raíz del repo, donde npm install dejó puppeteer y ffmpeg-static
const require = createRequire(path.join(renderDir, 'package.json'));
const puppeteer = require('puppeteer');
const FFMPEG = require('ffmpeg-static');

// --- argumentos
const pos = []; let FPS = 30, LIMITE = null, W = 1080, H = 1920;
const a = process.argv.slice(2);
for (let i = 0; i < a.length; i++) {
  if (a[i] === '--fps') FPS = Number(a[++i]);
  else if (a[i] === '--segundos') LIMITE = Number(a[++i]);
  else if (a[i] === '--ancho') W = Number(a[++i]);
  else if (a[i] === '--alto') H = Number(a[++i]);
  else pos.push(a[i]);
}
if (pos.length !== 3 || !(FPS > 0)) {
  console.error('Uso: node render.mjs <archivo.html> <audio.wav|mp4> <salida.mp4> [--fps 30] [--segundos N]');
  process.exit(2);
}
const SIN_AUDIO = pos[1] === 'ninguno';
const [HTML, AUDIO, OUT] = pos.map(p => path.resolve(p));
for (const f of SIN_AUDIO ? [HTML] : [HTML, AUDIO]) if (!fs.existsSync(f)) { console.error('No existe: ' + f); process.exit(2); }
fs.mkdirSync(path.dirname(OUT), { recursive: true });

// duración del audio (ffmpeg-static no trae ffprobe: se lee de la salida de ffmpeg -i)
function duracionAudio(f) {
  const r = spawnSync(FFMPEG, ['-i', f], { encoding: 'utf8' });
  const m = /Duration: (\d+):(\d+):(\d+\.\d+)/.exec(r.stderr || '');
  return m ? (+m[1]) * 3600 + (+m[2]) * 60 + parseFloat(m[3]) : null;
}
const durAudio = SIN_AUDIO ? null : duracionAudio(AUDIO);

const browser = await puppeteer.launch({ headless: true, args: ['--no-sandbox', '--allow-file-access-from-files'] });
const page = await browser.newPage();
await page.setViewport({ width: W, height: H, deviceScaleFactor: 1 });
const errs = [];
page.on('console', m => { if (m.type() === 'error') errs.push('console: ' + m.text()); });
page.on('pageerror', e => errs.push('pageerror: ' + e.message));
await page.goto(pathToFileURL(HTML).href + '?render');
await page.evaluate(() => document.fonts && document.fonts.ready);
await page.evaluate(() => window.renderReady);   // si el HTML la define; si no, undefined y sigue
await new Promise(r => setTimeout(r, 1000));

const info = await page.evaluate(() => {
  const cv = document.getElementById('c') || document.getElementById('cv') || document.querySelector('canvas');
  return { seek: typeof window.seek === 'function', dur: typeof window.DURATION === 'number' ? window.DURATION : null,
           canvas: cv ? (cv.id ? '#' + cv.id : 'canvas') : null };
});
if (!info.seek) { console.error('El HTML no expone window.seek(t).'); await browser.close(); process.exit(1); }
if (!info.canvas) { console.error('No encontré <canvas> (#c, #cv ni ninguno).'); await browser.close(); process.exit(1); }

let DUR = info.dur ?? durAudio;
if (!DUR) { console.error('No pude saber la duración (ni window.DURATION ni audio).'); await browser.close(); process.exit(1); }
const DUR_COMPLETA = DUR;
if (LIMITE) DUR = Math.min(DUR, LIMITE);
const N = Math.ceil(DUR * FPS);
console.log(`html=${path.basename(HTML)} canvas=${info.canvas} DURATION=${info.dur ?? '(sin definir)'} audio=${durAudio?.toFixed(2)} -> ${DUR.toFixed(2)} s, ${N} cuadros a ${FPS} fps`);
if (!LIMITE && durAudio && durAudio > DUR + 0.05)
  console.warn(`AVISO: el audio (${durAudio.toFixed(2)} s) es más largo que el video (${DUR.toFixed(2)} s) y se cortará. Sube window.DURATION o congela el final con video.sh congelar.`);

// apad + -shortest: si el audio es más corto se rellena con silencio; el video (finito) manda la duración final.
const ff = spawn(FFMPEG, ['-y', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'png', '-i', '-',
  ...(SIN_AUDIO ? ['-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo'] : ['-i', AUDIO]),
  '-map', '0:v', '-map', '1:a', '-af', 'apad', '-shortest', '-t', String(DUR),
  '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-r', String(FPS),
  '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', OUT], { stdio: ['pipe', 'inherit', 'pipe'] });
let log = ''; ff.stderr.on('data', d => { log += d; log = log.slice(-2000); });
const done = new Promise(r => ff.on('close', r));
const t0 = Date.now();
for (let i = 0; i < N; i++) {
  const b64 = await page.evaluate(async (t, sel) => {
    await window.seek(t);
    return document.querySelector(sel).toDataURL('image/png').split(',')[1];
  }, i / FPS, info.canvas);
  if (!ff.stdin.write(Buffer.from(b64, 'base64'))) await new Promise(r => ff.stdin.once('drain', r));
  if (i % 300 === 0) console.log(`cuadro ${i} / ${N}  ${((Date.now() - t0) / 1000).toFixed(0)} s`);
}
ff.stdin.end();
const code = await done;
console.log(`ffmpeg salió con ${code} en ${((Date.now() - t0) / 1000).toFixed(0)} s -> ${OUT}`);
console.log('Errores JS en la página:', errs.length ? '\n' + errs.join('\n') : 'ninguno');
if (code) console.log(log);
await browser.close();
process.exit(code ? 1 : 0);
