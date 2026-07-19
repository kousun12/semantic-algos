# Evaluation: retries and partial failure

## Purpose

Check that retries, canonical acceptance, branch independence, terminal
failure, and an unlaunched blocked dependent remain distinguishable in one
partial projection.

## Reproducible raw-run setup

Create a fresh Partial run with four application directories:

| Application | Observed outcome |
| --- | --- |
| 001 local `recoverHeading` | attempt 1 mechanically malformed; retry 2 accepted at root `result.md` |
| 002 local `safetyNotice` | independent success |
| 003 semantic critic | terminal semantic failure, no canonical result |
| 004 local synthesis | Blocked and never launched because 003 failed |

Preserve `applications/001-recover-heading/attempts/001-failure.md` and
`002-prompt.md`. Record 001 and 002 as initially independent, 003 as consuming
accepted 001, and 004 as depending on 001 plus 003. Declare return order as 002
then 001. The reference exercise has 20 source files and no initial `view/`.

Invoke a fresh producer with the explicit run root and no expected manifest or
conclusions.

## Material facts to preserve

- Both rejected attempt evidence and the retry prompt remain inspectable.
- Only root `applications/001-recover-heading/result.md` is the accepted 001
  value; the malformed attempt never masquerades as a result.
- Independent 002 remains succeeded, featured, and returned despite the later
  failed branch.
- Application 003 failed without a result and was not retried.
- Application 004 is an independently addressable blocked directory but has no
  accepted value and did not execute.
- Any relationship from failed 003 to blocked 004 is visibly unfulfilled
  control, never produced-value flow.
- Overall status is Partial and returns are `[002, 001]`; all 20 sources are
  inventoried.

## Degrees of freedom

Attempts may be secondary panels, event nodes, a retry group, retry edges, or
a combination. The independent success and blocked dependent may be featured
with any safe emphasis that keeps failure legible. Titles, IDs, summaries,
and optional group spellings are not golden.

## Observable failure signs

- The rejected failure file becomes a result panel or value source.
- The accepted recovery is hidden by retry bookkeeping or shown as two
  application nodes for one directory.
- The failed critic erases or de-emphasizes independent 002 beyond discovery.
- Blocked 004 is shown as succeeded, running, returned, or as having produced a
  value; conversely, its materialized directory is omitted.
- Overall status becomes Succeeded/Failed, or return order is changed.

## Fixed-consumer checks

Using only the bundle and referenced artifacts, a fresh consumer must recover
four applications and their statuses, two recovery attempts with only the
second accepted, the independent successful notice, the critic's terminal
semantic failure, the synthesis's unlaunched blocked state, Partial status,
and result order `[002, 001]`. It must locate all prompts, statuses, accepted
results, attempt files, and run-level documents among 20 unique artifacts.

The consumer must not infer execution of 004 from its prompt or a planned
program edge.

## Forward-test record

### 2026-07-19

- Producer `/root/phase4_implement/producer_retry` emitted and promoted a
  terminal Partial bundle with 20/20 artifacts, four application mappings,
  seven nodes, eight edges, fan-out/retry groups, two returns, and two
  warnings.
- Fresh consumer `/root/phase4_implement/consumer_retry` recovered the rejected
  mechanical attempt, retry prompt, canonical accepted 001 value, independent
  002 success, terminal 003 failure, unlaunched blocked 004, actual versus
  control-only dependencies, `[002, 001]` returns, and all 20 paths.
- Independent verifier `/root/phase4_implement/verifier_retry` initially
  questioned the satisfied 001-to-004 control prerequisite, then reread the
  raw interpretation/program/prompt/status and retracted the finding: 004
  depends on both 001 and 003, the 001 control edge does not imply execution or
  value consumption, and only the failed 003 dependency is unfulfilled.
- The same verifier confirmed that notes correctly retain the historical
  candidate-validation command after successful promotion removes candidates.
  Candidate and canonical validation passed; no change was required.
