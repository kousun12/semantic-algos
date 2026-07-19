# Evaluation: fan-out with a hidden intermediate

## Purpose

Check that a shared hidden upstream application appears once, remains
inspectable, and feeds two independent visible branches whose declared return
order differs from their ordinal and completion order.

## Reproducible raw-run setup

Create a fresh successful run with three application directories:

| Ordinal | Application | Input | Visibility / scheduling |
| --- | --- | --- | --- |
| 001 | local `normalizeIncident` | request | hidden shared upstream |
| 002 | local `operatorCard` | accepted 001 Result | fan-out batch `cards` |
| 003 | local `managerCard` | accepted 001 Result | fan-out batch `cards` |

The request says the north-pump pressure fell and its alarm sounded. Record
002 and 003 as independently launched after 001. Record ordinal/completion
order as operator then manager, but declare returned presentation order as
manager then operator. The reference exercise has 17 source files and no
pre-existing `view/`.

Invoke a fresh producer with only the explicit run root and the repository
`sem-present` skill.

## Material facts to preserve

- The hidden normalization is one independently addressable application, not
  copied once per branch and not omitted.
- Both branches consume the same accepted 001 value and neither consumes its
  sibling.
- Applications 002 and 003 form an independent fan-out after 001.
- Hidden means de-emphasized: 001 is not featured or returned, but its prompt,
  status, and result remain accessible.
- Return order is 003 manager then 002 operator, independent of directory and
  completion order.
- All three applications and all 17 source files are represented exactly
  once.

## Manifest-only structural provenance

Before opening referenced Markdown, the fixed consumer must derive the three
application mappings/operators/statuses and hidden emphasis from `nodes`, the
shared upstream and independent branch flow from `edges`, fan-out membership
and order (when represented as a group) from `groups`, `[003, 002]` from
`presentation.resultNodeIds`, and the 17-path inventory from `artifacts`.
Markdown may provide displayed request/result bodies or serve as independent
verification evidence after reconstruction; it may not be parsed to infer or
repair application identity, flow, visibility, status, grouping, or return
order.

## Degrees of freedom

The producer may use a `fan-out` group or communicate independence with edges
and summaries; it may add a source node or leave run-level documents in the
inventory. Titles, IDs, grouping labels, panel order, and initial camera hints
are non-golden. The fixed base vocabulary and material facts are not.

## Observable failure signs

- The shared upstream is duplicated, omitted, or shown as returned.
- Hidden suppresses the application's node or its artifacts.
- One branch is shown as consuming the other or the branches look sequential.
- Result order follows ordinals/filesystem order rather than manager then
  operator.
- A group replaces either branch's independent application identity.

## Fixed-consumer checks

With only the emitted bundle and its referenced artifacts, a fresh consumer
must first recover from manifest fields three application directories, the
single shared accepted input,
the two independent branch relationships, the hidden-but-inspectable status
of 001, Succeeded terminal status, and result order `[003, 002]`. It must also
locate every prompt, result, status, and run-level document through panels or
the 17-record inventory.

Do not require the consumer to agree with producer-specific titles or group
names and do not let it parse `program.md` to repair a deficient manifest.

## Forward-test record

### 2026-07-19

- Producer `/root/phase4_implement/producer_fanout` emitted and promoted a
  succeeded non-snapshot bundle with 17/17 artifacts, three application
  mappings, four nodes, three edges, one fan-out group, two ordered returns,
  and no warnings.
- Fresh consumer `/root/phase4_implement/consumer_fanout` recovered the shared
  hidden 001 value, independent 002/003 fan-out, ordinal/completion order,
  manager-before-operator return order, terminal state, and all source paths.
- Independent verifier `/root/phase4_implement/verifier_fanout` confirmed the
  exact inventory/mappings, hidden-but-inspectable treatment, branch
  independence, value flow, and return order. Its observation that the
  promoted bundle no longer retains `manifest.next.json` is expected: notes
  record candidate validation and successful promotion removes candidates.
- Candidate and canonical validation passed; no reusable change was needed.
