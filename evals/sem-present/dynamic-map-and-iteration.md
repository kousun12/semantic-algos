# Evaluation: dynamic map and iteration

## Purpose

Check that a presentation agent reconstructs dynamic language constructs from
the materialized trace without collapsing a map, repeat, semantic predicates,
or semantic choice into opaque source-level nodes.

## Reproducible raw-run setup

Create a fresh successful run with these nine application directories:

| Applications | Materialized role | Required order / result |
| --- | --- | --- |
| 001–003 | map `tagSignal` over amber, cobalt, fern | source item order |
| 004 | repeat body, round 1 | accepted refined label |
| 005 | semantic `cosmeticChange?`, round 1 | `false`, continue |
| 006 | repeat body, round 2 | accepted refined label |
| 007 | semantic `cosmeticChange?`, round 2 | `true`, stop |
| 008 | semantic `lengthSelector` | selects `short` |
| 009 | selected `shortForm` branch | sole return |

Record that applications 001–003 ran as an independent map batch, every
round/predicate was a distinct call, the repeat had a three-round maximum but
stopped semantically after round 2, and the long branch never materialized.
Include `inputs/signals.md`; the reference exercise has 36 source files and no
`view/`.

Invoke one fresh producer using only this raw run and the repository
`sem-present` skill.

## Material facts to preserve

- All three map items remain independent and ordered amber, cobalt, fern.
- Both repeat bodies and both semantic predicates remain independent
  applications; predicate results `false`, then `true`, explain termination
  before the three-round maximum.
- Accepted value flow crosses each executed round and predicate without
  turning a source-level repeat into a cycle or single node.
- Selector 008 is a semantic application, selected `short`, and only 009 ran.
- The unchosen long branch is absence, not a fabricated failed or blocked
  application.
- Application 009 is the only returned result; every one of 36 source files is
  inventoried.

## Degrees of freedom

`map`, `iteration`, and `choice` groups are useful but their exact nesting,
titles, collapse hints, optional group nodes, and edge labels are not golden.
The producer may omit a choice group when selector and selected-branch edges
already make the actual call clear. Member applications and their order may
never be replaced by a group.

## Observable failure signs

- Any map item, body round, semantic predicate, selector, or selected branch
  is missing or merged with another application.
- Item or round order is lost, or a cyclic edge pretends repeat is runtime
  recursion rather than materialized calls.
- A third round is fabricated, or termination is attributed only to maximum
  exhaustion instead of the accepted `true` predicate result.
- Predicate `true`/`false` results are treated as mechanical metadata rather
  than accepted semantic application values.
- Both terminal branches appear, or selection is attributed to the runner
  without application 008.
- The bundle returns an intermediate instead of 009 or omits dynamic prompts,
  statuses, results, or `inputs/signals.md`.

## Fixed-consumer checks

A fresh fixed consumer receives only the bundle and referenced source
artifacts. It must enumerate nine actual applications; recover the three item
order, two round order, predicate outcomes, semantic stop, selector result,
absence of the long branch, Succeeded status, sole returned 009 result, and
all 36 inventory paths. It may not parse `program.md` to invent missing graph
facts.

Agreement is required on materialized identities and flow, not on grouping
names or whether an optional stage node exists.

## Forward-test record

### 2026-07-19

- Producer `/root/phase4_implement/producer_dynamic` emitted and promoted a
  succeeded non-snapshot bundle with 36/36 artifacts, nine application
  mappings, 12 nodes, 18 edges, map/iteration/choice groups, and one return.
- Fresh consumer `/root/phase4_implement/consumer_dynamic` recovered every map
  item, both body/predicate rounds, `false` then `true` stop judgments,
  selector 008, short-only materialization, sole return 009, and all paths.
- Independent verifier `/root/phase4_implement/verifier_dynamic` confirmed all
  material facts but found one temporary-notes ambiguity: “initially visible”
  overstated the smaller featured focus set. The producer made a bounded notes
  correction distinguishing independently addressable/non-hidden applications
  from `featuredNodeIds`; the manifest stayed byte-for-byte unchanged.
- Fresh correction verifier
  `/root/phase4_implement/verifier_dynamic_recheck` rechecked the raw trace and
  canonical bundle. Candidate and canonical validation passed; no skill or
  validator change was needed.
- Phase reviewer `/root/phase4_review` found that the initial two-round maximum
  made the round-2 `true` predicate coincide with cap exhaustion. The reviewer
  changed the reproducible setup to a three-round maximum and regenerated from
  a clean copy with no `view/`.
- Fresh producer `/root/phase4_review/dynamic_forward_recheck` emitted a
  succeeded non-snapshot bundle with 36/36 artifacts, nine application
  mappings, 11 nodes, 16 edges, map/iteration/choice groups, and one return.
  Fresh fixed consumer `/root/phase4_review/dynamic_consumer_recheck` recovered
  all operators, item/round order, `false` then `true`, semantic stop before a
  third round, short-only materialization, sole return 009, and all 36 paths
  without using program intent to repair graph structure.
