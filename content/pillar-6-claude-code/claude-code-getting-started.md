---
title: "Claude Code — Complete Getting Started Guide (2026)"
slug: claude-code-getting-started
pillar: claude-code
meta_description: "New to Claude Code? This 2026 getting started guide covers installation, your first commands, project setup, and how to get the most from the CLI — step by step."
primary_keyword: "Claude Code getting started"
secondary_keywords:
  - "Claude Code CLI guide"
  - "Anthropic Claude Code install"
  - "Claude Code tutorial"
affiliates: []
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "What is Claude Code?"
    a: "Claude Code is Anthropic's official command-line interface (CLI) for Claude. It runs in your terminal and gives Claude direct access to your local codebase — it can read files, write code, run commands, search for patterns, and make multi-file edits. It is designed for developers who want AI assistance inside their actual development environment rather than a browser chat window."
  - q: "Is Claude Code free?"
    a: "Claude Code is available to Claude Pro and Max subscribers at no additional per-token cost within their plan limits. API users are billed for tokens consumed by Claude Code sessions. There is no separate charge for the CLI itself — you pay for the underlying Claude API usage."
  - q: "How is Claude Code different from Claude.ai?"
    a: "Claude.ai is a browser-based chat interface where you paste code manually and get responses in a conversation window. Claude Code runs in your terminal with direct file system access — it reads your actual project files, makes edits, runs tests, and executes shell commands autonomously. Claude Code is purpose-built for software development; Claude.ai is a general-purpose assistant."
summary: "Claude Code is Anthropic's terminal-based CLI that gives Claude direct access to your local codebase for reading, writing, and executing code. This guide covers installation, authentication, core commands, and the most effective ways to use Claude Code on real software projects."
hero_image: "/assets/images/heroes/photo-027-122100401427357116.jpg"
hero_alt: "Claude Code takes one npm install and an Anthropic login — then you have an AI pair programmer that reads your entire codebase, edits files, and runs shell commands directly in your terminal."
---

# Claude Code — Complete Getting Started Guide (2026)

*Last updated: 2026-06-07*

Claude Code getting started is simpler than most developers expect: install one npm package, authenticate with your Anthropic account, and you have a full AI pair programmer running inside your terminal. Claude Code is Anthropic's official CLI that gives Claude direct access to your project files, letting it read entire codebases, write and edit files, run shell commands, and navigate multi-file projects — all without copy-pasting code into a browser. This guide covers everything you need: installation, authentication, your first session, the most useful commands, and the project-level conventions that make Claude Code dramatically more powerful for serious development work.

## What is Claude Code?

Claude Code is a command-line interface built by Anthropic that embeds Claude directly into your development workflow. Unlike Claude.ai, which is a browser chat interface where you manually paste snippets, Claude Code has full access to your local file system. It can open, read, and edit files; run shell commands (with your approval); search codebases with grep and find; and make coordinated changes across dozens of files simultaneously.

Key capabilities that set Claude Code apart from browser-based AI assistants:

- **Codebase-wide context** — Claude Code indexes your project and understands the relationships between files. It knows how your `auth.py` imports from `models.py` without you explaining it.
- **Agentic task execution** — give Claude Code a high-level goal ("add rate limiting to all API endpoints") and it plans, implements, and verifies the work across multiple files.
- **CLAUDE.md project memory** — a markdown file at your project root that persists instructions, architecture notes, and conventions across every session.
- **Slash commands and MCP** — built-in commands for common actions plus the Model Context Protocol for integrating external tools and data sources.
- **Permission-gated shell access** — Claude Code can run bash commands, but it always asks before executing anything that modifies your system.

## How to Install Claude Code — Step by Step

### Step 1: Check Prerequisites

Claude Code requires Node.js 18 or higher. Check your version:

```bash
node --version
# Should output v18.0.0 or higher
```

If you need to install or upgrade Node.js, use [nvm](https://github.com/nvm-sh/nvm) (recommended) or download from nodejs.org.

### Step 2: Install the CLI

Install Claude Code globally via npm:

```bash
npm install -g @anthropic-ai/claude-code
```

Verify the installation succeeded:

```bash
claude --version
```

### Step 3: Authenticate

Run `claude` in any directory to launch the setup flow. Claude Code will open your browser to authenticate via your Anthropic account. You have two options:

- **Claude Pro or Max subscription** — authenticate with your claude.ai account. Usage counts toward your plan limits.
- **API key** — set your key as an environment variable before running:

```bash
export ANTHROPIC_API_KEY=sk-ant-your-key-here
claude
```

To make the API key permanent, add the export line to your `~/.bashrc` or `~/.zshrc`.

### Step 4: Navigate to Your Project

Claude Code works best when launched from your project root — this gives it the widest possible context for reading your files.

```bash
cd /path/to/your/project
claude
```

### Step 5: Run Your First Command

Once the Claude Code session starts, you interact through a conversational prompt. Try these first commands to get a feel for the tool:

```bash
# Ask Claude Code to summarise your project
> Summarise the architecture of this codebase in 3 paragraphs

# Ask it to find something specific
> Find all places where we call the Stripe API

# Ask for a code change
> Add input validation to the register() function in auth.py
```

Claude Code will read the relevant files, show you what it plans to do, and ask for confirmation before making any edits.

### Step 6: Set Up Your CLAUDE.md File

`CLAUDE.md` is the single most powerful Claude Code feature for sustained development work. Create a file called `CLAUDE.md` at your project root — Claude Code reads this file automatically at the start of every session. Use it to store:

- Project architecture overview
- Coding conventions and style rules
- Which files to avoid editing
- Common commands (how to run tests, linting, builds)
- Domain-specific context Claude needs to write good code

Here is a real example:

```markdown
# Project: PayTrack API

## Stack
- Python 3.12, FastAPI, PostgreSQL 15
- SQLAlchemy 2.0 (async), Alembic for migrations
- pytest for testing, ruff for linting

## Architecture
- `app/routers/` — FastAPI route handlers (one file per resource)
- `app/services/` — business logic, no DB calls here
- `app/models/` — SQLAlchemy ORM models
- `app/schemas/` — Pydantic request/response schemas

## Conventions
- All routes must have a corresponding test in `tests/routers/`
- Use `async def` for all route handlers and DB operations
- Never commit secrets — use environment variables from `config.py`
- Run `ruff check .` before marking any task done

## Commands
- Run tests: `pytest tests/ -v`
- Start dev server: `uvicorn app.main:app --reload`
- Apply migrations: `alembic upgrade head`
```

With a CLAUDE.md like this, Claude Code knows your stack, conventions, and architecture from the first message — you never need to re-explain context.

### Step 7: Explore Slash Commands

Claude Code has built-in slash commands for common workflows. Type `/` in the session to see them all. The most useful ones:

| Command | What it does |
|---|---|
| `/clear` | Clear conversation history and start fresh |
| `/compact` | Summarise the conversation to reduce token usage |
| `/model` | Switch Claude model mid-session |
| `/permissions` | Review and adjust file/shell permissions |
| `/mcp` | List connected MCP servers |
| `/cost` | Show token usage for the current session |

## Claude Code Key Features — Deep Dive

### Agentic Mode vs. Conversational Mode

Claude Code can operate in two modes. In **conversational mode**, you have a back-and-forth dialogue — ask a question, get an answer, ask a follow-up. In **agentic mode**, you hand Claude Code a multi-step task and it executes it autonomously, pausing only when it needs your approval on a significant action (like running a shell command or deleting a file).

For large tasks, agentic mode is transformative. Example:

```bash
> Refactor all database queries in the services/ directory to use 
  async SQLAlchemy 2.0 style. Run the tests after each file to 
  confirm nothing breaks.
```

Claude Code will work through each file methodically, run `pytest` after each change, and report back when done.

### Model Context Protocol (MCP)

MCP is an open standard that lets Claude Code connect to external tools and data sources. You can connect Claude Code to your database, Jira, GitHub, Linear, Figma, and dozens of other tools so Claude has live context — not just what's in your files.

To see connected MCP servers:

```bash
> /mcp
```

MCP servers are configured in your Claude Code settings file. See our [Claude MCP Explained guide](/claude-mcp-explained/) for a full walkthrough.

### Multi-File Editing

Claude Code's most impressive capability for real development work is coherent multi-file editing. Give it a task that spans many files and it maintains consistency across all of them:

```bash
> Add a `last_modified` timestamp field to the User model. 
  Update the migration, Pydantic schema, API response, and 
  relevant tests to match.
```

Claude Code traces the dependency chain across your codebase and makes all the required changes in one coordinated pass.

## What Claude Code Is Best For

Claude Code excels at tasks that are tedious but systematic:

- **Refactoring** — rename a function across 40 files, update all call sites, fix tests
- **Adding features** — implement a complete feature end-to-end from model to route to test
- **Debugging** — paste an error, Claude Code traces it back through your actual code
- **Code reviews** — ask it to review a file or diff for security issues, performance, or style
- **Writing tests** — generate comprehensive test coverage for existing functions
- **Documentation** — generate docstrings, README sections, or OpenAPI specs from code

It is less suited to tasks that require running a UI, interacting with a browser, or making real-time decisions based on live production data (though MCP integrations can bridge some of those gaps).

## Claude Code vs Claude.ai for Development

| Capability | Claude Code | Claude.ai |
|---|---|---|
| Reads your actual files | Yes | No — you paste manually |
| Makes file edits | Yes | No |
| Runs shell commands | Yes (with approval) | No |
| Remembers project context | Yes (CLAUDE.md) | Only in-session |
| Works with whole codebase | Yes | Limited by paste size |
| Best for | Production codebases | Quick questions, prototyping |
| Interface | Terminal | Browser |
| Multi-file coordination | Yes | No |

For serious development work on a real project, Claude Code is the right tool. Claude.ai is excellent for one-off questions, explaining concepts, or drafting code snippets when you are not near your development machine.

## Tips for Getting the Most from Claude Code

**Be specific about the goal, not the implementation.** Claude Code figures out the how — you just need to describe the what and why clearly.

**Use CLAUDE.md religiously.** Any time you find yourself explaining the same thing twice (your test framework, your naming conventions, your deployment setup), add it to CLAUDE.md.

**Give Claude Code permission to run tests.** The most powerful workflow is: make a change → run tests → fix failures → repeat. Claude Code can do this loop autonomously if you allow shell command execution.

**Review diffs before accepting.** Claude Code shows you exactly what it plans to change. Read the diff — Claude is very good but not infallible, and catching a wrong assumption early saves time.

**Use `/compact` on long sessions.** If you have been working for hours, the conversation history gets large and expensive. `/compact` summarises the session so you keep context without burning tokens.

## Related Claude Guides

- [Claude MCP Explained](/claude-mcp-explained/)
- [Claude API Getting Started](/claude-api-getting-started/)
- [Debug Code with Claude](/debug-code-with-claude/)
- [Claude Code Reviews](/claude-code-reviews/)
- [Building Apps with Claude as Your Co-Developer](/claude-co-developer/)
