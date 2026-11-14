# AI Video Factory: overview

**What it is.** The owner says "I want a video about <topic or nothing>" in a chat attached to this folder. They receive a text and a tone, paste them into Google AI Studio, download the WAV and hand it back to the chat. The next thing they receive is the MP4 and the text for Reels and TikTok. Every video has its own world: the method is copied, not the result. It is built to publish one video after another.

**How it is used.** The `fabrica-video` skill leads to the orchestrator guide (`orchestrator-guide.md`), which has every command. Engine: a route runner (`ruta ...`), route `video-fabrica`, for the example project. This repository contains the route definition (`pipeline/video-fabrica.json`), the model assignment (`pipeline/elenco.json`) and the stage tools (`engine/`); the route runner itself is not included.

## The map
| What | Where |
|---|---|
| Orchestrator step by step | `docs/orchestrator-guide.md` |
| Stages | `pipeline/video-fabrica.json` |
| Recipe, brief template for the art director model, worlds, brand | `craft/` (`RECETA-CREATIVA.md`, `ENCARGO-DIRECCION.md`, `MUNDOS.md`) |
| Voice without a model, sound effects | `engine/voz-preparar.py`, `engine/receta-voz-limpia.sh`, `engine/ruidos-base.py` |
| Measuring camera poses, camera motion, contact sheet | `engine/encuadre.py`, `engine/medir-camara.mjs`, `engine/hoja-html.mjs` |
| Reviews of the guide and code, pilot log | `docs/pilot-1.md` |
| The analysis the design came from | `docs/cost-analysis.md`, `docs/failure-log.md` |

## Orchestrator decisions (Nov 4)
- **Sketch before animating: yes, 5 code frames, one Opus and the art director model (Argon).** The earlier analysis proposed 3 images and a short draft. Images need Codex, which requires the owner's permission, and a moving draft would not be seen by anyone before the owner. But each video brings a world that was never tested, and the animation is the expensive part: about 1.2 USD against 7. What the draft was meant to protect against, motion sickness, is covered by `medir-camara`.
- **No frames approved by the owner, a 90 s cap, no stops on the owner:** an open letter from the owner (Nov 4); noted where those rules used to live.
- **Terra on the speech only if there are facts**, because of its quota cost (about 190 thousand tokens per turn). Dates that the package already carries do not count as facts.
- **Brand mark at y=196**, inside the safe zone. Reason in `MARCA.json`.
- **20 USD engine cap** per video: when it is exceeded the route stops at a gate and the orchestrator continues. Estimated by the analysis: 12 in engine.

## Honest limits
- **The engine has not run with real models end to end.** It was tested with fake agents and the real scripts, and a pilot done by hand (`pilot-1.md`, real Argon, test voice) produced a complete video. What remains to be seen: whether Argon can direct a world that is not made of paper, whether "life" comes out well in a single pass (so far it was done in two: if it fails, go back to two), the closing without a narrator on camera, and whether 3 idea stages are enough.
- **Motion and ear are judged only by the owner.** Nobody else saw the motion, not even in the pilot. `medir-camara` (travels, short steps, long takes), the contact sheet at every event and the mix measurements are substitutes; the first one was calibrated with two videos.
- **Everything is x1:** one video, one night, no publishing metrics. The owner's tastes may change. What is most likely to turn out worse is the style: nobody else did the merge that the owner liked.
- **Estimated cost 19 USD per video, 15 to 25,** from a single data point. On the Pro plan of the terminal, less than one video fits per 5-hour window: it will pause and continue. Measure it with `ruta retro` on the new account before promising a pace.
- **One route at a time per project.** Mass production is serial.
- Social handles not verified in the apps. AI label per network, unverified (does not apply if there is no realistic AI).

## What requires the owner
1. **Creative process: open, the owner follows it (Nov 4).** Hook, story, speech and what is shown are discussed with the owner until he closes them. See `craft/RECETA-CREATIVA.md`.
2. **Closing:** "Follow me and send it to..." (owner, Nov 4).
3. Offer and prices for a shopping-season topic, if he wants that topic.
4. A permissions list in `.claude/settings.json`, if an approval prompt stops the route.

These are not reminded in every message of this flow; they are said once, on delivery.
