# Evaluation: imported program

## Purpose

Check that a successfully executed imported Sem program is projected as an
ordinary run while the absence of compilation artifacts is represented
honestly rather than repaired or treated as corruption.

## Reproducible raw-run setup

Create a fresh successful run whose `program.md` was supplied directly. It
defines one local `weatherLine` application over “rain after midnight” and
returns that accepted result. Include request, program, runtime
interpretation, run log, one application's prompt/result/status, finalizer
prompt, and final report. Deliberately omit both `compiler-prompt.md` and
`compile-notes.md`; record in `interpretation.md` and `run.md` that compilation
did not run.

The reference exercise has nine source files, one application directory, and
no pre-existing `view/`. Invoke a fresh producer using only that root and the
repository `sem-present` skill.

## Material facts to preserve

- Invocation mode was imported; no compiler was invoked.
- The missing compiler prompt and compile notes are intentional absences, not
  source files to synthesize and not a validation error.
- Exactly one local semantic application ran and succeeded.
- Its canonical result is the sole returned artifact.
- The finalizer did run and its two source documents remain ordinary
  reporting evidence, not semantic applications.
- All nine existing source files, and only those files, appear once in the
  artifact inventory.

## Manifest-only structural provenance

Before opening referenced Markdown, the fixed consumer must derive terminal
run state from `run`, the one local application and status from `nodes`, its
accepted flow from `edges`, its sole return from
`presentation.resultNodeIds`, and the presence and absence of source roles
from `artifacts`. The deliberate imported-program interpretation must also be
represented in a manifest warning or node subtitle/summary rather than only in
notes. Markdown may supply the displayed weather text or let an independent
verifier confirm import provenance afterward; it may not be parsed to invent
the application, compiler absence, flow, status, finalizer role, or return.

## Degrees of freedom

The producer may use an informational warning, source-node subtitle/summary,
or another inert manifest base-vocabulary treatment to explain import
provenance; notes may supplement but not replace that manifest fact. It may
attach program and request panels to one source node or leave one in the
complete inventory. No exact warning code or prose is required.

## Observable failure signs

- Invented compiler nodes, artifacts, panels, or source files appear.
- The run is labeled malformed, partial, or unknown solely because compiler
  artifacts are absent.
- Finalizer bookkeeping is mislabeled as a semantic application.
- The local imported operator is mislabeled as repository standard library.
- Existing program/import evidence becomes unreachable or the application is
  not the sole result root.

## Fixed-consumer checks

From only the emitted bundle and referenced artifacts, a fresh consumer must
first reconstruct from manifest fields a Succeeded non-snapshot imported run,
one local application, its
accepted and returned result, deliberate absence of compiler artifacts, and
presence of actual finalizer evidence. It must enumerate exactly nine unique
source paths and must not need to parse the imported program to discover the
application or return.

Import explanation wording is free; the represented absence and actual
application identity are not.

## Forward-test record

### 2026-07-19

- Producer `/root/phase4_implement/producer_imported` emitted and promoted a
  succeeded non-snapshot bundle with 9/9 artifacts, one application mapping,
  three nodes, two edges, one return, and one import-provenance warning.
- Fresh consumer `/root/phase4_implement/consumer_imported` recovered direct
  import, deliberate compiler-artifact absence, the local `weatherLine`
  application and result, actual finalizer evidence, sole return, and all nine
  paths.
- Independent verifier `/root/phase4_implement/verifier_imported` confirmed the
  exact inventory, deliberate absences, mapping/operator/status, value flow,
  return, and finalization. Its only caveat was the intentionally transient
  candidate named by notes; canonical validation independently passed.
- No compiler/finalizer stage was invented and no reusable correction was
  needed.
