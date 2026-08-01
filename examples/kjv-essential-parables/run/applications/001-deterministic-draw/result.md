# 001 · deterministic-draw

- Function: local `deterministicDraw3`
- Inputs: literal timestamp and ordered 16-entry pool
- Configuration: three deterministic selections without replacement

## Result

### selectedEntries

1. Arendt — clear conceptual distinctions; plurality, action, and judgment as pressures; institutional conditions made morally visible.
2. James Baldwin — moral intimacy; witness joined to self-implication; lyrical clarity; social truth carried through human relation.
3. Emil Cioran — compressed metaphysical pessimism; paradox; exhaustion and negation treated as thought experiments.

### receipt

- Seed: `2026-08-01T12:34:43-0400`
- Extracted digit string: `202608011234430400`
- Digits, indexed from 1: `d[1..18] = [2, 0, 2, 6, 0, 8, 0, 1, 1, 2, 3, 4, 4, 3, 0, 4, 0, 0]`
- First selection:
  - Formula: `1 + ((sum(j * d[j], j = 1..18)) mod 16)`
  - Evaluated sum: `2 + 0 + 6 + 24 + 0 + 48 + 0 + 8 + 9 + 20 + 33 + 48 + 52 + 42 + 0 + 64 + 0 + 0 = 356`
  - Evaluated position: `1 + (356 mod 16) = 1 + 4 = 5`
  - Lookup: position 5 in the original 16-entry pool is source label `Arendt`.
  - Removal: remove original-pool entry 5, leaving original source positions `[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]`.
- Second selection:
  - Formula: `1 + ((sum((j + 3) * d[j], j = 1..18)) mod 15)`
  - Evaluated sum: `sum(j * d[j]) + 3 * sum(d[j]) = 356 + 3 * 40 = 476`
  - Evaluated position: `1 + (476 mod 15) = 1 + 11 = 12`
  - Removal-aware lookup: position 12 in `[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]` is original source position 13, label `James Baldwin`.
  - Removal: remove original-pool entry 13, leaving original source positions `[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16]`.
- Third selection:
  - Formula: `1 + ((sum((j * j + 1) * d[j], j = 1..18)) mod 14)`
  - Evaluated sum: `4 + 0 + 20 + 102 + 0 + 296 + 0 + 65 + 82 + 202 + 366 + 580 + 680 + 591 + 0 + 1028 + 0 + 0 = 4016`
  - Evaluated position: `1 + (4016 mod 14) = 1 + 12 = 13`
  - Removal-aware lookup: position 13 in `[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16]` is original source position 15, label `Emil Cioran`.
- Selected source labels in draw order: `[Arendt, James Baldwin, Emil Cioran]`
