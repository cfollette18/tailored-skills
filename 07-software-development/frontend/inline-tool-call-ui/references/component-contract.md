# Component contract

Use the target framework's existing primitives. This conceptual shape is portable:

```text
ToolActivity
  button [aria-expanded, aria-controls=unique-panel-id]
    icon | name | status label | status icon | chevron
  panel [id=unique-panel-id, hidden when collapsed]
    Purpose: short public explanation
    Result/Status: short observed outcome
  activity sentence | elapsed time
```

The component needs call identity, public display name, purpose, start timestamp, optional terminal timestamp/status, and optional safe summary. It should not need the entire model trace or unfiltered tool payload. Keep expansion in UI state keyed by conversation/turn/call identity; duplicate replay should not reset it.

| State | Header | Expanded detail | Timer |
|---|---|---|---|
| Active call in active turn | Working | What was requested; waiting for result | Elapsed since actual start |
| Successful tool response | Completed | Known bounded result or neutral “result returned” | Freeze at terminal time |
| Tool error | Needs attention | Safe failure summary | Freeze at terminal time |
| Turn stopped with no terminal result | Interrupted / Stopped | No completion recorded | Stop; do not invent completion time |
| Old incomplete call during new turn | Interrupted | Prior call did not complete | Never restart its spinner |
| Unknown or missing result | Explicitly unknown | State what is unavailable | Only show a defensible duration |

A validation rejection may be a successfully executed validation tool. Keep the execution status separate from “approved,” “published,” “paid,” or other domain outcomes. Reused call IDs in different turns must never share a result.

A native button can control a panel via `hidden`; details/summary is also viable if the product can implement its required structure and styles. Do not place links or another button inside the disclosure button. Use stable unique IDs; React useId or the framework equivalent works for DOM association, while event IDs remain data keys.

Render summaries as text. If limited Markdown is necessary, constrain it with the same content policy as assistant prose. Newlines, long labels, timestamps, and translated text must wrap without pushing status/action controls off screen. Compact text is a visual choice; do not use contrast-reducing opacity on the settled content.

If exposing a source/action link, label its purpose and show it inside the expanded panel or answer. Opening a link and expanding the tool are different actions. Give the caller a useful fallback if a preview is unavailable. Avoid equating result size with usefulness; two factual sentences are usually enough.

When adapting MCP responses, inspect whether the public tool payload is wrapped in a structured `result` object. Normalize known transport wrappers before reading outcome/status; otherwise an inner error can be incorrectly labelled Completed. Keep transport parsing separate from unrestricted source-text interpretation.
