#!/usr/bin/env python3
"""
serve.py — local preview server for howtoclaudeatoz.com
Usage: python serve.py
Then open http://localhost:8000 in your browser.
"""
import http.server
import socketserver
import os
from pathlib import Path

PORT = 8000
SITE_DIR = Path(__file__).parent / '_site'

if not SITE_DIR.exists():
    print(f'ERROR: _site/ not found. Run "python generate.py" first.')
    raise SystemExit(1)


class SiteHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SITE_DIR), **kwargs)

    def translate_path(self, path):
        # Strip query string
        path = path.split('?')[0].split('#')[0]
        full = SITE_DIR / path.lstrip('/')
        # If directory, serve index.html
        if full.is_dir():
            full = full / 'index.html'
        # If not found, serve 404
        if not full.exists():
            full = SITE_DIR / '404.html'
        return str(full)

    def log_message(self, fmt, *args):
        print(f'  {self.address_string()} — {fmt % args}')


print(f'')
print(f'  HowToClaudeAtoZ — Local Preview')
print(f'  ================================')
print(f'  Open: http://localhost:{PORT}')
print(f'  Ctrl+C to stop')
print(f'')

with socketserver.TCPServer(('', PORT), SiteHandler) as httpd:
    httpd.allow_reuse_address = True
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n  Server stopped.')
