---
name: human-please
description: >
  Adaptive explanations in the reader's language, grounded in their knowledge and preferences. Use when someone asks for plain language, says an explanation did not land, or needs a situation, project, session, concept or decision made understandable: "поясни по-простому", "объясни чистым языком", "поясни доступно", "я тупой, объясни", "я ничего не понял, давай нормально", "объясни нетехнарю", "объясни неайтишнику", "explain simply", "explícamelo sencillo", or equivalent intent in any language, even without naming this skill. Do NOT use for implementation-only requests, literal translation, quoted trigger phrases, or an explicit request for raw technical detail.
---

# Human, please

Explain to this person, about this question. Preserve accuracy while changing the route to understanding.

## Understand the reader

Read [context and preferences](references/context.md). Use the current conversation first; resolve missing preferences through scoped memory and 3 → 5 → 8 recent user sessions. Ask one targeted question if a consequential gap remains. Keep the reader profile temporary.

## Choose the explanation

Read [explanation methods](references/methods.md). Match the method to the missing understanding and the reader's purpose. Ground project/session claims in current evidence. Distinguish observed facts, reports, inferences and unknowns.

## Choose the form

Read [visuals and tools](references/visuals.md). Match the form to the relationships being explained and the current surface's actual capabilities.

## Deliver and repair

Lead with the answer in the reader's language. Build from familiar knowledge; define necessary terms in place. Include decision-relevant limits and a concrete example when it clarifies. For work status, distinguish changed, verified and remaining. If the explanation fails, change the framing instead of repeating it longer.

Check: language and depth fit; cause and effect connect; examples preserve the mechanism; claims match evidence; the reader can identify the practical consequence. Return the explanation itself.
