---
name: inline-tool-call-ui
description: Present agent tool calls as compact expandable rows inside a chat transcript, with short purpose and result snippets. Use when replacing a tool-trace sidebar or raw JSON panel, or adding accessible inline tool inspection to an AI product.
---

# Inline tool-call UI

Make a tool call understandable without making it the primary content. The source pattern is the owner-approved Namakan behavior: clicking a tool box expands it downward in the conversation. Preserve the clicked context and the full width of the answer area.

## Component shape

The header contains a small tool icon, human-readable name, status, and disclosure chevron. Immediately below it, show a quiet public activity sentence and elapsed time when useful. On expansion, insert two brief fields between the header and activity sentence:

- **Purpose:** the role of this tool in the requested task, grounded in its actual metadata.
- **Result** or **Status:** a bounded description of the returned result, problem, or current wait.

Default collapsed is appropriate when calls are frequent. Allow independent expansion unless the product deliberately chooses an accordion. Do not move focus to another rail, modal, or scroll region just to explain a tool. Debug inspectors can exist separately when explicitly requested; they should not be the default reader interaction.

Read [component and state contract](references/component-contract.md) when wiring the controls, identity, outcome summaries, and layout.

## Keep snippets useful and bounded

Choose a small adapter per tool family. It maps the actual operation plus validated fields to a purpose and public result summary. For example: “To inspect the uploaded documents for the requested information”; “Returned 4 matching documents.” Count only fields with a known meaning. An arbitrary tool response is not safe UI prose merely because it is JSON.

Do not infer a successful business outcome from the presence of a completion callback. Separate transport completion, tool error, domain rejection, and review approval. Use “request finished” or “result returned” when stronger wording is unsupported. Unknown tools get a neutral description. Keep raw arguments, hidden reasoning, stack traces, provider credentials, and lengthy source content out of the snippet.

For wording and cadence, use [agent-progress-summaries](../agent-progress-summaries/SKILL.md). For replay and current-turn matching, use [streaming-chat-lifecycle](../streaming-chat-lifecycle/SKILL.md).

## Interaction and styling

Use a native button with `aria-expanded` and a stable panel association. Enter and Space toggle it, and collapsed content must not retain focusable descendants. Keep status text available on mobile. A status icon and color supplement its label. WAI's [disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/) supplies the semantic baseline.

Use the existing theme's surfaces and text roles. Join the header and expanded body with matching borders/corners. Prefer a short entrance and chevron rotation; no dramatic unfolding or delayed result. Respect reduced motion. Details increase normal document height, and the enclosing conversation owns scrolling.

Verify running→completed/failed, interrupted→new turn, keyboard toggle, long labels, repeated clicks during animation, and narrow viewports. Assert that clicking a tool does not mount a details sidebar. See the [portable demo](../agent-chat-workspace/assets/chat-workspace-reference.html) for interaction examples, not a production API implementation.
