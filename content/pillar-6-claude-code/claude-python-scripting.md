---
title: "Claude for Python Scripting — Developer Guide (2026)"
slug: claude-python-scripting
pillar: claude-code
meta_description: "Use Claude for Python scripting to automate tasks, process data, call APIs, and build tools faster. Full guide with 3 complete, runnable Python scripts for 2026."
primary_keyword: "Claude Python scripting"
secondary_keywords:
  - "Claude write Python script"
  - "Claude Python automation"
  - "AI Python code generation"
affiliates:
  - make-com
date_published: "2026-06-07"
date_modified: "2026-06-07"
faq:
  - q: "Can Claude write Python scripts?"
    a: "Yes — Claude writes complete, runnable Python scripts including data processing pipelines, API clients, file automation, web scrapers, CLI tools, and more. It handles standard library modules, popular third-party packages (requests, pandas, SQLAlchemy, FastAPI, etc.), and Python 3.10+ features like structural pattern matching and improved type hints. You can ask for a complete script with error handling, logging, and CLI arguments in a single prompt."
  - q: "How good is Claude at Python?"
    a: "Claude is among the strongest AI models for Python. It writes idiomatic, Pythonic code — using list comprehensions where appropriate, context managers for resources, dataclasses, proper exception hierarchies, and type hints. It also knows when not to be clever. For production scripts, Claude consistently adds error handling, logging, and argument parsing without being asked."
  - q: "What Python libraries does Claude know?"
    a: "Claude has deep knowledge of the Python standard library plus the most widely used third-party packages: requests and httpx (HTTP), pandas and polars (data), SQLAlchemy (databases), FastAPI and Flask (web), pytest (testing), pydantic (validation), boto3 (AWS), Pillow (images), BeautifulSoup and Playwright (scraping/automation), and many more. It also knows the Anthropic Python SDK for building Claude-powered tools."
summary: "Claude writes production-quality Python scripts from plain-English prompts, handling data processing, API integration, and automation tasks with proper error handling and type hints. This guide shows you exactly how to get the best Python output from Claude — with three complete, runnable scripts as examples."
hero_image: "/assets/images/heroes/photo-022-122100403557357116.jpg"
hero_alt: "Give Claude a plain-English description of a Python task and it returns a complete, runnable script — error handling, type hints, logging, and argument parsing included."
---

# Claude for Python Scripting — Developer Guide (2026)

*Last updated: 2026-06-07*

Claude Python scripting is one of the most practical use cases for AI-assisted development. Python's combination of readable syntax, vast ecosystem, and heavy use in automation makes it ideal for AI generation — and Claude is exceptionally good at it. Give Claude a plain-English description of what you need, and it returns a complete, runnable script with error handling, type hints, logging, and argument parsing — the parts that are correct but tedious to write by hand. This guide covers how to get the best Python output from Claude, with three complete scripts you can run today, and how to chain Python scripts with tools like Make.com for full automation pipelines.

## How Claude Helps with Python Scripting

Claude does not just autocomplete Python — it understands intent. When you say "write a script to process customer CSV exports and load them to Postgres, skipping duplicates", Claude figures out:

- Which libraries to use (pandas + SQLAlchemy, or psycopg2 directly)
- How to handle CSV encoding edge cases
- What the upsert SQL should look like
- How to add `--dry-run` mode and `--verbose` flags
- How to log progress and failures

The result is a script you would write yourself, but in minutes instead of an hour. Here is how to get consistently good output.

## How to Get Great Python Scripts from Claude — Step by Step

### Step 1: Be Specific About Inputs and Outputs

The most common mistake is an under-specified prompt. Instead of:

```
Write a script to process CSV files
```

Say:

```
Write a Python script that:
- Reads all .csv files from an input/ directory
- Each CSV has columns: customer_id, email, amount, date (YYYY-MM-DD)
- Validates that amount is a positive number and email is valid format
- Writes valid rows to output/clean.csv and invalid rows to output/errors.csv with an added 'error_reason' column
- Logs progress to stdout and a logfile
- Accepts --input-dir and --output-dir as CLI arguments
```

### Step 2: Specify Your Python Version and Key Libraries

Claude defaults to Python 3.10+ idioms, but if you need compatibility with an older version or have specific library preferences, say so:

```
Use Python 3.11. Use httpx instead of requests for async support. 
Use pydantic v2 for validation.
```

### Step 3: Ask for Error Handling and Logging Explicitly (or Tell Claude to Add It)

Claude adds error handling when you ask for "production-ready" or "robust" scripts. A quick addition to your prompt:

```
Add proper error handling, retry logic for network calls, 
and structured logging using the standard logging module.
```

### Step 4: Iterate with Claude Code for File-Based Projects

For multi-file Python projects, Claude Code (the CLI) is more powerful than the browser interface. It reads your existing code, maintains consistency with your patterns, and can run the script to verify it works:

```bash
cd ~/projects/data-pipeline
claude
> Refactor the csv_processor.py script to use a class-based 
  approach so we can subclass it for JSON and XML inputs too.
  Run the tests after refactoring.
```

## Complete Python Script Examples from Claude

### Script 1: REST API Polling and Alert Tool

```python
#!/usr/bin/env python3
"""
Poll a REST API endpoint at regular intervals and send an alert
when a condition is met. Uses httpx for async HTTP and sends
alerts via a webhook URL (compatible with Slack, Discord, Make.com).

Usage:
    python api_monitor.py --url https://api.example.com/status \
                          --webhook https://hooks.slack.com/... \
                          --interval 60
"""

import argparse
import asyncio
import logging
import sys
from datetime import datetime

import httpx

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("monitor.log"),
    ],
)
log = logging.getLogger(__name__)


async def check_endpoint(client: httpx.AsyncClient, url: str) -> dict:
    """Fetch the endpoint and return parsed JSON."""
    response = await client.get(url, timeout=10.0)
    response.raise_for_status()
    return response.json()


def is_alert_condition(data: dict) -> tuple[bool, str]:
    """Return (should_alert, reason). Customise this logic."""
    status = data.get("status", "")
    if status not in ("ok", "healthy"):
        return True, f"Status is '{status}'"
    error_rate = data.get("error_rate_pct", 0)
    if error_rate > 5:
        return True, f"Error rate {error_rate:.1f}% exceeds 5%"
    return False, ""


async def send_alert(client: httpx.AsyncClient, webhook_url: str, reason: str) -> None:
    """POST an alert message to the webhook URL."""
    payload = {
        "text": f":warning: API Monitor Alert — {reason} at {datetime.utcnow().isoformat()}Z"
    }
    try:
        resp = await client.post(webhook_url, json=payload, timeout=10.0)
        resp.raise_for_status()
        log.info("Alert sent: %s", reason)
    except httpx.HTTPError as e:
        log.error("Failed to send alert: %s", e)


async def run_monitor(url: str, webhook_url: str, interval: int) -> None:
    """Main monitoring loop."""
    log.info("Starting monitor for %s, polling every %ds", url, interval)
    last_alerted = False

    async with httpx.AsyncClient() as client:
        while True:
            try:
                data = await check_endpoint(client, url)
                should_alert, reason = is_alert_condition(data)

                if should_alert and not last_alerted:
                    await send_alert(client, webhook_url, reason)
                    last_alerted = True
                elif not should_alert and last_alerted:
                    log.info("Condition resolved — no longer alerting")
                    last_alerted = False
                else:
                    log.debug("Status OK")

            except httpx.HTTPError as e:
                log.error("Request failed: %s", e)
                if not last_alerted:
                    await send_alert(client, webhook_url, f"Request failed: {e}")
                    last_alerted = True

            await asyncio.sleep(interval)


def main() -> None:
    parser = argparse.ArgumentParser(description="API endpoint monitor")
    parser.add_argument("--url", required=True, help="Endpoint URL to monitor")
    parser.add_argument("--webhook", required=True, help="Webhook URL for alerts")
    parser.add_argument("--interval", type=int, default=60, help="Poll interval in seconds")
    args = parser.parse_args()

    try:
        asyncio.run(run_monitor(args.url, args.webhook, args.interval))
    except KeyboardInterrupt:
        log.info("Monitor stopped")


if __name__ == "__main__":
    main()
```

### Script 2: CSV-to-PostgreSQL ETL Pipeline

```python
#!/usr/bin/env python3
"""
Read CSV files from an input directory, validate rows, and upsert
valid rows into a PostgreSQL table. Invalid rows are written to an
error CSV with a reason column.

Usage:
    python csv_to_pg.py --input-dir ./data --db-url postgresql://user:pass@localhost/mydb
"""

import argparse
import csv
import logging
import re
import sys
from pathlib import Path

import psycopg2
from psycopg2.extras import execute_values

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)

EMAIL_RE = re.compile(r"^[^@]+@[^@]+\.[^@]+$")

UPSERT_SQL = """
    INSERT INTO customers (customer_id, email, amount, sale_date)
    VALUES %s
    ON CONFLICT (customer_id)
    DO UPDATE SET
        email = EXCLUDED.email,
        amount = EXCLUDED.amount,
        sale_date = EXCLUDED.sale_date
"""


def validate_row(row: dict) -> tuple[bool, str]:
    if not row.get("customer_id", "").strip():
        return False, "Missing customer_id"
    if not EMAIL_RE.match(row.get("email", "")):
        return False, f"Invalid email: {row.get('email')}"
    try:
        amount = float(row["amount"])
        if amount <= 0:
            raise ValueError
    except (KeyError, ValueError):
        return False, f"Invalid amount: {row.get('amount')}"
    return True, ""


def process_file(filepath: Path, conn) -> tuple[int, int]:
    """Returns (inserted, rejected) counts."""
    valid_rows = []
    error_rows = []

    with filepath.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ok, reason = validate_row(row)
            if ok:
                valid_rows.append(
                    (row["customer_id"].strip(), row["email"].strip(),
                     float(row["amount"]), row["date"].strip())
                )
            else:
                error_rows.append({**row, "error_reason": reason})

    if valid_rows:
        with conn.cursor() as cur:
            execute_values(cur, UPSERT_SQL, valid_rows)
        conn.commit()

    if error_rows:
        error_path = filepath.parent / "errors" / filepath.name
        error_path.parent.mkdir(exist_ok=True)
        with error_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(error_rows[0].keys()))
            writer.writeheader()
            writer.writerows(error_rows)

    log.info("%s: %d inserted, %d rejected", filepath.name, len(valid_rows), len(error_rows))
    return len(valid_rows), len(error_rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="CSV to PostgreSQL ETL")
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument("--db-url", required=True)
    args = parser.parse_args()

    csv_files = list(args.input_dir.glob("*.csv"))
    if not csv_files:
        log.warning("No CSV files found in %s", args.input_dir)
        sys.exit(0)

    conn = psycopg2.connect(args.db_url)
    total_inserted = total_rejected = 0

    try:
        for filepath in csv_files:
            inserted, rejected = process_file(filepath, conn)
            total_inserted += inserted
            total_rejected += rejected
    finally:
        conn.close()

    log.info("Done. Total inserted: %d, rejected: %d", total_inserted, total_rejected)


if __name__ == "__main__":
    main()
```

### Script 3: Batch File Renamer with Preview Mode

```python
#!/usr/bin/env python3
"""
Rename files in a directory according to a pattern. Supports
preview (dry-run) mode, undo via a log file, and regex transformations.

Usage:
    # Preview
    python renamer.py --dir ./photos --pattern "{date}_{name}" --dry-run
    # Apply
    python renamer.py --dir ./photos --pattern "{date}_{name}"
    # Undo last run
    python renamer.py --undo
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

UNDO_LOG = Path(".renamer_undo.json")


def build_new_name(filepath: Path, pattern: str) -> str:
    """Substitute pattern variables with file metadata."""
    mtime = datetime.fromtimestamp(filepath.stat().st_mtime)
    replacements = {
        "{name}": filepath.stem,
        "{ext}": filepath.suffix.lstrip("."),
        "{date}": mtime.strftime("%Y-%m-%d"),
        "{datetime}": mtime.strftime("%Y%m%d_%H%M%S"),
    }
    result = pattern
    for key, value in replacements.items():
        result = result.replace(key, value)
    # Append original extension if pattern doesn't include {ext}
    if "{ext}" not in pattern and filepath.suffix:
        result += filepath.suffix
    return result


def rename_files(directory: Path, pattern: str, dry_run: bool) -> None:
    files = [f for f in directory.iterdir() if f.is_file() and not f.name.startswith(".")]
    if not files:
        print("No files found.")
        return

    undo_map = {}
    conflicts = set()

    renames = [(f, f.parent / build_new_name(f, pattern)) for f in files]

    # Check for conflicts
    new_names = [new for _, new in renames]
    seen = set()
    for new in new_names:
        if new in seen:
            conflicts.add(new)
        seen.add(new)

    for original, new_path in renames:
        if original == new_path:
            continue
        if new_path in conflicts:
            print(f"  SKIP (conflict): {original.name} -> {new_path.name}")
            continue
        print(f"  {'[DRY RUN] ' if dry_run else ''}Rename: {original.name} -> {new_path.name}")
        if not dry_run:
            original.rename(new_path)
            undo_map[str(new_path)] = str(original)

    if not dry_run and undo_map:
        UNDO_LOG.write_text(json.dumps(undo_map, indent=2))
        print(f"\nUndo log saved to {UNDO_LOG}")


def undo_renames() -> None:
    if not UNDO_LOG.exists():
        print("No undo log found.")
        sys.exit(1)
    undo_map = json.loads(UNDO_LOG.read_text())
    for current, original in undo_map.items():
        current_path, original_path = Path(current), Path(original)
        if current_path.exists():
            current_path.rename(original_path)
            print(f"Restored: {current_path.name} -> {original_path.name}")
        else:
            print(f"File not found, skipping: {current_path.name}")
    UNDO_LOG.unlink()
    print("Undo complete.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Batch file renamer")
    parser.add_argument("--dir", type=Path, help="Directory containing files to rename")
    parser.add_argument("--pattern", help="Name pattern. Variables: {name} {ext} {date} {datetime}")
    parser.add_argument("--dry-run", action="store_true", help="Preview without renaming")
    parser.add_argument("--undo", action="store_true", help="Undo the last rename operation")
    args = parser.parse_args()

    if args.undo:
        undo_renames()
    elif args.dir and args.pattern:
        rename_files(args.dir, args.pattern, args.dry_run)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## Integrating Claude Python Output with Make.com

Claude can write Python scripts that serve as the processing core of a Make.com automation. A common pattern: Make.com handles the trigger and data routing, and a Python script (deployed as an AWS Lambda or on a VPS) handles the heavy lifting.

Example workflow:

1. **Make.com trigger** — new row in Google Sheets
2. **Make.com HTTP module** — POST the row data to your Python webhook endpoint
3. **Python script** — validates, transforms, and loads data to Postgres
4. **Make.com** — receives the response, updates the Sheet status

Ask Claude to generate the Python Flask endpoint that Make.com calls:

```
Write a Flask endpoint at POST /process-lead that receives JSON with 
fields (name, email, company, source). Validate the data with pydantic, 
upsert to the leads table in Postgres, and return {success: true, lead_id: ...} 
or {success: false, error: ...}. The endpoint should use HTTP Basic Auth 
with credentials from environment variables.
```

Claude generates a complete, deployable Flask handler with pydantic validation, database upsert, and authentication — ready to plug into your Make.com scenario.

## Claude Code vs Claude.ai for Python Projects

| Use case | Use Claude Code | Use Claude.ai |
|---|---|---|
| Multi-file Python project | Yes — reads all files | No |
| Single standalone script | Either works | Quick and easy |
| Refactoring existing code | Claude Code | Paste and describe |
| Running and testing output | Claude Code | No |
| Quick data manipulation | Either | Faster for one-offs |
| Package a CLI tool | Claude Code | Possible but awkward |

## Related Claude Guides

- [Claude Code Getting Started](/claude-code-getting-started/)
- [Debug Code with Claude](/debug-code-with-claude/)
- [Claude for API Documentation](/claude-api-documentation/)
- [Building Apps with Claude as Your Co-Developer](/claude-co-developer/)
- [Claude Code vs n8n](/claude-code-vs-n8n/)
