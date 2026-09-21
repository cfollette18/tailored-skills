# Portable public event contract

This is an adaptation contract, not a verbatim Namakan API. Namakan currently uses ordered numeric event IDs, chat identity, tool call IDs, and user-event boundaries to determine the current turn. Prefer explicit turn IDs when the destination backend supports them.

```ts
type PublicEvent = {
  eventId: string;       // unique within the replay domain
  sequence: number;      // ordering cursor scoped to this conversation
  conversationId: string;
  turnId: string;
  timestamp: string;     // server timestamp
  type: 'user' | 'commentary' | 'tool_start' | 'tool_end'
      | 'assistant_delta' | 'assistant_final' | 'turn_end';
  payload: {
    callId?: string;
    messageId?: string;
    tool?: string;
    publicPurpose?: string;
    publicSummary?: string;
    safeArguments?: Record<string, string | number | boolean>;
    text?: string;
    outcome?: 'success' | 'error' | 'unknown';
    turnStatus?: 'completed' | 'failed' | 'cancelled' | 'interrupted';
  };
};
```

This type documents relationships; perform runtime validation at the boundary. Not every field is allowed for every event. Keep private model reasoning, system prompts, credentials, and full source/tool payloads outside the public contract. A UI-only renderer is not a security boundary.

## Reducer invariants

1. Accept only events for the active conversation; store background results under their own conversation.
2. Deduplicate by event identity. Do not derive new keys from render order.
3. Apply ordered events or buffer gaps; never assume arrival order across reconnects.
4. Tool identity is `(conversationId, turnId, callId)`. Match terminal events to that identity; unknown terminals can wait for replayed starts.
5. A turn-end event settles unresolved calls as interrupted/unknown according to the backend contract. It must not fabricate success.
6. A late event may reconcile a persisted result only under a documented server rule; it must not revive cancelled UI work on its own.
7. Finalize a streamed assistant message by message identity. Replaying its final snapshot replaces/reconciles its accumulated deltas; it does not append a second answer.
8. Derive current-turn counts from unique calls with terminal events. “Finished” may include errors; “successful” must count actual successes separately.

Keep timestamps for display and duration, not as the only ordering key. On a live mounted component, a monotonic clock can measure elapsed time; on reopen, reconstruct from recorded start/end timestamps and clamp clock skew. Freeze duration at terminal time. A missing terminal timestamp cannot produce an exact completion duration.

## Example sequence

```text
turn-1 user
turn-1 tool_start call-A
turn-1 tool_start call-B
turn-1 tool_end call-B error
turn-1 tool_end call-A success
turn-1 assistant_final message-1
turn-1 turn_end completed
turn-2 user
turn-2 tool_start call-A       # valid reuse; different turn
turn-2 turn_end cancelled     # call-A is not marked completed
```

A completed turn can explain a failed tool. If a side effect completed just before cancellation, preserve its recorded outcome; stopping the conversation does not undo it.
