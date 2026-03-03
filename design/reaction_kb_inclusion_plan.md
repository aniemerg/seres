# Reaction Coverage and Inclusion Plan

## Goal
Represent every reaction/group in `design/list_of_reactions.md` in the KB with process-level input/output semantics, while staying consistent with existing schema and Conservative Mode.

Interpretation used here:
- A reaction is considered represented when there is at least one process with materially-equivalent reactants and products.
- Multi-step process blocks are acceptable when the addendum marks a line as shorthand or chemically ambiguous.
- Existing placeholders are reused where sensible, then tightened.

Attribution for source intent: **"My Dastardly Plan to Colonise the Universe" by Alex Ellery**.

## Addendum-Driven Normalization Rules Applied
1. Split ambiguous shorthand reactions into balanced sub-steps when required for closure.
2. Do not encode equations with spectator reagents that cancel on both sides as-is.
3. For oxidation/reduction, explicitly include oxidant/reductant sources (especially O2/H2 on lunar context).
4. Keep long-duration crystallization as unit operations, not single "magic" stoichiometric steps.

## Non-Optional Scope for This Pass
- All listed production chains will be represented, even when alternate chains already exist.
- Existing chain variants remain in KB; new reaction-derived chains are added as additional variants/process routes.
- This plan does not use "only if needed later" gating for listed reactions.

## Intermediate Material Policy for This Pass
- Create explicit intermediate items when they are likely reusable in more than one chain or likely simulation-relevant (e.g., sodium_selenite, nickel_carbonyl intermediates, dimethyldichlorosilane, sodium_silicate).
- Use direct process input->output mapping (no new intermediate item) when an intermediate is highly transient and unlikely to be reused.
- When in doubt, prefer fewer new items unless the intermediate has clear cross-chain utility.

## Catalyst and Unmodified Material Policy
- Per ADR-003 direction: consumed materials and consumables go in `inputs`; reusable equipment goes in `resource_requirements`.
- Catalysts represented as catalyst hardware (reactor bed, cartridge, fixed catalyst module) should be modeled as machine/tool requirements in `resource_requirements`.
- Catalysts represented as charged chemical materials should be modeled in `inputs` with either:
  - equal recycle output if unchanged, or
  - explicit makeup/spent catalyst accounting if degraded.
- Do not model chemical catalyst mass as a one-way consumed input unless degradation is intended.

## ADR-018 Implications for Reaction Inclusion
- Every new reaction process and recipe variant must have resolvable `inputs` and `outputs` (no implicit empty material flow).
- Multi-step reaction chains (especially addendum-normalized splits) should define step-level `inputs`/`outputs` explicitly to avoid inference ambiguity.
- Recipe-level `outputs` must include the recipe `target_item_id` and unit-compatible quantity.
- If a generic/template process is used, mark it `is_template: true` and require explicit step-level material bindings in recipes.
- For chained intermediates, ensure each step output is consumable by the next step with explicit units and conversion-safe item definitions.
- Avoid note-only chemistry where process IO does not reflect the modeled transformation; ADR-018 validation/simulation behavior expects executable material flow.

## Additional ADR Implications (Beyond ADR-018)

### Binding in current repo behavior
- ADR-003 (partially deprecated but active): use `resource_requirements.machine_id` for machine/catalyst hardware requirements; keep material consumption in `inputs`/`outputs`.
- ADR-005 (implemented phase 1): prefer reusable `process_id`-based recipe steps; use inline steps sparingly and only where no reusable process exists.
- ADR-011 (accepted): keep regolith chains location-specific (`regolith_lunar_highlands`, `regolith_lunar_mare`, `regolith_polar_psc`, etc.); avoid reviving generic `regolith_excavated`.
- ADR-019 (implemented): BOM inference is available for machine recipes, but chemistry reaction recipes in this plan should still define explicit I/O for clarity and deterministic validation.
- ADR-023 (implemented): provenance is mass-based and boundary-sourced outputs become in-situ; ensure raw lunar extraction steps are modeled as boundary-style acquisition where appropriate, then propagate through chemical chains.
- Schema baseline (docs/kb_schema_reference + ADR-012/014/016/017 stack): new/updated processes should use current `process_type`, `time_model`, `energy_model`, valid compound units, and conversion-safe `scaling_basis`.

### Directional/watchlist constraints to follow where practical
- ADR-007 (proposed): if any reaction chain intentionally remains import-dependent, prefer explicit import-item modeling (`is_import: true`) over placeholder import processes.
- ADR-009 (proposed, but aligned with current policy docs): avoid placeholder chemistry and generic stock inputs; represent specific materials or explicit imports.
- ADR-020 (proposed): keep step decomposition and intermediate definitions compatible with future step-level orchestration/resource accounting (avoid black-box mega-steps when intermediates matter).
- ADR-024 (proposed): if mass-balance closure needs a sink, prefer `waste`/scrap-style byproduct handling at step level (not recipe-level outputs), consistent with current scrap conventions.

## Existing KB Assets (High Leverage)
- Water electrolysis: `kb/processes/water_electrolysis_v0.yaml`
- Ilmenite/Fe-Ti routes: `iron_reduction_from_ilmenite_v0`, `ulvospinel_hydrogen_reduction_v0`, `metalysis_ffc_reduction_v0`
- Carbonyl family (partial): `iron_carbonyl_synthesis_v0`, `iron_carbonyl_process_v0`, `mond_carbonyl_process_nickel_v0`, `dicobalt_octacarbonyl_synthesis_v0`, `cobalt_carbonyl_process_v0`
- Sulfur/acid routes: `claus_process_sulfur_recovery_v0`, `sulfuric_acid_contact_process_v0`, `ostwald_process_nitric_acid_v0`, `hcl_generation_from_nacl_v0`
- Anorthite/calcination routes: `anorthite_carbothermal_reduction_v0`, `aluminum_chloride_hydrate_formation_v0`, `aluminum_chloride_calcination_v0`
- Carbon/C1 chemistry: `sabatier_reaction_complete_v0`, `syngas_generation_steam_reforming_v0`, `methanol_synthesis_from_syngas_v0`, `methane_pyrolysis_v0`
- Silicone chain (placeholder-heavy): `methylchloride_synthesis_v0`, `rochow_process_reactor_v0`, `silicone_precursor_synthesis_v0`, `silicone_polymer_synthesis_v0`
- Salts/quartz: `solvay_process_sodium_carbonate_v0`, `nacl_regeneration_from_nano3_v0`, `quartz_crystal_synthesis_v0`

## Reaction-by-Reaction Coverage and Planned Changes

### 1) Ilmenite / Fe-Ti / magnetics
1. `FeO + H2O -> ferrofluidic sealing`
- Current: Not represented.
- Plan: Add a process block for ferrofluid precursor production and seal formulation.
- Conservative mapping: avoid creating a full ferrofluid machine stack; model as chemical mixing + separation.
- Likely additions: `ferrofluid_slurry_v0` material and `ferrofluid_sealant_v0` material/process.

2. `FeTiO3 + H2 -> TiO2 + H2O + Fe`
- Current: Partially represented by `ulvospinel_hydrogen_reduction_v0` and `iron_reduction_from_ilmenite_v0`.
- Gap: `iron_reduction_from_ilmenite_v0` currently outputs `oxygen_gas` instead of `water` for H2 reduction pathway.
- Plan: Add/adjust a hydrogen-ilmenite reduction process with explicit `water` byproduct (or revise `iron_reduction_from_ilmenite_v0` if used as that pathway).

3. `2H2O -> 2H2 + O2`
- Current: Represented by `water_electrolysis_v0` with `water` input and `hydrogen_gas`/`oxygen_gas` outputs.
- Plan: Keep.

4. `2Fe + 1.5O2 -> Fe2O3 /(Fe2O3.CoO)`
- Current: Not explicitly represented as a standalone process.
- Plan: Add explicit iron oxidation process to hematite (`iron_to_hematite_oxidation_v0`), then ferrite precursor process can consume Fe2O3 and cobalt oxide/cobalt feed.

5. `3Fe2O3 + H2 <-> Fe3O4 + H2O`
- Current: Not explicitly represented.
- Plan: Add `hematite_to_magnetite_h2_reduction_v0` and reverse oxidation variant (or one reversible process with clear direction in recipes).

6. `4Fe2O3 + Fe <-> 3Fe3O4`
- Current: Not represented.
- Plan: Add `hematite_iron_comproportionation_to_magnetite_v0`.

### 2) W inclusions
7. `W inclusions -> thermionic cathodic material`
- Current: Partially represented by `tungsten_density_separation_v0` and tungsten downstream recipes.
- Gap: tungsten chain still depends on imported `tungsten_powder`; extraction path does not feed final thermionic cathode materials directly.
- Plan:
  - Add process: `tungsten_concentrate_to_tungsten_powder_v0` or directly `tungsten_concentrate_refining_v0`.
  - Repoint tungsten recipes from imported `tungsten_powder` to local tungsten pathway.
  - Keep existing use in thermionic cathode recipes.

### 3) Carbonyl process / Ni-Fe meteorites / alloy feedstocks
8. `Fe(CO)5 <-> 5CO + Fe`
- Current: Represented in two-process form (`iron_carbonyl_synthesis_v0` + `iron_carbonyl_process_v0`).
- Plan: Tighten stoichiometric quantities and ensure CO recycle is explicit in outputs where decomposition occurs.

9. `Ni(CO)4 <-> 4CO + Ni`
- Current: Only partially represented (`mond_carbonyl_process_nickel_v0` models Ni purification without explicit Ni(CO)4 intermediate item).
- Plan: Add explicit intermediate process pair (formation/decomposition) or update Mond process to expose intermediate flow in step structure.

10. `Co2(CO)8 <-> 8CO + 2Co`
- Current: Partial (`dicobalt_octacarbonyl_synthesis_v0`, `cobalt_carbonyl_process_v0`) but decomposition to cobalt metal is not explicit.
- Plan: Add decomposition process yielding `cobalt_metal_pure` + `carbon_monoxide`.

11. `(S catalyst) alloying context`
- Current: Sulfur exists and Claus/H2S loops exist in part.
- Plan: Represent as catalyst requirement in carbonyl/alloy processes (`resource_requirements` or catalytic input with recycle output) rather than consumable bulk feed.

### 4) Troilite / sulfur / selenium chain
12. `4FeS + 7O2 -> 2Fe2O3 + 4SO2`
- Current: Represented in `claus_process_sulfur_recovery_v0` notes and mass logic.
- Plan: Keep and add explicit stage-1 roasting process for direct reaction representation.

13. `SO2 + H2S -> 3S + H2O`
- Current: Represented in Claus process stage 2.
- Plan: Keep and add standalone `claus_stage2_v0` process for direct reaction representation.

14. `FeSe + Na2CO3 + 1.5O2 -> FeO + Na2SeO3 + CO2`
- Current: Not explicitly represented.
- Plan: Add selenium roast/oxidation process with explicit `sodium_selenite` intermediate.
- Needed items likely: `iron_selenide` (or `fese_feed` alias), `sodium_selenite`.

15. Original line replaced per addendum:
- `Na2SeO3 + H2SO4 -> H2SeO3 + Na2SO4`
- `H2SeO3 + 2H2 -> Se + 3H2O` OR `H2SeO3 + 2SO2 + H2O -> Se + 2H2SO4`
- Current: Not explicit (selenium extraction is generic).
- Plan: Implement as 2-step selenium branch; pick H2 reduction as default, keep SO2 variant as alternate recipe.
- Product split: keep `selenium_refined` and add `selenium_photosensitive_v0` as a distinct output grade for optics/sensor chain use.

16. `Na2O + H2O -> 2NaOH`
- Current: Not explicit as sodium-oxide hydration.
- Existing nearby: `chloralkali_electrolysis_v0` produces `sodium_hydroxide` by different route.
- Plan: Add explicit sodium-oxide hydration process and recipe variant so this listed chain is represented directly.

17. `NaOH + HCl -> NaCl + H2O`
- Current: Represented conceptually by `naoh_hcl_salt_synthesis_v0` (produces `salt_contingency_nacl`).
- Gap: product item should align with mainstream salt item (`sodium_chloride`) unless deliberate contingency separation is needed.
- Plan: add normalized variant producing `sodium_chloride` directly or map contingency salt into sodium_chloride in downstream recipes.

### 5) Orthoclase -> illite/kaolinite -> binders/porcelain + nitrate swap
18. `3KAlSi3O8 + 2HCl + 12H2O -> illite + H4SiO4 + KCl`
- Current: Not represented explicitly.
- Plan: Add orthoclase weathering process.
- Needed items: `orthoclase_feldspar`, `illite_clay`, `potassium_chloride`.
- Reuse: existing `silicic_acid` item.

19. `H4SiO4 -> SiO2 + H2O`
- Current: Not explicit.
- Plan: Add silicic acid precipitation/dehydration process to `silica_purified` or `fused_silica` precursor.

20. `illite -> kaolinite ...`
- Current: Not represented; `kaolinite_clay` exists but is import placeholder and appears to reference missing recipe file.
- Plan: Add local kaolinite synthesis process chain and replace import-only placeholder behavior.

21. `KCl + NaNO3 -> NaCl + KNO3`
- Current: Intended by `nacl_regeneration_from_nano3_v0` but currently uses `sodium_chloride` as reactant slot where KCl should be.
- Plan: Fix process/recipe inputs to use `potassium_chloride`; keep `potassium_nitrate` output.

### 6) Anorthite routes
22. `CaAl2SiO8 + 4C -> CO + CaO + Al2O3 + 2Si`
- Current: Represented by `anorthite_carbothermal_reduction_v0` (modeled with `4CO`, consistent with balancing).
- Plan: Keep; no new entity required.

23. `CaO + H2O -> Ca(OH)2`
- Current: Represented at recipe-step level via `recipe_calcium_hydroxide_v0` using `chemical_mixing_basic_v0`.
- Plan: Keep existing route and add a named dedicated process variant for direct reaction traceability.

24. `Ca(OH)2 + CO2 -> CaCO3 + H2O`
- Current: Represented by `calcium_carbonate_from_hydroxide_v0`.
- Plan: Keep.

25. `CaAl2SiO8 + HCl... -> CaCl2 + AlCl3.6H2O + SiO2`
- Current: Partially represented via HCl regolith treatment/leaching and Al chloride downstream routes; not explicit as one balanced process.
- Plan: Add explicit `anorthite_hcl_leach_to_chlorides_v0` with intermediate outputs, then reuse existing chloride hydration/calcination.

26. `AlCl3.6H2O -> Al(OH)3 + 3HCl + H2O`
- Current: Not represented exactly.
- Existing: `aluminum_chloride_calcination_v0` goes directly to `alumina_powder` + HCl + water.
- Plan: Add explicit hydrate->hydroxide step as a separate variant chain while keeping current direct calcination route.

27. `Al(OH)3 -> Al2O3 + 3H2O`
- Current: Not explicit.
- Plan: Add explicit hydroxide calcination step; wire it to the explicit 26-chain.

28. `2Al + Fe2O3 -> 2Fe + Al2O3` (thermite)
- Current: Not explicit.
- Plan: Add thermite reduction as an explicit alternate reduction chain.

### 7) Olivine / fayalite / Mg binders
29. `Mg2SiO4 + 2CH4 -> 2CO + H2 + 2MgO + Si`
- Current: Not exact; closest is `carbothermal_methane_reduction_pyroxene_v0` (MgSiO3 basis).
- Plan: Add forsterite-specific methane reduction variant reusing same reactor/machine pattern.

30. `CO + 0.5O2 -> CO2`
- Current: Represented by `carbon_monoxide_oxidation_v0`.
- Plan: Keep.

31. `CO2 + 4H2 -> CH4 + 2H2O`
- Current: Represented by `sabatier_reaction_complete_v0`.
- Plan: Keep.

32. `CH4 -> C + 2H2`
- Current: Represented by `methane_pyrolysis_v0` (carbon as `carbon_anode_material`).
- Plan: Keep and map product as acceptable carbon form for steel route where needed.

33. Problematic hydration line per addendum.
- Current: Related `olivine_hydration_v0` exists but serves fayalite->magnetite pathway.
- Plan: Do not encode hydration-to-MgO as direct balanced route. Use reaction 29 / electrochemical routes for MgO supply.

34. `MgO + HCl -> MgCl2 + H2O`
- Current: Represented by `magnesium_chloride_from_mgo_v0` and `recipe_magnesium_chloride_v0`.
- Plan: Keep.

35. Fayalite->magnetite transformation
- Current: Represented in `olivine_hydration_v0` with non-canceling water and H2 output.
- Plan: Keep but annotate oxidant/redox assumptions to align with addendum guidance.

### 8) Pyroxene
36. `augite + HCl + H2O -> montmorillonite + ...`
- Current: Not explicit; closest material analogue is `bentonite` (montmorillonite) import placeholder.
- Plan: Add process converting `pyroxene_concentrate` (or new `augite_concentrate`) to bentonite/montmorillonite plus soluble salts.

37. `6MgSiO3 + H2O -> serpentine + talc`
- Current: Partial: `talc` exists with placeholder hydrothermal recipe; `serpentinite` exists as import placeholder.
- Plan: Add explicit enstatite hydrothermal process producing both `serpentinite` and `talc` (and water accounting).

### 9) C-type volatiles
38. `CH4 + H2 -> CO + 3H2` (as listed)
- Current: Not represented as written.
- Issue: chemically inconsistent as written; likely intended steam reforming (`CH4 + H2O -> CO + 3H2`).
- Plan: map to existing steam reforming pathway and annotate this normalization choice.

39. `CO + 2H2 -> CH3OH`
- Current: Represented by `methanol_synthesis_from_syngas_v0`.
- Plan: Keep.

40. `CH3OH + HCl -> CH3Cl + H2O`
- Current: Not represented (current methyl chloride synthesis uses methane + chlorine).
- Plan: Add methanol chlorination variant process and recipe.

41. `CH3Cl + Si -> (CH3)2SiCl2`
- Current: Partial; `rochow_process_reactor_v0` outputs methyl_trichlorosilane, not dimethyldichlorosilane.
- Plan: Add or adjust Rochow product slate with a distinct `dimethyldichlorosilane` item for this path.

42. `(CH3)2SiCl2 + nH2O -> ((CH3)2SiO)n + 2nHCl`
- Current: Not explicit; silicone precursor/polymer steps are generic placeholders.
- Plan: Add hydrolysis+polycondensation process that outputs silicone polymer and recycled HCl.

43. `N2 + 3H2 -> 2NH3`
- Current: Represented by `nitrogen_fixation_haber_bosch_v0`.
- Plan: Keep.

44. `4NH3 + 5O2 -> 4NO + 6H2O`
- Current: Represented inside `ostwald_process_nitric_acid_v0` stage notes.
- Plan: Keep aggregated Ostwald path and add explicit stage process for ammonia oxidation.

45. Ostwald absorption line
- Current: Aggregated in Ostwald process notes.
- Plan: Add explicit NO oxidation and NO2 absorption stage processes with NO recycle.

46. `2SO2 + O2 <-> 2SO3`
- Current: Represented in `sulfuric_acid_contact_process_v0` stage notes and batch I/O.
- Plan: Keep.

47. `SO3 + H2O -> H2SO4`
- Current: Represented in same contact process.
- Plan: Keep.

### 10) C-type salts
48. `2NaCl + CaCO3 <-> Na2CO3 + CaCl2`
- Current: Represented by `solvay_process_sodium_carbonate_v0`.
- Plan: Keep.

49. `Na2CO3 + SiO2 <-> Na2SiO3 + CO2` (transport chemistry)
- Current: Not explicit.
- Plan: Add sodium silicate transport process and item (`sodium_silicate_solution` or `sodium_silicate`), keep quartz crystallization as downstream operation.

50. `CaCO3 -> CaO + CO2`
- Current: Implied in notes and generic CaO extraction, not explicit as dedicated process.
- Plan: Add dedicated `calcium_carbonate_calcination_v0` process.

51. `NaCl + HNO3 -> HCl + NaNO3`
- Current: Represented by `hcl_generation_from_nacl_v0`.
- Plan: Keep.

## Cross-Cutting Data/Schema Cleanup Needed for This Plan
1. Resolve item-ID duplication/inconsistency:
- `hydrogen_gas` vs `hydrogen_gas_v0`
- `carbon_monoxide` vs `carbon_monoxide_gas*`
- `hydrogen_chloride` vs `hydrochloric_acid` vs `hcl`
2. Fix existing inaccurate reagent mapping:
- `nacl_regeneration_from_nano3_v0` should consume `potassium_chloride`, not `sodium_chloride`.
3. Replace import placeholders where these reactions need local closure:
- `kaolinite_clay`, `serpentinite`, possibly `bentonite`, `tungsten_powder`.
4. Tighten placeholder processes in ferrite/carbonyl/silicone chains where reaction-level coverage is required.

## ID Stability and Upgrade Handling
- Current intent: no forced rename of stable existing IDs in this reaction pass.
- Planned approach: avoid destructive ID renames in this phase whenever possible.
- Where canonicalization is needed, keep deprecated IDs in KB entries with explicit upgrade metadata (`deprecated`, `upgraded_to`, `upgrade_note`, `upgrade_since`) per ADR-025.
- Deprecated/upgraded IDs are not treated as silently compatible for execution.
- Simulator behavior is fail-fast on deprecated ID references (including runbooks/saved simulations): execution stops with structured upgrade guidance.
- No automatic migration/rewrite tool is planned; users/agents must investigate and update references intentionally.

## Proposed Implementation Sequence (No Priority Tiering, Full Coverage Pass)
1. Normalize IDs and aliases used by this chemistry domain (chlorides/nitrates/gases).
2. Add missing explicit reaction processes where no equivalent exists (notably 1, 4, 5, 6, 14, 15 split, 18, 19, 20, 29, 36, 37, 40, 41, 42, 49, 50).
3. Update partially represented processes to match intended chemistry and addendum constraints.
4. Connect recipes so new processes are reachable from existing raw-material chains.
5. Validate each touched process/recipe/item with `python -m src.cli validate --id ...` and confirm queue/validation stability.

## Machine Mapping for Planned New Processes
Planned `resource_requirements` for each new process (reusing existing machine IDs where possible):

| Planned process id | Primary machine requirements |
|---|---|
| `ferrofluid_precursor_synthesis_v0` | `generic_chemical_reactor_v0`, `labor_bot_general_v0` |
| `ferrofluid_seal_formulation_v0` | `chemical_reactor_basic`, `labor_bot_general_v0` |
| `ilmenite_hydrogen_reduction_explicit_v0` | `reduction_furnace_v0`, `gas_handling_loop_v0`, `labor_bot_general_v0` |
| `iron_to_hematite_oxidation_v0` | `furnace_basic`, `gas_handling_loop_v0`, `labor_bot_general_v0` |
| `hematite_to_magnetite_h2_reduction_v0` | `generic_chemical_reactor_v0`, `gas_handling_loop_v0`, `labor_bot_general_v0` |
| `hematite_iron_comproportionation_to_magnetite_v0` | `furnace_high_temp`, `labor_bot_general_v0` |
| `tungsten_concentrate_refining_v0` | `generic_chemical_reactor_v0`, `packed_bed_distillation_v0`, `labor_bot_general_v0` |
| `cobalt_carbonyl_decomposition_to_metal_v0` | `generic_chemical_reactor_v0`, `gas_handling_loop_v0`, `labor_bot_general_v0` |
| `troilite_roasting_stage1_v0` | `roasting_furnace_v0`, `gas_handling_loop_v0`, `labor_bot_general_v0` |
| `claus_stage2_sulfur_recovery_v0` | `generic_chemical_reactor_v0`, `catalyst_bed_assembly`, `labor_bot_general_v0` |
| `fese_roast_to_sodium_selenite_v0` | `roasting_furnace_v0`, `generic_chemical_reactor_v0`, `labor_bot_general_v0` |
| `selenite_acidification_v0` | `acid_reactor_v0`, `labor_bot_general_v0` |
| `selenous_acid_h2_reduction_v0` | `generic_chemical_reactor_v0`, `gas_handling_loop_v0`, `labor_bot_general_v0` |
| `selenous_acid_so2_reduction_v0` | `generic_chemical_reactor_v0`, `gas_handling_loop_v0`, `labor_bot_general_v0` |
| `sodium_oxide_hydration_v0` | `chemical_reactor_basic`, `labor_bot_general_v0` |
| `naoh_hcl_neutralization_to_nacl_v0` | `chemical_reactor_basic`, `labor_bot_general_v0` |
| `orthoclase_hcl_weathering_to_illite_v0` | `acid_reactor_v0`, `packed_bed_distillation_v0`, `labor_bot_general_v0` |
| `silicic_acid_precipitation_to_silica_v0` | `crystallization_unit_v0`, `packed_bed_distillation_v0`, `labor_bot_general_v0` |
| `illite_to_kaolinite_conversion_v0` | `generic_chemical_reactor_v0`, `acid_reactor_v0`, `labor_bot_general_v0` |
| `anorthite_hcl_leach_to_chlorides_v0` | `acid_reactor_v0`, `packed_bed_distillation_v0`, `labor_bot_general_v0` |
| `aluminum_chloride_hydrate_to_aluminum_hydroxide_v0` | `generic_chemical_reactor_v0`, `packed_bed_distillation_v0`, `labor_bot_general_v0` |
| `aluminum_hydroxide_calcination_v0` | `furnace_basic`, `gas_handling_loop_v0`, `labor_bot_general_v0` |
| `thermite_reduction_iron_from_hematite_v0` | `furnace_high_temp`, `labor_bot_general_v0` |
| `forsterite_methane_reduction_v0` | `high_temp_furnace_v0`, `gas_handling_loop_v0`, `labor_bot_general_v0` |
| `augite_hcl_to_montmorillonite_v0` | `acid_reactor_v0`, `generic_chemical_reactor_v0`, `labor_bot_general_v0` |
| `enstatite_hydrothermal_serpentine_talc_v0` | `pressure_vessel_steel`, `generic_chemical_reactor_v0`, `labor_bot_general_v0` |
| `methanol_hcl_to_methyl_chloride_v0` | `acid_reactor_v0`, `gas_handling_loop_v0`, `labor_bot_general_v0` |
| `rochow_dimethyldichlorosilane_variant_v0` | `chemical_reactor_basic`, `gas_handling_loop_v0`, `labor_bot_general_v0` |
| `dimethyldichlorosilane_hydrolysis_polycondensation_v0` | `chemical_reactor_basic`, `packed_bed_distillation_v0`, `labor_bot_general_v0` |
| `ostwald_stage1_ammonia_oxidation_v0` | `chemical_reactor_basic`, `catalyst_bed_assembly`, `labor_bot_general_v0` |
| `ostwald_stage2_no_oxidation_v0` | `chemical_reactor_basic`, `gas_handling_loop_v0`, `labor_bot_general_v0` |
| `ostwald_stage3_no2_absorption_v0` | `packed_bed_distillation_v0`, `generic_chemical_reactor_v0`, `labor_bot_general_v0` |
| `sodium_silicate_transport_equilibrium_v0` | `generic_chemical_reactor_v0`, `packed_bed_distillation_v0`, `labor_bot_general_v0` |
| `calcium_carbonate_calcination_v0` | `kiln_ceramic`, `gas_handling_loop_v0`, `labor_bot_general_v0` |

## Key Risks to Resolve Before KB Edits
- Several current processes encode chemistry mainly in notes while I/O is coarse placeholders.
- Some reactions in list require introducing intermediates not currently in KB (e.g., sodium selenite, orthoclase, potassium chloride, dimethyldichlorosilane).
- Enforcing strict reaction-level representation may increase item/process count; reuse and adaptation should be favored when functionally equivalent.

## Practical Mapping Notes for Next Editing Stage
- For catalyst handling (S catalyst, NH3 oxidation catalyst), use catalyst as process requirement or recycled catalytic input/output, not one-way consumable mass.
- For W inclusions, keep extraction as beneficiation + purification chain from `nife_alloy_byproduct`, then retire direct import dependency of `tungsten_powder` in thermionic paths.
- For addendum-corrected selenium, use two-step acidification/reduction process with explicit reductant source (default H2 route).

## Implementation Status (2026-03-03)
- Completed direct KB inclusion for all reaction groups in `design/list_of_reactions.md` using existing plus new process variants.
- Added explicit process/recipe coverage for missing chains:
  - Ferrofluid precursor + seal formulation (`ferrofluid_precursor_synthesis_v0`, `ferrofluid_seal_formulation_v0`).
  - Tungsten inclusion refinement to local `tungsten_powder` (`tungsten_concentrate_refining_v0`, `recipe_tungsten_powder_v0`).
  - Carbonyl explicit stages (`nickel_carbonyl_synthesis_v0`, `nickel_carbonyl_decomposition_v0`, `cobalt_carbonyl_decomposition_to_metal_v0`) with sulfur catalyst modeled as recycled material in nickel synthesis.
  - Claus split stages (`troilite_roasting_stage1_v0`, `claus_stage2_sulfur_recovery_v0`).
  - Orthoclase/illite/kaolinite chain, selenium split chain, and anorthite explicit subchain from prior chunk.
  - Forsterite, augite, and enstatite explicit routes (`forsterite_methane_reduction_v0`, `augite_hcl_to_montmorillonite_v0`, `enstatite_hydrothermal_serpentine_talc_v0`).
  - Methanol->methyl chloride, Rochow dimethyldichlorosilane, and silicone hydrolysis/polycondensation (`methanol_hcl_to_methyl_chloride_v0`, `rochow_dimethyldichlorosilane_variant_v0`, `dimethyldichlorosilane_hydrolysis_polycondensation_v0`).
  - Ostwald staged intermediates (`ostwald_stage1_ammonia_oxidation_v0`, `ostwald_stage2_no_oxidation_v0`, `ostwald_stage3_no2_absorption_v0`) and sodium silicate transport chemistry (`sodium_silicate_transport_equilibrium_v0`).
- Addendum-driven normalization applied:
  - Selenite -> Se represented as acidification + reduction stages.
  - Quartz-related sodium silicate chemistry represented as transport/equilibrium step, separate from crystallization.
  - C-type reaction 38 mapped to existing steam-reforming representation (`syngas_generation_steam_reforming_v0`) per addendum normalization.
- Index status after these edits: no new validation failures introduced; repository still has one pre-existing unrelated error (`recipe_excavator_basic_v0` mass imbalance).
