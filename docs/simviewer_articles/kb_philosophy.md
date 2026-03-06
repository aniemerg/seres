---
id: kb_philosophy
title: KB Design Philosophy — Gaps, Imports, and Conservative Modeling
type: article
---

The SERES knowledge base is intentionally incomplete. This page explains why, and what the gaps, imports, and warnings you see in the model actually mean.

## Gaps Are the Output

A common reaction to seeing warnings or unresolved items in the simulation is to treat them as errors. They are not. The simulation is designed to run with missing data and surface gaps explicitly. The gaps *are* the primary output — they tell you which manufacturing chains are not yet closed and where modeling effort should go next.

The model's job is to make incompleteness visible, not to paper over it with assumptions.

## Imports as Boundary Conditions

When an item cannot be manufactured locally — either because no recipe exists, or because its dependency chain is broken — it is treated as an *import*. Imports carry an explicit mass penalty. This means:

- The model never silently "succeeds" by hiding a missing dependency
- Every import appears in the mass accounting, making the gap quantified and visible
- Over time, imports can be replaced by local production as the KB grows

An item being marked as an import is not a claim that it can never be made locally. It is the model's way of saying: *we haven't modeled this yet*.

## Why the KB Uses Generic Items

The KB strongly favors generic, reusable items over highly specific ones. Instead of `steel_304_sheet_2mm` and `steel_316_sheet_3mm` as separate entries, the model uses `metal_sheet_structural` with a `material_class` of `metal`. This approach:

- Keeps the dependency graph tractable (hundreds of near-identical items obscure structure)
- Allows recipes to express "needs metal sheet" without committing to a specific alloy
- Reflects the actual precision of the model — at this level of analysis, the difference between 304 and 316 stainless is not meaningful

The tradeoff is that the model is less precise than an engineering specification. This is intentional. See [[parts_and_labor]] for the 5× equivalence rule that governs when two items are consolidated into one.

## Phase and State Variations

The KB does not create separate items for different states of the same material. Water, water vapor, and ice are all represented as `water`, with phase transitions modeled as process steps. Similarly, molten steel and solid steel are not separate items — the transformation is in the process.

This prevents an explosion of near-identical items and keeps the focus on what processes are needed, not on labeling every intermediate state.

## What Warnings Mean

The simulation export surfaces several categories of warnings:

**Unresolved wiki-links.** An article references a KB entity or another article by ID, but no matching entry was found. This is an article authoring issue, not a simulation problem.

**Missing KB categories.** Some machine entries are missing a `category` field. This is a minor completeness gap in the KB metadata, not a modeling problem.

**Undefined references.** A recipe or process references an item ID that doesn't exist in the KB. These are the most important gaps — they indicate broken dependency chains.

## The Conservative Modeling Principle

When building or extending the KB, the guiding principle is: *maximize reuse, minimize creation*. Before adding a new item, the model asks whether an existing item is close enough (within 5×), whether a phase variation of an existing item would work, or whether the gap reflects a typo or naming inconsistency rather than a genuinely new entity.

This discipline keeps the graph navigable. Item proliferation — hundreds of near-identical parts with slightly different names — is the primary threat to the model's analytical value.

## Related Articles

- [[about_seres]] — Project overview and why incompleteness is a design choice
- [[parts_and_labor]] — Part reuse policy and the 5× equivalence rule
- [[material_classes]] — How material substitution works (and when it is disabled)
