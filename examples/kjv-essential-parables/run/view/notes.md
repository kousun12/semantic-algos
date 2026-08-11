# Sem-present candidate notes

- Supplied run path: `/Users/rob/code/semantic-algos/sem-runs/kjv-essential-parables/2026-08-01-1234` (the uniquely identified prior Sem result referenced by the invocation)
- Resolved run path: `/Users/rob/code/semantic-algos/sem-runs/kjv-essential-parables/2026-08-01-1234`
- Observed status: `succeeded`
- Snapshot: `false`
- Generated at: `2026-08-01T13:16:41-04:00`
- Generation ID: `20260801T131641-b85f5df9`

## Graph shape

The projection contains one source node, interpretation and finalization stages, all 39 materialized applications as independent application nodes, one rejected-attempt event, and one structural result node for the returned twelve-parable collection. The graph exposes accepted value flow, the outline retry, and the three-part returned order without duplicating every artifact as a node.

The twelve dynamic leaf chains are grouped both as one ordered map and as twelve nested phase groups. Every leaf retains three independently addressable applications: heart-question adapter, `question-forge`, and `parable`.

## Evidence reconciliation

Canonical application results and status files establish that all 39 applications succeeded. The run log briefly records a provisional acceptance of outline application 003 before exact-count validation; the preserved rejected attempt, corrected status, canonical root result, and later run-log entries establish that the 13-leaf first attempt was rejected and the 12-leaf retry was accepted. The projection therefore represents the first output as a failed retry event and only the canonical root `result.md` as the application value.

No other consequential source disagreement was found. The finalizer summary agrees with the accepted result/status evidence.

## Presentation judgments

The declared return order comes from `program.md`, `compile-notes.md`, and `interpretation.md`: deterministic draw receipt, major.minor outline, then the structural `leafResults` collection. Accordingly, `presentation.resultNodeIds` is `app-001`, `app-003`, and `result-parable-cycle`. The collection node exposes the twelve canonical parable results in terminal-leaf number order.

The craft blend, heart questions, and forge reports are initially hidden because the runtime explicitly hides those intermediates. They remain fully addressable with prompt, result, and status panels. Parable applications are ordinary visible nodes; the draw, outline, and collection are primary.

## Inventory and limitations

- Authoritative source artifacts outside `view/`: 127
- Materialized application directories: 39
- Known noise excluded: `.DS_Store`
- Missing source artifacts: None
- Unknown or unsupported source artifacts: None
- Unsafe, broken, special, or escaping entries: None
- External Bible text was not retrieved by the source run; the view reports the recorded run and does not add facts.
- The bundle is a presentation projection only. It did not compile, execute, resume, finalize, or render the Sem run.
- Filesystem isolation is cooperative and path-validated; it is not a host-level security boundary.

## Validation

Command:

```text
python3 /Users/rob/.codex/skills/semantic-algos/skills/sem-present/scripts/validate_view.py /Users/rob/code/semantic-algos/sem-runs/kjv-essential-parables/2026-08-01-1234 view/manifest.20260801T131641-b85f5df9.next.json
```

Outcome: Success — `valid: view/manifest.20260801T131641-b85f5df9.next.json` (exit code 0).

## Snapshot and regeneration

This is a terminal, quiescent run, so the bundle is not a snapshot. Regeneration must still reconstruct from the authoritative source trace and replace the complete projection; consumers must not treat this view as runtime or resume state.
