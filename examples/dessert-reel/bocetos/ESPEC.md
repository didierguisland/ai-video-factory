# Bocetos El huequito del postre · encargo de construcción (Opus, 10-nov)

Dirección creativa: `../argon-tomas.md` (Argon; manda en encuadre, luz y detalles) y `../TOMAS-v1.md` (lo aterrizado por Opus). **Este archivo manda cuando choque** (ya trae las correcciones de Muse).
Referencia de estructura y herramientas (no de estilo): `../../2026-11-09-buen-fin/bocetos/ESPEC.md` y su `boceto.html`. Copia de ahí la arquitectura (seek puro, mundo 3D + capa 2D, render de PNG y hoja), no el tocador ni la paleta.

## Qué se entrega
1. `boceto.html` aquí: UN HTML con canvas `#cv` 1080×1920, `window.DURATION = 44.6`, `window.seek(t)` async y puro. `ESCENAS = [{desde, hasta, montar(), pose(t)}]`, un `mundo` 3D compartido y `capa2D(ctx, escena, t)` encima. Por ahora cada escena es su cuadro congelado (pose clave); la animación viene después sobre esta estructura.
2. Three.js local: `vendor/three.min.js` (three.js r159, MIT). Nada de CDN.
3. `cuadro-1.png` … `cuadro-10.png` (1080×1920) en los tiempos de abajo y `HOJA.png` (los 10 reducidos, dos filas de 5). Hoja: `node engine/hoja-html.mjs boceto.html HOJA.png --tiempos <los 10>`; PNG sueltos con un script tuyo en el scratchpad usando el puppeteer instalado en la raíz del repo.

## Mundo y estilo (amarra los 10)
- **Foyer de teatro matinée, de tarde:** nogal mate, terrazo crema con motitas, cromo cepillado, terciopelo vino. Luz de tarde ABUNDANTE y cálida desde tragaluces altos (~4200 K) + relleno generoso: nada de penumbra. Muse: el pastel tiene que BRILLAR contra el terciopelo vino; si el vino oscurece el cuadro, aclara el fondo o pon el pastel contra crema.
- 3D: formas simples con bordes boleados, `MeshStandardMaterial` mate (roughness ≥ 0.7; cromo cepillado metalness ~0.6, roughness 0.4). Cero plástico brillante, cero rojo saturado. ACES. Sombras suaves.
- 2D encima, como sticker: trazo grafito #3A3A3C uniforme, rellenos planos: caras (ojos, cejas, bocas), destellos, líneas cinéticas, globitos, gafete, letreros.
- Paleta: crema vainilla #F1E6D2, nogal #7A5638, terciopelo vino #6E2A35, coral empolvado #D98C7A, salvia #A9B8A0, grafito #3A3A3C, cromo #B9BCC0, dorado mate #C9A45C. Betún marfil #FBF5EA, cereza carmín mate #A23B45.
- Texto grande: sans gruesa del sistema (Avenir Next Heavy o Helvetica Neue Bold), grafito sobre pastilla crema si hace falta contraste; 6 palabras máximo en 2 líneas; desde y=280.
- Marca "Example Brand" fija en x 540, y 196–248, alto 52, discreta.
- Zonas: nada clave entre y 1390–1560 (subtítulos) ni bajo y 1574; márgenes laterales 64 px. Protagonista ≥ 18 % del ancho. Un foco por cuadro. Sin marcas reales. Sin subtítulos en los bocetos. Letras y números siempre en la capa 2D.
- Personajes (fijos en los 10): **Cadenero-cerebro**: cabeza en forma de cerebro coral empolvado mate, esmoquin grafito, guantes blancos, lentes oscuros cuadrados. **Pastel diva**: rebanada alta de tres capas vainilla, betún marfil, cereza carmín mate, lentes cat-eye. **Plato salado**: plato hondo hueso con borde salvia, guisado café, corbata floja y ojeras (cansado, no asqueroso). **Tacita**: expreso crema con borde dorado, patitas, gafete VIP «SOBREMESA» en el asa. **La señora**: solo su mano (pulsera de cromo) y su silla de nogal; nunca cuerpo ni cara.

## Los 10 cuadros (tiempo del PNG)
1. **0–2.7 · t=1.0** · Puerta acolchada de nogal con letrero «LLENO». El PASTEL GRANDE AL FRENTE, a medio entrar, colándose; el cadenero detrás, de lado, con la mano ARRIBA (¡alto!) y cara de sorpresa. Sin letrero de «Club del Antojo» aquí. Texto: «¿POR QUÉ SIEMPRE / CABE EL POSTRE?».
2. **2.7–6.8 · t=5.0** · Respaldo de silla de nogal y la mano de la señora desplomada sobre el brazo de la silla (gesto «hasta aquí» ya hecho); globito crema con batería al 100 %. Texto: «NO CABE UN ALFILER».
3. **6.8–11.5 · t=9.0** · Barra de terrazo al sol; campana de cromo levantada, el pastel revelado brillando; los dedos revividos atrapan un tenedor en el aire, líneas cinéticas. Texto: «¡MILAGRO DE SOBREMESA!».
4. **11.5–18.1 · t=15.5** · El atril del cadenero con un interruptor doble grande: «REPETIDO» abajo/apagado, «NUEVO» arriba/encendido, chispa dorada; el dedo enguantado acaba de subirlo. Es el único texto del cuadro (Muse: nada de sello 1981). Sin texto grande extra.
5. **18.1–22.0 · t=20.5** · El plato salado cansado (ficha «3ª»), y la cortina metálica vino recién bajada frente a él; el cadenero ni voltea. Texto (sobre la cortina): «MISMO SABOR: / NO PASA».
6. **22.0–26.1 · t=24.0** · El pastel diva en pasarela sobre terrazo crema, bajándose los lentes; la cereza destella; chispitas doradas. Texto: «SABOR NUEVO: / PASE DIRECTO».
7. **26.1–31.2 · t=29.0** · El cadenero sin lentes, ojos de estrella, reverencia; el cordón de terciopelo descolgado y la puerta «SALA VIP» abierta con luz miel. Texto: «CERO CULPA: / ES TU CEREBRO».
8. **31.2–35.5 · t=33.5** · Dentro de la sala VIP: el pastel en platito almendra, cucharita de cromo con la puntita cortada (bocado chico). Texto: «GUÁRDALO PARA / LA POSADA».
9. **35.5–39.6 · t=37.5** · Platito con el pastel a medias y, al lado, un medidor retro de nogal con aguja: «ANTOJO» que va bajando hacia una palomita salvia. Texto: «POSTRE AL FINAL, / EN PEDACITO». (No usar «el primer bocado sabe mejor»: no lo respalda el estudio).
10. **39.6–44.6 · t=42.0** · Puerta VIP: el cadenero sostiene el cordón abierto y guiña a cámara; entra corriendo de ladito la tacita con gafete «SOBREMESA». Texto: «MÁNDASELO A LA DE / "YA NO PUEDO"».

**Revisión propia:** mira tu HOJA una vez: zonas libres, nada cortado, un solo foco, que el pastel brille contra el vino y que el cuadro 1 se entienda en 1 segundo a tamaño de celular. Verifica que `seek(t)` dé el mismo cuadro dos veces. No hagas MP4 ni animación.

Notas de lo que no salga: al final, en «Notas del constructor».

## Notas del constructor (10-nov)
- Entregado: `boceto.html` (seek puro, `DURATION = 44.6`, 10 ESCENAS con `montar/pose/dibujar` sobre un `mundo` 3D compartido y capa 2D en dos pases), `three.min.js` local, `cuadro-1…10.png` (1080×1920) en 1.0, 5.0, 9.0, 15.5, 20.5, 24.0, 29.0, 33.5, 37.5, 42.0 y `HOJA.png` en 2 filas de 5. `seek(9.0)` dos veces da el mismo cuadro (comprobado); cero errores JS.
- HOJA: `hoja-html.mjs` arma 6 por fila (6+4), no 2×5. Lo corrí tal cual para validar (sin errores) y la `HOJA.png` de aquí sale de un script mío de 5 columnas con el mismo seek.
- Vino: el `#6E2A35` bajo esta luz se volvía rojo saturado; en 3D uso vino más oscuro (`#5A2E36` / `#4A262C`) para que se lea vino mate. El pastel brilla contra él en el cuadro 1 (puerta acolchada); en 6 está contra crema con telones vino a los lados y halo cálido 2D detrás; en 3 y 8 también lleva halo.
- Cuadro 1: pastel al frente (≈48 % del ancho) con cara pícara y cat-eye, cadenero detrás de 3/4 con la mano arriba, boca en «O» y rayitas; «LLENO» en placa de la puerta. A tamaño celular se lee, pero son tres cosas (pastel, cadenero, letrero): si se quiere más rápido, quitar las líneas cinéticas o agrandar el pastel.
- La rebanada se lee como pastel por las capas y la cereza, pero de frente se ve algo «rectangular»; en el 9 el «a medias» (punta cortada) casi no se nota. Sugerencia: más corte o migajas en 2D.
- Cuadro 4: el interruptor es una palanca de dos posiciones (NUEVO arriba, dorado y con brillo; REPETIDO abajo, gris); el guante entra desde arriba a la derecha. Sin texto grande, como pide.
- Cuadro 5: el cadenero está de espaldas (no se le ve cara) junto a la cortina; la cara del plato quedó en la panza del plato, abajo; la corbata cuelga del borde.
- Lentes de los personajes, moño, letreros, gafete, batería y medidor (aguja, zonas, palomita) van en 2D. El «SALA VIP» quedó en el dintel (más chico) para no chocar con el texto grande.
- Pies y bases de algunos personajes (1, 6, 7, 10) caen entre y 1390 y 1650; ahí no hay caras ni letras.

## Notas del constructor · ronda 2 (10-nov)
- Nuevo objeto `telonFondo` (telón vino mate cerrado, pliegues + fleco dorado) detrás del pastel en 3, 6, 8 y 9, con halo cálido 2D entre telón y pastel. Sobre el telón, la marca «Example Brand» pasa a crema para que se lea.
- 3: la mano entra en diagonal desde abajo a la derecha y cierra el puño sobre el mango del tenedor (el tenedor sale arriba y abajo del puño); la campana sigue alzándose arriba a la izquierda.
- 6: telón cerrado detrás (sin pared crema); lentes a media nariz y un bracito 2D con manita enguantada que jala el armazón.
- 8: pastel al 85 % y más abajo (la cereza ya no toca «LA POSADA»); punta con hueco de cuchara; la cucharita al frente, en la punta, con el bocado triangular.
- 9: medidor invertido (salvia y palomita a la izquierda, carmín a la derecha), aguja caída a la izquierda, flecha curva de bajada por fuera del arco; «ANTOJO» libre. Pastel al 95 % con las capas de arriba ya comidas (escalón) y hueco en la punta: el «a medias» se lee, aunque parece más escalón que mordida.
- 2: barras de la batería en carmín mate y sin las rayitas sobre el «100 %».
- 5: cadenero en 3/4 de frente, serio, con los brazos cruzados (brazos rectos cruzados al frente: se lee como bloqueo, no es un cruce de brazos anatómico). Plato sin corbata, «3ª» más grande y ojeras más marcadas.
- Se rehicieron los 10 PNG (los 1, 4, 7 y 10 salen iguales) y la HOJA; seek determinista y cero errores JS.

## Notas del constructor · ronda 3 (10-nov, notas de Muse)
- 1: la diva mira de reojo al cadenero (pupilas pegadas a la derecha, párpado a media asta, una ceja arriba) y va más inclinada, de puntitas. Lo demás igual.
- Pastel (1, 3, 8, 9): contorno fino vino mate por fuera del trazo grafito y cereza a 1.4×. El 6 no se tocó (bandera `r2`), así que ahí la cereza queda del tamaño anterior y sin contorno vino: si se quiere idéntica, es una línea.
- 4: el cadenero entra de medio cuerpo detrás del atril, con la cara visible: cejas arriba, media sonrisa y destellos dorados en los lentes. El guante que sube la palanca es su brazo (la manga apunta a su hombro). Va sin contorno de sticker para que el atril lo tape bien. Riesgo: su cabeza pesa casi tanto como el interruptor; si «NUEVO» debe mandar más, acercar la cámara al atril.
- 2: globito y batería a ~1.6× (globito entre y 545 y 915), batería con barras carmín y «100 %» grande.
- 8 y 9: cámara un poco más arriba para que la cereza grande no toque el texto.
- PNG rehechos: 1, 2, 3, 4, 8, 9 y la HOJA. Los PNG 5, 6, 7 y 10 son idénticos byte a byte a los de la ronda 2.
- Ronda 3b (aprobado): el 6 ya lleva la cereza a 1.4× y el contorno vino fino, como los demás; nada más cambió en ese cuadro. Rehechos `cuadro-6.png` y la HOJA.
