# KJV essential-structure parable cycle

```haskell
use [question-forge, parable]

sourceRequest = the exact request preserved in request.md

subject =
  CorpusReference
    { name = "the king james bible"
    , provenance = sourceRequest
    , externalText = none
      -- The runtime transforms the named subject in the request. It does not
      -- browse, open a Bible file, or introduce another textual source.
    }

runStamp = "2026-08-01T12:34:43-0400"

writerPoolInSourceOrder =
  [ { sourceLabel = "Camus"
    , broadMechanisms =
        [ lucid confrontation with absurd conditions
        , spare declarative pressure
        , ethical refusal without promised resolution
        ]
    }
  , { sourceLabel = "David F Wallace"
    , broadMechanisms =
        [ recursive self-scrutiny
        , systems entanglement
        , comic-anxious detail
        , compassion toward compromised participants
        ]
    }
  , { sourceLabel = "Borges"
    , broadMechanisms =
        [ compact metaphysical conceit
        , recursion and labyrinthine structure
        , pseudo-documentary framing
        , ontological ambiguity
        ]
    }
  , { sourceLabel = "Sontag"
    , broadMechanisms =
        [ aphoristic critical compression
        , attention to spectatorship and artifice
        , controlled intellectual distance
        ]
    }
  , { sourceLabel = "Arendt"
    , broadMechanisms =
        [ clear conceptual distinctions
        , plurality, action, and judgment as pressures
        , institutional conditions made morally visible
        ]
    }
  , { sourceLabel = "V. Woolf"
    , broadMechanisms =
        [ interior perception
        , rhythmic movement through consciousness
        , layered time
        , sensory transitions between minds and world
        ]
    }
  , { sourceLabel = "Barthes"
    , broadMechanisms =
        [ ordinary signs exposed as cultural codes
        , fragmentary conceptual turns
        , attention to how readers construct meaning
        ]
    }
  , { sourceLabel = "Le Guin"
    , broadMechanisms =
        [ anthropological world-building
        , moral reciprocity
        , a simple social rule with far-reaching consequences
        , quiet open-endedness
        ]
    }
  , { sourceLabel = "S Weil"
    , broadMechanisms =
        [ disciplined attention
        , affliction and obligation as moral forces
        , austere clarity
        , tension between gravity and grace
        ]
    }
  , { sourceLabel = "Geoff Dyer"
    , broadMechanisms =
        [ essayistic digression
        , self-aware observation
        , comic deflation
        , pivots from scene to concept
        ]
    }
  , { sourceLabel = "Mark Fisher"
    , broadMechanisms =
        [ systemic enclosure
        , lost futures
        , eerie pressure within everyday institutions
        , social structures felt as atmosphere
        ]
    }
  , { sourceLabel = "J Didion"
    , broadMechanisms =
        [ cool precise observation
        , implication through selected detail
        , fracture between orderly surface and underlying instability
        ]
    }
  , { sourceLabel = "James Baldwin"
    , broadMechanisms =
        [ moral intimacy
        , witness joined to self-implication
        , lyrical clarity
        , social truth carried through human relation
        ]
    }
  , { sourceLabel = "Stanislaw Lem"
    , broadMechanisms =
        [ speculative conceptual machinery
        , epistemic satire
        , bureaucratic absurdity
        , pressure on the limits of knowing
        ]
    }
  , { sourceLabel = "Emil Cioran"
    , broadMechanisms =
        [ compressed metaphysical pessimism
        , paradox
        , exhaustion and negation treated as thought experiments
        ]
    }
  , { sourceLabel = "Ivan Illich"
    , broadMechanisms =
        [ institutional inversion of intended benefits
        , attention to tools, scale, and dependency
        , convivial alternatives kept imaginable
        ]
    }
  ]

local deterministicDraw3(
  input: { seed: TimestampText, pool: exactly 16 ordered entries }
) -> { selectedEntries: exactly 3 distinct entries, receipt: DrawReceipt }:
  purpose:
    make the requested chance-like selection deterministic, observable, and
    reproducible inside a pure Markdown runtime
  moves:
    - delete every non-decimal character from `seed`, preserving digit order;
      call the resulting digits d[1..m]
    - from the original 16-entry pool choose position
      1 + ((sum over j=1..m of j * integer(d[j])) mod 16)
    - remove that entry while preserving the order of the remaining 15; choose
      from them at position
      1 + ((sum over j=1..m of (j + 3) * integer(d[j])) mod 15)
    - remove that entry while preserving the order of the remaining 14; choose
      from them at position
      1 + ((sum over j=1..m of (j*j + 1) * integer(d[j])) mod 14)
    - return the three entries in draw order
    - also return a receipt containing the seed, extracted digit string, all
      three formulas and evaluated positions, and the selected source labels
  return:
    exactly three unique pool entries plus one independently checkable receipt
  stop:
    after the third selection; uniqueness is guaranteed by removal
  guardrails:
    use 1-based positions, do not reorder the pool, request no entropy, and do
    not substitute an intuitive or model-chosen selection

local buildMajorMinorOutline(
  input: { subject: CorpusReference, terminalLeafCap: 12 }
) -> HierarchicalOutline:
  purpose:
    express the named corpus's essential whole as a compact hierarchical outline
  moves:
    - identify the fewest major movements that give coherent high-level coverage
      of the whole named corpus
    - under each major movement, define terminal minor sections that are
      collectively representative rather than an inventory of books
    - number major containers `1`, `2`, ... and terminal leaves `1.1`, `1.2`,
      `2.1`, ...; a major container is not itself a terminal leaf
    - give each leaf a concise title, scope description, and central material
      sufficient for an independent downstream question
    - keep recognizable corpus order unless a different ordering is essential
      to the structural account and is explicitly labeled
  return:
    one standalone numbered outline with no more than 12 terminal minor leaves
  stop:
    after one coherent outline of 8-12 terminal leaves, never exceeding 12
  guardrails:
    do not retrieve external text, quote invented passages, pretend that one
    outline is uniquely canonical, or let fine-grained coverage defeat the cap

local formIndependentHeartQuestion(leaf: OutlineLeaf) -> SurfaceQuestion:
  purpose:
    adapt one section descriptor into the question-shaped input required by
    `question-forge`
  moves:
    - identify the leaf's deepest live human, ethical, spiritual, or political
      tension supported by that leaf descriptor
    - phrase exactly one open question in which opposing answers retain weight
    - make it intelligible without any other leaf or the full outline
  return:
    one standalone surface question and nothing else
  stop:
    after one question
  guardrails:
    do not answer it, turn it into a factual or operational query, import a
    tension from another leaf, or add quotations and unsupported particulars

local blendBroadMechanisms(
  selectedBundles: exactly 3 lists of broad mechanisms
) -> AnonymousCraftBrief:
  purpose:
    convert the three selected, already-lowered bundles into one usable craft
    orientation without passing named-person imitation into story generation
  moves:
    - retain at least one compatible mechanism from each selected bundle
    - form a balanced set of 6-9 mechanisms spanning narrative form, stance,
      pacing or diction, and conceptual orientation when the inputs support them
    - resolve direct collisions by naming a productive tension in broad craft
      terms rather than privileging a source identity
    - remove source labels and biographical associations
  return:
    one anonymous craft brief containing only broad mechanisms and constraints
  stop:
    after one 6-9-mechanism brief
  guardrails:
    do not imitate signature voice, reproduce characteristic phrases, invent
    sample prose, or include any writer's name in the returned brief

kjvEssentialParables :: Program [Artifact]
kjvEssentialParables = do
  draw <- deterministicDraw3
            { seed = runStamp
            , pool = writerPoolInSourceOrder
            }

  selectedBundles =
    map structuralProjection(.broadMechanisms) draw.selectedEntries
    -- Pure field projection: writer labels do not cross this boundary.

  craftBrief <- blendBroadMechanisms selectedBundles

  outline <- buildMajorMinorOutline
               { subject = subject
               , terminalLeafCap = 12
               }

  leafResults <-
    outline.terminalLeavesInNumberOrder
    >>> map independently, preserving leaf order and failed positions:
          \leaf -> do
            surfaceQuestion <- formIndependentHeartQuestion leaf

            forgeReport <- questionForge surfaceQuestion

            forgedQuestionOnly =
              structuralProjection(forgeReport."The forged question")
              -- Pass only the forged question text, not the diagnosis,
              -- transformations, or "Living with it" material.

            story <-
              parable forgedQuestionOnly `with`
                { craftOrientation = craftBrief
                , relationToOtherLeaves = independent
                }

            return
              { leafNumber = leaf.number
              , leafTitle = leaf.title
              , parable = story
              , status = success
              }

            on failure:
              return the leaf number and title with the failed application's
              identity and no substitute story; continue other independent leaves

  hide [selectedBundles, craftBrief,
        every per-leaf surfaceQuestion, forgeReport, and forgedQuestionOnly]

  reveal [draw.receipt, outline, leafResults]
  pure [draw.receipt, outline, leafResults]
  >>> order [DeterministicDrawReceipt,
             MajorMinorOutline,
             ParablesInTerminalLeafNumberOrder]
```

Dynamic expansion: if the outline contains `n` terminal leaves, where
`8 <= n <= 12`, the mapped block creates exactly `n` independent
`formIndependentHeartQuestion` applications, `n` independent `question-forge`
applications, and `n` independent `parable` applications. Within one leaf those
three applications are sequential; across leaves they may run independently
after the shared outline and craft brief exist.
