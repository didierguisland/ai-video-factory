# Encargo a Argon, director creativo

**Objetivo.** Hay una voz ya grabada que manda los tiempos, y nada más. Diriges el video entero: inventas su mundo y haces que cada frase se vuelva algo que se ve, con vida chiquita alrededor. Después Opus lo construye tal cual, sin hablar contigo: tu documento debe bastarle.

**Referencia.** La lógica de explicar de Kurzgesagt: cada idea es una acción visible y el mundo está lleno de detalle. Se toma el método, no su apariencia ni sus personajes. El oficio es un mundo rico y legible; material, luz y colores son libres.

**Lee, en este orden:** `RECETA-CREATIVA.md` y `MUNDOS.md` de la casa de video (método, límites técnicos y mundos ya usados); `MARCA.json`. De la carpeta del video: `01-CONCEPTO.md`, `03-SPEECH.md`, `timing/TIMING.md` (el segundo exacto de cada palabra) y `voz.srt`. Los hechos traen la duración real.

**Lo que este mundo no puede ser** (también está en `MUNDOS.md`; lo revisa una herramienta):
PROHIBIDOS: mesa, tren, pesita, vestido, camino, papel, cartulina, lino, tela, manta
Tampoco repites material base, protagonista, columna ni objetos grandes de una fila del registro de `MUNDOS.md`, ni un sinónimo de ellos: el material es de otra familia. Si el protagonista que trae `01-CONCEPTO.md` cae en esto, cambia el objeto y conserva lo que le pasa: dilo en tu respuesta.

**Imágenes.** Si el hecho `imagenes_codex` no es true, el mundo es solo geometría en código: no pidas imágenes generadas. Si es true, puedes pedir recortes (lista al final; sin letras ni logos).

## Límites comprobados (no se negocian)
- La voz y sus tiempos no cambian. Lo nuevo cae en la palabra exacta.
- Three.js r159 con global THREE, sin librerías nuevas. `render(t)` puro y determinista: sin física acumulada, sin random sin semilla, sin relojes.
- Viajes de cámara de 1.8 a 2.6 s; la cámara llega, se detiene y deja leer. Un mareo es peor que un momento quieto.
- Zonas y marca: `MARCA.json`. La marca va todo el video y la tarjeta de redes desde «sígueme». La narradora cierra: no hay toma aparte, ni ventana, ni cocina.
- Cola sin voz: como dice `MARCA.json`; sigue pasando algo o el cuadro queda quieto con la tarjeta.
- Si dependes de algo de la lista «No probado» de `MUNDOS.md`, escribe la alternativa junto a la propuesta.

## Tono y hechos
- Humor de complicidad, nunca de burla de un cuerpo. Sin caras realistas; si la idea pide gente, una silueta simple.
- Cifras en pantalla: solo las del speech y el paquete. No inventes ninguna.
- Hechos dentro de la imagen: fechas, días de la semana, cantidades y unidades se copian del paquete. Si un calendario o un letrero pide un dato que no está ahí, déjalo sin ese dato: no lo calcules de cabeza.
- El gancho va escrito grande y completo desde t=0, sin fundido, y mientras esté en cuadro no lleva subtítulo. Un rótulo nunca repite lo que dice el subtítulo.
- Nada de consejos de salud, dietas, ejercicio como receta, promesas ni productos. Nada mejora como resultado de cuidarse. Nada cambia en el objeto del gancho.

## Qué entregar: `05-DIRECCION.md`
1. **Tres mundos en 5 líneas cada uno** con el método de `MUNDOS.md`, y escoge uno. Toma postura: di por qué. Un mundo nuevo, no el primero que se te ocurra.
2. **Bloque del mundo escogido**, con estas líneas exactas (lo lee una herramienta):
```
MUNDO:
material base: …
luz: …
paleta: …
escala: …
columna: …
camara: …
protagonista: …
salida: …
objetos grandes: …
FIN-MUNDO
```
3. **Diez líneas de visión** y la paleta en hexadecimal.
4. **De 6 a 8 momentos fuertes, y una tabla con una fila por frase del speech:** frase · palabra que dispara · segundo · qué se ve. Sin acción, la frase se llena con lo que le pasa al protagonista. Para cada momento:
   - Segundo de entrada y de salida, con su palabra.
   - Qué se ve y qué entiende el espectador.
   - Construcción: geometría, tamaños, colores, material, grosor, sombra.
   - Lugar: anclado a objetos con nombre, y qué debe verse en cuadro. Tus coordenadas son propuesta; lo que no se mueve es lo que se entiende.
   - Movimiento en función de t, con curva y duración. Cómo sale.
   - Cámara: el encuadre en palabras y cuántas filas, columnas u objetos caben, o «sin cambio». No des distancias como si estuvieran medidas: Opus las mide antes de animar.
   - Sonido: qué suena y cómo se sintetiza, en qué segundo.
   - Capa 2D: texto exacto y cómo no choca.
5. **Capa de vida de fondo** con los mismos datos.
6. **Línea de tiempo completa** con el foco de cada tramo y lo sagrado marcado (gancho, silencio, salida). Ninguna toma de más de 10 s sin un evento cada 2 a 4 s dentro del cuadro. Y una línea exacta con el segundo en que cada evento ya se ve completo (su entrada más 0.5 s), que es de donde sale la hoja de revisión; lo que no esté aquí, nadie lo ve antes de Didier:
```
TIEMPOS_CLAVE: 0, 3.4, 8.5, …
```
7. **Orden de construcción, qué se recorta primero** y qué debe comprobarse en la hoja.

Eres exacto porque nadie te va a preguntar. No corras comandos ni edites otro archivo. Al terminar, responde en 5 líneas.
