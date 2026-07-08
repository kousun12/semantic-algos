---
name: five-whys
description: Use the Five Whys method as a thinking tool for any question, problem, failure, confusion, or decision where the user wants to move from surface symptoms to deeper causes, assumptions, or principles.
compatibility: Created for Zo Computer
metadata:
  author: rob.zo.computer
---

# Five Whys

Use this skill when a question, problem, observation, bug, decision, emotional reaction, disagreement, or confusing situation would benefit from drilling down through layers of causality.

## Purpose

The Five Whys method repeatedly asks "why?" to move from the obvious surface explanation toward deeper causes. The goal is not always exactly five steps; stop when the next "why" becomes speculative, circular, or no longer useful.

## Procedure

1. State the surface issue in one sentence.
2. Ask "why did this happen / why does this seem true / why does this matter?"
3. Answer with the most concrete, testable explanation available.
4. Repeat the why-question on the answer.
5. Continue until you reach one or more root causes, structural causes, hidden assumptions, or irreducible tradeoffs.
6. Separate facts from guesses.
7. End with practical implications: what to check, change, test, or decide next.

## Output format

Use this concise structure unless the user asks otherwise:

```markdown
## Surface issue
...

## Five Whys
1. Why? ...
   - Because ...
2. Why? ...
   - Because ...
3. Why? ...
   - Because ...
4. Why? ...
   - Because ...
5. Why? ...
   - Because ...

## Likely root cause / deeper principle
...

## What to do next
- ...
```

## Guardrails

- Do not force exactly five whys if fewer or more are useful.
- Do not pretend uncertain causal links are known; label them as hypotheses.
- For human or organizational topics, avoid blame. Look for systems, incentives, constraints, and feedback loops.
- For philosophical or conceptual topics, treat each "why" as a move toward a deeper premise, not necessarily a literal cause.
