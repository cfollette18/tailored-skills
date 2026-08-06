# tailored-skills

Portable **skills** and **rules** for AI coding agents (Hermes, Cursor, and similar harnesses). Everything is organized in numbered categories so you can copy whole folders into a profile without hand-editing paths.

## Layout

```
tailored-skills/
├── README.md
├── LICENSE
├── skills/                    # numbered skill categories (see below)
│   ├── 01-ui-design/
│   ├── 02-ml-ai-research/
│   ├── 03-agent-harness/
│   ├── 04-anti-ai-slop/
│   └── ...
└── rules/                     # numbered rule categories
    ├── README.md              # loading + copy instructions
    ├── 01-security-and-secrets/
    ├── 02-portability/
    ├── 03-research-workflow/
    ├── 04-anti-ai-slop/
    ├── 05-ui-craft/
    └── 06-agent-discipline/
```

## Skills

Skills live under top-level numbered directories (`01-…`, `02-…`). Each skill is a folder with a `SKILL.md` (Hermes/Cursor skill format).

| Category | Theme |
|----------|-------|
| `01-ui-design/` | UI craft from ui-skills.com principles |
| `02-ml-ai-research/` | ML/AI research workflows |
| `03-agent-harness/` | Agent harness and tooling |
| `04-anti-ai-slop/` | Minimize generic AI output |

Copy a category or individual skill into `~/.hermes/profiles/<name>/skills/` or your editor's skills directory.

## Rules

Rules live under `rules/` in the same numbered category style. Each rule is a `.mdc` file (Markdown + YAML frontmatter).

| Category | Theme |
|----------|-------|
| `01-security-and-secrets/` | No secrets, keys, or personal paths |
| `02-portability/` | Artifacts must work for any clone |
| `03-research-workflow/` | Reproducible research discipline |
| `04-anti-ai-slop/` | Ban generic UI, prose, and unverified claims |
| `05-ui-craft/` | Surface-first composition, type, spacing |
| `06-agent-discipline/` | Prompt cache stability, hook hygiene |

See [rules/README.md](rules/README.md) for Hermes vs Cursor loading paths and copy examples.

### Quick copy (Hermes profile)

```bash
PROFILE=default
mkdir -p ~/.hermes/profiles/$PROFILE/rules
cp rules/01-security-and-secrets/*.mdc ~/.hermes/profiles/$PROFILE/rules/
cp rules/02-portability/*.mdc ~/.hermes/profiles/$PROFILE/rules/
```

### Quick copy (Cursor project)

```bash
mkdir -p .cursor/rules
cp rules/04-anti-ai-slop/*.mdc .cursor/rules/
cp rules/05-ui-craft/*.mdc .cursor/rules/
```

## License

MIT — see [LICENSE](LICENSE).
