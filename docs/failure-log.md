# B. Corrections and failures of the first serious video (task 54)

## Summary
1. The `video-mundo-3d` route never reached the end: it stayed at the `sonido` (sound) gate (`ruta.json`: phase `compuerta`, index 14). Clean voice, life layer, render, brand mark, take and join were done by hand outside the engine. **The path the owner liked is not in any route.**
2. What would most break a video without the owner: the open route 54 blocks `ruta iniciar`; the route carries text from this video and even about hair; `sonidos` still asks for the phone recipe; there is no step for SRT, cut-outs, life or final assembly.
3. Most dangerous failure of the engine: **a fallen workshop stops nothing**. With the 429 the gate opened without audio. A failed correction regenerates the sheet with the old HTML and looks corrected.
4. Argon medium said CHANGE in 4 of 4 reviews and once praised improvements that did not exist. It is no good as a gate. And `render()` automatically sends its CHANGE to Sonnet.
5. Already fixed in code, but not committed: `permite` per stage, real workshop error (cut to 100 characters), reviewer after the first sketch, `audio-final` in the render, `SPEECH:`/`FIN` block in `hechos.py` and A/B in the workshop stage. 2 tests of `test_oficios` fail (the `campana` craft).
6. Motion and ear are verified by nobody but the owner. They can only be substituted with a camera measurement and with the cast and recipes that he already approved.
7. The spend measures too little: the Opus that built the first sketch (20 min, killed by the cap) has no run in `marcador.db`.
8. The owner's and the orchestrator's hours are those of the `00-*.md` files (UTC). Those of `CHAT.md` are local (UTC-6): 22:26 of CHAT = 04:26.

Keys: **[C]** verified, **[I]** inferred. Status read in the code today: **FIXED**, **PARTIAL**, **UNFIXED**. Everything fixed is uncommitted (`git status`).

---

## 1. Orchestrator errors

| # | Failure and evidence | Root | Who saw it | Structural correction | Status |
|---|---|---|---|---|---|
| O1 | Took the reference as "a single take, a single world" (resp. 01:48 and 01:50). "it is not about literally copying" (owner 01:55) | Copied the reel's technique, not what he liked | Owner | Route: "there may be cuts or connected worlds" in all scene stages | PARTIAL: `estilo` and `animacion` already corrected (04:05), but `ajuste` still says "a single world" and so does the `brief` of task 54 |
| O2 | The correction of O1 lived 2 h only in RECURSOS-5, while the route kept saying "ONE SINGLE WORLD" (compaction, point 3; fixed with `ajustar_ruta.py` at 04:05) | Two sources of truth: package and JSON. Same lesson as FALLA 14 ("the template beats the instruction") | The orchestrator, before building | Rule: a correction is applied in the same turn to the stage's instruction. Instructions carry no text from the video | UNFIXED (it is a design point of the new route) |
| O3 | **Frozen brief.** `ruta.json` keeps "How much do you think it goes up...", "a single 3D world", "72 s" and "write me FIESTAS". It is prepended to every workshop brief (`_ruta.py`, `'instruccion': 'Brief del orquestador...'`). Opus had to clarify: "it overrides the one in the brief" (CHAT:390) | There is no command to change the brief | This analysis | Command `ruta brief "<text>"`, or a minimal brief (topic and duration) and what is decided in the deliverables | UNFIXED |
| O4 | Asked for "always something happening" and a non-stop camera came out; it caused dizziness: "very fast... not understood" (owner 02:23). "the fault of the dizziness was mine" (resp. 02:25). Then the room went to still shots of 8-13 s (resp. 02:29) | "Something new every 2-4 s" was read as a camera rule | Owner, and the orchestrator the opposite way | Written rule: camera moves, arrives, stops for ~2 s; the new thing happens inside the frame | FIXED as text (`notas.md:35`, `LIBRO:33`, `animacion`). It is not measured: see F9 |
| O5 | His opinions in the package and the room adopted all of them (resp. 01:25) | The boss's opinion inside the context of whoever ideates | The orchestrator | The ideation stages receive facts and limits, not opinions | UNFIXED as a rule (APRENDIZAJES.md, Nov 3) |
| O6 | Biased review: it listed to Argon what was asked (`#1234`) and Argon approved improvements on an old sheet. The neutral prompt worked (`#1300`) | Telling the judge what to expect | The orchestrator, on looking at the sheet | Fixed request: "first describe what you see", with no list of changes | PARTIAL: the route's `revisa` is already neutral; there is no general rule (x1) |
| O7 | "Almost two kilos" was published without a source: 0.37 + 1.4 = 1.77 is our own sum. The team stopped it (CHAT:269, "it is a sum of ours") and Opus proposed it again (CHAT:313). The book flagged it (`LIBRO-speech-2.md`) and Terra did not answer. The owner was told (resp. 02:38), never verified (`HANDOFF-15`) | A CHANGE from one stage does not survive the next, and the book only reports | Orchestrator and book | Facts stage: `HECHOS-VERIFICADOS.md` with sentence, source and whether read in full or not; the speech uses only that; the verifier compares figures. If not, say what was quoted (`a kilo and a half more`) | UNFIXED |
| O8 | Accepted the hair 3D because the channel said "approved": "I did not like it at all" (owner 01:55) | Approving a cut is not approving a style | Owner | In a new video no style is used as approved except by a registered taste decision | FIXED as a learning; nothing enforces it |
| O9 | Gave the phone recipe to a narrator of an invented world: "it breaks the aesthetics a lot" (owner 05:55). "It was my mistake" (resp. 05:56) | Recipe made for a real person on camera, set as the "base" | Owner, by ear | See M3 | **UNFIXED** in the route |
| O10 | Told him the concept in agent language: "I did not understand a thing" (owner 01:41) | Passed the deliverable along without translating | Owner | Every delivery to the owner is told as "what you are going to see". Template for the final report | UNFIXED as a template |
| O11 | Said "your 5-hour limit" without checking the account (resp. 05:04): "What??? ... my quota at 17%" (owner 05:08). Earlier blamed its own permissions ("error in how I built that stage", 05:04) | Did not know that the engine uses another account, and the real error was swallowed (`exit 1`) | Owner | Memory note `motor-cuenta-terminal.md`; quota preflight (see F3) | PARTIAL: memory yes, preflight no |
| O12 | Rendered it itself (`#1476`): "Have a medium Sonnet of ours render them" (owner 05:27) | The mechanical work was done by the orchestrator | Owner | Render through the engine, or Sonnet if outside | FIXED as a rule (`LIBRO:66`); the engine does it without a model |
| O13 | Final silence of 6 s put by hand in `voz.wav` (resp. 04:06): "a lot of time is lost there" (owner 07:15). It was sped up x1.8, from 6.3 to 3.5 s | Silence decided in text to "come in through the window", without seeing it | Owner | Rule: a voiceless tail of at most 3.5 s, in the storyboard and in the silences step | UNFIXED |
| O14 | The video reached the end without saying the brand: "nowhere does it say the brand" (owner 07:37) | The mark is a "Reference" (`LIBRO:84`) and the reviewer does not flag references | Owner | `final` step: brand and social handles always, with data from a file | UNFIXED |
| O15 | A 51.6 MiB MP4 did not reach the owner's phone (`#1547`, cap 30 MiB; resp. 05:31) | The heavy version was sent | The tool | Always deliver the light copy; the engine already has `comprimir` | PARTIAL: `comprimir` exists, delivery is not in the route |
| O16 | Added "something that can be done today" and schedules: "omit that completely" (owner 01:15). The room self-limited anyway (resp. 01:25) | Time entered as an ideation datum | Owner | No deadlines in ideation packages | UNFIXED as a rule; the room flagged it as surplus (`05-RETRO-RECURSOS.md`) |
| O17 | Concept of 35 s and video of 80 s: "it is coming out very short" (owner 01:46). The book flagged FAIL for 80 s (`LIBRO-speech-2`) | `LIBRO:27` and `notas.md:31` (this one, "if the brief says nothing else") fix a target of 45 s, against the owner's "1 min to 1:30" | Owner and a false alarm from the book | Change the book and the notes to the current range | UNFIXED |
| O18 | Hooks from the fact, four rounds (A/B, `gancho`, `gancho-2`, `speech-ajuste`): "it does not quite connect" (owner 02:23) | The orchestrator started from the fact, not from what people live | Owner | First instruction of the hook: what the woman lives, colloquial and funny; the fact comes later | PARTIAL: `LIBRO:16` and RECURSOS-5 have it; `rubrica.md` does not ask for humor |

**What the orchestrator did well and must become a function:**
- Caught promises and mockery that Argon let through: the dress bow, a 1.28 s camera, double focus, a loaded map (`05b-AJUSTES-ORQUESTADOR.md`, x1); a round person rolling (resp. 06:22).
- Passed the composition matters to the animation instead of a third Sonnet round (`#1322`). It came out well: "the little weight in scene 4 is now the protagonist" (resp. 05:31).

**The factory needs a promise-and-mockery filter** before building. Today it depends on the orchestrator's memory.

---

## 2. Agents: where they performed and which brief worked

| Agent | Well | Badly | Brief that worked / that did not |
|---|---|---|---|
| **Argon medium (reviewer)** | Saw real breakages: MARCH cut off, ring bread out of place (`#1139`) | CHANGE in 4 of 4. It hallucinates (below). It complained about the empty bottom space, which is a safe zone (resp. 04:44) | Works: "first describe what you see", with no list, only the sheet. Fails: a list of what was asked; letting it read `02-ESCENAS.md` without telling it how many frames there are |
| **Argon high (director)** | "I super super love it" (owner 06:45), its 460-line document made the leap | Coordinates calculated without seeing: Opus moved pot, ring bread, mountain, vignettes and poster. It put in a promise (bow) and a fast camera (1.28 s) | Works: `ENCARGO-ARGON-VIDA.md`, with a real strip every 2.5 s, timings per word, code, the owner's ideas that rule and outside ideas that it may discard. **Its coordinates are intention, not measurement** |
| **Argon in the room** | Directed styles; the train and the pin worked | Preferred the Scale model and the owner chose the other two (x1). Its "3 kilos" without a source (resp. 02:05) | Its taste does not replace the owner's: taste choices need written criteria |
| **Flash** | Loose ideas and jokes for the speech (guest of `speech-2`) | "Do you really gain 3 kilos?" with Argon, without a source | Good for diverging, never without Terra or Opus behind it |
| **Opus** | Animated the whole thing with no rounds (3.39 USD, 852 s, `RETRO`). Won the sound A/B: "200% better" (owner 05:55). Rebuilt the life with identical pixels in what was protected. Found that "THE DAYS IN BETWEEN" was never seen | First sketch: 20 min and killed by the cap (CHAT:415), with an invented assembly step (`_estilo/construir.mjs`) that broke the touch-up. Its doubt "paper and cloth look fake" almost toppled two styles (`APRENDIZAJES`) | Works: brief `#1718`: read, zone, steps, "Argon calculated without seeing", limits, STOP, criterion, report of 10 lines. Its technical assumptions are tested, not believed |
| **Sonnet** | SRT, render, join and brand mark clean. With the sheet in view, round 2 good (resp. 04:44) | Round 1 blind: broke posters and bread (`#1273`). "It meets the list, but does not think like a director" (resp. 04:44). Lost the sound A/B. The 2 touch-ups cost 1.70 USD, with cache/output of 65-71x (`RETRO`): the touch-up did not come out cheap | Works: a concrete list with its sheet and mechanical work with exact steps. Does not work: composition |
| **Sol** | Objected to "I start Monday" as an unproven moral (resp. 01:50) | Low evidence in this run: 3 runs | Guest only if there is a doubt about the story |
| **Terra** | Knocked down "3 kilos" and warned about the promise of the golden stretch | Did not resolve "almost two kilos" (`LIBRO-speech-2`). 843,712 tokens in 6 runs (`RETRO`) | A facts brief with source and quote, only once, not in every chat |
| **Codex Terra (images)** | Food cut-outs integrated in 3D (resp. 02:13) | - | Brief by file with `low`. It goes outside the route, see P7 |
| **Omni** | The take came out and was used | A canister with "Nutrition Facts" and a barcode; a visible phone (resp. 07:41). [I] The prompt names the "smartphone" and the "canister", and that may have induced them | If Omni returns: do not name the take's phone as an object; plain canister with no label. The owner accepted it without regenerating |

**When Argon hallucinates [C, x3 different]:**
- **Opines on the document and not on the image:** it talked about a "Scene 6" that was not in the sheet (`#1139`, resp. 04:29). Half corrected with "one line per frame".
- **Confirms what it was told:** "The pin is now matte", "the little weight now reads well" on `estilo.png` made with the HTML of 22:26, without changes (`#1236`).
- **Calculates what it does not see:** positions and pixels of `05-DIRECCION-ARGON.md`.

**What the factory must do:**
- Argon reviews with a sheet, number of frames and a neutral request.
- Its CHANGE goes through an Opus triage before reaching Sonnet.
- Its verdict is never an automatic gate.

**Touch-ups:**
- **They worked:** a concrete list with the sheet visible and permission to test (round 2); ffmpeg on the MP4 for the zoom and to attach audio, without re-rendering.
- **Blind:** round 1 of style; Sonnet edited `estilo.src.html`, could not run `node` and the engine regenerated the old sheet.

---

## 3. Engine and tools

| # | Failure and evidence | Root | Detected | Structural correction | Status [read in code] |
|---|---|---|---|---|---|
| M1 | **Workshop permissions.** Sonnet could not run `node _estilo/construir.mjs` (CHAT:424) nor `receta-voz.sh`, python or ffmpeg (CHAT:452) | Claude only allows the `verificar` command | Agent's notice | `permite` per stage (`_taller.py:101`, `_ruta.py` in `taller`) and the instruction "one command at a time, without chaining". Tested for real x1 (runs 409 and 410) | FIXED |
| M2 | **Invented assembly step.** Opus created `construir.mjs`; the touch-up could not rebuild | The `estilo` instruction asks for "embedded in base64" and nothing forbids assembling | Failed touch-up | Remove the assembly: cut-outs in `_estilo/recortes.js`, as `animacion` already says | **PARTIAL**: `animacion` yes; `estilo` (ruta:202) still asks for base64, and that may repeat failure and cost |
| M3 | **Phone recipe** in `sonidos` (ruta:265: "read audio-celular.sh... It is the base") | Instruction from another case | Owner | Instruction: narrator with `receta-voz-limpia`; phone only if the person appears on camera. Copy the recipe and `ruidos.py` to the craft library; today they live in a campaign folder | **UNFIXED** |
| M4 | **429 looked like an agent failure.** `did not finish (exit 1)` (CHAT:455) | `_ejecutar` threw the error away | Manual probe (`#1409`) | Real error saved (`_taller.py:29`) | PARTIAL: `_taller.py:160` cuts it to 100 characters (`..."usage_lim`, CHAT:460) |
| M5 | **429 stops nothing.** A and B fell and the gate opened without a file; the summary says "A continues" (CHAT:460-463, `#1403`) | `etapa_taller` and `taller_ganador` do not check the deliverable (`_ruta.py:794`, `803`); only `un_constructor` (`781`) does, and that one accepts an old file | Orchestrator | Require a new deliverable (fingerprint before and after), phase `pausada` with restart time and retry | **UNFIXED** |
| M6 | **No way to retry.** The orchestrator edited `ruta.json` by hand (`fase='lista'`) and left a `while sleep` (`#1413`) | `avanzar` at a gate only returns the summary (`_ruta.py:378`) | Orchestrator | Command `ruta reintentar` | **UNFIXED** |
| M7 | **A failed correction looks like a correction.** With `estilo.html` of 22:26 the engine generated a new sheet at 22:37 (`#1236`) | `corregir` does not compare the deliverable (`_ruta.py:714`) | Sonnet's notice and file times | If the fingerprint did not change: the pass fails and does not regenerate | **UNFIXED** |
| M8 | **Argon did not come in if there is no A/B.** "Shouldn't the review be done by Argon?" (owner 04:25) | The judge only existed in A/B | Owner | `un_constructor` calls the `revisor` (`_ruta.py:790`) | FIXED for the first sheet |
| M9 | **After correcting, it does not review again.** It only repeats in `platica` (`_ruta.py:467`). The orchestrator did it by hand (`#1234`, `#1255`, `#1300`) | Condition by type | Orchestrator (resp. 04:29) | Remove the condition for sheets | **UNFIXED** |
| M10 | **`render()` self-corrects with CHANGE** (`_ruta.py:822`). `cambia()` looks for the word in the whole text. With Argon at 4 of 4, Sonnet would receive every complaint, including false ones. **It was never executed in this run** | Reviewer as a trigger | Code reading | Opus triage between reviewer and touch-up; at most one pass; only concrete breakages | **UNFIXED** |
| M11 | **A 20 min cap kills work and erases its spend.** Opus on style (CHAT:415); no Opus run in `estilo` (`marcador.db`: only 396 and 400). `RETRO` attributes it to Sonnet | The process is killed before `_gasto_claude` (`_taller.py:107`, `150`); `claude -p --output-format json` only delivers usage at the end | This analysis | `tope` per stage, 40 min in animation: 14.2 min without life + ~19 min of life layer already exceed 20 (`HUMANIFY_TALLER_TOPE` exists). Register a run without tokens so that it is noticed. Warn that the result is partial | **UNFIXED**. The orchestrator did not tell the owner either: "The sketch is out" (resp. 04:26) |
| M12 | **`SPEECH:`/`FIN` format** ignored: HECHOS counted 6 (resp. 02:01) and 39 words. The orchestrator edited it by hand (`#828`) | It is asked for in `cierra` and not validated | Orchestrator | `hechos.py` reads the block (FIXED, line 44). What is missing is to **reject** a deliverable without the block | PARTIAL. Today `palabras_speech: 132` |
| M13 | **`PROCESOS.json`:** "video" or "reel" pull in another project's factory; removed by hand (`#230`). "campaign" pulls in RECURSOS 1-5 **and this video's `voz.srt`** (`git diff`) | Global keyword per project, and routes of this campaign | The orchestrator; the owner noticed the cost: "I do not know why the context rose so much" (01:29) | Remove those entries. Resources through `--recursos <folder>` in `ruta iniciar`, with only what belongs to that video | **UNFIXED**: the next video would inherit "write me FIESTAS", the merge and another SRT |
| M14 | **Large files in the prefix:** silently cut at 6000 characters (`_teams.py:242`). RECURSOS-4 weighs 5,906: at the limit. It goes in every turn of the six | No mark, against FALLA 37 ("nothing is cut silently") | This analysis | Use `recortar()` with a warning; a short package per stage | **UNFIXED** |
| M15 | **External files signed by whoever was speaking:** drafts as if from Argon (resp. 02:05); 20+ `sistema` lines in the channel (CHAT:329-350), which go into everyone's context [I cost] | `anunciar` attributes to the current turn | Orchestrator | What is outside already appears as `external change`; what is missing is ignoring `drafts/`, `_verificar/`, binaries and grouping | PARTIAL |
| M16 | **Sound cast on Sonnet** with `alternativa` (`elenco.json`) although Opus won | Decision not applied | HANDOFF-15 | `video.sonido: opus medium`, no alternative | **UNFIXED** |
| M17 | **No spend cap.** `tope_usd` is not in the route or the craft; `_ruta.py:399` would support it | With the owner at the gates it was not needed | This analysis | Set `tope_usd`; the value comes from the spend analysis | **UNFIXED** |
| M18 | **`@owner` in the workshop.** `_taller.py:77` invites asking him; `decidir` refuses if there are questions (`pendientes`). A Sonnet asked to approve commands (CHAT:424, 452) | Designed with the owner present | Code reading | Factory mode: "decide with these rules; if you cannot, `@orchestrator` and what you assume" | **UNFIXED** |
| M19 | **The book demands the owner:** "Show frames... without the owner asking" (`LIBRO:41`, topic "Visual y zonas", the one `render` reviews) and "Still frames approved by the owner" (`LIBRO:78`, a section the reviewer does not receive, but it is still the written rule) | Rules from when he was there | This analysis | Rewrite: the orchestrator approves with criteria; the owner only if the video asks | **UNFIXED**: [I] the reviewer could flag FAIL for `LIBRO:41` in every automatic video |
| M20 | **Failing tests.** `test_oficios`, `campana` craft: `KeyError: 'campana'` and `{} is not true` (run today) | New craft without `hechos` or expected values | Tests | Add them; commit only with `OK` (FALLA 26) | **UNFIXED** |
| M21 | **Hook `bloqueo-terceros`:** I found no block in the transcript [C, text search] | - | - | Nothing to correct. The rule stands: it is not worked around | No failure |
| M22 | **Account and quota:** the agents use the terminal's `claude` (Pro, `#1433`); the cap arrived at 7.85 USD with other activity in the window [C, x1]. The owner will change that account (07:56) | Two sessions, two quotas | Owner | Preflight with `claude auth status` and a ping; it spends almost nothing (`#1409`: 0.04 USD). **The real limit with the new account is not known** | UNFIXED |

### How it was tested and what cannot be tested
- **Unit tests:** the workshop uses a fake `claude`, so they check the arguments and not the real permission. `permite` passed the test and was later confirmed for real only by runs 409-410. **The routes need a short real test** (see P16).
- **What never ran:** `render` with reviewer, `final`, `cierre`, `decidir usar-b` in sound, and the whole complete route.
- **Motion:** nobody sees it before the owner: "I only reviewed loose frames" (hand-backs 02:12 and 02:14; resp. 07:08). A model only receives frames.
- **Ear:** it is only measured (dB, duration). No model hears: "how it sounds only you can judge" (resp. 06:07).
- **Possible substitutes:**
  - **Camera [I, untested]:** a script that calls `seek(t)`, reads the camera position if the HTML exposes it, and flags maximum speed and stops of less than 1.5 s; or a difference between frames with ffmpeg. Calibrate with version D (good) and the drafts (dizzying).
  - **Audio:** check voice-to-noises distance >= 15 dB, peak, and exact duration. Quality depends on the cast (Opus) and on copying the clean-voice recipe.

---

## 4. Prioritized list: what would break an automatic video

**P0: without this it does not start or surely comes out wrong**
1. **Close task 54** (`ruta abandonar` or finish it). If not, `ruta iniciar` says "there is already a route in progress" (`_ruta.py:336`). Careful: `abandonar` discards the chat (FALLA 27); save what is needed first.
2. **A new generic route.** The current one carries "about hair" (`concepto`), "merge of Pop-up and Tablecloth", `drafts/estilo-2-popup` (`estilo`), "the owner congratulates" and "dress" (`escenas-2`), little weight and balloon (`storyboard`). It is this video's log, not a recipe.
3. **`sonidos`:** clean voice, Opus and no A/B (M3, M16).
4. **Voice end to end.** The route expects `voz.wav` and `voz.srt` (ruta:192) and nothing creates them: the AI Studio text, the SRT with Whisper and the silences were manual work (`#892`). A step is needed: deliver text to the owner in the chat, receive WAV, `transcribe.py`, compare with the speech, silences with a tail <= 3.5 s. **It is the owner's only stop.**
5. **Image cut-outs.** `estilo` reads `drafts/imagenes/` and no stage creates them. They were made with Codex outside, and the global rule asks to ask before delegating to Codex. **Owner's decision:** written authorization for the factory, or an alternative without Codex.
6. **`final` step:** life layer, brand mark, social handles, light copy < 30 MiB and publishing texts (`LIBRO:71`; owner 07:48). Today none of this exists in the route. The Omni take is optional. Without Omni, the ending cannot "leave a way to the kitchen": `animacion` asks for it today.
7. **PROCESOS and brief** (M13, O3): take the campaign out of the general context.
8. **Mode without the owner** (M18, M19): the book, the notes and the workshop still ask him.

**P1: the video comes out, but may come out broken without anyone noticing**
9. **A fallen workshop stops the route** with pause and retry (M5, M6). It is the most important engine fix: at night there is nobody watching.
10. **A correction with no change does not count** (M7), and re-review after correcting (M9).
11. **Argon with triage** before self-correcting (M10), and a promise-and-mockery filter (section 1).
12. **Facts with a source** (O7): `almost two kilos` would repeat with another figure.
13. **Cap per stage and visible spend** (M11, M17). With the life layer, 20 min is not enough.
14. **Quota preflight** (M22).
15. **`estilo` without assembly or base64** (M2).

**P2: quality and cost**
16. **A short real test** of the new route, for example 10 s with a test voice, without waiting for the serious video.
17. **Measure the camera** (section 3): motion sickness is the only thing that today only the owner catches.
18. **Commit and tests green** (M20), so as not to lose the engine: nothing from this session is saved.
19. **Clean the book:** duration (O17), rules with the owner (M19), brand mark from reference to rule (O14); channel noise (M15) and cut with a warning (M14, M4).

---

## 5. Not verified
- Whether Argon or Terra read the original article: `HANDOFF-15` says no, and I did not search further.
- AI label per network: pending since 01:31; the publishing text already carries an AI line, but each network's rule is still unverified (resp. 07:48).
- How much the 20 min Opus spent: there is no data.
- The causes marked [I]: Omni's prompt and the cost of the noise in the channel.
- I did not see the videos or hear the audio. I did not listen to anything of what is described here as sound.
