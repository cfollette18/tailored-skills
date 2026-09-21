---
name: design-anti-slop
description: Detect and fix generic AI UI patterns — purple gradients, Inter defaults, three-card grids, glassmorphism soup. Use when interfaces look templated or "vibecoded."
version: 1.0.0
author: tailored-skills
license: MIT
metadata:
  hermes:
    tags: [ui, design, anti-slop, taste, review]
---

# Design Anti-Slop

Use when a UI looks **instantly AI-generated**: purple hero, three feature cards, centered everything, emoji icons, glass blur on everything.

## Slop signature (spot from across the room)

In order of reliability ([source](https://uxskill.laithjunaidy.com/what-is-ai-slop.html)):

1. Violet-to-indigo gradient (`#7c3aed` → `#6366f1`) with no brand reason
2. Row of **three identical feature cards** with icon + heading + two lines
3. **Inter** (or Roboto) as the only typeface, weight 700 headlines
4. Emoji used as icons
5. Three-tier pricing with middle plan highlighted
6. Stock hero under dark scrim
7. Uniform soft shadows + same border-radius on every element
8. Centered layout with no asymmetry
9. Marketing copy with generic uplift only ("streamline", "empower", "seamless")

Four or more on one page = slop centroid.

## Explicit avoid list (paste into prompts)

```
- No Inter, Roboto, or Arial as primary/display fonts
- No purple/indigo/violet gradients on heroes or primary buttons
- No three-equal-card feature grids; prefer 1 primary + 2 secondary
- No emoji as icons; use SVG or existing icon set
- No centered-everything layouts; use asymmetry and optical alignment
- No glassmorphism + neon glow + bounce-on-hover on every element
- Headline weight 500–600, not 700, unless brand requires it
- Max 3 accent color appearances on page total
```

## Checklist before ship

### Layout & hierarchy
- [ ] At least one **asymmetric** section (one large + two small beats three equals)
- [ ] Clear focal point per viewport; eye path is intentional
- [ ] Spacing uses a consistent scale (4/8px or project tokens), not random Tailwind jumps

### Typography
- [ ] Display font is **chosen**, not defaulted — pair with distinct body face if needed
- [ ] Measure / line-length appropriate for prose blocks
- [ ] Tabular nums for data; optical sizing for mixed scales

### Color
- [ ] Primary palette has **brand or product reason** (not "premium purple")
- [ ] Contrast passes WCAG for text and interactive states
- [ ] Accent used sparingly (≤3 moments per page)

### Motion
- [ ] Motion supports state change, not decoration on every hover
- [ ] `prefers-reduced-motion` respected
- [ ] No stagger-on-everything entrance choreography

### States & accessibility
- [ ] Focus, hover, active, disabled, empty, error, loading designed
- [ ] Keyboard path works; labels not color-only

## Before / after examples

### Hero background

**Before (slop):**
```css
.hero {
  background: linear-gradient(135deg, #7c3aed, #6366f1, #06b6d4);
}
```

**After:**
```css
.hero {
  background: #0a0a0b;
  background-image: radial-gradient(ellipse 80% 50% at 70% 20%, rgba(234, 88, 12, 0.15), transparent);
}
```

### Feature section

**Before:** Three equal cards, Lucide icon, `text-center`, `rounded-2xl shadow-lg`.

**After:** One wide case-study block + two compact supporting points; left-aligned text; icon size varies with hierarchy.

### Headlines

**Before:** `font-bold` (700) on every heading.

**After:** Display at 500–600; reserve 700 for single emphasis moment if at all.

## Fix workflow

1. **Audit** — Count slop tells; screenshot annotated.
2. **Constraint doc** — Write 5-line DESIGN.md: fonts, colors, layout rules, motion budget.
3. **Highest-impact fix first** — Usually gradient + type + card grid.
4. **Re-audit** — Purple often reappears in hover states if not banned explicitly.

## References

- [What is AI slop?](https://uxskill.laithjunaidy.com/what-is-ai-slop.html)
- [Why AI Design Looks Generic](https://superdesign.dev/blog/why-ai-design-looks-generic)
- [How to fix an AI slop website](https://rottoways.com/blog/fix-ai-slop-website)
- [Why Your AI Keeps Building the Same Purple Gradient Website](https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website)
- [SmoothUI: build → critique → fix loop](https://smoothui.dev/blog/ai-design-slop)
