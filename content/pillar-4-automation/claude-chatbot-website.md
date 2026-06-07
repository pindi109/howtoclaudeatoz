---
title: "Building a Claude Chatbot for Your Website (2026 Guide)"
slug: claude-chatbot-website
pillar: automation
meta_description: "Add a Claude AI chatbot to your website in 2026 — no-code Make.com approach, API method, system prompt templates, embed options, and real pricing estimates."
primary_keyword: "Claude chatbot website"
secondary_keywords:
  - "Claude AI chatbot"
  - "add AI chatbot website"
  - "Claude customer service bot"
affiliates:
  - make-com
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "How do I add a Claude chatbot to my website?"
    a: "There are two main approaches: no-code and API-based. The no-code approach uses a chatbot widget platform (like Tidio, Crisp, or Chatbase) that connects to Claude via Make.com webhook — no coding required. The API approach involves building a small backend that calls the Anthropic API and a frontend chat UI. The no-code approach takes hours; the API approach takes days but gives full control."
  - q: "Can I use Claude as a customer service chatbot?"
    a: "Yes. Claude is well-suited for customer service chatbots because it handles nuanced, multi-turn conversations naturally and follows instruction prompts reliably. You configure a system prompt that describes your business, products, policies, and tone. Claude answers questions based on that context and escalates to a human when needed."
  - q: "Is a Claude chatbot free?"
    a: "The Claude API is not free — you pay per token. However, costs are low. A chatbot handling 500 conversations per month with an average of 10 messages each (at ~100 tokens per message) costs roughly $1.50–$3 in API fees using Claude Sonnet. You'll also need a chatbot widget platform (many have free tiers) and Make.com (free tier available for low volume)."
summary: "You can add a Claude chatbot to your website through a no-code route using a chatbot widget and Make.com, or through a direct API integration for full customisation. This guide covers both approaches, system prompt best practices for chatbots, embed options, and a realistic pricing estimate."
---

# Building a Claude Chatbot for Your Website (2026 Guide)

*Last updated: 2026-06-07*

Adding a Claude chatbot to your website gives visitors instant, intelligent responses to questions about your products, services, pricing, and policies — 24 hours a day, without human staff. A Claude chatbot website integration can handle the top 80% of customer queries automatically, escalate the rest to a human, and do it in your brand's voice, using your specific business knowledge. This guide covers the no-code approach (fastest to launch), the API approach (most flexible), the system prompt structure that makes chatbots work, and a realistic cost breakdown so you know what to budget.

## What Makes Claude a Good Website Chatbot?

Not all AI models work equally well as customer-facing chatbots. Claude has several properties that make it particularly suitable:

**Instruction-following**: Claude reliably stays within the boundaries you set in your system prompt. If you tell it not to discuss competitors or to always recommend contacting support for billing issues, it will follow those instructions consistently.

**Nuanced conversation**: Claude handles multi-turn conversations naturally, remembering earlier context in the same chat session. Customers can ask follow-up questions without repeating themselves.

**Tone control**: Claude adapts its tone precisely to your brand voice as defined in the system prompt — professional, casual, warm, technical — and maintains it throughout the conversation.

**Honest uncertainty**: Claude says "I don't have information about that" rather than hallucinating an answer, which is critical for a customer-facing chatbot where incorrect information causes real problems.

## Approach 1: No-Code Claude Chatbot via Make.com

The no-code approach connects a third-party chatbot widget to Claude through Make.com. You get a chat interface embedded on your site, Make.com handles the API calls to Claude, and you configure everything visually.

### What You Need

- A chatbot widget platform that supports webhook integration: Tidio, Crisp, Chatbase, or similar
- A Make.com account (free tier works for low volume)
- An Anthropic API key with billing enabled

### Step 1: Set Up Your Chatbot Widget

Sign up for a chatbot widget platform. Most have a free tier. Install their embed code on your website — this is usually a single `<script>` tag added before `</body>`. Configure basic settings: chatbot name, avatar, opening message.

In the widget platform's settings, find the **Webhook** or **Custom AI integration** option. Copy the webhook URL that the widget will call when a user sends a message.

### Step 2: Create a Make.com Scenario as the AI Backend

In Make.com, create a new scenario with a **Webhooks > Custom Webhook** trigger. Copy the webhook URL that Make.com generates.

Paste this Make.com webhook URL into your chatbot widget platform as the AI endpoint. Now when a user sends a message, the widget calls Make.com.

### Step 3: Add the Claude Module

After the webhook trigger, add an **Anthropic** module. In the **System** field, paste your chatbot system prompt (see system prompt guidance below). In the **Content** field, map the user's message from the webhook payload: `{{1.message}}` or whatever variable name your widget platform sends.

Set **Model** to `claude-sonnet-4-5` and **Max Tokens** to 400-600 (enough for a helpful response without being overwhelming in a chat context).

### Step 4: Return Claude's Response to the Widget

Add an HTTP module configured to POST Claude's response back to your widget platform's response endpoint. The exact format depends on your widget — most accept a simple JSON body with a `message` field.

### Step 5: Test and Go Live

Use your widget platform's test mode to simulate conversations. Check that Claude's responses are being returned correctly. Adjust your system prompt based on what you observe. When satisfied, activate the Make.com scenario and your chatbot goes live.

## Approach 2: API-Based Claude Chatbot (Developer)

For full control over the chat UI, conversation history, and integration with your own backend systems, building directly with the Claude API gives you the most flexibility.

### Architecture Overview

```
User browser → Your frontend chat UI
     ↓
Your backend server (Node.js/Python/etc.)
     ↓
Anthropic API (Claude)
     ↑
Response returned up the chain
```

Your backend maintains the conversation history (the `messages` array) per user session. Each new user message appends to the array before sending the full history to Claude. This is what gives the chatbot its memory within a session.

### Minimal Python Backend (Flask)

```python
from flask import Flask, request, jsonify, session
import anthropic

app = Flask(__name__)
app.secret_key = "your-secret-key"
client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are a helpful assistant for Acme Co., a software company.
You help customers with questions about our product, pricing, and getting started.
If asked about billing or account issues, direct them to support@acme.co.
Keep responses concise and friendly. Never discuss competitors."""

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    if 'history' not in session:
        session['history'] = []
    
    session['history'].append({"role": "user", "content": user_message})
    
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=512,
        system=SYSTEM_PROMPT,
        messages=session['history']
    )
    
    assistant_reply = response.content[0].text
    session['history'].append({"role": "assistant", "content": assistant_reply})
    
    return jsonify({"reply": assistant_reply})
```

This minimal backend handles multi-turn conversation by maintaining history in the session. Your frontend sends a POST request to `/chat` with the user's message and displays the reply.

## Writing a Claude Chatbot System Prompt

The system prompt is the most important configuration decision for a chatbot. A well-written system prompt prevents Claude from going off-topic, establishes the right tone, and handles edge cases gracefully.

**Effective system prompt structure:**

```
You are [name], a [role] for [company name].

Your job: [primary purpose in one sentence].

What you know about [company]:
- [Key product/service info]
- [Pricing overview]
- [Key policies]
- [Common FAQs and answers]

Tone: [adjectives describing desired voice]

Rules:
- If asked about [sensitive topic], always [specific response]
- If you don't know something, say "I don't have that information — [escalation path]"
- Keep responses under [word count] words
- [Any other constraints]
```

**Example for an e-commerce chatbot:**

```
You are Aria, a friendly customer assistant for ShopBright, an online homewares retailer.

Your job: Help customers find products, answer questions about orders, and resolve common issues.

What you know:
- We ship UK-wide, free over £40
- Returns accepted within 30 days for unused items
- Orders take 2-4 business days to arrive
- Our bestselling categories are kitchen, bedroom, and bathroom

Tone: Warm, helpful, slightly informal — like a knowledgeable friend, not a corporate script.

Rules:
- For order tracking, ask for their order number and direct them to: shopsibright.com/track
- For refund requests, direct to: support@shopbright.com
- If unsure, say "I'm not 100% sure about that — let me get you to our team" and provide the support email
- Keep responses under 80 words
```

## Embed Options for Your Claude Chatbot

| Option | Effort | Control | Cost |
|---|---|---|---|
| **Third-party widget + Make.com** | Low (hours) | Medium | Widget platform fee + Make.com + API |
| **Chatbase / Botpress** | Low (hours) | Medium | Platform fee + API |
| **Custom frontend + your backend** | High (days) | Full | Hosting + API only |
| **Claude.ai embed** | Not available | N/A | N/A (Claude.ai is not embeddable) |

For most small businesses, a third-party widget connected to Claude via Make.com is the right starting point. You get a professional-looking chat interface, basic analytics, and mobile support without building anything from scratch.

## Pricing Estimate for a Claude Website Chatbot

Costs depend on conversation volume. Here is a realistic monthly estimate for a small business chatbot:

| Component | Usage assumption | Monthly cost |
|---|---|---|
| Claude Sonnet API | 500 conversations, 10 messages, 150 tokens avg | ~$3.50 |
| Make.com Core plan | Covers ~2,500 operations/month | $9.00 |
| Chatbot widget (Tidio free) | Up to 50 conversations/month free | $0 |
| **Total (low volume)** | | **~$12.50/month** |

For higher volume or a custom-built frontend, the Make.com cost disappears (you call the API directly) and the API cost scales linearly. At 5,000 conversations/month, you'd pay roughly $35/month in API fees with no platform fee.

## Related Claude Guides

- [Claude for Customer Service](/claude-customer-service/)
- [Claude Make.com Integration](/claude-make-com-integration/)
- [Claude API Getting Started](/claude-api-getting-started/)
- [Build a Claude AI Agent](/build-claude-ai-agent/)
- [Claude for Small Business](/claude-for-small-business/)
