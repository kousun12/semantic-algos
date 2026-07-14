# semantic-algos

Semantic algorithms: squishy, general-purpose reasoning programs for LLM agents. Each skill is an "algorithmic" sequencing of prompts — a repeatable procedure for attacking open-ended questions, the way sorting algorithms attack lists.

## Install

```bash
npx skills add kousun12/semantic-algos
```

Or install a single skill:

```bash
npx skills add kousun12/semantic-algos --skill dp-solve
```

## Skills

### Decompose
| Skill | What it does |
|---|---|
| [dp-solve](skills/dp-solve) | Dynamic-programming reasoning: decompose into overlapping subproblems, memoize subanswers, synthesize bottom-up |
| [first-principles-thinking](skills/first-principles-thinking) | Strip inherited assumptions, rebuild from irreducible fundamentals |
| [assumption-audit](skills/assumption-audit) | Enumerate every load-bearing assumption, grade confidence × criticality, name the cheapest tests |

### Drill
| Skill | What it does |
|---|---|
| [n-whys](skills/n-whys) | Why-chain exactly n levels deep (`n-whys n=8 q=...`) |
| [five-whys](skills/five-whys) | The classic root-cause preset of n-whys |

### Reframe
| Skill | What it does |
|---|---|
| [inversion](skills/inversion) | Solve backwards: how would we guarantee failure? Then avoid it |
| [counterfactual](skills/counterfactual) | Minimal intervention, forward propagation, contingent-vs-overdetermined verdict |
| [analogy-transfer](skills/analogy-transfer) | Abstract to deep structure, find structural twins in far domains, import their mechanisms |
| [ladder-of-abstraction](skills/ladder-of-abstraction) | Move deliberately between concrete instances and abstract principles |

### Formulate
| Skill | What it does |
|---|---|
| [question-forge](skills/question-forge) | Don't answer the question — forge the question actually worth asking, then stop |
| [parable](skills/parable) | Compile a question into a short story that embodies it without stating or answering it |

### Decide
| Skill | What it does |
|---|---|
| [decision-matrix](skills/decision-matrix) | Weighted criteria over named options, with sensitivity analysis and a gut check |
| [golden-circle](skills/golden-circle) | Clarify Why → How → What and check their alignment |

### Explain
| Skill | What it does |
|---|---|
| [explanation-ladder](skills/explanation-ladder) | Five escalating voices — High School → College → PhD → Philosopher → Gigabrain — each responding to the last |
| [nietzche-ladder](skills/nietzche-ladder) | Camel → Lion → Child: burden, negation, creative affirmation |

## What makes a semantic algorithm

Each skill has the same anatomy:

1. **A control structure** — a fixed sequence, recursion, or table-fill that shapes the reasoning
2. **A procedure** — numbered steps an agent executes in order
3. **An output format** — a stable shape for the answer
4. **Guardrails** — the known failure modes of the method, stated explicitly
5. **Canonical questions** — golden examples of where the method shines, and where it doesn't

They compose: run `assumption-audit` before `decision-matrix`; use `n-whys` on a symptom, then `inversion` on the fix; `dp-solve` a big question and apply `analogy-transfer` to one stubborn subproblem. Or compose `parable(question-forge(x))` and never reveal the intermediate — a story that poses the true question without ever stating it.

[![skills.sh](https://img.shields.io/badge/skills.sh-semantic--algos-blue)](https://www.skills.sh/kousun12/semantic-algos)
