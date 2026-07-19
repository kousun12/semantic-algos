# Sem Present: a render-ready projection for Sem runs

## Overview

Add a third Sem boundary, `skills/sem-present/`, that turns one existing
`sem-runs/<title>/<timestamp>/` directory into a render-ready view bundle.
`sem-present` runs after `sem-run`; it does not compile a program, execute an
application, finalize a result, or render a user interface.

The runtime remains Markdown-native and squishy. Its files are the durable
source of truth. The presentation skill reads the whole run after the fact,
interprets what actually happened, and writes a small additive projection at a
stable location:

```text
request -> sem-compile -> program -> sem-run -> Markdown trace
                                             -> sem-present -> view bundle
                                                            -> future UI
```

The future UI is deliberately outside this plan. Its contract is simply: given
a run directory, open `view/manifest.json`, validate the supported major
version, and render the referenced run-local artifacts using a fixed set of
graph, node-panel, Markdown, code, status, and fallback components.

The design keeps rigidity at the consumer boundary rather than pushing it back
into Sem. A capable presentation agent may decide that a construct is best
shown as a fan-out, an iteration group, a hidden intermediate, a retry, or a
single compound step. Once it makes that decision, it must encode it using the
stable manifest vocabulary, account for every runtime artifact, and pass a
deterministic validator.

This plan assumes [the Sem runtime plan](sem-run-runtime.md) is implemented and
that its run-directory contract is available to `sem-present`.

## Boundary and ownership

### Source of truth

The existing run directory is authoritative:

- `request.md`, `program.md`, and `compile-notes.md` describe intent and
  compilation;
- `interpretation.md` describes the runner's initial reading and later
  amendments;
- `run.md`, application statuses, attempts, and accepted results describe what
  actually happened;
- `final.md`, when present, describes returned artifacts and their order.

The view bundle is a disposable projection. It may be deleted and regenerated
without changing the meaning, resumability, or audit history of the run.
Neither `sem-run` nor a resumed application may consume it as runtime state.

When sources disagree, `sem-present` represents actual execution rather than
the idealized program:

1. accepted result and attempt files;
2. application status files and the append-only run log;
3. runtime interpretation and amendments;
4. compile notes and program intent;
5. the finalizer's prose summary.

Record any consequential reconciliation in `view/notes.md` rather than hiding
it in a label or silently repairing the source trace.

### Input

Require an explicit run-directory path. Accept successful, partial, failed,
blocked, and quiescent in-progress runs. For an in-progress run, describe the
bundle as a timestamped snapshot and expect callers to regenerate it after the
run changes.

Do not search for a vaguely described “latest” run. Do not accept the enclosing
`sem-runs/` directory or write outside the explicitly named run.

### Output

Write only:

```text
sem-runs/<title>/<timestamp>/
  ...authoritative Markdown trace...
  view/
    manifest.json
    notes.md
```

`manifest.json` is the deterministic machine entry point. `notes.md` is the
squishy explanation surface: reconstruction choices, ambiguities, unsupported
files, source disagreements, validation outcome, and snapshot caveats.

Version 1 should not generate duplicate excerpts or rewritten result files.
Node panels reference the existing Markdown artifacts and, where useful, a
named Markdown section such as `Result`. Large content therefore stays lazy:
the manifest scales with the graph, not with the size of every result.

### Non-responsibilities

`sem-present` does not:

- alter, normalize, or “fix” runtime Markdown;
- invent an application that did not run or a result that was not produced;
- decide Sem scheduling or resume behavior;
- become a canonical program IR, scheduler state, or replacement for
  `interpretation.md`;
- render HTML, React, CSS, SVG, canvas coordinates, or graph-library options;
- emit executable JavaScript, arbitrary component names, inline HTML, or other
  renderer instructions;
- browse, message, or perform external effects;
- require the same labels, grouping, or summaries from two independent
  presentation agents, as long as both valid bundles faithfully represent the
  same run.

## Product decisions

### `sem-present` is a view compiler, not a renderer

The skill performs semantic reconstruction that a static file walker cannot do
reliably: deciding which apparent steps are structural, matching dynamic
applications to their parent construct, identifying real value-flow edges,
distinguishing returned results from merely visible artifacts, and choosing
helpful group names and emphasis.

The renderer performs no such reconstruction. It follows a validated bundle.
This is the central boundary:

```text
squishy input trace -> agent judgment -> stable view vocabulary -> fixed UI
```

### The runtime's no-JSON rule ends at the projection boundary

`sem-run` must continue to produce Markdown only. `sem-present` deliberately
adds JSON because a future UI needs a predictable, cheaply validated entry
point. This does not contradict the runtime design: the JSON is downstream,
rebuildable, non-authoritative, and never used to execute or resume Sem.

### Stabilize the envelope, not the ontology

The manifest has a small required core:

- run metadata and status;
- a complete artifact inventory;
- display nodes;
- directed relationships;
- optional semantic groups;
- entry, featured, and returned-result node IDs;
- node panels that say which artifact or Markdown section to render;
- warnings and extension data.

The agent retains freedom over titles, summaries, group boundaries, optional
nodes, and presentation emphasis. The manifest permits namespaced extensions
and unknown optional fields. A consumer ignores fields it does not understand
and uses safe fallbacks for unknown optional types.

### Represent actual applications individually

Every runtime application directory receives an independently addressable
display node, including dynamically generated map items, repeat rounds,
semantic predicates, selectors, judges, synthesizers, failed calls, and
blocked calls. Groups may visually collect these nodes but may not replace or
hide their independent identity.

Retries remain inspectable. The default node can show the accepted result and
current status while attempt prompts and failures appear as secondary panels
or retry/event nodes. Rejected attempts never masquerade as accepted values.

### Keep value flow distinct from file ownership

An edge says how steps relate semantically or operationally; an artifact record
says where inspectable content lives. Do not infer graph edges merely because
one Markdown file links another.

Version 1 uses a small edge vocabulary:

- `value`: a produced semantic value became a declared input;
- `control`: one runtime stage enabled or scheduled another;
- `return`: a step or value was selected as a returned result;
- `contains`: a group owns or organizes members;
- `retry`: an attempt superseded or retried another attempt;
- `provenance`: a document or decision explains another node without carrying
  its semantic value.

Optional `subtype` and `label` fields can preserve local meaning. Unknown edge
subtypes use the base type's rendering.

### Make the graph useful before it is exhaustive on screen

The bundle must account for the entire run, but it can identify a smaller
default focus. A future UI should initially frame `featuredNodeIds` and
`resultNodeIds`, then let the user reveal groups, prompts, statuses, attempts,
compiler material, and the complete artifact inventory.

Do not encode pixels, coordinates, colors, or library-specific layout. Supply
only semantic hints such as ordered group membership, an ordinal, and a
`primary`, `normal`, `context`, or `hidden` emphasis. The renderer owns layout
and visual accessibility.

### Markdown remains the universal content fallback

Every node exposes one or more panels. A panel chooses an artifact, an optional
stable section selector, and one of these initial render modes:

- `markdown`;
- `code`;
- `plain-text`;
- `metadata`;
- `download`.

These modes name fixed consumer components, not arbitrary renderers. If a
selector or render mode is unsupported, the UI renders the complete artifact
as sanitized Markdown or plain text and keeps a direct file link.

The initial selector vocabulary is deliberately small:

- `whole`;
- `markdown-heading`, with heading text and optional occurrence.

Do not use line ranges: they become stale as the authoritative trace evolves.

### Partial and irregular runs are first-class

A bundle does not require `final.md` or a successful status. Missing expected
files become warnings or explicit failed/blocked nodes when the trace supports
that reading. A missing canonical runtime file that prevents faithful
reconstruction is a validation failure, not an invitation to fabricate it.

The result list may be empty. A partial run may feature the successful branch,
failed application, and blocked dependents together. A snapshot of an active
run records `generatedAt` and the observed overall status in both the manifest
and notes.

### Keep the consumer boundary safe

All artifact paths are POSIX-style, relative to the run root, and contain no
`..`, absolute prefix, URL scheme, or symlink escape. The validator resolves
each path and confirms it remains inside the explicit run directory.

The renderer treats all labels, summaries, Markdown, programs, prompts, and
results as untrusted content. It sanitizes Markdown, disallows executable HTML,
does not follow external links automatically, and never interprets manifest
data as code or authority.

## View bundle contract

### Deterministic entry point

A consumer pointed at a run performs only these discovery steps:

1. open `<run>/view/manifest.json`;
2. require `kind: "sem-run-view"`;
3. accept a supported `schemaVersion` major;
4. resolve every referenced artifact relative to `<run>/`;
5. render the graph and panels using the base types below;
6. fall back to links and sanitized Markdown for optional data it does not
   understand.

It does not scrape `interpretation.md`, parse a Sem program, or ask a model to
understand the trace.

### Manifest shape

The exact schema belongs in
`skills/sem-present/references/manifest-v1.schema.json`. Its conceptual shape
is:

```json
{
  "kind": "sem-run-view",
  "schemaVersion": "1.0",
  "generatedAt": "2026-07-19T15:30:00Z",
  "run": {
    "title": "What kids owe their parents — aporia",
    "status": "succeeded",
    "snapshot": false
  },
  "artifacts": [],
  "nodes": [],
  "edges": [],
  "groups": [],
  "presentation": {
    "entryNodeIds": [],
    "featuredNodeIds": [],
    "resultNodeIds": []
  },
  "warnings": [],
  "extensions": {}
}
```

Versioning rules:

- the major version changes when a valid old consumer cannot render the new
  required core;
- minor additions are optional and safely ignorable;
- `kind`, `schemaVersion`, base node/edge/group types, artifact paths, node
  IDs, edge endpoints, and presentation IDs are validated deterministically;
- free prose, summaries, labels, warnings, and namespaced extensions are not
  semantically validated.

### Artifacts

Every non-hidden regular source file under the run root, excluding `view/`,
appears exactly once in `artifacts`. Ignore known filesystem noise such as
`.DS_Store` and mention unexpected hidden files in `view/notes.md`.

Each artifact has:

- unique `id`;
- safe run-relative `path`;
- detected `mediaType`;
- base `role`, such as `request`, `program`, `compile-notes`,
  `interpretation`, `run-log`, `input`, `application-prompt`,
  `application-result`, `application-status`, `attempt`, `finalizer-prompt`,
  `final`, or `other`;
- human title;
- optional owner node ID and short description.

Unknown files use `role: "other"` and remain downloadable. The renderer never
drops a source artifact solely because it lacks a preferred role.

### Nodes

Each node has:

- unique stable-within-bundle `id`;
- base `type`: `source`, `stage`, `application`, `result`, `group`, `event`, or
  `note`;
- title and optional subtitle/summary;
- optional normalized status: `unknown`, `pending`, `ready`, `running`,
  `succeeded`, `failed`, `blocked`, or `partial`;
- emphasis: `primary`, `normal`, `context`, or `hidden`;
- optional ordinal and group IDs;
- zero or more panels;
- optional base-type-specific data such as operator identity.

An application node additionally identifies its operator as `standard-library`,
`local`, or `semantic-judgment`, when recoverable, and records the runtime
application directory. Do not require a formal Sem function signature.

Each runtime application directory maps to exactly one application node. A
separate result node is optional: use one when a structural return, collection,
or final document deserves its own navigable identity. Otherwise the
application node may itself appear in `resultNodeIds` and show its accepted
`result.md` as the primary panel.

This avoids forcing every run into a noisy bipartite application/value graph
while still allowing a presentation agent to introduce explicit value nodes
where they improve the display.

### Panels

A panel has:

- stable-within-node `id` and label;
- `artifactId`;
- `role`: `primary`, `result`, `prompt`, `status`, `source`, `explanation`,
  `attempt`, or `other`;
- `renderAs` from the fixed modes above;
- optional `selector`;
- optional order and default-open flag.

Every node remains useful if only its panels and artifact links are rendered.
Summaries are navigational aids, not substitutes for source content.

### Edges

Each edge has a unique ID, existing `from` and `to` node IDs, one base type,
and optional label, subtype, and order. Encode observed value flow from actual
accepted results. Encode planned but blocked dependencies only when their
status is clear, and label them as unfulfilled rather than visually implying a
produced value.

The materialized application graph should normally be acyclic even when the
source program used `repeat`: rounds become distinct nodes ordered within an
iteration group. Retry edges may point from a failed attempt/event toward the
later attempt or canonical application without creating a semantic value
cycle.

### Groups

Groups are optional semantic containers with:

- unique ID and title;
- base type: `fan-out`, `map`, `iteration`, `choice`, `retry`, `phase`, or
  `other`;
- ordered member node IDs;
- optional parent group ID, summary, and collapsed-by-default hint.

Groups do not erase member nodes. If the runtime interpretation and actual
application inventory disagree about a dynamic expansion, represent the
materialized applications and explain the disagreement in notes.

### Presentation roots

`presentation.entryNodeIds` identifies where a user can begin following the
semantic story. `featuredNodeIds` defines the initial camera/focus set without
hiding anything. `resultNodeIds` contains the returned artifacts in requested
presentation order, not execution or filesystem order.

Every referenced ID must exist. A successful run must have at least one result
node. A partial, blocked, failed, or in-progress run may have none when the
trace contains no returned artifact.

### Notes

`view/notes.md` contains:

1. source run path, observed status, and generation time;
2. a concise explanation of the chosen graph shape;
3. source disagreements and how precedence was applied;
4. grouping, result-order, or visibility judgments that were not mechanical;
5. missing, unrecognized, or unsupported artifacts;
6. validation command and outcome;
7. explicit snapshot warning for non-terminal runs.

Do not put private chain-of-thought in notes. Record decisions and evidence at
the level needed to audit or regenerate the projection.

## Emission workflow

`sem-present` follows this procedure:

1. Resolve and validate the explicit run root. Refuse broad, missing, or
   escaping paths.
2. Inventory all run-local files except `view/` and known filesystem noise.
3. Read the runtime contract, then read the run's request, program, notes,
   interpretation, run log, application statuses/results/prompts, attempts,
   inputs, finalizer prompt, and final result when they exist.
4. Reconstruct observed applications, declared inputs, actual accepted values,
   dynamic groups, retries, statuses, visibility, and returned order using the
   precedence rules above.
5. Choose the smallest useful display graph. Include every application and
   every artifact, but avoid redundant nodes when a panel or artifact link is
   clearer.
6. Write candidates as `view/manifest.next.json` and `view/notes.next.md`.
   Existing authoritative trace files are read-only.
7. Run the bundled validator. Repair structural errors without changing source
   artifacts. Limit semantic remapping to one deliberate reread rather than
   repeatedly guessing until validation happens to pass.
8. Only after validation succeeds, replace the canonical generated
   `view/manifest.json` and `view/notes.md`. Do not remove unrecognized files in
   `view/`. If validation fails, preserve any prior valid canonical bundle and
   report the candidate failure.
9. Report the run path, manifest path, observed status, node/application/result
   counts, warnings, and validation success.

`sem-present` is intentionally a whole-run, wide-context skill. It does not
spawn one worker per semantic application because it is not executing those
applications; it is reconstructing their relationships. It may itself be run
in a fresh subagent by a caller that wants the projection isolated from other
conversation.

## Validator contract

Include a dependency-free Python validator at
`skills/sem-present/scripts/validate_view.py`. It receives the run root, finds
`view/manifest.json` by default, and optionally accepts a candidate manifest
path during generation.

It validates only deterministic properties:

- valid JSON and supported schema version;
- required fields and allowed base enums;
- unique artifact, node, edge, group, and panel IDs;
- existing edge endpoints, group members, panel artifacts, owner nodes, and
  presentation roots;
- exactly one inventory record per non-hidden source file outside `view/`;
- every referenced path is relative, normalized, non-escaping, inside the run,
  and an existing regular file;
- every application directory has exactly one application node and its
  prompt/status/result/attempt files are inventoried when present;
- accepted-result panels point at canonical accepted results rather than
  rejected attempt files;
- group-parent relationships are non-cyclic;
- a successful run exposes at least one result node;
- `view/notes.md` exists for a canonical bundle.

The validator does not decide whether a summary is eloquent, an edge is the
best interpretation of ambiguous prose, or a group deserves a particular
name. Those remain skill behavior and evaluation concerns.

Exit nonzero with concise, path-specific diagnostics. Support a machine-readable
diagnostic mode only if it is useful during implementation; the render bundle
itself must not depend on validator output.

## Proposed repository structure

```text
skills/
  sem-present/
    SKILL.md
    agents/
      openai.yaml
    references/
      emission-protocol.md
      view-bundle-contract.md
      manifest-v1.schema.json
      example-manifests.md
    scripts/
      validate_view.py
tests/
  sem_present/
    test_validate_view.py
    fixtures/
      minimal-success/
      partial-fan-out/
      invalid-escaping-path/
evals/
  sem-present/
    single-local-application.md
    fan-out-hidden-intermediate.md
    dynamic-map-and-iteration.md
    retries-and-partial-failure.md
    imported-program.md
    incomplete-snapshot.md
```

The schema and examples explain the stable producer/consumer boundary. The
Python tests cover mechanical validation. The Markdown evaluations test the
presentation agent's semantic reconstruction without prescribing one golden
graph or one wording.

## Skill metadata target

Generate the final values from the completed skill. Initial targets are:

```yaml
# skills/sem-present/agents/openai.yaml
interface:
  display_name: "Sem Present"
  short_description: "Prepare Sem runs for graph-based display"
  default_prompt: "Use $sem-present to turn this Sem run directory into a validated render-ready view bundle."
```

The skill should trigger when a user invokes `$sem-present`, asks to prepare or
index a Sem run for display, requests a graph-ready representation of a run, or
needs a validated presentation bundle from an existing `sem-runs/...` folder.
It must not trigger merely because a user asks to execute a Sem program or
build the eventual React renderer.

## Evaluation strategy

### Mechanical contract tests

Use compact fixtures to cover:

- a minimal successful run with one local application;
- multiple applications and ordered returns;
- safe Markdown and text input paths;
- unknown files represented as `other`;
- missing artifacts and duplicate IDs;
- edge, group, panel, owner, and presentation references to missing IDs;
- absolute, parent-traversing, URL-like, and symlink-escaping paths;
- missing application nodes or duplicate mappings for one application
  directory;
- a successful run with no result root;
- partial and active runs with an empty result list;
- cyclic nested groups;
- canonical versus rejected attempt results.

Tests should assert concise diagnostic locations as well as success/failure.

### Squishy reconstruction evaluations

Each `evals/sem-present/*.md` case contains:

- a run shape or command for producing it;
- material facts the view must preserve;
- degrees of freedom the presentation agent may choose;
- observable failure signs;
- consumer checks that use only the emitted bundle and source artifacts.

The cases cover:

1. **Single local application:** the request, local operator, accepted result,
   and final result are easy to traverse without redundant graph clutter.
2. **Fan-out with a hidden intermediate:** shared upstream work appears once,
   branches are independent, hidden does not mean missing, and result ordering
   differs safely from execution order.
3. **Dynamic map and iteration:** every materialized call is independent,
   ordered groups explain the expansion, and no source-level loop becomes an
   opaque single node.
4. **Retries and partial failure:** rejected attempts remain inspectable,
   accepted values are unambiguous, independent success remains featured, and
   blocked dependents do not look executed.
5. **Imported program:** absence of compiler artifacts is represented honestly
   rather than treated as a malformed compiled run.
6. **Incomplete snapshot:** an active run can be rendered without fabricating
   final nodes and clearly advertises staleness/regeneration expectations.

Forward-test the skill in fresh contexts against completed and partial runs.
Give the evaluator only the run root and the emitted view bundle. Ask it to
recover:

- what the original request was;
- which semantic applications actually ran;
- how accepted values flowed;
- which calls were parallel, repeated, retried, failed, or blocked;
- which artifacts were returned and in what order;
- where to open every prompt, result, status, and run-level document.

Agreement on those facts matters. Agreement on exact node titles, summaries,
or whether an optional stage deserves its own node does not.

## Phases

| Phase | Name | Depends on | Parallelizable with |
| --- | --- | --- | --- |
| 1 | Establish the view-bundle contract | none | none |
| 2 | Build the deterministic validator | Phase 1 | none |
| 3 | Implement `sem-present` | Phase 2 | none |
| 4 | Evaluate reconstruction across run shapes | Phase 3 | none |
| 5 | Document the producer/consumer handoff | Phase 4 | none |

## Phase 1: Establish the view-bundle contract

- **Status:** Done
- **Depends on:** none
- **Objective:** Define the smallest stable projection that lets a fixed UI
  render any Sem run without parsing Sem or semantically interpreting Markdown.
- **Scope:** initialize `skills/sem-present/`; create
  `references/view-bundle-contract.md`,
  `references/manifest-v1.schema.json`, and
  `references/example-manifests.md`; generate initial `agents/openai.yaml`.
- **Out of scope:** skill execution workflow, validator implementation, React,
  graph layout, changes to `sem-run`, or runtime JSON.
- **Approach:** Initialize the skill in this repository with `references/` and
  `scripts/` support, but keep `SKILL.md` minimal until the contract is stable.
  Specify the projection/source-of-truth boundary, path base, versioning,
  artifact inventory, nodes, panels, edges, groups, presentation roots,
  statuses, fallbacks, and security rules. Include compact examples for a
  one-application success, fan-out with ordered returns, and partial failure.
  Examples illustrate valid alternatives rather than becoming golden output.
- **Acceptance criteria:**
  - A consumer can find one entry point at `view/manifest.json` from only the
    run root.
  - The schema requires enough information to render a graph, node detail
    panels, ordered results, statuses, groups, and complete artifact links.
  - Every runtime application remains independently addressable.
  - Application nodes may double as result nodes; explicit value/result nodes
    remain possible where useful.
  - The contract supports dynamic applications, hidden intermediates, retries,
    partial failures, imported programs, and active snapshots.
  - Existing Markdown remains authoritative and substantive result content is
    referenced rather than duplicated.
  - The manifest contains no coordinates, React concepts, executable content,
    arbitrary renderer names, or Sem execution state.
  - Versioning and unknown-field/type fallbacks are explicit.
- **Validation:**
  - Manually walk each example using the deterministic consumer discovery
    steps and confirm no semantic inference is required.
  - Compare every example application and artifact with its source fixture.
  - Validate the schema file as JSON with `python3 -m json.tool`.
  - Run the external standard skill validator against the initialized skill.
  - Run `git diff --check`.

## Phase 2: Build the deterministic validator

- **Status:** Done
- **Depends on:** Phase 1
- **Objective:** Make structural correctness, path safety, application
  coverage, and artifact coverage mechanically enforceable without judging the
  agent's semantic presentation choices.
- **Scope:** `skills/sem-present/scripts/validate_view.py`,
  `tests/sem_present/test_validate_view.py`, and compact fixtures under
  `tests/sem_present/fixtures/`; bounded corrections to the v1 contract/schema
  exposed by testability.
- **Out of scope:** generating manifests, parsing Sem programs, assigning
  semantic edges, frontend rendering, or validating prose quality.
- **Approach:** Implement a Python-standard-library validator with clear
  diagnostics and no dependency on the eventual UI. Validate JSON structure,
  safe resolved paths, IDs/references, source inventory coverage, one display
  application per runtime application directory, accepted versus rejected
  result use, group nesting, status/result consistency, and notes presence.
  Keep semantic labels, summaries, and ambiguous grouping outside the
  validator.
- **Acceptance criteria:**
  - The validator accepts every valid reference example and fixture.
  - It rejects every path escape before a consumer could open the target.
  - It catches missing and duplicate application coverage even when graph
    references are otherwise valid.
  - It catches omitted source artifacts and dangling graph/panel/presentation
    references with the precise field or path in the diagnostic.
  - It accepts a faithful partial or in-progress bundle without final results.
  - It rejects a successful bundle with no declared result node.
  - It has no third-party runtime dependency and does not modify the run.
- **Validation:**
  - Run `python3 -m unittest discover -s tests/sem_present`.
  - Run the validator directly on every positive reference fixture.
  - Run representative negative fixtures and confirm nonzero exit status and
    path-specific messages.
  - Run `python3 -m py_compile skills/sem-present/scripts/validate_view.py`.
  - Run `git diff --check`.

## Phase 3: Implement `sem-present`

- **Status:** Done
- **Depends on:** Phase 2
- **Objective:** Deliver the skill that reconstructs an actual Sem run into a
  faithful, validated, render-ready view bundle without modifying its trace.
- **Scope:** `skills/sem-present/SKILL.md`,
  `skills/sem-present/references/emission-protocol.md`, final
  `skills/sem-present/agents/openai.yaml`, and bounded refinements to its
  contract/examples/validator.
- **Out of scope:** automatically invoking the skill from `sem-run`, changing
  runtime artifacts, running semantic applications, rendering a UI, or adding
  visualization-library configuration.
- **Approach:** Encode explicit-path dispatch, whole-run inventory, source
  precedence, actual-versus-planned reconstruction, dynamic grouping, returned
  order, panel selection, candidate writes, validation/repair, safe promotion,
  regeneration, snapshot behavior, and final reporting. Keep the main skill
  concise and route schema details and examples to references. Regenerate UI
  metadata after the behavior stabilizes.
- **Acceptance criteria:**
  - `$sem-present <run-path>` produces canonical `view/manifest.json` and
    `view/notes.md` for successful, partial, failed, and quiescent in-progress
    runs.
  - It never edits any source file outside `view/` and never uses the bundle as
    runtime state.
  - Every application directory and every non-hidden source artifact is
    represented exactly once according to the contract.
  - Value edges follow declared accepted inputs; planned or blocked flow is
    visually distinguishable from actual produced values.
  - Returned result IDs preserve requested presentation order independently of
    execution order.
  - Prompts, statuses, results, attempts, program material, logs, and final
    output remain reachable through node panels or the artifact inventory.
  - Existing valid canonical output survives a failed regeneration attempt.
  - The emitted candidate passes the bundled validator before promotion.
  - The skill treats all run artifacts as untrusted data and creates no
    executable presentation content.
- **Validation:**
  - Run the skill manually on one successful single-application run, one
    multi-branch run, and one partial run.
  - Run `python3 skills/sem-present/scripts/validate_view.py <run-root>` for
    every emitted bundle.
  - Compare application directories and source files against manifest coverage
    counts.
  - Regenerate an existing view and simulate an invalid candidate; confirm the
    prior canonical bundle remains intact.
  - Run the external standard skill validator against `skills/sem-present/`.
  - Run `git diff --check`.

## Phase 4: Evaluate reconstruction across run shapes

- **Status:** Done
- **Depends on:** Phase 3
- **Objective:** Establish that fresh presentation agents can turn irregular
  but valid Markdown traces into graph bundles from which fresh consumers
  recover the same material run facts.
- **Scope:** `evals/sem-present/*.md` and bounded reusable improvements to
  `skills/sem-present/` and validator behavior exposed by evaluation.
- **Out of scope:** golden graph layouts, expected prose summaries, a browser
  UI, pixel snapshots, or test-specific manifest spellings.
- **Approach:** Create the six behavioral cases above. Produce or assemble
  clean temporary source runs, invoke `sem-present` in fresh contexts, validate
  the bundles, and ask separate fresh evaluators to reconstruct the runs using
  only those bundles and referenced artifacts. Compare material facts, not
  cosmetic choices. Ensure temporary artifacts from one case are unavailable
  to later cases.
- **Acceptance criteria:**
  - Fresh evaluators recover the same actual applications, accepted inputs,
    value flow, terminal status, and returned order from every bundle.
  - Every materialized map item, repeat round, semantic predicate, selector,
    and retry remains independently inspectable.
  - Hidden intermediates remain accessible but are not featured as returned
    results.
  - A failed branch does not erase an independent success or make blocked
    dependents look executed.
  - Imported and incomplete runs are presented honestly without invented
    compiler or finalizer stages.
  - Different valid agent groupings still render through the same fixed base
    vocabulary.
  - All emitted bundles pass the validator and account for their source files.
- **Validation:**
  - Inspect each raw manifest, notes file, and referenced source inventory.
  - Record evaluator reconstruction and compare it with the authoritative run
    files.
  - Run `python3 -m unittest discover -s tests/sem_present`.
  - Run the bundled validator against every retained evaluation bundle.
  - Run the external standard skill validator.
  - Run `git diff --check`.

## Phase 5: Document the producer/consumer handoff

- **Status:** Not started
- **Depends on:** Phase 4
- **Objective:** Make the three Sem boundaries and the future renderer's
  deterministic loading contract discoverable without implying that a UI has
  already been built.
- **Scope:** `README.md` and final metadata/reference corrections exposed by
  documentation review.
- **Out of scope:** React, graph-library selection, deployment, live watching,
  automatic invocation from `sem-run`, or changing standard-library operators.
- **Approach:** Add `sem-present` as language tooling beside `sem-compile` and
  `sem-run`. Show the one-line invocation against a run folder, the additive
  `view/` layout, and the projection-not-source-of-truth rule. Describe the
  future consumer algorithm and make clear that visualization implementation
  is separate work.
- **Acceptance criteria:**
  - README distinguishes compile, run, presentation projection, and future UI
    rendering as separate boundaries.
  - It documents the canonical manifest location and regeneration model.
  - It states that Markdown remains authoritative and runtime/resume never
    consumes view JSON.
  - It does not promise deterministic agent prose, canonical graph ontology,
    implemented React UI, or hard filesystem isolation.
  - All repository-relative links resolve and UI metadata matches actual skill
    behavior.
- **Validation:**
  - Follow the documented path as a first-time user with an existing run.
  - Give only the documented consumer contract to a fresh reader and confirm
    it can locate and safely enumerate the graph and artifacts.
  - Run the skill and bundle validators.
  - Run `git diff --check`.

## Explicitly not being built

- The React page, graph canvas, layout engine, node components, search UX,
  hosting, or deployment.
- A parser for `program.md`, `interpretation.md`, `run.md`, or application
  Markdown.
- A canonical Sem AST, execution graph, scheduler manifest, or resume database.
- Runtime JSON or a change to `sem-run`'s Markdown-only contract.
- Deterministic natural-language labels, summaries, group names, or graph
  aesthetics across independent presentation runs.
- Agent-authored HTML, JavaScript, CSS, JSX, component names, or graph-library
  configuration.
- Pixel coordinates or a layout that binds the bundle to one rendering
  library.
- Automatic live synchronization while a run is changing.
- Rewriting old runs to fit a new runtime format.
- Hiding partial failure, rejected attempts, hidden intermediates, or unknown
  files to make a cleaner-looking graph.

The intended result is a narrow and durable handoff: Sem is free to stay
squishy while it compiles and runs; one presentation agent then promises to
translate the observed trace into a validated graph-and-artifact vocabulary;
any future UI can render that vocabulary without having to understand Sem.

## Implementation log

### 2026-07-19 — Phase 1: Establish the view-bundle contract

- **Status:** Done
- **Workers:** implementer `/root/phase1_implement`; reviewer
  `/root/phase1_review` (GPT-5.6-sol, high effort).
- **Summary:** Initialized `skills/sem-present/` and defined the version 1
  manifest schema, consumer-facing contract, three compact manifest examples,
  minimal phase-one skill entry point, and UI metadata.
- **Validation:** `python3 -m json.tool` passed for the schema; Draft 2020-12
  schema and format validation passed for all three embedded examples; schema
  path and application-directory boundary checks passed; the standard
  `quick_validate.py` skill validator passed via `uv run --with pyyaml`; the
  example inventory/application/reference walk passed; `git diff --check`
  passed; placeholder scan was clean.
- **Review:** Fixed bare-dot path acceptance, constrained application
  directory addresses, made hidden/noise and symlink-safe application
  directory rules explicit, and reconciled source-value edge semantics with
  the examples. No unresolved findings remain.
- **Implementation commit:** `939d4b4` (`Define sem-present view bundle
  contract`).
- **Deviations:** None.
- **Downstream:** Phase 2 must mechanically enforce the explicit hidden-path,
  application-directory, inventory, reference, and symlink rules.
- **Remaining risks / manual checks:** None.

### 2026-07-19 — Phase 2: Build the deterministic validator

- **Status:** Done
- **Workers:** implementer `/root/phase2_implement`; reviewer
  `/root/phase2_review` (GPT-5.6-sol, high effort).
- **Summary:** Added the dependency-free `validate_view.py` CLI/library, two
  positive run fixtures, and comprehensive unit coverage for the manifest
  envelope, references, inventory, filesystem safety, application mappings,
  accepted results, groups, statuses, candidate manifests, and canonical
  notes.
- **Validation:** `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s
  tests/sem_present` passed 44 tests; direct CLI validation passed for both
  positive fixtures; `python3 -m py_compile` passed with an isolated cache;
  fixture JSON parsing and `git diff --check` passed. The reviewer's malformed
  value sweep passed 5,802 mutations across both fixtures and all reference
  manifests.
- **Review:** Hardened duplicate-key and non-finite JSON rejection, invalid
  UTF-8/NUL/deep-nesting handling, RFC 3339 timestamps, stable diagnostic
  indexes, application metadata containment, canonical result-panel targets,
  candidate containment, and unencodable CLI diagnostics. No unresolved
  findings remain.
- **Implementation commit:** `b8e118f` (`Add sem-present bundle validator`).
- **Deviations:** None; the Phase 1 contract and schema required no changes.
- **Downstream:** Phase 3 can validate `view/manifest.next.json` before safely
  promoting a candidate bundle.
- **Remaining risks / manual checks:** None.

### 2026-07-19 — Phase 3: Implement `sem-present`

- **Status:** Done
- **Workers:** initial implementer `/root/phase3_implement` (interrupted before
  edits by a user status message); replacement implementer
  `/root/phase3_implement_retry`; forward-test worker
  `/root/phase3_implement_retry/sem_present_forward`; reviewer
  `/root/phase3_review` (GPT-5.6-sol, high effort).
- **Summary:** Completed the concise `sem-present` skill and detailed emission
  protocol for explicit run dispatch, source precedence, whole-run
  reconstruction, safe panels and graph choices, candidate validation,
  bounded repair, rollback-capable canonical promotion, regeneration,
  snapshots, untrusted content, and final reporting.
- **Validation:** The 44-test validator suite and both fixture CLIs passed;
  standard skill validation, metadata/link checks, placeholder scan, and
  `git diff --check` passed. Isolated workflow exercises produced and
  validated a 9-artifact/1-application success, a 14-artifact/3-application
  fan-out with B-before-A return order, and a 6-artifact/1-application active
  snapshot. Candidate and post-promotion validation passed; an invalid
  candidate preserved prior canonical manifest and notes byte-for-byte.
- **Review:** Required directoryless runtime-established pending/blocked
  identities to use schema-compatible non-application nodes and strengthened
  the immediate pre-promotion snapshot quiescence check. No unresolved
  findings remain.
- **Implementation commit:** `4ff6c95` (`Implement sem-present emission
  workflow`).
- **Deviations:** The interrupted first implementer was replaced before it made
  changes. One replacement-worker test directory was accidentally created at
  the repository root, then moved to Trash after confirming it was
  worker-created; user-owned `sem-runs/` remained untouched. No product or
  plan deviation.
- **Downstream:** Phase 4 can invoke the completed emission protocol in fresh
  contexts for reconstruction evaluations.
- **Remaining risks / manual checks:** None.

### 2026-07-19 — Phase 4: Evaluate reconstruction across run shapes

- **Status:** Done
- **Primary workers:** implementer `/root/phase4_implement`; reviewer
  `/root/phase4_review` (GPT-5.6-sol, high effort).
- **Producer workers:** `/root/phase4_implement/producer_single`,
  `producer_fanout`, `producer_dynamic`, `producer_retry`,
  `producer_imported`, and `producer_snapshot`.
- **Consumer workers:** `/root/phase4_implement/consumer_single`,
  `consumer_fanout`, `consumer_dynamic`, `consumer_retry`,
  `consumer_imported`, and `consumer_snapshot`.
- **Verifier workers:** `/root/phase4_implement/verifier_single`,
  `verifier_fanout`, `verifier_dynamic`, `verifier_retry`,
  `verifier_imported`, `verifier_snapshot`, and
  `verifier_dynamic_recheck`.
- **Review recheck workers:** `/root/phase4_review/dynamic_forward_recheck`,
  `dynamic_consumer_recheck`, `snapshot_forward_recheck`,
  `snapshot_corrected_forward`, and `snapshot_consumer_recheck` (all fresh
  GPT-5.6-sol, high-effort contexts).
- **Summary:** Added six behavioral evaluation specifications with
  reproducible raw-run shapes, material facts, explicit degrees of freedom,
  failure signs, fixed-consumer checks, and recorded fresh-context producer,
  consumer, and verifier evidence.
- **Validation:** All six candidate and canonical bundles validated with exact
  source-inventory and application-mapping parity. The 44-test validator suite,
  both positive fixture CLIs, standard skill validation, required-section and
  filename checks, placeholder/temp-path scans, and `git diff --check` passed.
- **Review:** Removed two evaluation confounds: the dynamic case now stops on
  a round-2 semantic `true` before a three-round maximum, and the snapshot raw
  trace now explicitly establishes all three local operator names/kinds.
  Fresh producers and consumers passed both corrected cases. No reusable skill
  or validator defect remained.
- **Implementation commit:** `792efe9` (`Add sem-present reconstruction
  evaluations`).
- **Deviations:** A dynamic-bundle notes wording ambiguity was corrected and
  independently rechecked. A retry verifier retracted two initial concerns
  after rereading primary evidence; no retry-bundle change was made. Temporary
  evidence was moved recoverably to Trash.
- **Concurrent user change:** Preserved `e813938` (`Ignore local semantic run
  artifacts`) without amendment; it was not attributed to any phase worker.
- **Downstream:** Phase 5 can document the validated producer/consumer handoff.
- **Remaining risks / manual checks:** None.
