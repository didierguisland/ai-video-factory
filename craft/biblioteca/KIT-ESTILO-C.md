# KIT DE ESTILO C "noche plana" (Reels verticales 1080x1920)

> Referencia de diseño, no regla: es el estilo con el que más hemos animado a Example Brand; se usa si va con el proyecto (ver LEEME, "Reglas y referencias"). Las zonas seguras de la sección 2 sí son regla.

Sacado de `MUESTRA-C-noche.html` (aprobada). Todo se dibuja en canvas 2D, sin librerías ni imágenes externas. Lenguaje: formas planas, sin contorno, con una sombra de dos tonos en media luna.

## 1. Paleta, fondo y sombra plana

| Rol | Hex | Uso |
|---|---|---|
| Ciruela (fondo y texto sobre mostaza) | `#2B1B3D` | fondo medio, texto dentro de la píldora, ojos y boca |
| Ciruela claro | `#41295C` | centro luminoso del degradado |
| Ciruela oscuro | `#1B0F29` | bordes del degradado |
| Oscuro | `#1D1030` | sombra del texto grande, óvalos de suelo (alpha .55) |
| Rosa / rosa sombra | `#F4A6B7` / `#E087A2` | cuerpo principal, mejillas, "CEMENTO", firma |
| Mostaza / mostaza sombra | `#F2C14E` / `#D49A2C` | acento, píldora activa, varillas |
| Turquesa / turquesa sombra | `#5CC8C0` / `#3DA39C` | segundo color de personaje, "VARILLA" |
| Crema / crema sombra | `#FBEFD9` / `#E6D2B2` | luna, flechas, estrellas, etiquetas pequeñas |
| Violeta de base | `#5A3E78` / `#47306A` | cimientos, piso |

Regla de uso: máximo 4 colores vivos por escena (rosa, mostaza, turquesa, crema) sobre ciruela. Mostaza = lo que importa ahora.

**Fondo:** degradado radial `createRadialGradient(540,700,80, 540,960,1350)` con paradas 0 `#41295C`, .5 `#2B1B3D`, 1 `#1B0F29`. Encima, unas 90 estrellas (círculos de 0.8 a 3 px, crema, alpha .12-.52) y 6-8 destellos de 8 puntas (`sparkle`) en rosa, mostaza, crema y turquesa. **Grano:** sin grano (Instagram lo recomprime mal). Solo si el degradado del fondo muestra anillos: un grano leve y fijo, aplicado únicamente al fondo y no al cuadro completo (`getImageData` del fondo sumando a R, G y B un mismo valor aleatorio de ±4, semilla fija `rng(99)` para que no parpadee). Por defecto, no llamar a `grain()`.

**Sombra plana en media luna (regla):** cada forma se pinta dos veces. Primero el color sombra llenando toda la forma, y luego, con la forma recortada (`clip`), se pinta el color base desplazado `dx=-20, dy=-10` (luz arriba a la izquierda). Lo que queda a la vista del tono oscuro es una media luna en el borde inferior derecho. Desplazamiento proporcional al tamaño: grande (-26,-16), mediano (-8,-10), chico (-3,0). Nunca degradados ni blur dentro de las formas.

## 2. Tipografía y zonas seguras

Fuente única: `"Avenir Next","Avenir","Helvetica Neue",Arial,sans-serif` (del sistema).

- **Subtítulo karaoke:** 118 px, peso 800. Palabra activa: en la muestra aprobada va en **ciruela `#2B1B3D` sobre píldora mostaza** (mejor contraste que blanco; si se quiere blanca, usar `#fff` con sombra `#1D1030` +3,+3). Palabras no activas: blanco con alpha .55. Píldora: relleno `rr` con radio = 0.63 de la altura, padding horizontal 36, altura 1.26 x tamaño, hueco entre palabras 28. Si el ancho total pasa de 960 px, reducir el tamaño proporcional. Línea base en y=410 (tercio superior). Mayúsculas solo en la palabra clave.
- **Etiqueta del dato:** 100 px, peso 900, letterSpacing 2. Cada palabra en su color (rosa, mostaza, turquesa), con copia desplazada (+6,+7) en `#1D1030` como sombra. Ancho máximo 930 px, centrada, línea base y=1490 (medio-abajo). Rótulos chicos de escena: 40 px, peso 700, letterSpacing 6, crema alpha .75.
- **Firma:** "Example Brand", 46 px, peso 600, letterSpacing 6, rosa alpha .6, centrada, línea base y=1540 (la firma completa queda por encima de y=1570).
- **Zonas seguras:** texto con y ≥ 10 % (192 px); ilustración con y ≥ 7 % (134 px); nada en el 18 % de abajo (y > 1574; ahí van los botones de Instagram y TikTok). Márgenes laterales mínimos de 60 px.

## 3. Reglas de dibujo

- Formas planas, **cero contornos** (nunca `stroke` para siluetas; solo para boca sonriente y rayitas de textura). Todo es polígono relleno.
- Siluetas orgánicas: lista de 30-40 puntos de control y `smooth()` (Catmull-Rom cerrada). Para bordes algo irregulares, `rough()` o `deform()`.
- Personajes simples y simpáticos: cuerpo grande y redondeado, ojos = dos óvalos ciruela (9x11) con un brillo blanco de 3 px arriba a la derecha, mejillas = óvalos rosa (17x12), boca = arco ciruela `lineWidth 7`, `lineCap round`, de .25 a PI-.25 rad. Sin nariz ni cejas.
- **Fémur (hueso):** polígono turquesa (epífisis anchas arriba y abajo, caña estrecha de unos 120 px), dentro un "tuétano" crema obtenido con `inset(hueso, 26)`, salpicado de 40 puntitos (rosa o turquesa claro) como esponjoso. Varillas finas mostaza dentro del tuétano para mostrar el refuerzo.
- **Pared:** `rr` rosa (432x540, radio 28) con borde superior ondulado, 150 granitos de colores (círculos achatados con su propia media luna) como cemento; varillas verticales mostaza (24 de ancho, rayitas diagonales sombra a 45°) y travesaños crema; base violeta de cimentación.
- **Volumen con dos tonos:** siempre `flat(forma, base, sombra, dx, dy)`. Detalles dentro (granitos, rayas) se recortan con `clip` a la forma. Óvalo oscuro aplanado en el suelo debajo de cada objeto (`#1D1030`, alpha .55).
- Flechas: cinta (`ribbon`) crema de 22 px de grosor con punta; los destellos de 8 puntas dan vida (crema, mostaza, rosa).

## 4. Reglas de movimiento (nuevas)

Todo a 30 fps, tiempo `t` en segundos, curvas definidas en el código de abajo.
- **Entrada con rebote suave:** escala 0.8 → 1.05 → 1 en 0.35 s (0→0.21 s sube a 1.05 con `outCubic`, 0.21→0.35 s baja a 1 con `inOutQuad`) más fundido de opacidad 0→1 en los primeros 0.15 s. Escalonar entradas 0.08 s entre elementos.
- **Deslizamiento corto:** 40-60 px máximo, 0.4 s, `outCubic`. Texto desde abajo, objetos laterales desde su lado. Nunca cruzar toda la pantalla.
- **Cambio de escena:** barrido horizontal o fundido de **0.3 s** con `inOutCubic`. Barrido: un rectángulo ciruela `#2B1B3D` entra de izquierda a derecha y sale por la derecha; el contenido cambia justo a la mitad (0.15 s). Nunca cortes secos ni transiciones de más de 0.4 s.
- **Flotación leve en reposo:** `y += sin(t*TAU/3.2 + fase)*8` px y, opcional, escala `1 + sin(...)*0.012`. Fase distinta por elemento. Los destellos titilan: alpha `0.6 + 0.4*sin(t*TAU/1.6 + fase)`.
- **Palabra clave en el karaoke:** la píldora aparece en 0.12 s con "pop": escala del bloque palabra+píldora 0.85 → 1.08 → 1 en 0.25 s, y la palabra anterior baja a alpha .55 en 0.12 s. Un destello crema aparece 0.1 s después y se queda titilando.
- **Cámara:** quieta, o un zoom lento de 1.0 a 1.04 en toda la escena (`linear`). Prohibidos giros, rotaciones mayores a ±3°, sacudidas, parpadeos rápidos y rebotes de más de 1.08.
- Respiro: cada dato nuevo deja 1.2 s mínimo en pantalla antes de cambiar.

## 5. Código base (copiar tal cual)

```js
const W=1080,H=1920,TAU=Math.PI*2;
const C={PLUM:'#2B1B3D',DARK:'#1D1030',PINK:'#F4A6B7',PINKD:'#E087A2',MUS:'#F2C14E',MUSD:'#D49A2C',
 TEAL:'#5CC8C0',TEALD:'#3DA39C',CRM:'#FBEFD9',CRMD:'#E6D2B2'};
const FONT='"Avenir Next","Avenir","Helvetica Neue",Arial,sans-serif';
const cv=document.getElementById('c'),g=cv.getContext('2d');cv.width=W;cv.height=H;

// --- utilidades
function rng(s){s=s>>>0;return()=>{s|=0;s=s+0x6D2B79F5|0;let t=Math.imul(s^s>>>15,1|s);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
const path=(c,p)=>{c.beginPath();c.moveTo(p[0][0],p[0][1]);for(let i=1;i<p.length;i++)c.lineTo(p[i][0],p[i][1]);c.closePath()};
function rr(x,y,w,h,r,step=10){const o=[],a=(cx,cy,a0)=>{for(let i=0;i<=6;i++){const t=a0+i/6*Math.PI/2;o.push([cx+Math.cos(t)*r,cy+Math.sin(t)*r])}};
 a(x+w-r,y+r,-Math.PI/2);a(x+w-r,y+h-r,0);a(x+r,y+h-r,Math.PI/2);a(x+r,y+r,Math.PI);return o}
function circ(cx,cy,rx,ry,n=32){const o=[];for(let i=0;i<n;i++){const a=i/n*TAU;o.push([cx+Math.cos(a)*rx,cy+Math.sin(a)*ry])}return o}

// --- curvas y movimiento
const clamp=(v,a=0,b=1)=>Math.min(b,Math.max(a,v));
const E={outCubic:t=>1-Math.pow(1-t,3),inOutQuad:t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2,inOutCubic:t=>t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2};
// escala de entrada: 0.8 -> 1.05 -> 1 en 0.35 s (t = segundos desde que entra)
function popScale(t,d=.35,lo=.8,hi=1.05){const k=clamp(t/d),k1=.6;return k<k1?lo+(hi-lo)*E.outCubic(k/k1):hi+(1-hi)*E.inOutQuad((k-k1)/(1-k1))}
const popAlpha=t=>clamp(t/.15);
const slideY=(t,dist=50,d=.4)=>dist*(1-E.outCubic(clamp(t/d)));   // suma esto a y
const floatY=(t,ph=0,amp=8)=>Math.sin(t*TAU/3.2+ph)*amp;
const twinkle=(t,ph=0)=>.6+.4*Math.sin(t*TAU/1.6+ph);
// aplica escala/alfa alrededor de (cx,cy) y ejecuta fn
function withPop(t,cx,cy,fn,dy=0){g.save();g.globalAlpha*=popAlpha(t);const s=popScale(t);g.translate(cx,cy+slideY(t)+dy);g.scale(s,s);g.translate(-cx,-cy);fn();g.restore()}
// barrido de escena: p 0..1 durante 0.3 s; devuelve true cuando ya se puede cambiar el contenido (p>=.5)
function wipe(p){const e=E.inOutCubic(clamp(p)),x=-W+2*W*e;g.fillStyle=C.PLUM;g.fillRect(x,0,W,H);return p>=.5}

// --- forma plana con sombra en media luna
function flat(poly,base,shade,dx=-20,dy=-10){g.save();path(g,poly);g.clip();g.fillStyle=shade;g.fill();g.translate(dx,dy);path(g,poly);g.fillStyle=base;g.fill();g.restore()}
function plain(poly,col){path(g,poly);g.fillStyle=col;g.fill()}
function sparkle(x,y,R,col,a=1){const p=[];for(let i=0;i<8;i++){const an=i/8*TAU-Math.PI/2,r=i%2?R*.22:R;p.push([x+Math.cos(an)*r,y+Math.sin(an)*r])}g.save();g.globalAlpha=a;plain(p,col);g.restore()}

// --- fondo con estrellas (dibujar primero); grano opcional y solo del fondo (ver sección 1)
function background(starSeed=31){
 const gr=g.createRadialGradient(540,700,80,540,960,1350);gr.addColorStop(0,'#41295C');gr.addColorStop(.5,C.PLUM);gr.addColorStop(1,'#1B0F29');
 g.fillStyle=gr;g.fillRect(0,0,W,H);
 const r=rng(starSeed);for(let i=0;i<90;i++){const x=r()*W,y=r()*H,s=.8+r()*2.2;g.fillStyle=`rgba(251,239,217,${.12+r()*.4})`;g.beginPath();g.arc(x,y,s,0,TAU);g.fill()}}
function grain(seed=99,amp=8) /* opcional: solo en el fondo y solo si hay anillos; por defecto no se usa */{const img=g.getImageData(0,0,W,H),d=img.data,r=rng(seed);
 for(let i=0;i<d.length;i+=4){const v=(r()-.5)*amp;d[i]+=v;d[i+1]+=v;d[i+2]+=v}g.putImageData(img,0,0)}

// --- texto
function T(str,x,y,size,col,o={}){const{w='800',al='left',ls=0,a=1}=o;g.save();g.font=`${w} ${size}px ${FONT}`;g.textAlign=al;g.textBaseline='alphabetic';
 if('letterSpacing' in g)g.letterSpacing=ls+'px';g.globalAlpha*=a;g.fillStyle=col;g.fillText(str,x,y);g.restore()}
function TW(str,size,w='800',ls=0){g.save();g.font=`${w} ${size}px ${FONT}`;if('letterSpacing' in g)g.letterSpacing=ls+'px';const m=g.measureText(str).width;g.restore();return m}

// --- subtítulo karaoke: words=['es','la','VARILLA'], active=índice activo, tPop=segundos desde que la activa entró
function subtitle(words,active,tPop=9,y=410){
 let S=118;const gap=28,pad=36,wd=()=>words.map((w,i)=>TW(w,S)+(i===active?pad*2:0));
 let q=wd(),tot=q.reduce((a,b)=>a+b,0)+gap*(words.length-1);
 if(tot>960){S=S*960/tot*.98;q=wd();tot=q.reduce((a,b)=>a+b,0)+gap*(words.length-1)}
 let x=540-tot/2;
 words.forEach((w,i)=>{
  if(i!==active)T(w,x,y,S,'#fff',{a:.55});
  else withPop(tPop,x+q[i]/2,y-S*.3,()=>{flat(rr(x,y-S*.92-6,q[i],S*1.26,S*.63,8),C.MUS,C.MUSD,-8,-10);T(w,x+pad,y,S,C.PLUM)});
  x+=q[i]+gap})}

// --- etiqueta del dato: parts=[['CEMENTO',C.PINK],['+',C.MUS],['VARILLA',C.TEAL]]
function label(parts,y=1490){let S=100;const gp=28,ws=()=>parts.map(p=>TW(p[0],S,'900',2));let q=ws(),tot=q.reduce((a,b)=>a+b,0)+gp*(parts.length-1);
 if(tot>930){S=S*930/tot;q=ws();tot=q.reduce((a,b)=>a+b,0)+gp*(parts.length-1)}
 let x=540-tot/2;parts.forEach(([t,c],i)=>{T(t,x+6,y+7,S,C.DARK,{w:'900',ls:2});T(t,x,y,S,c,{w:'900',ls:2});x+=q[i]+gp})}

// --- firma
const signature=()=>T('Example Brand',540,1540,46,C.PINK,{al:'center',ls:6,a:.6,w:'600'});

// --- cuadro tipo (orden de dibujo): background → escena → subtitle → label → signature (sin grano)
// function frame(t){background();/*escena con flat()*/;subtitle(['es','la','VARILLA'],2,t-1.2);label([['CEMENTO',C.PINK],['+',C.MUS],['VARILLA',C.TEAL]]);signature();}
```

Nota: para exportar a video, renderizar cuadro a cuadro a 1080x1920 y juntar con FFmpeg a 30 fps.

## 6. Movimiento para explicar (28-oct, aprendido de Kurzgesagt; probada en limón y sed)

Complementa la sección 4; no la reemplaza. El porqué está en `GUIA-EXPLICAR.md`.
- **Un foco por escena:** el sujeto ocupa 35-60% del ancho útil. Capas: fondo, sujeto, acento; otra capa solo si aclara.
- **Conexión que se dibuja:** una línea o cinta crema crece de 0 a 100% en 0.5-0.8 s (`inOutCubic`); el nodo de llegada hace `popScale` al terminar. Sirve para "esto provoca aquello".
- **Revelado de dato:** máscara o panel que descubre el dato en 0.25-0.35 s (`inOutCubic`). El barrido de la sección 4 sigue siendo el cambio de escena.
- **Destello de evento:** cuando algo ocurre (un encuentro, un cambio), halo crema o mostaza fuera de la silueta: 0.18-0.3 s, alpha máxima 0.6-0.8, `shadowBlur` 12-24 px. Uno a la vez. Nunca blur dentro de las formas.
- **Partículas:** 4-10 puntitos alrededor del foco, se mueven 10-30 px en 1.5-3 s, alpha 0.15-0.45, nunca encima del texto.
- **Paralaje opcional:** por cada 20 px que se mueve el sujeto, el fondo se mueve 4-8 px. La cámara sigue sin pasar de zoom 1.04.
- **Flotación con fases distintas** para que nada se mueva al unísono (ya está en `floatY`, solo variar `ph`).
