# Phase 3 Staging Pilot

This directory contains pilot-only KB staging outputs for the reAM250 BOM-to-KB
conversion workflow. These files are not authoritative KB entries and must not
be copied into `kb/` without a later promotion review.

## Phase 3 Purpose

Phase 3 takes a completed Phase 2 merge review and turns it into a concrete
staging package:

- proposed item actions: `reuse_existing`, `create_new`, or `defer`;
- import/local manufacture decision for each proposed item;
- row-to-closure-item mappings with quantities and row-total mass preserved;
- KB-like item fields needed for later promotion;
- process assumptions and candidate existing KB process anchors;
- promotion blockers that must be resolved before writing final KB YAML.

Phase 3 is where the workflow first asks whether a merge decision is usable as a
KB edit. It should expose missing fields, unresolved material/process choices,
and whether the Phase 2 proposed item is too reAM250-specific or can become a
general reusable KB item.

## Pilot Scope

This pilot intentionally covers three representative cases:

- `ream250_kb_merge_0035_structural_frame_member`: partial merge with new staged
  structural items.
- `ream250_kb_merge_0040_threaded_fastening`: clean merge into an existing KB
  item.
- `ream250_kb_merge_0025_plumbing_connection`: partial merge with standard
  vacuum/fluid interfaces, sealing guardrails, and local-manufacture precision
  blockers.

The goal is to test the phase design, not to produce final closure data.

## Promotion Rule

Before any staged item is promoted to `kb/`, review:

- whether an equivalent KB item already exists;
- whether `kind`, `unit`, `unit_kind`, `mass_kg`, and `material_class` are
  compatible with current KB schema;
- whether recipes should reuse existing processes or need new process/recipe
  work;
- whether the item should be marked `is_import: true`, treated as locally
  manufacturable now, or kept as a local-manufacture candidate with recipe gaps;
- whether row-specific guardrails belong in item notes, BOM notes, recipe notes,
  or unresolved research tasks.
