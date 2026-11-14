# D · Spend and efficiency of the first video ("phantom half-kilo")

## Summary

- **Measured Claude spend: about 42 USD of API equivalent** (range 37-47), without the later analysis round. It is "equivalent": the owner pays a subscription quota, not USD. Gemini and Codex go separately, by quota, with no price in the tracker.
- **Split:** orchestrator (this chat) 16.4 USD (39 %); agents 25.3 USD (61 %): 15.6 in subagents of this session (outside the engine) and 9.8 in the engine (tasks 53, 54, 61). The campaign (name, resources, ideas) weighed about 3.4 USD; the video alone about 38.4.
- **53 % of the orchestrator's spend is re-reading context:** 43.8 M tokens of cache read in 171 calls (about 256 k per call). It is the cheapest thing to cut: a new chat per video plus a handoff.
- **The three complete drafts cost 7.5 USD** and only the mix of two was used. **The "chat" among many agents is cheap in USD (about 1.9 Claude over 10 stages) but spends about 1.03 M tokens of Gemini/Codex quota for about 1.1 k output tokens** (x1 video).
- **What is not cut:** the art-director model's direction and the "life" pass (5.58 USD plus Argon high) is what the owner called "super incredible" (07:15). Also not: Opus writing the speech, Opus on audio and animation.
- **Proposed pipeline: about 19 USD per video (range 15-25), an estimate.** Savings about 50 % without removing Argon, Opus-speech or Opus-audio.
- **Cap per 5 h window (weak estimate, a single data point):** the terminal's Pro account hit its limit after about 9 USD equivalent of engine in about 4.6 h. On Pro about 1 video per window fits at most, and only if the orchestrator does not share that account.

Conventions: **[measured]** comes from the tracker database or the transcript; **[inferred]** is my reading; **[estimated]** carries an assumption. Prices: those of the tracker's `precios` table (Opus 4/20/0.2/5 and Sonnet 2/10/0.2/2.5 USD per million: input/output/cache read/cache written).

---

## 1. Table by stage

Source: `RETRO.md` (task 54), the tracker's `corridas` (seconds = compute of the runs, not the owner's wait), subagent transcripts. "Passes" = correction rounds according to `ruta.json`/RETRO. USD = Claude only. Gemini/Codex tokens = quota, no price.

### 1a. Inside the engine (task 54)

| Stage | Who (model / effort) | USD Claude | Quota tokens | Compute | Passes | Did it reach the video? |
|---|---|---|---|---|---|---|
| concept | Argon med, Flash low, Opus med | 0.16 | 77 k Google | 96 s | 1 | Yes, v2 (the 35 s v1 was discarded: the owner moved up to 60-90 s) |
| adjustment | Argon, Flash, Sonnet, Opus, Sol low, Terra low | 0.22 | 80 k Google + 223 k ChatGPT | 131 s | 1 | Yes (section 3 was merged with 2) |
| directions | Argon, Flash, Opus | 0.11 | 63 k Google | 59 s | 0 | Partly: 3 styles proposed, a mix of 2 chosen |
| speech (v1) | Opus med (Argon guest), Terra, Sonnet | 0.32 | 20 k + 198 k | 125 s | 1 | No: replaced |
| hook | Argon, Flash, Sol, Opus, Terra | 0.04 | 59 k + 223 k | 106 s | 0 | Discarded: owner 02:23, "the hook does not connect" (ruta.json) |
| hook-2 | Argon, Sol, Sonnet, Opus, Flash, Terra | 0.16 | 59 k + 222 k | 120 s | 0 | Yes |
| scenes (v1) | Argon, Opus | 0.04 | 63 k Google | 65 s | 0 | No: replaced |
| speech-adjustment (v2) | Opus, Argon, Terra, Sonnet | 0.26 | 19 k + 27 k | 96 s | 1 | No: replaced |
| scenes-2 | Argon, Opus | 0.10 | 66 k Google | 84 s | 1 | Yes |
| speech-2 (final) | Opus, Argon, Flash, Terra, Sonnet | 0.45 | 40 k + 28 k | 126 s | 1 | Yes |
| no stage (Argon reviews of the sketch + 1 Argon high) | Argon med x4, Argon high x1, Opus low (grader) | 0.05 | 372 k Google | about 11 min (the high 585 s) | 0 | The Argon high produced `05-DIRECCION-ARGON.md`: yes |
| style (sketch) | Sonnet med, 2 passes | 1.70 | - | 350 s | 2 | Yes, but pass 1 was blind (section 3, #2) |
| storyboard | Opus med | 0.63 | - | 150 s | 0 | Yes |
| animation | Opus med, 1 run | 3.39 | - | 852 s | 0 | Yes, base of the reel |
| sounds | Sonnet med x2 + Opus med x1 (A/B) | 1.12 | - | 262 s (+ wait for the 429) | 0 | Only the Opus version |
| **Engine total** | | **8.75** | **about 919 k Google + 921 k ChatGPT** | **55.7 min of compute** (RETRO notes 298.8 min of clock) | | |

Times between stages [measured, `corridas` timestamps]: concept 01:36Z; adjustment 01:48; directions and speech 01:57-02:00; hook 02:04; hook-2 and scenes 02:25-02:27; speech-2 02:36-02:38. The whole ideas block about 1 h of clock, of which about 15 min is compute and the rest is the owner's wait. Then a gap of 2 h (02:38 -> 04:37) with the drafts (02:01-02:14), the owner's voice (04:02) and the sound decision. Style 04:37-04:43, storyboard 04:47, animation 05:01, sounds 05:02-05:25 (cut by the 429 at about 05:04Z, restart 05:20Z).

### 1b. Outside the engine (subagents of this session; Opus/Sonnet "medium" according to their `meta.json`; in the tracker they are tasks 56-68, origin `claude`)

| Piece | Who | USD | Time | Passes | Did it reach the video? |
|---|---|---|---|---|---|
| Style draft 1 Scale model | Opus med | 2.48 | 11.3 min | 1 | No (the owner chose Pop-up + Tablecloth) |
| Style draft 2 Pop-up | Opus med | 2.64 | 13.0 min | 1 | Yes, as one half of the style |
| Style draft 3 Tablecloth | Opus med | 2.44 | 11.4 min | 1 | Yes, the other half |
| SRT of the Aoede voice | Sonnet med | 0.39 | 1.6 min | 1 | Yes (`voz.srt`) |
| Render of the two versions (A/B) | Sonnet med | 0.51 | 3.3 min | 1 | A and B were a comparison; B (Opus) continued |
| Mix with clean voice | Sonnet med | 0.49 | 2.6 min | 1 | Yes (version C), later superseded by D |
| Life of the world in the reel | Opus med, guided by Argon high | 5.58 | 19.0 min | 1 | Yes: base of the final (version D) |
| Render of the version with life | Sonnet med | 0.42 | 3.3 min | 1 | Yes |
| Speed up final zoom | Sonnet med | 0.18 | 0.5 min | 1 | Yes |
| Phone voice recipe on the real person's take | Opus med | 0.34 | 0.2 min | 1 | Yes |
| Join and add brand mark | Sonnet med | 0.22 | 1.6 min | 1 | Yes (`final/`) |
| **Subtotal** | | **15.6** | | | |

### 1c. What cannot be measured

- **Gemini and Codex:** only quota tokens (Argon, Flash, Sol, Terra). There is no price in the tracker; none was invented. The images in `drafts/imagenes` (Codex/image) have no registered run.
- **Argon's and Flash's effort:** the tracker stores it as null; the cast file says "medium", and there is one "high" run.
- **The owner's wait** (seeing, deciding, speaking): not measured per stage, only inferred from timestamp gaps.
- **Engine changes** (`_ruta.py`, `_taller.py`, tests) made by the orchestrator: their cost is inside the 171 calls of this chat and cannot be separated without reading turn by turn. HANDOFF-15 lists at least "real workshop error", `permite` per stage, A/B in workshop and Argon reviewer on style.
- **Actual plan of each account:** the transcript does not say the plan of the app's account. For the terminal only "Pro" is known, from what the orchestrator checked at 05:09Z.

---

## 2. Orchestrator against agents

Measured with a script over the transcript (last record per `message.id`, without duplicating the 418 streaming lines): **171 assistant messages**, all Opus, medium effort.

| Orchestrator component | Tokens | USD |
|---|---|---|
| New input | 446 | about 0 |
| Output | 240.6 k | 4.81 |
| Cache read | 43.8 M | 8.76 |
| Cache written | 684 k | 3.42 |
| **Total** | | **17.0** (16.4 without the final analysis round) |

By stretch [measured, by UTC timestamp]:

| Stretch | What was happening | Calls | USD |
|---|---|---|---|
| 01:11-01:35 | Campaign: ideas, resources, name | 23 | 2.56 |
| 01:35-02:36 | Concepts, hook, speech in the engine | 40 | 4.50 |
| 02:36-04:00 | Drafts, voice | 11 | 1.06 |
| 04:00-05:35 | Style, animation, sound, 429, A/B render | 61 | 4.75 |
| 05:35-06:45 | Clean audio, plan for the life pass | 14 | 1.44 |
| 06:45-07:50 | Life, touch-ups, closing | 19 | 2.11 |
| 07:50 onward | This analysis round | 3 | 0.57 (excluded) |

**Total cost of the first video** [measured + sums]:

| Block | USD |
|---|---|
| Orchestrator (this chat), production | 16.4 |
| Engine, task 54 | 8.75 |
| Engine, task 53 (campaign room) | 0.85 |
| Engine, task 61 (storyboard Argon/Sol + grader) | 0.20 |
| Subagents of this session | 15.6 |
| **Total** | **about 41.8** |

Margin: +/-12 % from the orchestrator's cache write (if the TTL was 1 h, that line rises about 2 USD: total up to about 44), +/-5 % on agents (they use real `usage`) and the assumption that the tracker's prices are the current ones. **Declared range: 37-47 USD.** It does not include the 4 analysts of this round (about 3.6 USD so far; they are not a cost of the video).

Reading [inferred]: half of this chat's cost is re-reading the same thing. The owner noticed it at the start: "I do not know why the context rose so much" (01:29). The most expensive calls (384 k of cache read in the last one) drag along the campaign, the engine and the video's files in a single thread.

---

## 3. What was unnecessary spend and what was unrepeatable exploration

Costs in Claude. "Avoidable" is [estimated] and says with what assumption.

| # | Finding | Evidence | USD spent | Avoidable (est.) | What the factory does differently |
|---|---|---|---|---|---|
| 1 | **Three complete animated drafts** (11-13 min, 15-17 turns and about 1.7-2.0 M of cache read each); one entirely discarded | tasks 56-58; owner 02:23: "The ones I liked most were the pop-up and the tablecloth collage"; in the same intervention, the motion pleased him but made him dizzy (ruta.json, "hook" decision) | 7.5 (Scale model 2.48 unused) | about 5, if the style is chosen with 3 still images and a single short camera draft | Choose style with stills (Argon + image). Keep **one** animated draft of 5-8 s, because the defect the owner detected was motion sickness, and that is not seen in an image (x1) |
| 2 | **Sonnet "blind" sketch**: in pass 1 it could not see its own sheet (permissions problem), run 396 | Orchestrator 04:44: "worked without being able to see its sheet, because of the permissions problem"; tracker: 396 = 0.87 USD, 1.6 M of cache read, cache/output ratio 71x (the highest of the video) | 0.87 (+ 0.84 of pass 2, useful) | 0.87 | The root is a workshop permission, not the model. Before any visual stage, check that the agent can open the image. The owner had already asked "shouldn't the review be done by Argon?" (04:25) |
| 3 | **The same content fault corrected three times**: saying that the increase "stays / did not go down" | `ruta.json` reviews: speech, speech-adjustment and speech-2 say CHANGE for the same thing (the study only says the average was not lost in the following year). Also concept flagged "~1.8 kg" as our own sum (x3 the data fault) | 0.32 + 0.26 + 0.45 = 1.03 | about 0.5 and 3 reviewer passes | Put the data's limit ("195 adults in the US, average, was not lost in the following year, does not predict each person") in the speech brief from v1. It is the N1 rule "limits travel in the brief" (REGLAS.md) |
| 4 | **Audio chain with the wrong recipe**: A/B sounds + A/B render + clean mix. The audio came out flat, "as if recorded on a phone" (owner 05:55); the phone recipe is for a real person on camera, not for an animated world | Owner 05:55; HANDOFF-15: "phone recipe only for a person on camera" | 1.12 + 0.51 + 0.49 = 2.12 | about 1.3 (only Opus + clean voice + one render) | Clean voice by default in animated worlds; phone only if there is a take of a person. Drop the Sonnet version of the A/B, already resolved (section 5) |
| 5 | **Chat among many agents in the ideas stages** | Tracker: 6 Flash low runs (113 k tokens, output 60-84 each), 6 from Terra (844 k tokens, output 44-72; three with about 193 k input for about 60 tokens of answer), 3-4 from Sol low (78 k; output 63-115). Total about 1.03 M of quota for about 1.1 k output tokens | 1.86 Claude over 10 stages + 1.03 M of quota | about 1.0 Claude and almost all the quota | [inferred] They look like reviewers or watchers; I do not know what decision they changed. Keep one per stage (book check with Sonnet) and send it only what it reviews, not 193 k of context. Measure once whether Terra/Flash change anything; if not, remove them |
| 6 | **Duplicated context in every chat agent** | The 25 team runs rewrite 12-24 k tokens of cache per call (about 1.9 of the engine's 8.75 USD); Argon medium resends about 19 k of input in each of its 25 runs (about 475 k of 507 k tokens) | about 1.9 USD + 475 k tokens | about 1.2 | One compact context file per stage (the `_COMUN.md` of rule N1), not the whole kit in each turn |
| 7 | **Double rounds**: speech v1/v2/final, hook and hook-2, scenes and scenes-2 | RETRO | 1.1 of the 1.86 USD of ideas | about 0.8 | Merge hook + scenes + speech in one pass with the data limit written; one single book review |
| 8 | **Orchestrator re-reading context** | 8.76 USD of cache read; the owner asked to compact at 01:29 | 8.76 | about 4-5 [estimated: average context of 100 k instead of 256 k] | New chat per video, with handoff and a summary of <= 10 lines; the orchestrator does not drag along HTML or images (N1 rule "does not read long material") |
| 9 | **Wait for the 5 h limit (429)** | Orchestrator 05:04: "We hit your 5-hour limit"; start scheduled at 11:22 pm (05:22Z) | about 20 min of clock and 5 diagnostic messages | 20 min | See 4b: split across accounts, do not launch on the full account |
| 10 | **The animation is done twice** (base + life) | animation 3.39 + life 5.58 = 8.97 | 8.97 | about 2 [estimated: less re-reading of the HTML if Argon's direction comes in before animating] | **It is not removed**; it is moved earlier: Argon directs the life before Opus animates, a single pass |

**Unrepeatable exploration (the next video does not pay for it)** [inferred, x1 video]:
- Campaign: name, resources 1-5, method, task 53: about 3.4 USD.
- The scene's technical scaffolding (travelling camera, 195 instanced little figures, subtitles, render to MP4, `ruidos.py`, clean-voice recipe, SRT). They are pieces with reusable scripts; I estimate about 1/3 of the animation and sound cost (about 3 USD) was scaffolding that now exists.
- Discovering that there are two accounts (app and terminal) and what limit each has.
- The sound A/B (Opus beats Sonnet): it is a data point, no longer paid for.
- Engine changes: cost not separable (1c).

Pure repetition, not exploration: points 2, 3, 4, 6, 7 and 8.

---

## 4. Cheaper pipeline, keeping quality

### 4a. Changes by stage

| Today (10 ideas stages + style + storyboard + animation + sounds + 3 drafts + A/B + life) | Proposal | Who and effort | USD Claude [estimated] |
|---|---|---|---|
| concept, adjustment, directions, hook, hook-2, scenes, scenes-2, speech, speech-adjustment, speech-2 | **3 stages:** (1) concept + 3 hooks + directions, Argon, with the owner's approval; (2) scenes + speech in one pass, **Opus writes the speech, Argon as guest** (the owner's rule FALLA 49) with the data limit in the brief; (3) one book review | Argon med, Opus med; Sonnet med only for the rule-by-rule check | 1.0 |
| 3 animated drafts | **3 still images** of style (Argon + image) and **one** short animated draft to validate the motion | Argon + Opus med | 1.5 |
| style (Sonnet sketch, 2 passes) | A fixed sketch directly in Opus, reviewed by Argon before continuing (owner 04:25) | Opus med + Argon reviewer | 1.2 |
| storyboard | Same | Opus med | 0.6 |
| animation + life (two passes) | **A single pass**: the direction of Argon high ("life") comes in before animating | Argon high directs, Opus med builds | 6.5-7.0 |
| A/B sounds + A/B render + clean mix | **A single sound** from Opus + clean voice by default + one render | Opus med (sound), Sonnet med (ffmpeg) | 1.1 |
| touch-ups (zoom, recipe, brand mark) | Fixed scripts; Sonnet only if something is missing | Script / Sonnet | 0.4 |
| voice | Same: text to the owner -> AI Studio -> audio; SRT by script | Owner + script | 0 |
| final review | Argon reviews the final MP4 (today nobody did: HANDOFF-15 "Argon did not review the version with life") | Argon med | 0 |
| Orchestrator | New chat per video, handoff of <= 10 lines, long reads to Sonnet | Opus med | 6-8 |
| **Total** | | | **about 19 (range 15-25)** |

Assumptions: animation and sound at measured cost (3.39 and 0.62) plus about 3.0 for integrating the life in the same pass (half of the 5.58, because it no longer re-reads or rebuilds the HTML); orchestrator in about 100 calls with about 100 k of average context (about 0.07 USD per call) instead of 171 calls with 256 k (about 0.096); Argon and Codex are not charged in USD. If the owner keeps approving many stages, the orchestrator rises and hardly goes below about 10.

Against the measured (about 38.4 for the video without campaign) it is **about -50 %**. What remains is what makes the quality: Opus animating, Argon directing, Opus on audio.

### 4b. Cap per 5-hour window [weak estimate, a single data point]

- **Measured data:** between 00:29Z and 05:02Z the engine runs (terminal account: teams, workshop, grader) added up to about 9.0 USD equivalent (about 8.4 M tokens of cache read). At 05:04Z the 429 arrived, with a restart at 05:20Z ("Released at 11:20 pm", orchestrator).
- **Reading [inferred, x1]:** a Pro window withstands at least about 9 USD of this type of work (Opus/Sonnet with a lot of cache read). It is a minimum: the 429 may have arrived adding other uses of that account that I do not see.
- **With the proposed pipeline**, what runs in the engine (everything except the orchestrator) costs about 12 USD. It does not fit in a Pro window: about 0.75 video per window. The orchestrator must stay on the other account (the app's, which did not hit its limit: owner 05:08, "my quota at 17 %").
- **For the owner's new account** the plan is unknown. If it were Max, a rule of three with caps of 45 USD (5x) and 180 USD (20x) would give about 2-3 and about 9 videos per window if everything runs on that account (about 19 USD per video). It is arithmetic over a single data point and over multipliers I did not verify: **measure the first video on the new account with the same transcript script before promising a mass-production pace.**
- **Measured lever:** long agents fill the limit. On the terminal account, the 5 `taller` (workshop) runs weighed 5.9 of the 9.0 USD (the animation alone, 3.39). Split: heavy Opus on one account, orchestrator and touch-ups on the other, or launch the animation when a new window opens.

---

## 5. Risks of making it cheaper: where not to cut

| What not to touch | Evidence | Risk if cut |
|---|---|---|
| **Opus's speech with Argon as guest** | Cast rule (FALLA 49); owner in ruta.json: "Simple words and the first 3 seconds are the most important"; 02:33 he approved the corrections: "Very good analysis, congratulations" | Moving it to Sonnet or leaving it to Argon alone breaks a fixed rule of the owner. The speech is the only thing that can no longer be corrected once the voice is recorded |
| **Opus on audio** | Owner 05:55: "the final version will then be Opus's, which is 200 % better"; 04:09: "Audio is super, super important" | The A/B was already measured (x1, by the owner's ear). Moving to Sonnet saves about 0.3-0.5 USD and risks what the owner cares about most. The repetition is cut, not the model |
| **Argon's direction + life pass** | Owner 06:45: "I super super love it"; 07:15: "It came out super, super, super incredible" | That is where perceived quality rose. The saving is in moving it earlier, not in removing it |
| **Argon as reviewer** | Owner 04:25: "Shouldn't the review be done by Argon?" | Without a visual reviewer the broken sketch returns (month posters in profile, a cut-off turkey) |
| **Opus animating, in a single pass** | Owner 04:31-04:34 ruled out 5 parallel agents because of the risk of cuts and cost; 04:43: "why is Sonnet animating?" | Sonnet on style met the list but "does not think like a director" (orchestrator 04:44, x1). Splitting the animation risks cuts between scenes |
| **One short animated draft** | Owner: the motion makes him dizzy (ruta.json, "hook" decision) | Choosing style with still images alone does not detect the motion sickness, which was the main defect of the drafts [inferred] |
| **Clean voice in animated worlds** | Owner 05:55: the echo "breaks the aesthetics a lot" | Using the phone recipe outside a take with a person repeats the rework |

Risks of the cuts themselves [inferred]:
- Merging ideas stages removes control points. Keep the owner's three stops (concept/hooks, speech, sketch) and remove the intermediate ones.
- Turning off the Terra/Flash reviewers without measuring them may remove a useful filter. There is no data on what they changed (outputs of 44-115 tokens). I propose turning them off on the next video, keeping the book check with Sonnet and comparing the CHANGEs.
- The savings of section 4 come from a single video. They must be checked with the same measuring script on the second one.

---

## How it was measured (to repeat it)

- Tracker: `registro/marcador.db`, read-only; tables `corridas`, `etapas`, `precios`; tasks 53, 54, 56-68.
- Transcript: every `type=assistant` line was read, the last record of each `message.id` was taken (streaming lines are duplicated) and `usage` was multiplied by the tracker's price table. Subagents in `.../subagents/agent-*.jsonl`, with `meta.json` (model and effort).
- Script: a temporary one (the factory should keep a copy in its tools folder).
- Limitation: Gemini and Codex are in quota tokens, with no conversion to USD.
