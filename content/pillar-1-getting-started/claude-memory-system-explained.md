---
title: "Claude Memory System Explained — How It Works (2026)"
slug: claude-memory-system-explained
pillar: getting-started
meta_description: "Claude's memory system explained: how context windows, Projects, and workarounds help Claude remember across conversations. Complete 2026 guide."
primary_keyword: "Claude memory system"
secondary_keywords:
  - "does Claude remember conversations"
  - "Claude persistent memory"
  - "Claude Projects memory"
affiliates: []
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "Does Claude remember previous conversations?"
    a: "No. By default, Claude does not remember anything from previous conversations. Each new conversation starts with a blank slate. Claude only has access to the messages within the current conversation's context window. The exception is Claude Projects, where uploaded files and custom instructions persist across multiple conversations within that Project."
  - q: "How do Claude Projects help with memory?"
    a: "Claude Projects provide a form of persistent memory by storing files, documents, and custom instructions that are loaded at the start of every conversation within the Project. This means Claude always knows your background, your requirements, and your reference materials — without you re-pasting them each session. Projects do not carry conversation history between sessions, only the stored files and instructions."
  - q: "Can I make Claude remember things permanently?"
    a: "You can create a persistent memory by maintaining a document — sometimes called a 'memory file' — that you update with key information and upload to a Claude Project. At the start of new conversations, Claude reads this file and effectively 'remembers' what you have recorded. Some advanced users also use the Claude API with custom memory systems built on vector databases, but this requires technical setup."
summary: "Claude does not have persistent memory between conversations by default. This guide explains how Claude's memory system works, how Projects provide a form of persistent context, and practical techniques for maintaining continuity across sessions."
---

# Claude Memory System Explained — How It Works (2026)

*Last updated: 2026-06-07*

Claude's memory system is one of the most commonly misunderstood aspects of the tool. By default, Claude has no memory between conversations — every new chat starts completely fresh. But within a single conversation, Claude's memory system is powerful: it holds up to 200,000 tokens in a single session. This guide explains exactly how Claude's memory works, what the limitations are, and how to use Claude Projects and other techniques to create effective persistent memory for ongoing work.

## What is Claude's Memory System? — Overview

Claude's memory system operates in three distinct layers, each with different persistence and scope.

**Layer 1 — In-context memory:** Everything within the current conversation's context window. This is Claude's primary working memory. It holds the full conversation history, any uploaded files, and any instructions you have given in this session. It persists only for the duration of the conversation.

**Layer 2 — Project memory:** Files and instructions stored in a Claude Project. These persist across all conversations within the Project but do not carry over individual conversation history. They represent a form of long-term background knowledge.

**Layer 3 — External memory (advanced):** Custom memory systems built via the Claude API using external databases or vector stores. This is a developer-level feature requiring technical setup.

For most users, understanding layers 1 and 2 is sufficient.

## How Claude's In-Context Memory Works

### The Context Window as Working Memory

Claude's 200,000-token context window is its working memory for a single conversation. Every message you send, every response Claude gives, and every file you upload is stored within this window. Claude can reference any part of this content when generating a new response — it does not "forget" the beginning of a conversation while it is still within the window.

This is why a long, detailed conversation with Claude can be extremely productive: you can establish extensive context at the start and Claude will carry it throughout the session. You can say "refer back to the document I uploaded at the start" and Claude will do so accurately.

### What Happens When the Context Window Fills

When a conversation grows long enough to exceed 200,000 tokens, the earliest content begins to fall out of the context window. Claude can no longer access it. This manifests as Claude "forgetting" early-conversation details, repeating information, or becoming less coherent about context established at the start of a long session.

For practical guidance on this, see the [Claude context window guide](/claude-context-window-explained/).

### What Happens When You Start a New Conversation

When you click "New chat" in Claude, you begin an entirely fresh context window. Claude has no access to any previous conversation — not even the one you just finished. There is no background recall, no learned preferences, and no memory of your name, your projects, or your previous instructions. Every new conversation is, by design, a blank slate.

This is not a bug. It is a deliberate architectural choice made partly for privacy reasons — Claude does not build a persistent profile of you over time without your explicit involvement.

## How Claude Projects Provide Persistent Memory

### What Projects Store

Claude Projects (available on Pro, Max, and Team plans) address the blank-slate limitation by providing a persistent storage layer that is loaded automatically into every new conversation within the Project.

A Project stores:
- **Files you upload:** PDFs, documents, spreadsheets, code files, and more
- **Custom instructions:** Written instructions that tell Claude who it is working with, what the task is, what tone to use, and any standing rules

Every time you start a new conversation within a Project, Claude receives:
1. Your custom instructions (as a system prompt)
2. Access to all files stored in the Project

This creates a durable form of memory that persists as long as the Project exists.

### What Projects Do Not Store

Projects do not carry conversation history between sessions. If you have a 50-message conversation within a Project and then start a new conversation in the same Project, Claude will not remember what you discussed in the previous chat. It will only know the Project instructions and files — not the specific exchanges.

This is an important distinction. Project memory is background knowledge, not episodic memory. Claude knows your brief but not what you talked about last Tuesday.

## Practical Techniques for Extending Claude's Memory

### Technique 1: The Memory File

Create a plain text or Markdown document called something like "MEMORY.md" or "Context.txt." Record key facts, decisions, preferences, and ongoing work status in this file. Update it periodically as your work evolves. Upload this file to a Claude Project.

Claude will read the memory file at the start of every conversation and will effectively "remember" everything you have recorded in it.

Example memory file entries:
```
Project: Redesigning the Meridian Analytics website
Brand colours: #1A2B4C (navy), #F0A500 (amber), #FFFFFF (white)
Tone: Professional but approachable. No jargon.
Status as of 2026-06-07: Homepage done. Services page in progress.
Key decision: We are not redesigning the blog at this stage.
My name: Sarah. I am the marketing director.
```

This technique effectively gives Claude a persistent memory of your project without requiring any technical setup beyond file management.

### Technique 2: Conversation Summaries

At the end of a productive conversation, ask Claude to summarise the key decisions, outputs, and next steps in a concise format. Copy this summary and save it — either in a standalone document or in your memory file. At the start of the next relevant conversation, paste the summary as context.

**Prompt to generate a summary:** "Before we finish, write a concise summary of this conversation: the key decisions we made, the outputs we produced, and what the agreed next steps are. Format as a bulleted list."

### Technique 3: Re-Pasting Key Context

For important standing instructions that do not change often, create a plain-text "context block" — a concise paragraph or list that summarises who you are, what you are working on, and what Claude should know. Paste this at the top of every new conversation where it is relevant.

This is less elegant than Projects but works on the free plan where Projects are not available.

### Technique 4: API-Based Memory Systems (Advanced)

Developers who use the Claude API can build custom memory systems using vector databases like Pinecone or Weaviate. These systems retrieve relevant stored memories based on the current conversation and inject them into the context window automatically. This creates a richer, more dynamic form of persistent memory than simple file uploads, but requires significant technical implementation.

## Step by Step: Setting Up a Memory File in Claude Projects

### Step 1: Create a Project

In claude.ai, click "New Project" in the left sidebar. Name it after the work or context you want to maintain — for example, "Writing: Tech Blog" or "Client: Acme Corp."

### Step 2: Write a Memory Document

Create a plain text or Markdown file on your computer. Include:
- Your name and role
- The project name, goal, and current status
- Key decisions that have been made
- Stylistic or technical preferences
- Any facts Claude would otherwise need you to re-explain

### Step 3: Upload the Memory File to the Project

In the Project view, click "Add files" and upload your memory document. Claude will have access to it in every conversation within this Project.

### Step 4: Write Project Instructions

In the Project's custom instructions field, write a brief instruction that tells Claude to read and use the memory file. For example: "At the start of each conversation, review the memory file to understand the current project status and any standing decisions."

### Step 5: Update the Memory File Regularly

As your project evolves — decisions change, new facts emerge, phases complete — update your memory file and re-upload it to the Project. Remove the old version to avoid Claude drawing on outdated information.

## Claude Memory System — Summary

| Memory Type | Persists Between Conversations? | Requires Setup? | Available On |
|---|---|---|---|
| In-context (conversation) | No | No | All plans |
| Claude Projects (files + instructions) | Yes (files, not chat history) | Minimal | Pro, Max, Team |
| Manual memory file in Project | Yes | Low | Pro, Max, Team |
| Conversation summary re-paste | Sort of (manual) | None | All plans |
| API vector memory | Yes (fully dynamic) | High (developer) | API access |

## Related Claude Guides

- [How to Use Claude Projects](/how-to-use-claude-projects/) — Full guide to creating and managing Projects
- [Claude Context Window Explained](/claude-context-window-explained/) — How the 200K-token context works in practice
- [Claude Keyboard Shortcuts and Power User Tips](/claude-keyboard-shortcuts/) — Speed up your workflow including context management
- [Claude System Prompts](/claude-system-prompts/) — Advanced persistent instructions for consistent behaviour
