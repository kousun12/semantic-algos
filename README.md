# semantic-algos

Squishy semantic programs for LLM agents — reusable reasoning procedures that solve open-ended questions with "algorithmic" sequencing of prompts. Each skill is a thinking tool, not a code tool: it tells the agent *how* to structure its reasoning.

[![skills.sh](https://skills.sh/b/kousun12/semantic-algos)](https://skills.sh/kousun12/semantic-algos)

## Install

```bash
npx skills add kousun12/semantic-algos
```

Or install specific skills:

```bash
npx skills add kousun12/semantic-algos --skill dp-solve --skill n-whys
```

## Skills

| Skill | What it does |
| --- | --- |
| [`dp-solve`](skills/dp-solve) | Dynamic-programming-style reasoning: decompose into overlapping subproblems, memoize subanswers, synthesize from the memo table. |
| [`n-whys`](skills/n-whys) | Parameterized why-chain, exactly *n* levels deep. Invoke like `n-whys n=8 q=<question>`. |
| [`five-whys`](skills/five-whys) | Classic Five Whys — drill from surface symptoms to root causes and assumptions. |
| [`explanation-ladder`](skills/explanation-ladder) | Explain a topic at five escalating levels — High School → College → PhD → Philosopher → Gigabrain — each responding to the last. |
| [`nietzche-ladder`](skills/nietzche-ladder) | Three-stage Nietzschean explanation: Camel (burden), Lion (negation), Child (creative affirmation). |
| [`ladder-of-abstraction`](skills/ladder-of-abstraction) | Move deliberately between concrete particulars and abstract principles. |
| [`first-principles-thinking`](skills/first-principles-thinking) | Strip assumptions and rebuild the answer from fundamentals instead of analogy or convention. |
| [`golden-circle`](skills/golden-circle) | Separate purpose, method, and output: Why → How → What. |

## Why "semantic algorithms"?

Classical algorithms sequence deterministic operations over exact data. These skills sequence *prompts* over *meaning* — the control flow is precise (decompose, iterate n times, ascend the ladder) but each step is executed by an LLM's judgment. The result is a repeatable procedure for open-ended problems.
