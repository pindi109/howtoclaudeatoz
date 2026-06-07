---
title: "Claude for CRM Automation — Full Workflow Guide (2026)"
slug: claude-crm-automation
pillar: automation
meta_description: "Use Claude AI to automate CRM tasks in 2026 — lead scoring, email drafts, contact enrichment, and follow-up sequences. Works with HubSpot, Salesforce, Pipedrive, and Notion."
primary_keyword: "Claude CRM automation"
secondary_keywords:
  - "Claude HubSpot automation"
  - "AI CRM integration"
  - "Claude Salesforce workflow"
affiliates:
  - make-com
  - n8n
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "Can Claude integrate with CRMs?"
    a: "Yes. Claude integrates with any CRM that has an API — including HubSpot, Salesforce, Pipedrive, and Notion — through Make.com or n8n. These platforms have native modules for both Claude (via the Anthropic module) and major CRMs, allowing you to build AI-powered CRM workflows without writing code."
  - q: "How do I use Claude to automate CRM tasks?"
    a: "Common CRM automation tasks with Claude include: scoring new leads based on form data, writing personalised follow-up email drafts, enriching contact records with research, summarising deal history before sales calls, and classifying support tickets. Make.com connects Claude to your CRM visually; n8n is better for high-volume or self-hosted workflows."
  - q: "Which CRMs work with Claude?"
    a: "Claude works with any CRM via API. Make.com has native modules for HubSpot, Salesforce, Pipedrive, Zoho, ActiveCampaign, and more. Notion (used as a lightweight CRM) also has a Make.com module. For Salesforce, n8n's Salesforce node offers deep integration for complex enterprise workflows."
summary: "Claude automates the most time-consuming CRM tasks — lead scoring, email drafting, contact enrichment, and deal summaries — by connecting to HubSpot, Salesforce, Pipedrive, or Notion through Make.com or n8n. This guide covers CRM compatibility, four workflow examples, and how to set up your first Claude CRM automation."
---

# Claude for CRM Automation — Full Workflow Guide (2026)

*Last updated: 2026-06-07*

Claude CRM automation eliminates the manual work that clogs every sales pipeline: writing follow-up emails from scratch, scoring leads based on form data, researching prospects before calls, and updating records after meetings. Claude connects to your CRM through Make.com or n8n, reads contact and deal data, and outputs structured content or decisions that your automation routes back into the correct fields. The result is a CRM that stays up to date, with personalised outreach and qualified leads, without your sales team spending hours on admin. This guide covers which CRMs work with Claude, four automation examples, and how to build your first workflow.

## How Claude Connects to Your CRM

Claude does not connect directly to CRMs — it has no native HubSpot or Salesforce plugin. The connection happens through an automation platform that sits between Claude and your CRM:

**Via Make.com**: Make.com has native modules for HubSpot, Salesforce, Pipedrive, Zoho CRM, ActiveCampaign, and Notion. You add the Anthropic (Claude) module between a CRM trigger and a CRM action. Make.com handles all API authentication and data mapping visually.

**Via n8n**: n8n has built-in nodes for HubSpot, Salesforce, Pipedrive, and Notion. Like Make.com, you chain the Claude HTTP Request node between CRM trigger and action nodes. n8n is better for high-volume scenarios or teams that need to self-host.

**Via direct API code**: If you're a developer, you can call both the CRM API and the Anthropic API directly in Python or Node.js. This gives maximum flexibility but requires maintenance.

For most teams, Make.com is the fastest path to a working Claude CRM automation.

## CRM Compatibility with Claude

| CRM | Make.com module | n8n node | Native Claude | API access |
|---|---|---|---|---|
| **HubSpot** | Yes (native) | Yes (native) | No | Yes |
| **Salesforce** | Yes (native) | Yes (native) | No | Yes |
| **Pipedrive** | Yes (native) | Yes (native) | No | Yes |
| **Notion** | Yes (native) | Yes (native) | No | Yes |
| **Zoho CRM** | Yes (native) | Community node | No | Yes |
| **ActiveCampaign** | Yes (native) | Yes (native) | No | Yes |
| **Close** | Via HTTP | Via HTTP | No | Yes |
| **Copper** | Yes (native) | Via HTTP | No | Yes |

"Via HTTP" means no native node exists, but n8n's HTTP Request node can call the CRM's REST API directly. Any CRM with a REST API can connect to Claude via Make.com's HTTP module or n8n's HTTP Request node.

## 4 Claude CRM Automation Examples

### Automation 1: Lead Scoring on Form Submission

**Trigger**: Make.com watches for new HubSpot contacts (or any form submission)  
**Claude prompt**:
```
Score this new lead from 1-10 based on fit for our B2B SaaS product.
High score (8-10): Company 50+ employees, B2B industry, decision-maker title, specific pain described.
Low score (1-4): Individual/consumer, vague message, student email.
Mid (5-7): Everything else.

Name: {{name}}
Company: {{company}}
Job title: {{title}}
Company size: {{company_size}}
Message: {{message}}

Respond with JSON only: {"score": number, "tier": "hot|warm|cold", "reason": "one sentence"}
```
**Action**: HubSpot > Update Contact — writes score to a custom property, updates the lifecycle stage based on tier  
**Action 2** (hot leads only): Slack notification to the sales channel: "New hot lead: {{name}} from {{company}} — Score: {{score}}"

**Impact**: Every lead enters your CRM pre-scored. Sales reps see who to contact first without reviewing each form submission.

### Automation 2: Pre-Call Research Brief

**Trigger**: Make.com Schedule trigger (runs every morning at 7am)  
**Step 1**: HubSpot > List Contacts filtered by "meeting scheduled today"  
**Step 2**: For each contact, HubSpot > Get Contact (fetches full record: company, deal history, last activity, notes)  
**Claude prompt**:
```
Prepare a 5-bullet pre-call brief for a sales rep meeting with this prospect today.
Include: their likely goals, key concerns based on their form message, suggested opening question, relevant company context, and one personalisation point.

Contact record: {{contact_data}}
Deal stage: {{deal_stage}}
Last activity: {{last_activity_note}}
```
**Action**: Gmail > Send Email to the assigned sales rep with the brief

**Impact**: Sales reps arrive at every call prepared, without spending 20 minutes researching each prospect. Response times to "how did the call go?" improve because the rep felt confident.

### Automation 3: AI-Written Follow-Up Email Drafts

**Trigger**: HubSpot > Watch Deal Stage Changes (fires when a deal moves to "Follow Up Needed")  
**Claude prompt**:
```
Write a 150-word follow-up email to {{contact_name}} at {{company}}.
Context: We just had an introductory call. They showed interest in {{product_interest}} but raised concern about {{objection}}.
Goal: Keep the conversation warm, address the concern briefly, and propose a 30-minute demo next week.
Subject line: Include a compelling subject line prefixed with "Subject:"
Tone: Warm and confident, not pushy.
```
**Action**: Gmail > Create Draft (saves as a draft in the rep's Gmail inbox — they review and send)  
**Action 2**: HubSpot > Create Task ("Review and send follow-up email draft") assigned to the deal owner

**Impact**: Reps get a first draft ready in their Gmail. They spend 2 minutes editing rather than 15 minutes writing from scratch. Follow-up rate increases because the friction of "I need to write this email" is removed.

### Automation 4: Post-Meeting Note Summariser

**Trigger**: Webhooks > Custom Webhook (your meeting tool sends a transcript webhook — Otter.ai, Fireflies, or similar)  
**Claude prompt**:
```
Summarise this sales call transcript into a CRM note. Include:
1. Key topics discussed (3-5 bullets)
2. Next steps agreed (bulleted list)
3. Objections or concerns raised
4. Proposed timeline / deal stage recommendation

Transcript: {{transcript}}
```
**Action**: HubSpot > Create Note on the contact record (pastes Claude's summary)  
**Action 2**: HubSpot > Update Deal — update close date and stage based on Claude's recommendation (if Claude extracted that information)

**Impact**: CRM records update automatically after every call. No more half-filled deal records because reps didn't have time to write notes.

## Setting Up Your First Claude HubSpot Automation in Make.com

### Step 1: Connect HubSpot to Make.com

In Make.com, create a new scenario. Add a HubSpot trigger module. Click **Create a connection** and follow the OAuth flow to connect your HubSpot account. Choose your trigger type (Watch New Contacts, Watch Deal Stage Changes, etc.).

### Step 2: Add the Anthropic Module

After the HubSpot trigger, add an **Anthropic > Create a Message** module. Create an API key connection using your Anthropic API key. Write your prompt in the **Content** field, mapping HubSpot data variables ({{name}}, {{company}}, {{message}}) into the prompt text.

### Step 3: Parse Claude's Response

If Claude returns JSON (for scoring or structured data), add a **JSON > Parse JSON** module to extract the values into individual variables. If Claude returns plain text (for email drafts or summaries), you can map the raw text output directly.

### Step 4: Update the CRM

Add a HubSpot action module — **Update Contact**, **Create Note**, **Create Task**, or **Send Email**. Map Claude's parsed output into the relevant HubSpot fields.

### Step 5: Add Error Handling

Add an error handler to the Anthropic module (right-click > Add error handler). If the API call fails, set a fallback: send yourself a Slack message with the contact details so you can process it manually.

## Related Claude Guides

- [Claude Make.com Integration](/claude-make-com-integration/)
- [Claude n8n Workflows](/claude-n8n-workflows/)
- [Claude GetResponse Email Automation](/claude-getresponse-email-automation/)
- [Claude for Small Business](/claude-for-small-business/)
- [Claude Automation Workflows — 10 Templates](/claude-automation-workflows/)
