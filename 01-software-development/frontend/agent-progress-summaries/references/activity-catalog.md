# Public activity catalog

Maintain one adapter per meaningful tool family. The following are example copy patterns, not claims about a model's internal intent.

| Operation | Running text | Purpose | Supported outcome example |
|---|---|---|---|
| Search supplied documents | Searching the project documents… | To find material relevant to the requested brief. | Returned 4 matching documents, only if the result defines that count |
| Read a source | Reading the selected source… | To inspect the evidence and surrounding context. | Source request finished |
| Calculate a measure | Checking the numbers… | To derive the requested measure from supplied values. | Calculation returned; show unit/value only from a typed contract |
| Load criteria | Loading the review criteria… | To apply the selected method to this task. | Returned 6 criteria sections |
| Save an artifact | Saving the draft… | To create the requested saved version. | Draft saved, only when the result confirms persistence |
| Send an action for review | Submitting the draft for review… | To start the recorded review process. | Submission returned; review remains pending |
| Read connected data | Reading the selected records… | To retrieve the requested data from the connected account. | Data request finished |
| Unknown tool | Running a task tool… | To carry out a tool action for this request. | The tool returned its result |

For Namakan, “Checking SEC filings for CPRT” is derived from a known SEC tool and a validated ticker. In another product, substitute a document type, task name, or safe project label—not stock-specific language. Allowlist public fields and constrain their length/format. Omit private identifiers and sensitive search terms when the user-visible context does not need them.

Example adapter contract:

```text
describeTool(name, safeArguments) -> {
  displayName,
  runningSentence,
  purposeSentence,
  neutralCompletionSentence
}
summarizeResult(name, typedResult) -> {
  executionOutcome: success | error | unknown,
  publicResultSentence,
  domainOutcome?: pending | approved | rejected | other
}
```

The adapter should degrade to a neutral sentence when a provider changes shape. It should not parse arbitrary nested prose to invent a success claim. Prefer a backend public projection for sensitive integrations; hiding a field in the DOM does not remove it from the browser response.

For parallel calls, show per-call status and an aggregate active count. For streaming subprogress, display actual provider events such as “3 of 8 files processed” only when both values come from the tool contract. For long idle gaps, say “Waiting for the next update” and retain the last observed operation; do not simulate new work. If the transport is reconnecting, label that separately from model activity.
