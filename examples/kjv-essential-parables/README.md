# KJV Essential Structure: Twelve Parables

This is a complete historical `sem-run`, copied from
`sem-runs/kjv-essential-parables/2026-08-01-1234`. It shows how a natural-language
request becomes a compiled Sem program, an inspectable execution graph, 39
materialized applications, and a linked final result.

## Start here

Open [`run/final.md`](run/final.md) to read the returned outline and twelve parables.
From there, follow any standalone-result link into the application that
produced it.

For a guided tour of the machinery:

1. [`run/request.md`](run/request.md) preserves the exact request and its provenance.
2. [`run/program.md`](run/program.md) is the compiled Haskell-esque Sem program;
   [`run/compile-notes.md`](run/compile-notes.md) records the compiler's decisions.
3. [`run/interpretation.md`](run/interpretation.md) turns the program into an execution
   plan, while [`run/run.md`](run/run.md) records what actually happened.
4. One representative leaf passes through a local heart-question adapter,
   [`question-forge`](run/applications/005-leaf-1-1-forge/result.md), and
   [`parable`](run/applications/006-leaf-1-1-parable/result.md). Each application
   directory also retains its prompt and status.
5. The first outline exceeded the twelve-leaf cap. Its
   [recorded failure](run/applications/003-build-major-minor-outline/attempts/001-failure.md)
   and [retry prompt](run/applications/003-build-major-minor-outline/attempts/002-prompt.md)
   show how a recoverable validation failure stays visible in the trace.
6. [`run/finalizer-prompt.md`](run/finalizer-prompt.md) and [`run/final.md`](run/final.md) show the
   final projection from application results into the returned artifact.

## Optional view layer

This run was subsequently passed to `sem-present`. The authoritative record is
still the Markdown trace above; the files under `run/view/` are a disposable,
regenerable presentation projection:

- [`run/view/notes.md`](run/view/notes.md) explains the reconstructed graph,
  reconciliation decisions, inventory, and validation result.
- [`run/view/manifest.json`](run/view/manifest.json) is the validated machine-readable
  graph and panel manifest for a future renderer. Its artifact paths are
  relative to the `run/` root, so they remain navigable in this copy.

The run intentionally preserves timestamps and original host paths as
historical provenance. Those absolute paths describe where the run was created;
they are not required to browse the copied example.
