# HowToClaudeAtoZ

The definitive Claude AI encyclopaedia. Operated by Level up IT Solutions Ltd.

---

## Environment Variables

Add the following to your Netlify site settings under **Site settings → Environment variables**:

| Variable | Description |
|---|---|
| `ANTHROPIC_API_KEY` | Your Anthropic API key from [console.anthropic.com](https://console.anthropic.com/settings/keys). Required for the AI chat widget. |

---

## Local Development

```bash
npm install          # install Tailwind CLI
python generate.py   # build _site/
python serve.py      # preview at http://localhost:8000
```

---

## Generating Favicon Files

The site requires two favicon files that are **not committed to the repository** because they must be generated from the logo PNG. Generate them once and place them in the project root — `generate.py` will copy them to `_site/` on every build.

### Source file
`assets/images/logo.png` — the master logo (594 KB PNG)

### Step-by-step using favicon.io (free, no signup)

1. Go to **[favicon.io/favicon-converter](https://favicon.io/favicon-converter/)**
2. Click **Choose File** and upload `assets/images/logo.png`
3. Click **Download** — you'll get a zip containing several files
4. From the zip, copy **only** these two files into the project root `/home/pindi/howtoclaudeatoz/`:
   - `favicon.ico` (32×32, already included in the zip)
   - `apple-touch-icon.png` (180×180, already included in the zip)
5. Run `python generate.py` — it will copy both files to `_site/`

### Alternative: using any image editor
- Resize `assets/images/logo.png` to **32×32 px** → export as `favicon.ico`
- Resize `assets/images/logo.png` to **180×180 px** → export as `apple-touch-icon.png`
- Place both in the project root

### Verification
After generating and running `python generate.py`, confirm:
```
_site/favicon.ico          ← browser tab icon
_site/apple-touch-icon.png ← iOS home screen icon
```

Both are already referenced in all templates:
```html
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
```

---

## Deploy

The site deploys automatically from GitHub via Netlify.

Build command: `npm ci && python generate.py && npx pagefind --site _site`  
Publish directory: `_site`  
Functions directory: `netlify/functions`

---

## Company

Operated by **Level up IT Solutions Ltd**  
Company No. 17255978 — Registered in England & Wales  
8 Shaw Park Business Village, Shaw Rd, Wolverhampton, WV10 9LE  
pindi@howtoclaudeatoz.com · 07399 651836
