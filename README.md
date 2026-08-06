# tailored-skills

Portable **skills** for AI coding agents (Hermes, Cursor, and similar harnesses). Skills are organized in numbered categories so you can copy whole folders into a profile without hand-editing paths.

**Agent rules** (`.mdc`) live in the companion repo **[tailored-rules](https://github.com/cfollette18/tailored-rules)** — not in this repository.

## Layout

```
tailored-skills/
├── README.md
├── LICENSE
└── skills/                    # numbered skill categories (see below)
    ├── 01-ui-design/
    ├── 02-ml-ai-research/
    ├── 03-agent-harness/
    ├── 04-anti-ai-slop/
    └── ...
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

### Quick copy (Hermes profile)

```bash
PROFILE=default
mkdir -p ~/.hermes/profiles/$PROFILE/skills
cp -r skills/01-ui-design ~/.hermes/profiles/$PROFILE/skills/
```

### Rules

For portable `.mdc` rules (security, anti-slop, UI craft, agent discipline), use [github.com/cfollette18/tailored-rules](https://github.com/cfollette18/tailored-rules).

## License

MIT — see [LICENSE](LICENSE).
