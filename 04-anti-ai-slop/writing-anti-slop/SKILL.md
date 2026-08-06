---
name: writing-anti-slop
description: Cut hedging, filler, buzzwords, and engagement bait from technical and product writing. Use for docs, PRs, marketing copy, and agent responses.
version: 1.0.0
author: tailored-skills
license: MIT
metadata:
  hermes:
    tags: [writing, communication, anti-slop, clarity]
---

# Writing Anti-Slop

Use when prose feels **template-generated**: hedging everywhere, buzzword stacks, bullets that say nothing, or endings that bait engagement.

## Slop tells

- **Hedging chains:** "It's worth noting that...", "In order to...", "It should be mentioned..."
- **Buzzwords without referents:** leverage, robust, seamless, cutting-edge, holistic, synergy, delve, landscape, ecosystem (when vague)
- **False simplicity:** "Simply", "just", "easily" before a non-simple step
- **Empty bullets:** Each bullet restates the heading with different words
- **Engagement bait:** "Let me know if you'd like...", "Happy to help with...", "Say the word and I'll..."
- **Over-qualification:** Apologizing for existing; narrating tool calls the reader didn't ask for
- **Thesaurus syndrome:** Same idea repeated with synonyms in one paragraph

## Checklist

- [ ] First sentence answers **what changed** or **what to do**
- [ ] Every paragraph adds **one** new fact, decision, or instruction
- [ ] Active voice; subject performs action
- [ ] Concrete nouns (file names, metrics, APIs) replace abstractions
- [ ] Length proportional to complexity — no padding
- [ ] No unsolicited follow-up offers unless user asked for options

## Before / after

### PR description

**Before:**
> This PR leverages a robust approach to seamlessly enhance the authentication flow, ensuring a more holistic user experience while maintaining best practices.

**After:**
> Add refresh-token rotation to `/api/auth/refresh`. Expired refresh tokens now return 401 and clear the session cookie. Fixes #412.

### Technical explanation

**Before:**
> It's important to note that you'll want to carefully consider implementing a comprehensive validation layer in order to ensure data integrity across the system.

**After:**
> Validate `email` and `teamId` in `createInvite` before calling the DB. Reject unknown team IDs with 404.

### Agent reply ending

**Before:**
> I've updated the config! Let me know if you'd like me to also add tests or refactor the module — happy to help!

**After:**
> Updated `config.ts` with the new timeout. Tests in `config.test.ts` still pass.

## Revision pass (mandatory for outward-facing text)

1. Delete first draft intro paragraph; start at the substance.
2. Highlight every adjective; remove those that don't change meaning.
3. Replace buzzwords with **specific mechanism**.
4. Merge duplicate bullets.
5. Read aloud — if a sentence could appear on any company's blog, rewrite it.

## Tone by context

| Context | Target tone |
|---------|-------------|
| Commit message | Imperative, ≤72 char subject, why in body |
| PR / review | Evidence-linked; no praise padding |
| User docs | Task-oriented; numbered steps |
| Marketing | Specific benefit + proof; ban unmeasurable claims |

## References

- Strunk & White: omit needless words
- [AI slop in UX copy](https://uxskill.laithjunaidy.com/what-is-ai-slop.html) (generic uplift phrases)
- Internal: `07-software-development/simplify-code` (Reviewer 2 flags restating comments)
