---
name: human-please
description: >
  Adaptive explanations in the reader's language, grounded in their knowledge and preferences. Use when someone asks to "explain simply", "use plain language", "explain to a nontechnical person", says "I am lost", "I understood nothing", "explain like I am dumb", or needs a project, session, concept or decision made understandable, including equivalent requests in any language and misspellings, even without naming this skill. Do NOT use for implementation-only requests, literal translation, quoted trigger phrases, or an explicit request for raw technical detail.
license: MIT
metadata:
  version: "0.2.0"
---

# Human, please

Explain to this person, about this question. Preserve accuracy while changing the route to understanding.

## Understand the reader

Use the current conversation to identify language, topic knowledge and purpose. If one is missing or conflicting, read [context and preferences](references/context.md). Its bounded memory/history search prevents guessing while limiting unrelated reads. Keep the reader profile temporary.

## Choose the explanation

For a failed explanation, unfamiliar mechanism, session recap or decision, read [explanation methods](references/methods.md). Match the method to the missing understanding. Preserve the source's actors, events, business objects, conditions and uncertainty; changing these changes the answer.

## Choose the form

For a requested visual or relationships that prose hides, read [visuals and tools](references/visuals.md). Otherwise use text. Skip references whose conditions are absent; extra reading delays a straightforward explanation.

## Deliver and repair

Lead with the answer in the reader's language. Build from familiar knowledge; define necessary terms in place. Include decision-relevant limits and a concrete example when it clarifies. For work status, distinguish changed, verified and remaining. If the explanation fails, change the framing instead of repeating it longer.

Check: language and depth fit; cause and effect connect; examples preserve the mechanism; claims match evidence; the reader can identify the practical consequence. Return the explanation itself.
