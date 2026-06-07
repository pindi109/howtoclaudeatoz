---
title: "How to Generate Voiceover Scripts with Claude (2026 Guide)"
slug: claude-voiceover-scripts
pillar: video-voice
meta_description: "Generate professional voiceover scripts with Claude AI in 2026. TTS-optimised writing rules, templates for ads, explainers, and intros, plus ElevenLabs workflow tips."
primary_keyword: "Claude voiceover scripts"
secondary_keywords:
  - "AI voiceover script generator 2026"
  - "text to speech script writing Claude"
  - "Claude TTS script optimisation"
affiliates:
  - elevenlabs
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "Can Claude write voiceover scripts?"
    a: "Yes. Claude writes voiceover scripts for ads, explainer videos, e-learning narration, podcast intros, corporate training, and more. When prompted correctly, Claude writes in a spoken register — short sentences, natural phrasing, and pacing cues — rather than the denser written style that sounds awkward when read aloud by a TTS engine or human voice actor."
  - q: "How do I write a script for text-to-speech?"
    a: "TTS-optimised scripts follow specific rules: sentences should be under 20 words, punctuation should be used to control pacing rather than just for grammatical correctness, numbers should be written as words, acronyms should be spelled as they are spoken, and complex compound sentences should be broken into two. Claude applies all of these rules automatically when you tell it the script is for TTS output."
  - q: "What makes a good voiceover script?"
    a: "A good voiceover script sounds effortless when spoken aloud. It uses the active voice, addresses the listener directly, avoids jargon and abstract language, and places the most important information early in each sentence. Pacing is controlled through punctuation and sentence length rather than word choice. The listener should never have to re-listen to a sentence to understand it."
summary: "Claude generates TTS-optimised voiceover scripts for any format — ads, explainers, e-learning, intros — in minutes. This guide covers the writing rules that make voiceover scripts work, ready-to-use prompt templates, phonetic notation, and how to pair Claude scripts with ElevenLabs for final audio."
---

# How to Generate Voiceover Scripts with Claude (2026 Guide)

*Last updated: 2026-06-07*

Claude voiceover scripts are purpose-built for spoken delivery — optimised for text-to-speech engines and human voice actors alike. The difference between a standard written document and a voiceover-ready script is significant: one sounds natural when spoken, the other sounds like someone reading a report. Claude understands this distinction and applies spoken-word writing rules automatically when prompted correctly. This guide covers those rules, the templates for common voiceover types, phonetic notation techniques, and the ElevenLabs workflow for producing final audio.

## What Makes a Voiceover Script Different from Other Writing?

A voiceover script is heard, not read. The listener has one chance to understand each sentence — they cannot re-read a confusing clause or look up an unfamiliar word. This requires a specific writing style that diverges sharply from standard copywriting or editorial writing.

The core differences:

- **Sentence length:** Voiceover scripts use shorter sentences (12–18 words maximum for most contexts)
- **Sentence structure:** Subject-verb-object is almost always the correct order; no embedded clauses
- **Punctuation as pacing:** Commas, em dashes, and ellipses control breath and emphasis, not just grammar
- **Numbers and symbols:** Write as words ("forty-five percent", not "45%") to ensure correct TTS pronunciation
- **Acronyms:** Spell as spoken ("AI" reads correctly; "HMRC" may need "H-M-R-C" for letter-by-letter reading)
- **Contractions:** Use them — "it's" sounds more natural than "it is" in almost every context
- **Direct address:** Speak to "you" (one listener) not "users", "customers", or "viewers"
- **Vocabulary:** Prefer one-syllable or common two-syllable words over formal equivalents

## TTS-Optimised Writing Rules Claude Applies

When you tell Claude a script is for text-to-speech, it applies the following rules by default:

1. Sentences of 15 words or fewer for the main body
2. No more than one idea per sentence
3. No passive voice
4. No parenthetical clauses
5. Numbers written as words
6. Pause notation: `...` for a deliberate pause, `—` for a breath or beat
7. Emphasis notation: CAPITALISE words the voice should stress (for human actors or TTS with SSML support)
8. Paragraph breaks between topic shifts (ElevenLabs treats paragraph breaks as natural pause points)

Add to any voiceover script prompt: "Write for text-to-speech delivery. Apply spoken-word writing rules: short sentences, no passive voice, numbers as words, add `...` for deliberate pauses."

## How to Write Voiceover Scripts with Claude — Step by Step

### Step 1: Define the Voiceover Brief

Gather the key parameters before prompting Claude:

- **Type:** Ad, explainer, e-learning module, product video, corporate intro, trailer, app tutorial
- **Duration:** 15 seconds, 30 seconds, 60 seconds, 90 seconds, 3 minutes, etc.
- **Audience:** Who will hear this? (Role, age range, prior knowledge level)
- **Tone:** Warm and reassuring / authoritative and direct / energetic and conversational / neutral and informational
- **Key message:** The one thing the listener must take away
- **CTA:** What should the listener do after hearing this?

### Step 2: Use the Voiceover Script Prompt

> Write a [DURATION]-second voiceover script for a [TYPE] about [SUBJECT]. Audience: [AUDIENCE]. Tone: [TONE]. Key message: [MESSAGE]. CTA: [WHAT LISTENER SHOULD DO]. Write for text-to-speech delivery: short sentences under 18 words, no passive voice, numbers as words, add `...` for pause points, and a paragraph break between each section. Total word count should be approximately [WORD COUNT] words (150 words per minute spoken at a moderate pace).

### Step 3: Read Aloud Before Submitting to TTS

Read every Claude voiceover script aloud yourself before sending it to ElevenLabs or another TTS engine. This catches:

- Sentences that require a breath at an unnatural point
- Alliterations or consonant clusters that trip the tongue
- Brand names or product terms that sound wrong when spoken
- Phrasing that needs emphasis in a different place than the natural sentence stress

### Step 4: Add Phonetic Notation for Problem Words

If a word will be mispronounced by a TTS engine, add phonetic guidance. Options:

- **Respelling:** Write the word as it sounds ("Xorbit" → "Zor-bit")
- **Parenthetical pronunciation:** "Our platform, Quorvex (KWOR-vex), handles..."
- **SSML phoneme tags:** For ElevenLabs and most professional TTS, `<phoneme alphabet="ipa" ph="kwɔːrvɛks">Quorvex</phoneme>` forces the correct pronunciation

Ask Claude: "Review this script for words that a TTS engine might mispronounce. List them and provide a respelling or IPA pronunciation guide for each."

### Step 5: Generate Audio in ElevenLabs

Paste the final script into [ElevenLabs](https://elevenlabs.io). Key settings:

- Choose a voice that matches the script's tone (narration voices for explainers, conversational voices for ads)
- Set Stability to 0.55–0.65 for natural variation
- Set Clarity + Similarity Boost to 0.75
- Generate and listen to the full output before downloading
- Re-generate individual sentences if specific lines need adjustment

## Voiceover Script Templates by Type

### 30-Second Ad Script

**Word count target:** 75–85 words

**Structure:** Hook (5s) → Problem or context (8s) → Solution (10s) → Key benefit (5s) → CTA (5–7s)

**Claude prompt:**
> Write a 30-second voiceover script for an advertisement for [PRODUCT/SERVICE]. Audience: [AUDIENCE]. The hook should grab attention immediately — use a relatable problem or a bold claim. Introduce the product in the second sentence. Focus on one key benefit only. End with a specific, low-friction CTA. Write for TTS: short sentences, numbers as words, pause markers.

**Example output structure:**
```
You've been wasting three hours a week on invoicing.

Seriously — three hours.

[PRODUCT NAME] automates the whole process.

Connect your accounts, set your rates... and let it run.

Our users get paid 40% faster and spend a fraction of the time on admin.

Start free today. No credit card needed.
```

### 90-Second Explainer Script

**Word count target:** 220–250 words

**Structure:** Problem (15s) → Introduce solution (15s) → How it works, 3 steps (40s) → Outcome/benefit (15s) → CTA (15s)

**Claude prompt:**
> Write a 90-second explainer video voiceover script for [PRODUCT/CONCEPT]. Audience: [AUDIENCE]. Structure: open with the problem the viewer faces, introduce [PRODUCT] as the solution, explain how it works in 3 clear steps, describe the outcome, and close with a specific CTA. Write for TTS: short sentences, active voice, pause markers `...`, numbers as words.

### E-Learning Module Introduction (60 seconds)

**Word count target:** 140–160 words

**Structure:** Welcome + context (15s) → Learning objectives (20s) → What the learner will be able to do (15s) → Navigation instructions (10s)

**Claude prompt:**
> Write a 60-second introductory narration for an e-learning module titled [TITLE]. Audience: [ROLE/LEVEL]. Include: a brief welcome, the 3 learning objectives for this module (use the stem "By the end of this module, you will be able to..."), and a one-sentence navigation instruction. Warm and encouraging tone. Write for TTS with short sentences and pause markers.

### Corporate Video Intro (20 seconds)

**Word count target:** 45–55 words

**Claude prompt:**
> Write a 20-second corporate video intro for [COMPANY NAME]. The video is about [TOPIC]. Tone: [professional and energetic / calm and trustworthy / innovative and direct]. Include the company name and a one-sentence positioning statement. No clichés. Write for TTS with short sentences.

## Word Count to Duration Reference

| Duration | Word Count (150 wpm) | Word Count (160 wpm — faster pace) |
|---|---|---|
| 15 seconds | 37–38 words | 40 words |
| 30 seconds | 75 words | 80 words |
| 60 seconds | 150 words | 160 words |
| 90 seconds | 225 words | 240 words |
| 3 minutes | 450 words | 480 words |
| 5 minutes | 750 words | 800 words |
| 10 minutes | 1,500 words | 1,600 words |

## Common TTS Problems and Claude Fixes

| Problem | Example | Claude Fix |
|---|---|---|
| Number mispronunciation | "45%" read as "forty-five percent sign" | Ask Claude to write "forty-five percent" |
| Acronym mispronunciation | "FAQ" read as one word | Ask Claude to write "F-A-Q" or "frequently asked questions" |
| Brand name mispronounced | "Xero" read as "zero" | Ask Claude to add "(ZEE-ro)" after first mention |
| Unnatural sentence stress | Stress falls on wrong word | Ask Claude to CAPITALISE the word that should be emphasised |
| Run-on sentences | Voice runs clauses together without pause | Ask Claude to break into two sentences with a pause marker |
| Passive voice sounds flat | "Results are shown in the dashboard" | Ask Claude to rewrite in active voice: "The dashboard shows your results" |

## Related Claude Guides

- [Claude + ElevenLabs Voiceover Workflow](/claude-elevenlabs-voiceover-workflow/)
- [Writing Podcast Scripts with Claude AI](/claude-podcast-scripts/)
- [Claude + Synthesia — Corporate Training Video](/claude-synthesia/)
- [How to Write YouTube Scripts with Claude AI](/claude-youtube-scripts/)
- [Claude for Documentary Scriptwriting](/claude-documentary-scriptwriting/)
