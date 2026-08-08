# 028: Material, Raw Material, and Resource Item Classification

**Status:** Proposed; parser support implemented
**Date:** 2026-07-31
**Decision Makers:** Project team
**Related ADRs:** ADR-011 (Regolith Organization Pattern), ADR-023 (Material Provenance Tracking), ADR-027 (Item Performance and Mass Ranges)

---

## Context

The KB previously mixed several different concepts under `kind: material`:

- natural lunar source materials, such as regolith, ores, feldspars, and meteorite material
- process-ready engineering materials, such as powders, concentrates, stock, chemicals, byproducts, and scrap
- non-material resources, such as solar flux, electrical energy, heat, and data-like inputs

This made closure analysis and material selection harder to interpret. A material can be geologically present on the Moon while still lacking a usable KB route to a process-ready manufacturing feedstock. Likewise, energy and information resources are process inputs, but they are not materials and should not be treated as lunar material availability.

## Decision

Item classification is split into three explicit KB categories:

1. `raw_material`
   - Directory: `content/kb/items/raw_materials/`
   - Meaning: natural, mined, collected, or otherwise primary source material that is not yet a controlled process-ready engineering material.
   - Examples: `regolith_lunar_highlands`, `regolith_lunar_mare`, `anorthite_ore`, `plagioclase_feldspar`, `nife_meteorite_material`.

2. `material`
   - Directory: `content/kb/items/materials/`
   - Meaning: process-ready engineering material, chemical, feedstock, stock form, powder, wire, ingot, slurry, intermediate, byproduct, or scrap.
   - Examples: `steel_stock`, `alumina_powder`, `ceramic_powder`, `regolith_powder`, `ilmenite_concentrate`, `metal_wire_feed`.

3. `resource`
   - Directory: `content/kb/items/resources/`
   - Meaning: non-material process input/output such as energy, heat, environmental flux, data, or another service-like resource.
   - Examples: `solar_irradiance`, `solar_radiation`, `electrical_energy`, `waste_heat`, `coded_data`.

The operating guide for design screening is `docs/lunar_material.md`; it does
not replace content-specific closure analysis.

## Consequences

- Closure analysis can use `raw_material` as a source-side boundary without confusing it with processed feedstock.
- Lunar material design reviews must distinguish natural availability from a proven KB process route.
- Powders and concentrates produced from regolith are modeled as `material`, not `raw_material`.
- Solar flux, electrical energy, heat, and data are modeled as `resource`, not `material`.
- The indexer, schema validation, lazy item loader, and SimViewer search must accept all three categories.

Existing `kind: material` and `kind: part` entries remain supported. This ADR
does not require an engine PR to migrate a separately versioned content
repository, and directory placement alone must not silently rewrite item kind.

## Non-Goals

- This ADR does not make every lunar material locally producible.
- This ADR does not define substitution groups. Item identity still uses explicit item IDs; material substitution should be modeled separately from item classification.
- This ADR does not remove material provenance tracking. Provenance remains a simulation concern that records whether inventory mass came from in-situ or imported sources.
