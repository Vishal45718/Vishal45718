#!/usr/bin/env python3
"""Generate a compact SVG dashboard from public GitHub profile/repository data.

The script uses only the Python standard library so it runs in GitHub Actions
without installing dependencies. Set GITHUB_TOKEN to raise the API rate limit.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from html import escape
from pathlib import Path

USERNAME = "Vishal45718"
API_ROOT = "https://api.github.com"
OUTPUT = Path("assets/profile-dashboard.svg")


def github_get(url: str):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "Vishal45718-profile-dashboard",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")[:500]
        raise RuntimeError(f"GitHub API returned HTTP {exc.code}: {details}") from exc


def collect_stats() -> dict[str, int]:
    profile = github_get(f"{API_ROOT}/users/{USERNAME}")
    repos = []
    page = 1
    while True:
        query = urllib.parse.urlencode({
            "type": "owner",
            "sort": "pushed",
            "per_page": 100,
            "page": page,
        })
        batch = github_get(f"{API_ROOT}/users/{USERNAME}/repos?{query}")
        if not batch:
            break
        # Only public repositories are returned by this public endpoint.
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    return {
        "repos": int(profile.get("public_repos", len(repos))),
        "stars": sum(int(repo.get("stargazers_count", 0)) for repo in repos),
        "forks": sum(int(repo.get("forks_count", 0)) for repo in repos),
        "followers": int(profile.get("followers", 0)),
    }


def build_svg(stats: dict[str, int]) -> str:
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d  %H:%M UTC")
    tiles = [
        ("PUBLIC REPOSITORIES", stats["repos"], "Owned public repositories"),
        ("STARS", stats["stars"], "Across owned public repositories"),
        ("FORKS", stats["forks"], "Across owned public repositories"),
        ("FOLLOWERS", stats["followers"], "GitHub profile followers"),
    ]
    x_positions = [32, 270, 508, 746]
    cards = []
    for x, (label, value, hint) in zip(x_positions, tiles):
        cards.append(f"""
  <g>
    <rect x="{x}" y="104" width="222" height="78" rx="10"
          fill="#101b2d" stroke="#26364d"/>
    <rect x="{x}" y="104" width="3" height="78" rx="1.5" fill="#67e8a5"/>
    <text x="{x + 17}" y="128" class="label">{escape(label)}</text>
    <text x="{x + 17}" y="157" class="value">{value:,}</text>
    <text x="{x + 17}" y="173" class="hint">{escape(hint)}</text>
  </g>""")

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="224" viewBox="0 0 1000 224" role="img" aria-labelledby="title desc">
  <title id="title">Vishal Varukolu — GitHub profile dashboard</title>
  <desc id="desc">Public GitHub repositories, stars, forks, and followers. Refreshed automatically.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#080d18"/>
      <stop offset="100%" stop-color="#111b2b"/>
    </linearGradient>
    <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#7c91ad" stroke-opacity=".08" stroke-width="1"/>
    </pattern>
    <style>
      text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
      .eyebrow {{ fill: #67e8a5; font-size: 10px; font-weight: 700; letter-spacing: 2px; }}
      .headline {{ fill: #edf4ff; font-size: 21px; font-weight: 700; letter-spacing: .3px; }}
      .subhead {{ fill: #9baec6; font-size: 11px; }}
      .label {{ fill: #9baec6; font-size: 9px; font-weight: 700; letter-spacing: .7px; }}
      .value {{ fill: #f3f7ff; font-size: 23px; font-weight: 700; }}
      .hint {{ fill: #71859e; font-size: 8px; }}
      .footer {{ fill: #71859e; font-size: 9px; }}
    </style>
  </defs>
  <rect width="1000" height="224" rx="16" fill="url(#bg)"/>
  <rect width="1000" height="224" rx="16" fill="url(#grid)"/>
  <rect x="1" y="1" width="998" height="222" rx="15" fill="none" stroke="#26364d"/>
  <circle cx="970" cy="22" r="3" fill="#67e8a5"/>
  <text x="32" y="29" class="eyebrow">VISHAL45718 / PROFILE.SNAPSHOT</text>
  <text x="32" y="59" class="headline">Systems-minded. Measurement-driven.</text>
  <text x="32" y="79" class="subhead">IIT Hyderabad · CSE '27 · Systems / Backend / Compilers / Applied ML</text>
  <rect x="829" y="38" width="139" height="24" rx="12" fill="#12352c" stroke="#235c49"/>
  <text x="898.5" y="53.5" text-anchor="middle" class="eyebrow" style="font-size:9px;letter-spacing:1px">● LIVE PROFILE DATA</text>
  {''.join(cards)}
  <text x="32" y="207" class="footer">SOURCE: GITHUB PUBLIC API</text>
  <text x="968" y="207" text-anchor="end" class="footer">UPDATED {escape(updated)}</text>
</svg>
'''


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    stats = collect_stats()
    svg = build_svg(stats)
    OUTPUT.write_text(svg, encoding="utf-8")
    print(f"Updated {OUTPUT} with public GitHub profile stats: {stats}")


if __name__ == "__main__":
    main()
