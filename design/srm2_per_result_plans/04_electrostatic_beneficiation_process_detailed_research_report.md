# Electrostatic Beneficiation Process Detailed Research Report

Date: 2026-03-04
Scope: `design/srm2_bom_research_results/04_electrostatic_beneficiation_process.md`
Purpose: convert the report flowsheet into concrete KB process/recipe updates using existing materials wherever possible.

## 1) Source extraction summary
Report 04 describes a staged dry beneficiation chain:
1. feed conditioning and sizing
2. optional magnetic pre-clean
3. tribocharging
4. parallel-plate electrostatic split into multiple product streams
5. middlings reclean loop for grade/recovery tuning

The report emphasizes explicit stream splitting and downstream routing:
- plagioclase/anorthite-rich stream
- pyroxene/mafic stream
- ilmenite-bearing stream
- tailings and middlings

## 2) Existing KB mapping
Reusable process/machine/material chain already present:
- processes:
  - `beneficiate_regolith_magnetic_v0`
  - `beneficiation_magnetic_basic_v0`
  - `mineral_processing_basic_v0`
- machines:
  - `screening_equipment`
  - `magnetic_separator_drum_v0`
  - `vibratory_feeder_v0`
  - `electrostatic_separator_v0` (added in result 03)
- materials:
  - `ilmenite_concentrate`
  - `pyroxene_concentrate`
  - `anorthite_ore`
  - `tailings`

Gap:
- no electrostatic beneficiation process ID with explicit split outputs
- no explicit middlings stream item for recycle accounting
- no electrostatic-specific recipe variants for existing concentrate/tailings IDs

## 3) Recommended KB structure for result 04
### Process layer
- `electrostatic_beneficiation_regolith_v0`

### Material layer
- `electrostatic_middlings_v0` (new intermediate stream)

### Recipe layer (electrostatic variants)
- `recipe_ilmenite_concentrate_electrostatic_v0`
- `recipe_pyroxene_concentrate_electrostatic_v0`
- `recipe_tailings_electrostatic_v0`
- `recipe_anorthite_ore_electrostatic_v0`
- `recipe_electrostatic_middlings_v0`

## 4) Process design intent
`electrostatic_beneficiation_regolith_v0` should:
- consume dry feed (`regolith_powder`) as a batch/continuous split operation input
- produce mass-balanced coproduct streams:
  - `anorthite_ore`
  - `pyroxene_concentrate`
  - `ilmenite_concentrate`
  - `electrostatic_middlings_v0`
  - `tailings`
- require explicit machine chain:
  - `electrostatic_separator_v0`
  - `screening_equipment`
  - `magnetic_separator_drum_v0`
  - `vibratory_feeder_v0`
  - `labor_bot_general_v0`

## 5) Intermediate policy justification
`electrostatic_middlings_v0` should be modeled explicitly because:
- report 04 highlights recleaning middlings as a core tuning strategy
- the intermediate can be reused by later optimization loops (grade vs recovery tradeoffs)
- this is a high-value intermediate, not a one-off disposable byproduct

## 6) Conservative-mode compliance notes
- reused existing concentrate/tailings IDs to avoid unnecessary item proliferation
- added only one new stream ID (`electrostatic_middlings_v0`) where explicit reuse value is high
- process is represented once; recipe variants map target outputs without duplicating process definitions

## 7) Validation checklist for result 04 implementation
- `python -m src.cli validate --id process:electrostatic_beneficiation_regolith_v0`
- `python -m src.cli validate --id item:electrostatic_middlings_v0`
- `python -m src.cli validate --id item:ilmenite_concentrate`
- `python -m src.cli validate --id item:pyroxene_concentrate`
- `python -m src.cli validate --id item:tailings`
- full index after updates; only known pre-existing global issues should remain.
