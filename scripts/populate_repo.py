#!/usr/bin/env python3
"""Populate tailored-skills repo from ui-skills.com registry and vera subset."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path("/home/cfollette18/tailored-skills")
VERA = Path("/home/cfollette18/vera/skills")
REGISTRY_URL = "https://www.ui-skills.com/skills/registry.json"
REGISTRY_CACHE = Path("/tmp/ui-skills-registry.json")

# Personal / machine-specific path scrubbing
SCRUB_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"/home/cfollette18/[^\s\"']+"), "$PROJECT_ROOT"),
    (re.compile(r"\bvera/"), "$PROJECT_ROOT/"),
]

VERA_COPIES: list[tuple[str, str]] = [
    # (vera relative path, destination category dir)
    ("research", "02-ml-ai-research"),
    ("data-science", "02-ml-ai-research"),
    ("planning/custom-model-plan", "02-ml-ai-research"),
    ("mlops/research/dspy", "02-ml-ai-research/mlops-research"),
    ("autonomous-ai-agents", "03-agent-harness"),
    ("mcp", "03-agent-harness"),
    ("reproducible-training-studio", "03-agent-harness"),
    ("mlops/training-studio-recipes", "03-agent-harness"),
    ("mlops/training-studio-trainer", "03-agent-harness"),
    ("mlops/training-studio-api", "03-agent-harness"),
    ("mlops/training-studio-workflow", "03-agent-harness"),
    ("mlops", "05-mlops"),
    ("mlops-inference", "05-mlops"),
    ("security", "06-security-eval"),
    ("red-teaming", "06-security-eval"),
    ("software-development/plan", "07-software-development"),
    ("software-development/spike", "07-software-development"),
    ("software-development/systematic-debugging", "07-software-development"),
    ("software-development/test-driven-development", "07-software-development"),
    ("software-development/writing-plans", "07-software-development"),
    ("software-development/requesting-code-review", "07-software-development"),
    ("software-development/simplify-code", "07-software-development"),
    ("software-development/subagent-driven-development", "07-software-development"),
    ("software-development/python-debugpy", "07-software-development"),
    ("software-development/node-inspect-debugger", "07-software-development"),
    ("software-development/dogfood", "07-software-development"),
    ("software-development/hermes-agent-skill-authoring", "07-software-development"),
    ("github", "08-github"),
    ("diagramming", "09-diagramming"),
    ("creative/excalidraw", "09-diagramming"),
    ("creative/architecture-diagram", "09-diagramming"),
    ("architectural-planning", "10-architectural-planning"),
]


def fetch_registry() -> list[dict]:
    if REGISTRY_CACHE.exists():
        data = json.loads(REGISTRY_CACHE.read_text())
    else:
        with urllib.request.urlopen(REGISTRY_URL, timeout=60) as resp:
            data = json.load(resp)
        REGISTRY_CACHE.write_text(json.dumps(data, indent=2))
    return data["registry"]


def download_text(url: str) -> str | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "tailored-skills-setup/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        print(f"  FAIL {url}: {exc}", file=sys.stderr)
        return None


def ensure_frontmatter(content: str, name: str, description: str) -> str:
    if content.lstrip().startswith("---"):
        return content
    desc = description.replace('"', '\\"')
    header = f"---\nname: {name}\ndescription: {description}\n---\n\n"
    return header + content


def scrub_content(text: str) -> str:
    for pattern, repl in SCRUB_PATTERNS:
        text = pattern.sub(repl, text)
    return text


def write_ui_skills(registry: list[dict]) -> tuple[int, list[str]]:
    base = REPO / "01-ui-design"
    base.mkdir(parents=True, exist_ok=True)
    fetched = 0
    failed: list[str] = []
    seen_urls: dict[str, Path] = {}

    manifest: list[dict] = []
    for entry in registry:
        slug = entry["slug"]
        path_slug = entry.get("pathSlug", slug)
        dest_name = path_slug.replace("/", "-")
        dest = base / dest_name
        raw_url = entry["rawUrl"]
        description = entry.get("description", "")
        source = f"{entry.get('user', '?')}/{entry.get('repo', '?')}"

        manifest.append(
            {
                "slug": slug,
                "pathSlug": path_slug,
                "dest": dest_name,
                "source": source,
                "rawUrl": raw_url,
                "topics": entry.get("topics", []),
            }
        )

        if raw_url in seen_urls:
            # Symlink-style stub pointing to canonical skill
            canonical = seen_urls[raw_url]
            dest.mkdir(parents=True, exist_ok=True)
            stub = dest / "SKILL.md"
            stub.write_text(
                ensure_frontmatter(
                    f"# Alias: {slug}\n\n"
                    f"This skill shares content with `{canonical.relative_to(REPO)}`.\n\n"
                    f"- Source: {source}\n"
                    f"- Canonical URL: {raw_url}\n\n"
                    f"See the canonical skill directory for full guidance.\n",
                    slug,
                    description or f"Alias for {canonical.name}",
                )
            )
            (dest / "SOURCE.json").write_text(json.dumps(entry, indent=2) + "\n")
            fetched += 1
            continue

        content = download_text(raw_url)
        if content is None:
            failed.append(f"{slug} ({raw_url})")
            dest.mkdir(parents=True, exist_ok=True)
            (dest / "SKILL.md").write_text(
                ensure_frontmatter(
                    f"# {slug}\n\n"
                    f"**Fetch failed** — could not retrieve content from:\n\n"
                    f"- {raw_url}\n\n"
                    f"Description from ui-skills.com registry:\n\n{description}\n\n"
                    f"Re-run `npx ui-skills get {slug}` or fetch manually from GitHub.\n",
                    slug,
                    description or slug,
                )
            )
            (dest / "SOURCE.json").write_text(json.dumps(entry, indent=2) + "\n")
            continue

        dest.mkdir(parents=True, exist_ok=True)
        skill_path = dest / "SKILL.md"
        skill_path.write_text(ensure_frontmatter(scrub_content(content), slug, description or slug))
        (dest / "SOURCE.json").write_text(json.dumps(entry, indent=2) + "\n")
        seen_urls[raw_url] = dest
        fetched += 1

    (base / "REGISTRY-MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return fetched, failed


def copy_vera_skills() -> int:
    count = 0
    for rel, category in VERA_COPIES:
        src = VERA / rel
        if not src.exists():
            print(f"  SKIP missing vera path: {rel}", file=sys.stderr)
            continue
        dest_root = REPO / category
        dest = dest_root / Path(rel).name if "/" in rel else dest_root / rel
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(
            src,
            dest,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"),
        )
        for path in dest.rglob("*"):
            if path.is_file() and path.suffix in {".md", ".py", ".sh", ".tex", ".bib"}:
                try:
                    text = path.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    continue
                path.write_text(scrub_content(text), encoding="utf-8")
        count += 1
    return count


def main() -> None:
    print("Fetching ui-skills registry...")
    registry = fetch_registry()
    print(f"Registry: {len(registry)} skills")

    print("Downloading ui-skills...")
    ui_count, failed = write_ui_skills(registry)
    print(f"UI skills written: {ui_count}, failed: {len(failed)}")

    print("Copying vera skills...")
    vera_count = copy_vera_skills()
    print(f"Vera skill trees copied: {vera_count}")

    failures_path = REPO / "01-ui-design" / "FETCH-FAILURES.json"
    failures_path.write_text(json.dumps(failed, indent=2) + "\n")
    print("Done.")


if __name__ == "__main__":
    main()
