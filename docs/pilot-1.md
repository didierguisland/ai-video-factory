# Factory pilot 1: log (Nov 4, 2026, early morning)

Pilot run by an Opus subagent playing by hand the role of the engine and of the Claude agents. Without `ruta avanzar/decidir`, without `claude -p`. Real Argon through its wrapper script. Flash and Terra were played by the subagent (noted at each stage). Voice is a TEST voice from the system, not from AI Studio.

Format: stage · gap · what would fix it.

## Times
| Stage | Start | End | Notes |
|---|---|---|---|
| Topic | 02:41 | 02:43 | Argon medium, 2 turns of 15 to 20 s |
| Speech | 02:43 | 02:44 | Argon medium, 13 s |
| Voice (text, say, prepare) | 02:44 | 02:45 | Whisper 18 s |
| Direction | 02:45 | 03:01 | Argon high, 956 s, 83 thousand in and 54 thousand out |
| Grounding | 03:01 | 03:04 | By hand |
| Sketch and animation | 03:04 | 06:32 | Written together. **Includes a long pause for the agent's quota, about 3 h:** the real work was in the order of 20 to 30 min, not well measured |
| Sound | 06:34 | 06:36 | `ruidos.py` runs in 4 s |
| Render and 2 passes | 06:36 | 06:44 | Render 48 to 50 s, Argon high reviewing 60 to 80 s |
| Texts, world, closing | 06:44 | 06:46 | |

## Findings

### Before starting
- **preflight.** `ruta preflight` without `--ping` gives all ok. `--ping` was not run (it spends Sonnet). It says "whisper in cache: ok", but in the shell used `uv` is not on the PATH (see voz-preparar).
- **ruta iniciar did not run.** `ruta estado` says there is a finished "video-mundo-3d" route in the project, not archived. To start it would have to be archived; the guide does cover it. It was not done because this test does not run the engine, and a half route state was not wanted. **Consequence:** the facts were computed by hand (`palabras_max_speech` = 65 x 2.3 = 149).
- **Topic: the bank's rule clashes with the bank's note.** "Take the first one with a verified fact or one that does not need it" points to #1 (clothes that feel tight), but its own note says it is the closest to video 1 (a dress) and the owner's decision notes say "repeats table, object or topic -> change it". #4 was chosen (the Guadalupe-Reyes holiday stretch, Dec 12 to Jan 6, as a marathon): it does not ask for kilos and matches the campaign idea ("between one stop and the next"). #3 has the joke "rolling all the way to Reyes" already used. #2 repeats the study of video 1. **Fix:** one line in the bank: "first one that does not repeat an object or a joke from 'Already used'".
- **Derived fact.** From Dec 12 to Jan 6 is 26 days, but "a derived fact does not enter" and the package only allows the dates. Is counting calendar days derived? It was decided not to say "26" aloud: only the dates. **Fix:** clarify in Permitted data whether counting calendar days is allowed.
- **`video-nuevo.py` and the name.** The folder ended up as `videos/01-pilot-...` although the first video of the campaign lives in another folder as `01-...`: two "01". Minor, but `MUNDOS.md` also numbers. **Fix:** make it count that other folder too, or start at 02.

### Topic (2 min, real Argon medium; Flash and Opus by hand)
- **Flash did not run:** its 5 phrases and 3 gags were written by the subagent. The recipe says the best joke came from Flash; here that contribution was not tested.
- **Argon opened with weak angles on the cause** (car and battery, a rubber band that "ends up giving", 26 derived days). Opus's filter was needed. **The best hook did not come out of the 3 angles**, it came out of the topic itself: `abre` asks for a "doubt with an object" and Argon went off into side jokes. Fine with the gate.
- **The closing does not respect what was already used:** Argon put in "the Kings' Day ring bread" (already used in video 1) and "next to the narrator", and "most of the little squares", which is not measured. Corrected with a note in `01-CONCEPTO.md`. **Fix:** have `cierra` repeat "do not repeat objects from Already used".
- **Ambiguity:** does `decidir corregir` on topic re-run the whole `cierra`? The guide does not say whether the orchestrator may edit `01-CONCEPTO.md`. For `03-SPEECH.md` it does say (it is text). A note was added at the end.

### Speech (1 min, real Argon medium; Flash and Terra by hand)
- **Word cap is very hard on jokes:** the first draft had 192; getting to 149 removed two jokes. The guide allows "unless the idea has room for more", with no criterion. It stayed at 149 because the request was normal duration.
- **The counter is not the same:** `wc -w` and the engine count differently with hyphenated names. Irrelevant, but the voice report says 151 and the text 149.
- **Argon did contribute:** the silence before "They are called Tuesdays". Its complaint about the card was rejected (solved with stamps over the calendar, without a card).
- **Terra by hand:** there are only two dates; PASS. The `revisor_si` regex fires because of the "12" even if it is a date from the Frame. It would spend 190 thousand tokens of Terra to review two dates. **Fix:** make the regex not count verified dates from the Frame.

### Voice (1 min)
- **`voz-preparar.py texto`** came out on the first try, with voice, description and text. Good.
- **`voz-preparar.py preparar .` fails with a relative path:** it runs Whisper with `cwd=tempdir`, and `timing-original/_guia.txt` is not found. The error suggests a missing cache, and that is not it. The engine passes an absolute path, so it does not affect the route. **Fix:** `Path(carpeta).resolve()` in `preparar`.
- **`voz-prueba.py` is no good for this step:** it writes `voz.wav` and `voz.srt`, not `voz-original.wav`, and spreads silences between sentences. The macOS `say` command was used directly (`-v Paulina -r 178`). It is a **TEST VOICE**, 54.9 s original and 58.56 s with the silence.
- **`uv` is not on the PATH** of the pilot's shell: it falls back to `python3 -m uv` and works. Preflight does not distinguish it. No problem.
- **Dirty Whisper subtitles (REAL GAP):** `voz.srt` carries invented quotation marks, a space before the "?", split mid-sentence and joining two sentences. "¡No!" loses its marks and joins "a cada quien". The report does not warn (DIFERENCIAS: 3 only because of `doce/12`) and **no stage reviews the SRT**; `sonido` forbids touching it and `animacion` says to use it. **Fix:** align the SRT against the SPEECH block (speech text, Whisper timings) instead of using Whisper's text.
- **False DIFERENCIAS:** `doce` against `12` and `seis` against `6` count as a difference; the guide says 0 or small changes are approved. With a real voice it will be the same. **Fix:** normalize numbers into words before comparing.

### Direction and grounding (Argon high 16 min, 54 thousand output tokens; grounding by hand)
- **Argon high did deliver** a buildable 435-line document with a new world (steel board and wooden tokens), a valid MUNDO block and 8 moments. It gives the tennis shoe personality without being asked. It is the agent that is worth the most in the chain.
- **Argon invented the calendar (FACTS GAP):** it wrote "Friday Dec 12... Tuesday Jan 6, Tuesday 16, 23, 30 and 6". Real: Saturday 12, Wednesday 6, Tuesday 15, 22, 29 and 5. If a calendar appears on screen, nobody verifies it: **the grounding list does not include "world facts"** (dates, days, units) and `revisor_si` only looks at the speech. **Fix:** add HECHOS EN PANTALLA to the grounding list, and put in the package the weekdays of the Frame's dates.
- **Impossible camera coordinates:** its Pose 3 sees 3.8 wide and the grid measures 6.7; it declares that it fits in 110..970 px. The recipe warns, but Argon makes many false calculations with great confidence. The grounding caught it with a hand calculation. **Fix:** one line in the brief: "give the framing in words and how many rows/columns fit, not z".
- **It says "19.1 %" and "9.8 %" of time in motion in the same document**, and "4 rows" when there were 5. It does not matter if Opus distrusts every number.
- **The guide says "Read 05b; 05b rules"**, at most 6 points. The ceiling forces joining several things per point. It works.
- **The stage cap (1500 s) was enough;** it took 956 s.

### Sketch, animation, render
- **Separating sketch and animation was artificial here.** The world and the timeline were written together in one file; `estilo.html` comes out of `reel.html` by changing a constant, with 5 key times. It is cheaper and nothing was lost. The route treats them as two agents ("starting from the code of estilo.html"). **Possible fix:** have the animation deliver the "style" mode and make the sketch just a first stop of the same file.
- **The sketch tested nothing about motion and neither did the engine.** Nobody saw the video in motion: only still frames were seen. A rhythm error or a jump between frames is not seen in the sheet. **Real gap with no fix using these tools.**
- **`hoja.png` every 2 s hides events:** the bread fell at 8.02 s and in the sheet it did not exist; Argon reported it as "the bread is not seen". It was fixed by leaving it in frame from 5.75 s, and it came out better, but by chance. The `TIEMPOS_CLAVE` line of `--tiempos-de` existed in `oficio.json` but the route uses `--cada 2`, and **no instruction asks to write TIEMPOS_CLAVE**. **Fix:** use the seconds of the 05-DIRECCION table.
- **A failure that almost slipped by:** in the first sheet the hook label did not appear at t=0 (fade-in from alpha 0), and **frame 1 is sacred**. It is only seen because the sheet starts at 0.0. **Fix:** in the sketch checklist, "does frame t=0 carry the full hook?".
- **`medir-camara` flags as "fast travel" something the recipe allows:** short steps of 0.6 to 1 s with 8 %. It flagged 38.4-39.1 s and not 9.7-10.3 s, being the same type of step. It is a contradiction between the tool and `RECETA-CREATIVA`; the guide says "fast travel = `--fondo`". **Fix:** threshold by distance traveled, not only by duration.
- **Still stretch:** 39.1 to 50.3 s without camera (11 s) and 9 % in motion, against 24 % of the video that was liked. The rule allows up to 13 s if something changes. An extra short step at 45 s was tried and it overlapped the label with the brand mark: removed. It is left like that: it is what worries the author most in motion.
- **Argon in its blind review** (2 passes, with CHANGE in both, as the guide warns). Triage: useful were "empty and dark", the excess text, the bread and the topper's label. False: the brand mark over the calendar (it is mandatory), the silence without subtitle, the calendar cut off in close-ups, the "12 DEC" cut off in mid-camera. In `hoja.png` it opines on a travel as if it were a still frame. It says "flat 2D" and "plastic" in different reviews: **careful, without an example I do not know how much to believe it.** Three iterations of light and color raised the frame a lot: the first version was really flat.
- **Frame 1 with subtitle:** the route says subtitles "by sentence" and the hook is written on top: the same thing twice. It was decided no subtitle on the hook. **A rule is missing.**
- **Labels against subtitles:** the recipe allows 2 live ones, and `MARCA.json` does not say how much the subtitle is repeated. 3 labels that repeated were removed. **A rule is missing:** "a label does not repeat the subtitle".
- **The dirty SRT was bypassed** with a subtitle list inside `reel.html`, written by hand with Whisper's timings and the speech's text. A real builder might use `voz.srt` as is: stray quotation marks would come out in the 3 s frame.
- **Sound:** `ruidos-base.py` came out on the first try, 4 s, 18.7 dB. Nobody listened to it. The instruction carries the exact command and it works. **It is the most solid piece.**
- **`voz-preparar.py` does not keep the "¡No!" as a sentence:** added above.
- **Spend gate, retro, book:** not tested (no engine). Book reviewer: done by eye with "Visual y zonas"; a separate reviewer was not run. Terra, Flash, Sonnet: by hand.
- **`copia-ligera.py`:** 6.3 MB, crf 23, first try. **`mundo-registrar.py`:** first try. The register was left with the pilot's row: if this video is discarded, it has to be deleted, or the next one will not be able to repeat this world.
- **`BANCO-TEMAS.md` unchanged:** the topic was not moved to "Already used" because the video carries a test voice and the owner has not reacted yet. The guide does not contemplate an unpublished video.
- **The agent's own quota:** the pilot stopped for a usage limit for about 3 h. The state in files allowed it to continue without losing anything.

### Closing: the most useful lesson
The engine and the scripts hold; the gaps are in the **verification of what nobody looks at**: facts inside the image (the calendar), Whisper subtitles, and motion. Priority: SRT against the speech text, facts in the grounding list, and a way to see motion.

## Pilot verdict
Complete video without the engine. Clean frames and its own world. Without seeing motion or hearing the mix: **not publishable with this voice**; with the real voice and a look from the owner at the rhythm, publishable. Weakest: 39 to 50 s with the same shot, and the pile of the "a little bit" somewhat confusing.
