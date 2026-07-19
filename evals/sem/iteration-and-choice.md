# Evaluation: bounded iteration and semantic choice

## Purpose

Check that Sem can introduce a useful language-level construct, expand every
semantic judgment into its own worker, enforce an observable stopping test and
hard bound, and execute only the selected terminal branch.

## User-style invocation

Present only this block to the system under evaluation:

```text
$sem-run I keep abandoning hobbies as soon as I become competent at them.

Use a little spiral: in each round, forge the current question, have a fresh judge compare the incoming and forged questions, and stop if their meaning differs only cosmetically. If it has not stopped, ask a three-level why-chain about the forged question and use the deepest resulting claim as the next round's input. Never exceed three rounds.

After the spiral, have a fresh selector decide whether the surviving tension is mainly practical or existential. If practical, run inversion toward a concrete guard plan. If existential, turn it into a parable. Show me the round trail and return only the chosen branch's result. Do not run both endings.
```

## Compilation must preserve

- The “spiral” is an invented construct with a local gloss explaining round
  inputs, generated applications, result propagation, termination, maximum
  rounds, visibility, and failure behavior.
- Every round's question forge, semantic equivalence judgment, and executed
  three-level why-chain is identifiable. The equivalence judgment is not a
  mechanical string comparison.
- A `true` cosmetic-change judgment stops expansion. The hard cap of three
  rounds stops it even if the semantic predicate never does.
- The deepest why-chain claim feeds the next round only when another round is
  allowed. Exhaustion behavior and the final surviving tension are explicit.
- Route selection is a semantic application with “practical” and “existential”
  criteria stated well enough for a fresh worker. Only the selected
  standard-library branch runs: `inversion` or `parable`.
- The round trail is visible, while only the selected terminal result is
  returned. The compiler may invent any readable notation for this behavior.
- Expansion is bounded above by three applications per round plus one selector
  and one selected branch (eleven semantic applications at most); unused work
  may be skipped and unchosen work must not run.

## Independent applications

- Every question-forge, stop predicate, and why-chain execution is a separate
  fresh no-history application with its own artifact.
- A predicate depends only on the incoming and forged questions for its round.
  A why-chain depends on that forged question and runs only if needed.
- The route selector is a separate application after the spiral terminates.
- The chosen inversion or parable is another application. The other branch has
  no worker and no fabricated result directory.
- Applications from different rounds are dependency-ordered; the runner must
  not hide the loop inside one persistent subagent.

## Expected run artifact shape

The normal top-level Markdown trace is present. Before execution,
`interpretation.md` explains the dynamic construct and known static boundaries;
dated amendments or `run.md` entries record each generated application and why
another round was or was not created.

Every generated semantic call has its own prompt/result/status directory.
Statuses and the run log make the stopping predicate, cap, selector result, and
chosen route reconstructable. `final.md` links the visible round trail and
chosen result, says which stop fired, records that the unchosen branch did not
run, and indexes all generated Markdown artifacts.

## Observable failure signs

- The compiler rejects the spiral because it has no built-in syntax, or expands
  it without a usable local gloss.
- One worker performs several rounds, decides its own stop, or also selects and
  executes the ending.
- Stopping is inferred from wording similarity without a fresh semantic
  predicate application.
- More than three rounds or more than eleven semantic applications execute.
- Both inversion and parable run, or neither selector criteria nor selector
  result is recorded.
- Generated applications are missing from `interpretation.md`/`run.md`, lack
  standalone artifacts, or cannot be reconstructed from the run directory.

## Evaluation note

There is no golden number of rounds, route choice, program spelling, or prose
result. Different defensible semantic judgments are acceptable within the
declared stop, bound, and artifact rules.
