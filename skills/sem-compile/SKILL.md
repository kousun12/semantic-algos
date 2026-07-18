---
name: sem-compile
description: "Compile natural language or a loose composition sketch into a readable, Haskell-esque Sem program that composes this repository's semantic skills. Use when a user asks to express, design, or revise a semantic program without running it."
---

# Sem Compile

Express requests as interpretable semantic programs. Sem is deliberately
squishy: produce clear executable prose, not parseable source code.

Before writing a program, read
[references/language-conventions.md](references/language-conventions.md). Use
[references/example-programs.md](references/example-programs.md) to calibrate
how much structure a program needs and how to expose its application
boundaries.

Treat other semantic skills in this repository as the standard library. Read a
candidate skill's complete `SKILL.md` before using it as an operator. Keep
language tooling out of ordinary programs unless the request is itself about
compilation or execution.

This skill compiles only. Do not execute the program or answer the source
request.
