> Parte de la fábrica: empieza en `Videos/fabrica/LEEME.md`; esta receta es la biblioteca de la ruta html-explica.

# Receta: Reel animado de Example Brand, de la idea al MP4
Probada el 28-oct-2026 con un primer Reel de ejemplo (64 s). Salió muy bien a la primera. El proceso y la capa de retención se siguen igual; lo visual (estilo C, píldora, colores) es referencia y se escoge según el proyecto.

> **Desde el 29-oct, quién hace qué y con qué comando lo manda `ARQUITECTURA-BARATA.md`** (probada con "La sed no avisa"). Lo de abajo sigue valiendo para el QUÉ; donde choque el quién, manda la arquitectura (por ejemplo, el speech lo escribe Opus y el detalle pasa por Sol y Argon).

## Quién hace qué
- **Didier:** trae la idea (muchas veces de la persona que lleva la cuenta), decide en cada puerta, pone la voz (AI Studio u otra, según la ruta; ver paso 4) y pega prompts en la app de Claude.
- **Opus (Claude Code):** piensa el ángulo, escribe encargos, el speech y el storyboard, y arma el prompt final. No construye ni renderiza.
- **Codex Terra (high, solo lectura):** verifica datos con fuente.
- **Gemini (agy):** Argon (medium) da analogías y dirección de arte; Flash (medium) la lluvia de ganchos y chistes. Opus elige.
- **Sonnet (subagente):** trámites con muchos tokens: leer prompts largos, bocetos de estilo, kit, render.
- **Opus en la app de Claude:** construye la animación (HTML).

## Los pasos
**0. Tema.** Se elige con `Bases/ELEGIR-TEMA.md`.

**1. Ángulo (Opus + Didier, plática).** Se toma la idea del dueño de la cuenta como referencia, no tal cual. Se busca el giro contra la creencia ("no es solo para arrugas") y una analogía de la casa mexicana que cualquier señora entienda (pared, cemento y varillas; nada de "colado"). Se define el público: señoras de 50 a 60.

**2. Datos y materia prima, en paralelo.**
- Terra: `codex --search exec --skip-git-repo-check -C <carpeta> -m gpt-6.1-terra -c model_reasoning_effort="high" -s read-only -o <ruta ABSOLUTA>/REPORTE.md - < ENCARGO.md` (o `herramientas/llamar.sh terra ENCARGO.md REPORTE.md`). Pedir: veredicto por dato (cierto, matizar o mito), frase segura de 10 a 20 palabras, fuente, y las frases que NO se deben decir. Ejemplo: `EJEMPLO-encargo-terra.md`.
- Argon: `agy -p "No uses herramientas ni comandos: contesta directo en texto. $(cat ENCARGO.md)" --model gemini-4-argon-medium --sandbox --print-timeout 600s > REPORTE.md`; Flash: lo mismo con `--model gemini-3.8-flash-medium` y `--print-timeout 300s` (o `herramientas/llamar.sh argon|flash ENCARGO.md REPORTE.md`). High solo si medium sale pobre. Sin la frase inicial se queda vacío (intenta usar comandos). Pedir ganchos de 2 s con su imagen, chistes de señoras y comadres, analogías dibujables, remates "no es X, es Y" y frases de "mándaselo a tu comadre que…". Ejemplo: `EJEMPLO-encargo-gemini.md`.
- Gemini promete sin querer ("pide colado nuevo"): filtrar todo contra la lista de frases prohibidas de Terra.

**3. Speech (Opus).** Con el checklist de `Bases/investigacion/videos/ANALISIS-patron-reels.md`, unas 120 palabras (meta de 45 s; hasta 65 s, unas 180 palabras, si el tema lo pide y el arranque retiene; cuéntalas con `herramientas/video.sh contar`):
- Pregunta + giro en los primeros 2 segundos.
- **Regla de los 5 segundos:** justo después del giro, prometer algo que se paga a los dos tercios ("y cuando te lo tomas, pasa algo que casi nadie sabe… pero primero:") y repetir la promesa al pagarla ("y aquí está lo que casi nadie sabe").
- Un número traducido ("de cada 10 gramos, 3"), una analogía por idea, "y lo más curioso" antes del segundo giro.
- Remate espejo del gancho y "Sígueme y mándaselo a tu comadre que…" (con chiste).
- Nada que ligue un síntoma con el producto (ej. un síntoma cotidiano NO se liga con el producto).
- Para los datos curiosos que explican cómo funciona el cuerpo: metáfora con oficio, viaje de escala y plantilla de 45 s de `GUIA-EXPLICAR.md` (aprendido de Kurzgesagt).

**4. Voz (la fija la ficha del video; criterio por ruta).** En html-explica y documento, Didier la graba en Google AI Studio; en video-real, la voz de la persona del propio video; en ia-omni, la que genera Omni cuando los personajes hablan en cuadro (salió mejor), y AI Studio solo si es un narrador fuera de cuadro. En AI Studio caben una o dos voces (máximo dos): cada línea del speech empieza con su etiqueta `Nombre:` (por ejemplo `Example Brand:` y `Tía:`), en un solo bloque con etiquetas `<short pause>`, `<long pause>`, `<chuckles>`, `<laughs>`. Tono: "Warm, friendly, conversational, like a Mexican woman in her fifties talking to a close friend. Mexican Spanish. Light humor, never salesy." No pedir "faster": apura de más y en tema serio valen más esos segundos.

**5. Timing por palabra.** Whisper local primero (`python3 -m uv run --python 3.12 --with faster-whisper --with numpy python transcribe.py <voz.wav> <carpeta> --texto SPEECH.md` (script no incluido en este repo): faster-whisper large-v3-turbo con uv aislado, con el speech grabado como referencia de ortografía). Plan B, solo si lo local falla: un chat de la app de Claude saca el SRT (su red a veces no deja instalar). Opus lo pasa a formato compacto ("palabra 0.16–0.43 ·").

**6. Storyboard (Opus).** Tabla por escena: tiempo, qué se ve (un dibujo literal por frase), palabra de la píldora y etiqueta del dato (solo 3 o 4 en todo el video). Un hilo visual que sostenga la promesa (el sobrecito "¿?" que espera en la esquina y se abre al pagarla). Si explica un mecanismo, marcar dónde van conexiones que se dibujan, revelados y el destello (KIT-ESTILO-C, sección 6). Didier lo aprueba. Ejemplo: `Bases/investigacion/colageno/STORYBOARD-v1.md`.

**7. Prompt para la app.** Se juntan tres archivos en uno y se copia al portapapeles:
`cat ENCABEZADO-PROMPT.md KIT-ESTILO-C.md STORYBOARD.md > PROMPT.md && LANG=en_US.UTF-8 pbcopy < PROMPT.md`
En el encabezado se cambian `<TEMA>` y `<DURACIÓN DEL WAV>`. **La duración es la del audio completo**, no la de la última palabra; si no, se corta la risa del final.

**8. Construcción (Opus en la app de Claude, chat nuevo).** Primero entrega un HTML con un cuadro fijo por escena. Didier lo revisa (y si quiere, Opus aquí da una segunda opinión) y se aprueba con ajustes. Luego hace la animación completa. El audio NO se sube (Claude no lo escucha); va al final como voz.wav.

**9. Render (subagente Sonnet).** Con `node engine/render.mjs <html> <voz.wav> <salida.mp4>` (Chrome sin ventana + ffmpeg-static de `Videos/render/node_modules`; `--segundos 2` para una prueba rápida): cuadro por cuadro con `window.seek(i/30)`, por pipe a ffmpeg, H.264 crf 18, AAC 192k, `+faststart`. Revisar 3 cuadros de muestra. Unos 4 minutos.
Si el audio sale más largo que el video, no se re-renderiza: se congela el último cuadro con `engine/video.sh congelar <entrada> <segundos> <salida> <voz-original>` (`tpad=stop_mode=clone`; el cuarto argumento vuelve a pegar la voz original completa).

## Capa de retención (29-oct-2026, obligatoria en cada Reel)
De dónde sale: el video de las "3 claves", comprobado con Terra, Sol, Argon, una búsqueda en TikTok y nuestros números (`Bases/investigacion/retencion/SINTESIS-2.md`). En nuestros tres primeros Reels la gente se iba en el segundo 1.

1. **Chicle (segundo 0 a 2): el primer cuadro ES la duda de la señora.** Va escrita en grande y dicha en voz, sin portada, sin título de serie, sin saludo (vale en todas las rutas, también en "una amiga me preguntó") y sin animación que "va entrando". Un solo objeto o cuerpo y fondo limpio. Fórmulas que pegan: "¿Te ha pasado…?" (que se reconozca), cifra con promesa ("3 señales de…") o reto que puede hacer ya ("Pruébalo ahora…"). La portada o el logo de la serie van después del segundo 3, o como marco que ya está desde el cuadro 1.
2. **Paleta (de 3 s al final): algo nuevo que ayuda a entender, más o menos cada 2 a 4 s, siempre ligado al gancho.** Imagen, dato, giro o cambio de toma. Hay que dejar tiempo para leer. En el storyboard se hace una tabla por tramos de 2 s: si un tramo no trae nada nuevo, se marca.
3. **Pay de manzana (el cierre): se paga lo prometido y se da algo para llevarse o mandar.** Antes de construir: ¿la última frase responde la primera? Si no, se reescribe el gancho, porque un gancho que no se cumple es "traición". Al final: "mándaselo a tu comadre que…" (los envíos son la señal que más pesa) y el puente a la siguiente edición o al producto.
4. **Duración:** meta de 45 s (unas 120 palabras); se acepta hasta 65 s si el tema lo pide y el arranque retiene; más de 75 s no, salvo documento (horizontal, otro público). Va en la ficha.
5. **Medir:** a las 24 h y a los 7 días en `Bases/investigacion/retencion/BITACORA-METRICAS.md`. Cambiar una sola cosa por Reel. Mirar en qué segundo se cae la curva, el tiempo promedio y los compartidos entre vistas. Para probar ganchos, usar los Reels de prueba de Instagram.
6. **Referencias:** dos cuentas de referencia (formato A, divulgación visual; formato B, mujeres de 40 en adelante).

## El estilo de Example Brand: opción C, ilustración plana de noche
- Kit: `KIT-ESTILO-C.md` (paleta, fondo ciruela sin grano (leve y fijo solo en el fondo si hay anillos), sombras en media luna, karaoke con la palabra en ciruela dentro de una píldora mostaza, etiquetas, zonas seguras, movimiento y código base).
- Ejemplo en movimiento: `EJEMPLO-reel.html` (no incluido en este repo). Si un Reel nuevo sale disparejo, agregarlo al prompt como referencia de código. Ojo: trae grano completo (excepción al 18 % inferior); mandan KIT y DECISIONES.
- Cómo se eligió: el Style Atlas de Futurepedia fue solo referencia (material de la marca, no incluido). Un Sonnet hizo 3 bocetos baratos, luego 3 pulidos en tamaño real, y Didier eligió el C. Regla: estilo propio, un solo universo visual, nunca copiar.

## Lo que cuesta y lo que no
- Caro: leer prompts de miles de líneas y ver imágenes. Eso va a Sonnet, que solo regresa un resumen.
- Barato: speech, storyboard y encargos (Opus, poco texto). Comandos de un paso (ffmpeg) los corre Opus directo, sin subagente.
- Corregir en el storyboard o en los cuadros fijos cuesta poco; en la animación terminada, mucho.
