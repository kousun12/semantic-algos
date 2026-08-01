# Interpretation

## Reasoned reading

The ready program is a finite pure-text run over the named corpus reference “King James Bible”; it authorizes no Bible file, web retrieval, or quotation source. “Major.minor” means major containers numbered `1`, `2`, … with terminal leaves numbered `1.1`, `1.2`, … . The outline operator may choose 8–12 leaves and must never exceed 12. One timestamp-seeded draw of three distinct entries is reused across all leaf parables. Writer labels remain visible only in the draw receipt; parable workers receive an anonymous craft brief.

The compiler’s `map structuralProjection` and later field projections are mechanical field selection, not semantic applications. Naming, hiding, revealing, packaging leaf records, preserving mapped order, and final ordering are also structural.

## Static applications

### 001 · deterministic-draw

- Program excerpt: `draw <- deterministicDraw3 { seed = runStamp, pool = writerPoolInSourceOrder }`
- Function: local `deterministicDraw3`, fully defined in `program.md` and copied into the worker prompt.
- Inputs: literal timestamp `2026-08-01T12:34:43-0400` and the literal ordered pool of 16 lowered entries.
- Configuration: 1-based, three draws without replacement, exact formulas from the program.
- Expected result: three selected entries plus independently checkable receipt.
- Stop: after the third selection.
- Dependencies: none. Parallel group A with 003.
- Visibility: selected entries are hidden downstream data; receipt is returned first.

### 002 · blend-craft-mechanisms

- Program excerpt: `craftBrief <- blendBroadMechanisms selectedBundles`
- Function: local `blendBroadMechanisms`, fully defined in `program.md` and copied into the worker prompt.
- Inputs: application 001’s selected entries after structural projection to their `broadMechanisms` fields.
- Configuration: retain contribution from all three; anonymous 6–9 mechanism brief.
- Expected result: anonymous craft brief with only broad mechanisms and constraints.
- Stop: after one 6–9-mechanism brief.
- Dependencies: 001.
- Parallel group: B.
- Visibility: hidden but passed to every parable application.

### 003 · build-major-minor-outline

- Program excerpt: `outline <- buildMajorMinorOutline { subject = subject, terminalLeafCap = 12 }`
- Function: local `buildMajorMinorOutline`, fully defined in `program.md` and copied into the worker prompt.
- Inputs: literal corpus reference “King James Bible”; no external text.
- Configuration: coherent representative corpus order; 8–12 terminal leaves; hard cap 12.
- Expected result: standalone hierarchical outline whose leaves each include number, title, scope, and central material.
- Stop: after one coherent 8–12-leaf outline.
- Dependencies: none. Parallel group A with 001.
- Visibility: returned second and used to expand the leaf map.

## Dynamic leaf expansion

After 003 succeeds with `n` leaves (`8 <= n <= 12`), create three applications per leaf in terminal-leaf number order:

1. local `formIndependentHeartQuestion(leaf)` using exactly that leaf’s descriptor;
2. repository `question-forge` using only the accepted surface question Result;
3. repository `parable` using only the structurally projected `## The forged question` text from the forge Result, configured by the accepted anonymous craft brief from 002.

Within a leaf, those applications are sequential. Across leaves, all ready applications at the same stage are mutually independent. The adapter and forge results are hidden but traceable. The parable result is returned in its leaf position. A leaf-chain failure blocks only its dependent applications, preserves the position and failure identity, and does not stop independent leaves.

The local adapter returns exactly one standalone open question and stops after one pass. `question-forge` is one pass and must retain its full prescribed report, although only its forged-question field passes downstream. `parable` returns one title and 300–800 word story, then stops. Each worker receives its selected function contract, smallest declared inputs, configuration, and assigned result path only.

## Terminal artifacts and presentation order

1. Deterministic draw receipt from 001.
2. Major.minor outline from 003.
3. Leaf-labeled parables in terminal-leaf number order, with failed positions represented structurally rather than replaced.

## Failure behavior

Independent branches continue after failure. A failed 001 blocks 002 and therefore every parable, but not 003 or the per-leaf adapters and forges that depend only on the outline. A failed 002 blocks parables only. A failed 003 prevents leaf expansion. Malformed results receive at most one fresh-worker mechanical retry under the runtime protocol.

## Isolation note

Fresh no-history workers and narrow read/write prompts provide conversational isolation and a behavioral filesystem boundary. Because workers share the workspace, this is not an operating-system filesystem sandbox.

## Runtime amendment · accepted dynamic expansion

Application 003 attempt 1 was rejected for returning 13 leaves and preserved unchanged. Retry attempt 2 was accepted with 12 leaves. In leaf order, the runner assigned these chains: 004–006 = 1.1; 007–009 = 1.2; 010–012 = 1.3; 013–015 = 2.1; 016–018 = 2.2; 019–021 = 2.3; 022–024 = 2.4; 025–027 = 3.1; 028–030 = 3.2; 031–033 = 4.1; 034–036 = 4.2; 037–039 = 4.3. Within each triplet the order is heart adapter, question-forge, parable.
