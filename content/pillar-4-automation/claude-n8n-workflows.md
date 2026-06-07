---
title: "Claude + n8n — How to Build AI Workflows (2026 Guide)"
slug: claude-n8n-workflows
pillar: automation
meta_description: "Connect Claude AI to n8n and build powerful automation workflows in 2026. Step-by-step setup, 4 real workflow examples, and self-hosted vs cloud comparison."
primary_keyword: "Claude n8n workflow"
secondary_keywords:
  - "n8n Claude API"
  - "n8n AI automation"
  - "Anthropic n8n node"
affiliates:
  - n8n
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "How do I use Claude with n8n?"
    a: "In n8n, add an HTTP Request node configured to call the Anthropic Messages API at https://api.anthropic.com/v1/messages. Set the x-api-key header to your Anthropic API key, set the model, and pass your prompt in the messages array. n8n also has community nodes for Anthropic that wrap this into a cleaner interface."
  - q: "Is n8n better than Make.com for Claude?"
    a: "n8n is better if you want to self-host, need unlimited workflow runs without per-operation billing, or are comfortable with a slightly more technical setup. Make.com is better if you want a fully managed cloud platform and a gentler learning curve. Both connect to Claude's API equally well."
  - q: "Can n8n use the Claude API?"
    a: "Yes. n8n connects to the Claude API via the HTTP Request node (calling the Anthropic REST API directly) or through community-built Anthropic nodes available in the n8n community node library. Both approaches give full access to Claude's models and parameters."
summary: "n8n is an open-source automation platform that connects to Claude's API through HTTP Request nodes or community Anthropic nodes, letting you build AI workflows you can self-host or run in n8n Cloud. This guide walks through setup, four practical workflow examples, and when to choose n8n over Make.com."
---

# Claude + n8n — How to Build AI Workflows (2026 Guide)

*Last updated: 2026-06-07*

A Claude n8n workflow combines n8n's powerful open-source automation engine with Claude's AI reasoning capabilities, letting you build intelligent pipelines that write, classify, summarise, and make decisions — all without per-operation pricing. Unlike cloud-only automation platforms, n8n can be fully self-hosted on your own server, making it attractive for teams with data privacy requirements or high workflow volumes where per-operation billing would become expensive. This guide covers connecting Claude to n8n, four practical workflow examples, and the key differences between self-hosted and cloud n8n.

## What is n8n and How Does It Work with Claude?

n8n is an open-source workflow automation tool with a visual node-based editor similar to Make.com. Each "node" in n8n represents either a trigger (something that starts the workflow) or an action (something the workflow does). Nodes pass data between each other as JSON objects, and you can transform, filter, and route that data using n8n's built-in expression language.

Claude connects to n8n via the Anthropic Messages API. You can call it in two ways:

**Option A — HTTP Request Node**: n8n's built-in HTTP Request node can call any REST API. You configure it to POST to `https://api.anthropic.com/v1/messages` with your API key in the headers. This requires a little more setup but works on any n8n version and gives you complete control over every parameter.

**Option B — Community Anthropic Node**: The n8n community library includes Anthropic-specific nodes that provide a cleaner, form-based interface for Claude. Search "Anthropic" in the n8n community nodes panel to install. Note that community nodes are maintained by third parties, not Anthropic or n8n.

For production workflows, the HTTP Request approach is more reliable because it doesn't depend on a community maintainer keeping their node up to date.

## How to Set Up Claude in n8n — Step by Step

### Step 1: Get Your Anthropic API Key

Go to [console.anthropic.com](https://console.anthropic.com), sign in, and navigate to **API Keys**. Click **Create Key**, name it "n8n Workflows", and copy the key. Add billing credits under the Billing section — API calls won't succeed without a positive balance.

### Step 2: Install or Access n8n

**Cloud (n8n.io)**: Create an account at n8n.io. You get a hosted instance with a visual editor accessible from your browser. This is the fastest way to get started.

**Self-hosted (Docker)**: Run `docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n docker.n8n.io/n8nio/n8n` in your terminal. Access the editor at `http://localhost:5678`. Self-hosting gives you unlimited workflow executions and full data control, but you manage your own infrastructure.

### Step 3: Store Your API Key as a Credential

In n8n, open **Credentials** from the left sidebar. Click **New Credential** and search for "Header Auth". Name it "Anthropic API" and add a header:

- **Name**: `x-api-key`
- **Value**: your Anthropic API key

Save the credential. You'll reference this in every HTTP Request node that calls Claude.

### Step 4: Build Your First Claude Node

In your workflow, add an **HTTP Request** node. Configure it:

- **Method**: POST
- **URL**: `https://api.anthropic.com/v1/messages`
- **Authentication**: Select "Header Auth" and choose your "Anthropic API" credential
- **Headers**: Add `anthropic-version: 2023-06-01` and `content-type: application/json`
- **Body (JSON)**:

```json
{
  "model": "claude-sonnet-4-5",
  "max_tokens": 1024,
  "messages": [
    {
      "role": "user",
      "content": "{{ $json.prompt }}"
    }
  ]
}
```

Replace `{{ $json.prompt }}` with your actual prompt text or a reference to upstream node data.

### Step 5: Extract Claude's Response

Claude's API returns a JSON object. The response text lives at `content[0].text` in the response body. In n8n, access it with the expression `{{ $json.content[0].text }}`. Add a **Set** node after your HTTP Request node to extract this into a cleaner variable for downstream nodes.

### Step 6: Connect Downstream Actions

Add any n8n node as your action: Gmail, Slack, Google Sheets, Notion, Airtable, HubSpot — n8n has hundreds of built-in integrations. Map the extracted Claude response into the relevant fields of your action node.

### Step 7: Test and Activate

Use the **Execute Workflow** button to run a test with sample data. Review each node's output panel to confirm data flows correctly. Once satisfied, toggle the workflow **Active** so it runs automatically from its trigger.

## 4 Practical Claude n8n Workflow Examples

### Workflow 1: Automated Email Response Drafts

**Trigger**: Gmail node set to watch for new emails in your inbox  
**Claude node prompt**: "You are an email assistant. Read this email and write a professional draft reply. Keep it under 150 words. Be helpful and direct. Email subject: {{subject}}. Email body: {{body}}"  
**Action**: Gmail > Create Draft (creates a draft in your Gmail for human review before sending)

This workflow means you never start an email reply from scratch. Every incoming email gets a draft reply waiting for you to review, edit if needed, and hit send.

### Workflow 2: Content Brief to Blog Post Pipeline

**Trigger**: Airtable node watches for new rows in a "Content Briefs" table  
**Claude node 1**: "Expand this brief into a full 800-word blog post with H2 subheadings. Brief: {{brief}}"  
**Claude node 2**: "Write an SEO meta description (150-160 characters) for this blog post: {{post}}"  
**Action**: Airtable > Update Row (writes the full post and meta description back to the same row)

The content team adds briefs to Airtable, and complete draft posts appear in the same table within minutes.

### Workflow 3: Support Ticket Classification and Routing

**Trigger**: Webhook node (your support form posts here)  
**Claude node prompt**: "Classify this support message into exactly one category from this list: billing, technical-bug, feature-request, general-question, urgent-complaint. Reply with only the category. Message: {{message}}"  
**Switch node**: Routes based on Claude's category output  
**Actions**: Different Slack channel notifications or email forwards per category

This workflow eliminates manual triage. Claude reads the message, outputs a single category, and the Switch node routes it to the right team instantly.

### Workflow 4: Weekly Competitor Monitoring Report

**Trigger**: Schedule node (fires every Monday at 8am)  
**HTTP node**: Fetches RSS feeds or web pages from competitor sites  
**Claude node**: "Here are the latest updates from competitor sites. Summarise the 5 most important developments for our team in bullet points. Highlight anything that might require a response from us: {{content}}"  
**Action**: Gmail > Send Email (sends the summary to your team)

No more manually checking competitor sites. The workflow runs weekly, Claude synthesises everything into a readable briefing, and it lands in your inbox before the working week begins.

## Self-Hosted vs Cloud n8n for Claude Workflows

Choosing between self-hosted and n8n Cloud affects your costs, data handling, and operational overhead.

| Factor | Self-Hosted n8n | n8n Cloud |
|---|---|---|
| **Pricing** | Free (pay for server costs only) | Starts ~$20/month |
| **Workflow executions** | Unlimited | Limited by plan tier |
| **Setup effort** | Moderate (Docker or VPS required) | Minutes (browser-based) |
| **Data privacy** | Full control, data stays on your server | Data passes through n8n's servers |
| **Maintenance** | You manage updates and uptime | n8n manages infrastructure |
| **Scaling** | Manual (you add server resources) | Automatic within plan limits |
| **Best for** | High volume, sensitive data, developers | Getting started, small teams, non-technical users |

**Self-host if**: you have sensitive customer data, you're running thousands of workflow executions per month, or you have a developer comfortable managing a Linux server.

**Use n8n Cloud if**: you want to start building immediately without DevOps overhead, your workflow volume is moderate, and data privacy requirements are standard.

Both connect to the Claude API identically — the only difference is where n8n itself runs.

## Related Claude Guides

- [Make.com vs n8n for Claude](/claude-make-vs-n8n/)
- [Claude Make.com Integration](/claude-make-com-integration/)
- [Build a Claude AI Agent](/build-claude-ai-agent/)
- [Claude Automation Workflows — 10 Templates](/claude-automation-workflows/)
- [Claude API Getting Started](/claude-api-getting-started/)
