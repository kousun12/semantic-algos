# Evaluation: single local application

## Purpose

Check that a fresh presentation agent turns the smallest successful local run
into an easy traversal without inventing semantic stages or forcing a
redundant application/value graph.

## Reproducible raw-run setup

Create a fresh run root outside the repository with the ordinary compiled-run
documents, one directory `applications/001-incident-brief/`, and no `view/`.
Use a request that asks a complete local `incidentBrief` operator to preserve
the facts “Beacon 7”, “failed at dawn”, and “the backup lamp held” in exactly
two sentences. Record one accepted result and an overall Succeeded status;
declare that application as the only return.

The reference exercise uses 11 source files: request, compiler prompt,
program, compile notes, interpretation, run log, the application's prompt,
result, and status, plus finalizer prompt and final report.

Invoke a fresh producer with only:

```text
Use $sem-present from this repository on the one explicit fresh run path
supplied by the evaluation harness.
```

## Material facts to preserve

- The original request is reachable as source evidence.
- Exactly one semantic application ran: local `incidentBrief`.
- Its canonical `result.md` is the accepted value and includes the three
  requested incident facts in two sentences.
- The run and application both succeeded.
- The application is the sole returned result; `final.md` is reporting
  evidence, not another semantic result.
- Every one of the 11 source files remains reachable from the artifact
  inventory, including prompt, status, accepted result, and run-level files.

## Degrees of freedom

The producer may choose titles, summaries, IDs, optional source/stage nodes,
panel order, and whether the application node itself doubles as the result.
It need not create an explicit result node. No graph layout, prose, or node ID
is golden.

## Observable failure signs

- The local operator is mislabeled as standard library or semantic judgment.
- Compiler or finalizer bookkeeping appears as an application.
- The result is duplicated into manifest prose or an unnecessary value node
  obscures the only application.
- `final.md` replaces the canonical application result as the accepted value.
- Any source artifact is omitted or the sole result root is missing.

## Fixed-consumer checks

Give a separate fresh consumer only the emitted `view/` bundle and the
artifact paths referenced by it. Without parsing the Sem program, it must be
able to:

1. list one application directory and identify it as local;
2. open its prompt, status, and canonical accepted result;
3. recover the request facts and the two-sentence result;
4. report Succeeded and exactly one returned result;
5. enumerate all 11 source artifacts with no duplicate path.

The consumer may render any valid optional grouping or node titles. Its answer
is compared to the raw files above, not to a golden manifest spelling.

## Forward-test record

### 2026-07-19

- Producer `/root/phase4_implement/producer_single` emitted and promoted a
  succeeded, non-snapshot bundle with 11/11 artifacts, one application
  mapping, two nodes, one edge, no groups, one result, and no warnings.
- Fresh consumer `/root/phase4_implement/consumer_single` recovered the exact
  request facts, one local application, canonical result, one-attempt status,
  value flow, terminal status, sole return, and all 11 paths without expected
  answers or evaluation context.
- Independent verifier `/root/phase4_implement/verifier_single` compared the
  bundle with the raw trace: exact path set, mapping, operator, status, value,
  return, and panel reachability all matched.
- Candidate and canonical validation passed. No skill correction was needed;
  the exercised `view/` remained outside the repository.
