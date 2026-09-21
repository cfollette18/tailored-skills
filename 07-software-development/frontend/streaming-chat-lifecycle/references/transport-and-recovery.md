# Transport and recovery

Choose the existing product transport if it supports the requirements. SSE is suitable for server-to-browser event delivery; requests to send or stop work can use normal HTTP. WebSockets, fetch streams, or framework transports can implement the same public event model.

## SSE integration notes

Serve correctly framed `text/event-stream` messages with stable IDs. Native EventSource reconnects and provides a last-event cursor; replay events after that cursor and deduplicate on the client. Named SSE events use corresponding listeners. Close subscriptions on unmount or confirmed terminal state. These mechanics are documented in [MDN's SSE guide](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events).

Do not recreate the stream on every elapsed-time tick or transcript update. Keep the initial cursor plus reconnect semantics coherent. A comment heartbeat can keep a connection alive, but is not a model reasoning update. Verify proxy buffering and disconnect behavior in the target deployment.

## Recovery policy

| Situation | Product behavior |
|---|---|
| Transport drops during an active run | Reconnecting state; preserve transcript; retry subscription, not side effects |
| Final event races with status read | Recheck durable status and replay through the terminal cursor |
| Browser switches conversations | Close/unsubscribe old view; route late events by conversation identity |
| Browser closes | Follow explicit server job policy; do not assume stop |
| Process crashes | Mark unresolved work interrupted or reconcile with durable jobs |
| User presses Stop | Request cancellation, acknowledge stopping, settle when the backend confirms |
| Stop follows completed side effect | Keep the saved side effect and explain its state accurately |
| Second submit during active turn | Apply the product's explicit queue/one-run policy; avoid accidental duplicate runs |
| Start request times out | Recover by idempotency key or server run lookup before retrying |

The Namakan implementation is loopback/single-user, with a local SQLite event store and one active model run. Those constraints are source context, not a multi-user deployment recipe. A publicly hosted port needs the product's authenticated user/tenant boundaries and job lifecycle; use the repository's relevant authentication/deployment skills when that work is in scope.
