# tailored-skills


**Agent rules** (`.mdc`) live in the companion repo **[tailored-rules](https://github.com/cfollette18/tailored-rules)** — not in this repository.
Curated agent skills for design engineering, ML/AI research, agent harnesses, and anti-slop quality — organized for [Hermes](https://github.com/NousResearch/hermes-agent) and Cursor-compatible skill loaders.

## Category map

| Dir | Theme | Skills |
|-----|-------|--------|
| `01-ui-design/` | General UI/UX from [ui-skills.com](https://www.ui-skills.com/) and original frontend theming and motion | 200 |
| `02-ml-ai-research/` | Research, datasets, custom model planning | 8 |
| `03-agent-harness/` | Agent runtimes, Hermes profile layout, hooks, context loading, skill authoring, subagents, MCP, training studio | 18 |
| `anti-ai-slop/` | Anti-slop principles, code, writing, design, presentations, icon libraries, free typography, color, and motion quality | 35 |
| `05-mlops/` | Training, eval, inference, datasets | 30 |
| `06-security-eval/` | Credentials, red-teaming | 2 |
| `07-software-development/` | Plan, TDD, debugging, review (no frontend fluff) | 10 |
| `08-github/` | OSS workflow, PRs, issues, auth | 6 |

**Total:** 309 `SKILL.md` files (run `find . -name SKILL.md | wc -l` to verify).

Each skill lives in its own subdirectory with `SKILL.md` in Hermes/Cursor format (`name`, `description` YAML frontmatter).

### Anti-slop skills (`anti-ai-slop/`)

All anti-slop skills now live in [`anti-ai-slop/`](anti-ai-slop/README.md): five original quality guides, nine imported frontend/writing/presentation guides, four icon-library guides, thirteen free-typography guides, two color-quality guides, and two motion-quality guides. The icon guides are:

| Skill | Use |
|-------|-----|
| [phosphor-icons](anti-ai-slop/phosphor-icons/SKILL.md) | React integration, visual weights, and complete Phosphor migrations |
| [iconoir-icons](anti-ai-slop/iconoir-icons/SKILL.md) | SVG sizing, shared stroke defaults, and Iconoir migrations |
| [radix-icons](anti-ai-slop/radix-icons/SKILL.md) | Compact toolbar/menu icons and native-grid rendering |
| [streamline-icons](anti-ai-slop/streamline-icons/SKILL.md) | Family selection and licensed SVG/JSX asset integration |

The icon guides include accessible control treatment and migration verification. The [free-font selection guide](anti-ai-slop/free-font-selection/SKILL.md) covers 12 families: Cabinet Grotesk, Uncut Sans, Bricolage Grotesque, Ranade, IBM Plex Sans, Instrument Sans, Source Sans 3, Switzer, Newsreader, Source Serif 4, Fraunces, and IBM Plex Mono. Each has a dedicated skill; see [the typography index](anti-ai-slop/README.md#free-typography).

These original integration skills are separate from the 202-entry upstream registry. Their `SOURCE.json` records link to official documentation and distinguish free commercial-use licensing from open-source licensing. No third-party icon or font assets are bundled.

### `03-agent-harness/` in more detail

Portable skills for **how the agent harness works** (not ML training UI alone):

- Autonomous agent runtimes (Hermes, Claude Code, Codex, OpenCode, computer-use)
- Hermes profile layout — rules / learnings / fixes / skills / hooks piping
- Shell hooks (`pre_tool_call` block/audit) and session / prompt-cache discipline
- Context loading parity (`AGENTS.md`, `SOUL.md`, `.hermesrules` / `.cursorrules`)
- Skill authoring, portable harness conventions, subagent delegation
- Native MCP client integration
- Reproducible training-studio patterns (API, recipes, trainer, workflow)

## Reusable color theming

Frontend implementation skills live in `01-ui-design/`:

- [semantic-color-theming](01-ui-design/semantic-color-theming/SKILL.md) — roles, tokens, component/state migrations, and asset consistency.
- [theme-accessibility-validation](01-ui-design/theme-accessibility-validation/SKILL.md) — contrast and rendered interaction checks.

Color direction and review skills live in `anti-ai-slop/`:

- [restrained-color-design](anti-ai-slop/restrained-color-design/SKILL.md) — purposeful use of an owner-selected palette.
- [color-consistency-review](anti-ai-slop/color-consistency-review/SKILL.md) — find and repair theme drift across surfaces.

All four are brand- and framework-agnostic. They are original guides, separate from the 202-entry upstream registry, and do not prescribe Namakan or Databricks colors.

## Animation, transitions, and motion

Seven original skills separate motion direction, implementation, reference research, and verification:

| Skill | Use |
|---|---|
| [motion-anti-slop](anti-ai-slop/motion-anti-slop/SKILL.md) | Choose purposeful motion and preserve deliberate icon character without generic effects |
| [motion-quality-review](anti-ai-slop/motion-quality-review/SKILL.md) | Audit choreography, repetition, reference fidelity, and delayed interaction |
| [frontend-motion-system](01-ui-design/frontend-motion-system/SKILL.md) | Motion roles, timing/easing tokens, engine choices, and interruption policy |
| [animated-interface-icons](01-ui-design/animated-interface-icons/SKILL.md) | Authored SVG/Lottie-style icon gestures inside stable controls |
| [navigation-and-view-transitions](01-ui-design/navigation-and-view-transitions/SKILL.md) | Sidebar, selection, drawer, popover, and view continuity |
| [motion-accessibility-performance](01-ui-design/motion-accessibility-performance/SKILL.md) | Reduced motion, keyboard/touch, lifecycle, and rendering verification |
| [motion-reference-research](01-ui-design/motion-reference-research/SKILL.md) | Evidence-based website/video analysis with a timestamp-aware extraction helper |

The [Muse sidebar study](01-ui-design/animated-interface-icons/references/muse-sidebar-study.md) includes six icon-only filmstrips from an owner-supplied recording, timestamped observations, public implementation findings, and adaptation guidance. It distinguishes observed gestures, source-confirmed primitives, and proposed implementations. The original video, surrounding conversation, and proprietary Muse animation assets are not bundled.

These skills are product- and framework-agnostic. The Muse and investing-workspace examples are contextual references, not mandatory styles. Each skill records its primary sources in `SOURCE.json`; the upstream registry remains unchanged by these original additions.

## Import into Hermes

### Option A — profile import (recommended)

```bash
hermes profile import /path/to/tailored-skills
```

Or import a single category:

```bash
hermes profile import /path/to/tailored-skills/anti-ai-slop
```

### Option B — symlink into Hermes skills home

```bash
HERMES_SKILLS="${HERMES_HOME:-$HOME/.hermes}/skills"
mkdir -p "$HERMES_SKILLS"

# Symlink categories you want
for cat in 01-ui-design anti-ai-slop 05-mlops; do
  ln -sfn "$(pwd)/$cat" "$HERMES_SKILLS/tailored-$cat"
done
```

### Option C — Cursor

Copy or symlink skill dirs into `.cursor/skills/` or reference via your Cursor skills config.

## Sources

### ui-skills.com (`01-ui-design/` and `anti-ai-slop/`)

- Full registry from `https://www.ui-skills.com/skills/registry.json` (202 imported entries: 193 UI and 9 anti-slop)
- Each imported skill includes `SOURCE.json` with upstream author, repo, and `rawUrl`
- See `01-ui-design/REGISTRY-MANIFEST.json` for the imported registry index; `dest` paths are relative to `01-ui-design/`, including relocated `../anti-ai-slop/` entries. The import script preserves that routing.

### vera subset (categories `02`–`08`, except `04`)

Copied and adapted from the on-mission subset of `/vera/skills/` plus Hermes profile knowledge (`rules/`, `hooks/`, agent-hooks patterns):

- **Included:** research, mlops, agent harness, security, red-teaming, software-development (plan/TDD/debug — not `frontend-dev`), github
- **Harness expansions:** profile layout, shell hooks, context loading, prompt-cache discipline, portable authoring; skill-authoring and subagent workflows live under `03-agent-harness/`
- **Excluded:** diagramming, architectural-planning categories; vera learnings/fixes blobs — skills and portable harness docs only
- Personal paths scrubbed to `$PROJECT_ROOT` / `$HERMES_HOME` placeholders

### Original anti-slop guides (`anti-ai-slop/`)

The five original quality guides were synthesized from:

- Web research: [AI slop UX](https://uxskill.laithjunaidy.com/what-is-ai-slop.html), [Superdesign](https://superdesign.dev/blog/why-ai-design-looks-generic), [SmoothUI](https://smoothui.dev/blog/ai-design-slop), [Rottoways](https://rottoways.com/blog/fix-ai-slop-website)
- vera `simplify-code` slop patterns (code review heuristics)

The category also contains the nine imported anti-slop guides with their original provenance and four icon-library skills, thirteen free-typography skills, two color-quality skills, and two motion-quality skills grounded in primary sources and reference analysis. See [the category index](anti-ai-slop/README.md).

## Portability conventions

| Placeholder | Meaning |
|-------------|---------|
| `$PROJECT_ROOT` | Active workspace / ML project root |
| `${HERMES_HOME:-$HOME/.hermes}` | Hermes config and skills directory |
| `$HERMES_AGENT_ROOT` | Checkout of hermes-agent when contributing upstream |
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
