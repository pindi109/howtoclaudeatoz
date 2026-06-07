---
title: "How to Use Claude Projects — Complete Guide (2026)"
slug: how-to-use-claude-projects
pillar: getting-started
meta_description: "Learn how to use Claude Projects in 2026: create a project, add files, set custom instructions, and maintain persistent context across conversations."
primary_keyword: "how to use Claude Projects"
secondary_keywords:
  - "Claude Projects guide"
  - "Claude persistent memory"
  - "Claude Projects files"
affiliates: []
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "What are Claude Projects?"
    a: "Claude Projects are persistent workspaces within Claude where you can store files, write custom instructions, and start multiple conversations that all share the same background context. Unlike regular conversations, Projects maintain their files and instructions indefinitely — you do not need to re-paste your documents or re-explain your requirements each time you start a new chat within the Project."
  - q: "Can I share Claude Projects?"
    a: "On the Claude Team plan, Projects can be shared with other team members who have access to the same Team workspace. On individual plans (Pro and Max), Projects are private to your account and cannot be shared with other users. Shared Projects allow collaborators to start conversations, view Project files, and contribute to the shared context."
  - q: "How many files can I add to a Claude Project?"
    a: "Claude Projects support multiple file uploads across a range of formats including PDFs, Word documents, spreadsheets, code files, and plain text. Anthropic does not publish a hard limit on file count, but total storage per Project is subject to a size limit. As of 2026, Projects support up to approximately 200,000 tokens of stored content across all files and instructions — matching the conversation context window."
summary: "Claude Projects are persistent workspaces that store files, custom instructions, and shared context across multiple conversations. This guide explains how to create a Project, add files, write effective instructions, and use Projects for ongoing work."
---

# How to Use Claude Projects — Complete Guide (2026)

*Last updated: 2026-06-07*

Claude Projects are one of the most powerful features for anyone who uses Claude regularly. Learning how to use Claude Projects means you can stop re-explaining your requirements, re-uploading your documents, and re-establishing context every single time you start a new conversation. A Project stores files, custom instructions, and shared background — so every conversation within it starts with Claude already knowing what it needs to know about your work.

## What are Claude Projects? — Definition

Claude Projects are persistent workspaces in Claude that maintain files, instructions, and context across multiple conversations. A standard Claude conversation is ephemeral: when you start a new chat, Claude remembers nothing from previous sessions. A Project changes this by giving you a container where:

- Uploaded files remain available across all conversations in the Project
- Custom instructions you write persist and apply to every chat in that Project
- The Project's shared context is loaded automatically at the start of each new conversation

Projects are available on Claude Pro, Max, and Team plans. The Team plan additionally allows Projects to be shared across multiple users.

## How to Use Claude Projects — Step by Step

### Step 1: Open the Projects Panel

Log in to claude.ai. In the left sidebar, look for the "Projects" section. Click "New Project" (or the "+" icon next to Projects). A dialogue will appear asking you to name the Project.

### Step 2: Name Your Project

Give the Project a clear, specific name that describes its purpose. Good names include:

- "Q3 Marketing Campaign"
- "Website Redesign — Smith & Co"
- "Python Codebase Review"
- "PhD Thesis — Chapter Drafts"
- "Client: Acme Corp — Contract Review"

The Project name is only for your reference — it does not affect Claude's behaviour.

### Step 3: Write Your Project Instructions

Project instructions are the most important part of a well-configured Project. They tell Claude who it is working with, what the task is, what tone to use, what to avoid, and any standing rules that apply to every conversation. Instructions are written in plain text — you do not need special formatting.

**Example Project instructions for a content writing Project:**

```
You are helping me write blog posts for a UK-based B2B SaaS company called Meridian Analytics. 
Our audience is data analysts and business intelligence managers at mid-market companies.
Tone: clear, professional, slightly informal. Avoid jargon where plain English works.
Always use British English spelling (e.g., "analyse" not "analyze").
Do not use bullet points in article body text — use prose paragraphs.
Article lengths: introductions 150 words, sections 200–300 words.
When I share a brief, ask clarifying questions before writing.
```

Strong instructions are specific about audience, tone, format, length, and any non-obvious constraints. See [Claude System Prompts](/claude-system-prompts/) for advanced instruction-writing techniques.

### Step 4: Upload Files to the Project

Click the "Add files" button within the Project view to upload documents that Claude should be able to reference in any conversation within this Project. Useful file types to add:

- **Reference documents:** Brand guidelines, style guides, technical specifications, previous examples of good work
- **Background material:** Research papers, reports, company information, product documentation
- **Templates:** Document structures, email formats, code boilerplate
- **Data:** Spreadsheets or CSV files Claude should be able to analyse

Claude will be able to see and reason over all uploaded files in every conversation started within the Project. You do not need to re-upload them.

### Step 5: Start a Conversation Within the Project

Click "New conversation" inside the Project view (not the main "New chat" button in the sidebar, which creates a standard conversation outside any Project). Claude will automatically receive your Project instructions and have access to all Project files.

Your first message can go straight to the task — you do not need to re-introduce the context that is already in the instructions. For example, in the content writing Project above, you can simply start with: "Here's the brief for the next post: [brief]."

### Step 6: Manage Multiple Conversations Within a Project

Each Project can contain many conversations, each focused on a different specific task. The conversations do not share each other's history — they only share the Project instructions and files. This is intentional: it keeps individual conversations focused without bloating the context with unrelated prior chats.

Good uses of multiple conversations within a Project:

- One conversation per article in a writing Project
- One conversation per feature in a software development Project
- One conversation per client meeting in a consulting Project
- One conversation per document in a contract review Project

### Step 7: Update Instructions as the Project Evolves

Project instructions are not static. As your project evolves, update the instructions to reflect new constraints, updated brand guidelines, revised requirements, or lessons learned from early conversations. Click the Project settings icon to edit instructions at any time. Changes take effect immediately in new conversations.

## Claude Projects — Key Features

| Feature | Description |
|---|---|
| Persistent instructions | Written once; apply to every conversation in the Project |
| Shared file storage | Upload files once; available in all Project conversations |
| Multiple conversations | Keep work organised by topic within a single Project |
| Team sharing (Team plan) | Share a Project with colleagues; everyone sees the same files and instructions |
| Conversation history | All conversations within a Project are stored and searchable |
| No re-uploading | Files stay in the Project until you remove them |

## What Claude Projects Are Best Used For

### Ongoing Content Creation

Writers and marketers who produce regular content benefit enormously from Projects. Upload your brand voice guide, previous published articles, and audience persona documents. Write instructions that specify your publication's style. Every new article draft starts with Claude already knowing your brand, format, and audience.

### Software Development

Developers can upload a codebase, architecture documentation, coding standards, and dependency documentation to a Project. Claude will reference these files when writing new features, reviewing code, or debugging — without you needing to re-paste the codebase each session. For long-running development Projects, this saves significant time.

### Research and Analysis

Researchers can upload academic papers, datasets, interview transcripts, or literature reviews to a Project. Claude will be able to cross-reference these documents in every conversation — useful for literature synthesis, thematic coding, and report drafting.

### Client Work

Consultants, lawyers, and account managers can create one Project per client. Upload the client's documents, background information, and any relevant correspondence. Write instructions that explain the client's industry and goals. Every conversation within that Project is grounded in the client's specific context.

### Long-Form Writing

Authors and report writers can upload chapter outlines, character notes, research files, or style guides. Claude will maintain consistency across multiple drafting sessions without forgetting what was established in earlier chapters or sections.

## Claude Projects vs. Standard Conversations — Comparison

| Feature | Standard Conversation | Claude Project Conversation |
|---|---|---|
| Context persists between chats | No | Yes (files + instructions) |
| Upload files once, use many times | No | Yes |
| Custom standing instructions | No | Yes |
| Shareable (Team plan) | No | Yes |
| Available on free plan | Yes | No (Pro, Max, Team only) |
| Best for | One-off tasks | Ongoing, recurring work |

## Tips for Getting the Most from Claude Projects

- **Write detailed instructions upfront.** Vague instructions produce inconsistent results. The time spent writing thorough instructions pays off across every future conversation.
- **Organise files logically.** Remove outdated files when they are superseded by newer versions. Stale files can create confusion if Claude draws on outdated information.
- **Create one Project per distinct context.** Do not mix unrelated work in a single Project. A Project for blog writing and a Project for software development should be kept separate.
- **Use the conversation title field.** Give each conversation a clear title so you can find it later. Claude does not do this automatically.
- **Check your instructions periodically.** Instructions written at the start of a long project can become outdated. Review and revise them every few weeks.

## Related Claude Guides

- [Claude Memory System Explained](/claude-memory-system-explained/) — How Claude's memory works across conversations and Projects
- [Claude Artifacts Guide](/claude-artifacts-guide/) — Creating and using Claude's interactive output panel
- [How to Write Your First Prompt in Claude](/how-to-write-first-prompt-claude/) — Writing effective prompts and Project instructions
- [Claude Plans Comparison](/claude-plans-comparison/) — Which plans include Claude Projects
