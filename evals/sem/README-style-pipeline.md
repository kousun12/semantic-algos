# Evaluation: README-style pipeline

## Purpose

Check that `sem-run` can treat a loose Haskell-flavored composition as
executable prose, resolve named repository skills by their actual contracts,
and preserve sequence, parallel fan-out, collection, synthesis, and a final
audit without asking for parser-valid syntax.

## User-style invocation

Present only this block to the system under evaluation:

```text
$sem-run Here's the rough program I want to run. The notation is just a sketch.

libraryFines =
  questionForge "Should our community library eliminate overdue fines?"
  >>> ( firstPrinciplesThinking
        &&& inversion `with` { goal = "change the policy without hurting access or sustainability" }
        &&& analogyTransfer `with` { seek = "ways other systems replace punishment while preserving return" }
      )
  >>> dpSolve `with` { objective = "synthesize the branches, especially their reused constraints and disagreements" }
  >>> assumptionAudit

Keep the three branch results visible and return the final audit.
```

## Compilation must preserve

- The original policy question is forged once before branching; the compiler
  must not answer it while compiling.
- The three named branches receive the same forged-question result and remain
  distinguishable.
- `first-principles-thinking`, `inversion`, `analogy-transfer`, `dp-solve`, and
  `assumption-audit` are resolved from their exact repository skill folders.
  `questionForge` mechanically resolves to `question-forge`.
- `dp-solve` receives the collected branch results and performs the requested
  synthesis before `assumption-audit` audits that synthesis.
- The three branch results remain visible even though the final audit is the
  sole returned artifact.
- Fan-out and collection may be expressed in any intelligible notation. No
  exact formatting, type signature, or syntactic spelling is required.
- No local semantic operator should be invented for work already covered by a
  named standard-library contract. Structural collection is not an application.

## Independent applications

- Forging the question is one application.
- The first-principles, inversion, and analogy-transfer branches are three
  separate applications. Once the forged question succeeds, they are mutually
  independent and should be eligible for the same scheduling batch.
- `dp-solve` is a later application dependent on all three branch results.
- `assumption-audit` is a final application dependent on the synthesis.
- Every one of these six semantic applications must use a distinct fresh
  no-history worker and produce its own standalone result.

## Expected run artifact shape

A successful run contains the ordinary top-level Markdown trace: `request.md`,
`compiler-prompt.md`, `program.md`, `compile-notes.md`, `interpretation.md`,
`run.md`, `finalizer-prompt.md`, and `final.md`.

Under `applications/`, expect one prompt/result/status directory for the forge,
one for each of the three branches, one for synthesis, and one for the audit.
Directory ordinals and descriptive names may vary, but dependencies and the
parallel group must be reconstructable from `interpretation.md` and `run.md`.
`final.md` links the visible branch artifacts, includes or links the returned
audit, summarizes the actual dataflow, and indexes every Markdown artifact.

## Observable failure signs

- The sketch is rejected or mechanically repaired merely because it is not
  valid Haskell.
- A named function is selected by semantic resemblance instead of exact
  repository-slug or mechanical camel-case resolution.
- A branch contract is replaced by a generic prompt, or a local `synthesize`
  shim silently replaces the named `dp-solve` application.
- Two or more branch operations are performed in one worker, or a branch sees
  sibling results it was not declared to consume.
- Synthesis starts before every required branch succeeds.
- The visible branch results disappear from the trace or `final.md` omits
  application prompts, statuses, or results from its artifact index.

## Evaluation note

Judge the semantic boundaries, contract use, artifacts, and dataflow. Do not
compare the prose results to a golden answer or require one compiled notation.
