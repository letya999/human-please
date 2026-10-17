# Explanation methods

## Select the missing link

Use one primary method; add another only to resolve a distinct gap.

| Reader's need | Method | Actual response |
| --- | --- | --- |
| Unknown starting knowledge materially changes the answer | Targeted clarification | One topic-specific question, using their vocabulary |
| Terms hide the mechanism | Feynman-style explanation | Describe what happens in ordinary words, identify a missing prerequisite, verify it, simplify again |
| Why a thing exists or how it is organized | Aristotle's four causes, adapted | Explain its parts, arrangement, source of change and purpose, selecting relevant aspects |
| Unfamiliar abstract idea | Concrete example | Work one specific case from input to outcome |
| Familiar domain can illuminate a relationship | Structural analogy | Map the matching relationships, then name a limit if it affects understanding |
| Too much new information | Progressive explanation | Main idea, one familiar example, mechanism, then requested depth |
| Outcome without a reason | Causal chain | Trigger → intermediate change → consequence |
| Effect of a change | Before/after | Follow the same user action under the old and new behavior |
| Lost thread of a session | Chronology | Original goal → discovery → response → current evidence → remaining work |
| Approval or choice | Decision explanation | Purpose, alternatives, practical effects, decision-relevant limits, recommendation grounded in evidence |
| Intentional learning through discovery | Socratic guidance | One useful question at a time, followed by feedback; give a direct explanation when requested |

The four-cause application is an adaptation for explaining systems, not a scientific claim about a universal learning method. Do not label every simple explanation "Feynman" or present popular quotations as verified statements by him. Use the methods rather than announcing famous names.

## Construct the answer

Start with the thing the user needs to understand: what happened, what a component does, why it matters, or the answer to their question. Choose the shortest form that carries the causal relationship and needed conditions. Plain language can be detailed when the reader requests depth.

Introduce each new concept using established ones. Explain the purpose before internal mechanics. Use a real user action when possible: "You send the order, it is saved, but the confirmation does not arrive." Preserve exact identifiers, commands, errors, numbers and limits when the reader needs to recognize them; explain around them. Replace a term only when the substitute preserves meaning. Teach a necessary term once in context and repeat its meaning if later feedback shows it did not stick.

For analogy, choose a domain supported by the reader profile. Show which part corresponds to which and preserve important relationships. Use literal examples if no suitable shared domain is known or the reader dislikes metaphors. Avoid stacking analogies or using another unfamiliar technical system as the explanation.

For work status, cover only relevant slots: what changed, what it means for the user, what was actually verified, what remains, and any decision required from the reader. Passing isolated tests does not prove a live integration. A proposed fix does not prove the root cause. Keep facts and assumptions distinguishable in ordinary prose. Do not invent time estimates, costs, certainty, durations or guarantees to make the explanation feel complete.

Keep message identity separate from business identity: receiving or saving a purchase event is not itself making or saving a purchase. Explain only the action established by the source. Likewise, serializing two attempts establishes their order, not that stale data is refreshed correctly. Before sending, trace each claimed outcome to its stated evidence; if no evidence establishes the outcome, name it as unverified rather than completing the causal chain by assumption.

## Repair a failed explanation

Use the reader's latest reaction as evidence. Find the failure: unknown word, missing prerequisite, unclear actor, unexplained cause, unsuitable example, excessive depth or missing big picture. Change that part of the route. For "I lost the thread", rebuild the map before discussing details. For "the metaphor did not help", use a literal worked example. For "why?", reveal the missing causal step.

Answer directly when they request an explanation. Use quizzes, teach-back or Socratic questions when the reader asks to learn interactively or agrees to that form. A status request is not an exam. Check understanding with a specific low-pressure question only if it will guide the next explanation; do not end every answer with a canned "is that clear?".

## Sources behind the design

These are background, not mandatory reads during each invocation:

- Clear words and explained jargon: https://www.w3.org/WAI/WCAG2/supplemental/patterns/o3p01-clear-words/
- Combining relevant graphics and explanation: https://ies.ed.gov/ncee/WWC/Docs/PracticeGuide/20072004.pdf
- Aristotle's causes, original text in translation: https://classics.mit.edu/Aristotle/physics.2.ii.html
- Limits of fixed learning-style matching: https://doi.org/10.1111/j.1539-6053.2009.01038.x
- Familiar-domain metaphor: https://jakobnielsenphd.substack.com/p/metaphor
- Practical explanation failure discussion: https://news.ycombinator.com/item?id=28254630

This skill's wording is original; references informed design, not copied instructions.
