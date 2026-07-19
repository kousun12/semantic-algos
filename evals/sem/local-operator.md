# Evaluation: locally defined operator

## Purpose

Check that compilation invents a clear local semantic operator when no
repository skill has the requested contract, labels it honestly, and then
composes it with an exact standard-library function.

## User-style invocation

Present only this block to the system under evaluation:

```text
$sem-run Two people gave me these accounts of a rollback:

Dana: "At 2:10 the error rate crossed 8%. Lee said the new cache was safe, so I waited ten minutes before rolling back."
Lee: "At 2:10 the dashboard showed an 8% spike. I said the cache metrics were incomplete and Dana decided to wait before rolling back."

First make a neutral ledger that separates only the observations both accounts support from interpretations attributed to each speaker. Do not decide who is truthful and do not add facts. Also identify which attributed interpretation most directly bore on the decision to wait. Then audit the assumptions inside that one interpretation. Return both the ledger and the audit.
```

## Compilation must preserve

- The neutral-ledger operation is local. No existing repository skill exactly
  contracts to reconcile witness accounts into shared observations and
  attributed interpretations.
- The local definition states its purpose, accepted input, concrete moves,
  return shape, stopping condition, and guardrails. In particular, it stops
  after classifying the supplied claims, preserves attribution, adds no facts,
  and makes no credibility judgment.
- Selecting the interpretation most directly connected to the wait decision is
  part of the ledger's declared output, so the downstream input is unambiguous.
- `assumption-audit` resolves to the repository skill and receives only that
  selected attributed interpretation as its semantic focus, with the ledger
  available only if explicitly declared as supporting context.
- Both the ledger and audit are returned in that order.
- The compiler may name and notate the local operator freely. Its contract, not
  a particular spelling, is what this evaluation requires.

## Independent applications

- Producing the ledger is one fresh-worker application of the complete local
  contract.
- Auditing the selected interpretation is a second fresh-worker application
  using the full `assumption-audit` contract.
- These applications are sequential because the audit depends on the local
  result. They must not be collapsed into a single analyst prompt.

## Expected run artifact shape

The top-level program and compile notes explicitly distinguish the local
operator from repository functions and contain enough of its contract for a
fresh reader to execute it. `interpretation.md` records the two applications,
their dependency, declared input slices, and ordered returns.

Under `applications/`, the ledger and audit each have independent prompt,
result, and status files. The ledger result is understandable without chat
history and links its source provenance; the audit result links the selected
ledger output. `final.md` returns both artifacts in order and indexes the whole
Markdown run.

## Observable failure signs

- The compiler claims a repository skill provides the ledger contract when it
  does not, or labels the local function as standard library.
- The local definition is merely “make a neutral ledger” with no moves, result
  shape, stopping rule, or guardrails that a fresh worker can follow.
- Unsupported facts are merged into the agreed record, attribution is lost, or
  the worker decides which narrator is truthful.
- The audit runs on the entire incident instead of the selected interpretation.
- One worker creates both the ledger and the audit.
- `program.md`, an application prompt, or `final.md` depends on undisclosed chat
  context to explain what the local operation meant.

## Evaluation note

Do not require a golden ledger, a golden audit, a fixed local-operator name, or
one program syntax. Require only a defensible classification and an executable
local contract with honest provenance.
