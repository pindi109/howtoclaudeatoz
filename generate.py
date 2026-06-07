#!/usr/bin/env python3
"""
generate.py — Static site generator for howtoclaudeatoz.com
"""

import os
import re
import json
import shutil
import subprocess
import urllib.request
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# YAML parsing — try PyYAML, fall back to simple regex parser
# ---------------------------------------------------------------------------
try:
    import yaml
    def parse_yaml(text):
        return yaml.safe_load(text)
except ImportError:
    def parse_yaml(text):
        """Minimal YAML parser supporting str, int, bool, and simple lists."""
        result = {}
        lines = text.splitlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            # Skip blank lines and comments
            if not line.strip() or line.strip().startswith('#'):
                i += 1
                continue
            # List item under a key (indented with - )
            list_match = re.match(r'^  - (.+)$', line)
            if list_match:
                i += 1
                continue  # handled inside key parsing below
            key_match = re.match(r'^(\w[\w_-]*):\s*(.*)', line)
            if key_match:
                key = key_match.group(1)
                val = key_match.group(2).strip()
                if val == '':
                    # possible block list
                    items = []
                    i += 1
                    while i < len(lines) and re.match(r'^  - ', lines[i]):
                        item_val = lines[i].strip()[2:].strip().strip('"').strip("'")
                        items.append(item_val)
                        i += 1
                    result[key] = items
                    continue
                else:
                    # Strip inline quotes
                    if (val.startswith('"') and val.endswith('"')) or \
                       (val.startswith("'") and val.endswith("'")):
                        val = val[1:-1]
                    # Booleans
                    if val.lower() == 'true':
                        val = True
                    elif val.lower() == 'false':
                        val = False
                    else:
                        # Try integer
                        try:
                            val = int(val)
                        except ValueError:
                            pass
                    result[key] = val
            i += 1
        return result


# ---------------------------------------------------------------------------
# Frontmatter parser
# ---------------------------------------------------------------------------
def parse_frontmatter(raw):
    """
    Split raw file content into (frontmatter_dict, body_str).
    Expects content delimited by --- markers.
    """
    raw = raw.lstrip('\ufeff')  # strip BOM if present
    if not raw.startswith('---'):
        return {}, raw
    # Find the closing ---
    rest = raw[3:]
    end = rest.find('\n---')
    if end == -1:
        return {}, raw
    yaml_text = rest[:end]
    body = rest[end + 4:].lstrip('\n')
    fm = parse_yaml(yaml_text) or {}
    return fm, body


# ---------------------------------------------------------------------------
# Markdown → HTML converter
# ---------------------------------------------------------------------------
def convert_tables(md):
    """Pre-process: convert markdown tables to HTML before line-by-line parsing."""
    lines = md.split('\n')
    result = []
    i = 0
    while i < len(lines):
        if lines[i].startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s\-:|]+\|', lines[i + 1]):
            header_cells = [c.strip() for c in lines[i].strip('|').split('|')]
            i += 2  # skip header + separator
            html = ['<table>', '<thead>', '<tr>']
            for h in header_cells:
                html.append(f'<th>{h}</th>')
            html += ['</tr>', '</thead>', '<tbody>']
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip('|').split('|')]
                html.append('<tr>')
                for c in cells:
                    html.append(f'<td>{c}</td>')
                html.append('</tr>')
                i += 1
            html += ['</tbody>', '</table>']
            result.append('\n'.join(html))
        else:
            result.append(lines[i])
            i += 1
    return '\n'.join(result)


def markdown_to_html(md):
    """
    Convert a subset of Markdown to HTML.
    Supports: h1-h4, **bold**, *italic*, `code`, numbered lists,
    bullet lists, blockquotes, horizontal rules, tables, paragraphs.
    """
    md = convert_tables(md)
    lines = md.split('\n')
    html_parts = []
    in_ul = False
    in_ol = False
    ol_counter = 0

    def close_lists():
        nonlocal in_ul, in_ol, ol_counter
        parts = []
        if in_ul:
            parts.append('</ul>')
            in_ul = False
        if in_ol:
            parts.append('</ol>')
            in_ol = False
            ol_counter = 0
        return parts

    def inline(text):
        """Apply inline formatting."""
        # Bold (must come before italic)
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)
        # Italic
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        text = re.sub(r'_(.+?)_', r'<em>\1</em>', text)
        # Inline code
        text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
        # Links [text](url)
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
        return text

    i = 0
    while i < len(lines):
        line = lines[i]

        # Heading 4
        if line.startswith('#### '):
            html_parts.extend(close_lists())
            html_parts.append(f'<h4>{inline(line[5:].strip())}</h4>')
            i += 1
            continue

        # Heading 3
        if line.startswith('### '):
            html_parts.extend(close_lists())
            html_parts.append(f'<h3>{inline(line[4:].strip())}</h3>')
            i += 1
            continue

        # Heading 2
        if line.startswith('## '):
            html_parts.extend(close_lists())
            html_parts.append(f'<h2>{inline(line[3:].strip())}</h2>')
            i += 1
            continue

        # Heading 1
        if line.startswith('# '):
            html_parts.extend(close_lists())
            html_parts.append(f'<h1>{inline(line[2:].strip())}</h1>')
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^[-*_]{3,}\s*$', line):
            html_parts.extend(close_lists())
            html_parts.append('<hr>')
            i += 1
            continue

        # Blockquote
        if line.startswith('> '):
            html_parts.extend(close_lists())
            html_parts.append(f'<blockquote><p>{inline(line[2:].strip())}</p></blockquote>')
            i += 1
            continue

        # Ordered list item
        ol_match = re.match(r'^\d+\.\s+(.*)', line)
        if ol_match:
            if not in_ol:
                html_parts.extend(close_lists())
                html_parts.append('<ol>')
                in_ol = True
            html_parts.append(f'<li>{inline(ol_match.group(1).strip())}</li>')
            i += 1
            continue

        # Unordered list item
        ul_match = re.match(r'^[-*+]\s+(.*)', line)
        if ul_match:
            if not in_ul:
                html_parts.extend(close_lists())
                html_parts.append('<ul>')
                in_ul = True
            html_parts.append(f'<li>{inline(ul_match.group(1).strip())}</li>')
            i += 1
            continue

        # Blank line
        if line.strip() == '':
            html_parts.extend(close_lists())
            html_parts.append('')
            i += 1
            continue

        # Regular paragraph line — collect until blank or structural element
        html_parts.extend(close_lists())
        para_lines = [line]
        i += 1
        while i < len(lines):
            next_line = lines[i]
            if (next_line.strip() == '' or
                    next_line.startswith('#') or
                    next_line.startswith('> ') or
                    re.match(r'^[-*_]{3,}\s*$', next_line) or
                    re.match(r'^\d+\.\s+', next_line) or
                    re.match(r'^[-*+]\s+', next_line)):
                break
            para_lines.append(next_line)
            i += 1
        para_text = ' '.join(para_lines).strip()
        if para_text:
            html_parts.append(f'<p>{inline(para_text)}</p>')

    html_parts.extend(close_lists())

    # Join and clean up excessive blank lines
    html = '\n'.join(html_parts)
    html = re.sub(r'\n{3,}', '\n\n', html)
    return html.strip()


# ---------------------------------------------------------------------------
# Schema builders
# ---------------------------------------------------------------------------
BASE_URL = 'https://howtoclaudeatoz.com'


def build_article_schema(fm, slug):
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": fm.get('title', ''),
        "description": fm.get('meta_description', ''),
        "url": f"{BASE_URL}/{slug}/",
        "image": f"{BASE_URL}/og/{slug}.png",
        "datePublished": str(fm.get('date_published', '')),
        "dateModified": str(fm.get('date_modified', '')),
        "author": {
            "@type": "Person",
            "name": "Pindi Sahota",
            "url": f"{BASE_URL}/about/"
        },
        "publisher": {
            "@type": "Organization",
            "name": "HowToClaudeAtoZ",
            "url": BASE_URL,
            "logo": {
                "@type": "ImageObject",
                "url": f"{BASE_URL}/logo.svg"
            }
        }
    }
    return json.dumps(schema, indent=2)


def build_faq_schema(faq_list):
    if not faq_list:
        return ''
    entities = []
    for item in faq_list:
        if isinstance(item, dict) and 'q' in item and 'a' in item:
            entities.append({
                "@type": "Question",
                "name": item['q'],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": item['a']
                }
            })
    if not entities:
        return ''
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities
    }
    return json.dumps(schema, indent=2)


def build_breadcrumb_schema(fm, slug):
    pillar = fm.get('pillar', '')
    pillar_name = pillar_display_name(pillar)
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": f"{BASE_URL}/"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": pillar_name,
                "item": f"{BASE_URL}/{pillar}/"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": fm.get('title', ''),
                "item": f"{BASE_URL}/{slug}/"
            }
        ]
    }
    return json.dumps(schema, indent=2)


def build_howto_schema(fm, slug):
    if not fm.get('howto'):
        return ''
    steps = fm.get('howto_steps', [])
    step_list = []
    for idx, step in enumerate(steps, 1):
        if isinstance(step, dict):
            step_list.append({
                "@type": "HowToStep",
                "position": idx,
                "name": step.get('name', f'Step {idx}'),
                "text": step.get('text', '')
            })
        elif isinstance(step, str):
            step_list.append({
                "@type": "HowToStep",
                "position": idx,
                "name": step,
                "text": step
            })
    schema = {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": fm.get('title', ''),
        "description": fm.get('meta_description', ''),
        "url": f"{BASE_URL}/{slug}/",
        "step": step_list
    }
    return json.dumps(schema, indent=2)


# ---------------------------------------------------------------------------
# Pillar helpers
# ---------------------------------------------------------------------------
PILLAR_NAMES = {
    'getting-started':    'Getting Started with Claude',
    'writing-content':    'Claude for Writing & Content',
    'seo':                'Claude for SEO',
    'automation':         'Claude for Automation & AI Workflows',
    'video-voice':        'Claude for Video, Voice & Creative Media',
    'claude-code':        'Claude Code & Developer Use Cases',
    'business':           'Claude for Business & Productivity',
    'advanced':           'Advanced Claude',
    'comparison-pages':   'Comparison Pages',
}


def pillar_display_name(pillar_slug):
    return PILLAR_NAMES.get(pillar_slug, pillar_slug.replace('-', ' ').title())


# ---------------------------------------------------------------------------
# Template rendering
# ---------------------------------------------------------------------------
def render_template(template_str, variables):
    """Replace {{ key }} placeholders with values from the variables dict."""
    def replacer(m):
        key = m.group(1).strip()
        return str(variables.get(key, ''))
    return re.sub(r'\{\{\s*([\w_]+)\s*\}\}', replacer, template_str)


# ---------------------------------------------------------------------------
# Visible HTML helpers
# ---------------------------------------------------------------------------
def build_faq_html(faq_list):
    if not faq_list:
        return ''
    parts = ['<section class="faq-block"><h2>Frequently Asked Questions</h2><dl>']
    for item in faq_list:
        if isinstance(item, dict) and 'q' in item and 'a' in item:
            parts.append(f'<dt>{item["q"]}</dt>')
            parts.append(f'<dd>{item["a"]}</dd>')
    parts.append('</dl></section>')
    return '\n'.join(parts)


def build_breadcrumbs_html(fm, slug):
    pillar = fm.get('pillar', '')
    pillar_name = pillar_display_name(pillar)
    title = fm.get('title', slug)
    return (
        f'<nav aria-label="Breadcrumb" class="breadcrumbs">'
        f'<ol>'
        f'<li><a href="/">Home</a></li>'
        f'<li><a href="/{pillar}/">{pillar_name}</a></li>'
        f'<li aria-current="page">{title}</li>'
        f'</ol>'
        f'</nav>'
    )


def build_affiliate_disclosure(fm):
    affiliates = fm.get('affiliates', [])
    if affiliates:
        return (
            '<p class="affiliate-disclosure text-sm text-gray-500 '
            'border-l-4 border-amber-400 pl-3 my-4">'
            '<em>This page contains affiliate links. If you purchase through them, '
            'I may earn a commission at no extra cost to you.</em></p>'
        )
    return ''


def build_author_byline(fm):
    date_mod = fm.get('date_modified', '')
    return (
        f'<p class="text-sm text-gray-500">By '
        f'<a href="/about/" class="underline">Pindi Sahota</a> '
        f'&middot; Last updated: {date_mod}</p>'
    )


def first_n_sentences(text, n=2):
    """Return the first n sentences from a string."""
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return ' '.join(sentences[:n])


# ---------------------------------------------------------------------------
# Homepage nav HTML
# ---------------------------------------------------------------------------
# Premium pillar card metadata — display name, short descriptor, card number
PILLAR_META = {
    'getting-started': ('Getting Started',    'Your first steps with Claude AI',       '01'),
    'writing-content': ('Writing & Content',  'Blogs, copy, emails and social',        '02'),
    'seo':             ('Claude for SEO',     'Rank higher with AI-assisted SEO',      '03'),
    'automation':      ('Automation',         'Agents, workflows and integrations',    '04'),
    'video-voice':     ('Video & Voice',      'Scripts, voiceovers and AI video',      '05'),
    'claude-code':     ('Claude Code',        'Build faster with Claude as co-pilot',  '06'),
    'business':        ('Business',           'Streamline operations and decisions',   '07'),
    'advanced':        ('Advanced',           'Prompting, models and deep dives',      '08'),
}

# Inline SVGs — gold stroke, 36×36 viewBox, stroke="currentColor"
PILLAR_SVGS = {
    'getting-started': '<svg class="pillar-icon" viewBox="0 0 36 36" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="18" cy="18" r="13"/><path d="M23 13l-5 9-5-2 5-9 5 2z"/><circle cx="18" cy="18" r="2" fill="currentColor" stroke="none" opacity=".6"/></svg>',
    'writing-content': '<svg class="pillar-icon" viewBox="0 0 36 36" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 26l2-6 13-13 4 4-13 13-6 2z"/><path d="M27 7l2 2"/><line x1="10" y1="30" x2="26" y2="30"/><line x1="16" y1="20" x2="20" y2="16"/></svg>',
    'seo':             '<svg class="pillar-icon" viewBox="0 0 36 36" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="15" cy="15" r="9"/><line x1="22" y1="22" x2="30" y2="30"/><path d="M11 19l3-5 3 3 3-5"/></svg>',
    'automation':      '<svg class="pillar-icon" viewBox="0 0 36 36" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="14" y="3" width="8" height="6" rx="1.5"/><rect x="3" y="27" width="8" height="6" rx="1.5"/><rect x="25" y="27" width="8" height="6" rx="1.5"/><line x1="18" y1="9" x2="18" y2="18"/><line x1="18" y1="18" x2="7" y2="27"/><line x1="18" y1="18" x2="29" y2="27"/><circle cx="18" cy="18" r="2.5" fill="currentColor" stroke="none" opacity=".5"/></svg>',
    'video-voice':     '<svg class="pillar-icon" viewBox="0 0 36 36" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="11" width="22" height="16" rx="2"/><path d="M26 16l6-4v10l-6-4"/><path d="M9 23V15"/><path d="M13 23v-5"/><path d="M17 23v-8"/><path d="M21 23v-3"/></svg>',
    'claude-code':     '<svg class="pillar-icon" viewBox="0 0 36 36" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="6" width="30" height="24" rx="2.5"/><line x1="3" y1="12" x2="33" y2="12"/><path d="M10 19l5 4-5 4"/><line x1="20" y1="27" x2="26" y2="27"/><circle cx="8" cy="9" r="1" fill="currentColor" stroke="none"/><circle cx="12" cy="9" r="1" fill="currentColor" stroke="none"/></svg>',
    'business':        '<svg class="pillar-icon" viewBox="0 0 36 36" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="13" width="28" height="17" rx="2"/><path d="M13 13v-2a2 2 0 012-2h6a2 2 0 012 2v2"/><line x1="4" y1="22" x2="32" y2="22"/><line x1="17" y1="22" x2="17" y2="26"/><line x1="19" y1="22" x2="19" y2="26"/></svg>',
    'advanced':        '<svg class="pillar-icon" viewBox="0 0 36 36" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="18" cy="18" r="6"/><line x1="18" y1="4" x2="18" y2="8"/><line x1="18" y1="28" x2="18" y2="32"/><line x1="4" y1="18" x2="8" y2="18"/><line x1="28" y1="18" x2="32" y2="18"/><line x1="8.5" y1="8.5" x2="11.5" y2="11.5"/><line x1="24.5" y1="8.5" x2="27.5" y2="5.5"/><line x1="8.5" y1="27.5" x2="11.5" y2="24.5"/><line x1="24.5" y1="27.5" x2="27.5" y2="24.5"/></svg>',
}


def build_pillar_links(pages_by_pillar):
    """
    Build {{ pillar_links }} — premium dark 4×2 grid of pillar cards.
    Each card: watermark number, inline SVG icon, title, descriptor,
    article count badge, 4 article links, Explore all CTA.
    """
    card_parts = []
    pillar_order = [k for k in PILLAR_NAMES if k != 'comparison-pages']

    for idx, pillar_slug in enumerate(pillar_order):
        pages = pages_by_pillar.get(pillar_slug, [])
        meta  = PILLAR_META.get(pillar_slug, (pillar_slug, '', '0' + str(idx + 1)))
        display_name, descriptor, num = meta
        svg   = PILLAR_SVGS.get(pillar_slug, '')
        total = len(pages)
        delay = idx * 80   # 80ms stagger per card

        sorted_pages = sorted(pages, key=lambda x: x.get('title', ''))
        links_html = ''
        for fm in sorted_pages[:4]:
            slug  = fm.get('slug', '')
            title = fm.get('title', slug)
            # Truncate long titles to keep layout clean
            if len(title) > 52:
                title = title[:49] + '…'
            links_html += (
                f'<li class="pillar-link-item">'
                f'<a href="/{slug}/">{title}</a>'
                f'</li>\n'
            )

        card_parts.append(
            f'<article class="pillar-card" data-reveal-delay="{delay}" id="{pillar_slug}">\n'
            f'  <span class="pillar-num" aria-hidden="true">{num}</span>\n'
            f'  {svg}\n'
            f'  <h3 class="pillar-title">{display_name}</h3>\n'
            f'  <p class="pillar-desc">{descriptor}</p>\n'
            f'  <span class="pillar-badge">{total} guides</span>\n'
            f'  <ul class="pillar-article-links">\n{links_html}  </ul>\n'
            f'  <a href="/#{ pillar_slug}" class="pillar-cta">Explore all <span class="pillar-cta-arrow">→</span></a>\n'
            f'</article>\n'
        )

    return '\n'.join(card_parts)


def build_page_nav_links(pages_by_pillar):
    """Alias used for {{ page_nav_links }} in page template (same content)."""
    return build_pillar_links(pages_by_pillar)


# ---------------------------------------------------------------------------
# File generation helpers
# ---------------------------------------------------------------------------
def generate_sitemap(all_pages, today_str):
    urls = [
        f"""  <url>
    <loc>{BASE_URL}/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
    <lastmod>{today_str}</lastmod>
  </url>"""
    ]
    for fm in all_pages:
        slug = fm.get('slug', '')
        pillar = fm.get('pillar', '')
        changefreq = 'monthly' if pillar == 'comparison-pages' else 'weekly'
        lastmod = str(fm.get('date_modified', today_str))
        urls.append(
            f"""  <url>
    <loc>{BASE_URL}/{slug}/</loc>
    <changefreq>{changefreq}</changefreq>
    <priority>0.8</priority>
    <lastmod>{lastmod}</lastmod>
  </url>"""
        )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + '\n'.join(urls)
        + '\n</urlset>\n'
    )


def generate_robots():
    return f"""User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Googlebot
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""


def generate_llms_txt(pages_by_pillar, full=False):
    lines = [
        '# howtoclaudeatoz.com',
        '',
        '> The definitive A-to-Z encyclopaedia for Claude AI. Covers every use case, '
        'feature, integration, workflow, prompt technique, and tool pairing. '
        'Written for beginners through power users.',
        '',
    ]
    for pillar_slug, pillar_name in PILLAR_NAMES.items():
        pages = pages_by_pillar.get(pillar_slug, [])
        if not pages:
            continue
        lines.append(f'## {pillar_name}')
        for fm in sorted(pages, key=lambda x: x.get('title', '')):
            slug = fm.get('slug', '')
            title = fm.get('title', slug)
            meta_desc = fm.get('meta_description', '')
            first_sentence = first_n_sentences(meta_desc, 1)
            entry = f'- [{title}]({BASE_URL}/{slug}/) — {first_sentence}'
            if full:
                summary = fm.get('summary', '') or first_n_sentences(meta_desc, 2)
                if summary and summary != first_sentence:
                    entry += f' {summary}'
            lines.append(entry)
        lines.append('')
    return '\n'.join(lines)


def generate_webmanifest():
    manifest = {
        "name": "HowToClaudeAtoZ",
        "short_name": "HowToClaudeAtoZ",
        "description": "The definitive A-to-Z encyclopaedia for Claude AI",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#d97706",
        "icons": [
            {"src": "/logo.svg", "sizes": "any", "type": "image/svg+xml"}
        ]
    }
    return json.dumps(manifest, indent=2) + '\n'


# ---------------------------------------------------------------------------
# GitHub data fetchers
# ---------------------------------------------------------------------------
def fetch_discussions_cache(base_dir, site_dir):
    """
    Fetch top discussions from the Prompt Library and Share Your Workflow
    categories via the GitHub GraphQL API (using the `gh` CLI).
    Saves _site/data/discussions.json.
    Falls back to empty lists if `gh` is unavailable (e.g. on Netlify).
    """
    query = """
query {
  repository(owner: "pindi109", name: "howtoclaudeatoz") {
    prompts: discussions(first: 20, categoryId: "DIC_kwDOSzXQbs4C-toW", orderBy: {field: CREATED_AT, direction: DESC}) {
      nodes { number title body url upvoteCount author { login } createdAt }
    }
    workflows: discussions(first: 20, categoryId: "DIC_kwDOSzXQbs4C-toX", orderBy: {field: CREATED_AT, direction: DESC}) {
      nodes { number title body url upvoteCount author { login } createdAt }
    }
  }
}
""".strip()

    def parse_nodes(nodes):
        result = []
        for node in nodes:
            body = node.get('body') or ''
            result.append({
                'number':       node.get('number', 0),
                'title':        node.get('title', ''),
                'body_excerpt': body[:200],
                'url':          node.get('url', ''),
                'upvotes':      node.get('upvoteCount', 0),
                'author':       (node.get('author') or {}).get('login', ''),
                'createdAt':    node.get('createdAt', ''),
            })
        return sorted(result, key=lambda x: x['upvotes'], reverse=True)

    data = {'prompt_library': [], 'workflows': []}
    try:
        result = subprocess.run(
            ['gh', 'api', 'graphql', '-f', f'query={query}'],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip())
        payload = json.loads(result.stdout)
        repo = payload.get('data', {}).get('repository', {})
        data['prompt_library'] = parse_nodes(
            repo.get('prompts', {}).get('nodes', [])
        )
        data['workflows'] = parse_nodes(
            repo.get('workflows', {}).get('nodes', [])
        )
    except Exception as exc:
        print(f'WARNING: fetch_discussions_cache failed — {exc}')

    data_dir = site_dir / 'data'
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / 'discussions.json').write_text(
        json.dumps(data, indent=2), encoding='utf-8'
    )
    print('Fetched: discussions.json')


def fetch_roadmap_cache(base_dir, site_dir):
    """
    Fetch all open issues labelled `roadmap` from the GitHub REST API.
    Saves _site/data/roadmap.json, grouped by status label.
    Falls back to empty lists if the fetch fails.
    """
    url = (
        'https://api.github.com/repos/pindi109/howtoclaudeatoz/issues'
        '?labels=roadmap&state=open&per_page=50'
    )

    data = {'planned': [], 'in_progress': [], 'published': []}
    try:
        # Get auth token from gh CLI
        token_result = subprocess.run(
            ['gh', 'auth', 'token'],
            capture_output=True, text=True, timeout=10
        )
        token = token_result.stdout.strip() if token_result.returncode == 0 else ''

        req = urllib.request.Request(url)
        req.add_header('Accept', 'application/vnd.github+json')
        req.add_header('X-GitHub-Api-Version', '2022-11-28')
        if token:
            req.add_header('Authorization', f'Bearer {token}')

        with urllib.request.urlopen(req, timeout=15) as resp:
            issues = json.loads(resp.read().decode('utf-8'))

        for issue in issues:
            label_names = [lbl.get('name', '') for lbl in issue.get('labels', [])]
            reactions = issue.get('reactions', {}) or {}
            entry = {
                'number':    issue.get('number', 0),
                'title':     issue.get('title', ''),
                'url':       issue.get('html_url', ''),
                'reactions': {
                    'total_count': reactions.get('total_count', 0),
                    '+1':          reactions.get('+1', 0),
                },
                'labels':    label_names,
            }
            if 'status:in-progress' in label_names:
                data['in_progress'].append(entry)
            elif 'status:published' in label_names:
                data['published'].append(entry)
            else:
                data['planned'].append(entry)

    except Exception as exc:
        print(f'WARNING: fetch_roadmap_cache failed — {exc}')

    data_dir = site_dir / 'data'
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / 'roadmap.json').write_text(
        json.dumps(data, indent=2), encoding='utf-8'
    )
    print('Fetched: roadmap.json')


# ---------------------------------------------------------------------------
# Main build
# ---------------------------------------------------------------------------
def main():
    base_dir = Path(__file__).parent.resolve()
    content_dir = base_dir / 'content'
    templates_dir = base_dir / 'templates'
    affiliate_path = base_dir / 'affiliate' / 'links.json'
    site_dir = base_dir / '_site'

    site_dir.mkdir(exist_ok=True)

    # Load affiliate data
    affiliate_data = {}
    if affiliate_path.exists():
        with open(affiliate_path, 'r', encoding='utf-8') as f:
            affiliate_data = json.load(f)

    # Load page template
    page_template_path = templates_dir / 'page.html'
    page_template = ''
    if page_template_path.exists():
        with open(page_template_path, 'r', encoding='utf-8') as f:
            page_template = f.read()
    else:
        print(f'WARNING: {page_template_path} not found — page HTML will not be rendered')

    # Load index template
    index_template_path = templates_dir / 'index.html'
    index_template = ''
    if index_template_path.exists():
        with open(index_template_path, 'r', encoding='utf-8') as f:
            index_template = f.read()
    else:
        print(f'WARNING: {index_template_path} not found — homepage will not be rendered')

    # Discover and parse all .md files
    md_files = list(content_dir.rglob('*.md')) if content_dir.exists() else []

    all_pages = []   # list of fm dicts for valid pages
    page_data = []   # list of (fm, body_html) for rendering

    for md_path in sorted(md_files):
        raw = md_path.read_text(encoding='utf-8')
        fm, body = parse_frontmatter(raw)

        # Validate required fields
        if not fm.get('title'):
            print(f'WARNING: missing "title" in {md_path} — skipping')
            continue
        if not fm.get('slug'):
            print(f'WARNING: missing "slug" in {md_path} — skipping')
            continue

        body_html = markdown_to_html(body)
        all_pages.append(fm)
        page_data.append((fm, body_html))

    # Group by pillar
    pages_by_pillar = {}
    for fm in all_pages:
        pillar = fm.get('pillar', 'uncategorised')
        pages_by_pillar.setdefault(pillar, []).append(fm)

    today_str = date.today().isoformat()

    # Build each content page
    built_count = 0
    for fm, body_html in page_data:
        slug = fm['slug']
        print(f'Building: {slug}')

        pillar = fm.get('pillar', '')
        faq_list = fm.get('faq', [])
        if not isinstance(faq_list, list):
            faq_list = []

        # Schema strings
        article_schema = build_article_schema(fm, slug)
        faq_schema = build_faq_schema(faq_list)
        breadcrumb_schema = build_breadcrumb_schema(fm, slug)
        howto_schema = build_howto_schema(fm, slug)

        # Wrap schemas in <script> tags
        def schema_tag(s):
            return f'<script type="application/ld+json">\n{s}\n</script>' if s else ''

        variables = {
            'title':               fm.get('title', ''),
            'slug':                slug,
            'meta_description':    fm.get('meta_description', ''),
            'canonical_url':       f'{BASE_URL}/{slug}/',
            'og_image':            f'{BASE_URL}/og/{slug}.png',
            'date_published':      str(fm.get('date_published', '')),
            'date_modified':       str(fm.get('date_modified', '')),
            'pillar_name':         pillar_display_name(pillar),
            'pillar_slug':         pillar,
            'content':             body_html,
            'article_schema':      schema_tag(article_schema),
            'faq_schema':          schema_tag(faq_schema),
            'breadcrumb_schema':   schema_tag(breadcrumb_schema),
            'howto_schema':        schema_tag(howto_schema),
            'faq_html':            build_faq_html(faq_list),
            'affiliate_disclosure': build_affiliate_disclosure(fm),
            'internal_links_html': '',
            'author_byline':       build_author_byline(fm),
            'breadcrumbs_html':    build_breadcrumbs_html(fm, slug),
            'page_nav_links':      build_page_nav_links(pages_by_pillar),
        }

        if page_template:
            rendered = render_template(page_template, variables)
        else:
            # Minimal fallback
            rendered = (
                f'<!DOCTYPE html><html><head><title>{fm["title"]}</title></head>'
                f'<body>{body_html}</body></html>'
            )

        out_dir = site_dir / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / 'index.html').write_text(rendered, encoding='utf-8')
        built_count += 1

    # Build homepage
    if index_template:
        pillar_links_html = build_pillar_links(pages_by_pillar)
        homepage_vars = {
            'pillar_links':    pillar_links_html,
            'page_nav_links':  pillar_links_html,
        }
        rendered_home = render_template(index_template, homepage_vars)
        (site_dir / 'index.html').write_text(rendered_home, encoding='utf-8')
        print('Building: homepage')

    # Generate sitemap.xml
    sitemap_xml = generate_sitemap(all_pages, today_str)
    (site_dir / 'sitemap.xml').write_text(sitemap_xml, encoding='utf-8')
    print('Generated: sitemap.xml')

    # Generate robots.txt
    (site_dir / 'robots.txt').write_text(generate_robots(), encoding='utf-8')
    print('Generated: robots.txt')

    # Generate llms.txt
    llms = generate_llms_txt(pages_by_pillar, full=False)
    (site_dir / 'llms.txt').write_text(llms, encoding='utf-8')
    print('Generated: llms.txt')

    # Generate llms-full.txt
    llms_full = generate_llms_txt(pages_by_pillar, full=True)
    (site_dir / 'llms-full.txt').write_text(llms_full, encoding='utf-8')
    print('Generated: llms-full.txt')

    # Generate site.webmanifest
    (site_dir / 'site.webmanifest').write_text(generate_webmanifest(), encoding='utf-8')
    print('Generated: site.webmanifest')

    # Copy static asset directories (icons/, assets/) into _site/
    # Wipe destination first so removed source files don't linger
    for asset_dir in ['icons', 'assets']:
        src_asset = base_dir / asset_dir
        dst_asset = site_dir / asset_dir
        if src_asset.exists():
            if dst_asset.exists():
                shutil.rmtree(dst_asset)
            dst_asset.mkdir(parents=True)
            for f in src_asset.rglob('*'):
                if f.is_file():
                    rel = f.relative_to(src_asset)
                    dest = dst_asset / rel
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(f, dest)
            print(f'Copied: {asset_dir}/')

    # Copy root-level static files into _site/
    for static_file in ['logo.svg', 'logo.png', 'src/tokens.css']:
        src_f = base_dir / static_file
        if src_f.exists():
            dest_name = Path(static_file).name
            shutil.copy2(src_f, site_dir / dest_name)
    print('Copied: logo.svg, logo.png, tokens.css')

    # Build Tailwind CSS from the generated HTML
    import subprocess
    tw_result = subprocess.run(
        ['npx', 'tailwindcss',
         '-i', 'src/input.css',
         '-o', '_site/tailwind.css',
         '--minify'],
        cwd=str(base_dir),
        capture_output=True, text=True
    )
    if tw_result.returncode == 0:
        print('Built: tailwind.css')
    else:
        print(f'WARNING: tailwindcss skipped — {tw_result.stderr[:120].strip()}')

    # Fetch GitHub data caches
    fetch_discussions_cache(base_dir, site_dir)
    fetch_roadmap_cache(base_dir, site_dir)

    print(f'\nBuilt {built_count} pages → _site/')


if __name__ == '__main__':
    main()
