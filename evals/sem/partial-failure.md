# Evaluation: partial failure in a fan-out

## Purpose

Check that one terminal branch failure does not cancel independent work, that
failure is not converted into invented semantic output, and that finalization
leaves an honest, resumable Markdown account.

## User-style invocation

Present only this block to the system under evaluation:

```text
$sem-run Treat this as the entire release plan: “Ship the billing migration Friday. Kim owns the rollout. Roll back if error rate exceeds 2%.”

Run three branches in parallel:
1. invert the goal of shipping safely on Friday into an anti-failure plan;
2. audit the release plan's assumptions;
3. apply a local `approvalBoundSummary`: it may summarize only when its input contains the exact standalone line `APPROVED: yes`; if that line is absent, the application must terminate as Failed without a result. Do not infer approval, substitute another condition, or retry this semantic failure.

The supplied plan intentionally has no approval line. Let independent branches finish. Return the inversion and audit in that order, followed by an honest note about the failed branch.
```

## Compilation must preserve

- The input is one shared plan value feeding three independent branches.
- `inversion` and `assumption-audit` resolve to their exact repository
  contracts and retain their distinct output forms.
- `approvalBoundSummary` is local, with the exact approval precondition,
  absence behavior, return condition, and no-inference/no-retry guardrails
  fully available to its worker.
- Missing approval is a deliberate terminal semantic failure for that
  application, not compiler ambiguity, successful refusal prose, or a reason
  to block the independent branches.
- The two successful results retain the requested presentation order. The
  failed branch is reported honestly but has no accepted semantic result.
- Any readable fan-out notation is acceptable; no golden program syntax is
  implied by the numbered prose.

## Independent applications

- Inversion, assumption audit, and approval-bound summary are three separate
  fresh no-history applications with only the shared plan as semantic input.
- All three are ready together and may be scheduled in one batch. Neither
  successful branch depends on the failing branch.
- The failed worker must not be reused for a retry or for either successful
  branch. No worker may synthesize the final response itself.

## Expected run artifact shape

The normal top-level Markdown trace is present. `interpretation.md` identifies
all three applications as independent, while `run.md` records their scheduling
and final overall state as Partial.

Each successful branch directory contains prompt, accepted result, and status.
The failed branch contains its exact prompt and terminal status, plus any
preserved failure material required by the runtime contract, but no canonical
accepted `result.md`. There is no automatic retry for this semantic failure.

`final.md` returns the two successful artifacts in order, names the failed
branch and reason, marks the run Partial, explains what actually happened, and
indexes all Markdown artifacts including the failed application records.

## Observable failure signs

- The entire run stops, becomes Failed/Blocked, or discards successful work
  merely because the approval branch failed.
- Approval is inferred, the missing line is fabricated, or refusal text is
  accepted as the requested summary result.
- The runtime automatically retries a deterministic semantic precondition
  failure.
- One worker performs multiple fan-out branches or receives a sibling branch's
  result without a declared dependency.
- `final.md` says Succeeded, hides the failure, omits successful results, or
  links a nonexistent accepted result for the failed application.
- The Markdown state is insufficient for a fresh reader to tell which work
  completed and why the third branch cannot be resumed without changed input.

## Evaluation note

Do not compare the inversion or audit prose to a golden answer. The evaluated
behavior is branch independence, faithful failure semantics, artifact
retention, ordering, and honest partial finalization.
