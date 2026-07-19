# Evaluation: terse natural language

## Purpose

Check that a low-fidelity request can become a small program without making the
user choose operators, learn notation, or endure unnecessary compiler ceremony.

## User-style invocation

Present only this block to the system under evaluation:

```text
$sem-run I keep volunteering for projects and then resenting everyone for needing me. Find the real question hiding under that, then turn it into a short story where the dilemma becomes physical and nobody explains the lesson. Only show me the story.
```

## Compilation must preserve

- The source tension includes both self-initiated helpfulness and later
  resentment; it must not be simplified into generic overwork advice.
- Finding the underlying question and embodying that question as a story are
  separate semantic transformations with explicit dataflow.
- The final form is a parable-like story that refuses an explanatory moral,
  not analysis followed by decorative fiction.
- The upstream reframing remains hidden from the presentation but retained in
  the inspectable run trace.
- Only the story is returned to the user. Hidden does not mean unrecorded.
- Compilation should choose the smallest contract-justified program. It may
  use the repository's `question-forge` and `parable` functions, but this case
  does not prescribe their surface spelling or a canonical program layout.

## Independent applications

- The question-finding step and the story-making step require separate fresh
  no-history workers and separate artifacts.
- The story step depends on the accepted result of the question step; these
  two applications are sequential rather than parallel.
- The story worker receives only the declared reframed question, the selected
  function contract, its local constraints, and its assigned output contract.
  It must not receive the full original request or the return list.

## Expected run artifact shape

The run contains the standard top-level Markdown trace and two materially
distinct application directories, each with `prompt.md`, `result.md`, and
`status.md`. If the compiler chooses an equally small decomposition with an
additional genuinely necessary semantic application, the reason must be clear
in `compile-notes.md` and `interpretation.md`; ceremony alone is not sufficient.

`final.md` presents the story in useful form, links the hidden upstream result
through its complete artifact index, identifies the value flow in its summary,
and does not expose hidden analysis as an additional returned answer.

## Observable failure signs

- The runner asks the user to provide Sem syntax or select named skills.
- The compiler answers the dilemma, writes the story itself, or turns the
  request into a sprawling analysis program.
- One worker both reframes the question and writes the story.
- The story is generic burnout advice, explicitly states its lesson, or loses
  the contradiction between volunteering and resenting dependence.
- The hidden intermediate has no standalone result or is omitted from the
  final artifact index.
- The story worker's prompt contains the full request, downstream presentation
  instructions, or undeclared run artifacts.

## Evaluation note

There is no expected story and no mandatory compiled syntax. Evaluate fidelity,
restraint, isolation, and the trace left by the chosen applications.
