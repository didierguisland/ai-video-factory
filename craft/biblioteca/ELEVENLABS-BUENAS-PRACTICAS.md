# ElevenLabs: buenas prácticas para la voz (referencia)

Resumen en español de la guía oficial "Best practices" de ElevenLabs que pasó Didier el 10-nov-2026.
Es referencia (N2, "por validar"): lo que diga aquí se confirma probando con nuestra voz antes de volverlo regla.
Sirve de base para la guía de voces cuando la hagamos. Cuando algo se compruebe en un video, se anota en `LIBRO-CORRECCIONES.md` o en `VOZ-NARRADORA.md`.

## Qué modelo
- **Eleven v4 (`eleven_v4`)** es el recomendado: mejor que v3 en casi todo, sigue mejor las etiquetas y acepta clones profesionales (PVC). v3 no está optimizado para PVC.
- Multilingual v2 lee números y fechas de forma más humana que los modelos chicos (Flash). Flash es para baja latencia, no para nosotros.

## Pausas
- **v4 y v3 NO aceptan `<break time="1.5s" />`.** Las pausas se hacen con puntuación y etiquetas: puntos suspensivos (…), guiones (— o -), punto y aparte, o `[short pause]` / `[long pause]`.
- `<break>` solo sirve en modelos v2, hasta 3 s, y muchos en una misma generación la vuelven inestable (acelera, mete ruidos).

## Etiquetas de audio (v4)
Van entre corchetes, justo antes (o después) del trozo que modifican.
- **Emoción y entrega:** `[excited]`, `[curious]`, `[sarcastic]`, `[thoughtful]`, `[surprised]`, `[happy]`, `[sad]`, `[annoyed]`, `[mischievously]`, `[whispers]`, `[shouting]`.
- **No verbales:** `[laughs]`, `[chuckles]`, `[giggles]`, `[sighs]`, `[exhales]`, `[inhales deeply]`, `[clears throat]`, `[gulps]`.
- **Descriptivas (más precisas):** `[low, gravelly voice]`, `[warm, conversational tone, faint amusement]`, `[quietly, with controlled fear]`. Mejor describir la cualidad de voz que algo que suene a efecto, porque v4 también genera efectos y puede confundir una etiqueta con un sonido.
- **Experimentales:** `[strong X accent]`, `[sings]`. Menos consistentes; probar antes.
- **Evitar:** etiquetas que no son de voz (`[music]`, `[standing]`, `[grinning]`, `[pacing]`).
- La voz importa: lo que ya está en su entrenamiento sale mejor. Una voz tranquila no grita bien y una acelerada no susurra bien. v4 lo intenta igual, pero hay que probar.
- Se pueden combinar varias etiquetas.

## Puntuación (pesa mucho en v4)
- **Puntos suspensivos:** pausa y peso.
- **MAYÚSCULAS:** énfasis en esa palabra.
- Puntuación normal: ritmo natural. Signos de interrogación y exclamación cambian la entonación.
- La estructura del texto manda: frases como se hablan, contexto emocional claro.

## Emoción sin etiquetas
- Contexto narrativo ("dijo, con la voz temblando") también guía, pero el modelo **lee en voz alta** esa acotación; habría que cortarla en edición. Con v4 conviene más la etiqueta.

## Velocidad
- Ajuste **speed** en la configuración de la voz: 1.0 normal, mínimo 0.7, máximo 1.2. Los extremos bajan la calidad.
- El ritmo base depende de las muestras con que se creó la voz: para clonar, muestras largas y continuas.
- Para nosotros sigue valiendo el tope de unas 3 palabras por segundo (`LIBRO-CORRECCIONES.md`).

## Pronunciación
- **v4 entiende IPA entre diagonales** dentro del texto: `"/kolaˈxeno/"`. Con acentos de fuerza (ˈ primaria, ˌ secundaria). Solo en las palabras que lo necesiten, y probar con la voz elegida: puede variar.
- Sin IPA: escribir la palabra como suena, con guiones o mayúsculas en la sílaba fuerte ("di-fun-tos", "coláGEno").
- **Diccionarios de pronunciación** (Studio y API, archivo `.pls` o `.txt`): pares palabra → cómo decirla, con fonema o con alias (`UN` → "United Nations"). Distingue mayúsculas y usa la primera coincidencia. Útil para nombres de marca y productos que se repiten en todos los videos.
- Etiquetas `<phoneme>` solo en modelos v2 (Flash v2), palabra por palabra.

## Normalizar el texto antes de mandarlo
Escribir con letra lo que el modelo puede leer mal:
- Números y dinero: "$1,500" → "mil quinientos pesos"; "2do" → "segundo"; "3.5" → "tres punto cinco".
- Porcentajes y unidades: "100%" → "cien por ciento"; "5 kg" → "cinco kilos".
- Fechas y horas: "14/11" → "catorce de noviembre"; "14:30" → "dos y media de la tarde".
- Abreviaturas desarrolladas: "Dra." → "doctora".
- Teléfonos, direcciones y sitios web, con letra y por partes.

## Botón "Enhance"
En la web, Enhance usa un modelo de lenguaje para agregar etiquetas sin cambiar las palabras. Sus reglas sirven de molde si las ponemos nosotros: no tocar el texto, solo agregar etiquetas de voz que encajen con la emoción, variar las emociones, poner énfasis con mayúsculas, signos o puntos suspensivos, y nada de música ni efectos.

## Cómo trabajar
- Generar por partes y unirlas en edición cuando haga falta precisión.
- Si una palabra sale mal, probar otra ortografía antes que otra voz.
- Generar dos o tres veces lo importante y quedarse con la mejor.
- Iterar cambiando etiquetas, puntuación o acotaciones, una cosa a la vez.

## Voice Design (crear una voz desde un prompt; guía oficial que pasó Didier el 10-nov)
- **Formato recomendado:** `Native <idioma y variante>. <Género>, <edad>. <Calidad>. Persona: <2–5 palabras>. Emotion: <2–3 adjetivos>.` y luego 1–2 frases de timbre, ritmo y entrega.
- **El idioma y la variante van en la primera frase**, explícitos, para que no se vaya a otro dialecto.
- **"Accent" solo para dialecto.** Si se quiere decir entonación o énfasis, describirlo así; la palabra "accent" puede mover el dialecto.
- **Nada de palabras de efecto** (reverb, echo, phone, tape): bajan la calidad.
- **Calidad:** "Very good / Excellent / Studio quality" ayudan a la limpieza, pero en voces muy específicas pueden bajar la precisión del prompt.
- **Timbre ≠ emoción:** timbre es lo físico (grave, cálida, rasposa, con aire); la emoción y la actitud van aparte.
- **Texto de prueba (preview):** actúa como guion y moldea la voz. Debe ir con la personalidad del prompt (si choca, sale raro). Mejor largo, un párrafo; acepta etiquetas como `[laughs]`.
- **Guidance scale:** alto = más fiel al prompt pero puede ensuciar el audio si el prompt es raro; bajo = más natural y libre. Los ejemplos oficiales andan entre 20% y 40%.
- Cada generación da 3 opciones y cobra solo los caracteres del texto de prueba una vez; guardar una ocupa un espacio de voz.
- **Ojo:** las voces de Voice Design funcionan en v4 y v3, pero en v4 "pueden ser menos actuadas". Probar las dos con el mismo texto.
- Es experimental: un clon profesional (PVC) es lo más consistente.
