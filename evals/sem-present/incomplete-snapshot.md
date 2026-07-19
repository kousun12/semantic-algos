# Evaluation: incomplete snapshot

## Purpose

Check that a stable observation of a non-terminal run can be rendered without
fabricated accepted values, returns, finalizer stages, or claims of live
synchronization.

## Reproducible raw-run setup

Create a quiescent raw run whose source says Overall status: Running and whose
three application directories contain:

| Application | Snapshot state |
| --- | --- |
| 001 local `extractFact` | Succeeded with canonical result |
| 002 local `draftBulletin` | Running with prompt/status and no result |
| 003 local `reviewBulletin` | Pending, not launched, waiting for 002 |

The program declares 003 as the eventual return, but finalization has not
started. Record all three operator identities and their `local` kind in the
raw trace rather than relying on directory slugs or evaluator expectations.
Deliberately omit `finalizer-prompt.md` and `final.md`. The reference exercise
contains 13 source files. Keep source paths, types, sizes, and modification
times stable during generation and start with no `view/`.

Invoke a fresh producer with only this explicit root and the repository skill.

## Material facts to preserve

- Overall status is Running and `run.snapshot` is true at `generatedAt`.
- All three local operator names and kinds remain recoverable from the bundle.
- Application 001 has an accepted result; application 002 does not.
- Application 003 is pending/unlaunched and has no produced-value edge from
  002; a planned dependency may appear only as unfulfilled control.
- The program's eventual return declaration does not create a current returned
  result. `presentation.resultNodeIds` is empty.
- No finalizer or final artifact/node is invented.
- Notes and warnings explicitly say the projection is a stale-able
  timestamped snapshot that must be regenerated after source changes.
- All three applications and all 13 source files remain inspectable.

## Manifest-only structural provenance

Before opening referenced Markdown, the fixed consumer must derive
Running/`snapshot: true` from `run`; all three local mappings, operators, and
statuses from `nodes`; accepted versus unfulfilled relationships from `edges`;
the empty current return from `presentation.resultNodeIds`; and the exact
artifact/finalizer absence from `artifacts`. Warnings and notes may carry the
regeneration caveat. Markdown may provide displayed result/status prose or be
used by an independent verifier after reconstruction, but it may not fill in
operators, statuses, applications, flow, return state, or absent finalization.

## Degrees of freedom

The producer may feature the completed, running, and pending nodes together or
focus the running frontier. It may show planned dependency with a labeled
control edge or only status/panel evidence. Titles, warning code, summary
prose, and optional source/stage nodes are not golden.

## Observable failure signs

- `snapshot` is false, terminal status is invented, or staleness/regeneration
  is not explicit.
- Missing 002/003 results are fabricated from prompts or program intent.
- Recoverable operator metadata is omitted, forcing a consumer to infer names
  or kinds from directory spellings or program intent.
- The eventual review is listed as a current returned result.
- A finalizer/final node or artifact is invented.
- Pending 003 looks executed or receives a value edge from still-running 002.
- The producer reads a torn source state rather than refusing promotion.

## Fixed-consumer checks

Give a fresh consumer only the canonical bundle and its referenced artifacts.
From manifest fields before artifact reads, it must recover Running/snapshot,
the three local operator identities, the
statuses Succeeded/Running/Pending, accepted value only for 001, no current
returns, no finalizer artifacts, and the regeneration caveat. It must
enumerate all 13 source artifacts and locate each application prompt/status
plus the one accepted result.

The consumer is not asked to predict the eventual result or parse `program.md`
to fill absent state.

## Forward-test record

### 2026-07-19

- Producer `/root/phase4_implement/producer_snapshot` emitted and promoted a
  Running snapshot with 13/13 artifacts, three application mappings, four
  nodes, three edges, no groups/results, and two snapshot warnings after
  confirming source identity/size/time stability.
- Fresh consumer `/root/phase4_implement/consumer_snapshot` recovered
  Succeeded/Running/Pending states, accepted value only for 001, actual value
  flow through 002, unfulfilled control to unlaunched 003, no current return,
  no finalizer artifacts, and the regeneration caveat.
- Independent verifier `/root/phase4_implement/verifier_snapshot` confirmed
  exact inventory/mappings, statuses, flow, deliberate absences, warnings, and
  notes. The transient candidate command in notes is expected promotion
  provenance, not a retained artifact reference.
- Candidate and canonical validation passed. No skill correction was needed;
  the run remained temporary.
- Phase reviewer `/root/phase4_review` found that the initial raw trace named
  the applications but did not establish their operator kinds, so the producer
  correctly omitted `application.operator`. The reviewer tightened the setup
  to record local kinds explicitly and regenerated from a clean copy.
- Fresh producer `/root/phase4_review/snapshot_corrected_forward` emitted a
  stable Running snapshot with 13/13 artifacts, three complete application
  mappings, four nodes, three edges, no groups or current returns, and two
  snapshot/return warnings. Candidate and canonical validation passed, and the
  source identity/size/time snapshot remained stable through promotion.
- Fresh fixed consumer `/root/phase4_review/snapshot_consumer_recheck`
  recovered all three local operators, Succeeded/Running/Pending statuses,
  accepted value only for 001, unfulfilled control to unlaunched 003, no
  current return or finalizer, all 13 paths, and the explicit regeneration
  requirement without using program intent to repair graph structure.
