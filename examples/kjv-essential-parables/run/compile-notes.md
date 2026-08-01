# Compile notes

Status: ready
Input mode: natural language

## Preserved requirements

- The named subject remains the King James Bible, referenced only through the
  exact request preserved in `request.md`.
- The structural breakdown is a hierarchical numbered outline: major containers
  use `1`, `2`, ... and terminal minor leaves use `1.1`, `1.2`, ... .
- The outline targets 8-12 terminal leaves and has a hard cap of 12.
- Each leaf independently becomes a question-shaped input, passes through
  `question-forge` once, and sends only its forged-question field to `parable`.
- One three-entry selection is drawn from the exact 16-name source-order pool.
  Its fixed timestamp seed, arithmetic, evaluated positions, and selected names
  are visible in a draw receipt, making the selection reproducible without an
  external random service.
- The same selected mixture informs every leaf parable, while the leaf content
  branches remain independent.
- Visible results are the deterministic draw receipt, the major.minor outline,
  and the leaf-labeled parables in terminal-leaf number order. Question-forge
  reports and other working values remain traceable dependencies but are hidden.

## Standard-library resolution

- `question-forge`: exact fit after the local adapter produces one non-operational
  surface question per leaf. Its full one-pass report is retained internally;
  only the `The forged question` field is structurally projected downstream.
- `parable`: exact fit for turning each forged question into a 300-800 word story
  that embodies one tension, uses one unexplained strange rule, gives competing
  stances dignity, implicates the reader, and ends without adjudication. The
  anonymous craft brief refines but does not replace that contract.
- `sem-run` appears in the preserved request as the requested invocation mode,
  but is language tooling rather than an executable semantic operator and is not
  included in the compiled program.

## Local operators and invented constructs

- `deterministicDraw3`: a bounded, purely mechanical three-without-replacement
  draw from an ordered pool. The timestamp already fixed in `request.md` is its
  seed. It returns selected entries plus an auditable receipt after exactly
  three choices.
- `buildMajorMinorOutline`: performs the semantic corpus-level decomposition that
  no selected repository skill supplies. It returns one ordered hierarchical
  outline with 8-12 terminal leaves and never more than 12.
- `formIndependentHeartQuestion`: adapts one outline leaf to the question input
  shape required by `question-forge`, without answering or importing other leaves.
- `blendBroadMechanisms`: combines exactly three already-lowered craft bundles,
  retaining contribution from each and returning an anonymous 6-9-mechanism brief.
- `structuralProjection`: field selection only, not a semantic application. It
  removes writer labels before craft blending and extracts only the forged
  question before parable generation.
- The mapped leaf block is finite because `buildMajorMinorOutline` returns 8-12
  leaves. It preserves leaf order and failed positions; each leaf has three
  sequential applications, while different leaves are independent once shared
  upstream values exist.

## Named-style lowering

Every source reference is preserved in `request.md` and in the observable draw
pool, but executable `parable` applications receive only the anonymous result of
`blendBroadMechanisms`. The conservative broad mappings are:

- Camus -> lucid confrontation with absurd conditions; spare declarative
  pressure; ethical refusal without promised resolution.
- David F Wallace -> recursive self-scrutiny; systems entanglement; comic-anxious
  detail; compassion toward compromised participants.
- Borges -> compact metaphysical conceit; recursion and labyrinthine structure;
  pseudo-documentary framing; ontological ambiguity.
- Sontag -> aphoristic critical compression; attention to spectatorship and
  artifice; controlled intellectual distance.
- Arendt -> clear conceptual distinctions; plurality, action, and judgment;
  institutional conditions made morally visible.
- V. Woolf -> interior perception; rhythmic movement through consciousness;
  layered time; sensory transitions between minds and world.
- Barthes -> ordinary signs exposed as cultural codes; fragmentary conceptual
  turns; attention to readerly construction of meaning.
- Le Guin -> anthropological world-building; moral reciprocity; a simple social
  rule with far-reaching consequences; quiet open-endedness.
- S Weil -> disciplined attention; affliction and obligation; austere clarity;
  tension between gravity and grace.
- Geoff Dyer -> essayistic digression; self-aware observation; comic deflation;
  pivots from scene to concept.
- Mark Fisher -> systemic enclosure; lost futures; eerie everyday institutions;
  social structures felt as atmosphere.
- J Didion -> cool precise observation; implication through selected detail;
  fracture between orderly surface and underlying instability.
- James Baldwin -> moral intimacy; witness with self-implication; lyrical
  clarity; social truth carried through human relation.
- Stanislaw Lem -> speculative conceptual machinery; epistemic satire;
  bureaucratic absurdity; limits of knowing.
- Emil Cioran -> compressed metaphysical pessimism; paradox; exhaustion and
  negation as thought experiments.
- Ivan Illich -> institutional inversion of intended benefits; tools, scale,
  and dependency; convivial alternatives kept imaginable.

These mechanisms preserve the requested orienting function without asking for
signature-voice imitation, characteristic phrases, or biographical simulation.

## Inferences

- “Major.minor form” is read as a hierarchy whose terminal nodes are numbered
  `1.1`, `1.2`, and so on, rather than as decimal scores or version numbers.
- “About 12 total leaves” is implemented as an 8-12 target with a hard maximum
  of 12, favoring compression over fine-grained book-by-book coverage.
- The singular phrase “a mixture of 3 writers chosen randomly” is read as one
  run-level draw reused for all parables, not a new draw per leaf.
- Because true nondeterministic entropy is unavailable and the caller required
  observability and reproducibility in pure Markdown, “randomly” is implemented
  as a chance-like deterministic draw seeded by the request's fixed creation
  timestamp. No selected names or calculated draw positions were produced at
  compile time.
- The requested final artifacts are interpreted as the outline and parables.
  The question-forge reports are intermediate transformations and are hidden;
  the draw receipt is additionally visible to satisfy reproducibility.
- No Bible text or other workspace/external text was authorized. The program
  therefore operates on the corpus reference named in the request and forbids
  browsing, file reads, or quotation retrieval.

## Ambiguities

- “Essential structure” has multiple defensible scholarly and theological
  readings. The program preserves that non-uniqueness as a guardrail and asks
  the outline operator for one coherent, representative account rather than
  claiming a uniquely canonical decomposition.
- “Sensibility/orientation” could mean voice imitation, thematic orientation,
  or craft influence. The program uses broad craft and conceptual mechanisms,
  which preserves the creative function while avoiding named-person imitation.

Neither ambiguity blocks the dataflow under the conservative readings above.

## Handoff audit

- Static applications are recoverable: one `deterministicDraw3`, one
  `blendBroadMechanisms`, and one `buildMajorMinorOutline`, each with declared
  inputs, output shape, bound, and guardrails.
- For `n` outline leaves (`8 <= n <= 12`), dynamic expansion is recoverable:
  `n` local question adapters, `n` `question-forge` applications, and `n`
  `parable` applications. Each leaf chain is sequential; the `n` chains are
  mutually independent after their shared dependencies are available.
- The draw always stops after three removal-based selections. All other local
  operators are one-pass. `question-forge` is one-pass and `parable` produces
  one bounded story under their repository contracts.
- Each parable's semantic input is exactly its leaf's forged-question text; its
  only additional configuration is the shared anonymous craft brief.
- Failed leaf positions remain visible and do not cause replacement stories or
  halt independent leaves.
- Visible returns and presentation order are explicit: draw receipt, numbered
  outline, then leaf-labeled parables in terminal-leaf order. Hidden values are
  retained as dependencies rather than erased.
- Preservation audit passed: objective, subject, finite hierarchy, leaf cap,
  independent forging, question-only handoff, three-source mixture, named-style
  lowering, visibility, and ordering are all represented without executing any
  semantic function or generating runtime content.
