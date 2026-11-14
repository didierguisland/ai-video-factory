#!/usr/bin/env node
// hoja-html.mjs <archivo.html> <salida.png> [--cada 2] [--tiempos 1,3.5,8] [--tiempos-de 05-DIRECCION.md] [--y-cada 2]
// --y-cada junta los dos: un cuadro cada N s y además uno en cada tiempo clave. Lo que cae entre dos cuadros no se puede juzgar.
// --tiempos-de lee la línea 'TIEMPOS_CLAVE: 0.5, 6.2, …' de ese archivo (relativo a la carpeta del HTML): la hoja
// muestra cada escena en su pose clave, no un cuadro cada N s. Si el archivo o la línea faltan, usa --cada.
// Hoja de cuadros de un HTML de canvas con window.seek(t) (y window.DURATION), sin renderizar video ni usar modelos.
// Usa el puppeteer instalado en la raíz del repo (npm install); otra carpeta con HUMANIFY_RENDER_DIR.
import { createRequire } from 'node:module';
import { pathToFileURL, fileURLToPath } from 'node:url';
import path from 'node:path';
import fs from 'node:fs';

const RENDER = process.env.HUMANIFY_RENDER_DIR || path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const require = createRequire(path.join(RENDER, 'package.json'));
const puppeteer = require('puppeteer');

const pos = []; let CADA = 2, TIEMPOS = null, TIEMPOS_DE = null, JUNTAR = false;
const a = process.argv.slice(2);
for (let i = 0; i < a.length; i++) {
  if (a[i] === '--cada') CADA = Number(a[++i]);
  else if (a[i] === '--y-cada') { CADA = Number(a[++i]); JUNTAR = true; }
  else if (a[i] === '--tiempos') TIEMPOS = a[++i].split(',').map(Number);
  else if (a[i] === '--tiempos-de') TIEMPOS_DE = a[++i];
  else pos.push(a[i]);
}
if (pos.length !== 2 || !(CADA > 0)) {
  console.error('Uso: node hoja-html.mjs <archivo.html> <salida.png> [--cada 2] [--tiempos 1,3.5,8]');
  process.exit(2);
}
const [HTML, PNG] = pos.map(p => path.resolve(p));
if (!fs.existsSync(HTML)) { console.error('No existe: ' + HTML); process.exit(2); }
if (TIEMPOS_DE && !TIEMPOS) {
  const archivo = path.resolve(path.dirname(HTML), TIEMPOS_DE);
  const linea = fs.existsSync(archivo) ? fs.readFileSync(archivo, 'utf8').match(/TIEMPOS_CLAVE:\**[ \t]*([\d.,\t ]+)/) : null;
  const leidos = linea ? linea[1].split(',').map(x => Number(x.trim())).filter(x => Number.isFinite(x)) : [];
  if (leidos.length) TIEMPOS = leidos;
  else console.log('tiempos clave: no hay línea TIEMPOS_CLAVE en ' + TIEMPOS_DE + '; uso un cuadro cada ' + CADA + ' s');
}

const navegador = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
const errores = [];
try {
  const pagina = await navegador.newPage();
  pagina.on('pageerror', e => errores.push(e.message));
  await pagina.setViewport({ width: 1080, height: 1920 });
  await pagina.goto(pathToFileURL(HTML).href, { waitUntil: 'load' });
  const duracion = await pagina.evaluate(() => Number(window.DURATION) || 0);
  if ((await pagina.evaluate(() => typeof window.seek)) !== 'function') {
    throw new Error('el HTML no expone window.seek(t)');
  }
  const parejos = Array.from({ length: Math.max(1, Math.ceil(duracion / CADA)) }, (_, k) => k * CADA);
  let tiempos = TIEMPOS || parejos;
  if (JUNTAR) {
    // Sin dos cuadros a menos de 0.3 s: serían el mismo. Lo que pase de la duración no existe.
    const clave = (TIEMPOS || []).filter(t => t >= 0 && (!duracion || t <= duracion));
    tiempos = parejos.concat(clave.filter(t => !parejos.some(p => Math.abs(p - t) < 0.3))).sort((x, y) => x - y);
  }
  const cuadros = [];
  for (const t of tiempos) {
    cuadros.push(await pagina.evaluate(async t => {
      await window.seek(t);
      const c = document.querySelector('#c') || document.querySelector('#cv') || document.querySelector('canvas');
      return c.toDataURL('image/jpeg', 0.7);
    }, t));
  }
  // La hoja se compone en el mismo navegador: 6 por fila, celdas de 270x480 con su segundo.
  const COLS = Math.min(cuadros.length > 36 ? 8 : 6, cuadros.length), W = 270, H = 480;
  const hoja = await navegador.newPage();
  await hoja.setViewport({ width: COLS * W, height: Math.ceil(cuadros.length / COLS) * H });
  await hoja.setContent('<body style="margin:0;background:#000"><canvas id="h"></canvas></body>');
  await hoja.evaluate(async (cuadros, tiempos, COLS, W, H) => {
    const c = document.getElementById('h');
    c.width = COLS * W; c.height = Math.ceil(cuadros.length / COLS) * H;
    const x = c.getContext('2d');
    for (let i = 0; i < cuadros.length; i++) {
      const im = new Image(); im.src = cuadros[i]; await im.decode();
      const px = (i % COLS) * W, py = Math.floor(i / COLS) * H;
      x.drawImage(im, px, py, W, H);
      x.fillStyle = 'rgba(0,0,0,.6)'; x.fillRect(px, py, 58, 26);
      x.fillStyle = '#fff'; x.font = 'bold 16px sans-serif'; x.fillText(tiempos[i].toFixed(1) + ' s', px + 6, py + 18);
      x.strokeStyle = '#000'; x.lineWidth = 2; x.strokeRect(px, py, W, H);
    }
  }, cuadros, tiempos, COLS, W, H);
  fs.mkdirSync(path.dirname(PNG), { recursive: true });  // _verificar/ no existe la primera vez y el agente no tiene mkdir
  await (await hoja.$('#h')).screenshot({ path: PNG });
  console.log('hoja: ' + PNG + ' (' + tiempos.length + ' cuadros: ' + tiempos.map(t => t.toFixed(1)).join(', ') + ')');
  console.log('Errores JS: ' + (errores.length ? errores.slice(0, 3).join(' | ') : 'ninguno'));
} catch (e) {
  console.error('hoja-html: ' + e.message);
  process.exitCode = 1;
} finally {
  await navegador.close();
}
