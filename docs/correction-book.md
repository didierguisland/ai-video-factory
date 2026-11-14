# Corrections book: what the owner has already corrected

A single book since Nov 9, 2026: it merges two earlier books (one from the engine and one from the example brand, which repeated almost everything). It applies to any brand; what is specific to a brand lives in its own `MARCA.md`. New corrections are noted here. The engine reads it by name: do not rename it. (This is a translation of `craft/LIBRO-CORRECCIONES.md`; the Spanish file is the working one.)

How the reviewer uses it: it opens the book, takes only the topics that apply to the step and checks rule by rule with the material in view. It returns a PASS/FAIL list, with the exact line that fails and the rule cited (topic and text). It does not correct, it reports.
All of this is a rule, except the final section "Design references", which is chosen according to the project. The reviewer does not flag FAIL for a reference.
(xN) = it was repeated N times. If two rules clash, the most recent one rules; in `video-fabrica`, in addition, whoever holds the gate decides.

## How to talk to the owner
- Chat, do not interrogate: paragraphs, one question at a time, no long lists and no 7 questions (x3, APRENDIZAJES.md:17, CLAUDE.md).
- The plan is a flexible forum of "what do we do today?", not a military one; texts to the team short but with the why (APRENDIZAJES.md:19-20).
- What the owner must paste into another app goes pasted in the chat, ready to copy, not only in a file (APRENDIZAJES.md:201).

## Words and tone
- Words that any woman understands; nothing like "colado", "chalán" or "kólla" (it sounds like a double entendre) (x3, APRENDIZAJES.md:73,114, ELEGIR-TEMA.md:19).
- Hook and facts from everyday life: "Do you put lemon on everything?", "3 out of 10" (APRENDIZAJES.md:96,114).
- Nothing translated into English without warning; the script in Spanish (APRENDIZAJES-VIDEO.md:13).
- In the AI Studio tone, no "faster"; on a serious topic those seconds are worth more (DECISIONES 11).
- Voice labels `Name:` at the start of the line, at most 2 voices in AI Studio (DECISIONES 10).

## Speech and retention
- A number or a rhythm phrase needs its frame first: say first what is being rated and on what scale; each block names the thing, tells what happened and then gives the number. No filler phrases without an object ("I already put it on": what?) (owner, Nov 11).
- The hook carries tension at second 0: prohibition + confession + promise (owner, Nov 11).
- In a short video, the keepable item and the useful rule go at the end, right before the "send it to...": in the middle it sounds as though the video already ended and then keeps dropping facts (owner, Nov 10, dessert; the trends assistant wanted it in the middle).
- The woman's doubt, written (and spoken, if there is voice) in frame 1, also as "a friend asked me" (x3, RECETA-REEL.md:50, DECISIONES 4).
- (only the example-brand series; does not apply in `video-fabrica`) Cover or series seal after second 3, or as a frame from frame 1; the cover lost 85-90 % in 3 s (DECISIONES 4).
- Something new every 2 to 4 s; in the 2 s table no empty stretch left unmarked (RECETA-REEL.md, retention layer).
- The last frame answers the first; a hook that is not fulfilled is a betrayal (RECETA-REEL.md, apple pie).
- (only the example-brand series; does not apply in `video-fabrica`) Closing with "send it to your comadre who..." and a bridge to the next edition or to the product (RECETA-REEL.md).
- Target of 60 to 70 s (130 to 150 words); up to 90 if the idea has room, without stretching (owner, Nov 4: "1 minute, 1:20, 1:30"; he liked 66 s). It used to say 45 s and a cap of 75. **Under review (Nov 9):** the trends assistant's playbook, with account data, recommends 20 to 35 s; the owner decides (`Bases/ESTADO.md`). Meanwhile, this rule holds.
- Voice: at most about 3 words per second; if it swallows syllables it is a lack of time: give time in the SRT and write the word in syllables in the description ("di-fun-tos") (APRENDIZAJES-VIDEO of the example brand).
- Each metaphor keeps the cause: the float yes, the doorbell no (ARQUITECTURA-BARATA.md:45).
- Do not connect the content of one Reel with another ("Friend with lemon"); the closing bridge is only to the next edition of the same series or to the product.
- A breather of at least 1.2 s per moment (x2, ENCABEZADO-PROMPT.md:18, REPORTE-sol de la sed).

## Visuals and zones
- Quality floor of the example brand's animations: a 3D world (local Three.js) with scenes, camera movements (dolly, pan, tilt, travels that arrive and stop), lights that change per scene and rhythm; 2D goes as a layer on top (faces, gags, signs). Before the frames, Argon directs each shot (lens, light, composition, camera entry and exit), as in `2026-11-12-siguiente/argon-tomas.md`. Never drop to flat 2D in a hurry (owner, Nov 13: "why is there no 3D rhythm, camera movements, lights, scenes?").
- A camera that can be understood: it moves, arrives, stops and lets you read before the next movement; "something new every 2 to 4 s" is not a camera that never stops. If it makes you dizzy or cannot be understood, it is too fast (owner, Nov 3, drafts of the first campaign).
- A single visual universe per video; never mix 5 styles nor copy the Atlas (x3, APRENDIZAJES.md:72, RECETA-REEL.md:60, DECISIONES 13).
- Zones: text with y >= 10 %, illustration >= 7 %, nothing in the bottom 18 % (x3, APRENDIZAJES.md:125, DECISIONES 5).
- No film grain (material texture yes); if there are rings, a light and fixed grain only in the background (APRENDIZAJES.md:108, DECISIONES 6).
- Measure each text with `measureText` in the real font of the Mac (x2, CORRECCIONES-1.md).
- Texts marked with a star are literal; a space before the word with an asterisk; logo in full color (x2, AJUSTES-cuadros-v1.md).
- Objects that are recognized instantly (orange, creams) in their real color (ENCABEZADO-PROMPT.md).
- DURATION of the prompt = that of the complete WAV, not that of the last word (the laugh got cut) (RECETA-REEL.md:55).
- The frames are reviewed before animating and before rendering. In the factory Argon and the orchestrator approve them; the owner sees the MP4 (open letter, Nov 4; before, he approved them).
- The "Example Brand" mark visible for the whole video and the social card from "follow me"; values in `MARCA.json` (owner, Nov 4: "nowhere does it say the brand").
- Without voice and without an event, at most about 3.5 s (owner, Nov 4: "a lot of time is lost there").
- Every sentence has something that is seen; two consecutive frames that are almost equal in the sheet are a weak stretch (owner, Nov 4).
- A freeze that is not marked as an effect (no zoom, sound or text) looks like a failure; when removing silences, check that the freezes still fall where they are read (owner, Nov 11).
- HTML preview: the video rules the clock and the voice follows it; if the page corrects the video, it goes back and looks like it is stuck (Nov 11).
- The trends assistant reviews with the contact sheet PLUS the script with timings; without timings it proposes cuts that mutilate the recorded voice (Nov 11).
- Subtitles and stickers reviewed on the real frames, not on paper: they covered the product and one said "Lo" when she said "los" (APRENDIZAJES-VIDEO of the example brand).

- A single text layer: karaoke of the voice, word by word with the timing (the one that sounds is highlighted); no separate headlines that repeat the voice nor little notes on top. Labels that are part of the drawing (clapperboard, plaque) do not count (owner, Nov 11, little coffee).

## Omni and AI
- Omni does not freeze or do editing effects: ask for the complete action, with trajectory, and freeze in editing. Never "is about to". The expression changes from A to B, the camera carries lens and movement, and something moves in frame (a drop, a lock of hair). A realistic kitchen with window light = dark and out of focus; a plain light set with a single action hooks more (x2, product reel, Nov 11, Argon and the trends assistant).
- Each remedy or moment starts clean: it is not chained from the last frame if it drags the previous state (product reel, Nov 11).
- 2D sticker-type cut-outs next to realistic video look cheap; the real product is never generated with AI if its real photo can be used (x2, product reel, Nov 11).
- A continuity jump from Omni (something appears suddenly) is covered with a cut: a sudden zoom-in on the side that is visible right before the jump and a return to the wide shot afterward; with two cuts it reads as the passing of time (product reel, Nov 11).
- Omni spreading something on the hair (a hand smearing) looks fake in motion: in editing it is cut from the previous gesture (spoon leaving the jar) to the result already applied, without showing the contact (owner, Nov 11).
- No noticeable slow motion: a shot slowed to 0.75x in the closing lowers the rhythm; at most 0.85x (owner, Nov 11).
- If the shot runs out, it is not stretched with back-and-forth (boomerang) or long freezes: another shot is requested from Omni (owner, Nov 11: "I did not like them at all").
- Shots of 10, 8 or 4 s; no stretching to 10.6; the fewest shots possible (APRENDIZAJES.md:201, DECISIONES 12).
- The same STYLE, VOICES and CHARACTERS block word for word in every shot (APRENDIZAJES.md:201, DECISIONES 12).
- Letters, numbers and logos never generated by AI: they go in the layer (x2, APRENDIZAJES.md:200).
- AI images: "not resembling anyone famous" (the scientist came out as Einstein) (APRENDIZAJES.md:116).
- Do not invent prices, neighborhoods or apps; what is missing is marked `[TO CONFIRM]` (edicion/PROMPT-EDICION.md).
- Images are uploaded to the app together with the prompt, not separately (video with a real person).
- Omni prompt in this order: REFERENCES (optional) · STYLE · LIGHT · SETTING · CHARACTERS described completely even if there is a reference · VOICES · VOICE TIMINGS in SRT · CAMERA by seconds · ACTION by seconds · SOUND without music · AVOID. Characters with a 6-angle sheet; order: story -> characters -> sheets -> shots (APRENDIZAJES-VIDEO of the example brand).
- "Violates policies" block on images: it appears with women described with words of body or fabric ("huggable", "full body", "lace", "satin") or white powder in the mouth. Try removing one thing at a time (APRENDIZAJES-VIDEO of the example brand).
- Voice decided in the sheet: on camera = Omni's; off-camera narrator = AI Studio (DECISIONES 2).
- AI video prompts, step by step and with physics (owner, Nov 12, "6:02 am"): each movement is described with its direction and its amount (the car window goes down from top to bottom in X s; it goes down N steps, always downward, away from the camera), how what moves reacts (the wind comes in from the left and throws the locks to the right, fast and natural, and they stay tousled), the geometry of the place (where the staircase goes, which side the railing is on) and the camera (where it starts, at what distance it follows and at what height). If it stays ambiguous, the AI invents: the staircase went up and down and the glass looked strange.
- More of the same (Nov 12, car shot): say where she looks and that the head does not turn (otherwise it turns and the face is seen); that the clothing receives light so that its color is seen (in shadow, the wine-colored blouse came out black); that what moves comes already moving from frame 0 (otherwise the car "starts from nothing"); do not draw glass if it can be avoided (window open from the start); do not put the camera where a real object would cover the character (the AI removes the object: the headrest disappeared).
- With a reference character (Nov 12): say that from the reference only body, skin and hair are taken, and name the clothing of the shot ("in the reference she wears a black shirt; here, a wine-colored blouse"), also in AVOID. If not, it copies the reference's clothing.
- No exaggerating in the prompt (Nov 12, rearview mirror): "nest", "halo", "pure hair", "dozens of little hairs" and repeating it produced a caricature (a tuft that stuck out of the mirror). Ask for the effect in a realistic degree ("tousled as after driving with the window open") and that it respect physics (nothing leaves the frame of a mirror).
- The product is described looking at the real photo, not from memory (Nov 12): I wrote "cap with a glass dropper" and the real bottle does not have it in view (cylindrical silver cap with a flat button); the AI gave it a glass bulb. The text rules more than the reference image.

- **Face in a close shot (Nov 13, shot F of 6:02):** in a wide full-body shot the AI draws the face badly (it comes out deformed). If the face matters, a short medium shot, from the chest to the head. And do not ask for wind to show off the hair: it tousles it or covers the face. The hair is shown off with a head turn against the light.

- **Product size with a known object (Nov 13, shot G):** "ten centimeters tall" is not enough: the AI made it thick like a thermos. Give height AND thickness, and compare it with something from every day (the bottle is the size of a whiteboard marker). And the wink is asked for early, with the order that afterwards both eyes stay open.

## Health and product
- No health promises and no linking a symptom to the product (x4, CLAUDE.md, ENCABEZADO-PROMPT.md:15, ELEGIR-TEMA.md:22, RECETA-REEL.md:29).
- A "may" never becomes certainty; facts go through Terra (in `video-fabrica`, after writing the speech; it does not apply as a failure earlier) (APRENDIZAJES.md, sed).
- Document: total fidelity, do not invent or lose; "there are 4 steps"; if it contradicts itself, ask the owner (MATRIZ-FIDELIDAD.md:18,24).
- Sentences filtered against Terra's list of prohibited ones, above all what comes out of Gemini (RECETA-REEL.md:21).
- If the closing asks for a message or a word, it must promise a concrete and useful answer (use, price, routine), not only ask for contact (x3, HUMANIFY-CANDIDATOS of the example brand).

## Process and models
- Order after the voice: SRT (Sonnet medium) -> taken to the owner -> conceptual storyboard by Opus discussed with Argon over the SRT -> the trends assistant reviews it -> still frames -> animation. No jumping to frames or to builders beforehand, and one step at a time (owner, Nov 13: "hold on, calm down").
- To ideate a new video: first ask the trends assistant, in a few bullets, which topics are trending; the brainstorm comes from there. Never arrive with a finished idea from the old queue or only from metrics (owner, Nov 13: "your proposal is horrible").
- Use all the models, each in its own thing; if one is left out, say so, except in `video-fabrica`, where the cast is fixed (x2, ARQUITECTURA-BARATA.md:48, APRENDIZAJES.md:190,198).
- Decide the type of production and the voice on day 1, in the sheet; in `video-fabrica` it is already fixed (APRENDIZAJES.md:205, HANDOFF-10.md:7).
- Argon and Flash on medium, except what the route's cast says; Terra with `--search`; the `-o` path always absolute (DECISIONES 8).
- Argon and Flash carry "do not use tools" or come out empty (RECETA-REEL.md:21).
- Local Whisper first; the Claude app only as plan B (DECISIONES 9).
- A separate Opus builds (the builder, or an app chat), never the orchestrator; the render is run by the engine; a one-step ffmpeg is run by the orchestrator directly (ANALISIS-clases-motion.md:18, RECETA-REEL.md:63, HANDOFF-10).
- Before delegating to Codex or agy, tell the owner in one line what is being sent (CLAUDE.md). In `video-fabrica` there is no asking per delegation: Argon, Flash and Terra run because they are part of the team that the owner already authorized in the routes (policy in `orchestrator-guide.md`). Images by Codex stay off unless he says yes.
- A block by the third-party hook is never worked around; the command is given to the owner (global CLAUDE.md).

## Publishing
- Instagram and TikTok texts in `TEXTOS-PUBLICACION.md` before calling it ready (APRENDIZAJES.md:136).
- Schedule 30-45 min before the hour. Separation between videos of the same account and schedules: those of the brand (`MARCA.md`); the example brand, with the trends assistant's data, asks for 8 h if there are two on the same day (before 3-4 h).
- Measure at 48 h (and at 7 days if possible) in the brand's `REGISTRO-reels.md`; change a single thing per Reel (RECETA-REEL.md, retention; trends assistant, Nov 9). The old `BITACORA-METRICAS.md` stayed in the brand's data folder.
- Note the % of use per video in ARQUITECTURA-BARATA.md (ARQUITECTURA-BARATA.md:50).

## What the data say (trends assistant, Nov 9; to be validated, the reviewer does not flag FAIL)
They come from 7 reels of the example brand. They become a rule when the `REGISTRO` confirms them with more videos.
- The start decides: what is lost is lost in the first 3 s. If the skip rate goes above 55 %, only the hook is rewritten; if it drops below 35 %, that hook structure is repeated.
- A single idea per video and the promised fact at the end (open loop); the closing connects with the start so that it is replayed.
- If saves are at 0, something keepable is missing (list, recipe, steps). If there are views but no followers, a request to follow is missing.
- Answer comments in the first 2 h; if that is not possible, too much is being published.

## What the engine already guarantees (the reviewer does not receive it)
- The speech is written by Opus, never Sonnet: Sonnet's came out flat (x2, ARQUITECTURA-BARATA.md:6, APRENDIZAJES.md:189).
- A sketch of key frames reviewed before animating: a fixed stage of `video-fabrica`. Argon and the orchestrator approve it (change of Nov 4; x6 before with the owner).
- Narrator with a clean voice and Opus's sound: fixed recipe and cast (owner, Nov 4).
- Count words with the command, not by eye: Sonnet counts badly (ARQUITECTURA-BARATA.md).

## Design references (they are not rules; chosen according to the project)
What we already tried and came out well. Used as a starting point, not as an obligation.
- Style C (flat night) for the example brand's animation; other projects carry their own. An AI video in plasticine was dressed with the world of the video itself (DECISIONES 13).
- What the "Example Brand" seal looks like: in one project it was plasticine, trembling; in another, fixed on top and sober. That it is there is a rule (Visuals and zones).
- A closing that invites without selling: the owner's latest is "follow me and send it to your friend" (Nov 4, x1), and that is what is used. Before: a question plus one word per message ("Write me BREAD").
- Staggered movement at 12 fps, "boil" and squash entries: for the animated or plasticine; in premium, smooth and still movements.
- What the subtitles look like (karaoke with a mustard pill of style C, an amate-paper strip in one project, cream serif in another): according to the style. That there are subtitles is looked after (see the project's PROPUESTAS).
- Synthesized sound effects (another project): when they add, not always.
