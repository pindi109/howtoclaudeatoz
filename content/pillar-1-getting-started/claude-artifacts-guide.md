---
title: "Claude Artifacts — What They Are and How to Use Them (2026)"
slug: claude-artifacts-guide
pillar: getting-started
meta_description: "Claude Artifacts explained: what they are, how to create them, and all artifact types including code, HTML, SVG, and documents. Complete 2026 guide."
primary_keyword: "Claude Artifacts"
secondary_keywords:
  - "Claude Artifacts guide"
  - "Claude code artifacts"
  - "Claude HTML artifacts"
affiliates: []
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "What are Claude Artifacts?"
    a: "Claude Artifacts are self-contained, interactive outputs that Claude displays in a dedicated side panel alongside the conversation. When Claude generates a substantial, standalone piece of content — such as a working webpage, a code file, a formatted document, or an SVG image — it can present it as an Artifact so you can preview, interact with, and iterate on it without cluttering the chat window."
  - q: "Can I download Claude Artifacts?"
    a: "Yes. Claude Artifacts include a copy button that lets you copy the full content to your clipboard. For code and text artifacts, you can paste the copied content directly into your development environment, text editor, or document. As of 2026, direct file download from the Artifacts panel is available for certain content types via the download icon that appears in the Artifact toolbar."
  - q: "What types of Artifacts can Claude create?"
    a: "Claude can create several types of Artifacts: code files (any programming language), HTML webpages (rendered and interactive), React components (rendered live), SVG graphics (rendered visually), Markdown documents, plain text files, and structured data files like JSON or CSV. The Artifact type is determined automatically based on the content Claude generates."
summary: "Claude Artifacts are interactive output panels that display self-contained content — code, webpages, documents, images — alongside the conversation. This guide explains all artifact types, how to create them, and how to iterate on them effectively."
hero_image: "/assets/images/heroes/photo-070-122100373449357116.jpg"
hero_alt: "Claude Artifacts open in a dedicated side panel — so instead of digging through raw code in a chat message, you get a live, interactive preview of HTML pages, SVG graphics, React components, and more."
---

# Claude Artifacts — What They Are and How to Use Them (2026)

*Last updated: 2026-06-07*

Claude Artifacts are one of the most useful and underused features in Claude's interface. Claude Artifacts appear as a dedicated side panel when Claude generates a substantial, self-contained output — a working webpage, a formatted document, a code file, an SVG graphic, or a React component. Instead of scrolling through raw code or text buried inside a chat message, you get a clean, interactive preview alongside the conversation. This guide explains every type of Artifact, how to create them, and how to iterate on them effectively.

## What are Claude Artifacts? — Definition

A Claude Artifact is a self-contained piece of content rendered in a separate panel to the right of the conversation window. Artifacts appear automatically when Claude determines that the output would be better presented independently rather than inline in the chat. They allow you to:

- **Preview** content in its rendered form (see HTML as a webpage, SVG as an image)
- **Interact** with live React components and simple web apps
- **Copy** the full content with one click
- **Iterate** by asking Claude to update the Artifact, which generates a new version in the same panel

Artifacts were introduced by Anthropic as a way to make Claude more useful for technical and creative output tasks. They are particularly valuable for developers, designers, and content creators who want to see results immediately rather than copy-pasting into other tools.

## All Claude Artifact Types — With Use Cases

### Code Artifacts

A code Artifact displays a code file in a syntax-highlighted panel with a copy button. Claude automatically creates a code Artifact when it generates a substantial standalone code file (rather than a short inline snippet).

**Common use cases:**
- Full Python scripts, functions, or classes
- JavaScript and TypeScript files
- SQL queries
- Shell scripts
- Configuration files (YAML, TOML, JSON)

**When it appears:** When you ask Claude to "write a Python script that does X" or "create a SQL query for Y" and the output is substantial enough to warrant a standalone display.

### HTML Artifacts (Rendered Webpages)

An HTML Artifact renders an HTML (HyperText Markup Language) file live in the panel — you see the actual webpage, not just the source code. You can interact with the rendered page: click buttons, fill in forms, and see how the layout behaves.

**Common use cases:**
- Landing page mockups
- Email templates
- Simple data visualisations with inline CSS and JavaScript
- Interactive calculators or tools
- Portfolio or profile page prototypes

**When it appears:** When you ask Claude to "build a webpage," "create an HTML email template," or "make an interactive tool in HTML."

### React Component Artifacts

React Artifacts render live React (JavaScript library for building user interfaces) components directly in the panel. You can see how the component looks and behaves, interact with its state, and iterate on the design without any build step.

**Common use cases:**
- UI (user interface) component prototypes
- Interactive dashboards
- Data visualisation components
- Form builders
- Mini-applications

**When it appears:** When you ask Claude to "create a React component" or "build this as a React app." Claude will use React with Tailwind CSS for styling by default.

### SVG Artifacts (Rendered Graphics)

An SVG (Scalable Vector Graphics) Artifact renders the graphic visually in the panel so you can see the image directly rather than reading the XML source code. SVG files scale to any size without losing quality.

**Common use cases:**
- Simple icons and logos
- Diagrams and flowcharts
- Infographic elements
- Charts and graphs
- Geometric illustrations

**When it appears:** When you ask Claude to "create an SVG icon," "draw a simple diagram as SVG," or "generate a vector graphic of X."

### Markdown Document Artifacts

A Markdown Artifact displays a formatted document with headings, bullet points, tables, bold text, and other formatting rendered cleanly. Markdown is a plain-text formatting syntax widely used for documentation, README files, and content writing.

**Common use cases:**
- Technical documentation
- README files for software projects
- Structured reports
- Blog post drafts
- Meeting notes or agendas

**When it appears:** When you ask Claude to "write a README," "draft a report," or produce any long-form structured document that benefits from clean formatting.

### Plain Text Artifacts

A plain text Artifact displays content without any formatting markup. Useful for outputs that need to be pasted into systems that do not support formatting.

**Common use cases:**
- Email drafts (to paste into email clients)
- Social media copy
- Script text for voiceovers
- Legal clauses or contract text
- Any content intended for a plain-text destination

### JSON and Data Artifacts

A JSON (JavaScript Object Notation) or structured data Artifact displays data in a clean, readable format that can be copied directly into an application, database, or API.

**Common use cases:**
- API response schemas
- Configuration file generation
- Dataset creation
- Mock data for development and testing
- Structured content for import into CMS (Content Management System) platforms

## How to Create Claude Artifacts — Step by Step

### Step 1: Ask Claude to Create a Self-Contained Output

Artifacts appear automatically when your request produces substantial standalone content. You do not need to explicitly say "create an Artifact." Simply ask for the output type you want.

Prompts that reliably produce Artifacts:
- "Write a Python script that [task]."
- "Build an HTML page that [description]."
- "Create a React component for [UI element]."
- "Draw an SVG diagram of [subject]."
- "Write a Markdown README for this project."

### Step 2: View and Interact With the Artifact

When an Artifact appears, it displays in a panel to the right of the conversation. For HTML and React Artifacts, you will see the rendered output — click around to test interactive elements. For code Artifacts, you will see syntax-highlighted source code. Use the toolbar at the top of the Artifact panel to:

- **Copy** the full content to clipboard
- **Download** (where available for the content type)
- **Switch between preview and source code** (for HTML and React Artifacts)

### Step 3: Iterate on the Artifact

To update an Artifact, simply continue the conversation with your revision instructions. Claude will update the same Artifact in the panel rather than posting the entire output again in the chat.

**Effective iteration prompts:**
- "Change the background colour to dark blue and the text to white."
- "Add a 'Submit' button that validates the form fields before submitting."
- "Refactor this script to use a class instead of standalone functions."
- "Make the heading larger and centre-align the layout."

Each iteration creates a new version of the Artifact. You can navigate between versions using the arrows in the Artifact panel toolbar, which lets you compare iterations.

### Step 4: Copy or Export the Finished Artifact

When you are satisfied with the output, click the copy button to copy the content to your clipboard. Paste it directly into:
- Your code editor for code and scripts
- Your CMS or document editor for text content
- An image editor or SVG file for graphics
- A design tool or email sender for HTML content

## Claude Artifacts — Key Tips for Better Results

- **Describe the complete end state upfront.** For complex Artifacts, explain all the requirements in your initial prompt rather than adding features piecemeal. "Build an HTML page with a header, three feature cards with icons, a contact form, and a dark footer" produces a more complete first draft than "Build an HTML page" followed by individual requests.

- **Use "update" rather than "rewrite" for iterations.** Saying "update the button colour" is clearer than "rewrite it with a different button colour." This helps Claude understand that you want a targeted change, not a full regeneration.

- **Request specific libraries when you have preferences.** If you want Chart.js for a visualisation, Tailwind for styling, or a specific Python version, say so. Claude defaults to common choices but will follow your preferences.

- **Export early and often.** Copy your Artifact at meaningful milestones so you have a working version to fall back on if an iteration goes in the wrong direction.

## Artifact Types — Summary Table

| Artifact Type | Rendered? | Best For |
|---|---|---|
| Code | No (syntax-highlighted) | Scripts, functions, full files |
| HTML | Yes (live preview) | Webpages, emails, tools |
| React | Yes (live interactive) | UI components, mini-apps |
| SVG | Yes (rendered image) | Icons, diagrams, graphics |
| Markdown | Yes (formatted) | Documentation, reports |
| Plain text | No | Email drafts, plain copy |
| JSON / data | No (formatted) | API schemas, config, mock data |

## Related Claude Guides

- [How to Use Claude Projects](/how-to-use-claude-projects/) — Save and reuse Artifacts across conversations with Projects
- [How to Write Your First Prompt in Claude](/how-to-write-first-prompt-claude/) — Structure prompts to get better Artifact outputs
- [Claude Context Window Explained](/claude-context-window-explained/) — How to work with large files and long outputs
- [How to Write Blog Posts with Claude](/how-to-write-blog-posts-with-claude/) — Using Markdown Artifacts for content creation
