#!/usr/bin/env python3
"""Build Vishal Varukolu's terminal-style GitHub profile dashboard.

Uses only Python's standard library and GitHub's public REST API.
Set GITHUB_TOKEN (as GitHub Actions does) to use the authenticated API limit.
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
        raise RuntimeError(
            f"GitHub API returned HTTP {exc.code}: {details}"
        ) from exc


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
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    tiles = [
        ("PUBLIC REPOSITORIES", stats["repos"], "owned public repositories"),
        ("STARS", stats["stars"], "across owned public repositories"),
        ("FORKS", stats["forks"], "across owned public repositories"),
        ("FOLLOWERS", stats["followers"], "GitHub profile followers"),
    ]
    x_positions = [32, 270, 508, 746]
    cards = []

    for x, (label, value, hint) in zip(x_positions, tiles):
        cards.append(f"""
  <g>
    <rect x="{x}" y="157" width="222" height="78" rx="8"
          fill="#0d1625" stroke="#26364d"/>
    <rect x="{x}" y="157" width="3" height="78" rx="1.5" fill="#67e8a5"/>
    <text x="{x + 17}" y="180" class="label">{escape(label)}</text>
    <text x="{x + 17}" y="210" class="value">{value:,}</text>
    <text x="{x + 17}" y="226" class="hint">{escape(hint)}</text>
  </g>""")

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="280" viewBox="0 0 1000 280" role="img" aria-labelledby="title desc">
  <title id="title">Vishal Varukolu — terminal-style GitHub profile dashboard</title>
  <desc id="desc">A terminal window showing public GitHub repositories, stars, forks, and followers.</desc>
  <defs>
    <linearGradient id="screen" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#070c14"/>
      <stop offset="100%" stop-color="#101b2b"/>
    </linearGradient>
    <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#8195ad" stroke-opacity=".055" stroke-width="1"/>
    </pattern>
    <style>
      text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
      .chrome {{ fill: #8fa2b9; font-size: 10px; }}
      .prompt {{ fill: #67e8a5; font-size: 11px; font-weight: 700; }}
      .headline {{ fill: #edf4ff; font-size: 21px; font-weight: 700; letter-spacing: .2px; }}
      .subhead {{ fill: #9baec6; font-size: 11px; }}
      .label {{ fill: #9baec6; font-size: 9px; font-weight: 700; letter-spacing: .65px; }}
      .value {{ fill: #f3f7ff; font-size: 23px; font-weight: 700; }}
      .hint {{ fill: #71859e; font-size: 8px; }}
      .footer {{ fill: #71859e; font-size: 9px; }}
    </style>
  </defs>

  <rect width="1000" height="280" rx="13" fill="url(#screen)"/>
  <rect width="1000" height="280" rx="13" fill="url(#grid)"/>
  <rect x=".5" y=".5" width="999" height="279" rx="12.5" fill="none" stroke="#2b3b51"/>

  <path d="M13 1 H987 A12 12 0 0 1 999 13 V36 H1 V13 A12 12 0 0 1 13 1 Z" fill="#121d2e"/>
  <path d="M1 36 H999" stroke="#2b3b51"/>
  <circle cx="20" cy="18" r="4" fill="#ff6b6b"/>
  <circle cx="35" cy="18" r="4" fill="#f6c65b"/>
  <circle cx="50" cy="18" r="4" fill="#67e8a5"/>
  <text x="500" y="22" text-anchor="middle" class="chrome">vishal@iith: ~/profile — zsh</text>
  <text x="32" y="58" class="prompt">vishal@iith:~$ ./profile --snapshot</text>
  <text x="32" y="87" class="headline">Vishal Varukolu</text>
  <text x="32" y="107" class="subhead">CSE @ IIT Hyderabad · Class of 2027</text>
  <text x="32" y="126" class="subhead">systems / backend infrastructure / compilers / applied ML</text>
  <rect x="798" y="77" width="170" height="25" rx="5" fill="#102a25" stroke="#235b48"/>
  <circle cx="812" cy="89.5" r="3" fill="#67e8a5"/>
  <text x="823" y="93" class="prompt" style="font-size:9px;letter-spacing:.4px">PUBLIC API SNAPSHOT</text>
  <text x="32" y="145" class="chrome"># profile metrics — not research benchmarks</text>
  {''.join(cards)}
  <text x="32" y="261" class="footer">SOURCE: GITHUB PUBLIC REST API</text>
  <text x="968" y="261" text-anchor="end" class="footer">LAST GENERATED: {escape(updated)}</text>
</svg>
'''


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    stats = collect_stats()
    OUTPUT.write_text(build_svg(stats), encoding="utf-8")
    print(f"Updated {OUTPUT} from GitHub's public API: {stats}")


if __name__ == "__main__":
    main()
