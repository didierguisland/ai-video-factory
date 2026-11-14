# Orchestrator guide: from "I want a video" to the MP4

This is enough to take a video from zero to MP4. The only thing asked of the owner is the voice. Everything else you decide with this guide and the owner's decision notes. On this route the guide overrides the generic video contract and the model-assignment rules wherever they say to stop and ask the owner: that is the owner's open letter of Nov 4. Looking at the contact sheet and the sketch is your job, even though a general rule says the orchestrator does not look at images: it is judgment.

**You do not build, you do not render and you do not read long material.** The commands and `ruta` do the work; you read their summary and decide. One new chat per video or per batch: 53 % of the orchestrator's spend on the first video was re-reading its own context (`cost-analysis.md`). Do not load HTML, base64 images or the analysis files.

(`$HUMANIFY_HOME` is the folder of the route runner, which is not included in this repository.)

Every Bash call is a new shell, and a background one even more so: put this at the start of every command (abbreviated `$H` below).
```
H=$HUMANIFY_HOME/herramientas/humanify.sh;
```

**Team.** Argon and Flash (Google) and Terra (Codex, ChatGPT) are part of the team the owner already authorized for the routes, and earlier routes already ran them. Policy of this route: they run without asking for each delegation. Terra only enters if the speech carries facts. Codex is free for whatever the video asks, above all images (owner, Nov 4): it is used without asking.

**Captures (owner, Nov 4).** Every 2.5 s a capture is taken to show to Argon. That is the only part of Sonnet or the engine in the visual review: you do not look at images, you read what Argon reports.

**Creative process (owner, Nov 4): open, he follows it.** The pilot did not carry the hook he expected. Before another video, read `craft/RECETA-CREATIVA.md` and ask him about hook, story, speech and what is shown: until he closes it, that is not decided alone.

## 0. Is there already a half-finished video?
Always first, also if the owner says "the voice is ready", "where is my video?" or the chat was compacted:
```
$H ruta estado --proyecto <PROJECT>
```
It spends nothing and opens nothing. It says the route, the stage, the phase, the folder and what comes next.
- **`video-fabrica` unfinished:** that is the folder and that is the video. Do not create another one and do not archive. Continue according to the phase: `compuerta` (gate) or `espera` (waiting), `ruta avanzar` reprints the gate or the voice text without spending (if the owner brings the WAV, section 4); `pausada` (paused), section 6; `trabajando` (working) and "keeps running", wait for its output; `trabajando` and "was cut off", `ruta reintentar` continues on what it left.
- **`terminada` (finished) or "no route":** continue with section 1.
- **Another unfinished route (not the factory):** `$H ruta archivar --proyecto <PROJECT> "<why>"`. It does not delete or spend, and leaves its conversation closed. Never archive a half-finished `video-fabrica` without having read it this way: topic, speech and an already recorded voice would be thrown away; only if the owner asks for another one and that one is no longer going ahead.

## 1. Before starting
```
$H ruta preflight --ping
```
Everything must say `ok`. The ping spends one "ok" from Sonnet and tells whether there is quota. If it says NO QUOTA, set up the wait of section 6 (the notice, per its rule). If something is missing that only he can fix, tell him with the exact command.

## 2. Choose the topic and start (without asking him)
If the owner gave a topic, that one. If not, open the campaign's topic bank (`BANCO-TEMAS.md`) and also look at `PROHIBIDOS` and the register in `craft/MUNDOS.md`: **rotation**, from top to bottom, the first live and risk-free one that does not repeat an object, doubt, place or joke from "Already used" or from that register. What is most similar to the previous video is never the next one. With no live topics: a new one of humor and calendar, without figures, noted in the bank. If what was asked does not fit the campaign's Frame: its own folder with its own `BANCO-TEMAS.md` (same sections, without the holidays Frame). Then:
```
/usr/bin/python3 $HUMANIFY_HOME/herramientas/video-nuevo.py $HUMANIFY_HOME/campanas/<campaign> "<short name>" --tema "<topic in one sentence>"
```
It prints the folder (`.../videos/NN-name`). If below it says `AVISO de rotación` (rotation warning), the topic shares something with what is vetoed or used: if it is the same object or the same doubt, delete that freshly made folder and choose another. Open its `00-PAQUETE.md`: it is everything the agents know about the campaign, with the forbidden and used worlds. If the topic needs a fact, confirm that it is in Permitted data; do not add opinions of your own: the room adopts what you tell it. Then:
```
$H ruta iniciar --proyecto <PROJECT> --ruta video-fabrica --carpeta "<folder>" --brief "Tema: <topic>." --hechos '{"duracion_objetivo_s":65,"imagenes_codex":false}'
```
If it says there is already a route in progress, go back to section 0. Only one route runs at a time per project.

**How to run long things.** `ruta avanzar`, `ruta decidir` and `ruta reintentar` can take from seconds to an hour. Always run them in the background, with `caffeinate -i` (`run_in_background: true`), and read their output when they finish:
```
H=$HUMANIFY_HOME/herramientas/humanify.sh; caffeinate -i $H ruta avanzar --proyecto <PROJECT>
```
The animation is the longest and most expensive: launch it with the quota window freshly opened if you can, so that a 429 does not hit it halfway through the pass.

## 3. The gates
Each command ends in one of these outputs. Do not ask the owner anything at any of them: `ruta decidir` is yours to resolve.

| If the output says | Do this |
|---|---|
| `Compuerta «tema»` (topic gate) | Read `01-CONCEPTO.md`. Run the questions below. `decidir aprobar` or `decidir corregir "<what>"`. |
| `Compuerta «speech»` | Read `03-SPEECH.md` in full. Same. It is the last thing that can be corrected before recording. Reviewer: if it says `sin revisión` (no review) or `no contestó` (did not answer), the figure was not reviewed: check every number yourself against Permitted data. |
| `ALERTA de repetición` (repetition alert) | The engine found something forbidden or already used, by words, and already did one pass. If it really repeats: `corregir` (topic) or `--fondo` (sketch). If it is false (the word came up in passing), continue and say why in the note. |
| `faltan voz-original.wav` (voice missing) | The voice: section 4. This is the only thing you ask him for. |
| `Compuerta «voz»` | Read `DIFERENCIAS` (differences). Section 4. |
| `Compuerta «boceto»` (sketch gate) | Read `05b-AJUSTES.md` and what Argon reports about `estilo.png`. Section 5. |
| `Compuerta «final»` | Read what Argon reports about `hoja.png`, the book and the camera. Section 5. On approval the texts come out and it ends. |
| `Compuerta «tope de gasto»` (spend cap) | Normal if it is the first video of an account. `decidir aprobar`, and say so on delivery. |
| `Preguntas sin contestar` (unanswered questions) | `$H ruta nota --proyecto <PROJECT> "<answer or: assume X>"` and then decide. |
| `PAUSADA` (paused) | Section 6. |
| `Ruta terminada` (route finished) | Section 7. |

Commands: `$H ruta decidir --proyecto <PROJECT> aprobar "<note>"` · `corregir "<what>"` · `corregir "<what>" --fondo`. On topic and speech, `corregir` passes the current text to the leader; a text detail you can edit yourself in the file and approve, and the engine announces it as an external change. The brief does not change by itself: if a decision makes it false, `$H ruta brief --proyecto <PROJECT> "<new>"`.

**Topic and speech: the test.** One correction pass, two at most.
- Can it be told in one paragraph saying "first you see..., then..."? Would the woman say "that happens to me" within 3 s, without a fact?
- Hook from real life, with a drawable object, in under 3 s? Health threat or mockery of a body? Out.
- Does it get an accomplice's laugh? At least 3 jokes. Can every sentence be seen?
- Figures only from Permitted data? Without a source, it is removed. Does it sound like a lawyer or a study? It is rewritten.
- Does the last idea answer the hook without promising? Does it close with "follow me" and who to send it to, reusing a joke? Does it have VOZ and SILENCIOS blocks, a 2 to 3.5 s tail?
- `Hechos: palabras_speech` (word count) in the gate output: from 130 to 150. "It has room for more" means that what would be cut is a joke that can be drawn, not explanation: up to about 170, and say so on delivery. Never stretch.
- Does any object, metaphor or joke repeat "Already used" or `PROHIBIDOS`? It is changed even if the engine did not see it.

## 4. The voice: the only stop
The output carries the text marked `PASTE THIS TO THE OWNER AS IS`. Paste it in the chat, with nothing more than this: "Paste this in Google AI Studio, download the WAV and leave it here in the chat. I do the rest".

When the file arrives (even if it has another name or format; it usually arrives as a path into the downloads folder). If he said he already downloaded it and there is no path: look for the newest `.wav` in the downloads folder, and confirm it is less than 10 min old. If it is older, ask for it in one line.
```
cp "<what he sent>" "<folder>/voz-original.wav"
H=$HUMANIFY_HOME/herramientas/humanify.sh; caffeinate -i $H ruta avanzar --proyecto <PROJECT>
```
It prepares the voice without a model (Whisper, silences, clean voice and subtitles, under one minute) and stops at `Compuerta «voz»`, with `DIFERENCIAS: N`. The subtitles already come out with the spelling of the approved speech and the timings of the voice, and "doce" against "12" does not count as a difference.
- **0, or only small changes** (a word, punctuation, a question mark turned into a colon): `decidir aprobar`. The voice may interpret; the timings come from the WAV. If the difference is Whisper's hearing and not the voice, there is nothing to correct: the subtitle already says what the speech says.
- **A sentence was swallowed, a figure was said wrong, or the joke came out changed:** ask the owner for that take again with the text above and a line on what happened. When it arrives, replace `voz-original.wav` and `decidir corregir "new voice"`.
- If it says a silence could not be placed: the sentence does not match. Edit SILENCIOS in `03-SPEECH.md` and `decidir corregir "silence"`.

Up to the sketch it runs by itself: direction by Argon high (ten minutes or more) and grounding by Opus.

## 5. Judging the visuals
**Argon's verdict is not a gate.** It said CHANGE in 4 of 4 reviews and once praised improvements that did not exist. It is asked neutrally and never told what was corrected (the route already does this). You do the triage:

| What it says | It is | Do |
|---|---|---|
| Broken, cut off, overlapping, illegible, covered by the subtitle, at a specific second | Concrete | `decidir corregir "<short list with seconds>"`. Goes to Sonnet, with its sheet in view. |
| Empty, flat, not understood, the idea does not read, lacks life | Fundamental | `decidir corregir "<what>" --fondo`. Goes to Opus. Never to Sonnet: "it meets the list, but does not think like a director". |
| Bothered by the free space at the bottom (it is the safe zone) or the brand mark (mandatory), opines on something that is not in the sheet, judges a half-finished camera travel as if it were a still frame, taste with no consequence | False | `decidir aprobar "<why not>"`. |
| Small detail: something covered for a second, a flag that crosses | Small | If it is cheap, together with the rest; if not, it does not stop the video. |

**Sketch.** Read `05b-AJUSTES.md`: if Opus flagged promise, mockery or repeated world and it was not resolved, correct. Its `POSES` and `HECHOS EN PANTALLA` blocks are what the animation will use: a pose that does not fit or a date that cannot be sustained is fixed here, not at the end. Does frame 1 carry the full hook? Vetoes: generic or plastic 3D; resemblance to the previous world (compare against its row in the `MUNDOS.md` register and `PROHIBIDOS`, not from memory); a protagonist that can be confused. Is every frame understood at phone size? One pass. It is the insurance against spending the animation on a world that was never tested.

**Final.** Argon looks at `hoja.png` (one frame every 2.5 s and one at each second of `TIEMPOS_CLAVE`; they are still frames, the motion is not seen). Look in its report, and if it does not say, ask it:
- Does frame t=0 carry the full hook and no subtitle? Does any label repeat the subtitle? Are the dates and quantities in the image those of `HECHOS EN PANTALLA`?
- Is every joke understood? Nothing that explains after the subtitle? Two consecutive frames that are almost equal? An event is missing there.
- Does it show the brand on all of them, and the right social handles at the end? (`MARCA.json`).
- `CAMARA.md`: `AVISOS` (warnings): fast travel, or a long stretch without voice. The video that was liked: 24 % in motion, travels of 1.8 to 2.6 s. A fast travel is a sure motion sickness: `--fondo`. The short steps the recipe allows are counted separately and are not a warning. `misma toma` (same shot) longer than 10 s: look at those frames in the sheet; if nothing changes every 2 to 4 s, `--fondo` with an event or a short step. If it says it could not be measured, there is no measurement: say so on delivery.
- What would the owner add on seeing it? Five times he added something. If it is obvious, do it now.
- Corrections book: a `FALLA` (FAIL) on figure, health or brand is corrected; the rest is weighed. It works for topic and speech the same.
- Without the brand mark or the social handles the video is not finished.
- At most 2 passes. With more, deliver the best and say in one line what was not achieved: "a video with errors and a list of decisions is worth more than a question that holds it up".
- If the correction says `ALERTA: ... NO se aplicó` (NOT applied): the sheet is the previous one. Ask for it again in other words or `--fondo`. If it was cut off by time (`más de N min`), the HTML may have been left half done: `--fondo` saying to continue on what exists.

Motion and ear are judged only by the owner. You review what is measurable and say so in the delivery.

## 6. Errors
`PAUSADA` carries the real error. The route does not continue by itself: nothing is left going on.
- **Usage limit (429).** The output carries the time and the exact command; with no time, try every 30 min. Run it in the background and continue with your own work. On waking it retries by itself and does not repeat what already came out: if the one that ran out of quota was the reviewer, nothing is rebuilt. Look at who failed in the `PAUSADA` line before blaming an account: Opus or Sonnet spend the terminal's account, not the app's (`$H ruta preflight` tells the plan); Argon and Flash spend Google; Terra, ChatGPT. With a small plan less than one video fits per 5-hour window: this will happen.
- **`más de N min`, partial.** `ruta reintentar`: the agent continues on what it left. If it happens again, split it or cut scope with `ruta nota`, and say so on delivery.
- **`no contestó` or `sin revisión` from a reviewer.** It is not a pause: the route continues and that was not reviewed. If it is about facts, check every figure yourself; or `ruta reintentar` if it marks it paused.
- **`terminó sin entregar` or `sin cambiar`** (finished without delivering / without changing). `ruta reintentar` once. If it repeats, read its message and `ruta nota` with the concrete instruction before retrying.
- **`sin el formato pedido`, `voz_texto falló`.** Edit `03-SPEECH.md` yourself (it is text) and `ruta reintentar`.
- **A script failed** (render, sheet, voice). Read the error. If it is in the HTML, it is fundamental: retry with a `ruta nota` about what failed. Whisper without cache: give the command to the owner, do not install it yourself.
- **A hook blocks something.** It is never worked around. Give the command to the owner and note it.
- If it cannot continue in any way: tell him what happened, with the verified cause and the right account. Only then.

**The only notification rule.** Notify the owner only for: the voice; the finished video; a block that only he can resolve; a new expense (a paid service); or that the video only works with a health promise or a figure that cannot be sustained and there is no other angle. Never for topic, hook, style, color, camera, model, a 60 to 90 s duration or "do I approve?". After the voice, silence, unless a 429 or an error moves the delivery more than 30 min from normal: then one line, "continues at HH:MM", with the right account. Silence irritates him when he is waiting, and that line covers it. The pending questions of the overview are not reminded in this flow; they are said once, on delivery.

## 7. Delivery
When it says `Ruta terminada`:
```
$H ruta retro --proyecto <PROJECT>
```
Send him, in a single message:
1. The MP4: the light copy `<folder>/reel-redes.mp4` (under 28 MB; the heavy one is `reel.mp4`). If the gate said the copy did not come out, send the heavy one and say so.
2. The content of `TEXTOS-PUBLICACION.md`, ready to copy.
3. "I decided for you", three to five lines about what he sees, not about agents: "first you see..., the joke is..., I closed it with...". And what I could not judge (motion and ear). If he has not seen them yet, one line: "check that your social handles on the card are the right ones".

**Language.** What he will see, never what happened in the engine: an earlier delivery was not understood because the concept was told in agent language. No stage or model names, unless he asks. Short paragraphs.

After that: in `BANCO-TEMAS.md` move the topic to "Already used" with its joke (also if it is not yet published: the world is already in the register); note his first reaction to the MP4 in `craft/LIBRO-CORRECCIONES.md`, in the form of a rule, and in the decision notes if he reconfirms or contradicts something (raise x1 to x2). If he vetoes an object or material, it goes to `PROHIBIDOS` in `craft/MUNDOS.md` and in `ENCARGO-DIRECCION.md`. If he gives figures on how it went, to the bank. Close with the closing cycle of the project's instructions.

**Next video:** section 2 again. For a batch, continue in this chat if the context is low; if it was already compacted, "it is a good time to open a new chat" and leave the handoff.

## Optional, off
Image cut-outs by Codex: `--con imagenes` on `ruta iniciar`, with `"imagenes_codex":true` in the facts. Authorized by the owner (Nov 4): turn it on when the video asks for it; otherwise, geometry in code.
