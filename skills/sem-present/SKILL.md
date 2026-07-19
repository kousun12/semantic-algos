---
name: sem-present
description: "Turn an explicitly named existing Sem run directory into a validated, render-ready view bundle. Use when a user invokes $sem-present, asks to prepare or index a Sem run for display, requests a graph-ready representation of a run, or needs a presentation bundle from an existing sem-runs/... folder; do not use merely to execute a Sem program or build a renderer."
---

# Sem Present

Prepare a disposable presentation projection from one authoritative Sem run.
Do not execute or resume the run, alter its Markdown trace, or render a user
interface.

The emission workflow is intentionally deferred. For the stable producer and
consumer boundary, read [the view-bundle contract](references/view-bundle-contract.md)
completely. Consult [the example manifests](references/example-manifests.md)
only to understand valid representations; they are illustrations, not golden
graph shapes.
