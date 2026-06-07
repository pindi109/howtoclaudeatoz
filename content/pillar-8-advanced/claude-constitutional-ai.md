---
title: "How Claude's Constitutional AI Works — Technical Guide (2026)"
slug: claude-constitutional-ai
pillar: "advanced"
meta_description: "A technical guide to Claude's Constitutional AI: how it works, what the constitution contains, how it shapes refusals, and how it compares to RLHF. Updated 2026."
primary_keyword: "Claude Constitutional AI"
secondary_keywords:
  - "how Constitutional AI works"
  - "Claude training methods"
  - "Constitutional AI vs RLHF"
affiliates: []
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "What is Constitutional AI?"
    a: "Constitutional AI (CAI) is a training method developed by Anthropic in which an AI model is trained to evaluate and revise its own outputs according to a set of explicit principles — a 'constitution.' Instead of relying solely on human raters to label harmful outputs, CAI uses the model itself (and a separate 'critic' model) to identify responses that violate the principles, then generates revised versions. The final model is trained on these self-improved outputs, learning to internalise the constitutional principles."
  - q: "How does Claude decide what to refuse?"
    a: "Claude's refusals are not the result of a keyword filter or a simple blocklist. They emerge from values and judgement internalised during training. Claude weighs the potential harms of a response against its potential benefits, considers the likely intent behind a request, and assesses whether providing information would meaningfully enable harm beyond what is freely available. Borderline cases are genuinely evaluated in context — the same question might get a different response depending on how it is framed and what context the user has provided."
  - q: "Is Constitutional AI better than RLHF?"
    a: "Anthropic's research suggests CAI produces models with more consistent, principled safety behaviour than RLHF alone — and does so without requiring human raters to read and label large volumes of potentially harmful content. RLHF is better at aligning model outputs to general human preferences (tone, style, helpfulness), but it depends on the consistency and values of human labellers. Constitutional AI adds a layer of explicit, transparent principles that can be audited and refined. Most state-of-the-art AI models, including Claude, use both CAI and RLHF in combination."
summary: "Constitutional AI is Anthropic's method for training Claude to internalise explicit safety principles rather than relying purely on human feedback labels. This guide explains the full CAI pipeline — from principles to self-critique to training — and how it produces Claude's characteristic approach to safety and helpfulness."
---

# How Claude's Constitutional AI Works — Technical Guide (2026)

*Last updated: 2026-06-07*

Claude's Constitutional AI is the training methodology that defines how Claude reasons about safety, helpfulness, and harm — and it is fundamentally different from the RLHF approach used by most other large language models. Understanding Claude Constitutional AI is important for anyone who wants to understand why Claude behaves the way it does, why it refuses certain requests, and why it is often more nuanced in its responses than models trained purely on human preference labels. This guide covers the full technical pipeline, what the "constitution" actually contains, and how CAI compares to alternative alignment approaches.

## What is Constitutional AI?

Constitutional AI (CAI) is a technique published by Anthropic researchers in 2022 and used in training all versions of Claude. The core idea: instead of relying exclusively on human labellers to identify harmful or unhelpful model outputs, use the model itself to evaluate and improve its responses according to a set of explicit principles.

The analogy to constitutional law is deliberate. A constitution defines foundational principles that all behaviour should be consistent with. In CAI, these principles form a written document — the "constitution" — that guides how the model evaluates its own outputs during training.

The key insight is that this approach:

1. Scales without requiring human labellers to read potentially harmful content at volume
2. Makes the safety principles explicit and auditable (unlike RLHF, where the "values" exist implicitly in labeller decisions)
3. Produces more consistent safety behaviour because it is grounded in principles rather than pattern-matching on labeller preferences

## The Constitutional AI Training Pipeline

CAI has two main phases:

### Phase 1: Supervised Learning from AI Feedback (SL-CAI)

**Step 1 — Generate responses to harmful prompts.** A "red-team" dataset of prompts is created — prompts designed to elicit harmful, dangerous, or unethical responses from the model.

**Step 2 — Model produces initial responses.** The model generates responses to these prompts without any safety filtering. Many responses will be harmful.

**Step 3 — Self-critique.** The model is then prompted to critique its own response according to a randomly sampled constitutional principle. For example:

```
Critique: Identify specific ways in which the assistant's last response is harmful, 
unethical, racist, sexist, toxic, dangerous, or illegal.
```

**Step 4 — Revision.** The model is then prompted to revise its response:

```
Revision: Please rewrite the assistant response to remove any and all harmful, 
unethical, racist, sexist, toxic, dangerous, or illegal content.
```

**Step 5 — Training.** The model is fine-tuned on the revised (improved) responses. This teaches it to produce the revised version rather than the original harmful version.

### Phase 2: Reinforcement Learning from AI Feedback (RLAIF)

In standard RLHF, human labellers compare pairs of model responses and indicate which is better. This is expensive, slow, and introduces human inconsistency. In RLAIF (the second phase of CAI), the preference labelling is done by a "feedback model" — a separate AI that has been shown the constitutional principles.

**Step 1 — Generate response pairs.** The SL-CAI model produces two different responses to the same prompt.

**Step 2 — AI preference labelling.** The feedback model evaluates both responses according to constitutional principles and selects which is more helpful, harmless, and honest.

**Step 3 — Reward model training.** A reward model is trained on these AI-generated preference labels.

**Step 4 — RL fine-tuning.** The policy model is fine-tuned using PPO (Proximal Policy Optimisation) to maximise the reward model's scores.

The result is a model trained to prefer outputs that the constitutional principles indicate are better — without requiring human labellers to evaluate potentially harmful content.

## What Is in Claude's Constitution?

Anthropic has published research describing the types of principles included in Claude's constitution. They fall into several categories:

**Harm avoidance principles:**
- Do not help with the creation of weapons capable of mass casualties
- Do not produce content that sexually exploits minors
- Do not provide information that primarily serves to harm individuals
- Do not produce content designed to deceive users in ways that damage their interests

**Helpfulness principles:**
- Be genuinely helpful rather than reflexively cautious
- Do not add unnecessary caveats that reduce the usefulness of responses
- Do not refuse reasonable requests by citing possible but highly unlikely harms
- Treat users as intelligent adults capable of determining what is good for them

**Honesty principles:**
- Do not claim to be human when sincerely asked
- Do not assert things you believe to be false
- Acknowledge uncertainty rather than confabulating confident answers
- Do not create false impressions through technically true but misleading statements

**Value conflict resolution principles:**
- When privacy and safety conflict, err towards safety
- When user autonomy and harm prevention conflict, give significant weight to autonomy for actions affecting only the user
- When institutional authority and ethical principles conflict, ethical principles take precedence

The specific wording and weighting of these principles has evolved across Claude versions. Anthropic's published model cards and research papers provide the most current descriptions of the principles in use.

## How Constitutional AI Shapes Claude's Responses

### The Calibrated Refusal Approach

Because Claude has internalised principles rather than a blocklist, its refusal behaviour is contextually calibrated. The same question can receive different responses depending on context:

- "How do household chemicals create toxic gases?" → Claude will typically answer this because safety information is widely available and the question is more often asked for harm prevention than harm causation.
- "Give me step-by-step instructions to poison my neighbour" → Clear malicious intent transforms the same chemical knowledge into something Claude will refuse to provide.
- "I'm a nurse and need to understand overdose thresholds" → Stated professional context shifts Claude's assessment of the population of people likely to be asking this question.

This is not perfect. Claude can be wrong in both directions — sometimes refusing benign requests and sometimes missing genuinely malicious ones. But the contextual calibration makes it categorically different from keyword-based safety systems.

### The "Thoughtful Senior Anthropic Employee" Test

Anthropic's guidance to Claude includes a heuristic: imagine how a thoughtful, senior Anthropic employee would react if they saw your response. This person cares deeply about safety but also finds unnecessary refusals and excessive moralising frustrating. A response that refuses a reasonable request by citing highly unlikely harms would concern this person just as much as a response that provides genuine assistance with harm.

This framing is significant: it means Claude's training explicitly penalises over-refusal and excessive caution, not just harm. The goal is calibrated helpfulness, not maximum restriction.

### Hardcoded vs Softcoded Behaviours

Constitutional AI produces two types of safety behaviour:

**Hardcoded (absolute):** These are the "bright lines" Claude will not cross regardless of instructions — producing CSAM, providing detailed synthesis routes for biological or chemical weapons, undermining oversight mechanisms for AI. These are behaviours where Anthropic has determined that no legitimate use case justifies the risk, so they are absolute.

**Softcoded (configurable):** These are defaults that can be adjusted by operators (via system prompts) or users (in conversation). For example, Claude defaults to not producing explicit sexual content, but adult content platforms can unlock this via Anthropic's operator permissions. Claude defaults to adding safety caveats on certain topics, but operators can reduce this for professional contexts.

## Constitutional AI vs RLHF — Technical Comparison

| Aspect | RLHF | Constitutional AI (CAI) |
|---|---|---|
| Feedback source | Human labellers | AI model guided by principles |
| Principles | Implicit in labeller preferences | Explicit, written, auditable |
| Scalability | Limited by human labeller capacity | Scales with compute |
| Consistency | Varies with labeller pool and training | More consistent across similar inputs |
| Transparency | Low — values live in labeller decisions | High — principles can be inspected |
| Harm to labellers | Labellers exposed to harmful content | Model, not human, processes harmful content |
| Use in Claude | Yes (combined with CAI) | Yes (primary alignment method) |
| Use in GPT-4 | Yes | Partial (some constitutional elements) |
| Use in Gemini | Yes | Partial |

Claude uses both RLHF and CAI. RLHF trains the model to be helpful and respond well to general human preferences (tone, style, format). CAI provides the principled safety layer. The two methods are complementary.

## Why Constitutional AI Matters for Developers

**Predictable boundaries:** Because Claude's behaviour emerges from principles, developers can reason about where the edges are. The question to ask is not "what keywords will trigger a refusal?" but "does this request violate Claude's constitutional principles?" The latter is more predictable.

**Operator configuration:** Anthropic's operator system lets businesses adjust Claude's default softcoded behaviours via system prompts. This works because the underlying principles accommodate context — they distinguish between a medical professional asking about drug doses and an anonymous user with no context.

**Jailbreak resistance:** Constitutional AI produces more robust refusal behaviour than safety measures applied as a post-processing filter. The safety principles are embedded in the model's weights, not sitting on top of an otherwise unconstrained model.

**Research reproducibility:** Because the principles are published, researchers can study the relationship between the stated principles and Claude's actual behaviour, identify inconsistencies, and contribute to improving alignment techniques.

## Limitations of Constitutional AI

**Principle conflicts:** When two constitutional principles conflict (user autonomy vs harm prevention), the resolution is not always obvious and can be inconsistent across similar inputs.

**Training distribution gaps:** CAI works on the scenarios covered in the training red-team dataset. Novel adversarial prompts that were not anticipated may not trigger the appropriate constitutional reasoning.

**Over-refusal on ambiguous cases:** Claude can be more cautious than necessary on topics that are adjacent to but not actually violating any principle. This is a calibration problem that Anthropic continues to work on.

**Opacity of the constitution's full contents:** While Anthropic has published significant detail, the exact wording, weighting, and completeness of the current production constitution is not fully public.

## Related Claude Guides

- [Claude Safety Features Explained](/claude-safety-features/)
- [Advanced Prompt Engineering with Claude](/advanced-prompt-engineering-claude/)
- [Claude System Prompts — How to Use Them](/claude-system-prompts/)
- [The Future of Claude — What's Coming in 2026](/future-of-claude-2026/)
- [Claude Opus vs Sonnet vs Haiku — Full Model Breakdown](/claude-opus-vs-sonnet-vs-haiku/)
