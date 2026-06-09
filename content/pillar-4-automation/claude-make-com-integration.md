---
title: "Claude + Make.com — Complete Integration Guide (2026)"
slug: claude-make-com-integration
pillar: automation
meta_description: "Learn how to integrate Claude AI with Make.com in 2026. Build no-code automations that use Claude to write, classify, summarise, and respond — step by step."
primary_keyword: "Claude Make.com integration"
secondary_keywords:
  - "Claude AI automation"
  - "Make.com AI workflow"
  - "Anthropic API Make.com"
affiliates:
  - make-com
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "How do I connect Claude to Make.com?"
    a: "Go to Make.com, create a new scenario, search for the Anthropic (Claude) module, and click 'Create a connection'. You'll be prompted to enter your Anthropic API key, which you can generate at console.anthropic.com. Once saved, the connection persists across all your scenarios."
  - q: "Does Make.com have a native Claude module?"
    a: "Yes. Make.com has a native Anthropic (Claude) module that connects directly to the Claude API. You can use it to send prompts, pass dynamic data from other modules, and route Claude's responses to any downstream app — no custom code required."
  - q: "What can I automate with Claude and Make.com?"
    a: "Common workflows include auto-generating blog drafts from RSS feeds, classifying customer support emails and routing them, summarising documents uploaded to Google Drive, writing personalised cold email sequences from a CRM, and creating social media captions from product data."
summary: "Claude integrates with Make.com through the native Anthropic module, enabling no-code automations that pipe Claude's AI capabilities into any app in your stack. This guide covers setting up the connection, building your first scenario, and scaling to real production workflows."
hero_image: "/assets/images/heroes/photo-041-122100392829357116.jpg"
hero_alt: "Make."
---

# Claude + Make.com — Complete Integration Guide (2026)

*Last updated: 2026-06-07*

The Claude Make.com integration turns Anthropic's AI into the reasoning engine of your no-code automation stack. With Make.com's native Anthropic (Claude) module, you can pass any data into Claude — a customer email, a product feed, a form submission — and route the AI-generated response directly to Gmail, Slack, Airtable, Google Docs, or hundreds of other apps, all without writing a single line of code. This guide covers everything: connecting your Anthropic API key, building your first scenario from scratch, choosing between webhook and scheduled triggers, and five high-impact workflow templates you can deploy today.

## What is the Claude Make.com Integration?

Make.com (formerly Integromat) is a visual automation platform that connects thousands of apps through a drag-and-drop scenario builder. Claude is Anthropic's AI model capable of writing, summarising, classifying, translating, and reasoning over text. When you combine the two, Claude becomes the intelligent middle layer in your automations — it receives raw inputs from any trigger, processes them with AI reasoning, and passes structured outputs to any downstream action.

The Claude Make.com integration works through Make.com's native Anthropic module. You do not need to write HTTP requests or handle authentication manually. Make.com manages the API call, you supply the prompt and your API key, and the module returns Claude's response as a mappable variable you can use anywhere in the scenario.

Make.com supports all current Claude models including claude-haiku-4-5 (fast and cheap), claude-sonnet-4-5 (the everyday workhorse), and claude-opus-4-5 (maximum capability). You select the model per module, so you can use Haiku for high-volume classification tasks and Sonnet for writing tasks within the same scenario.

## How to Connect Claude to Make.com — Step by Step

### Step 1: Get Your Anthropic API Key

Visit [console.anthropic.com](https://console.anthropic.com) and sign in or create an account. Navigate to **API Keys** in the left sidebar and click **Create Key**. Give it a descriptive name like "Make.com Automations". Copy the key immediately — Anthropic only shows it once. Add a credit balance under **Billing** if you haven't already; API calls won't work without credits loaded.

### Step 2: Open Make.com and Create a New Scenario

Log into your Make.com account and click **Create a new scenario** from the dashboard. You'll see a blank canvas with a large "+" in the centre. This is where your trigger module will go. Every Make.com scenario starts with a trigger — the event that kicks off the workflow.

### Step 3: Choose Your Trigger

Click the "+" to browse modules. For your first test, choose **Webhooks > Custom Webhook**. This lets you trigger the scenario manually by sending a POST request, which is perfect for testing. For production workflows, common triggers include:

- **Gmail > Watch Emails** — fires when a new email arrives in a specific label
- **Google Sheets > Watch Rows** — fires when a new row is added
- **HTTP > Watch Requests** — fires when your website form submits data
- **Schedule** — fires on a time interval (every hour, every day at 9am)

Click the trigger module you chose and follow the setup prompts.

### Step 4: Add the Anthropic (Claude) Module

Click the "+" after your trigger to add the next module. Search for **Anthropic** in the module search box. Select **Anthropic > Create a Message**. Click **Add** next to the Connection field, enter a name for the connection, and paste your Anthropic API key. Click **Save**.

Now configure the module:

- **Model**: Select `claude-sonnet-4-5` for most tasks, `claude-haiku-4-5` for speed-sensitive high-volume tasks
- **Max Tokens**: Set to 500–2000 depending on output length needed
- **Messages**: This is your prompt. Click into the **Content** field and mix static text with dynamic variables mapped from your trigger. For example: `Summarise this customer email in 3 bullet points:\n\n{{1.Body}}`

### Step 5: Map Claude's Output to the Next Module

After the Anthropic module runs, its response is available as `{{2.content[].text}}` (or similar, depending on your scenario numbering). Add your action module — for example, **Gmail > Send an Email**, **Slack > Create a Message**, or **Google Sheets > Add a Row** — and map Claude's response into the relevant field.

### Step 6: Add Error Handling

Claude API calls can occasionally fail due to rate limits or network issues. In Make.com, right-click the Anthropic module and select **Add error handler**. Choose **Resume** or **Rollback** depending on whether downstream steps should still run. For production scenarios, add a fallback route that sends you a Slack or email alert when Claude fails.

### Step 7: Test and Activate

Click **Run once** to test with live data. Inspect each module's output in the execution log to confirm data is flowing correctly. When satisfied, toggle the scenario from **Off** to **On** and set your scheduling or keep the webhook active.

## Claude Make.com — 5 High-Impact Automation Examples

### 1. Auto-Draft Blog Posts from RSS Feeds

**Trigger**: RSS > Watch New Articles from competitor or news RSS feed  
**Claude prompt**: "Based on this news article headline and summary, write a 600-word blog post for a [your niche] audience. Include an introduction, three key takeaways, and a conclusion: {{headline}} — {{summary}}"  
**Action**: Google Docs > Create Document (saves the draft for human review)

This workflow surfaces content ideas and produces a usable first draft automatically. A content team can review and publish instead of starting from a blank page.

### 2. Customer Support Email Triage

**Trigger**: Gmail > Watch Emails (support inbox label)  
**Claude prompt**: "Classify this customer support email into one of these categories: [billing, technical, general, complaint, positive-feedback]. Reply with only the category name. Email: {{Body}}"  
**Action**: Gmail > Move Email to Label (routes to the right team folder automatically)

This eliminates manual sorting. Claude reads the email and outputs a single category word, which Make.com uses to route the message to the correct label or even forward it to the right team member.

### 3. Lead Enrichment from Form Submissions

**Trigger**: Typeform > Watch Responses (or any form tool)  
**Claude prompt**: "A new lead has submitted this form. Based on their company name '{{company}}', job title '{{title}}', and message '{{message}}', write a personalised 3-sentence follow-up email. Be warm and professional. Do not mention their form submission directly."  
**Action**: Gmail > Send Email (sends the personalised reply immediately)  
**Action 2**: HubSpot > Create Contact (logs the lead in your CRM)

### 4. Google Drive Document Summariser

**Trigger**: Google Drive > Watch Files (watches a specific folder)  
**Action 1**: Google Drive > Download File  
**Claude prompt**: "Summarise this document in a 5-bullet executive summary. Focus on action items and key decisions: {{file content}}"  
**Action 2**: Slack > Create Message (posts summary to a #summaries channel)

When anyone drops a document into the watched folder, the team gets an instant Slack summary without reading the full file.

### 5. Social Media Caption Generator

**Trigger**: Google Sheets > Watch New Rows (product info spreadsheet)  
**Claude prompt**: "Write 3 versions of a social media caption for this product. Version A: professional LinkedIn tone. Version B: casual Instagram tone. Version C: punchy Twitter/X tone. Product name: {{name}}. Key features: {{features}}. Price: {{price}}."  
**Action**: Google Sheets > Update Row (writes the 3 captions back into columns D, E, F)

The marketing team fills in product info, and captions for three platforms appear in the same row automatically.

## Webhook vs Scheduled Trigger — Which Should You Use?

Choosing the right trigger type affects cost, speed, and reliability.

| Criteria | Webhook Trigger | Scheduled Trigger |
|---|---|---|
| **Speed** | Near-instant (fires within seconds of event) | Delayed (fires on next scheduled interval) |
| **Make.com operations used** | 1 per event | 1 per check interval, even if no data |
| **Best for** | Form submissions, emails, live events | Batch processing, reports, daily digests |
| **Requires always-on webhook** | Yes (URL must remain active) | No |
| **Data volume** | Processes one record at a time | Can process batches with iterators |
| **Cost at high volume** | Higher (many individual runs) | Lower (one run processes many rows) |

**Use a webhook trigger** when you need immediate action — customer emails, form responses, payment notifications.

**Use a scheduled trigger** when you are batch-processing data — daily report generation, weekly digest emails, nightly CRM enrichment runs.

For most Claude Make.com integrations, webhooks handle real-time interactions and scheduled triggers handle batch content generation.

## Claude Make.com Integration — Pricing Considerations

Make.com charges by operations (each module execution = 1 operation). A typical 4-module Claude scenario uses 4 operations per run. Make.com's free plan gives 1,000 operations/month, suitable for testing. The Core plan ($9/month) gives 10,000 operations/month.

Claude API costs are separate and billed by Anthropic. Claude Haiku is roughly $0.0008 per 1,000 input tokens — processing 1,000 emails per month costs under $1 in API fees. Claude Sonnet is roughly 10x more expensive but still very low-cost at typical automation volumes.

For a workflow processing 500 emails per month with a 4-module scenario, expect to pay roughly $5–15/month total (Make.com + API), far less than any SaaS tool that offers comparable intelligence.

## Related Claude Guides

- [Claude vs n8n for Automation](/claude-make-vs-n8n/)
- [Claude n8n Workflows](/claude-n8n-workflows/)
- [Build a Claude AI Agent](/build-claude-ai-agent/)
- [Claude for CRM Automation](/claude-crm-automation/)
- [Claude Automation Workflows — 10 Templates](/claude-automation-workflows/)
