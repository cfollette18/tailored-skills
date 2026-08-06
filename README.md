# tailored-skills

Curated agent skills for design engineering, ML/AI research, agent harnesses, and anti-slop quality — organized for [Hermes](https://github.com/NousResearch/hermes-agent) and Cursor-compatible skill loaders.

## Category map

| Dir | Theme | Skills |
|-----|-------|--------|
| `01-ui-design/` | UI/UX from [ui-skills.com](https://www.ui-skills.com/) | 202 |
| `02-ml-ai-research/` | Research, datasets, custom model planning | 8 |
| `03-agent-harness/` | Autonomous agents, MCP, training studio | 11 |
| `04-anti-ai-slop/` | Guardrails against generic AI output | 5 |
| `05-mlops/` | Training, eval, inference, datasets | 30 |
| `06-security-eval/` | Credentials, red-teaming | 2 |
| `07-software-development/` | Plan, TDD, debugging, review (no frontend fluff) | 12 |
| `08-github/` | OSS workflow, PRs, issues, auth | 6 |
| `09-diagramming/` | Excalidraw, architecture diagrams | 2 |
| `10-architectural-planning/` | Codebase redesign planning | 1 |

**Total:** 279 `SKILL.md` files (run `find . -name SKILL.md | wc -l` to verify).

Each skill lives in its own subdirectory with `SKILL.md` in Hermes/Cursor format (`name`, `description` YAML frontmatter).

## Import into Hermes

### Option A — profile import (recommended)

```bash
hermes profile import /path/to/tailored-skills
```

Or import a single category:

```bash
hermes profile import /path/to/tailored-skills/04-anti-ai-slop
```

### Option B — symlink into Hermes skills home

```bash
HERMES_SKILLS="${HERMES_HOME:-$HOME/.hermes}/skills"
mkdir -p "$HERMES_SKILLS"

# Symlink categories you want
for cat in 01-ui-design 04-anti-ai-slop 05-mlops; do
  ln -sfn "$(pwd)/$cat" "$HERMES_SKILLS/tailored-$cat"
done
```

### Option C — Cursor

Copy or symlink skill dirs into `.cursor/skills/` or reference via your Cursor skills config.

## Sources

### ui-skills.com (`01-ui-design/`)

- Full registry from `https://www.ui-skills.com/skills/registry.json` (202 entries)
- Each skill includes `SOURCE.json` with upstream author, repo, and `rawUrl`
- See `01-ui-design/REGISTRY-MANIFEST.json` for the full index

### vera subset (categories `02`–`10`, except `04`)

Copied from the on-mission subset of `/vera/skills/`:

- **Included:** research, mlops, agent harness, security, red-teaming, software-development (plan/TDD/debug — not `frontend-dev`), github, diagramming, architectural-planning
- **Excluded:** vera rules, learnings, fixes — skills only
- Personal paths scrubbed to `$PROJECT_ROOT` placeholders

### Anti-slop (`04-anti-ai-slop/`)

Original skills synthesized from:

- Web research: [AI slop UX](https://uxskill.laithjunaidy.com/what-is-ai-slop.html), [Superdesign](https://superdesign.dev/blog/why-ai-design-looks-generic), [SmoothUI](https://smoothui.dev/blog/ai-design-slop), [Rottoways](https://rottoways.com/blog/fix-ai-slop-website)
- vera `simplify-code` slop patterns (code review heuristics)

## Portability conventions

| Placeholder | Meaning |
|-------------|---------|
| `$PROJECT_ROOT` | Active workspace / ML project root |
| `${HERMES_HOME:-$HOME/.hermes}` | Hermes config and skills directory |
| `$FRONTEND_PROJECT_ROOT` | Frontend app path in monorepos |
| `$PROJECT_ENV_FILE` | Project `.env` or equivalent (never commit secrets) |
| `$EDGE_HOST` | Remote training/inference host when applicable |

**Never commit:** `.env`, tokens, keys — see `.gitignore`.

## Fetch gaps (ui-skills.com)

Some registry URLs returned 404 at import time. See `01-ui-design/FETCH-FAILURES.json`.

| Status | Skills | Handling |
|--------|--------|----------|
| **Backfilled** | MengTo taste skills (11) | Mirrored from `Leonxlnx/taste-skill` |
| **Backfilled** | `remotion-best-practices` | Alternate path on `remotion-dev/skills` |
| **Backfilled** | `next-*` (3) | Cursor Vercel plugin cache; `next-best-practices` uses `nextjs` skill |
| **Stub only** | AccessLint (5 aliases) | Registry points to missing marketplace path; stub + registry description |
| **Stub only** | `mengto-image-to-code`, `mengto-seo-audit`, `mengto-swiftui-pro` | No mirror found; stub with description |
| **Stub only** | `mattpocock-to-issues`, `mattpocock-to-prd` | Not yet in public repo |
| **Stub only** | `brotzky-*` performance skills | Repo path 404 |

Re-fetch anytime:

```bash
python3 scripts/populate_repo.py
npx ui-skills get <slug>   # upstream CLI
```

## License

MIT — see [LICENSE](LICENSE). Individual ui-skills retain upstream licenses noted in `SOURCE.json`.
