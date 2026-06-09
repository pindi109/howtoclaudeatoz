---
title: "How to Write Your First Prompt in Claude — Beginner's Guide (2026)"
slug: how-to-write-first-prompt-claude
pillar: getting-started
meta_description: "Learn how to write a prompt in Claude that actually works. This beginner's 2026 guide covers structure, length, examples, and common mistakes to avoid."
primary_keyword: "how to write a prompt in Claude"
secondary_keywords:
  - "Claude prompt examples"
  - "writing effective Claude prompts"
  - "Claude prompt tips"
affiliates: []
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "What makes a good Claude prompt?"
    a: "A good Claude prompt is specific, gives Claude a clear role or context, states the desired output format, and includes any constraints upfront. The most common mistake is being too vague — 'Write something about marketing' will produce a generic result, while 'Write a 300-word email to a B2B SaaS prospect who has gone cold, using a consultative tone' will produce something immediately usable."
  - q: "How long should a Claude prompt be?"
    a: "Prompt length should match task complexity. Simple requests (translate this sentence, fix this bug) can be one line. Complex tasks benefit from 3–5 sentences of context: your role, the audience, the format, and the goal. You do not need to write paragraphs for every prompt, but more context almost always produces better results. There is no upper limit — Claude's 200,000-token context window means you can include thousands of words of background."
  - q: "Can I use templates for Claude prompts?"
    a: "Yes. Prompt templates are one of the most effective ways to get consistent results from Claude. A good template includes placeholders for role, task, context, format, and constraints. You can save templates in Claude Projects as custom instructions so they apply automatically to every conversation in that Project. You can also paste a template into any conversation and fill in the blanks."
summary: "Writing an effective prompt in Claude means being specific, giving Claude a clear role and output format, and providing relevant context upfront. This guide walks through the anatomy of a good Claude prompt with real before-and-after examples."
hero_image: "/assets/images/heroes/photo-063-122100378615357116.jpg"
hero_alt: "A vague prompt gets a vague answer — but a few simple habits consistently double the quality of what Claude gives you back."
---

# How to Write Your First Prompt in Claude — Beginner's Guide (2026)

*Last updated: 2026-06-07*

Knowing how to write a prompt in Claude is the single most important skill for getting useful results from any AI assistant. A vague prompt produces a vague answer; a specific, well-structured prompt produces something you can use immediately. The good news is that Claude is forgiving — it does not require a special syntax or elaborate ritual. But a few simple habits will consistently double the quality of what you get back. This guide covers the anatomy of an effective Claude prompt, walks through real good vs. bad examples, and gives you a reusable template for any task.

## What is a Claude Prompt? — Definition

A Claude prompt is any message you send to Claude in a conversation. It can be a question, an instruction, a request for creative work, a block of code you want reviewed, or a document you want summarised. Claude processes your entire prompt — including any files you attach — and generates a response designed to fulfil your intent. The quality of the response is directly shaped by the clarity, specificity, and context of your prompt.

## How to Write a Prompt in Claude — Step by Step

### Step 1: State the Task Clearly in the First Sentence

The most important part of any prompt is the opening sentence. Claude reads your entire message before responding, but a clear opening sentence sets expectations and helps Claude prioritise correctly. Start with the verb: "Write," "Summarise," "Fix," "Explain," "Translate," "Analyse," "List," or "Compare."

**Weak:** "I need something for my presentation."
**Strong:** "Write five bullet-point talking points for a 10-minute investor presentation about a B2B SaaS product in the HR technology space."

### Step 2: Give Claude a Role When It Helps

Assigning Claude a role or persona is one of the most effective prompt techniques. It tells Claude what perspective to write from, what expertise level to assume, and what tone to use. This is especially useful for professional or technical tasks.

**Examples of role assignment:**
- "You are an experienced senior software engineer reviewing a junior developer's code."
- "You are a copywriter specialising in direct response marketing."
- "You are a plain-English legal summariser. Avoid jargon."

Role assignment is not mandatory for every prompt — Claude handles simple requests well without one. Use it when the tone, expertise level, or perspective of the output matters.

### Step 3: Provide Context That Claude Cannot Infer

Claude does not know anything about you, your company, your project, or your audience unless you tell it. Include any context that would change what a good response looks like. Common context elements:

- **Audience:** "This is for a non-technical executive audience."
- **Background:** "We are a small UK-based accountancy firm."
- **Existing work:** "Here is the draft I have written so far: [paste draft]"
- **Constraints:** "Keep it under 200 words. Do not use bullet points."

### Step 4: Specify the Output Format

Claude will default to a sensible format, but telling it explicitly what you want saves editing time. Be specific about length, structure, and style.

| Instead of... | Say... |
|---|---|
| "Write something about this" | "Write a 400-word blog introduction, no subheadings" |
| "Summarise this document" | "Summarise in 5 bullet points, each under 20 words" |
| "Fix my code" | "Fix the bug and explain what was wrong in 2 sentences" |
| "Give me ideas" | "List 10 ideas as a numbered list. One sentence per idea." |

### Step 5: Include Examples When You Have Them

Examples are one of the most powerful context signals you can give Claude. If you want it to match a particular tone, structure, or style, paste an example and say "write something similar to this." If you want it to follow a data format, show one sample row and say "use this format for all entries."

**Example:** "Here is a previous product description we used: [example]. Write a new one for the following product with the same tone: [product details]."

### Step 6: Review and Iterate

Your first prompt will not always produce exactly what you want — and that is fine. Claude is designed for iteration. You can respond to any output with:

- "Make this shorter."
- "The tone is too formal — make it more conversational."
- "Great structure, but replace the second point with [alternative]."
- "Rewrite this from the perspective of the customer rather than the company."

Each follow-up message is itself a prompt. Treat a conversation with Claude as a drafting session, not a one-shot transaction.

## Claude Prompt Examples — Good vs. Bad

### Example 1: Writing Task

**Bad prompt:** "Write an email about our new product."

**Good prompt:** "Write a 150-word launch announcement email for our new project management tool, aimed at small business owners who currently use spreadsheets. The tone should be friendly and direct. Include one clear call to action: 'Start your free 14-day trial.' Do not use exclamation marks."

**Why it works:** The good prompt specifies length (150 words), audience (small business owners using spreadsheets), tone (friendly and direct), a required element (specific call to action), and a constraint (no exclamation marks). Claude can produce a near-finished output from this in one pass.

### Example 2: Coding Task

**Bad prompt:** "Fix my code."

**Good prompt:** "Here is a Python function that is supposed to read a CSV file and return a list of dictionaries. It currently throws a KeyError on line 12. Here is the code: [paste code]. Fix the bug and explain in two sentences what was causing it."

**Why it works:** The good prompt gives Claude the code, the expected behaviour, the specific error, and a clear instruction about the format of the explanation. It will receive a working fix with a brief, clear explanation — not a three-paragraph essay about Python error handling.

### Example 3: Research and Summarisation

**Bad prompt:** "Tell me about electric vehicles."

**Good prompt:** "Summarise the three most important barriers to electric vehicle (EV) adoption in the UK in 2026, focusing on infrastructure and consumer behaviour rather than technology. Write this as a bulleted list, one sentence per point, suitable for including in a business strategy document."

**Why it works:** The good prompt narrows the topic (UK, 2026, infrastructure and consumer behaviour), specifies the number of points (three), the format (bulleted list, one sentence each), and the use case (business strategy document). The output will be immediately usable.

## The Anatomy of a Strong Claude Prompt — Template

You do not need to use every element in every prompt. For complex tasks, this template ensures you have covered the most important variables:

```
[Role]: You are a [describe role/expertise].

[Task]: [Verb] [specific thing] for [purpose].

[Context]: [Relevant background, audience, constraints, existing material].

[Format]: Respond as [format: bullet list, numbered list, prose paragraphs, table, etc.]. 
Length: [word count, number of items, or length guideline].

[Example] (optional): Here is an example of the style/format I want: [example].
```

You can use this template verbatim for any task and fill in the brackets.

## Common Claude Prompting Mistakes to Avoid

- **Too vague:** "Help me with marketing" gives Claude no direction. Add specifics.
- **No format specified:** Claude defaults to prose paragraphs unless you ask for a list, table, or other structure.
- **Forgetting to include relevant material:** If you want Claude to summarise a document, paste or upload the document. Do not expect Claude to find it.
- **Too many goals in one prompt:** If you want Claude to research, write, and format in one go, break it into steps. "First, list 5 key points from this article. Then, using those points, write a 300-word summary." works better than asking for everything at once without structure.
- **Not iterating:** If the first response is 90% right, ask Claude to adjust the 10% that is wrong. You do not need to rewrite the whole prompt.

## Claude Prompt Length — What Works Best

Short prompts (1–2 sentences) work well for simple, clear tasks: "Fix the typos in this paragraph," "Translate this sentence into German," "What does HTTP stand for?" For complex tasks, 3–6 sentences of context produces meaningfully better results. There is no need to write an essay for every prompt, but more relevant context almost always helps. Claude's 200,000-token context window means you can include thousands of words of background — paste entire documents, long code files, or detailed briefs without worrying about fitting within a limit.

## Related Claude Guides

- [What is Claude AI?](/what-is-claude-ai/) — Overview of Claude's capabilities and how to get started
- [Claude Context Window Explained](/claude-context-window-explained/) — Why Claude can handle very long prompts and documents
- [Advanced Prompt Engineering for Claude](/advanced-prompt-engineering-claude/) — Master techniques for complex, multi-step prompts
- [Claude System Prompts](/claude-system-prompts/) — How to set persistent instructions for consistent results
