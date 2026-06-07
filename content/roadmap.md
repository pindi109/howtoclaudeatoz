---
title: "HowToClaudeAtoZ — Public Site Roadmap"
slug: "roadmap"
pillar: "getting-started"
meta_description: "See what pages are coming to HowToClaudeAtoZ. Vote for the pages you want most — the most-upvoted get written first."
primary_keyword: "HowToClaudeAtoZ roadmap"
secondary_keywords:
  - "Claude AI guides coming soon"
  - "vote for Claude content"
  - "Claude encyclopaedia roadmap"
affiliates: []
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "How do I vote for a page?"
    a: "Click any card on the roadmap. This opens the GitHub Issue for that page — click the 👍 reaction to upvote it. Pages with the most votes get written first."
  - q: "How often is the roadmap updated?"
    a: "The roadmap is rebuilt automatically on every site deploy. Status changes (Planned → In Progress → Published) are reflected within hours."
  - q: "Can I suggest a page that is not on the roadmap?"
    a: "Yes — use the Suggest a Page button on any article to open a pre-filled GitHub Issue with your suggestion."
summary: "The public roadmap for HowToClaudeAtoZ showing all planned, in-progress, and published pages. Upvote what you want next."
---

# HowToClaudeAtoZ Public Roadmap

Every page on this site starts as a GitHub Issue. That means you can see exactly what is being worked on, what is planned, and what has already been published — and more importantly, you can vote on what gets written next. The most-upvoted issues move to the top of the writing queue. If there is a guide you need, this is the page to visit and the 👍 reaction is the mechanism that gets it written.

The roadmap updates automatically on every site deploy. When a page moves from planned to in progress, or from in progress to published, the status card changes. You do not need to check GitHub directly — this page reflects the current state of the site.

## How Voting Works

The kanban board below shows all tracked pages across three columns: Planned, In Progress, and Published. Each card links directly to the GitHub Issue for that page.

To vote for a page you want written:

1. Click the card for the page you want.
2. This opens the GitHub Issue in a new tab.
3. Scroll to the bottom of the issue and click the 👍 reaction.
4. That is all. Your vote is counted.

You need a GitHub account to vote. If you do not have one, creating a free account takes two minutes and is worth it — the same account lets you contribute prompts to the [Prompt Library](/prompt-library/), suggest new pages, and comment on issues to explain why a particular guide matters to you.

The votes are visible on each issue and are checked regularly when deciding which planned pages to move into the writing queue. A page with fifty 👍 reactions will be prioritised over one with two, everything else being equal. If you want a page written urgently, sharing the issue link with others who would find it useful is the most effective thing you can do.

<div id="roadmap-board" style="margin:2rem 0;">
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.5rem;">

    <div id="col-planned" style="background:#1c1917;border-radius:12px;padding:1.25rem;border-top:4px solid #3b82f6;">
      <h3 style="color:#93c5fd;font-size:0.85rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;margin:0 0 1rem 0;">📋 Planned</h3>
      <div id="items-planned"><p style="color:#57534e;font-size:0.85rem;">Loading...</p></div>
    </div>

    <div id="col-inprogress" style="background:#1c1917;border-radius:12px;padding:1.25rem;border-top:4px solid #d97706;">
      <h3 style="color:#fbbf24;font-size:0.85rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;margin:0 0 1rem 0;">✍️ In Progress</h3>
      <div id="items-inprogress"><p style="color:#57534e;font-size:0.85rem;">Loading...</p></div>
    </div>

    <div id="col-published" style="background:#1c1917;border-radius:12px;padding:1.25rem;border-top:4px solid #22c55e;">
      <h3 style="color:#86efac;font-size:0.85rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;margin:0 0 1rem 0;">✅ Published</h3>
      <div id="items-published"><p style="color:#57534e;font-size:0.85rem;">Loading...</p></div>
    </div>

  </div>
  <script>
  (function(){
    function card(item){
      return '<a href="'+item.url+'" target="_blank" rel="noopener" style="display:block;background:#292524;border-radius:8px;padding:0.85rem 1rem;margin-bottom:0.6rem;text-decoration:none;transition:background 0.15s;" onmouseover="this.style.background=\'#3b3533\'" onmouseout="this.style.background=\'#292524\'">'
        +'<div style="display:flex;justify-content:space-between;align-items:flex-start;gap:0.5rem;">'
        +'<span style="color:#e7e5e4;font-size:0.875rem;font-weight:500;line-height:1.4;">'+item.title+'</span>'
        +(item.reactions&&item.reactions['+1']>0?'<span style="color:#d97706;font-size:0.8rem;white-space:nowrap;margin-top:2px;">👍 '+item.reactions['+1']+'</span>':'')
        +'</div>'
        +'<p style="color:#57534e;font-size:0.75rem;margin-top:0.3rem;">Click to vote →</p>'
        +'</a>';
    }
    fetch('/data/roadmap.json').then(r=>r.json()).then(function(data){
      ['planned','in_progress','published'].forEach(function(key){
        var col = key==='in_progress'?'inprogress':key;
        var el = document.getElementById('items-'+col);
        if(!el) return;
        var items = data[key]||[];
        if(!items.length){ el.innerHTML='<p style="color:#57534e;font-size:0.85rem;">Nothing here yet.</p>'; return; }
        el.innerHTML = items.map(card).join('');
      });
    }).catch(function(){ document.getElementById('roadmap-board').innerHTML='<p style="color:#78716c;">Roadmap loading failed — <a href="https://github.com/pindi109/howtoclaudeatoz/issues?q=label%3Aroadmap" style="color:#d97706;">view on GitHub</a></p>'; });
  })();
  </script>
</div>

## What's Coming Next

The pages currently in the writing queue are the ones in the In Progress column above. These are actively being researched and drafted and will be published within the next few weeks.

The Planned column represents the full backlog. Every issue there has been scoped — we know what the page needs to cover, what questions it should answer, and roughly how long it will be. What determines the order in which they are written is primarily community votes, with secondary weight given to pages that fill obvious gaps in the existing content.

A few areas that are heavily requested and moving up the queue:

**Claude for coding workflows.** Several issues cover using Claude Code for real development tasks — reviewing pull requests, writing tests from existing code, explaining legacy codebases, and generating documentation from source. These have consistently high upvote counts and are moving into production.

**Comparison pages.** Pages that compare Claude to specific alternatives — GPT-4o, Gemini, Copilot — are among the most searched topics in the space. A set of rigorous, benchmark-backed comparison pages is planned and will be published as a batch.

**Prompt engineering deep dives.** The fundamentals guide already covers the basics. What the community is asking for is specificity: how to write prompts for particular industries, how to handle edge cases, how to build prompt libraries for teams. These are in the queue.

**Claude API and developer content.** The Claude Code and developer section of the site is the least complete pillar. Issues covering the API, MCP (Model Context Protocol), tool use, and building Claude-powered applications are planned and will be a focus over the coming months.

## Suggest a Page

The roadmap only covers what has already been thought of. If you need a guide that is not on the list, open a new suggestion and it will be considered for the roadmap.

To suggest a page, [open a new GitHub Issue](https://github.com/pindi109/howtoclaudeatoz/issues/new) with a title that describes the page you want and a brief note explaining what you are trying to accomplish and why existing guides do not cover it. The more specific you are about the use case — "I need to know how to use Claude to process PDF invoices and extract line items into a spreadsheet" rather than "guide about PDFs" — the easier it is to scope and write the right page.

Suggestions that come with clear use cases and detail consistently get added to the roadmap within a week of being filed. Suggestions that gather 👍 reactions from other community members are treated as high-priority additions.

## Related Guides

- [Getting Started with Claude](/getting-started-with-claude/) — if you are new to Claude and want to know what it can actually do
- [Prompt Library](/prompt-library/) — community-contributed prompts you can use right now, ranked by upvotes
- [Claude for Business Workflows](/claude-for-business/) — how teams are using Claude to automate repeatable tasks
- [Advanced Claude Techniques](/advanced-claude-techniques/) — power-user features including Projects, memory, and multi-step reasoning
