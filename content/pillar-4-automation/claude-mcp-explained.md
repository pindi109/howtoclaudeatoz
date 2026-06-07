---
title: "Claude MCP (Model Context Protocol) Explained — Complete Guide (2026)"
slug: claude-mcp-explained
pillar: automation
meta_description: "What is Claude MCP? Complete 2026 guide to the Model Context Protocol — how it works, the client/server model, 5 use cases, and how it differs from the API."
primary_keyword: "Claude MCP Model Context Protocol"
secondary_keywords:
  - "Model Context Protocol explained"
  - "Claude MCP tools"
  - "MCP server Claude"
affiliates: []
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "What is Claude MCP?"
    a: "MCP (Model Context Protocol) is an open standard developed by Anthropic that lets Claude connect to external tools, data sources, and services in a standardised way. Instead of every integration requiring custom code, MCP defines a common protocol so any MCP-compatible tool can plug into Claude automatically."
  - q: "How does MCP work?"
    a: "MCP uses a client/server architecture. The MCP server exposes tools, resources, or prompts that Claude can use. The MCP client (your app or Claude Desktop) connects to the server and passes requests between Claude and the server. Claude sees the available tools, decides when to call them, and the client handles the actual execution."
  - q: "What tools can I connect to Claude with MCP?"
    a: "MCP servers exist for file systems, web browsers, databases (PostgreSQL, SQLite), GitHub, Slack, Google Drive, Notion, and many more. You can also build custom MCP servers that expose your own internal tools and data sources to Claude."
summary: "The Model Context Protocol (MCP) is Anthropic's open standard for connecting Claude to external tools and data sources in a consistent, interoperable way. This guide explains the architecture, how clients and servers interact, five practical use cases, and how MCP differs from using the Claude API directly."
---

# Claude MCP (Model Context Protocol) Explained — Complete Guide (2026)

*Last updated: 2026-06-07*

Claude MCP — the Model Context Protocol — is the open standard Anthropic built to solve a fundamental problem: every tool you want to connect to Claude used to require a bespoke integration. MCP defines a shared protocol so that any tool or data source can be connected to Claude once, and then used by any MCP-compatible Claude client. Think of MCP as USB for AI tools — a standard plug that works everywhere, instead of custom adapters for every device. This guide explains what MCP is, how the client/server model works, the five most valuable use cases, and how MCP compares to calling the Claude API directly.

## What Problem Does Claude MCP Solve?

Before MCP, connecting Claude to external tools meant one of two things: either you wrote custom code for each integration (parse the API response, pass it into Claude's context, handle errors), or you relied on workflow platforms like Make.com or n8n to bridge the gap.

This worked, but it created friction. Each new tool required a new integration. Tools built for one Claude app didn't work in another. There was no standard way for Claude to discover what tools were available or how to use them.

MCP solves this by defining a universal interface. An MCP server exposes its capabilities — tools Claude can call, resources Claude can read, prompts it can use — in a standard format. Any MCP client (Claude Desktop, a custom app, an IDE extension) can connect to any MCP server and immediately understand what it can do. The ecosystem becomes composable: build an MCP server once, use it everywhere.

Anthropic released MCP as an open standard in late 2024. By 2026, the MCP ecosystem includes hundreds of community-built servers covering most major tools and platforms.

## How Claude MCP Works — The Architecture

MCP uses a client/server architecture with three main components:

### The MCP Host

The host is the application where Claude lives and where the user interacts. Examples include:

- **Claude Desktop** — Anthropic's desktop app for Mac and Windows
- **Cursor / VS Code** — AI-powered code editors with MCP support
- **Custom applications** — apps you build using the Anthropic SDK with MCP client support

The host manages the user interface, maintains the conversation, and coordinates between Claude and connected MCP servers.

### The MCP Client

The MCP client lives inside the host application. It is responsible for:

- Discovering what MCP servers are configured
- Connecting to those servers
- Fetching the list of available tools, resources, and prompts
- Routing Claude's tool call requests to the right server
- Returning tool results to Claude

Each host maintains one MCP client per connected server.

### The MCP Server

The MCP server is the external tool or data source. It exposes three types of capabilities:

**Tools**: Functions Claude can call to take actions or retrieve data. Examples: `read_file`, `search_database`, `send_slack_message`, `create_github_issue`. Claude decides when to call a tool based on context; the server executes the call and returns the result.

**Resources**: Data sources Claude can read into its context. Examples: file contents, database records, API responses, web pages. Resources are read-only — Claude can access them but not modify them through the resource interface.

**Prompts**: Reusable prompt templates the server exposes. These let server developers suggest effective prompts for their tools.

### The Communication Flow

Here is what happens when Claude uses an MCP tool:

1. User sends a message to Claude in the host app
2. Claude reasons about what it needs to do and decides to call a tool
3. The MCP client intercepts the tool call and forwards it to the relevant MCP server
4. The MCP server executes the tool (reads the file, queries the database, calls the API)
5. The server returns the result to the MCP client
6. The MCP client passes the result back to Claude
7. Claude incorporates the result into its response and either calls another tool or responds to the user

This loop can repeat multiple times within a single conversation turn, giving Claude the ability to take multiple steps to complete a task.

## How to Connect an MCP Server to Claude Desktop

Claude Desktop supports MCP servers configured in a JSON settings file. Here is a minimal example adding a file system server:

1. Install Claude Desktop from claude.ai/download
2. Open the configuration file:
   - Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
3. Add your MCP server configuration:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/yourname/Documents"]
    }
  }
}
```

4. Restart Claude Desktop. Claude can now read and write files in your Documents folder when you ask it to.

Official MCP servers from Anthropic are available at [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) and cover file systems, Git, GitHub, Slack, Google Drive, PostgreSQL, SQLite, web fetching, and more.

## 5 Claude MCP Use Cases

### Use Case 1: File System Access for Document Work

**MCP server**: `@modelcontextprotocol/server-filesystem`  
**What it enables**: Claude can read, write, and navigate your local files and folders. You can ask Claude to "summarise all the PDFs in my Reports folder", "find all spreadsheets modified this week and tell me what changed", or "write a new file combining the key points from these three documents".

This is one of the most immediately practical MCP servers — it turns Claude into a genuine file assistant rather than a chat interface.

### Use Case 2: Database Querying and Analysis

**MCP server**: `@modelcontextprotocol/server-postgres` or SQLite equivalent  
**What it enables**: Claude can query your database in plain English. Ask "how many new customers signed up last month?", "show me the top 10 products by revenue this quarter", or "find all orders over £500 that haven't shipped". Claude translates your question into SQL, runs the query via MCP, and explains the results — no SQL knowledge required.

This replaces BI tool dashboards for ad-hoc analysis and makes your database accessible to non-technical team members.

### Use Case 3: GitHub Integration for Development Workflows

**MCP server**: `@modelcontextprotocol/server-github`  
**What it enables**: Claude can read your repositories, create issues, review pull requests, and search code. Development teams use this to ask Claude to "review the open PRs and summarise what needs attention", "create a GitHub issue from this bug report", or "find all functions in the codebase that handle payments".

Combined with Claude's code understanding, this makes Claude a genuine development assistant with direct access to your project.

### Use Case 4: Slack Integration for Team Communication

**MCP server**: Community Slack MCP server  
**What it enables**: Claude can read channel messages, post updates, search message history, and manage notifications. Ask Claude to "summarise what was discussed in #product-updates this week", "post this release note to #announcements", or "find all messages mentioning the outage last Tuesday".

This is particularly useful for catching up after time off or synthesising decisions that happened across multiple Slack threads.

### Use Case 5: Custom Internal Tool Access

**MCP server**: Build your own using the MCP SDK  
**What it enables**: Any internal system you want Claude to access. Common examples: your company's internal wiki, a proprietary database, an internal API, a customer data platform. Anthropic provides SDKs in Python and TypeScript for building custom MCP servers.

Building a custom MCP server requires developer work, but once built, it exposes your internal tools to any MCP client — Claude Desktop, your custom app, and future MCP-compatible tools as the ecosystem grows.

## How Claude MCP Differs from the Claude API

MCP and the Claude API are complementary, not competing. Understanding the difference helps you use each appropriately.

| Aspect | Claude API | Claude MCP |
|---|---|---|
| **Purpose** | Call Claude to generate text responses | Give Claude access to external tools and data |
| **Who uses it** | Developers building apps | App developers + end users via Claude Desktop |
| **Integration model** | Custom per-app | Standard protocol, reusable across apps |
| **Tool access** | Manual: you pass tool results into context | Automatic: MCP client handles tool calls |
| **Setup complexity** | Code required | Server config + compatible client |
| **State** | Stateless per call (you manage history) | Client manages connection and state |

The Claude API is how you call Claude to generate text. MCP is how Claude connects to the world — reading files, querying databases, calling APIs — as part of that generation. In a complete Claude application, you typically use both: the API for Claude's intelligence layer, MCP for its tool access layer.

## Related Claude Guides

- [Claude API Getting Started](/claude-api-getting-started/)
- [Build a Claude AI Agent](/build-claude-ai-agent/)
- [Claude Make.com Integration](/claude-make-com-integration/)
- [What is Claude AI?](/what-is-claude-ai/)
- [Claude Automation Workflows — 10 Templates](/claude-automation-workflows/)
