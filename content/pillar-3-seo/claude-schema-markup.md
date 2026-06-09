---
title: "How to Generate Schema Markup with Claude (2026 Guide)"
slug: "claude-schema-markup"
pillar: "seo"
meta_description: "Use Claude to generate JSON-LD schema markup in 2026. Article, FAQ, HowTo, Product, LocalBusiness schema examples, testing tips, and ready-to-use prompts."
primary_keyword: "generate schema markup with Claude"
secondary_keywords:
  - "Claude JSON-LD schema"
  - "AI schema markup generator"
  - "Claude structured data"
  - "FAQ schema Claude"
affiliates: []
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "Can Claude write JSON-LD schema?"
    a: "Yes. Claude generates valid JSON-LD schema markup for all major schema types including Article, FAQ, HowTo, Product, LocalBusiness, Review, BreadcrumbList, and more. Give Claude your page content or key details and it will produce ready-to-paste JSON-LD that you can validate in Google's Rich Results Test before adding to your site."
  - q: "What schema types can Claude generate?"
    a: "Claude can generate any schema type documented on Schema.org. The most SEO-valuable types it handles include: Article, NewsArticle, FAQPage, HowTo, Product, Review, AggregateRating, LocalBusiness, BreadcrumbList, VideoObject, Event, Recipe, and Organization. Claude applies the correct required and recommended properties for each type."
  - q: "How do I test Claude-generated schema?"
    a: "Paste the JSON-LD from Claude directly into Google's Rich Results Test (search.google.com/test/rich-results). This tool validates the schema against Google's requirements and shows you which rich result types your schema qualifies for. Schema.org Validator is a second option for catching structural errors. Fix any warnings before adding the code to your site."
summary: "Claude generates accurate, valid JSON-LD schema markup for any schema type — from FAQ and HowTo to Product and LocalBusiness. This guide covers the most valuable schema types for SEO, example prompts, real JSON-LD outputs, and how to test and implement the results."
hero_image: "/assets/images/heroes/photo-049-122100388773357116.jpg"
hero_alt: "Claude generates valid JSON-LD schema markup — Article, FAQ, HowTo, Product, LocalBusiness — in seconds, ready to paste and test in Google's Rich Results Tool."
---

# How to Generate Schema Markup with Claude (2026 Guide)

*Last updated: 2026-06-07*

Generating schema markup with Claude is one of the most practical and time-saving applications of AI in SEO. Schema markup (structured data) tells search engines exactly what your content is — an FAQ, a product, a local business, a how-to guide — and unlocks rich results in the SERP: star ratings, FAQ dropdowns, step-by-step instructions, and price information. Writing JSON-LD manually is tedious and error-prone. Claude generates accurate, valid schema for any type in seconds, and you can test it immediately with Google's Rich Results Tool. This guide covers every major schema type with example prompts and outputs.

## What is Schema Markup and Why Does It Matter?

Schema markup is structured data added to your HTML that helps search engines understand the content of a page beyond plain text. It uses the Schema.org vocabulary and is typically implemented as JSON-LD (JavaScript Object Notation for Linked Data) — a block of code in the `<head>` or `<body>` of your page.

Schema does two things for SEO:

1. **Enables rich results** — star ratings, FAQ dropdowns, HowTo steps, and product information appear directly in search results, significantly increasing click-through rates
2. **Improves understanding** — even without rich results, structured data helps Google index your content more accurately, which can improve rankings for relevant queries

Claude can generate correct, ready-to-use JSON-LD for all major schema types without requiring you to know the Schema.org specification.

## Schema Types Claude Can Generate

| Schema Type | What It Enables | Best For |
|---|---|---|
| Article | News, blog, article markup | Blog posts, news articles |
| FAQPage | FAQ dropdowns in SERP | Pages with Q&A sections |
| HowTo | Step-by-step instructions in SERP | Tutorial and guide pages |
| Product | Price, availability, rating in SERP | E-commerce product pages |
| Review / AggregateRating | Star ratings in SERP | Reviews, comparison pages |
| LocalBusiness | Business details in knowledge panel | Local service businesses |
| BreadcrumbList | Breadcrumb navigation in SERP | All site pages |
| VideoObject | Video rich results | Pages with embedded video |
| Organization | Brand knowledge panel information | Homepage, About page |
| Event | Event details in SERP | Event listing pages |
| Recipe | Ingredients, time, calories in SERP | Recipe websites |

## How to Generate Schema Markup with Claude — Step by Step

### Step 1: FAQPage schema

FAQPage schema is the highest-value schema type for most content sites. FAQ dropdowns in Google results can double the visual real estate your result occupies.

Prompt:

```
Generate FAQPage JSON-LD schema markup for a page with the following questions and answers.

Page URL: [https://example.com/your-page/]

FAQs:
Q: [question 1]
A: [answer 1]

Q: [question 2]
A: [answer 2]

Q: [question 3]
A: [answer 3]

Output valid JSON-LD that I can add inside a <script type="application/ld+json"> tag.
```

Example output Claude produces:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How much do solar panels cost in the UK?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Solar panels for a typical UK home cost between £5,000 and £11,000 depending on system size. A 3.5kWp system for a 3-bedroom house typically costs £6,000-£8,000 including installation."
      }
    },
    {
      "@type": "Question",
      "name": "How long do solar panels last?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most solar panels come with a 25-year performance warranty and a 10-12 year product warranty. In practice, quality panels last 30-40 years with minimal degradation — typically less than 0.5% output loss per year."
      }
    }
  ]
}
```

### Step 2: HowTo schema

HowTo schema enables rich results showing your step-by-step instructions directly in the SERP, with estimated time and materials.

Prompt:

```
Generate HowTo JSON-LD schema for a page that explains the following process.

Page title: [title]
Page URL: [URL]
Description: [1-2 sentence description of what the guide teaches]
Total time: [e.g. PT30M for 30 minutes]
Tools/materials needed (optional): [list]

Steps:
1. [Step 1 name]: [Step 1 description]
2. [Step 2 name]: [Step 2 description]
3. [Step 3 name]: [Step 3 description]
[continue for all steps]

Output valid JSON-LD.
```

### Step 3: Article schema

Article schema should be added to all blog posts and news articles. It is not always a rich result trigger, but it improves Google's understanding of your content type and authorship.

Prompt:

```
Generate Article JSON-LD schema for the following blog post.

Headline: [article title]
URL: [full URL]
Date published: [YYYY-MM-DD]
Date modified: [YYYY-MM-DD]
Author name: [full name]
Author URL: [author page URL if available]
Publisher name: [website/brand name]
Publisher logo URL: [logo image URL]
Description: [meta description text]
Image URL: [featured image URL]

Use Article type (not NewsArticle). Output valid JSON-LD.
```

### Step 4: Product schema

Product schema with AggregateRating is one of the most visible rich results — star ratings appear under your listing in the SERP.

Prompt:

```
Generate Product JSON-LD schema with AggregateRating for the following product.

Product name: [name]
Description: [1-2 sentence description]
URL: [product page URL]
Image URL: [product image URL]
Brand: [brand name]
Price: [price]
Currency: [GBP / USD / EUR]
Availability: [InStock / OutOfStock / PreOrder]
Average rating: [e.g. 4.7]
Review count: [e.g. 124]

Output valid JSON-LD.
```

### Step 5: LocalBusiness schema

LocalBusiness schema populates Google's knowledge panel with your business details and improves local search visibility.

Prompt:

```
Generate LocalBusiness JSON-LD schema for the following business.

Business name: [name]
Business type: [e.g. Electrician, Restaurant, Dental Clinic — use Schema.org type where possible]
URL: [website URL]
Address: [full postal address]
Telephone: [phone number with country code]
Email: [contact email]
Opening hours: [e.g. Monday-Friday 09:00-17:00, Saturday 10:00-14:00]
Geographic coordinates (optional): latitude [lat], longitude [lon]
Price range: [£ / ££ / £££]
Social profiles (optional): [list URLs]

Output valid JSON-LD.
```

### Step 6: BreadcrumbList schema

BreadcrumbList schema adds the breadcrumb navigation trail to your SERP listing. It is easy to implement and supported on virtually all site types.

Prompt:

```
Generate BreadcrumbList JSON-LD schema for this page.

Breadcrumb trail:
1. Home — [https://example.com/]
2. [Category name] — [https://example.com/category/]
3. [Current page title] — [https://example.com/category/page/]

Output valid JSON-LD.
```

## Testing Claude-Generated Schema

Always validate schema before adding it to your site. There are two tools:

**Google Rich Results Test** — the most important validator. Go to search.google.com/test/rich-results, paste your JSON-LD, and see whether it qualifies for rich results and whether there are any errors. Fix all errors before deploying.

**Schema.org Validator** — validator.schema.org provides deeper validation against the full Schema.org specification. Use this to catch property-level warnings that Google's tool might not flag.

Common errors Claude-generated schema might have (and how to fix them):

| Error | Cause | Fix |
|---|---|---|
| Missing required property | Claude omitted a field Google requires | Ask Claude to add the missing property |
| Invalid URL format | URL missing https:// or contains a typo | Fix the URL in the JSON |
| Price format incorrect | Should be a string e.g. "29.99" not a number | Ask Claude to correct to string format |
| Date format incorrect | Should be YYYY-MM-DD | Correct the date format |

If you get errors, paste the error message back to Claude:

```
The Rich Results Test returned this error for the schema you generated:
"[paste error message]"

Fix the JSON-LD to resolve this error.
```

## Adding Schema to Your Site

There are three ways to add JSON-LD to your pages:

1. **Direct in HTML** — paste the `<script type="application/ld+json">` block into your page template, just before `</head>` or `</body>`
2. **CMS plugin** — WordPress plugins like Yoast SEO, RankMath, or Schema Pro allow you to paste JSON-LD or have built-in schema generators
3. **Google Tag Manager** — add schema as a custom HTML tag, which avoids editing template files

For sites with many pages requiring the same schema structure (e.g. all product pages), ask Claude to generate a template with placeholder variables that your developer or CMS can populate dynamically.

## Related Claude Guides

- [Claude for On-Page SEO Optimisation](/claude-on-page-seo/) — Schema is one part of a complete on-page SEO checklist
- [Claude for Local SEO](/claude-for-local-seo/) — LocalBusiness schema in the context of a full local SEO strategy
- [Claude Meta Titles and Descriptions](/claude-meta-titles-descriptions/) — Complement schema with strong meta tags
- [How to Write SEO Content with Claude](/how-to-write-seo-content-with-claude/) — Writing the content that schema markup enhances
- [Site Audit with Claude](/site-audit-with-claude/) — Identify pages missing schema as part of a full site audit
