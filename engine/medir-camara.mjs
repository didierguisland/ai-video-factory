#!/usr/bin/env node
// medir-camara.mjs <reel.html> <CAMARA.md> [--paso 0.1]: nadie del equipo ve el movimiento antes que Didier; esto lo mide.
// Pide window.seek(t) y lee la variable global `camera` (o window.camera). Separa quietud de viaje y marca lo que mareó:
// viajes rápidos, más de un viaje en 4 s y tramos largos con la misma toma. Los pasos cortos que la receta permite (0.6 a 1 s,
// poca distancia) se cuentan aparte y no son aviso. Es un sustituto del ojo, no el ojo: calibrado con dos videos.
import { createRequire } from 'node:module';
import { pathToFileURL, fileURLToPath } from 'node:url';
import path from 'node:path';
import fs from 'node:fs';

const RENDER = process.env.HUMANIFY_RENDER_DIR || path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const require = createRequire(path.join(RENDER, 'package.json'));
const puppeteer = require('puppeteer');

const a = process.argv.slice(2); let PASO = 0.1; const pos = [];
for (let i = 0; i < a.length; i++) { if (a[i] === '--paso') PASO = Number(a[++i]); else pos.push(a[i]); }
if (pos.length !== 2) { console.error('Uso: medir-camara.mjs <reel.html> <CAMARA.md> [--paso 0.1]'); process.exit(2); }
const [HTML, MD] = pos.map(p => path.resolve(p));
const navegador = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox', '--allow-file-access-from-files'] });
let muestras;
try {
  const pagina = await navegador.newPage();
  await pagina.setViewport({ width: 1080, height: 1920 });
  await pagina.goto(pathToFileURL(HTML).href, { waitUntil: 'load' });
  await pagina.evaluate(() => window.renderReady);
  muestras = await pagina.evaluate(async (paso) => {
    const cam = () => (typeof camera !== 'undefined' ? camera : window.camera);
    if (typeof window.seek !== 'function' || !cam()) return null;
    const salida = [];
    for (let t = 0; t <= window.DURATION + 1e-6; t += paso) {
      await window.seek(t);
      const c = cam(), d = c.getWorldDirection(new c.position.constructor());
      salida.push([t, c.position.x, c.position.y, c.position.z, d.x, d.y, d.z, c.fov]);
    }
    return salida;
  }, PASO);
} finally { await navegador.close(); }
if (!muestras) { console.error('El HTML no expone window.seek(t) ni una variable global camera.'); process.exit(1); }

// Rapidez relativa al tamaño del escenario, para que el umbral sirva en cualquier mundo.
const PASO_LARGO_MAX = 0.2, PASO_GIRO_MAX = 20, TOMA_LARGA = 10, TOMA_MAXIMA = 13;
const distancia = (a, b) => Math.hypot(a[1] - b[1], a[2] - b[2], a[3] - b[3]);
const angulo = (a, b) => Math.acos(Math.min(1, Math.max(-1, a[4] * b[4] + a[5] * b[5] + a[6] * b[6]))) * 180 / Math.PI;
// El escenario es la caja de todo lo que recorre la cámara: medir desde t=0 hacía que el mismo paso contara distinto según dónde arrancó.
const eje = k => { const v = muestras.map(m => m[k]); return Math.max(...v) - Math.min(...v); };
const ancho = Math.max(1e-6, Math.hypot(eje(1), eje(2), eje(3)));
const moviendo = [];
for (let i = 1; i < muestras.length; i++) {
  const v = distancia(muestras[i], muestras[i - 1]) / ancho, g = angulo(muestras[i], muestras[i - 1]), f = Math.abs(muestras[i][7] - muestras[i - 1][7]);
  moviendo.push(v > 0.0008 || g > 0.05 || f > 0.02);
}
const viajes = [];
for (let i = 0; i < moviendo.length; i++) {
  if (!moviendo[i]) continue;
  let j = i; while (j + 1 < moviendo.length && (moviendo[j + 1] || moviendo[j + 2])) j++;
  const giro = angulo(muestras[i], muestras[j + 1]);
  viajes.push({ de: muestras[i][0], a: muestras[j + 1][0], giro, largo: distancia(muestras[i], muestras[j + 1]) / ancho });
  i = j;
}
const total = muestras[muestras.length - 1][0];
const enMovimiento = viajes.reduce((s, v) => s + v.a - v.de, 0);
const avisos = [];
// Un paso corto de acercamiento (como 8 % del escenario, 0.6 a 1 s) sí gustó; lo que marea es cruzar el mundo rápido.
const pasoCorto = v => v.a - v.de <= 1.2 && v.largo <= PASO_LARGO_MAX && v.giro <= PASO_GIRO_MAX;
const pasos = viajes.filter(pasoCorto), largos = viajes.filter(v => !pasoCorto(v));
// La misma toma: entre dos movimientos, o desde el principio o hasta el final. Se permite hasta 13 s si el cuadro cambia cada 2 a 4 s.
const quietos = [];
let desde = muestras[0][0];
for (const v of viajes) { quietos.push([desde, v.de]); desde = v.a; }
quietos.push([desde, total]);
for (const [de, a] of quietos) {
  const dur = a - de;
  if (dur > TOMA_LARGA) avisos.push(`misma toma ${de.toFixed(1)}-${a.toFixed(1)} (${dur.toFixed(1)} s)${dur > TOMA_MAXIMA ? ', pasa de los ' + TOMA_MAXIMA + ' s' : ''}: mira que cambie algo cada 2 a 4 s`);
}
viajes.forEach((v, k) => {
  const dur = v.a - v.de;
  if (dur < 1.8 && !pasoCorto(v) && (v.largo > PASO_LARGO_MAX || v.giro > PASO_GIRO_MAX)) avisos.push(`viaje rápido: ${v.de.toFixed(1)}-${v.a.toFixed(1)} s (${dur.toFixed(1)} s)`);
  if (dur > 4.5) avisos.push(`viaje de ${dur.toFixed(1)} s en ${v.de.toFixed(1)} s: «se pierde tiempo» (Didier) si va sin voz`);
  if (v.giro > 90) avisos.push(`giro de ${v.giro.toFixed(0)}° en ${v.de.toFixed(1)} s`);
  if (k && v.de - viajes[k - 1].a < 1.0) avisos.push(`sin parada antes de ${v.de.toFixed(1)} s`);
});
const lineas = [`Cámara: ${largos.length} viajes y ${pasos.length} pasos cortos, en movimiento ${(100 * enMovimiento / total).toFixed(0)} % de ${total.toFixed(1)} s (el video que gustó: 24 %).`,
  'Viajes: ' + (largos.map(v => `${v.de.toFixed(1)}-${v.a.toFixed(1)} (${(v.a - v.de).toFixed(1)} s)`).join(', ') || 'ninguno'),
  'Pasos cortos: ' + (pasos.map(v => `${v.de.toFixed(1)}-${v.a.toFixed(1)}`).join(', ') || 'ninguno'),
  avisos.length ? 'AVISOS: ' + avisos.join('; ') : 'AVISOS: ninguno'];
fs.writeFileSync(MD, lineas.join('\n') + '\n');
console.log(lineas.join('\n'));
