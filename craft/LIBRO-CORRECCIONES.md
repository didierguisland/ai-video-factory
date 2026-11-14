# Libro de correcciones: lo que Didier ya corrigió
Libro único desde el 9-nov-2026: fusiona dos libros anteriores (uno del motor y uno de la marca de ejemplo, que repetía casi todo). Vale para cualquier marca; lo propio de una marca vive en su `MARCA.md`. Aquí se anotan las correcciones nuevas. El motor lo lee por nombre: no renombrarlo.
Cómo lo usa el revisor: abre el libro, toma solo los temas que aplican al paso y revisa regla por regla con el material a la vista.
Entrega una lista PASA/FALLA, con la línea exacta que falla y la regla citada (tema y texto). No corrige, reporta.
Todo esto es regla, salvo la sección final "Referencias de diseño", que se escoge según el proyecto (ver LEEME, "Reglas y referencias"). El revisor no marca FALLA por una referencia.
(xN) = se repitió N veces. Si dos reglas chocan, manda la más reciente; en `video-fabrica`, además, decide quien tenga la compuerta.

## Cómo hablarle a Didier
- Platicar, no interrogar: párrafos, una pregunta a la vez, sin listas largas ni 7 preguntas (x3, APRENDIZAJES.md:17, CLAUDE.md).
- El plan es un foro flexible de "¿qué hacemos hoy?", no uno militar; textos al equipo cortos pero con el porqué (APRENDIZAJES.md:19-20).
- Lo que Didier deba pegar en otra app va pegado en el chat, listo para copiar, no solo en archivo (APRENDIZAJES.md:201).

## Palabras y tono
- Palabras que entienda cualquier señora; nada de "colado", "chalán" ni "kólla" (suena a albur) (x3, APRENDIZAJES.md:73,114, ELEGIR-TEMA.md:19).
- Gancho y datos de lo cotidiano: "¿Le pones limón a todo?", "3 de cada 10" (APRENDIZAJES.md:96,114).
- Nada traducido al inglés sin avisar; el guion en español (APRENDIZAJES-VIDEO.md:13).
- En el tono de AI Studio, nada de "faster"; en tema serio valen más esos segundos (DECISIONES 11).
- Etiquetas de voz `Nombre:` al inicio de línea, máximo 2 voces en AI Studio (DECISIONES 10).

## Speech y retención
- Un número o una frase de ritmo necesita su marco antes: decir primero qué se califica y en qué escala; cada bloque nombra la cosa, cuenta qué pasó y luego da el número. Nada de muletillas sin objeto («Yo ya me lo puse»: ¿qué?) (Didier, 11-nov).
- El gancho trae tensión en el segundo 0: prohibición + confesión + promesa (Didier, 11-nov).
- En un video corto, lo guardable y la regla útil van al final, justo antes del «mándaselo»; a la mitad suena a que el video ya acabó y luego sigue soltando datos (Didier, 10-nov, postre; Muse lo quería a la mitad).
- La duda de la señora, escrita (y dicha, si hay voz) en el cuadro 1, también en "una amiga me preguntó" (x3, RECETA-REEL.md:50, DECISIONES 4).
- (solo serie Example Brand; no aplica en `video-fabrica`) Portada o sello de serie después del segundo 3, o como marco desde el cuadro 1; la portada perdió al 85-90 % en 3 s (DECISIONES 4).
- Algo nuevo cada 2 a 4 s; en la tabla de 2 s ningún tramo vacío sin marcar (RECETA-REEL.md, capa de retención).
- El último cuadro responde el primero; un gancho que no se cumple es traición (RECETA-REEL.md, pay de manzana).
- (solo serie Example Brand; no aplica en `video-fabrica`) Cierre con "mándaselo a tu comadre que…" y puente a la siguiente edición o al producto (RECETA-REEL.md).
- Meta de 60 a 70 s (130 a 150 palabras); hasta 90 si la idea da, sin estirar (Didier, 4-nov: «1 minuto, 1:20, 1:30»; 66 s le gustó). Antes decía 45 s y tope de 75. **En revisión (9-nov):** el playbook de Muse, con datos de la cuenta, recomienda 20 a 35 s; lo decide Didier (`Bases/ESTADO.md`). Mientras, vale esta regla.
- Voz: máximo unas 3 palabras por segundo; si se come sílabas es falta de tiempo: dar tiempo en el SRT y escribir la palabra en sílabas en la descripción ("di-fun-tos") (APRENDIZAJES-VIDEO de Example Brand).
- Cada metáfora conserva la causa: el flotador sí, el timbre no (ARQUITECTURA-BARATA.md:45).
- No conectar el contenido de un Reel con otro ("Amiga con limón"); el puente del cierre es solo a la siguiente edición de la misma serie o al producto .
- Un respiro de al menos 1.2 s por momento (x2, ENCABEZADO-PROMPT.md:18, REPORTE-sol de la sed).

## Visual y zonas
- Piso de calidad de los animados de Example Brand: mundo 3D (Three.js local) con escenas, movimientos de cámara (dolly, paneo, tilt, viajes que llegan y se detienen), luces que cambian por escena y ritmo; el 2D va como capa encima (caras, gags, letreros). Antes de los frames, Argon dirige cada toma (lente, luz, composición, entrada y salida de cámara), como en `2026-11-12-siguiente/argon-tomas.md`. Nunca bajar a 2D plano por prisa (Didier, 13-nov: «¿por qué no hay ritmo 3D, movimientos de cámara, luces, escenas?»).
- Cámara que se entienda: se mueve, llega, se detiene y deja leer antes del siguiente movimiento; "algo nuevo cada 2 a 4 s" no es cámara sin parar. Si marea o no se entiende, va muy rápida (Didier, 3-nov, drafts de la primera campaña).
- Un solo universo visual por video; nunca mezclar 5 estilos ni copiar el Atlas (x3, APRENDIZAJES.md:72, RECETA-REEL.md:60, DECISIONES 13).
- Zonas: texto con y >= 10 %, ilustración >= 7 %, nada en el 18 % de abajo (x3, APRENDIZAJES.md:125, DECISIONES 5).
- Sin grano de película (textura de material sí); si hay anillos, un grano leve y fijo solo en el fondo (APRENDIZAJES.md:108, DECISIONES 6).
- Medir cada texto con `measureText` en la fuente real de la Mac (x2, CORRECCIONES-1.md).
- Textos ★ literales; un espacio antes de la palabra con asterisco; logo a color completo (x2, AJUSTES-cuadros-v1.md).
- Objetos que se reconocen al instante (naranja, cremas) en su color real (ENCABEZADO-PROMPT.md).
- DURATION del prompt = la del WAV completo, no la de la última palabra (se cortó la risa) (RECETA-REEL.md:55).
- Los cuadros se revisan antes de animar y de renderizar. En la fábrica los aprueban Argon y el orquestador; Didier ve el MP4 (carta abierta, 4-nov; antes los aprobaba él).
- Marca «Example Brand» visible todo el video y tarjeta de redes desde «sígueme»; valores en `MARCA.json` (Didier, 4-nov: «en ningún lado dice la marca»).
- Sin voz y sin evento, máximo unos 3.5 s (Didier, 4-nov: «ahí se pierde mucho tiempo»).
- Cada frase tiene algo que se ve; dos cuadros seguidos casi iguales en la hoja son un tramo flojo (Didier, 4-nov).
- Un congelado que no se marca como efecto (sin zoom, sonido ni texto) se ve como falla; al quitar silencios, revisar que los congelados sigan cayendo donde se leen (Didier, 11-nov).
- Vista previa en HTML: el video manda el reloj y la voz lo sigue; si la página corrige el video, este se regresa y parece que se traba (11-nov).
- Muse revisa con la hoja de cuadros MÁS el guion con tiempos; sin tiempos propone cortes que mutilan la voz grabada (11-nov).
- Subtítulos y stickers revisados sobre los cuadros reales, no en papel: tapaban el producto y uno decía "Lo" cuando ella decía "los" (APRENDIZAJES-VIDEO de Example Brand).

- Una sola capa de texto: karaoke de la voz, palabra por palabra con el timing (la que suena resaltada); nada de titulares aparte que repitan la voz ni notitas encima. Los rótulos que son parte del dibujo (claqueta, placa) no cuentan (Didier, 11-nov, cafecito).

## Omni e IA
- Omni no congela ni hace efectos de edición: pedir la acción completa, con trayectoria, y congelar en edición. Nunca «está a punto de». La expresión cambia de A a B, la cámara lleva lente y movimiento, y algo se mueve en cuadro (gota, mechón). Cocina realista con luz de ventana = oscura y sin foco; un set liso claro con una sola acción engancha más (x2, reel de producto, 11-nov, Argon y Muse).
- Cada remedio o momento arranca limpio: no se encadena desde el último cuadro si arrastra el estado anterior (reel de producto, 11-nov).
- Recortes 2D tipo sticker junto a video realista se ven baratos; el producto real nunca se genera con IA si se puede usar su foto real (x2, reel de producto, 11-nov).
- Un brinco de continuidad de Omni (algo aparece de golpe) se tapa con un corte: acercamiento de golpe al lado que sí se ve justo antes del brinco y regreso al plano abierto después; con dos cortes se lee como paso del tiempo (reel de producto, 11-nov).
- Omni untando algo en el pelo (mano que embarra) se ve falso en movimiento: en edición se corta del gesto previo (cuchara saliendo del frasco) al resultado ya puesto, sin mostrar el contacto (Didier, 11-nov).
- Nada de cámara lenta notoria: una toma alentada a 0.75× en el cierre baja el ritmo; máximo 0.85× (Didier, 11-nov).
- Si se acaba la toma, no se estira con ida y vuelta (boomerang) ni congelados largos: se pide otra toma a Omni (Didier, 11-nov: «cero me gustaron»).
- Tomas de 10, 8 o 4 s; nada de estirar a 10.6; el menor número de tomas (APRENDIZAJES.md:201, DECISIONES 12).
- Mismo bloque STYLE, VOICES y CHARACTERS palabra por palabra en cada toma (APRENDIZAJES.md:201, DECISIONES 12).
- Letras, números y logos nunca generados por IA: van en la capa (x2, APRENDIZAJES.md:200).
- Imágenes de IA: "no parecido a nadie famoso" (el científico salió Einstein) (APRENDIZAJES.md:116).
- No inventar precios, colonias ni apps; lo que falte se marca `[POR CONFIRMAR]` (edicion/PROMPT-EDICION.md).
- Las imágenes se suben a la app junto con el prompt, no aparte (video con persona real).
- Prompt de Omni en este orden: REFERENCIAS (opcional) · STYLE · LUZ · ESCENARIO · PERSONAJES descritos completos aunque haya referencia · VOCES · TIEMPOS DE VOZ en SRT · CÁMARA por segundos · ACCIÓN por segundos · SONIDO sin música · AVOID. Personajes con hoja de 6 ángulos; orden: historia → personajes → hojas → tomas (APRENDIZAJES-VIDEO de Example Brand).
- Bloqueo "incumple políticas" en imágenes: sale con mujeres descritas con palabras de cuerpo o tela ("huggable", "full body", "lace", "satin") o polvo blanco en la boca. Probar quitando una cosa a la vez (APRENDIZAJES-VIDEO de Example Brand).
- Voz decidida en la ficha: en cuadro = la de Omni; narrador fuera de cuadro = AI Studio (DECISIONES 2).
- Prompts de video de IA, paso a paso y con física (Didier, 12-nov, «6:02 am»): cada movimiento se describe con su dirección y su cantidad (la ventanilla baja de arriba abajo en X s; baja N escalones, siempre hacia abajo, alejándose de la cámara), cómo reacciona lo que se mueve (el viento entra por la izquierda y lanza los mechones hacia la derecha, rápido y natural, y se quedan despeinados), la geometría del lugar (hacia dónde va la escalera, de qué lado está el barandal) y la cámara (desde dónde arranca, a qué distancia sigue y a qué altura). Si queda ambiguo, la IA inventa: la escalera subía y bajaba y el vidrio se veía raro.
- Más de lo mismo (12-nov, toma del coche): decir hacia dónde mira y que la cabeza no gira (si no, voltea y se le ve la cara); que la ropa reciba luz para que se vea su color (en la sombra, la blusa vino salió negra); que lo que se mueve ya venga en movimiento desde el cuadro 0 (si no, el coche «arranca de la nada»); no dibujar vidrios si se pueden evitar (ventanilla abierta desde el inicio); no poner la cámara donde un objeto real taparía al personaje (la IA quita el objeto: desapareció la cabecera).
- Con personaje de referencia (12-nov): decir que de la referencia se toman solo cuerpo, piel y cabello, y nombrar la ropa de la toma («en la referencia trae camisa negra; aquí, blusa vino»), también en AVOID. Si no, copia la ropa de la referencia.
- Sin exagerar en el prompt (12-nov, retrovisor): «nido», «halo», «puro cabello», «decenas de pelitos» y repetirlo sacaron una caricatura (un copete que se salía del espejo). Pedir el efecto en grado realista («despeinado como después de manejar con la ventana abierta») y que respete la física (nada sale del marco de un espejo).
- El producto se describe mirando la foto real, no de memoria (12-nov): escribí «tapa con gotero de vidrio» y el frasco real no lo tiene a la vista (tapa plateada cilíndrica con botón plano); la IA le puso un bulbo de vidrio. El texto manda más que la imagen de referencia.

- **Cara en plano cerrado (13-nov, toma F del 6:02):** en plano abierto de cuerpo entero la IA dibuja mal la cara (sale deforme). Si la cara importa, plano medio corto, del pecho a la cabeza. Y no pedir viento para lucir el pelo: lo despeina o le tapa la cara. El pelo se luce con un giro de cabeza a contraluz.

- **Tamaño del producto con un objeto conocido (13-nov, toma G):** «diez centímetros de alto» no basta: la IA lo hizo grueso como un termo. Dar alto Y grosor, y compararlo con algo de todos los días (el frasco es del tamaño de un plumón de pizarrón). Y el guiño se pide temprano, con la orden de que después los dos ojos se queden abiertos.

## Salud y producto
- Nada de promesas de salud ni de ligar un síntoma con el producto (x4, CLAUDE.md, ENCABEZADO-PROMPT.md:15, ELEGIR-TEMA.md:22, RECETA-REEL.md:29).
- Un "puede" nunca se vuelve certeza; los datos pasan por Terra (en `video-fabrica`, después de escribir el speech; no aplica como falla antes) (APRENDIZAJES.md, sed).
- Documento: fidelidad total, no inventar ni perder; "son 4 pasos"; si se contradice, se le pregunta al dueño (MATRIZ-FIDELIDAD.md:18,24).
- Frases filtradas contra la lista de prohibidas de Terra, sobre todo lo que sale de Gemini (RECETA-REEL.md:21).
- Si el cierre pide un mensaje o una palabra, debe prometer una respuesta concreta y útil (uso, precio, rutina), no solo pedir contacto (x3, HUMANIFY-CANDIDATOS de Example Brand).

## Proceso y modelos
- Orden después de la voz: SRT (Sonnet medium) → se le lleva a Didier → storyboard conceptual de Opus platicado con Argon sobre el SRT → Muse lo revisa → frames fijos → animación. Nada de saltar a cuadros ni a constructores antes, y un paso a la vez (Didier, 13-nov: «a ver, calma»).
- Para idear un video nuevo: primero se le pregunta a Muse, en pocas viñetas, qué temas están en tendencia; de ahí sale la lluvia de ideas. Nunca llegar con una idea armada desde la fila vieja o solo desde las métricas (Didier, 13-nov: «esta horrible tu propuesta»).
- Usar todos los modelos, cada uno en lo suyo; si alguno se queda fuera, decirlo, salvo en `video-fabrica`, donde el reparto es fijo (x2, ARQUITECTURA-BARATA.md:48, APRENDIZAJES.md:190,198).
- Decidir el tipo de producción y la voz el día 1, en la ficha; en `video-fabrica` ya está fijo (APRENDIZAJES.md:205, RELEVO-10.md:7).
- Argon y Flash en medium, salvo lo que diga el elenco de la ruta; Terra con `--search`; la ruta de `-o` siempre absoluta (DECISIONES 8).
- Argon y Flash llevan "no uses herramientas" o salen vacíos (RECETA-REEL.md:21).
- Whisper local primero; la app de Claude solo como plan B (DECISIONES 9).
- Construye un Opus aparte (el constructor, o un chat de la app), nunca el orquestador; el render lo corre el motor; un ffmpeg de un paso lo corre el orquestador directo (ANALISIS-clases-motion.md:18, RECETA-REEL.md:63, RELEVO-10).
- Antes de delegar a Codex o agy, decirle a Didier en una línea qué se manda (CLAUDE.md). En `video-fabrica` no se pregunta por delegación: Argon, Flash y Terra corren porque son del equipo que Didier ya autorizó en las rutas (política en `fabrica/GUIA-ORQUESTADOR.md`). Las imágenes por Codex siguen apagadas salvo su sí.
- Un bloqueo del hook de terceros nunca se rodea; se le da el comando a Didier (CLAUDE.md global).

## Publicar
- Textos de Instagram y TikTok en `TEXTOS-PUBLICACION.md` antes de dar por listo (APRENDIZAJES.md:136).
- Programar 30-45 min antes de la hora. Separación entre videos de la misma cuenta y horarios: los de la marca (`MARCA.md`); la marca de ejemplo, con los datos de Muse, pide 8 h si hay dos el mismo día (antes 3-4 h).
- Medir a las 48 h (y a los 7 días si se puede) en el `REGISTRO-reels.md` de la marca; cambiar una sola cosa por Reel (RECETA-REEL.md, retención; Muse, 9-nov). La vieja `BITACORA-METRICAS.md` quedó en la carpeta de datos de la marca.
- Anotar el % de uso por video en ARQUITECTURA-BARATA.md (ARQUITECTURA-BARATA.md:50).

## Lo que dicen los datos (Muse, 9-nov; por validar, el revisor no marca FALLA)
Salen de 7 reels de Example Brand. Se vuelven regla cuando el `REGISTRO` los confirme con más videos.
- El arranque decide: lo que se pierde se pierde en los primeros 3 s. Si el salto (skip rate) pasa de 55 %, se reescribe solo el gancho; si baja de 35 %, se repite esa estructura de gancho.
- Una sola idea por video y el dato prometido al final (open loop); el cierre conecta con el inicio para que se repita.
- Si los guardados están en 0, falta algo guardable (lista, receta, pasos). Si hay vistas pero no seguidores, falta pedir que la sigan.
- Contestar comentarios en las primeras 2 h; si no se puede, se está publicando de más.

## Ya lo garantiza el motor (el revisor no lo recibe)
- El speech lo escribe Opus, nunca Sonnet: el de Sonnet salió plano (x2, ARQUITECTURA-BARATA.md:6, APRENDIZAJES.md:189).
- Boceto de cuadros clave revisado antes de animar: etapa fija de `video-fabrica`. Lo aprueban Argon y el orquestador (cambio del 4-nov; x6 antes con Didier).
- Narradora con voz limpia y sonido de Opus: receta y elenco fijos (Didier, 4-nov).
- Contar palabras con el comando, no a ojo: Sonnet cuenta mal (ARQUITECTURA-BARATA.md).

## Referencias de diseño (no son reglas; se escogen según el proyecto)
Lo que ya probamos y salió bien. Se usa como punto de partida, no como obligación.
- Estilo C (noche plana) para la animación de Example Brand; otros proyectos llevan el suyo. Un video de IA en plastilina se vistió con el mundo del propio video (DECISIONES 13).
- Cómo se ve el sello "Example Brand": en un proyecto fue de plastilina, temblando; en otro, fijo arriba y sobrio. Que esté es regla (Visual y zonas).
- Cierre que invita sin vender: lo último de Didier es «sígueme y mándaselo a tu amiga» (4-nov, x1), y es lo que se usa. Antes: pregunta más palabra por mensaje («Escríbeme PAN»).
- Movimiento escalonado a 12 fps, "boil" y entradas por aplastón: para lo animado o de plastilina; en lo premium, movimientos suaves y quietos.
- Cómo se ven los subtítulos (karaoke con píldora mostaza del estilo C, tira de papel amate en un proyecto, serif crema en otro): según el estilo. Que haya subtítulos sí se cuida (ver PROPUESTAS del proyecto).
- Efectos de sonido sintetizados (otro proyecto): cuando sumen, no siempre.

