---
title: "Writing Meta Titles and Descriptions with Claude (2026 Guide)"
slug: "claude-meta-titles-descriptions"
pillar: "seo"
meta_description: "Use Claude to write SEO-optimised meta titles and descriptions at scale. Prompts, templates, character count rules, and batch generation workflows included."
primary_keyword: "meta titles and descriptions with Claude"
secondary_keywords:
  - "Claude write meta descriptions"
  - "AI meta title generator"
  - "SEO meta tags Claude"
  - "batch meta description generation"
affiliates: []
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "Can Claude write meta descriptions?"
    a: "Yes. Claude writes high-quality meta descriptions that include the target keyword, a clear value proposition, and a call to action — all within the 150-160 character limit. You can generate meta descriptions one at a time or in batches of 20-50 pages using a simple structured prompt."
  - q: "How long should a meta description be?"
    a: "Google typically displays 155-160 characters of a meta description on desktop and around 120 characters on mobile. The practical target is 150-158 characters — long enough to include keyword, benefit, and CTA without getting cut off. Claude can be instructed to hit this range precisely."
  - q: "Does Claude know SEO best practices for titles?"
    a: "Yes. Claude knows that meta titles should be 50-60 characters, include the primary keyword near the start, avoid keyword stuffing, use power words or numbers where appropriate, and match the search intent of the target keyword. It applies these rules automatically when you give it the right context in your prompt."
summary: "Claude can write SEO-optimised meta titles and descriptions individually or in batches of 50+ pages. This guide covers character count rules, prompt templates, batch generation workflows, and examples of strong versus weak meta copy."
hero_image: "/assets/images/heroes/photo-051-122100387855357116.jpg"
hero_alt: "A well-written meta description can increase click-through rate by 5–30% — and Claude can generate them at scale, in bulk, with correct character counts baked in from the start."
---

# Writing Meta Titles and Descriptions with Claude (2026 Guide)

*Last updated: 2026-06-07*

Writing meta titles and descriptions with Claude is one of the fastest wins in SEO. Meta tags are short, rule-bound, and repetitive — exactly the type of task where AI excels. Claude knows the character limits, understands keyword placement, and can match tone of voice across dozens of pages in a single prompt. Whether you need one meta description for a new article or need to rewrite 200 tags for an existing site, Claude handles it accurately and quickly. This guide covers the rules Claude applies, the prompts that produce the best output, and a batch generation workflow for large sites.

## What Are Meta Titles and Descriptions — and Why Do They Matter?

A **meta title** (also called a title tag) is the clickable blue headline in Google search results. It is the single most important on-page SEO element after the content itself — Google uses it to understand what the page is about and users use it to decide whether to click.

A **meta description** is the grey paragraph below the title in search results. Google does not use it as a direct ranking factor, but it directly affects click-through rate (CTR), which in turn affects your rankings. A well-written meta description can increase CTR by 5-30% compared to a generic or truncated one.

Claude understands both of these elements and the rules that govern them.

## Character Count Rules Claude Follows

| Element | Ideal Length | Max Before Cut-Off | Key Rule |
|---|---|---|---|
| Meta title | 50-60 characters | 60 characters (desktop) | Primary keyword in first 3 words |
| Meta description | 150-158 characters | 160 characters (desktop) | Include keyword + benefit + CTA |
| Title — mobile | 40-55 characters | ~55 characters | Shorter is safer for mobile-first |
| Description — mobile | 110-120 characters | ~120 characters | Front-load the key benefit |

When you instruct Claude to write meta tags, always specify the character limit explicitly. Claude will respect it, but only if you ask.

## How to Write Meta Titles and Descriptions with Claude — Step by Step

### Step 1: Single-page meta tag generation

For a single page, use this prompt structure:

```
Write an SEO-optimised meta title and meta description for the following page.

Page type: [blog post / product page / category page / landing page]
Primary keyword: [keyword]
Secondary keywords: [optional]
Page topic: [1-2 sentence summary of the page content]
Target audience: [who is searching for this]
Tone of voice: [professional / conversational / urgent / etc.]

Rules:
- Meta title: 50-60 characters, primary keyword in first 3 words
- Meta description: 150-158 characters, include keyword, a specific benefit, and a call to action
- Do not use clickbait or misleading language
- Write in British English

Output format:
Title: [title here] ([X] chars)
Description: [description here] ([X] chars)
```

### Step 2: Generate 3-5 variations for A/B testing

For high-traffic pages, generating multiple options and testing them is worth the extra effort:

```
Write 3 variations of the meta title and 3 variations of the meta description for this page.

[paste page brief from above]

For each variation, note the different angle being used (e.g. benefit-led, question-led, data-led).
```

### Step 3: Batch generation for multiple pages

For a site audit or content migration, batch generation saves hours. Structure your input as a table and ask Claude to process each row:

```
Write meta titles and descriptions for the following pages. Apply SEO best practices to each: keyword near the start of the title, benefit and CTA in the description, correct character counts.

| URL Slug | Primary Keyword | Page Topic Summary |
|---|---|---|
| /solar-panels-cost/ | solar panels cost UK | Guide to solar panel costs for UK homeowners |
| /best-solar-panels/ | best solar panels UK | Comparison of top solar panel brands in UK |
| /solar-installation-guide/ | solar panel installation | Step-by-step guide to installing solar panels |

Output as a table: Slug | Meta Title (chars) | Meta Description (chars)
```

Claude can process 20-50 pages per prompt reliably. For larger sites, split into batches of 30-40 rows and maintain a consistent tone brief at the top of each batch.

### Step 4: Review and adjust for brand voice

After Claude generates the tags, review them for:

- Brand name inclusion (add "[Brand] |" at the end of titles if your style requires it)
- Consistency of tone across pages
- Any titles that exceed 60 characters — Claude occasionally runs slightly long
- Descriptions that do not include a clear CTA

Use a follow-up prompt to fix any issues:

```
The following meta descriptions are too long or lack a clear CTA. Rewrite each one to be 150-158 characters and end with an action phrase.

[paste the specific tags that need fixing]
```

### Step 5: Rewrite existing poor-performing tags

If you have pages with low CTR in Google Search Console, use Claude to rewrite them:

```
These meta titles and descriptions are underperforming (low CTR in Search Console). Rewrite each one to be more compelling while keeping the primary keyword.

Current title: [title]
Current description: [description]
Primary keyword: [keyword]
Average position: [position]
Current CTR: [CTR]

Suggest 2 new titles and 2 new descriptions. Explain the change you made to each.
```

## Good vs. Weak Meta Tags — Examples

| | Meta Title | Meta Description |
|---|---|---|
| **Weak** | Solar Panels (58 chars) | We sell solar panels for homes and businesses. Contact us today for more info about our range. | 
| **Strong** | Solar Panel Costs UK 2026 — Full Price Guide (46 chars) | Find out exactly how much solar panels cost for a UK home in 2026. Compare brands, grants, and payback periods. Get your free quote. (134 chars) |
| **Weak** | About Our Services | Learn about the services we provide to customers in various industries across the country. |
| **Strong** | Construction Project Management Software — Free Trial (54 chars) | Manage timelines, budgets, and teams on one platform built for construction. Trusted by 2,000+ project managers. Start free today. (131 chars) |

The strong examples share three qualities: they include the keyword naturally, they state a specific benefit, and they end with a clear next action.

## Claude Meta Title Rules — Cheat Sheet

**Do include:**
- Primary keyword in the first 3 words
- A number or year where relevant (e.g. "2026", "10 Best")
- A power word where it fits naturally (e.g. "Complete", "Free", "Proven")
- Your brand name at the end for branded pages

**Do not include:**
- Keyword repetition ("Solar Panels — Best Solar Panels UK Solar")
- All caps
- Symbols that look spammy (!!!,  →→→)
- Vague phrases ("Welcome to our website", "Find out more")

## Automating Meta Tags at Scale

For sites with hundreds or thousands of pages, consider building a Claude-powered workflow using the API. You can feed Claude a CSV of page data — URL, primary keyword, page title, category — and receive back a CSV of optimised meta tags. This is particularly valuable for:

- E-commerce sites with large product catalogues
- News or blog sites where every new post needs a meta description
- Site migrations where you want to refresh all meta tags

The prompt structure is the same as the batch method above, just automated via the API rather than copy-pasted manually.

## Related Claude Guides

- [Claude for On-Page SEO Optimisation](/claude-on-page-seo/) — Meta tags are one part of on-page SEO; this guide covers the full checklist
- [How to Write SEO Content with Claude](/how-to-write-seo-content-with-claude/) — Writing the full article to go with your optimised meta tags
- [Claude Schema Markup](/claude-schema-markup/) — Add structured data to complement your meta tag optimisation
- [Building a Content Strategy with Claude](/building-content-strategy-with-claude/) — Plan the pages that will need meta tags written
- [Site Audit with Claude](/site-audit-with-claude/) — Identify which existing pages have missing or poor-quality meta tags
