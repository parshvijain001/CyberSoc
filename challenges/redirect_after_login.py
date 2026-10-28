"""Bonus challenge B: the "continue" redirect.

Several links send you through /go?next=... so the app can bounce you onward
(e.g. back to the page you came from). The handler redirects to whatever `next`
says, including a full URL on another site. An attacker can send someone a
link to OUR site that quietly forwards them to a lookalike phishing page -- this
is an open redirect.

YOUR JOB: `safe_target` should allow only redirects that stay on THIS site
(a path like /notes). Anything pointing at another host should fall back to "/".

WATCH OUT: it's not just "starts with http". A leading "//" or "https:\\" is
also treated as another site by browsers. Allow only values that are a single
local path.

HINT: urllib.parse.urlparse(next).netloc must be empty AND the value must start
with a single "/" (reject "//..."). Then it's same-site.
"""
from flask import redirect
from urllib.parse import urlparse

def safe_target(next_value):
    if not next_value:
            return "/"
        
    parsed = urlparse(next_value)
        
        # 1. netloc must be empty (ensures no external domain like http://evil.example)
        # 2. Must start with a single "/" AND not start with "//" (protocol-relative check)
    if parsed.netloc or not next_value.startswith("/") or next_value.startswith("//"):
            return "/"
            
    return next_value


def handle(request):
    return redirect(safe_target(request.args.get("next", "")))
