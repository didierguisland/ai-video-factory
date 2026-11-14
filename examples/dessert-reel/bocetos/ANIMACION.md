# Animación · El huequito del postre (encargo de Opus, 10-nov)

Eres un constructor nuevo: no necesitas la historia de las rondas. Lee solo esto, `ESPEC.md` (estilo, personajes y cuadros; las «Notas del constructor» dicen cómo quedó cada uno), `boceto.html` (los 10 cuadros ya aprobados) y `../voz.srt` (+ `../TIEMPOS.md`). Para copiar el reproductor, los subtítulos y el método, mira `../../2026-11-09-buen-fin/bocetos/animacion.html` (no su estilo).

## Qué se entrega
- `animacion.html` aquí, partiendo de una copia de `boceto.html` (que queda como está). Canvas 1080×1920, `window.DURATION = 44.6`, `window.seek(t)` puro (el cuadro depende solo de t; nada de estado acumulado), para renderizar a MP4 después con el mismo archivo.
- Reproductor (lo pide Didier: HTML completo, todavía no MP4): Reproducir/Pausa, barra de tiempo y reloj, audio `../voz.wav` sincronizado (el tiempo sale de `audio.currentTime`). Canvas escalado a la ventana, centrado, fondo oscuro. Controles fuera del canvas u ocultos con `?render=1`.
- Subtítulos del `../voz.srt` embebidos como datos (no fetch), en la banda y 1390–1560, ≥ 60 px, grafito grueso #3A3A3C sobre pastilla crema con borde fino; máximo 2 líneas, ~5 palabras por línea, palabra por palabra igual a lo que se oye. «1981» se escribe así.
- `REVISION-ANIMACION.png`: hoja reducida con un cuadro por golpe (unos 20). No hagas MP4.

## Reglas de movimiento (mandan)
- Un foco que se mueve por momento; lo demás casi quieto (respiración leve). Nunca todo moviéndose a la vez.
- Orden de preferencia (Muse): caras que reaccionan, zoom a un detalle, algo que cae o rebota; cambios rápidos solo al final. Algo nuevo cada 2–4 s; sin voz y sin evento, máximo 3.5 s.
- Stickers con ease-out y un poco de overshoot. Cámara: viajes de 1.8–2.6 s, suaves, nunca moviéndose mientras aparece un texto; sin vueltas de más de 90°.
- Textos grandes entran con pop corto cuando la voz llega a ese momento y se quedan quietos.
- Cortes limpios entre escenas (o barrido ≤ 0.3 s), nada de fundidos largos. «Example Brand» fija todo el video. Sin tarjeta de «sígueme».
- Último ~0.8 s quieto.

## Golpes por escena (tiempos de la voz)
1. **0–2.7** · Desde el cuadro 0 ya hay conflicto (nada de pantalla vacía): el pastel ya va a medio colarse, el texto del gancho con pop en 0.15. El pastel avanza de puntitas un poco más (0–1.5) mirando de reojo; el cadenero levanta la mano de golpe y abre la boca en «O» (~1.2).
2. **2.7–6.8** · «Dices ya no puedo» → la mano hace «hasta aquí» (2.8–3.6) y se desploma en el brazo de la silla (~4.6); el globito con la batería al 100 % hace pop (~4.8) y la batería tiembla de llena.
3. **6.8–11.5** · «llega el pastel» (~7.0) → la campana sube y revela el pastel con halo; «mágicamente» (~8.8) → la mano revive y atrapa el tenedor en el aire; en el silencio 10.3–11.5, tink-tink (dos golpecitos del tenedor, el pastel parpadea).
4. **11.5–18.1** · Escena larga: no la dejes quieta. 11.5 entra el cadenero mirando el interruptor; ~14.5 lo piensa (cejas); «saciedad sensorial específica» (~16.5) → sube la palanca a NUEVO con chispa dorada y destello en sus lentes.
5. **18.1–22.0** · El plato salado cansado avanza arrastrando (18.1–20.0); ~20.1 la cortina vino cae y rebota en seco, el texto MISMO SABOR: NO PASA con pop; el plato parpadea resignado.
6. **22.0–26.1** · **PICO (con 7):** el pastel diva entra en pasarela con chispitas (22.0–24.0); ~24.2 la manita se baja los lentes, la cereza destella como flash.
7. **26.1–31.2** · **PICO:** el cadenero se quita los lentes, ojos de estrella que se encienden (~26.3), reverencia; ~28.6 desengancha el cordón y abre la SALA VIP con luz miel; empuje suave hacia la puerta. Este paso del 6 al 7 es lo que la gente va a querer ver otra vez: dale el mejor timing y la mejor reacción de cara del video.
8. **31.2–35.5** · «guárdalo para la posada» (31.8) → texto con pop; la cucharita corta la puntita (~33.6) con destello.
9. **35.5–39.6** · La aguja del ANTOJO baja en dos pasos con cada bocado (~36.0 y ~37.8) hasta la palomita salvia (pop).
10. **39.6–44.6** · Silbidito visual (notitas) y el cadenero vuelve a abrir el cordón (~39.8); entra corriendo la tacita con su gafete SOBREMESA (40.8–42.0); ~43.2 guiño del cadenero a cámara; quieto desde ~43.8.

## Arreglo pendiente
Cuadro 6: la punta del tallo de la cereza roza la pastilla de «PASE DIRECTO». Mueve el texto o el pastel unos píxeles para que respiren.

## Revisión propia
Mira tu `REVISION-ANIMACION.png` UNA vez: zonas libres, nada cortado, un foco por golpe, subtítulos sin tapar caras. Verifica que `seek(t)` dé el mismo cuadro dos veces y que corra fluido. Notas al final de este archivo en «Notas del animador».

## Notas del animador (10-nov)
- Entregado: `animacion.html` (copia de `boceto.html` con `montar(t)` animado por escena, `DURATION = 44.6`, `seek(t)` puro) y `REVISION-ANIMACION.png` (24 cuadros, uno por golpe, 6 por fila). `boceto.html` no se tocó. Reproductor: Reproducir/Pausa (también barra espaciadora), barra y reloj; el tiempo sale de `audio.currentTime` de `../voz.wav`; con `?render=1` se ocultan los controles y el canvas queda a 1080×1920.
- Verificado: `seek(t)` da el mismo cuadro dos veces (1.3, 24.5 y 29.3 s, comparando el PNG completo); cero errores JS; ~4 ms por cuadro en el Chrome de puppeteer, así que debería ir fluido (si una máquina va lenta, el reproductor salta cuadros, no se desfasa del audio).
- Subtítulos: el SRT viene palabra por palabra; los agrupé a mano en 23 frases (tabla `N` en el código; si se cambia el SRT hay que ajustarla, y avisa en consola si no cuadra). Cada frase dura de su primera a su última palabra (+0.6 s máx.). La última se queda hasta el final para que el último tramo quede quieto. «1981» sale así.
- Pico 6→7: la diva entra contoneándose (22.0–24.0), se planta con rebote, la manita aparece (24.05) y se baja los lentes (24.2–24.55) y la cereza hace flash en «llega» (24.7). Corte limpio a 26.1: el 7 arranca más cerca de la cara del cadenero (doble toma: boca en «O» con lentes 26.1–26.3, se los arranca y los ojos de estrella se encienden con sobregiro, rayitas y rubor en 26.3). Texto con pop en 26.75, reverencia 27.3–28.1, cordón se desengancha 28.6, la puerta se abre con luz miel 28.7–29.5 y la cámara viaja hacia la puerta 28.75–31.15 (después del texto); destello en el letrero en 30.5.
- Cambios de encuadre respecto a los bocetos: 6 con la cámara un poco más arriba (el tallo ya no roza «PASE DIRECTO», ~40 px de aire); 7 empieza más cerrado; en 5 el plato va más atrás (z 1.3, escala 1.1) y en 10 la tacita también (z 1.5, escala 1.7) porque sus caras caían bajo los subtítulos.
- Desvíos: la mano del «hasta aquí» (2) se lee más como «mano plana estirada» que como el gesto clásico; en 4 el guante del cadenero descansa a la altura de su moño antes de subir la palanca (se ve un poco suelto); en 8 la cucharita llega por abajo y casi todo su viaje queda tras los subtítulos (solo se ve claro el corte). La cortina del 5 enrollada deja ver el marco vacío antes de caer. El 10 no tiene cordón entre dos postes: el cadenero sostiene el extremo y lo alza.

## Notas del animador · ronda 2 (10-nov)
- 1: el «¡alto!» ahora es una palma abierta de frente (sticker 2D de guante blanco sobre el brazo 3D, que se levanta más vertical), arriba y a la derecha de la cereza, sin encimarse.
- 2: el «hasta aquí» es la mano con la palma hacia abajo a la altura del cuello (arriba del cuadro, con los dedos hacia cámara), con golpecitos verticales y una línea punteada de nivel «lleno hasta aquí» (3.0–4.6). Se sigue leyendo un poco como mano plana; el gesto de verdad pide la muñeca doblada, que la mano 3D no tiene.
- 3: tras atraparlo, el tenedor rebota, baja al plato (9.35–10.2) y da dos golpecitos en 10.4 y 10.9, con arquitos de sonido y parpadeo del pastel en cada uno.
- 6: manita con guante blanco de contorno vino y grafito, más grande. Los lentes bajan más y en diagonal (los ojos y las pestañas quedan a la vista desde ~24.4). El flash de la cereza ahora es breve y chico, en 24.8–25.15.
- 7: estrellas grandes (1.3×), doradas claras con halo y un pulso leve hasta ~30.5. Se asientan un poco después. La puerta abre desde 28.6, y en 28.75–29.45 los dos postes se corren a la orilla con el cordón colgando: la entrada queda libre y se ve el interior dorado.
- 8: la cucharita viaja por arriba de la banda de subtítulos. Su mango cruza el cuerpo del pastel bajo la boca, sin tapar la cara.
- 9: «ANTOJO» va más arriba, sobre una pastillita crema dibujada encima de la aguja, para que nunca la tape. La rebanada ya no tiene escalones: cada bocado es una mordida redonda en la punta de arriba (recorte 2D sobre la capa del pastel, con contorno) y crece en el segundo bocado.
- 10: el cadenero levanta el cordón (39.75) y lo suelta en 40.35–40.75. Cae colgando del poste antes de que la tacita entre en 40.8. Gafete 1.3× más grande.
- Rehecha `REVISION-ANIMACION.png` con los mismos 24 tiempos. `seek(t)` sigue determinista y no hay errores JS.
