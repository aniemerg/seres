# Machine Review Decision Checklist

This checklist is the single source of truth for decisions coming out of the machine reality reviews in `research/machines/`.

In this repo, `machine` / `machine_id` is a broad reusable process resource convention. Checklist actions should distinguish standalone equipment, reusable tooling, instruments, consumables, infrastructure, stations, subsystems, and placeholders without assuming non-equipment resources are invalid.

Instructions for reviewers:

- Check only the decisions you want implemented.
- For `Choose one` groups, check at most one option.
- For `Choose all that apply` groups, multiple checked options are allowed.
- Use each `custom_user_instruction` checkbox for freeform instructions not covered by the listed options.
- A later agent should enqueue KB edit tasks only from checked decisions.
- If multiple options in a `Choose one` group are checked, the enqueue agent must stop and ask for clarification.

See `research/machines_analysis/machine_review_checklist_plan.md` for the full generation and enqueue-safety plan.

## Progress

- Last reviewed machine ID: `work_rest_adjustable`
- Total machine review files: 117
- Checklist status: complete

## anvil_or_die_set

Source review: `research/machines/anvil_or_die_set.md`
KB item: `kb/items/parts/anvil_or_die_set.yaml`
Decision status: unresolved

Summary: Real reusable forging tooling. It provides passive anvil/die surfaces for forging, but not heat or force. The review flags likely overlap with `anvil_and_die_set` and `anvil_block_basic`, and notes that the current recipe may be self-referential because it uses forging processes that require the item being made.

### Primary Path: Choose One

- [ ] `anvil_or_die_set.keep_as_forging_tooling_resource`
  Action: Keep `anvil_or_die_set` as the canonical reusable forging tooling resource and clarify that it is not standalone powered equipment.
  Action type: `note_cleanup`
  Queue task if checked: Update `kb/items/parts/anvil_or_die_set.yaml` notes/capabilities as needed to describe interchangeable forging tooling used with `induction_forge_v0`, `power_hammer_or_press`, or forging presses. Preserve process requirements that need forging tooling. Source review: `research/machines/anvil_or_die_set.md`.
  Notes: Do not remove the item from forging processes just because it is tooling; it is still a valid reusable process resource.
  Freeform instructions:
  > 

- [ ] `anvil_or_die_set.consolidate_with_anvil_and_die_set`
  Action: Treat `anvil_or_die_set` and `anvil_and_die_set` as duplicates or near-duplicates and choose one canonical item.
  Action type: `dedupe_or_consolidation`
  Queue task if checked: Inspect `anvil_or_die_set`, `anvil_and_die_set`, `anvil_block_basic`, and forging process references. Propose and apply a Conservative Mode consolidation to one canonical forging-tooling resource where safe, preserving `anvil_block_basic` if it represents the heavy fixed anvil mass. Source review: `research/machines/anvil_or_die_set.md`.
  Notes: If references imply different scales or functions, do not merge blindly; document the distinction.
  Freeform instructions:
  > 

- [ ] `anvil_or_die_set.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `anvil_or_die_set` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `anvil_or_die_set.fix_self_referential_recipe`
  Action: Replace the suspect self-referential manufacturing route with a cast/machined/heat-treated tooling route.
  Action type: `bom_or_recipe_update`
  Queue task if checked: Inspect the recipe(s) for `anvil_or_die_set` and remove any circular dependency where forging processes require `anvil_or_die_set` to produce `anvil_or_die_set`. Prefer a seed route using steel stock or casting, machining/grinding, heat treatment, and inspection. Source review: `research/machines/anvil_or_die_set.md`.
  Notes: Split implementation into smaller tasks if recipe changes touch unrelated forging infrastructure.
  Freeform instructions:
  > 

- [ ] `anvil_or_die_set.decide_open_vs_impression_die_scope`
  Action: Decide whether this item covers only open-die tooling or also part-specific impression dies.
  Action type: `note_cleanup`
  Queue task if checked: Review forging processes using `anvil_or_die_set` and update notes or process requirements to distinguish general open-die tooling from closed/impression dies where part geometry requires dedicated tooling. Source review: `research/machines/anvil_or_die_set.md`.
  Notes: This can remain a documentation/scoping task unless specific process references need migration.
  Freeform instructions:
  > 

- [ ] `anvil_or_die_set.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `anvil_or_die_set` using the freeform instructions below. Source review: `research/machines/anvil_or_die_set.md`.
  Freeform instructions:
  > 

## assembly_tools_basic

Source review: `research/machines/assembly_tools_basic.md`
KB item: `kb/items/machines/assembly_tools_basic.yaml`
Decision status: unresolved

Summary: Real reusable assembly resource. It may mean a portable basic tool kit, an assembly workstation/tool bundle, or an instrumented guided assembly station. The review warns that it overlaps with `hand_tools_basic` and should not become a catch-all substitute for specialty tools.

### Primary Scope: Choose One

- [ ] `assembly_tools_basic.keep_as_assembly_workstation`
  Action: Keep `assembly_tools_basic` as a basic assembly workstation and tool set.
  Action type: `note_cleanup`
  Queue task if checked: Update `kb/items/machines/assembly_tools_basic.yaml` wording to describe a reusable basic assembly workstation/tool set with bench/station, hand tools, drivers, clamps/fixtures, bins, power, ESD provisions where relevant, and basic guided-assembly support if already implied by the BOM. Source review: `research/machines/assembly_tools_basic.md`.
  Notes: This keeps it distinct from a portable hand-tool kit while preserving its broad assembly-resource role.
  Freeform instructions:
  > 

- [ ] `assembly_tools_basic.consolidate_with_hand_tools_basic`
  Action: Consolidate or narrow `assembly_tools_basic` if it is intended only as a basic hand-tool kit.
  Action type: `dedupe_or_consolidation`
  Queue task if checked: Compare `assembly_tools_basic`, `hand_tools_basic`, `hand_tools_mechanical`, and `hand_tools_electrical`. If `assembly_tools_basic` is only portable hand tools, migrate or consolidate references under the appropriate hand-tool resource. Source review: `research/machines/assembly_tools_basic.md`.
  Notes: Stop if process references depend on workstation/station semantics rather than portable tools.
  Freeform instructions:
  > 

- [ ] `assembly_tools_basic.split_mechanical_electrical_assembly_resources`
  Action: Split or scope mechanical assembly and electronics/ESD assembly resources separately.
  Action type: `split_item`
  Queue task if checked: Review process references to `assembly_tools_basic` and decide whether electronics/ESD work, torque-controlled mechanical assembly, PCB work, and general hand assembly should use separate existing or new reusable resources. Source review: `research/machines/assembly_tools_basic.md`.
  Notes: Use this only if current references are too broad for one resource; otherwise prefer note cleanup.
  Freeform instructions:
  > 

- [ ] `assembly_tools_basic.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `assembly_tools_basic` from this review.
  Freeform instructions:
  > 

### Guardrails and Additions: Choose All That Apply

- [ ] `assembly_tools_basic.add_specialty_tooling_guardrail`
  Action: Add notes that `assembly_tools_basic` does not replace specialty tooling.
  Action type: `note_cleanup`
  Queue task if checked: Update notes or related process guidance to state that crimping, hydraulic assembly, precision bearing fits, PCB rework, welding, calibrated torque work, and similar specialty operations should still require dedicated tools/resources where modeled. Source review: `research/machines/assembly_tools_basic.md`.
  Notes: This is compatible with keeping the item broad.
  Freeform instructions:
  > 

- [ ] `assembly_tools_basic.add_calibrated_torque_tooling_requirement`
  Action: Decide how calibrated torque tools are represented.
  Action type: `process_requirement_update`
  Queue task if checked: Inspect assembly processes where torque control matters and decide whether calibrated torque tools should be included in `assembly_tools_basic`, split into a separate reusable resource, or included in `measurement_equipment`. Source review: `research/machines/assembly_tools_basic.md`.
  Notes: Treat this as a KB edit task; split into smaller process tasks if many unrelated references are affected.
  Freeform instructions:
  > 

- [ ] `assembly_tools_basic.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `assembly_tools_basic` using the freeform instructions below. Source review: `research/machines/assembly_tools_basic.md`.
  Freeform instructions:
  > 

## ball_mill_v0

Source review: `research/machines/ball_mill_v0.md`
KB item: `kb/items/machines/ball_mill_v0.yaml`
Decision status: unresolved

Summary: Real medium-scale rotary powder milling machine. The review recommends keeping it distinct from crushers, CNC mills, surface grinders, powder mixers, and grinding wheels. Main fixes are media/tooling requirements and process-scoping details.

### Primary Path: Choose One

- [ ] `ball_mill_v0.keep_and_refine_scope`
  Action: Keep `ball_mill_v0` and clarify it as a rotary ball mill for wet/dry bulk comminution and powder homogenization.
  Action type: `note_cleanup`
  Queue task if checked: Update `kb/items/machines/ball_mill_v0.yaml` notes/capabilities as needed to define it as a rotary ball mill for bulk comminution/powder homogenization, not a crusher, CNC mill, surface grinder, or blending-only mixer. Source review: `research/machines/ball_mill_v0.md`.
  Notes: This is the review's default recommendation.
  Freeform instructions:
  > 

- [ ] `ball_mill_v0.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `ball_mill_v0` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `ball_mill_v0.add_grinding_media_requirement`
  Action: Add grinding media as explicit tooling/consumable inventory for ball milling.
  Action type: `consumable_or_tooling_modeling`
  Queue task if checked: Inspect `ball_mill_v0` BOM and ball-milling process requirements. Add or require appropriate grinding media such as `grinding_media_steel` or `grinding_media_alumina_v0` where the KB can model it without breaking schema expectations. Source review: `research/machines/ball_mill_v0.md`.
  Notes: A ball mill without media cannot mill. Treat media as reusable/wearing tooling or consumable inventory, depending on existing KB conventions.
  Freeform instructions:
  > 

- [ ] `ball_mill_v0.add_process_guardrails`
  Action: Add guidance that ball mills are downstream of crushing and not the default for blending-only steps.
  Action type: `process_requirement_update`
  Queue task if checked: Review ball-milling and powder-preparation process references. Ensure rock/coarse feed has crushing upstream where needed, and use `powder_mixer` rather than `ball_mill_v0` for blending-only operations without size reduction. Source review: `research/machines/ball_mill_v0.md`.
  Notes: Split into smaller tasks if many unrelated recipes/processes need migration.
  Freeform instructions:
  > 

- [ ] `ball_mill_v0.model_dust_screening_wear_contamination`
  Action: Add realism notes or requirements for dust/slurry handling, screening/classification, liner wear, and media contamination.
  Action type: `process_requirement_update`
  Queue task if checked: Inspect regolith, ceramic, graphite, and metal powder workflows using `ball_mill_v0`. Add notes or requirements for dust collection or wet slurry handling, downstream screening/classification, liner wear, and media contamination where process realism depends on it. Source review: `research/machines/ball_mill_v0.md`.
  Notes: This may be a broad design cleanup; split implementation by process family if needed.
  Freeform instructions:
  > 

- [ ] `ball_mill_v0.evaluate_reactive_powder_handling`
  Action: Decide whether reactive metal powder milling needs inert atmosphere or wet milling assumptions.
  Action type: `research_or_design_followup`
  Queue task if checked: Create a KB design/edit task to review metal powder processes using `ball_mill_v0` and decide whether inert atmosphere, wet milling, dust explosion controls, or alternate milling equipment should be modeled. Source review: `research/machines/ball_mill_v0.md`.
  Notes: Use this for safety/process realism; it may require design judgment before direct YAML edits.
  Freeform instructions:
  > 

- [ ] `ball_mill_v0.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `ball_mill_v0` using the freeform instructions below. Source review: `research/machines/ball_mill_v0.md`.
  Freeform instructions:
  > 

## blast_furnace_or_smelter

Source review: `research/machines/blast_furnace_or_smelter.md`
KB item: `kb/items/machines/blast_furnace_or_smelter.yaml`
Decision status: unresolved

Summary: Real smelting/reduction equipment category, but the current "blast furnace or smelter" name conflates blast furnaces, cupolas, direct-reduction/bloomery furnaces, induction furnaces, electric arc furnaces, crucible furnaces, and generic smelters. The current 5000 kg item is plausible as a compact smelter, not a full industrial blast furnace.

### Primary Path: Choose One

- [ ] `blast_furnace_or_smelter.keep_temporary_coarse_smelter`
  Action: Keep the item as a temporary coarse smelting resource and clarify its limits.
  Action type: `note_cleanup`
  Queue task if checked: Update `kb/items/machines/blast_furnace_or_smelter.yaml` notes to state that this is a compact coarse smelting/reduction furnace abstraction, not a universal furnace for all metals and feedstocks. Source review: `research/machines/blast_furnace_or_smelter.md`.
  Notes: Use this if the KB is not ready to split smelting equipment yet.
  Freeform instructions:
  > 

- [ ] `blast_furnace_or_smelter.rename_to_small_smelter_furnace`
  Action: Rename or alias the item toward `small_smelter_furnace_v0`.
  Action type: `rename_or_alias`
  Queue task if checked: Rename or alias `blast_furnace_or_smelter` conceptually as a compact ore/scrap smelter. Update display name, notes, and references as appropriate while preserving IDs if a rename is too disruptive. Source review: `research/machines/blast_furnace_or_smelter.md`.
  Notes: This keeps one item but removes the misleading full blast-furnace implication.
  Freeform instructions:
  > 

- [ ] `blast_furnace_or_smelter.split_by_furnace_type`
  Action: Split the generic item into specific smelting/remelting/reduction furnace types.
  Action type: `split_item`
  Queue task if checked: Review process references and split uses into blast furnace/direct reduction for iron ore, cupola for cast iron remelting, induction/electric arc for metal remelting/steelmaking, crucible furnace for small melts, and reduction furnace where chemistry/offgas matters. Source review: `research/machines/blast_furnace_or_smelter.md`.
  Notes: This is a larger migration. Split implementation into smaller KB edit tasks by process family.
  Freeform instructions:
  > 

- [ ] `blast_furnace_or_smelter.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `blast_furnace_or_smelter` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `blast_furnace_or_smelter.add_process_requirements`
  Action: Add explicit support requirements for true smelting/reduction uses.
  Action type: `process_requirement_update`
  Queue task if checked: Inspect `iron_smelting_reduction_v0` and related smelting processes. Add or document requirements for blower, tuyeres, flux, reductant/fuel, refractory lining, tapping system, slag handling, and emissions/offgas handling where appropriate. Source review: `research/machines/blast_furnace_or_smelter.md`.
  Notes: Do not assume one generic item can handle aluminum, copper, iron ore, scrap steel, and specialty alloys without notes.
  Freeform instructions:
  > 

- [ ] `blast_furnace_or_smelter.decide_iron_smelting_route`
  Action: Decide what `iron_smelting_reduction_v0` actually represents.
  Action type: `research_or_design_followup`
  Queue task if checked: Create a KB design/edit task to decide whether `iron_smelting_reduction_v0` means pig iron from blast furnace, bloom/direct reduction, or generic smelter reduction, then align machine requirements accordingly. Source review: `research/machines/blast_furnace_or_smelter.md`.
  Notes: This may require domain judgment before direct YAML edits.
  Freeform instructions:
  > 

- [ ] `blast_furnace_or_smelter.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `blast_furnace_or_smelter` using the freeform instructions below. Source review: `research/machines/blast_furnace_or_smelter.md`.
  Freeform instructions:
  > 

## casting_furnace_v0

Source review: `research/machines/casting_furnace_v0.md`
KB item: `kb/items/machines/casting_furnace_v0.yaml`
Decision status: unresolved

Summary: Real foundry furnace category, but the KB item is already deprecated/consolidated into `furnace_basic` by local dedupe notes. Many process references still use `casting_furnace_v0`, so the main decision is whether to finish consolidation or replace references with specific furnace subtypes where needed.

### Primary Path: Choose One

- [ ] `casting_furnace_v0.finish_consolidation_to_furnace_basic`
  Action: Finish migrating active references from `casting_furnace_v0` to `furnace_basic` where the generic small-furnace abstraction is sufficient.
  Action type: `reference_migration`
  Queue task if checked: Inspect process references to `casting_furnace_v0` and migrate simple casting/melting uses to `furnace_basic` consistent with `docs/dedupe_decisions.md`. Keep or update deprecation notes on `casting_furnace_v0`. Source review: `research/machines/casting_furnace_v0.md`.
  Notes: Do not migrate steelmaking/refining or specialized foundry processes blindly if they need higher temperature, induction, slag/refining practice, or holding/pouring infrastructure.
  Freeform instructions:
  > 

- [ ] `casting_furnace_v0.replace_with_specific_foundry_subtypes`
  Action: Replace `casting_furnace_v0` references with specific foundry furnace subtype resources where process needs differ.
  Action type: `split_item`
  Queue task if checked: Review all `casting_furnace_v0` process references and assign specific equipment where appropriate, such as `small_crucible_furnace`, `induction_melting_furnace`, `holding_furnace`, `cupola_furnace`, `furnace_high_temp`, or `blast_furnace_or_smelter`. Source review: `research/machines/casting_furnace_v0.md`.
  Notes: This is a larger migration and should be split by process family if many unrelated processes are affected.
  Freeform instructions:
  > 

- [ ] `casting_furnace_v0.keep_deprecated_no_reference_migration_now`
  Action: Keep `casting_furnace_v0` deprecated but defer active reference migration.
  Action type: `note_cleanup`
  Queue task if checked: Ensure `casting_furnace_v0` notes clearly state its deprecated/consolidated status and preferred replacement path, but do not migrate process references yet. Source review: `research/machines/casting_furnace_v0.md`.
  Notes: Use this if current references are too risky to migrate without a furnace-family design pass.
  Freeform instructions:
  > 

- [ ] `casting_furnace_v0.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `casting_furnace_v0` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `casting_furnace_v0.audit_steel_and_stainless_references`
  Action: Audit steel/stainless smelting and refining references before any generic migration.
  Action type: `research_or_design_followup`
  Queue task if checked: Review `steel_ingot_cast_v0`, `stainless_steel_smelting_v0`, `steel_refining_basic_v0`, `stainless_refining_basic_v0`, and related references using `casting_furnace_v0` to decide whether `furnace_basic` is sufficient or a higher-temperature/specialized furnace is required. Source review: `research/machines/casting_furnace_v0.md`.
  Notes: This is a guardrail against over-consolidating specialized metallurgy.
  Freeform instructions:
  > 

- [ ] `casting_furnace_v0.remove_heat_treatment_implication`
  Action: Separate heat-treatment semantics from casting furnace semantics.
  Action type: `note_cleanup`
  Queue task if checked: Update `casting_furnace_v0` notes or related process guidance so melting/holding/pouring duties are not conflated with controlled heat treatment. Use `heat_treatment_furnace_v0` for heat-treatment cycles where metallurgy matters. Source review: `research/machines/casting_furnace_v0.md`.
  Freeform instructions:
  > 

- [ ] `casting_furnace_v0.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `casting_furnace_v0` using the freeform instructions below. Source review: `research/machines/casting_furnace_v0.md`.
  Freeform instructions:
  > 

## casting_mold_set

Source review: `research/machines/casting_mold_set.md`
KB item: `kb/items/machines/casting_mold_set.yaml`
Decision status: unresolved

Summary: Real reusable foundry tooling. It is plausible as a generic kit of flasks, patterns, gates/risers tooling, core boxes, simple ingot molds, or a few reusable permanent molds, but it should not imply universal molds for every casting geometry.

### Primary Path: Choose One

- [ ] `casting_mold_set.keep_generic_foundry_tooling`
  Action: Keep `casting_mold_set` as a generic foundry mold tooling kit.
  Action type: `note_cleanup`
  Queue task if checked: Update `kb/items/machines/casting_mold_set.yaml` notes to clarify that it represents reusable foundry mold tooling such as flasks, pattern equipment, core boxes, gates/risers tooling, and simple molds, not a universal mold set for all part geometries. Source review: `research/machines/casting_mold_set.md`.
  Notes: Keep it separate from `sand_casting_flask_set` if that item represents reusable sand-casting support frames specifically.
  Freeform instructions:
  > 

- [ ] `casting_mold_set.split_mold_tooling_subtypes`
  Action: Split generic mold tooling into more specific resources.
  Action type: `split_item`
  Queue task if checked: Review casting process references and split where needed into resources such as `ingot_mold_set`, `sand_casting_pattern_set`, `permanent_mold_set`, and material-specific glass/metal mold tooling. Source review: `research/machines/casting_mold_set.md`.
  Notes: Split implementation by process family if many unrelated casting workflows are affected.
  Freeform instructions:
  > 

- [ ] `casting_mold_set.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `casting_mold_set` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `casting_mold_set.add_part_specific_mold_guardrail`
  Action: Add guidance that complex or dedicated casting geometries need part-specific patterns or molds.
  Action type: `process_requirement_update`
  Queue task if checked: Review casting processes for machine frames, motor housings, complex fluid parts, glass casting, and other geometry-specific outputs. Add notes or requirements for part-specific pattern/mold tooling where a generic `casting_mold_set` would hide important tooling. Source review: `research/machines/casting_mold_set.md`.
  Freeform instructions:
  > 

- [ ] `casting_mold_set.decide_sand_binder_scope`
  Action: Decide whether `casting_mold_set` includes only reusable tooling or also consumable sand/binder.
  Action type: `consumable_or_tooling_modeling`
  Queue task if checked: Inspect `casting_mold_set`, `sand_casting_flask_set`, and sand-casting processes. Clarify whether molding sand/binder are separate consumables or included in this reusable tooling resource. Source review: `research/machines/casting_mold_set.md`.
  Freeform instructions:
  > 

- [ ] `casting_mold_set.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `casting_mold_set` using the freeform instructions below. Source review: `research/machines/casting_mold_set.md`.
  Freeform instructions:
  > 

## cement_mixer_small

Source review: `research/machines/cement_mixer_small.md`
KB item: `kb/items/machines/cement_mixer_small.yaml`
Decision status: unresolved

Summary: Real small mixer used for cementitious, refractory, or binder preparation. The KB mass is plausible for rugged/industrial use but heavy for a common portable 100-150 L mixer. The BOM may include redundant drive motors.

### Primary Path: Choose One

- [ ] `cement_mixer_small.keep_as_rugged_refractory_mixer`
  Action: Keep as a ruggedized small industrial/refractory mixer and document that assumption.
  Action type: `note_cleanup`
  Queue task if checked: Update `kb/items/machines/cement_mixer_small.yaml` notes to clarify that the 309.5 kg mass represents a rugged small industrial or refractory-duty mixer, not a lightweight homeowner portable concrete mixer. Source review: `research/machines/cement_mixer_small.md`.
  Freeform instructions:
  > 

- [ ] `cement_mixer_small.revise_to_portable_drum_mixer`
  Action: Scope it as a common portable 100-150 L drum mixer and review mass/BOM accordingly.
  Action type: `bom_or_recipe_update`
  Queue task if checked: Review `cement_mixer_small` mass, BOM, and recipe against a portable 100-150 L drum mixer assumption. Adjust mass/components if the KB intends a common small portable mixer rather than a rugged industrial unit. Source review: `research/machines/cement_mixer_small.md`.
  Freeform instructions:
  > 

- [ ] `cement_mixer_small.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `cement_mixer_small` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `cement_mixer_small.decide_drum_mortar_or_pan_mixer`
  Action: Decide whether the item should be a drum mixer, mortar mixer, or pan mixer.
  Action type: `note_cleanup`
  Queue task if checked: Review refractory/binder processes and `refractory_installation_tools` usage to decide whether `cement_mixer_small` should be a drum mixer, mortar mixer, or pan mixer. Update notes/name if needed. Source review: `research/machines/cement_mixer_small.md`.
  Freeform instructions:
  > 

- [ ] `cement_mixer_small.audit_dual_motor_bom`
  Action: Check whether both `mixer_motor_small` and `drive_motor_medium` are needed.
  Action type: `bom_or_recipe_update`
  Queue task if checked: Inspect `cement_mixer_small` BOM and recipe for possible duplicated motor/drive components. Commercial mixers usually have one primary motor/engine plus gearbox/transmission unless a second motor represents an accessory. Source review: `research/machines/cement_mixer_small.md`.
  Freeform instructions:
  > 

- [ ] `cement_mixer_small.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `cement_mixer_small` using the freeform instructions below. Source review: `research/machines/cement_mixer_small.md`.
  Freeform instructions:
  > 

## chemical_reactor_basic

Source review: `research/machines/chemical_reactor_basic.md`
KB item: `kb/items/machines/chemical_reactor_basic.yaml`
Decision status: unresolved

Summary: Real small stirred/jacketed reactor category, but broad. It should have a defined pressure, temperature, materials, corrosion, gas-handling, and catalyst/solids envelope, and it should be distinguished from or consolidated with `generic_chemical_reactor_v0`.

### Primary Path: Choose One

- [ ] `chemical_reactor_basic.define_stirred_jacketed_reactor`
  Action: Keep as concrete small stirred/jacketed batch or semi-batch reactor.
  Action type: `note_cleanup`
  Queue task if checked: Update `kb/items/machines/chemical_reactor_basic.yaml` notes/capabilities to define it as a small stirred/jacketed reactor with moderate temperature, mixing, gas ports, pressure relief, temperature control, and ordinary steel/stainless compatibility unless otherwise stated. Source review: `research/machines/chemical_reactor_basic.md`.
  Notes: This differentiates it from abstract placeholders and specialized reactors.
  Freeform instructions:
  > 

- [ ] `chemical_reactor_basic.consolidate_with_generic_chemical_reactor`
  Action: Consolidate or clearly separate `chemical_reactor_basic` and `generic_chemical_reactor_v0`.
  Action type: `dedupe_or_consolidation`
  Queue task if checked: Compare `chemical_reactor_basic` and `generic_chemical_reactor_v0` usage. Either consolidate references to one canonical reactor abstraction or document `generic_chemical_reactor_v0` as abstract placeholder while `chemical_reactor_basic` remains the concrete stirred/jacketed reactor. Source review: `research/machines/chemical_reactor_basic.md`.
  Freeform instructions:
  > 

- [ ] `chemical_reactor_basic.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `chemical_reactor_basic` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `chemical_reactor_basic.audit_specialized_reactor_processes`
  Action: Move incompatible chemistry to more specific reactor classes.
  Action type: `process_requirement_update`
  Queue task if checked: Audit processes using `chemical_reactor_basic` for acid-lined, high-pressure, high-temperature molten salt, packed-bed catalytic, electrochemical, refractory, corrosive chloride, or solids-heavy service. Migrate requirements to specific reactor resources where needed. Source review: `research/machines/chemical_reactor_basic.md`.
  Notes: Split implementation by chemistry family if many unrelated processes are affected.
  Freeform instructions:
  > 

- [ ] `chemical_reactor_basic.add_hazardous_service_notes`
  Action: Add explicit service notes to hazardous reactor processes.
  Action type: `note_cleanup`
  Queue task if checked: For hazardous processes using `chemical_reactor_basic`, add notes covering pressure, temperature, materials of construction, corrosion, gas handling, pressure relief, and catalyst/solid compatibility assumptions. Source review: `research/machines/chemical_reactor_basic.md`.
  Freeform instructions:
  > 

- [ ] `chemical_reactor_basic.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `chemical_reactor_basic` using the freeform instructions below. Source review: `research/machines/chemical_reactor_basic.md`.
  Freeform instructions:
  > 

## chemical_reactor_vessel_v0

Source review: `research/machines/chemical_reactor_vessel_v0.md`
KB item: `kb/items/machines/chemical_reactor_vessel_v0.yaml`
Decision status: unresolved

Summary: Real chemical reactor vessel or pressure-vessel component. It is best modeled as a reactor shell/subassembly, not as complete reaction capability unless a process only needs a passive vessel.

### Primary Path: Choose One

- [ ] `chemical_reactor_vessel_v0.keep_as_reactor_vessel_subassembly`
  Action: Keep the item but make its component/subassembly role explicit.
  Action type: `infrastructure_or_subsystem_modeling`
  Queue task if checked: Update `kb/items/machines/chemical_reactor_vessel_v0.yaml` notes/name as appropriate to clarify it is a reactor vessel shell/subassembly used inside complete reactor systems, not a standalone process reactor by default. Source review: `research/machines/chemical_reactor_vessel_v0.md`.
  Freeform instructions:
  > 

- [ ] `chemical_reactor_vessel_v0.promote_to_full_reactor_unit`
  Action: Treat direct process uses as requiring a full reactor unit instead of only the vessel.
  Action type: `reference_migration`
  Queue task if checked: Inspect direct resource requirements on `chemical_reactor_vessel_v0`, especially `chemical_synthesis_process_v0`. Replace direct vessel requirements with `chemical_reactor_basic`, `generic_chemical_reactor_v0`, or a specific reactor unit unless the process truly only needs a passive vessel. Source review: `research/machines/chemical_reactor_vessel_v0.md`.
  Freeform instructions:
  > 

- [ ] `chemical_reactor_vessel_v0.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `chemical_reactor_vessel_v0` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `chemical_reactor_vessel_v0.split_service_classes`
  Action: Split future vessel variants by service class where needed.
  Action type: `split_item`
  Queue task if checked: Review vessel usage and decide whether atmospheric tanks, pressure vessels, jacketed stirred vessels, acid-lined vessels, high-temperature refractory vessels, and high-pressure gas reactors need separate KB items or notes. Source review: `research/machines/chemical_reactor_vessel_v0.md`.
  Notes: Use this only where process requirements differ materially.
  Freeform instructions:
  > 

- [ ] `chemical_reactor_vessel_v0.add_pressure_material_notes`
  Action: Add pressure, temperature, and material compatibility notes for hazardous/aggressive chemistry.
  Action type: `note_cleanup`
  Queue task if checked: Add or update notes around pressure rating, temperature rating, material compatibility, corrosion lining, relief, inspection, and testing assumptions for `chemical_reactor_vessel_v0` and hazardous process uses. Source review: `research/machines/chemical_reactor_vessel_v0.md`.
  Freeform instructions:
  > 

- [ ] `chemical_reactor_vessel_v0.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `chemical_reactor_vessel_v0` using the freeform instructions below. Source review: `research/machines/chemical_reactor_vessel_v0.md`.
  Freeform instructions:
  > 

## chemical_separation_equipment

Source review: `research/machines/chemical_separation_equipment.md`
KB item: `kb/items/machines/chemical_separation_equipment.yaml`
Decision status: unresolved

Summary: Real modular chemical/hydrometallurgy separation skid, not one universal separator. It can remain a coarse process-train resource, but high-fidelity models should split leach tanks, filters, mixer-settlers, precipitation tanks, ion-exchange columns, electrowinning cells, and acid recycling.

### Primary Path: Choose One

- [ ] `chemical_separation_equipment.keep_as_modular_skid`
  Action: Keep as explicitly generic modular chemical separation skid.
  Action type: `note_cleanup`
  Queue task if checked: Update `kb/items/machines/chemical_separation_equipment.yaml` display name/notes to describe a modular hydrometallurgy or chemical separation skid/process train, not one universal machine. Source review: `research/machines/chemical_separation_equipment.md`.
  Freeform instructions:
  > 

- [ ] `chemical_separation_equipment.split_by_separation_operation`
  Action: Split into specific separation equipment classes where process needs differ.
  Action type: `split_item`
  Queue task if checked: Review nickel, cobalt, REE, chloride recycling, and related processes using `chemical_separation_equipment`. Split requirements into solvent extraction mixer-settlers, filter presses/clarifiers, precipitation tanks, ion-exchange columns, electrowinning cells, acid recycling modules, or leach tanks where needed. Source review: `research/machines/chemical_separation_equipment.md`.
  Notes: Split implementation by chemistry/process family.
  Freeform instructions:
  > 

- [ ] `chemical_separation_equipment.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `chemical_separation_equipment` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `chemical_separation_equipment.review_duplicate_resource_requirements`
  Action: Review processes that require this item more than once.
  Action type: `process_requirement_update`
  Queue task if checked: Inspect processes such as `ree_extraction_kreep_v0` that may list `chemical_separation_equipment` multiple times. Decide whether the duplicate means two modules, two stages, or an accidental duplicate, and update notes or requirements accordingly. Source review: `research/machines/chemical_separation_equipment.md`.
  Freeform instructions:
  > 

- [ ] `chemical_separation_equipment.add_corrosion_material_notes`
  Action: Add materials/corrosion assumptions for acids, chlorides, solvents, and elevated temperatures.
  Action type: `note_cleanup`
  Queue task if checked: Update notes for `chemical_separation_equipment` and key processes to document assumed corrosion-resistant materials, secondary containment, pumps, seals, sensors, and solvent/acid compatibility. Source review: `research/machines/chemical_separation_equipment.md`.
  Freeform instructions:
  > 

- [ ] `chemical_separation_equipment.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `chemical_separation_equipment` using the freeform instructions below. Source review: `research/machines/chemical_separation_equipment.md`.
  Freeform instructions:
  > 

## cnc_mill

Source review: `research/machines/cnc_mill.md`
KB item: `kb/items/machines/cnc_mill.yaml`
Decision status: unresolved

Summary: Real and canonical precision milling machine. Local dedupe notes already consolidate `milling_machine_general_v0` into `cnc_mill`. The main decisions are whether to clarify scale/capabilities and how to represent tooling, coolant, workholding, and calibration support.

### Primary Path: Choose One

- [ ] `cnc_mill.keep_canonical_compact_cnc_mill`
  Action: Keep `cnc_mill` as the canonical compact-shop CNC milling resource.
  Action type: `note_cleanup`
  Queue task if checked: Update `kb/items/machines/cnc_mill.yaml` notes if needed to clarify that the 785 kg item is compact-shop scale, not a full production VMC unless otherwise documented. Source review: `research/machines/cnc_mill.md`.
  Freeform instructions:
  > 

- [ ] `cnc_mill.revise_to_production_vmc_assumption`
  Action: Treat `cnc_mill` as a more complete enclosed VMC and review mass/BOM.
  Action type: `bom_or_recipe_update`
  Queue task if checked: Review `cnc_mill` mass, BOM, coolant, enclosure, tool changer, controller, spindle, and axis hardware assumptions against a production VMC interpretation. Source review: `research/machines/cnc_mill.md`.
  Freeform instructions:
  > 

- [ ] `cnc_mill.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `cnc_mill` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `cnc_mill.finish_milling_machine_consolidation`
  Action: Finish or verify consolidation from `milling_machine_general_v0` into `cnc_mill`.
  Action type: `dedupe_or_consolidation`
  Queue task if checked: Inspect remaining references to `milling_machine_general_v0` and dedupe documentation. Migrate or document remaining references so `cnc_mill` is the canonical milling resource unless manual milling is intentionally preserved as separate. Source review: `research/machines/cnc_mill.md`.
  Freeform instructions:
  > 

- [ ] `cnc_mill.add_tooling_coolant_workholding_requirements`
  Action: Represent CNC milling support resources more explicitly.
  Action type: `process_requirement_update`
  Queue task if checked: Review CNC milling processes and recipes for cutting tools, coolant, workholding/fixtures, metrology/calibration artifacts, and consumables. Add notes or requirements where currently hidden. Source review: `research/machines/cnc_mill.md`.
  Freeform instructions:
  > 

- [ ] `cnc_mill.distinguish_precision_and_multiaxis_capabilities`
  Action: Decide whether rough, precision, and multi-axis CNC milling need separate capability tags.
  Action type: `note_cleanup`
  Queue task if checked: Review `cnc_mill` capabilities and process requirements to decide whether existing notes/tags should distinguish rough milling, precision milling, and true 5-axis simultaneous machining. Source review: `research/machines/cnc_mill.md`.
  Freeform instructions:
  > 

- [ ] `cnc_mill.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `cnc_mill` using the freeform instructions below. Source review: `research/machines/cnc_mill.md`.
  Freeform instructions:
  > 

## coil_winding_machine

Source review: `research/machines/coil_winding_machine.md`
KB item: `kb/items/machines/coil_winding_machine.yaml`
Decision status: unresolved

Summary: Real semi-automatic coil winding machine for motors, transformers, inductors, solenoids, relays, and heating coils. Core features are controlled rotation, turn counting, wire guiding, and tension control. Potential duplication exists with `coil_winding_machine_v0`, `winding_machine`, and `winding_drums`.

### Primary Path: Choose One

- [ ] `coil_winding_machine.keep_generic_electrical_coil_winder`
  Action: Keep as the canonical generic electrical coil winder.
  Action type: `note_cleanup`
  Queue task if checked: Update `kb/items/machines/coil_winding_machine.yaml` notes/capabilities to define it as a generic semi-automatic electrical coil winder with tension control, turn counting, traverse/guiding, and winding-pattern support. Source review: `research/machines/coil_winding_machine.md`.
  Freeform instructions:
  > 

- [ ] `coil_winding_machine.split_heavy_and_fine_winding_variants`
  Action: Split fine magnet-wire winding from heavy transformer/heating-element winding if needed.
  Action type: `split_item`
  Queue task if checked: Review process references for motors, transformers, resistive heating, relays, solenoids, and precision windings. Decide whether one `coil_winding_machine` covers all wire sizes or whether heavy winding needs a separate variant. Source review: `research/machines/coil_winding_machine.md`.
  Freeform instructions:
  > 

- [ ] `coil_winding_machine.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `coil_winding_machine` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `coil_winding_machine.normalize_duplicate_winding_ids`
  Action: Normalize references among `coil_winding_machine`, `coil_winding_machine_v0`, `winding_machine`, and `winding_drums`.
  Action type: `dedupe_or_consolidation`
  Queue task if checked: Inspect winding-related items and process references. Decide whether `coil_winding_machine` is the electrical-coil-specialized resource, whether `winding_machine` is a broader spooling/fiber machine, and whether `winding_drums` are only subcomponents/tooling. Source review: `research/machines/coil_winding_machine.md`.
  Freeform instructions:
  > 

- [ ] `coil_winding_machine.add_winding_consumables`
  Action: Ensure coil winding recipes model necessary consumables and forms.
  Action type: `process_requirement_update`
  Queue task if checked: Review coil, transformer, motor, relay, solenoid, and heating-element recipes for magnet wire, resistive wire, insulation, bobbins/forms, slot liners, varnish/impregnation, and curing requirements. Source review: `research/machines/coil_winding_machine.md`.
  Freeform instructions:
  > 

- [ ] `coil_winding_machine.audit_photolithographic_coil_reference`
  Action: Decide whether photolithographic coil creation should use this machine.
  Action type: `process_requirement_update`
  Queue task if checked: Review `photolithographic_coil_winding_v0` and related recipes. If the process is PCB/photolithographic patterning rather than physical wire winding, migrate away from `coil_winding_machine` to PCB/photolithography resources. Source review: `research/machines/coil_winding_machine.md`.
  Freeform instructions:
  > 

- [ ] `coil_winding_machine.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `coil_winding_machine` using the freeform instructions below. Source review: `research/machines/coil_winding_machine.md`.
  Freeform instructions:
  > 

## control_compute_module_imported

Source review: `research/machines/control_compute_module_imported.md`
KB item: `kb/items/machines/control_compute_module_imported.yaml`
Decision status: unresolved

Summary: Real imported electronics boundary component used across many machine BOMs. It likely represents PLC/SBC/microcontroller control hardware, but may currently also cover safety PLCs and AI/vision compute.

### Primary Path: Choose One

- [ ] `control_compute_module_imported.keep_broad_imported_controller`
  Action: Keep as a broad imported industrial control module.
  Action type: `note_cleanup`
  Queue task if checked: Update `kb/items/machines/control_compute_module_imported.yaml` notes/display name to clarify it is an imported industrial control module or PLC/SBC boundary component for early phases, not locally manufacturable just because PCB assembly exists. Source review: `research/machines/control_compute_module_imported.md`.
  Freeform instructions:
  > 

- [ ] `control_compute_module_imported.split_controller_safety_ai`
  Action: Split ordinary embedded control, safety PLC, and AI/vision compute where risk or capability matters.
  Action type: `split_item`
  Queue task if checked: Review uses of `control_compute_module_imported` across BOMs and processes. Decide whether to split into ordinary embedded controller/PLC, safety-rated controller, and AI/vision/edge compute resources. Source review: `research/machines/control_compute_module_imported.md`.
  Notes: Keep broad reuse under Conservative Mode unless specific safety/performance needs justify splits.
  Freeform instructions:
  > 

- [ ] `control_compute_module_imported.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `control_compute_module_imported` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `control_compute_module_imported.add_no_local_semiconductor_guardrail`
  Action: Add explicit note that local PCB assembly does not imply local compute module manufacture.
  Action type: `note_cleanup`
  Queue task if checked: Add notes to `control_compute_module_imported` or related recipes stating that processors, memory, precision power management, communications ICs, and safety certification remain imported/advanced-manufacturing dependencies in early phases. Source review: `research/machines/control_compute_module_imported.md`.
  Freeform instructions:
  > 

- [ ] `control_compute_module_imported.consider_software_firmware_modeling`
  Action: Decide whether software/firmware should be modeled separately from imported hardware.
  Action type: `deferred_schema_or_modeling_decision`
  Queue task if checked: Create a KB modeling/design task to decide whether control software, firmware, calibration/configuration, and machine programs should be represented separately from imported control hardware. Source review: `research/machines/control_compute_module_imported.md`.
  Freeform instructions:
  > 

- [ ] `control_compute_module_imported.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `control_compute_module_imported` using the freeform instructions below. Source review: `research/machines/control_compute_module_imported.md`.
  Freeform instructions:
  > 

## controlled_atmosphere_chamber

Source review: `research/machines/controlled_atmosphere_chamber.md`
KB item: `kb/items/machines/controlled_atmosphere_chamber.yaml`
Decision status: unresolved

Summary: Real sealed atmosphere-control equipment category, but broad. Best interpreted as a sealed process chamber/load-lock subsystem with vacuum purge and gas manifold, not a complete furnace, glovebox, or inert gas supply system.

### Primary Path: Choose One

- [ ] `controlled_atmosphere_chamber.keep_as_sealed_process_chamber`
  Action: Keep as sealed process chamber/load-lock with vacuum purge and inert/process gas manifold.
  Action type: `infrastructure_or_subsystem_modeling`
  Queue task if checked: Update `kb/items/machines/controlled_atmosphere_chamber.yaml` notes to define it as a sealed process chamber or load-lock style subsystem, including vacuum purge and gas manifold assumptions. Source review: `research/machines/controlled_atmosphere_chamber.md`.
  Freeform instructions:
  > 

- [ ] `controlled_atmosphere_chamber.integrate_into_specific_furnaces`
  Action: Move high-temperature atmosphere requirements into specific furnace items where needed.
  Action type: `reference_migration`
  Queue task if checked: Review high-temperature sintering, magnet, glass, and silica process references. Replace generic chamber requirements with controlled-atmosphere furnace, vacuum furnace, hot press, or specific furnace requirements where a chamber alone is insufficient. Source review: `research/machines/controlled_atmosphere_chamber.md`.
  Notes: Split by furnace/process family if needed.
  Freeform instructions:
  > 

- [ ] `controlled_atmosphere_chamber.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `controlled_atmosphere_chamber` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `controlled_atmosphere_chamber.add_not_furnace_or_glovebox_guardrail`
  Action: Add notes distinguishing this item from complete furnaces, gloveboxes, and gas supply systems.
  Action type: `note_cleanup`
  Queue task if checked: Update notes to keep `inert_atmosphere_system` separate for gas storage/purification/flow, `glove_box_or_dry_room` separate for operator-accessible handling, and furnace-specific items separate for heated processing. Source review: `research/machines/controlled_atmosphere_chamber.md`.
  Freeform instructions:
  > 

- [ ] `controlled_atmosphere_chamber.add_vacuum_gas_safety_assumptions`
  Action: Add chamber performance and safety assumptions.
  Action type: `note_cleanup`
  Queue task if checked: Add assumptions for leak testing, vacuum level, leak rate, pressure rating, relief, feedthroughs, seals, oxygen/moisture sensing, and hydrogen/reducing-gas purge/exhaust safety where applicable. Source review: `research/machines/controlled_atmosphere_chamber.md`.
  Freeform instructions:
  > 

- [ ] `controlled_atmosphere_chamber.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `controlled_atmosphere_chamber` using the freeform instructions below. Source review: `research/machines/controlled_atmosphere_chamber.md`.
  Freeform instructions:
  > 

## crucible_graphite

Source review: `research/machines/crucible_graphite.md`
KB item: `kb/items/parts/crucible_graphite.yaml`
Decision status: unresolved

Summary: Real graphite crucible/tooling component for high-temperature containment. It is finite-life reusable tooling/consumable inventory, not standalone equipment. Suitability depends on atmosphere, melt chemistry, carbon contamination, and temperature.

### Primary Path: Choose One

- [ ] `crucible_graphite.keep_distinct_graphite_crucible`
  Action: Keep `crucible_graphite` distinct from generic refractory crucibles.
  Action type: `consumable_or_tooling_modeling`
  Queue task if checked: Update notes for `crucible_graphite` as needed to preserve graphite-specific properties and limits, including thermal shock resistance, conductivity, reducing behavior, oxidation risk, and carbon contamination. Source review: `research/machines/crucible_graphite.md`.
  Freeform instructions:
  > 

- [ ] `crucible_graphite.consolidate_graphite_crucible_variants`
  Action: Consolidate duplicate graphite crucible names where size/capability differences do not matter.
  Action type: `dedupe_or_consolidation`
  Queue task if checked: Compare `crucible_graphite`, `graphite_crucible_v0`, `crucible_graphite_small`, and `crucible_graphite_large`. Consolidate only where differences are within Conservative Mode reuse/variant tolerance or can be represented as variants. Source review: `research/machines/crucible_graphite.md`.
  Freeform instructions:
  > 

- [ ] `crucible_graphite.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `crucible_graphite` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `crucible_graphite.add_atmosphere_and_contamination_notes`
  Action: Add atmosphere and contamination guardrails to graphite crucible use.
  Action type: `note_cleanup`
  Queue task if checked: Add or update notes for graphite crucible processes stating that graphite is more realistic in inert, vacuum, or reducing environments, and can reduce oxides, add carbon, or form carbides in incompatible melts. Source review: `research/machines/crucible_graphite.md`.
  Freeform instructions:
  > 

- [ ] `crucible_graphite.audit_glass_and_fused_silica_use`
  Action: Check whether graphite is appropriate for glass/fused silica processes.
  Action type: `process_requirement_update`
  Queue task if checked: Review `glass_envelope_forming_v0`, `glass_casting_v0`, `glass_casting_process_v0`, `fused_silica_production_v0`, and related processes using `crucible_graphite`. Replace with silica/alumina/zirconia/refractory crucibles where graphite contamination or reduction is inappropriate. Source review: `research/machines/crucible_graphite.md`.
  Freeform instructions:
  > 

- [ ] `crucible_graphite.model_lifetime_replacement`
  Action: Decide whether crucible lifetime/replacement rate should be modeled.
  Action type: `deferred_schema_or_modeling_decision`
  Queue task if checked: Create a KB modeling task to decide whether crucible wear, oxidation, thermal shock, and replacement rates should be represented for repeated high-temperature cycles. Source review: `research/machines/crucible_graphite.md`.
  Freeform instructions:
  > 

- [ ] `crucible_graphite.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `crucible_graphite` using the freeform instructions below. Source review: `research/machines/crucible_graphite.md`.
  Freeform instructions:
  > 

## crucible_refractory

Source review: `research/machines/crucible_refractory.md`
KB item: `kb/items/machines/crucible_refractory.yaml`
Decision status: unresolved

Summary: Real reusable/consumable refractory crucible ware for high-temperature containment. It should be treated as tooling/consumable inventory used with furnaces and handling tools, not standalone equipment. Material compatibility is process-specific.

### Primary Path: Choose One

- [ ] `crucible_refractory.keep_generic_refractory_crucible`
  Action: Keep as generic refractory crucible tooling with clarified limits.
  Action type: `consumable_or_tooling_modeling`
  Queue task if checked: Update `kb/items/machines/crucible_refractory.yaml` notes to describe a reusable/replaceable refractory crucible container for furnace/casting operations, with material-compatibility limits. Source review: `research/machines/crucible_refractory.md`.
  Freeform instructions:
  > 

- [ ] `crucible_refractory.consolidate_duplicate_crucibles`
  Action: Consolidate overlapping generic crucible names where safe.
  Action type: `dedupe_or_consolidation`
  Queue task if checked: Compare `crucible_refractory`, `crucible_ceramic_refractory`, `crucible_set`, and related crucible items. Consolidate generic duplicates under Conservative Mode while preserving material-specific variants where process compatibility matters. Source review: `research/machines/crucible_refractory.md`.
  Freeform instructions:
  > 

- [ ] `crucible_refractory.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `crucible_refractory` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `crucible_refractory.preserve_material_specific_variants`
  Action: Preserve material-specific crucible variants where compatibility matters.
  Action type: `note_cleanup`
  Queue task if checked: Add notes or requirements distinguishing alumina/ceramic, clay-graphite, silicon carbide, graphite, fused silica, and specialty crucibles for processes where melt chemistry, contamination, or atmosphere matters. Source review: `research/machines/crucible_refractory.md`.
  Freeform instructions:
  > 

- [ ] `crucible_refractory.audit_insufficient_generic_uses`
  Action: Audit processes where a generic refractory crucible is probably insufficient.
  Action type: `process_requirement_update`
  Queue task if checked: Review molten silicon, steelmaking, alkali melts, high-purity glass, sapphire/Czochralski, and other aggressive high-temperature processes using `crucible_refractory`. Replace with material-specific crucibles where needed. Source review: `research/machines/crucible_refractory.md`.
  Freeform instructions:
  > 

- [ ] `crucible_refractory.model_lifetime_replacement`
  Action: Decide whether crucible lifetime/replacement rate should be modeled.
  Action type: `deferred_schema_or_modeling_decision`
  Queue task if checked: Create a KB modeling task to decide how reusable consumable tooling such as crucibles should represent lifetime, thermal shock failure, corrosion, and replacement. Source review: `research/machines/crucible_refractory.md`.
  Freeform instructions:
  > 

- [ ] `crucible_refractory.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `crucible_refractory` using the freeform instructions below. Source review: `research/machines/crucible_refractory.md`.
  Freeform instructions:
  > 

## cutting_tools_general

Source review: `research/machines/cutting_tools_general.md`
KB item: `kb/items/machines/cutting_tools_general.yaml`
Decision status: unresolved

Summary: Real reusable/wearing cutting-tool inventory, not standalone equipment. The current BOM looks like a small manual kit, while many processes imply machine-tool consumables such as drills, end mills, taps, inserts, saw blades, and specialty cutters.

### Primary Path: Choose One

- [ ] `cutting_tools_general.keep_general_tooling_inventory`
  Action: Keep as broad general cutting-tool inventory with clarified scope.
  Action type: `consumable_or_tooling_modeling`
  Queue task if checked: Update `kb/items/machines/cutting_tools_general.yaml` display name/notes to describe general cutting-tool kit or machine cutting-tool inventory, not a standalone machine. Source review: `research/machines/cutting_tools_general.md`.
  Freeform instructions:
  > 

- [ ] `cutting_tools_general.split_hand_and_machine_cutting_tools`
  Action: Split manual cutting tools from machine cutting-tool consumables.
  Action type: `split_item`
  Queue task if checked: Review references to `cutting_tools_general`, `saw_or_cutting_tool`, `hand_tools_basic`, `metal_shear_or_saw`, CNC/milling/lathe processes, and stock cutting. Split hand cutting, powered stock cutting, and machine cutting-tool inventories where process realism requires. Source review: `research/machines/cutting_tools_general.md`.
  Freeform instructions:
  > 

- [ ] `cutting_tools_general.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `cutting_tools_general` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `cutting_tools_general.add_specialty_cutting_tool_requirements`
  Action: Add explicit specialty tooling where generic cutting tools hide important requirements.
  Action type: `process_requirement_update`
  Queue task if checked: Review gear cutting, threading, milling, drilling, carbide tooling, saw band, and precision machining processes. Add hobs/form cutters, taps/dies, end mills, drills, carbide inserts, saw blades, or other specialty tooling where needed. Source review: `research/machines/cutting_tools_general.md`.
  Freeform instructions:
  > 

- [ ] `cutting_tools_general.model_tool_wear_consumption`
  Action: Decide whether cutting-tool wear/consumption should be modeled.
  Action type: `deferred_schema_or_modeling_decision`
  Queue task if checked: Create a KB modeling task to decide how cutting tool wear, replacement, sharpening, carbide/HSS distinction, and consumable tooling inventory should be represented. Source review: `research/machines/cutting_tools_general.md`.
  Freeform instructions:
  > 

- [ ] `cutting_tools_general.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `cutting_tools_general` using the freeform instructions below. Source review: `research/machines/cutting_tools_general.md`.
  Freeform instructions:
  > 

## dies

Source review: `research/machines/dies.md`
KB item: `kb/items/parts/dies.yaml`
Decision status: unresolved

Summary: Real passive die/tooling set, currently too generic. Its only noted use is hot pressing/sintering, where graphite, ceramic, carbide, or refractory tooling may be more realistic than ordinary hardened steel depending on temperature, atmosphere, pressure, and material chemistry.

### Primary Path: Choose One

- [ ] `dies.rename_to_hot_press_die_set`
  Action: Rename or scope `dies` as a basic hot-press die set.
  Action type: `rename_or_alias`
  Queue task if checked: Update `dies` display/name/notes toward `hot_press_die_set_basic` if its primary use remains `sintering_and_hot_pressing_v0`. Clarify that it is reusable/finite-life tooling used with `hot_press_v0` and related furnace/press resources. Source review: `research/machines/dies.md`.
  Freeform instructions:
  > 

- [ ] `dies.rename_to_powder_pressing_die_set`
  Action: Rename or scope `dies` as a basic powder-pressing die set.
  Action type: `rename_or_alias`
  Queue task if checked: Update `dies` display/name/notes toward `powder_pressing_die_set_basic` if the intended scope is cold powder compaction before sintering rather than high-temperature hot pressing. Source review: `research/machines/dies.md`.
  Freeform instructions:
  > 

- [ ] `dies.keep_generic_press_die_placeholder`
  Action: Keep as generic press/sintering die placeholder but document limits.
  Action type: `note_cleanup`
  Queue task if checked: Update `dies` notes to state it is a generic placeholder for press/sintering dies and not interchangeable with drawing dies, press-brake dies, crimp dies, or other tooling families. Source review: `research/machines/dies.md`.
  Freeform instructions:
  > 

- [ ] `dies.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `dies` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `dies.revisit_material_assumptions`
  Action: Review steel, graphite, ceramic, carbide, or refractory die material assumptions.
  Action type: `bom_or_recipe_update`
  Queue task if checked: Inspect `dies` BOM/recipe and `sintering_and_hot_pressing_v0` requirements. Decide whether high-carbon/tool steel is appropriate or whether graphite/ceramic/carbide/refractory tooling is needed for hot pressing. Source review: `research/machines/dies.md`.
  Freeform instructions:
  > 

- [ ] `dies.add_precision_heat_treatment_steps`
  Action: Add heat treatment, grinding/polishing, and dimensional inspection if steel dies are retained.
  Action type: `bom_or_recipe_update`
  Queue task if checked: Update the `dies` manufacturing route to include heat treatment, precision grinding/polishing, dimensional inspection, and compatible material inputs if a steel-die route remains. Source review: `research/machines/dies.md`.
  Freeform instructions:
  > 

- [ ] `dies.model_hot_press_die_lifetime`
  Action: Decide whether hot-press dies are consumable or finite-life tooling.
  Action type: `deferred_schema_or_modeling_decision`
  Queue task if checked: Create a KB modeling task to decide how die wear, fracture risk, release coatings, graphite foil/BN separators, and replacement/spares should be represented for hot pressing. Source review: `research/machines/dies.md`.
  Freeform instructions:
  > 

- [ ] `dies.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `dies` using the freeform instructions below. Source review: `research/machines/dies.md`.
  Freeform instructions:
  > 

## drawing_die_set_basic

Source review: `research/machines/drawing_die_set_basic.md`
KB item: `kb/items/machines/drawing_die_set_basic.yaml`
Decision status: unresolved

Summary: Real passive wire/rod drawing die tooling. It must be used with a pulling machine, draw bench, capstan, lubricant, and process setup. It likely overlaps with `wire_drawing_die_set`.

### Primary Path: Choose One

- [ ] `drawing_die_set_basic.keep_canonical_basic_drawing_die_set`
  Action: Keep as the canonical basic drawing die set resource.
  Action type: `consumable_or_tooling_modeling`
  Queue task if checked: Update `drawing_die_set_basic` notes to clarify that it is passive reusable tooling for wire/rod drawing and must be paired with pulling equipment and lubricant. Source review: `research/machines/drawing_die_set_basic.md`.
  Freeform instructions:
  > 

- [ ] `drawing_die_set_basic.consolidate_with_wire_drawing_die_set`
  Action: Consolidate `drawing_die_set_basic` with `wire_drawing_die_set` if they are duplicates.
  Action type: `dedupe_or_consolidation`
  Queue task if checked: Compare `drawing_die_set_basic` and `wire_drawing_die_set`, including paths, recipes, process references, materials, and size ranges. Prefer one canonical die-set ID unless the KB needs distinct materials or wire-size ranges. Source review: `research/machines/drawing_die_set_basic.md`.
  Freeform instructions:
  > 

- [ ] `drawing_die_set_basic.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `drawing_die_set_basic` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `drawing_die_set_basic.add_material_grade_scope`
  Action: Decide die material assumptions for different wire materials.
  Action type: `note_cleanup`
  Queue task if checked: Review wire drawing processes for copper, aluminum, steel, kovar, tungsten, or other metals and update notes/requirements for steel, carbide, PCD, or diamond die suitability where needed. Source review: `research/machines/drawing_die_set_basic.md`.
  Freeform instructions:
  > 

- [ ] `drawing_die_set_basic.ensure_pulling_machine_requirement`
  Action: Ensure wire drawing processes require a pulling mechanism separate from die tooling.
  Action type: `process_requirement_update`
  Queue task if checked: Inspect wire drawing processes using `drawing_die_set_basic` and ensure they also require an appropriate wire drawing machine, draw bench, capstan, or pulling resource plus lubricant as needed. Source review: `research/machines/drawing_die_set_basic.md`.
  Freeform instructions:
  > 

- [ ] `drawing_die_set_basic.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `drawing_die_set_basic` using the freeform instructions below. Source review: `research/machines/drawing_die_set_basic.md`.
  Freeform instructions:
  > 

## drill_press

Source review: `research/machines/drill_press.md`
KB item: `kb/items/machines/drill_press.yaml`
Decision status: unresolved

Summary: Real shop drilling machine with realistic BOM and mass. It should remain distinct from field/mining drilling equipment. Potential refinements are PCB drilling, drill-bit consumables, and tapping capability.

### Primary Path: Choose One

- [ ] `drill_press.keep_as_shop_drill_press`
  Action: Keep `drill_press` as the canonical shop drill press.
  Action type: `note_cleanup`
  Queue task if checked: Ensure `kb/items/machines/drill_press.yaml` notes clearly describe a bench/floor shop drill press for vertical hole drilling, distinct from `drilling_equipment_v0` field/mining drill systems. Source review: `research/machines/drill_press.md`.
  Freeform instructions:
  > 

- [ ] `drill_press.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `drill_press` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `drill_press.audit_pcb_drilling_use`
  Action: Decide whether PCB fabrication should use drill press or dedicated PCB drill/router.
  Action type: `process_requirement_update`
  Queue task if checked: Review `pcb_fabrication_v0` and related PCB processes. Decide whether coarse modeling can use `drill_press` or whether fine PCB holes/vias require `pcb_fab_equipment`, PCB drill/router, or CNC routing equipment. Source review: `research/machines/drill_press.md`.
  Freeform instructions:
  > 

- [ ] `drill_press.add_drill_bit_consumables`
  Action: Ensure drill bits/cutting tools are modeled separately from the drill press.
  Action type: `consumable_or_tooling_modeling`
  Queue task if checked: Review drilling processes and add notes or requirements for drill bits/cutting tools via `cutting_tools_general` or more specific tooling where needed. Source review: `research/machines/drill_press.md`.
  Freeform instructions:
  > 

- [ ] `drill_press.decide_tapping_capability`
  Action: Decide whether this drill press includes tapping capability.
  Action type: `note_cleanup`
  Queue task if checked: Review drill-press notes and drilling/tapping processes to decide whether `drill_press` supports tapping or only drilling. Add capability tags or route tapping to other tooling if needed. Source review: `research/machines/drill_press.md`.
  Freeform instructions:
  > 

- [ ] `drill_press.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `drill_press` using the freeform instructions below. Source review: `research/machines/drill_press.md`.
  Freeform instructions:
  > 

## drilling_equipment_v0

Source review: `research/machines/drilling_equipment_v0.md`
KB item: `kb/items/machines/drilling_equipment_v0.yaml`
Decision status: unresolved

Summary: Real compact field drilling rig category for polar regolith/ice access. It should remain distinct from `drill_press` and hand drills. The 500 kg mass implies shallow compact drilling, not deep terrestrial mining.

### Primary Path: Choose One

- [ ] `drilling_equipment_v0.keep_with_clarified_field_scope`
  Action: Keep and clarify as compact field drilling rig for polar regolith/ice access.
  Action type: `note_cleanup`
  Queue task if checked: Update `kb/items/machines/drilling_equipment_v0.yaml` notes/display name to clarify compact field drilling rig, shallow polar regolith/ice access, and distinction from `drill_press`. Source review: `research/machines/drilling_equipment_v0.md`.
  Freeform instructions:
  > 

- [ ] `drilling_equipment_v0.rename_to_specific_drill_rig`
  Action: Rename or alias toward a more specific ID such as `field_drilling_rig_v0`, `polar_regolith_drill_rig_v0`, or `compact_core_drill_rig_v0`.
  Action type: `rename_or_alias`
  Queue task if checked: Propose and apply a clearer name/alias for `drilling_equipment_v0` that matches current polar/subsurface use while preserving references safely. Source review: `research/machines/drilling_equipment_v0.md`.
  Freeform instructions:
  > 

- [ ] `drilling_equipment_v0.no_action`
  Action: No KB change from this review.
  Action type: `no_action`
  Queue task if checked: Do not enqueue KB work for `drilling_equipment_v0` from this review.
  Freeform instructions:
  > 

### Additional Compatible Actions: Choose All That Apply

- [ ] `drilling_equipment_v0.define_depth_diameter_method`
  Action: Define assumed drilling depth, diameter, penetration rate, and method.
  Action type: `note_cleanup`
  Queue task if checked: Review polar water/regolith processes using `drilling_equipment_v0` and document whether the drill is rotary, rotary-percussive, coring, auger, or thermal, plus expected depth/diameter/penetration assumptions. Source review: `research/machines/drilling_equipment_v0.md`.
  Freeform instructions:
  > 

- [ ] `drilling_equipment_v0.audit_auger_drill_overlap`
  Action: Check overlap with `auger_drill_assembly_v0`.
  Action type: `dedupe_or_consolidation`
  Queue task if checked: Compare `drilling_equipment_v0` with `auger_drill_assembly_v0` and related drill-string/bit parts. Decide whether auger drill assembly is a component/tooling subsystem or a parallel machine. Source review: `research/machines/drilling_equipment_v0.md`.
  Freeform instructions:
  > 

- [ ] `drilling_equipment_v0.model_drill_string_bit_wear`
  Action: Decide whether drill bits, casing, and drill string are consumables/finite-life tooling.
  Action type: `deferred_schema_or_modeling_decision`
  Queue task if checked: Create a KB modeling/edit task to represent drill bit wear, drill string/casing, cuttings removal, mast/feed mechanism, anchoring, and abrasive frozen-regolith wear where needed. Source review: `research/machines/drilling_equipment_v0.md`.
  Freeform instructions:
  > 

- [ ] `drilling_equipment_v0.custom_user_instruction`
  Action: Apply custom user instructions for this machine review.
  Action type: `custom_user_instruction`
  Queue task if checked: Enqueue a KB edit task for `drilling_equipment_v0` using the freeform instructions below. Source review: `research/machines/drilling_equipment_v0.md`.
  Freeform instructions:
  > 

## drying_basic_v0

Source review: `research/machines/drying_basic_v0.md`

Current interpretation: Real practical low-temperature drying/curing equipment category, but this machine entry likely duplicates `drying_oven` and also collides by ID with the `drying_basic_v0` process.

### Primary Path - Choose One

- [ ] Decision ID: `drying_basic_v0.consolidate_machine_to_drying_oven`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Use `drying_oven` as the canonical reusable resource for low-temperature drying/curing and keep `drying_basic_v0` as a process ID only.
  - Queue task: Review the `drying_basic_v0` machine/process ID collision; migrate machine-resource references such as `drying_and_curing_v0` to `drying_oven` where appropriate; leave process references to `drying_basic_v0` as process references; add any needed deprecation or alias notes.

- [ ] Decision ID: `drying_basic_v0.rename_to_large_drying_chamber`
  - Action type: `rename_or_alias`, `note_cleanup`
  - Action: Keep a distinct larger drying chamber resource and rename or rescope the machine to something like `drying_chamber_large_v0`.
  - Queue task: Preserve `drying_basic_v0` process identity, rename/rescope the machine so it no longer shares the process ID, clarify the 370 kg larger-chamber role, and distinguish it from `drying_oven`.

- [ ] Decision ID: `drying_basic_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `drying_basic_v0` as both a machine and process for now.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `drying_basic_v0.add_missing_name_material_class`
  - Action type: `note_cleanup`
  - Action: If this remains a machine item, add missing `name` and `material_class` fields.
  - Queue task: Populate machine metadata for `kb/items/machines/drying_basic_v0.yaml` if the item remains after dedupe or rename decisions.

- [ ] Decision ID: `drying_basic_v0.audit_recipe_machine_requirements`
  - Action type: `process_requirement_update`
  - Action: Audit recipes using the `drying_basic_v0` process and confirm they require a suitable low-temperature oven resource such as `drying_oven`.
  - Queue task: Review process/recipe requirements that use `drying_basic_v0`; route low-temperature drying and curing to `drying_oven` or the selected large chamber, and avoid using `furnace_high_temp` where a drying oven is the realistic resource.

- [ ] Decision ID: `drying_basic_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## drying_oven

Source review: `research/machines/drying_oven.md`

Current interpretation: Real practical low-temperature forced-air drying and curing oven; this should remain the canonical reusable resource for 50-300 C drying, stoving, adhesive/coating cure, and moisture removal.

### Primary Path - Choose One

- [ ] Decision ID: `drying_oven.confirm_canonical_low_temp_oven`
  - Action type: `note_cleanup`
  - Action: Explicitly preserve `drying_oven` as the canonical low-temperature drying/curing machine.
  - Queue task: Add or update notes on `drying_oven` and nearby dedupe references to clarify that it covers 50-300 C forced-air drying/curing but not annealing, kiln firing, sintering, vacuum drying, or inert-atmosphere drying.

- [ ] Decision ID: `drying_oven.no_action`
  - Action type: `no_action`
  - Action: Leave `drying_oven` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `drying_oven.add_capacity_assumption`
  - Action type: `note_cleanup`
  - Action: Add an explicit chamber-volume or batch-mass assumption for the 120 kg oven.
  - Queue task: Estimate and document the intended chamber size/batch capacity represented by `drying_oven`, or add a TODO if this requires later design work.

- [ ] Decision ID: `drying_oven.audit_special_drying_requirements`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Check whether any drying processes require vacuum, inert atmosphere, condensation, exhaust, or volatile/waste handling.
  - Queue task: Audit recipes and processes that use `drying_oven`; add separate requirements or resources for vacuum/inert drying, exhaust, condensation, solvent vapor, or hazardous off-gas handling where the review indicates the forced-air oven is insufficient.

- [ ] Decision ID: `drying_oven.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## dust_collection_system

Source review: `research/machines/dust_collection_system.md`

Current interpretation: Real practical generic support system for dusty regolith/mineral handling; a combined cyclone-plus-cartridge collector is appropriate at current KB scale.

### Primary Path - Choose One

- [ ] Decision ID: `dust_collection_system.keep_combined_support_system`
  - Action type: `note_cleanup`
  - Action: Keep `dust_collection_system` as a combined small industrial cyclone/filter/blower/ducting support machine.
  - Queue task: Clarify item notes and BOM intent for `dust_collection_system` as a cyclone-plus-cartridge dust collection system serving crushing, grinding, screening, and sieving.

- [ ] Decision ID: `dust_collection_system.split_for_high_throughput`
  - Action type: `split_item`, `infrastructure_or_subsystem_modeling`
  - Action: Split larger-scale dust control into separate reusable subsystem resources.
  - Queue task: Replace the combined item where needed with explicit resources such as `cyclone_preseparator`, `baghouse_or_cartridge_collector`, `industrial_blower`, and `ductwork_system` for high-throughput continuous mining or processing contexts.

- [ ] Decision ID: `dust_collection_system.no_action`
  - Action type: `no_action`
  - Action: Leave the dust collection model unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `dust_collection_system.normalize_duplicate_files`
  - Action type: `dedupe_or_consolidation`
  - Action: Resolve duplicate machine files that appear to define the same `id`.
  - Queue task: Inspect `kb/items/machines/dust_collection_system.yaml` and `kb/items/machines/dust_collection_system_v0.yaml`; consolidate duplicate definitions or rename one so the KB has a single authoritative item per ID.

- [ ] Decision ID: `dust_collection_system.model_filter_consumables`
  - Action type: `consumable_or_tooling_modeling`, `bom_or_recipe_update`
  - Action: Model replaceable filter cartridges and lifetime assumptions if maintenance realism matters.
  - Queue task: Add or update consumable filter media/cartridge items and maintenance/lifetime notes for `dust_collection_system`.

- [ ] Decision ID: `dust_collection_system.add_regolith_specific_constraints`
  - Action type: `process_requirement_update`, `note_cleanup`
  - Action: Add notes or requirements for abrasive dust, final filtration level, dust loading, and safety mitigation.
  - Queue task: Review regolith crushing/grinding/screening processes and add requirements for abrasion-resistant linings, HEPA/fine filtration, explosion/combustion mitigation, or dust-loading assumptions where warranted.

- [ ] Decision ID: `dust_collection_system.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## electrodes

Source review: `research/machines/electrodes.md`

Current interpretation: Real practical electrode item, but likely not the reusable process resource itself. It should probably be modeled as consumable tooling or a component of electrolysis equipment, while processes require an electrolysis cell/reactor.

### Primary Path - Choose One

- [ ] Decision ID: `electrodes.reclassify_as_graphite_electrode_set`
  - Action type: `consumable_or_tooling_modeling`, `rename_or_alias`, `reference_migration`
  - Action: Reclassify or replace `electrodes` with a part/consumable tooling item such as `graphite_electrode_set_v0`.
  - Queue task: Move `electrodes` out of machine-style resource modeling where appropriate; preserve it as an input, BOM component, or maintenance consumable for electrolysis/MRE/FFC equipment; update references to a clearer graphite electrode set ID.

- [ ] Decision ID: `electrodes.keep_generic_component_item`
  - Action type: `note_cleanup`, `consumable_or_tooling_modeling`
  - Action: Keep `electrodes` as a generic component/tooling item but document that it is not the standalone electrolysis resource.
  - Queue task: Add notes clarifying that `electrodes` represents electrode stock or a generic replaceable electrode set, not the capital equipment that performs electrolysis.

- [ ] Decision ID: `electrodes.no_action`
  - Action type: `no_action`
  - Action: Leave `electrodes` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `electrodes.replace_machine_requirements_with_cell`
  - Action type: `process_requirement_update`, `reference_migration`
  - Action: Replace `machine_id: electrodes` style requirements with actual reusable process resources such as `mre_reactor_v0` or `electrolysis_cell_unit_v0`.
  - Queue task: Audit electrolysis and molten regolith processes; use the appropriate electrolysis cell/reactor as the process resource and model electrodes as consumed inputs, installed components, or maintenance parts.

- [ ] Decision ID: `electrodes.dedupe_with_electrode_set_mre`
  - Action type: `dedupe_or_consolidation`
  - Action: Decide whether `electrodes` should be deprecated in favor of `electrode_set_mre` or retained as a generic graphite electrode set.
  - Queue task: Compare `electrodes`, `electrode_set_mre`, and related material-specific electrode items; consolidate or document scope boundaries among generic graphite, MRE-specific, refractory-metal, battery, and welding electrode concepts.

- [ ] Decision ID: `electrodes.model_lifetime_and_consumption`
  - Action type: `consumable_or_tooling_modeling`, `process_requirement_update`
  - Action: Add electrode lifetime, replacement, and consumption assumptions for high-temperature electrolysis.
  - Queue task: Determine which electrolysis processes consume electrode mass versus only require installed electrode surfaces, then add replacement/lifetime assumptions or consumable rates where justified.

- [ ] Decision ID: `electrodes.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## electrolysis_cell_unit_v0

Source review: `research/machines/electrolysis_cell_unit_v0.md`

Current interpretation: Real electrochemical machine category, but current KB item is over-generic and internally inconsistent across chlor-alkali, aqueous electrowinning, Hall-Heroult, and molten-salt/regolith uses.

### Primary Path - Choose One

- [ ] Decision ID: `electrolysis_cell_unit_v0.keep_as_generic_placeholder`
  - Action type: `note_cleanup`, `deferred_schema_or_modeling_decision`
  - Action: Keep the item as a temporary generic electrochemical-cell placeholder for early closure/provenance work.
  - Queue task: Rename or document `electrolysis_cell_unit_v0` as a generic placeholder, explicitly warning that it is not a realistic universal cell for chlor-alkali, Hall-Heroult, electrowinning, and molten-regolith electrolysis.

- [ ] Decision ID: `electrolysis_cell_unit_v0.split_by_chemistry`
  - Action type: `split_item`, `process_requirement_update`, `bom_or_recipe_update`
  - Action: Split current uses into chemistry-specific electrolysis resources.
  - Queue task: Create or route requirements to distinct machine/resource classes such as `chloralkali_membrane_cell`, `aqueous_electrowinning_cell`, and `hall_heroult_reduction_cell`; update current process requirements and recipes accordingly.

- [ ] Decision ID: `electrolysis_cell_unit_v0.no_action`
  - Action type: `no_action`
  - Action: Leave the generic electrolysis cell unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `electrolysis_cell_unit_v0.route_molten_regolith_to_specific_reactors`
  - Action type: `process_requirement_update`, `reference_migration`
  - Action: Route molten-regolith and FFC-style electrolysis to `mre_reactor_v0`, `ffc_reactor_unit_v0`, or another specific reactor rather than the generic cell.
  - Queue task: Audit molten-salt/regolith electrolysis processes and replace generic electrolysis-cell requirements with the selected MRE/FFC reactor resources where appropriate.

- [ ] Decision ID: `electrolysis_cell_unit_v0.scale_or_replace_hall_heroult_use`
  - Action type: `process_requirement_update`, `split_item`
  - Action: Do not use a 25 kg generic cell as a realistic Hall-Heroult pot unless explicitly modeled as a lab/demo cell.
  - Queue task: Review `aluminum_smelting_hall_heroult_v0`; either mark the process as lab/demo scale using a correspondingly small cell or introduce a realistic Hall-Heroult reduction cell/pot resource with matching BOM and energy assumptions.

- [ ] Decision ID: `electrolysis_cell_unit_v0.complete_aqueous_electrowinning_bom`
  - Action type: `bom_or_recipe_update`
  - Action: If retained for cobalt or similar aqueous electrowinning, add tank, plate electrodes, bus bars, circulation, ventilation, and power-interface assumptions.
  - Queue task: Update the electrowinning cell model or create a dedicated aqueous electrowinning cell with realistic components and process requirements.

- [ ] Decision ID: `electrolysis_cell_unit_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## enclosure_small

Source review: `research/machines/enclosure_small.md`

Current interpretation: Real standard electronics/electrical enclosure, but it is best treated as a part or subassembly rather than the reusable process resource itself. Its current `kind: machine` and one `machine_id` use are likely legacy/modeling artifacts.

### Primary Path - Choose One

- [ ] Decision ID: `enclosure_small.reclassify_as_part_or_subassembly`
  - Action type: `consumable_or_tooling_modeling`, `rename_or_alias`, `reference_migration`
  - Action: Reclassify `enclosure_small` from machine-style modeling to a part/subassembly classification if the schema supports it.
  - Queue task: Update `enclosure_small` so it behaves as an electronics/electrical enclosure component; migrate any process-resource uses to the actual assembly tool, fixture, or workcell resource that performs the operation.

- [ ] Decision ID: `enclosure_small.keep_as_capability_carrier`
  - Action type: `deferred_schema_or_modeling_decision`, `note_cleanup`
  - Action: Keep `enclosure_small` in its current kind only if the schema needs it to advertise reusable housing/enclosure capabilities.
  - Queue task: Add notes documenting why `enclosure_small` remains machine-kind despite being a component, and clarify that it is not a capital production asset.

- [ ] Decision ID: `enclosure_small.no_action`
  - Action type: `no_action`
  - Action: Leave `enclosure_small` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `enclosure_small.rename_for_clarity`
  - Action type: `rename_or_alias`
  - Action: Rename or alias to `electronics_enclosure_small` or `electrical_enclosure_small`.
  - Queue task: Decide whether to rename the item for clearer scope; update references or add aliases so existing recipes and BOMs remain interpretable.

- [ ] Decision ID: `enclosure_small.split_material_variants`
  - Action type: `split_item`, `bom_or_recipe_update`
  - Action: Separate steel sheet-metal and polymer printed enclosure assumptions if material properties matter.
  - Queue task: Preserve both manufacturing routes but clarify or split material assumptions so the additive polymer route does not silently produce a steel enclosure for high-temperature, EMI, fire-rated, vacuum, or impact-sensitive contexts.

- [ ] Decision ID: `enclosure_small.audit_computer_core_machine_requirement`
  - Action type: `process_requirement_update`
  - Action: Review `computer_core_assembly_v0` using `enclosure_small` as a `machine_id`.
  - Queue task: Replace `enclosure_small` as a process resource in `computer_core_assembly_v0` unless the intended resource is specifically an assembly fixture/chassis; model the enclosure as an input part instead.

- [ ] Decision ID: `enclosure_small.keep_import_option`
  - Action type: `reference_migration`, `note_cleanup`
  - Action: Keep a purchased/import path for bootstrap scenarios.
  - Queue task: Ensure early bootstrap or import-stub modeling treats small commercial enclosures as standard purchased parts rather than special capital machines.

- [ ] Decision ID: `enclosure_small.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## epoxy_synthesis_unit

Source review: `research/machines/epoxy_synthesis_unit.md`

Current interpretation: Real small resin synthesis reactor/skid category, but current usage is too generic and the BOM/recipe are placeholders for actual epoxy/resin process equipment.

### Primary Path - Choose One

- [ ] Decision ID: `epoxy_synthesis_unit.keep_as_resin_synthesis_skid`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Define `epoxy_synthesis_unit` specifically as a small epoxy/resin synthesis reactor or skid.
  - Queue task: Update item notes, BOM, and recipe assumptions for `epoxy_synthesis_unit` to include stirred reactor, heating/cooling, feed addition, condensation/distillation or solvent recovery, washing/separation, corrosion-compatible materials, controls, and waste/byproduct handling.

- [ ] Decision ID: `epoxy_synthesis_unit.replace_with_generic_reactor_for_synthesis`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Model epoxy resin production as generic stirred-reactor chemistry plus separation instead of a dedicated epoxy machine.
  - Queue task: Replace or deprecate `epoxy_synthesis_unit` in favor of `chemical_reactor_basic`, `generic_chemical_reactor_v0`, `chemical_reactor_vessel_v0`, and any required separation/vacuum/distillation resources for epoxy resin synthesis.

- [ ] Decision ID: `epoxy_synthesis_unit.use_mixer_for_formulation_only`
  - Action type: `reference_migration`, `process_requirement_update`
  - Action: If the KB only needs epoxy mixing/formulation/curing, use a mixer or dispensing station rather than synthesis equipment.
  - Queue task: Audit epoxy processes and distinguish resin synthesis from purchased resin formulation; route formulation-only work to mixer/dispensing resources and keep synthesis equipment only where base resin is produced from feedstocks.

- [ ] Decision ID: `epoxy_synthesis_unit.no_action`
  - Action type: `no_action`
  - Action: Leave the epoxy synthesis unit unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `epoxy_synthesis_unit.remove_unrelated_hcl_use`
  - Action type: `process_requirement_update`, `reference_migration`
  - Action: Move `hcl_synthesis_from_h2_cl2_v0` off the epoxy unit.
  - Queue task: Replace `epoxy_synthesis_unit` in HCl synthesis with `chemical_reactor_basic` or a specific HCl reactor/resource suited to hydrogen-chlorine chemistry.

- [ ] Decision ID: `epoxy_synthesis_unit.remove_unrelated_mos2_use`
  - Action type: `process_requirement_update`, `reference_migration`
  - Action: Move `mos2_solid_lubricant_synthesis_v0` off the epoxy unit unless epoxy equipment is truly needed.
  - Queue task: Replace `epoxy_synthesis_unit` in MoS2 solid-lubricant synthesis with `generic_chemical_reactor_v0` or a more specific sulfur/solid-lubricant synthesis reactor.

- [ ] Decision ID: `epoxy_synthesis_unit.add_scale_and_feedstock_assumptions`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Add scale and feedstock assumptions for the 200 kg unit.
  - Queue task: Document whether this is a lab, pilot, or small production resin unit; specify assumed epoxy feedstocks and whether it handles epichlorohydrin/caustic/BPA-style chemistry or another pathway.

- [ ] Decision ID: `epoxy_synthesis_unit.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## excavator_basic

Source review: `research/machines/excavator_basic.md`

Current interpretation: Real practical compact excavator resource; 2000 kg is plausible for a mini excavator, but lunar environment and throughput scope need explicit limits.

### Primary Path - Choose One

- [ ] Decision ID: `excavator_basic.scope_as_terrestrial_style_mini_excavator`
  - Action type: `note_cleanup`
  - Action: Scope the item as a compact terrestrial-style electric/hydraulic mini excavator analog.
  - Queue task: Update notes to preserve the 2000 kg compact-excavator interpretation and warn that it is not a proxy for large mining equipment, deep mining, hard-rock ripping, or high-throughput excavation.

- [ ] Decision ID: `excavator_basic.scope_as_lunar_adapted_excavator`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Treat the item as a lunar-adapted small regolith excavator rather than a direct terrestrial mini-excavator.
  - Queue task: Add lunar-operation assumptions for low-gravity traction, abrasive dust, thermal/vacuum compatibility, autonomy, power source, bucket wear, and hydraulic fluid/seal limits; adjust BOM if electric actuators or sealed hydraulics are selected.

- [ ] Decision ID: `excavator_basic.no_action`
  - Action type: `no_action`
  - Action: Leave `excavator_basic` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `excavator_basic.separate_specialized_excavation_cases`
  - Action type: `process_requirement_update`
  - Action: Use specialized resources for ice-cemented polar regolith, hard rock, subsurface sampling, or drilling.
  - Queue task: Audit excavation/mining processes and route hard rock, polar ice, and subsurface sampling work to `drilling_equipment_v0` or other specialized excavation resources rather than assuming `excavator_basic` covers them.

- [ ] Decision ID: `excavator_basic.keep_loader_distinct`
  - Action type: `dedupe_or_consolidation`, `process_requirement_update`
  - Action: Keep `loader_small` distinct for scooping and short-haul material handling.
  - Queue task: Review processes that need loading/transport rather than boom digging; use `loader_small` or another haulage resource instead of `excavator_basic` where appropriate.

- [ ] Decision ID: `excavator_basic.add_throughput_and_bucket_capacity`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Add bucket capacity and throughput assumptions for regolith mining.
  - Queue task: Estimate or document expected bucket volume, cycle time, and throughput for `excavator_basic` so process rates do not silently imply larger equipment.

- [ ] Decision ID: `excavator_basic.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## fixturing_workbench

Source review: `research/machines/fixturing_workbench.md`

Current interpretation: Real passive workholding/shop infrastructure for welding and fabrication. It should remain distinct from a generic bench because fixture pattern, clamps, stops, flatness, and load rating provide process capability.

### Primary Path - Choose One

- [ ] Decision ID: `fixturing_workbench.keep_as_distinct_workholding_resource`
  - Action type: `note_cleanup`
  - Action: Keep `fixturing_workbench` as a distinct reusable workholding resource for welding and structural fabrication.
  - Queue task: Clarify notes/classification so `fixturing_workbench` is treated as tooling/workholding/shop equipment with `fixturing_table` capability, separate from `workbench_basic` and `assembly_workbench_v0`.

- [ ] Decision ID: `fixturing_workbench.merge_with_generic_workbench`
  - Action type: `dedupe_or_consolidation`
  - Action: Consolidate into a generic workbench only if precision fixturing is not needed.
  - Queue task: Compare `fixturing_workbench`, `workbench_basic`, `assembly_workbench_v0`, and related table items; merge only if process requirements do not need fixture-table flatness, hole/T-slot patterns, clamps, stops, or repeatable alignment.

- [ ] Decision ID: `fixturing_workbench.no_action`
  - Action type: `no_action`
  - Action: Leave `fixturing_workbench` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `fixturing_workbench.model_accessory_set`
  - Action type: `bom_or_recipe_update`, `consumable_or_tooling_modeling`
  - Action: Add or preserve accessory items such as clamps, stops, squares, fixture plates, and vise mounting hardware.
  - Queue task: Review BOM and related items for `fixturing_workbench`; ensure process capability includes practical fixture accessories, not only a table frame/top.

- [ ] Decision ID: `fixturing_workbench.add_size_flatness_load_limits`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Add table size, flatness, and load-rating assumptions so it is not treated as unlimited.
  - Queue task: Document the 150 kg table's approximate working envelope, load rating, and precision grade; audit large-frame fabrication processes for requirements beyond this table.

- [ ] Decision ID: `fixturing_workbench.define_precision_grades`
  - Action type: `split_item`, `deferred_schema_or_modeling_decision`
  - Action: Introduce rough welding-table versus higher-precision metrology/alignment fixture grades if needed.
  - Queue task: Decide whether separate fixture-table precision grades are needed and add/link items accordingly.

- [ ] Decision ID: `fixturing_workbench.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## forging_press_v0

Source review: `research/machines/forging_press_v0.md`

Current interpretation: Real compact hot-forging press resource, plausible at 850 kg, but it overlaps with general `hydraulic_press` and `power_hammer_or_press` unless sustained controlled hot-forging force is specifically needed.

### Primary Path - Choose One

- [ ] Decision ID: `forging_press_v0.keep_dedicated_hot_forging_press`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep `forging_press_v0` for controlled hot forging under sustained press force.
  - Queue task: Clarify the item and `metal_forging_process_v0` requirements so `forging_press_v0` is used only where hot-forging press duty, frame rigidity, ram guidance, dies, stroke/speed, and thermal environment matter.

- [ ] Decision ID: `forging_press_v0.consolidate_to_existing_press_or_hammer`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Dedupe if current uses can be satisfied by `hydraulic_press` or `power_hammer_or_press` plus a heat source.
  - Queue task: Review `metal_forging_process_v0`; migrate to `hydraulic_press` for general pressing/cold forming or `power_hammer_or_press` for impact forging if dedicated press forging is not required, and deprecate or alias `forging_press_v0` if unused.

- [ ] Decision ID: `forging_press_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `forging_press_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `forging_press_v0.add_force_rating`
  - Action type: `note_cleanup`
  - Action: Add the force rating implied by the 850 kg compact press.
  - Queue task: Estimate or document a conservative tonnage/force rating and working envelope for `forging_press_v0` so process uses do not imply industrial-scale forging.

- [ ] Decision ID: `forging_press_v0.add_tooling_and_heat_requirements`
  - Action type: `process_requirement_update`, `consumable_or_tooling_modeling`
  - Action: Add die/tooling and heat-source assumptions to forging processes.
  - Queue task: Ensure forging processes require appropriate dies/anvils/tooling and a heat source such as `induction_forge_v0`; the press alone should not imply metal heating.

- [ ] Decision ID: `forging_press_v0.add_safety_performance_notes`
  - Action type: `note_cleanup`
  - Action: Document local-build safety and performance constraints.
  - Queue task: Add notes for frame deflection, weld quality, hydraulic pressure relief, die retention, hot scale, guarding, and ram alignment if local fabrication remains modeled.

- [ ] Decision ID: `forging_press_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## furnace_basic

Source review: `research/machines/furnace_basic.md`

Current interpretation: Real useful generic 200-1200 C refractory-lined box/crucible furnace. It should remain the moderate-temperature default, but not a catch-all for controlled-atmosphere, high-temperature, reduction, heat-treatment, glass, or foundry-specific work.

### Primary Path - Choose One

- [ ] Decision ID: `furnace_basic.keep_as_moderate_temp_generic_furnace`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep `furnace_basic` as the canonical general-purpose 200-1200 C furnace with explicit scope limits.
  - Queue task: Update notes and process guidance so `furnace_basic` means a general refractory-lined box/crucible furnace for moderate-temperature heating, calcination, basic annealing/stress relief, ceramic firing within range, and simple low-scale melting where atmosphere/pouring details are not critical.

- [ ] Decision ID: `furnace_basic.split_box_and_crucible_variants`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split into box/muffle and crucible/melting variants if current uses need different equipment.
  - Queue task: Review process uses of `furnace_basic`; introduce separate box/muffle and crucible/melting furnace resources only where process requirements differ materially.

- [ ] Decision ID: `furnace_basic.no_action`
  - Action type: `no_action`
  - Action: Leave `furnace_basic` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `furnace_basic.route_high_temp_to_furnace_high_temp`
  - Action type: `process_requirement_update`, `reference_migration`
  - Action: Move processes above roughly 1200-1300 C to `furnace_high_temp`.
  - Queue task: Audit `furnace_basic` process references and migrate high-temperature uses to `furnace_high_temp` where required.

- [ ] Decision ID: `furnace_basic.route_reduction_chemistry_to_reduction_furnace`
  - Action type: `process_requirement_update`, `reference_migration`
  - Action: Move reduction/offgas/reductant-control chemistry to `reduction_furnace_v0`.
  - Queue task: Audit reduction, carbothermal, and atmosphere-sensitive chemistry processes using `furnace_basic`; replace with `reduction_furnace_v0` or add required gas/offgas resources.

- [ ] Decision ID: `furnace_basic.route_metallurgical_heat_treatment`
  - Action type: `process_requirement_update`, `reference_migration`
  - Action: Use `heat_treatment_furnace_v0` where controlled heat-treatment cycles are central.
  - Queue task: Audit annealing, hardening, stress-relief, and metallurgy-specific heat-treatment processes; move from `furnace_basic` to `heat_treatment_furnace_v0` where cycle control and quench/cooling integration matter.

- [ ] Decision ID: `furnace_basic.route_glass_work_to_glass_furnace`
  - Action type: `process_requirement_update`, `reference_migration`
  - Action: Use `glass_furnace_v0` for glass melting/forming where refractory chemistry, fining, tank/crucible design, or forming access matter.
  - Queue task: Audit glass processes currently using `furnace_basic` and migrate to `glass_furnace_v0` where appropriate.

- [ ] Decision ID: `furnace_basic.add_foundry_support_requirements`
  - Action type: `process_requirement_update`, `consumable_or_tooling_modeling`
  - Action: Add crucibles, tongs/lifting/pouring tools, mold handling, spill containment, and quench/cooling stations where furnace processes need them.
  - Queue task: Review melting/casting and heat-treatment processes using `furnace_basic`; add support-tooling and handling requirements not represented by the furnace alone.

- [ ] Decision ID: `furnace_basic.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## furnace_high_temp

Source review: `research/machines/furnace_high_temp.md`

Current interpretation: Real important high-temperature furnace category, but the current 1600-3000 C span covers multiple practical design classes and should not absorb moderate-temperature, heat-treatment, drying, or vacuum-specific work by default.

### Primary Path - Choose One

- [ ] Decision ID: `furnace_high_temp.keep_broad_high_temp_family`
  - Action type: `note_cleanup`
  - Action: Keep `furnace_high_temp` as a broad high-temperature furnace family for current KB scale.
  - Queue task: Clarify notes that `furnace_high_temp` is a coarse high-temperature family, distinct from `furnace_basic`, `drying_oven`, and `heat_treatment_furnace_v0`, with further specialization deferred.

- [ ] Decision ID: `furnace_high_temp.split_1600_1800_and_ultra_high_temp`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split ordinary 1600-1800 C furnace uses from 2500-3000 C graphite/vacuum/hydrogen furnace uses.
  - Queue task: Create or route processes between a 1600-1800 C high-temperature chamber/sintering furnace and an ultra-high-temperature graphite/vacuum or hydrogen furnace for graphitization, refractory-metal sintering, and oxygen-free 2500-3000 C work.

- [ ] Decision ID: `furnace_high_temp.no_action`
  - Action type: `no_action`
  - Action: Leave `furnace_high_temp` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `furnace_high_temp.audit_temperature_requirements`
  - Action type: `process_requirement_update`
  - Action: Identify which processes truly require 2500-3000 C versus 1600-1800 C.
  - Queue task: Audit all `furnace_high_temp` process references and record required temperature ranges; downgrade uses to `furnace_basic` or a 1600-1800 C furnace where ultra-high-temperature capability is not needed.

- [ ] Decision ID: `furnace_high_temp.require_atmosphere_for_sensitive_work`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Add explicit vacuum, inert, hydrogen, gas handling, chamber seals, cooling, and pyrometry requirements where needed.
  - Queue task: For tungsten sintering, graphitization, refractory metals, and oxygen-sensitive materials, add `vacuum_furnace_v0` or atmosphere/gas-handling requirements rather than relying on a generic high-temperature furnace.

- [ ] Decision ID: `furnace_high_temp.separate_solar_heat_source`
  - Action type: `split_item`, `infrastructure_or_subsystem_modeling`
  - Action: Treat solar concentration as a separate heat source/receiver system rather than part of the furnace item.
  - Queue task: Review furnace notes and processes using solar concentration; model `solar_concentrator_fresnel` or a receiver as a separate resource feeding a furnace/thermal receiver if selected.

- [ ] Decision ID: `furnace_high_temp.audit_overuse_for_drying_or_basic_heating`
  - Action type: `process_requirement_update`, `reference_migration`
  - Action: Move low/moderate-temperature uses to `drying_oven` or `furnace_basic`.
  - Queue task: Audit recipes currently requiring `furnace_high_temp`; migrate drying, curing, moderate calcination, and basic heating uses to the appropriate lower-temperature resource.

- [ ] Decision ID: `furnace_high_temp.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## generic_chemical_reactor_v0

Source review: `research/machines/generic_chemical_reactor_v0.md`

Current interpretation: Real reactor equipment family, but this item is a coarse closure placeholder rather than one universal physical reactor for all chemistry. It can stand for a small stirred/jacketed reactor only within explicit pressure, temperature, corrosion, and safety limits.

### Primary Path - Choose One

- [ ] Decision ID: `generic_chemical_reactor_v0.keep_as_stirred_jacketed_placeholder`
  - Action type: `note_cleanup`, `deferred_schema_or_modeling_decision`
  - Action: Keep as a temporary generic stirred/jacketed reactor placeholder with clear limits.
  - Queue task: Annotate `generic_chemical_reactor_v0` as a coarse stirred/jacketed reactor placeholder, not a universal reactor; document excluded requirements such as high pressure, severe corrosion, high-temperature gas-phase reactions, packed beds, and hazardous relief systems.

- [ ] Decision ID: `generic_chemical_reactor_v0.consolidate_with_chemical_reactor_basic`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Consolidate with `chemical_reactor_basic` if both serve the same coarse reactor role.
  - Queue task: Compare `generic_chemical_reactor_v0`, `chemical_reactor_basic`, `chemical_reactor_vessel_v0`, and `chemical_reactor_unit_v1`; pick one canonical coarse reactor where feasible and migrate or alias duplicate references.

- [ ] Decision ID: `generic_chemical_reactor_v0.split_into_specific_reactor_classes`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Sort current references into reactor classes by chemistry and operating envelope.
  - Queue task: Create or route processes to acid-resistant reactors, pressure reactors/autoclaves, packed-bed catalyst reactors, high-temperature tube reactors, gas-absorption reactors, and stirred batch/CSTR reactors where process conditions require them.

- [ ] Decision ID: `generic_chemical_reactor_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `generic_chemical_reactor_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `generic_chemical_reactor_v0.audit_high_pressure_gas_reactions`
  - Action type: `process_requirement_update`
  - Action: Audit Sabatier, Bosch, RWGS, carbonyl, hydrogenation, and other pressure/gas reactions before using the generic reactor.
  - Queue task: Review high-pressure and gas-phase reactions currently requiring `generic_chemical_reactor_v0`; add pressure-rated reactor, catalyst bed, compressor, relief, gas-handling, and control requirements where needed.

- [ ] Decision ID: `generic_chemical_reactor_v0.audit_corrosive_acid_reactions`
  - Action type: `process_requirement_update`
  - Action: Audit sulfuric/nitric acid, chlorination, hydrothermal, and mineral-acid chemistry for corrosion-compatible equipment.
  - Queue task: Route corrosive chemistry to acid-resistant, glass-lined, polymer-lined, or otherwise compatible reactor resources instead of assuming the generic reactor is safe.

- [ ] Decision ID: `generic_chemical_reactor_v0.complete_250kg_scope`
  - Action type: `bom_or_recipe_update`, `note_cleanup`
  - Action: Clarify what the 250 kg mass includes.
  - Queue task: Document whether `generic_chemical_reactor_v0` includes jacket/coil, agitator, seals, controls, relief valves, corrosion lining, and instrumentation; update BOM if selected.

- [ ] Decision ID: `generic_chemical_reactor_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## glass_furnace_v0

Source review: `research/machines/glass_furnace_v0.md`

Current interpretation: Real small glass melting furnace resource. The 1400 kg item is plausible for lab/studio/pilot production, but not for industrial continuous tank, float-glass, or container-glass capacity.

### Primary Path - Choose One

- [ ] Decision ID: `glass_furnace_v0.scope_as_small_electric_glass_melter`
  - Action type: `note_cleanup`
  - Action: Clarify `glass_furnace_v0` as a small electric glass melting furnace.
  - Queue task: Update item notes to describe a small refractory-lined electric pot/crucible/day-tank-style glass furnace with high-current heating, temperature control, cooling where needed, and molten-glass containment.

- [ ] Decision ID: `glass_furnace_v0.split_large_industrial_tank_furnace`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Add separate large tank/forehearth/forming-line equipment if industrial glass capacity is needed.
  - Queue task: Create or route large-scale float-glass, container-glass, continuous tank, forehearth, or forming-line processes to separate industrial glass furnace/forming resources rather than the 1400 kg small furnace.

- [ ] Decision ID: `glass_furnace_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `glass_furnace_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `glass_furnace_v0.separate_downstream_forming_equipment`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Separate melting from annealing, reheating, forming, forehearth conditioning, fibers, envelopes, sheets, or precision glass-part equipment where needed.
  - Queue task: Audit glass processes using `glass_furnace_v0`; add downstream forming/annealing/conditioning resources where the furnace alone is not sufficient.

- [ ] Decision ID: `glass_furnace_v0.verify_refractory_by_glass_type`
  - Action type: `process_requirement_update`, `bom_or_recipe_update`
  - Action: Check quartz, aluminosilicate, basalt, and other melts for temperature and refractory compatibility.
  - Queue task: Document whether one generic refractory furnace is compatible with current glass/basalt melts; add refractory/material constraints or specialized furnace variants where corrosive or higher-temperature melts require them.

- [ ] Decision ID: `glass_furnace_v0.preserve_cooling_and_spill_containment`
  - Action type: `bom_or_recipe_update`, `note_cleanup`
  - Action: Preserve or strengthen cooling loop, refractory shell, and molten-glass spill containment in the BOM.
  - Queue task: Review `bom_glass_furnace_v0` and related recipes to ensure cooling, refractory containment, power distribution, controls, and spill handling are represented.

- [ ] Decision ID: `glass_furnace_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## gravity_separator

Source review: `research/machines/gravity_separator.md`

Current interpretation: Real compact mineral-processing density separator. Current BOM most closely resembles a dry air table/fluidized-bed separator, but process semantics may be broader than one separator type.

### Primary Path - Choose One

- [ ] Decision ID: `gravity_separator.scope_as_dry_air_table`
  - Action type: `rename_or_alias`, `note_cleanup`
  - Action: Scope and optionally rename the item as a dry air-table gravity/density separator.
  - Queue task: Annotate or rename `gravity_separator` to `dry_air_table_gravity_separator` or `gravity_density_separator_table`; align notes/BOM around vibration, air plenum/manifold, porous deck, splitters, and dry granular feed.

- [ ] Decision ID: `gravity_separator.keep_abstract_density_separator`
  - Action type: `deferred_schema_or_modeling_decision`, `note_cleanup`
  - Action: Keep as an abstract density-separation resource covering multiple gravity methods at coarse KB scale.
  - Queue task: Document that `gravity_separator` is an abstract density-separation placeholder and should be specialized later into air tables, wet shaking tables, jigs, spirals, or centrifugal concentrators when process detail requires it.

- [ ] Decision ID: `gravity_separator.split_separator_methods`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split dry air table, wet shaking table, jig, spiral, and centrifugal concentrator methods.
  - Queue task: Review current mineral concentration and tungsten processes; assign each to a specific density-separation machine based on particle size, medium, throughput, density contrast, and gravity environment.

- [ ] Decision ID: `gravity_separator.no_action`
  - Action type: `no_action`
  - Action: Leave `gravity_separator` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `gravity_separator.add_process_assumptions`
  - Action type: `process_requirement_update`, `note_cleanup`
  - Action: Add particle size, feed preparation, density contrast, moisture, air/water medium, and throughput assumptions.
  - Queue task: Audit processes using `gravity_separator` and document operating assumptions that determine whether density separation is plausible.

- [ ] Decision ID: `gravity_separator.add_lunar_environment_constraints`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Add lunar low-gravity, vacuum, gas/water, and dust-control constraints where relevant.
  - Queue task: For lunar/regolith processes, note that ordinary gravity separation is weakened in low gravity and may require pressurized gas handling, vibration/air fluidization, centrifugal assistance, magnetic/electrostatic alternatives, or explicit dust collection.

- [ ] Decision ID: `gravity_separator.keep_distinct_from_screening`
  - Action type: `dedupe_or_consolidation`, `note_cleanup`
  - Action: Keep density separation distinct from screening/sieving.
  - Queue task: Ensure `gravity_separator` process notes distinguish density/specific-gravity separation from size separation done by `screening_equipment` or `vibrating_screen_v0`.

- [ ] Decision ID: `gravity_separator.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## grinding_wheels

Source review: `research/machines/grinding_wheels.md`

Current interpretation: Real consumable abrasive tooling set. It should be required by grinders and grinding processes, but it is not the active grinder resource itself.

### Primary Path - Choose One

- [ ] Decision ID: `grinding_wheels.reclassify_as_consumable_tooling`
  - Action type: `consumable_or_tooling_modeling`, `reference_migration`
  - Action: Reclassify `grinding_wheels` as tooling/consumable if non-machine process requirements are supported.
  - Queue task: Move `grinding_wheels` out of standalone machine modeling where appropriate; preserve it as required consumable tooling for `surface_grinder`, `bench_grinder`, `bearing_grinding_machine_v0`, `precision_grinding_system_v0`, and grinding processes.

- [ ] Decision ID: `grinding_wheels.keep_as_machine_kind_capability_item`
  - Action type: `deferred_schema_or_modeling_decision`, `note_cleanup`
  - Action: Keep current kind only if the schema needs machine-kind items to express reusable process requirements.
  - Queue task: Add notes explaining that `grinding_wheels` are consumable abrasive tooling despite current machine-kind classification, and that process capability still comes from the grinder plus wheels.

- [ ] Decision ID: `grinding_wheels.no_action`
  - Action type: `no_action`
  - Action: Leave `grinding_wheels` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `grinding_wheels.add_quality_and_safety_steps`
  - Action type: `bom_or_recipe_update`, `note_cleanup`
  - Action: Add dressing, truing, balancing, speed rating, and burst-proof testing assumptions.
  - Queue task: Update `recipe_grinding_wheels_isru_v0` and notes to include wheel grade/grit/porosity/bond control, dressing/truing, balancing, inspection, and speed/proof testing for safety-critical rotating wheels.

- [ ] Decision ID: `grinding_wheels.reconcile_import_placeholder_bom`
  - Action type: `bom_or_recipe_update`, `note_cleanup`
  - Action: Reconcile any BOM/import-placeholder language with the current `is_import: false` ISRU recipe.
  - Queue task: Inspect `grinding_wheels` BOM and recipe metadata; remove or clarify obsolete imported-placeholder notes if the canonical route is local vitrified alumina/glass-bond production.

- [ ] Decision ID: `grinding_wheels.separate_advanced_wheel_variants`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Separate diamond, cBN, high-speed cutoff, silicon-carbide, or other specialized wheels from generic ISRU alumina wheels.
  - Queue task: Audit grinding processes and machine BOMs; require specialized wheel variants only where needed and keep generic ISRU vitrified alumina wheels limited to low-to-medium performance uses.

- [ ] Decision ID: `grinding_wheels.dedupe_with_aluminum_oxide_wheel`
  - Action type: `dedupe_or_consolidation`
  - Action: Decide whether `grinding_wheel_aluminum_oxide` should replace or become a variant of generic `grinding_wheels`.
  - Queue task: Compare `grinding_wheels` and `grinding_wheel_aluminum_oxide`; consolidate, alias, or define variant relationships.

- [ ] Decision ID: `grinding_wheels.model_wear_replacement`
  - Action type: `consumable_or_tooling_modeling`
  - Action: Model wheel wear and replacement if the simulator supports consumable lifetime.
  - Queue task: Add conservative lifetime or replacement assumptions for grinding wheels, or document that current simulation only checks availability of a wheel set.

- [ ] Decision ID: `grinding_wheels.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## hand_tools_basic

Source review: `research/machines/hand_tools_basic.md`

Current interpretation: Real reusable manual tool kit. It is appropriate as a general labor-bot support resource, but it is tooling rather than powered capital equipment and overlaps with specialized hand-tool kits.

### Primary Path - Choose One

- [ ] Decision ID: `hand_tools_basic.reclassify_as_tooling`
  - Action type: `consumable_or_tooling_modeling`, `reference_migration`
  - Action: Reclassify as part/tooling if the schema supports reusable non-machine process resources.
  - Queue task: Move `hand_tools_basic` to an explicit tooling/tool-kit classification while preserving its use as a reusable process requirement for low-complexity manual tasks.

- [ ] Decision ID: `hand_tools_basic.keep_machine_kind_schema_convenience`
  - Action type: `deferred_schema_or_modeling_decision`, `note_cleanup`
  - Action: Keep current classification but document that machine-kind is being used for reusable shop tooling.
  - Queue task: Add notes clarifying that `hand_tools_basic` is a reusable manual tool kit for labor-bot work and not powered process equipment.

- [ ] Decision ID: `hand_tools_basic.no_action`
  - Action type: `no_action`
  - Action: Leave `hand_tools_basic` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `hand_tools_basic.keep_general_fallback`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep `hand_tools_basic` as the general fallback for low-precision manual work with `labor_bot_general_v0`.
  - Queue task: Ensure manual assembly/maintenance processes use `hand_tools_basic` only for ordinary hand-tool work and add specialized tools only when process requirements exceed the generic kit.

- [ ] Decision ID: `hand_tools_basic.consolidate_near_duplicate_kits`
  - Action type: `dedupe_or_consolidation`
  - Action: Avoid proliferating near-identical hand-tool kits.
  - Queue task: Compare `hand_tools_basic`, `hand_tools_mechanical`, `assembly_tools_basic`, `tool_set_general`, and related kits; consolidate or define clear scope boundaries.

- [ ] Decision ID: `hand_tools_basic.keep_specialized_electrical_or_torque_tools`
  - Action type: `consumable_or_tooling_modeling`, `process_requirement_update`
  - Action: Keep insulated electrical tools, crimping tools, torque tools, or other specialized kits distinct where safety or calibration matters.
  - Queue task: Audit processes requiring electrical insulation, crimping, torque calibration, high durability, or other special properties; require specialized tool kits instead of `hand_tools_basic` where needed.

- [ ] Decision ID: `hand_tools_basic.review_mass_and_durability`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Check whether 4.1 kg is enough for the implied kit size and durability.
  - Queue task: Review `hand_tools_basic` BOM/recipe and update mass, steel quality, heat treatment, grip/insulation, tolerances, and durability assumptions if current usage implies a larger industrial kit.

- [ ] Decision ID: `hand_tools_basic.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## hand_tools_electrical

Source review: `research/machines/hand_tools_electrical.md`

Current interpretation: Real reusable electrical hand-tool kit. It should be treated as hand tooling for low-volume wiring/electrical assembly, not as powered equipment and not as a substitute for connector-specific crimping, soldering, or electrical test equipment.

### Primary Path - Choose One

- [ ] Decision ID: `hand_tools_electrical.keep_specialized_electrical_toolkit`
  - Action type: `consumable_or_tooling_modeling`, `note_cleanup`
  - Action: Keep separate from generic hand tools where insulation, wire stripping, electrical safety, or electrical assembly scope matters.
  - Queue task: Clarify `hand_tools_electrical` as a compact electrical hand-tool kit with insulated screwdrivers/pliers, cutters, wire strippers, probes, and terminal-installation hand tools.

- [ ] Decision ID: `hand_tools_electrical.consolidate_into_hand_tools_basic`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Consolidate into `hand_tools_basic` for coarse assembly processes if specialized electrical properties are not modeled.
  - Queue task: Review processes using `hand_tools_electrical`; migrate coarse low-risk assembly uses to `hand_tools_basic` if insulation, stripping, or electrical-specific tooling is not required.

- [ ] Decision ID: `hand_tools_electrical.no_action`
  - Action type: `no_action`
  - Action: Leave `hand_tools_electrical` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `hand_tools_electrical.reclassify_as_tooling`
  - Action type: `consumable_or_tooling_modeling`
  - Action: Reclassify as reusable tooling if the schema supports it.
  - Queue task: Move `hand_tools_electrical` to a tooling/tool-kit classification while preserving process-resource semantics.

- [ ] Decision ID: `hand_tools_electrical.keep_crimping_tools_distinct`
  - Action type: `process_requirement_update`, `dedupe_or_consolidation`
  - Action: Do not let `hand_tools_electrical` replace connector-specific crimping tools where crimp quality matters.
  - Queue task: Audit cable harness, terminal, and connector processes; require `wire_crimping_tools` or `crimping_tool_set` where connector-specific dies and validated crimps are needed.

- [ ] Decision ID: `hand_tools_electrical.keep_soldering_and_test_equipment_distinct`
  - Action type: `process_requirement_update`
  - Action: Keep soldering stations, multimeters, and electrical test benches distinct from the hand-tool kit.
  - Queue task: Review electrical assembly/test processes and ensure `soldering_station`, `multimeter_set`, or `test_bench_electrical` are required where heating, measurement, calibration, or powered testing is needed.

- [ ] Decision ID: `hand_tools_electrical.add_insulation_requirement`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Add dielectric insulation and testing assumptions if live-circuit or electrical-safety work is modeled.
  - Queue task: Update BOM/recipe notes for insulated handles, dielectric materials, insulation coverage, and test requirements if the kit is used for live or safety-critical electrical work.

- [ ] Decision ID: `hand_tools_electrical.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## hand_tools_mechanical

Source review: `research/machines/hand_tools_mechanical.md`

Current interpretation: Real reusable mechanical hand-tool kit. It is useful as tool inventory for maintenance, assembly, tensioning, deburring, and adjustment, but overlaps with `hand_tools_basic` and `assembly_tools_basic`.

### Primary Path - Choose One

- [ ] Decision ID: `hand_tools_mechanical.keep_specialized_mechanical_toolkit`
  - Action type: `consumable_or_tooling_modeling`, `note_cleanup`
  - Action: Keep as a robust mechanical maintenance and assembly tool kit distinct from generic basic tools.
  - Queue task: Clarify `hand_tools_mechanical` as reusable tool inventory for wrenches, sockets, screwdrivers, pliers, hammers, Allen keys, punches, files, and related mechanical work.

- [ ] Decision ID: `hand_tools_mechanical.consolidate_into_basic_or_assembly_tools`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Consolidate into `hand_tools_basic` or `assembly_tools_basic` for coarse process modeling.
  - Queue task: Compare usage of `hand_tools_mechanical`, `hand_tools_basic`, and `assembly_tools_basic`; migrate references and deprecate/alias duplicates if separate mechanical scope does not change process capability.

- [ ] Decision ID: `hand_tools_mechanical.no_action`
  - Action type: `no_action`
  - Action: Leave `hand_tools_mechanical` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `hand_tools_mechanical.reclassify_as_tooling`
  - Action type: `consumable_or_tooling_modeling`
  - Action: Reclassify as reusable tooling/tool inventory if the schema supports it.
  - Queue task: Move `hand_tools_mechanical` to a tooling classification while preserving reusable process-resource behavior.

- [ ] Decision ID: `hand_tools_mechanical.keep_powered_equipment_distinct`
  - Action type: `process_requirement_update`
  - Action: Do not use mechanical hand tools as substitutes for powered cutting, machining, pressing, welding, or precision metrology.
  - Queue task: Audit processes using `hand_tools_mechanical`; add powered equipment, inspection tools, or specialized fixtures where the required work exceeds manual hand-tool capability.

- [ ] Decision ID: `hand_tools_mechanical.review_deburring_requirement`
  - Action type: `process_requirement_update`, `consumable_or_tooling_modeling`
  - Action: Check whether `finishing_deburring_v0` needs a specific deburring/cutting-tool kit rather than general mechanical tools.
  - Queue task: Review `finishing_deburring_v0`; require files, deburring tools, abrasive papers/wheels, or powered finishing tools as appropriate.

- [ ] Decision ID: `hand_tools_mechanical.define_bootstrap_tool_inventory`
  - Action type: `deferred_schema_or_modeling_decision`, `note_cleanup`
  - Action: Decide whether bootstrap inventory should include one general kit or multiple specialized kits.
  - Queue task: Document the intended relationship among `hand_tools_basic`, `hand_tools_mechanical`, and `hand_tools_electrical` in bootstrap/self-reproduction inventory.

- [ ] Decision ID: `hand_tools_mechanical.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## heat_treatment_furnace_v0

Source review: `research/machines/heat_treatment_furnace_v0.md`

Current interpretation: Real programmable chamber heat-treatment furnace for controlled metal thermal cycles. It should remain distinct from generic heating, reduction, sintering, glass, and ultra-high-temperature furnaces.

### Primary Path - Choose One

- [ ] Decision ID: `heat_treatment_furnace_v0.keep_programmable_chamber_furnace`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep as a programmable chamber heat-treatment furnace for hardening, tempering, annealing, and stress relief.
  - Queue task: Update notes/process guidance to emphasize ramp/soak/cool cycle control, temperature uniformity, part handling, and metallurgy-specific use; keep distinct from `furnace_basic`, `furnace_high_temp`, `reduction_furnace_v0`, and `sintering_furnace_v0`.

- [ ] Decision ID: `heat_treatment_furnace_v0.consolidate_to_furnace_basic`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Consolidate only if controlled metallurgical cycle modeling is intentionally out of scope.
  - Queue task: Review all heat-treatment processes; migrate to `furnace_basic` only if the KB deliberately treats heat treatment as generic moderate-temperature heating without cycle/uniformity/quench requirements.

- [ ] Decision ID: `heat_treatment_furnace_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `heat_treatment_furnace_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `heat_treatment_furnace_v0.add_controlled_atmosphere_requirements`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Add controlled-atmosphere, vacuum, oxygen-control, or protective-gas hardware where processes require it.
  - Queue task: Audit carburizing, nitriding, bright annealing, oxidation-sensitive alloys, brazing, and advanced heat-treatment processes; add gas/vacuum/atmosphere resources rather than assuming the basic heat-treatment furnace includes them.

- [ ] Decision ID: `heat_treatment_furnace_v0.link_quench_tank_for_hardening`
  - Action type: `process_requirement_update`
  - Action: Link hardening operations to a separate quench tank or cooling station if hardening is modeled.
  - Queue task: Review hardening processes and add `quench_tank` or cooling-station requirements where quenching is required; preserve quench racks/baskets as handling accessories.

- [ ] Decision ID: `heat_treatment_furnace_v0.add_temperature_uniformity_assumption`
  - Action type: `note_cleanup`
  - Action: Add maximum temperature and temperature-uniformity assumptions.
  - Queue task: Document the furnace's maximum temperature, working volume, temperature uniformity, calibration expectations, and whether it needs temperature uniformity surveys.

- [ ] Decision ID: `heat_treatment_furnace_v0.review_alnico_special_requirements`
  - Action type: `process_requirement_update`, `research_or_design_followup`
  - Action: Check whether AlNiCo heat treatment requires magnetic-field fixtures or special atmosphere.
  - Queue task: Review `alnico_heat_treatment_v0`; add magnetic-field fixture, atmosphere, or process-specific requirements if needed.

- [ ] Decision ID: `heat_treatment_furnace_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## heating_furnace

Source review: `research/machines/heating_furnace.md`

Current interpretation: Real 600-1200 C heating/preheating furnace category, but likely overlaps with `furnace_basic` unless it is specifically a preheat furnace for rolling/forming lines or getter activation.

### Primary Path - Choose One

- [ ] Decision ID: `heating_furnace.consolidate_to_furnace_basic`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Consolidate into `furnace_basic` if it only means general moderate-temperature heating.
  - Queue task: Review all `heating_furnace` references; migrate general 600-1200 C heating, moderate heat treatment, and ordinary furnace uses to `furnace_basic`, then deprecate or alias `heating_furnace` if no distinct duty remains.

- [ ] Decision ID: `heating_furnace.rename_as_preheating_furnace`
  - Action type: `rename_or_alias`, `process_requirement_update`
  - Action: Keep separate as a dedicated preheating furnace for rolling/forming or getter activation.
  - Queue task: Rename or annotate as `preheating_furnace` and document the distinct duty, chamber/load assumptions, workflow role, and why it is separate from `furnace_basic`.

- [ ] Decision ID: `heating_furnace.no_action`
  - Action type: `no_action`
  - Action: Leave `heating_furnace` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `heating_furnace.keep_temp_scope_distinct`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep this item distinct from `furnace_high_temp` and `drying_oven` by temperature and duty.
  - Queue task: Add notes or process checks so `heating_furnace` does not cover high-temperature carbothermal/sintering/MRE work and does not replace low-temperature drying/moisture-removal ovens.

- [ ] Decision ID: `heating_furnace.clarify_mass_and_handling`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Clarify whether the 512 kg mass includes power conditioning and material handling.
  - Queue task: Document chamber size, load mass, power conditioning, and material handling assumptions for the 512 kg furnace if it remains separate.

- [ ] Decision ID: `heating_furnace.review_self_reproducing_set_duplicate`
  - Action type: `dedupe_or_consolidation`
  - Action: Decide whether the self-reproducing set needs both `furnace_basic` and `heating_furnace`.
  - Queue task: Review bootstrap/self-reproducing machine lists and dedupe decisions; remove duplicate moderate-temperature furnace entries unless each has a distinct process role.

- [ ] Decision ID: `heating_furnace.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## heating_plate_induction_heater

Source review: `research/machines/heating_plate_induction_heater.md`

Current interpretation: Real small heating equipment, but the current item combines induction bearing/shrink-fit heating with resistive hot-plate/general heating-plate roles.

### Primary Path - Choose One

- [ ] Decision ID: `heating_plate_induction_heater.rename_as_thermal_fit_heater`
  - Action type: `rename_or_alias`, `note_cleanup`
  - Action: Scope the item around bearing installation and thermal-fit/shrink-fit heating.
  - Queue task: Rename or annotate as `thermal_fit_heater_v0` or `induction_bearing_heater_v0`; document use for bearing/ring/housing/toolholder expansion and local induction or bearing-heater operation.

- [ ] Decision ID: `heating_plate_induction_heater.rename_as_controlled_heating_plate`
  - Action type: `rename_or_alias`, `reference_migration`
  - Action: Scope the item as a general controlled resistive heating plate.
  - Queue task: Rename or annotate as `controlled_heating_plate_v0`; route bearing thermal-fit work elsewhere if induction-specific capability is needed.

- [ ] Decision ID: `heating_plate_induction_heater.split_induction_and_resistive_heaters`
  - Action type: `split_item`, `process_requirement_update`, `bom_or_recipe_update`
  - Action: Split induction bearing/shrink-fit heater from resistive hot plate/heating-plate equipment.
  - Queue task: Create or distinguish `induction_bearing_heater_v0` and `controlled_heating_plate_v0`; migrate bearing installation to induction/thermal-fit heater and extruder/reactor heating uses to heating plates or barrel/heating-jacket resources.

- [ ] Decision ID: `heating_plate_induction_heater.no_action`
  - Action type: `no_action`
  - Action: Leave `heating_plate_induction_heater` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `heating_plate_induction_heater.keep_distinct_from_heat_treatment_furnace`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Do not treat this as a general heat-treatment furnace.
  - Queue task: Add notes/process checks that this item is a small local heater for parts or surfaces, not a furnace for bulk heat-treatment cycles.

- [ ] Decision ID: `heating_plate_induction_heater.add_induction_requirements`
  - Action type: `bom_or_recipe_update`, `note_cleanup`
  - Action: If induction remains in scope, add coil/yoke geometry, high-current power electronics, cooling, shielding, grounding, and demagnetization assumptions.
  - Queue task: Update BOM/recipe notes for induction-specific hardware and bearing demagnetization where required.

- [ ] Decision ID: `heating_plate_induction_heater.audit_extruder_and_reactor_uses`
  - Action type: `process_requirement_update`, `reference_migration`
  - Action: Check whether plastic extruder and reactor heating/cooling BOM uses really need heating plates, barrel heaters, jackets, or another resource.
  - Queue task: Review `bom_plastic_extruder_v0` and `bom_reactor_heating_cooling_system_v0`; replace this item with specific barrel heaters, heating jackets, controlled plates, or thermal-control subsystems as appropriate.

- [ ] Decision ID: `heating_plate_induction_heater.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## heliostat_array_system_v0

Source review: `research/machines/heliostat_array_system_v0.md`

Current interpretation: Real modular heliostat field/array resource. It should be interpreted as a small coordinated mirror field, not a single monolithic machine and not a utility-scale solar power tower plant.

### Primary Path - Choose One

- [ ] Decision ID: `heliostat_array_system_v0.keep_small_modular_field`
  - Action type: `note_cleanup`
  - Action: Keep as a small modular heliostat field for redirecting or concentrating sunlight to a receiver/target.
  - Queue task: Update notes to define `heliostat_array_system_v0` as a small modular field composed of mirror panels, frames, two-axis actuators, controls, and mounts; scale larger applications by number of modules.

- [ ] Decision ID: `heliostat_array_system_v0.split_illumination_and_thermal_concentration`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Separate polar illumination support from solar thermal concentration if the use cases need different optical layouts and receivers.
  - Queue task: Review polar mining/water extraction and solar-thermal processes; create or route to distinct resources for polar light redirection, process heat concentration, and power-generation support where needed.

- [ ] Decision ID: `heliostat_array_system_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `heliostat_array_system_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `heliostat_array_system_v0.add_mirror_area_and_output`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Add mirror area and expected delivered heat/light/power-support assumptions for the 885 kg system.
  - Queue task: Estimate or document mirror area, tracking accuracy, optical losses, delivered flux/illumination, and whether the item supplies heat, light, electrical-power support, or only redirected sunlight.

- [ ] Decision ID: `heliostat_array_system_v0.add_calibration_and_metrology`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Model optical alignment, calibration, aiming logic, and maintenance where field accuracy matters.
  - Queue task: Add requirements or notes for optical metrology tools, field alignment, receiver aiming control, cleaning/maintenance, and safety interlocks.

- [ ] Decision ID: `heliostat_array_system_v0.keep_distinct_from_fresnel_or_dish`
  - Action type: `dedupe_or_consolidation`, `note_cleanup`
  - Action: Keep heliostats distinct from Fresnel/dish concentrators.
  - Queue task: Document that heliostats redirect sunlight to a remote receiver, while Fresnel lenses and dish concentrators focus locally; audit solar concentrator references for correct resource selection.

- [ ] Decision ID: `heliostat_array_system_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## high_temperature_power_supply_v0

Source review: `research/machines/high_temperature_power_supply_v0.md`

Current interpretation: Real high-current industrial process power supply, but the name is misleading because the supply powers high-temperature processes rather than operating at high temperature itself.

### Primary Path - Choose One

- [ ] Decision ID: `high_temperature_power_supply_v0.rename_high_current_process_supply`
  - Action type: `rename_or_alias`, `note_cleanup`
  - Action: Rename or annotate as `high_current_process_power_supply_v0`.
  - Queue task: Clarify that this item is an industrial high-current power conversion system for electrolysis, resistive/furnace heating, electrode processes, or refining; update name/aliases if selected.

- [ ] Decision ID: `high_temperature_power_supply_v0.split_by_power_application`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split supplies by voltage/current/waveform/regulation/duty-cycle needs where process requirements differ.
  - Queue task: Sort MRE, FFC, molten-salt electrolysis, steel refining, furnace heating, and getter/receiver fabrication uses into specific DC rectifier, controlled electrolysis supply, furnace transformer/AC controller, or other power-supply resources.

- [ ] Decision ID: `high_temperature_power_supply_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `high_temperature_power_supply_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `high_temperature_power_supply_v0.dedupe_related_power_supplies`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Compare and consolidate overlapping high-current supply items where requirements match.
  - Queue task: Review `high_temperature_power_supply_v0`, `high_temp_power_supply_unit`, `power_supply_dc_high_current`, `ffc_power_supply_controlled_v0`, and related items; consolidate, alias, or define scope boundaries by current, voltage, regulation, and duty cycle.

- [ ] Decision ID: `high_temperature_power_supply_v0.keep_bench_supplies_distinct`
  - Action type: `process_requirement_update`, `reference_migration`
  - Action: Do not use this item for ordinary lab electronics.
  - Queue task: Audit references and route low-power electronics/test uses to `power_supply_benchtop` or `power_supply_bench` rather than the industrial high-current supply.

- [ ] Decision ID: `high_temperature_power_supply_v0.add_converter_bom_scope`
  - Action type: `bom_or_recipe_update`, `note_cleanup`
  - Action: Clarify whether the 320 kg mass includes transformers, rectifiers/SCRs, busbars, cooling, insulation, controls, safety interlocks, and enclosure.
  - Queue task: Update BOM/notes to specify converter topology and included subsystems, including power semiconductors/import constraints if relevant.

- [ ] Decision ID: `high_temperature_power_supply_v0.audit_ac_vs_dc_processes`
  - Action type: `process_requirement_update`
  - Action: Distinguish furnace AC/transformer control from electrolysis DC rectification.
  - Queue task: Review each process using this supply and document whether it requires DC electrolysis current, AC furnace power, controlled waveform, low-voltage high-current output, or other specialized electrical behavior.

- [ ] Decision ID: `high_temperature_power_supply_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## hot_press_v0

Source review: `research/machines/hot_press_v0.md`

Current interpretation: Real specialized hot press combining controlled heat and uniaxial pressure for powder, ceramic, magnet, electrode, or diffusion-bonded part consolidation.

### Primary Path - Choose One

- [ ] Decision ID: `hot_press_v0.keep_specialized_hot_press`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep distinct from `hydraulic_press` and `sintering_furnace_v0` where simultaneous heat and pressure are required.
  - Queue task: Clarify `hot_press_v0` as a pilot-scale heated platen/vacuum hot press for powder and ceramic consolidation; preserve it for processes that require pressure during heating.

- [ ] Decision ID: `hot_press_v0.downgrade_to_heated_hydraulic_press`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Use a simpler heated hydraulic press if only low-temperature polymer/composite pressing is needed.
  - Queue task: Review current uses; migrate low-temperature polymer/composite pressing to `hydraulic_press` plus heated platens or a simpler heated press resource if high-temperature hot pressing is unnecessary.

- [ ] Decision ID: `hot_press_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `hot_press_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `hot_press_v0.add_force_temp_size_limits`
  - Action type: `note_cleanup`
  - Action: Add maximum force, temperature, and platen/die size assumptions.
  - Queue task: Document force rating, temperature range, working envelope, and whether the 950 kg item represents a lab or pilot-scale machine.

- [ ] Decision ID: `hot_press_v0.add_high_temp_tooling_and_sensors`
  - Action type: `bom_or_recipe_update`
  - Action: Add explicit dies/tooling, load measurement, displacement measurement, and safety shielding.
  - Queue task: Update BOM/recipe notes for die sets, graphite/high-temperature tooling, load cells, displacement sensors, guarding, and hydraulic/thermal safety interlocks.

- [ ] Decision ID: `hot_press_v0.add_vacuum_or_inert_requirements`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Add vacuum/inert/reducing atmosphere hardware for oxidation-sensitive ceramics, magnets, metals, graphite, tungsten, or refractory materials.
  - Queue task: Audit `ndfeb_magnet_sintering_v0`, ceramics, electrodes, and other hot-press processes; require vacuum or inert atmosphere resources where needed.

- [ ] Decision ID: `hot_press_v0.separate_sps_or_hip`
  - Action type: `split_item`, `deferred_schema_or_modeling_decision`
  - Action: Keep spark plasma sintering and hot isostatic pressing as separate future machine concepts if needed.
  - Queue task: Do not fold SPS or HIP assumptions into `hot_press_v0`; create separate items only when process recommendations require pulsed-current sintering or isostatic gas-pressure consolidation.

- [ ] Decision ID: `hot_press_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## hydraulic_power_unit_basic

Source review: `research/machines/hydraulic_power_unit_basic.md`

Current interpretation: Real hydraulic power-pack subsystem that converts motor power into pressurized fluid for presses, cylinders, clamps, drilling equipment, and related hydraulic actuators.

### Primary Path - Choose One

- [ ] Decision ID: `hydraulic_power_unit_basic.keep_reusable_subsystem`
  - Action type: `note_cleanup`, `infrastructure_or_subsystem_modeling`
  - Action: Keep separate from `hydraulic_press` and other hydraulic machines as a reusable hydraulic power subsystem.
  - Queue task: Clarify `hydraulic_power_unit_basic` as a hydraulic power pack/subassembly with pump, reservoir, motor, valve manifold, relief valve, filtration, and controls; preserve its role in multiple machine BOMs.

- [ ] Decision ID: `hydraulic_power_unit_basic.embed_in_each_machine`
  - Action type: `dedupe_or_consolidation`, `bom_or_recipe_update`
  - Action: Stop modeling a standalone HPU if all hydraulic machines embed their own hydraulic power packs.
  - Queue task: Review hydraulic machine BOMs and decide whether HPUs are shared modular subsystems or embedded per machine; migrate BOMs accordingly.

- [ ] Decision ID: `hydraulic_power_unit_basic.no_action`
  - Action type: `no_action`
  - Action: Leave `hydraulic_power_unit_basic` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `hydraulic_power_unit_basic.add_pressure_flow_rating`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Add pressure and flow rating assumptions.
  - Queue task: Document required pressure, flow, reservoir volume, duty cycle, and whether the 150 kg unit can serve current presses/drilling equipment within Conservative Mode size-equivalence limits.

- [ ] Decision ID: `hydraulic_power_unit_basic.model_fluid_seals_filters_hoses`
  - Action type: `bom_or_recipe_update`, `consumable_or_tooling_modeling`
  - Action: Add hydraulic fluid, seals, hoses/fittings, gauges, return filters, breathers, and cooling if reliability matters.
  - Queue task: Update BOM/recipe notes or consumable modeling for hydraulic fluid, contamination control, filtration, hoses, seals, fittings, relief protection, gauges, and cooling.

- [ ] Decision ID: `hydraulic_power_unit_basic.decide_shared_vs_embedded_use`
  - Action type: `infrastructure_or_subsystem_modeling`
  - Action: Decide whether one HPU can serve multiple machines through quick-connect plumbing or whether each machine has a dedicated unit.
  - Queue task: Add notes to machine BOMs/processes indicating shared modular HPU use versus embedded machine-specific HPU use.

- [ ] Decision ID: `hydraulic_power_unit_basic.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## hydraulic_press

Source review: `research/machines/hydraulic_press.md`

Current interpretation: Real canonical general-purpose hydraulic press for low-to-medium throughput pressing, compaction, bearing installation, straightening, and shop operations.

### Primary Path - Choose One

- [ ] Decision ID: `hydraulic_press.keep_canonical_general_press`
  - Action type: `note_cleanup`, `dedupe_or_consolidation`
  - Action: Preserve `hydraulic_press` as the canonical general-purpose press and keep smaller generic press aliases consolidated into it.
  - Queue task: Confirm and document existing dedupe decision for `hydraulic_press`; preserve it as the default controlled high-force linear press for general shop pressing, compaction, bearing installation, and straightening.

- [ ] Decision ID: `hydraulic_press.split_by_press_function`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split only where mechanics, throughput, tooling, or tolerances differ materially.
  - Queue task: Audit processes using `hydraulic_press`; route sheet bending to `press_brake`, repetitive forming to `stamping_press_basic`, hot forging to forging equipment, and controlled powder/ceramic compaction to a dedicated compaction press only where needed.

- [ ] Decision ID: `hydraulic_press.no_action`
  - Action type: `no_action`
  - Action: Leave `hydraulic_press` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `hydraulic_press.add_capacity_tonnage`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Document approximate tonnage, daylight, stroke, and working envelope.
  - Queue task: Estimate or record capacity assumptions for the 600 kg press so process uses do not imply a benchtop jack press or massive production press.

- [ ] Decision ID: `hydraulic_press.keep_tooling_separate`
  - Action type: `consumable_or_tooling_modeling`, `bom_or_recipe_update`
  - Action: Keep molds, platens, dies, and fixture sets separate from the press frame/hydraulics.
  - Queue task: Review pressing processes and ensure required tooling/mold/platen sets are modeled separately where shape, pressure distribution, or part geometry matters.

- [ ] Decision ID: `hydraulic_press.add_hydraulic_safety_details`
  - Action type: `bom_or_recipe_update`, `note_cleanup`
  - Action: Ensure hydraulic fluid, seals, hoses, gauges, guarding, overload protection, and relief safety are represented adequately.
  - Queue task: Update notes/BOM or link to `hydraulic_power_unit_basic` details for hydraulic reliability and safety.

- [ ] Decision ID: `hydraulic_press.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## induction_forge_v0

Source review: `research/machines/induction_forge_v0.md`

Current interpretation: Real induction billet/bar heating resource for forging and heat-treatment workflows, but current BOM/recipe underrepresent the induction power electronics, coil, capacitor, cooling, and controls that make it work.

### Primary Path - Choose One

- [ ] Decision ID: `induction_forge_v0.scope_as_industrial_billet_heater`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Keep 1800 kg scale as an industrial induction billet/bar heating station.
  - Queue task: Update notes and BOM to define `induction_forge_v0` as an industrial induction billet/bar heater with high-power supply, capacitor bank, copper coils, cooling/chiller, temperature sensing, controls, shielding, and handling hardware.

- [ ] Decision ID: `induction_forge_v0.rescope_as_small_forge_shop_unit`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: If intended as a small forge-shop induction heater, reduce scale/mass and simplify accordingly.
  - Queue task: Decide whether this is a blacksmith/forge-shop unit; if so, revise mass, power, cooling, and BOM assumptions away from the current 1800 kg industrial scale.

- [ ] Decision ID: `induction_forge_v0.consolidate_to_generic_furnace`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Merge into generic furnace heating only if induction-specific fast/localized heating is not needed.
  - Queue task: Audit forging and heating processes; migrate to `furnace_basic` or `heating_furnace` only where induction-specific heating, coil geometry, clean operation, or rapid localized control is not required.

- [ ] Decision ID: `induction_forge_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `induction_forge_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `induction_forge_v0.repair_core_bom`
  - Action type: `bom_or_recipe_update`
  - Action: Replace motor/shaft/bearing-centered BOM emphasis with actual induction heating subsystems.
  - Queue task: Update canonical BOM/recipe so induction coil(s), high-power inverter or medium-frequency supply, resonant capacitor bank, cooling loop, temperature measurement, controls, shielding, grounding, and safety interlocks are explicit.

- [ ] Decision ID: `induction_forge_v0.model_replaceable_coils`
  - Action type: `consumable_or_tooling_modeling`, `bom_or_recipe_update`
  - Action: Model coils as replaceable tooling matched to stock geometry if needed.
  - Queue task: Add replaceable induction coil tooling or notes for stock diameter/geometry, duty cycle, cooling, wear, and maintenance.

- [ ] Decision ID: `induction_forge_v0.keep_bearing_heater_distinct`
  - Action type: `process_requirement_update`, `dedupe_or_consolidation`
  - Action: Use a smaller induction bearing/thermal-fit heater for bearing installation rather than the forge-scale unit.
  - Queue task: Audit bearing thermal-fitting processes and route them to `heating_plate_induction_heater` or a renamed induction bearing heater, not the industrial billet forge unless explicitly intended.

- [ ] Decision ID: `induction_forge_v0.add_power_frequency_stock_assumptions`
  - Action type: `note_cleanup`
  - Action: Add power level, frequency range, stock diameter, and duty-cycle assumptions.
  - Queue task: Document the assumed electrical power, frequency, stock size range, heating rate, duty cycle, and cooling capacity.

- [ ] Decision ID: `induction_forge_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## inspection_tools_basic

Source review: `research/machines/inspection_tools_basic.md`

Current interpretation: Real manual inspection/metrology tool kit. It should be treated as reusable tooling or metrology inventory, with clear separation between simple inspection aids and calibrated reference standards.

### Primary Path - Choose One

- [ ] Decision ID: `inspection_tools_basic.scope_as_basic_inspection_aids`
  - Action type: `note_cleanup`, `dedupe_or_consolidation`
  - Action: Use `inspection_tools_basic` for low-end manual inspection and sorting only.
  - Queue task: Clarify that `inspection_tools_basic` covers magnifiers, straightedges, rulers, simple gauges, calipers, and visual aids; move micrometers, gauge blocks, dial indicators, and electrical instruments to broader metrology items where appropriate.

- [ ] Decision ID: `inspection_tools_basic.keep_as_compact_calibrated_kit`
  - Action type: `note_cleanup`, `deferred_schema_or_modeling_decision`
  - Action: Keep as a compact calibrated inspection kit including micrometers and gauge blocks.
  - Queue task: Document calibration-chain assumptions, storage/protection, operator training, and which reference standards are included in the 8 kg kit.

- [ ] Decision ID: `inspection_tools_basic.consolidate_with_measurement_equipment`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Merge into `measurement_equipment` if both are serving the same calibrated metrology role.
  - Queue task: Compare `inspection_tools_basic` and `measurement_equipment`; consolidate or define clear scope boundaries between manual inspection aids and broader calibrated metrology/electrical measurement kits.

- [ ] Decision ID: `inspection_tools_basic.no_action`
  - Action type: `no_action`
  - Action: Leave `inspection_tools_basic` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `inspection_tools_basic.reclassify_as_tooling`
  - Action type: `consumable_or_tooling_modeling`
  - Action: Reclassify as reusable inspection tooling/metrology kit if the schema supports it.
  - Queue task: Move or document `inspection_tools_basic` as a tool kit rather than powered process equipment while preserving process-resource semantics.

- [ ] Decision ID: `inspection_tools_basic.add_calibration_chain_notes`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Add calibration and traceability notes where precision work depends on it.
  - Queue task: Document which inspection tools require calibration, what reference standards are needed, and whether gauge blocks remain early import seed items.

- [ ] Decision ID: `inspection_tools_basic.route_precision_measurement_elsewhere`
  - Action type: `process_requirement_update`, `reference_migration`
  - Action: Use specialized metrology resources for optical, CMM, microscope, comparator, or high-precision machine construction work.
  - Queue task: Audit precision grinding/scraping and precision machine processes; route specialized inspection to `optical_metrology_tools`, optical comparators, microscopes, CMMs, gauge blocks, or surface plates as needed.

- [ ] Decision ID: `inspection_tools_basic.require_labor_plus_kit`
  - Action type: `process_requirement_update`
  - Action: Ensure manual inspection uses labor plus the tool kit rather than treating the kit as autonomous inspection.
  - Queue task: Review manual inspection processes and require `labor_bot_general_v0` or equivalent operator labor alongside inspection tools where appropriate.

- [ ] Decision ID: `inspection_tools_basic.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## labor_bot_general_v0

Source review: `research/machines/labor_bot_general_v0.md`

Current interpretation: Real industrial/collaborative robot-arm class and deliberate SERES modeling primitive for reusable labor capacity. It should remain central, but not be treated as human-equivalent general autonomy or as a replacement for active process machines.

### Primary Path - Choose One

- [ ] Decision ID: `labor_bot_general_v0.keep_core_labor_resource`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Preserve `labor_bot_general_v0` as the core indoor/pressurized general labor resource.
  - Queue task: Clarify `labor_bot_general_v0` as a robot arm plus end effector, tooling, fixtures, work-cell safety, integration, and programming/calibration assumptions; preserve Conservative Mode guidance to use labor bot plus tools for low-throughput manipulation.

- [ ] Decision ID: `labor_bot_general_v0.split_collaborative_and_industrial_variants`
  - Action type: `split_item`, `deferred_schema_or_modeling_decision`
  - Action: Split into lighter collaborative and heavier guarded industrial arm variants if payload/reach/safety assumptions need more fidelity.
  - Queue task: Decide whether to add separate robot variants for collaborative low-payload work and heavier industrial machine-tending/handling; migrate process requirements by payload, reach, speed, guarding, and integration needs.

- [ ] Decision ID: `labor_bot_general_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `labor_bot_general_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `labor_bot_general_v0.add_environment_limits`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep indoor/pressurized-habitat assumptions explicit.
  - Queue task: Add notes that `labor_bot_general_v0` is not an EVA, vacuum, abrasive-regolith fieldwork, high-temperature-proximity, or dusty excavation robot without specialized protection or a different robot.

- [ ] Decision ID: `labor_bot_general_v0.add_payload_precision_limits`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep payload, reach, repeatability, and end-effector limits visible.
  - Queue task: Document whether 20 kg payload is Earth-equivalent, lunar-effective, or flange payload including end effector; preserve +/-0.5 mm repeatability and use lifting equipment or precision machines/metrology for heavier/tighter tasks.

- [ ] Decision ID: `labor_bot_general_v0.review_mass_realism`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Consider increasing mass or clarifying assumptions for a 20 kg payload at roughly 2 m reach.
  - Queue task: Compare 120 kg mass to commercial 20-25 kg payload, 1.8-2.0 m reach robot arms; update mass or add rationale if current value is lunar/optimized/partial-system mass.

- [ ] Decision ID: `labor_bot_general_v0.preserve_imported_critical_subcomponents`
  - Action type: `bom_or_recipe_update`, `reference_migration`
  - Action: Preserve imported or hard-to-localize status for compute, sensing, servo electronics, encoders, harmonic drives, force/torque sensors, cameras, and rare-earth magnets unless production chains exist.
  - Queue task: Audit BOM/recipe and import assumptions for precision robot components; do not imply local fabrication of advanced motion-control parts without explicit KB chains.

- [ ] Decision ID: `labor_bot_general_v0.model_setup_programming_calibration`
  - Action type: `process_requirement_update`, `deferred_schema_or_modeling_decision`
  - Action: Decide whether setup time, tool changing, fixture setup, programming, and calibration should be modeled separately from productive labor hours.
  - Queue task: Add notes or future modeling tasks for work-cell setup, tool changes, fixtures, programming, and calibration if simulator currently counts only productive labor-bot hours.

- [ ] Decision ID: `labor_bot_general_v0.keep_active_machines_distinct`
  - Action type: `process_requirement_update`
  - Action: Do not use labor bot plus tools to replace active process machines where machinery supplies the core physics.
  - Queue task: Audit any processes where labor bot may be substituting for mills, grinders, furnaces, pumps, presses, power converters, or continuous feedback systems; require the active process machine where needed.

- [ ] Decision ID: `labor_bot_general_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## lifting_equipment

Source review: `research/machines/lifting_equipment.md`

Current interpretation: Real small rated workshop lifting system, such as a gantry crane or overhead hoist/trolley, for components too heavy or awkward for the labor bot alone.

### Primary Path - Choose One

- [ ] Decision ID: `lifting_equipment.keep_small_rated_gantry_hoist`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep as a generic 500 kg workshop gantry/hoist/trolley system.
  - Queue task: Clarify `lifting_equipment` as a small rated gantry crane or overhead hoist/trolley system for 500 kg component handling during assembly; keep it distinct from large cranes, forklifts, and mining material-handling systems.

- [ ] Decision ID: `lifting_equipment.split_by_lifting_method`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split manual chain hoist, electric hoist, gantry crane, jib crane, and hydraulic shop crane only where capacity/workflow differs.
  - Queue task: Audit heavy-assembly and material-handling processes and introduce separate lifting resources only where span, lift height, mobility, power, or load capacity differs materially.

- [ ] Decision ID: `lifting_equipment.no_action`
  - Action type: `no_action`
  - Action: Leave `lifting_equipment` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `lifting_equipment.add_capacity_and_safety_factor`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: State rated load, safety factor, span, lift height, and inspection/test assumptions.
  - Queue task: Document the 500 kg capacity, 3-4 m lift height, structural safety factor, rated fasteners, and load-test/inspection requirements.

- [ ] Decision ID: `lifting_equipment.add_rigging_components`
  - Action type: `bom_or_recipe_update`, `consumable_or_tooling_modeling`
  - Action: Add slings, shackles, hooks, trolleys, beam clamps, chains, and rated fasteners if not bundled.
  - Queue task: Update BOM/notes to include rigging and hoist accessories needed for safe component handling.

- [ ] Decision ID: `lifting_equipment.audit_heavy_processes`
  - Action type: `process_requirement_update`
  - Action: Require lifting equipment for components near or above labor-bot payload limits.
  - Queue task: Audit machine assembly, motor assembly, material handling, and maintenance processes; add `lifting_equipment` where loads exceed labor-bot payload or awkward handling limits.

- [ ] Decision ID: `lifting_equipment.review_capacity_for_self_reproducing_set`
  - Action type: `research_or_design_followup`, `process_requirement_update`
  - Action: Check whether 500 kg capacity is enough for the heaviest self-reproducing machine assemblies.
  - Queue task: Identify heaviest assemblies and decide whether a higher-capacity hoist/crane variant is required.

- [ ] Decision ID: `lifting_equipment.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## measurement_equipment

Source review: `research/machines/measurement_equipment.md`

Current interpretation: Real calibrated metrology/equipment set, not a powered production machine. It should cover broader calibrated measurement than `inspection_tools_basic`, while full CMMs and advanced optical metrology remain separate.

### Primary Path - Choose One

- [ ] Decision ID: `measurement_equipment.keep_calibrated_metrology_set`
  - Action type: `note_cleanup`, `dedupe_or_consolidation`
  - Action: Define as a calibrated measurement and metrology equipment set.
  - Queue task: Update notes so `measurement_equipment` includes calibrated calipers, micrometers, dial indicators, gauge blocks/reference standards, multimeter if selected, cases/holders, and calibration support; keep distinct from low-end `inspection_tools_basic`.

- [ ] Decision ID: `measurement_equipment.split_dimensional_and_electrical_kits`
  - Action type: `split_item`, `reference_migration`
  - Action: Split dimensional metrology from electrical measurement if the mixed kit causes ambiguity.
  - Queue task: Decide whether multimeters belong in `measurement_equipment` or only in `test_equipment_electronics`/`multimeter_set`; migrate references accordingly.

- [ ] Decision ID: `measurement_equipment.no_action`
  - Action type: `no_action`
  - Action: Leave `measurement_equipment` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `measurement_equipment.reclassify_as_tooling_or_equipment_set`
  - Action type: `consumable_or_tooling_modeling`
  - Action: Reclassify as reusable metrology tooling/equipment if schema supports it.
  - Queue task: Move or document `measurement_equipment` as a calibrated tool/equipment set rather than a powered process machine while preserving process-resource semantics.

- [ ] Decision ID: `measurement_equipment.remove_or_clarify_cmm_language`
  - Action type: `note_cleanup`, `reference_migration`
  - Action: Remove or clarify "coordinate measuring equipment" unless it means a small portable arm; keep full CMMs separate.
  - Queue task: Update notes and references so full coordinate measuring machines remain separate items such as `coordinate_measuring_machine_v0`, not hidden inside the 30 kg metrology kit.

- [ ] Decision ID: `measurement_equipment.add_surface_plate_height_gauge`
  - Action type: `bom_or_recipe_update`, `deferred_schema_or_modeling_decision`
  - Action: Decide whether the kit should include a surface plate and height gauge.
  - Queue task: Review metrology requirements for alignment/calibration; add surface plate, height gauge, squares, pins, and blocks if needed, or keep them separate.

- [ ] Decision ID: `measurement_equipment.add_traceability_assumptions`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Document calibration traceability level and early import assumptions.
  - Queue task: Add notes for gauge-block calibration, traceable standards, calibration intervals, and which precision artifacts remain early import seed items.

- [ ] Decision ID: `measurement_equipment.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## metal_forming_basic_v0

Source review: `research/machines/metal_forming_basic_v0.md`

Current interpretation: Real low-volume shop forming capability bundle, not one standard purchasable machine. It combines pressing, bending, rolling, fixture-supported forming, and anvil work, and it shares an ID with a process.

### Primary Path - Choose One

- [ ] Decision ID: `metal_forming_basic_v0.keep_as_generic_forming_cell`
  - Action type: `note_cleanup`, `deferred_schema_or_modeling_decision`
  - Action: Keep as a conservative catch-all forming equipment set for miscellaneous low-volume forming.
  - Queue task: Add a display name such as "Basic metal forming equipment set" and document that this is a shop forming cell/equipment bundle, not a single standard machine or high-throughput production line.

- [ ] Decision ID: `metal_forming_basic_v0.replace_with_specific_machines`
  - Action type: `dedupe_or_consolidation`, `reference_migration`, `process_requirement_update`
  - Action: Replace process references with specific forming machines where the operation is known.
  - Queue task: Audit all `metal_forming_basic_v0` machine-resource references; use `hydraulic_press` for pressing/compaction/straightening, `press_brake` for straight-line sheet bending, `plate_rolling_mill` or a plate roll for rolling, and `power_hammer_or_press` for hot forging.

- [ ] Decision ID: `metal_forming_basic_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `metal_forming_basic_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `metal_forming_basic_v0.resolve_machine_process_id_collision`
  - Action type: `rename_or_alias`, `reference_migration`
  - Action: Review and resolve ambiguity from `metal_forming_basic_v0` existing as both a machine item and process ID.
  - Queue task: Inspect machine and process references for `metal_forming_basic_v0`; rename/rescope the machine or add explicit notes/aliases if same-ID machine/process usage is intentional.

- [ ] Decision ID: `metal_forming_basic_v0.add_capability_limits`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Add tonnage, roll width/diameter, frame stiffness, material thickness, tooling, and throughput assumptions.
  - Queue task: Document forming capacity limits so the 1102 kg forming set is not treated as unlimited production equipment.

- [ ] Decision ID: `metal_forming_basic_v0.model_tooling_and_fixtures`
  - Action type: `bom_or_recipe_update`, `consumable_or_tooling_modeling`
  - Action: Add hardened dies, rollers, bearings, fixture plates, guards, and interchangeable tooling assumptions.
  - Queue task: Update BOM/notes to represent the tooling and fixture requirements needed for realistic pressing, rolling, and bending.

- [ ] Decision ID: `metal_forming_basic_v0.keep_labor_bot_for_setup_not_force`
  - Action type: `process_requirement_update`
  - Action: Use labor bots for setup and handling, but not as substitutes for high-force forming equipment.
  - Queue task: Audit forming processes and ensure high-force pressing/rolling/bending uses actual machinery while labor bot plus fixtures handles setup, positioning, and low-force miscellaneous tasks.

- [ ] Decision ID: `metal_forming_basic_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## metal_shear_or_saw

Source review: `research/machines/metal_shear_or_saw.md`

Current interpretation: Real shop metal stock-prep capability, but the combined item conflates sheet/plate shearing with bandsaw/cold-saw cutting of bar, tube, billet, and structural sections.

### Primary Path - Choose One

- [ ] Decision ID: `metal_shear_or_saw.keep_generic_stock_prep_station`
  - Action type: `note_cleanup`, `deferred_schema_or_modeling_decision`
  - Action: Keep as the broad canonical metal stock-prep cutting machine for low-detail fabrication recipes.
  - Queue task: Add notes that `metal_shear_or_saw` represents a small shop cutting station/capability, not one precise machine and not a full industrial plate shear.

- [ ] Decision ID: `metal_shear_or_saw.split_bandsaw_and_sheet_shear`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split into `metal_cutting_bandsaw` and `sheet_metal_shear` when process geometry matters.
  - Queue task: Audit cutting, tube, sheet, plate, bar, and fabrication processes; route bar/tube/sections/billet to a bandsaw or cold saw and straight sheet/plate cuts to a shear.

- [ ] Decision ID: `metal_shear_or_saw.no_action`
  - Action type: `no_action`
  - Action: Leave `metal_shear_or_saw` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `metal_shear_or_saw.keep_small_cutting_tools_distinct`
  - Action type: `dedupe_or_consolidation`, `process_requirement_update`
  - Action: Keep `saw_or_cutting_tool` for small hand/power cutting, gasket cutting, and core cutting.
  - Queue task: Audit cutting processes and preserve the distinction between shop stock-prep machinery and smaller manual/powered cutting tools.

- [ ] Decision ID: `metal_shear_or_saw.reconcile_mass`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Revisit 78 kg mass if current processes imply industrial plate shearing.
  - Queue task: Compare current mass to dedupe notes and process requirements; keep 78 kg for a light bandsaw/cutting station or update mass/variant if hydraulic plate shearing is intended.

- [ ] Decision ID: `metal_shear_or_saw.model_blade_wear`
  - Action type: `consumable_or_tooling_modeling`
  - Action: Model bandsaw blades, saw blades, or shear blades as consumable/wear tooling if needed.
  - Queue task: Add consumable blade/band/knife wear and replacement assumptions for metal cutting processes.

- [ ] Decision ID: `metal_shear_or_saw.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## milling_machine_general_v0

Source review: `research/machines/milling_machine_general_v0.md`

Current interpretation: Real manual/general milling machine concept, but KB state is inconsistent: the item is marked deprecated/consolidated into `cnc_mill` while many active processes still require it.

### Primary Path - Choose One

- [ ] Decision ID: `milling_machine_general_v0.finish_consolidation_to_cnc_mill`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Finish consolidation into `cnc_mill` if the self-reproducing set wants one canonical milling machine.
  - Queue task: Migrate remaining process references from `milling_machine_general_v0` to `cnc_mill`; preserve or update deprecation notes so the deprecated item is no longer operationally required.

- [ ] Decision ID: `milling_machine_general_v0.keep_as_manual_mill`
  - Action type: `rename_or_alias`, `note_cleanup`, `bom_or_recipe_update`
  - Action: Keep as a lower-complexity manual mill distinct from CNC.
  - Queue task: Rename/rescope to `manual_milling_machine_v0` or `vertical_knee_mill_v0`, remove deprecated note, clarify lower automation/precision than `cnc_mill`, and update mass/BOM for a realistic manual mill frame and spindle system.

- [ ] Decision ID: `milling_machine_general_v0.no_action`
  - Action type: `no_action`
  - Action: Leave the deprecated-but-used state unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `milling_machine_general_v0.review_mass_and_stiffness`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Decide whether 370 kg represents a benchtop/light mill or should be increased toward a knee-mill class.
  - Queue task: Compare intended processes to machine mass/stiffness; update notes/BOM if serious steel gear cutting and machine-tool fabrication require a heavier frame than 370 kg.

- [ ] Decision ID: `milling_machine_general_v0.remove_compute_if_manual`
  - Action type: `bom_or_recipe_update`
  - Action: Remove imported control compute module if this remains a manual mill.
  - Queue task: If keeping a manual mill, update BOM to remove unnecessary CNC/control-compute components and instead include handwheels, leadscrews, feeds/DRO if desired, vises, clamps, and manual controls.

- [ ] Decision ID: `milling_machine_general_v0.add_gear_cutting_tooling`
  - Action type: `consumable_or_tooling_modeling`, `process_requirement_update`
  - Action: Add indexing/dividing-head tooling for gear-cutting processes if this machine is used for gears.
  - Queue task: Audit gear-cutting processes using `milling_machine_general_v0`; require dividing head/indexer, gear cutters, arbors, fixtures, or route to more specific gear-cutting machinery.

- [ ] Decision ID: `milling_machine_general_v0.document_build_requirements`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Document machine-tool build requirements such as ways, spindle bearings, scraping/grinding, calibration, and metrology.
  - Queue task: Update notes/BOM to include rigid base/column, precision ways/table, spindle head, leadscrews/ballscrews, bearings, drives, workholding, cutting tools, and alignment/calibration needs.

- [ ] Decision ID: `milling_machine_general_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## mixer_or_blender

Source review: `research/machines/mixer_or_blender.md`

Current interpretation: Real generic lab/pilot mixer or blender category. It is appropriate for low-detail mixing, but material behavior may require specific mixer types.

### Primary Path - Choose One

- [ ] Decision ID: `mixer_or_blender.keep_generic_lab_pilot_default`
  - Action type: `note_cleanup`, `deferred_schema_or_modeling_decision`
  - Action: Keep as a generic 80 kg low-detail mixing/blending default.
  - Queue task: Add notes that `mixer_or_blender` covers low-detail small-batch mixing where material behavior is not central, and that it is not equally valid for every liquid, slurry, powder, high-viscosity paste, abrasive castable, hot, or reactive material.

- [ ] Decision ID: `mixer_or_blender.split_by_material_behavior`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split or route processes by dry powder, paste/kneader, planetary, liquid tank, and refractory/cement mixer requirements.
  - Queue task: Audit all `mixer_or_blender` uses and assign specific mixer resources where high shear, low shear, dry blending, wet slurry, vacuum, heating, abrasive aggregate, viscosity, or dust containment matters.

- [ ] Decision ID: `mixer_or_blender.no_action`
  - Action type: `no_action`
  - Action: Leave `mixer_or_blender` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `mixer_or_blender.dedupe_or_scope_powder_mixer`
  - Action type: `dedupe_or_consolidation`
  - Action: Decide whether `powder_mixer` is a distinct dry-powder uniformity/dust-containment resource or a variant of `mixer_or_blender`.
  - Queue task: Compare `powder_mixer` and `mixer_or_blender`; consolidate or define a dry-powder-specific boundary.

- [ ] Decision ID: `mixer_or_blender.route_refractory_castables`
  - Action type: `process_requirement_update`, `reference_migration`
  - Action: Use a cement/refractory mixer for abrasive castables if aggregate handling matters.
  - Queue task: Review `refractory_castable_mixing_v0`; route to `cement_mixer_small` or a refractory/castable mixer if aggregate abrasion and paste consistency exceed the generic mixer scope.

- [ ] Decision ID: `mixer_or_blender.scope_mixing_station`
  - Action type: `dedupe_or_consolidation`, `process_requirement_update`
  - Action: Use `mixing_station` for formulation/potting workflows if dispensing, containers, ventilation, cleanup, and workflow support are included.
  - Queue task: Compare `mixing_station` and `mixer_or_blender`; assign formulation/potting workflows to a station only where extra workflow infrastructure is required beyond the mixer itself.

- [ ] Decision ID: `mixer_or_blender.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## molding_press

Source review: `research/machines/molding_press.md`

Current interpretation: Real molding/powder compaction press category, but likely duplicates `molding_press_basic` unless graphite molding needs distinct equipment.

### Primary Path - Choose One

- [ ] Decision ID: `molding_press.consolidate_to_molding_press_basic`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Use `molding_press_basic` as the canonical basic compression/cold-warm molding press.
  - Queue task: Migrate ordinary `molding_press` references, including `graphite_molding_v0` if appropriate, to `molding_press_basic`; deprecate or alias unversioned `molding_press` if no distinct service class remains.

- [ ] Decision ID: `molding_press.keep_as_graphite_powder_press`
  - Action type: `rename_or_alias`, `note_cleanup`, `process_requirement_update`
  - Action: Keep only if redefined as a graphite-specific or powder-compaction press.
  - Queue task: Rename/rescope `molding_press` as a graphite/powder compaction press and document differences from `molding_press_basic`, including force rating, mold/die requirements, platen alignment, ejectors, and process-specific assumptions.

- [ ] Decision ID: `molding_press.route_graphite_to_hot_press`
  - Action type: `reference_migration`, `process_requirement_update`
  - Action: Use `hot_press_v0` if graphite molding requires simultaneous high temperature and pressure.
  - Queue task: Review `graphite_molding_v0`; migrate to `hot_press_v0` if process physics require hot pressing rather than cold/warm compression molding.

- [ ] Decision ID: `molding_press.no_action`
  - Action type: `no_action`
  - Action: Leave `molding_press` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `molding_press.keep_mold_tooling_separate`
  - Action type: `consumable_or_tooling_modeling`, `bom_or_recipe_update`
  - Action: Keep `pressing_mold_set` separate from the press machine.
  - Queue task: Ensure graphite and molding processes require mold/die tooling separately where part geometry matters.

- [ ] Decision ID: `molding_press.add_press_specs_if_retained`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Document heated platens, force rating, daylight, stroke, platen parallelism, pressure measurement, and ejector capability if retained.
  - Queue task: Update notes/BOM for `molding_press` if it remains a distinct item.

- [ ] Decision ID: `molding_press.consolidate_unversioned_variants`
  - Action type: `dedupe_or_consolidation`
  - Action: Review unversioned/versioned molding press variants for consolidation.
  - Queue task: Compare `molding_press`, `molding_press_v0`, and `molding_press_basic`; consolidate, alias, or define explicit variant boundaries.

- [ ] Decision ID: `molding_press.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## molding_press_basic

Source review: `research/machines/molding_press_basic.md`

Current interpretation: Real basic hydraulic compression/powder molding press. It can cover cold or modest-temperature compression and green pressing, but not injection molding or high-temperature hot pressing without added equipment.

### Primary Path - Choose One

- [ ] Decision ID: `molding_press_basic.keep_canonical_basic_molding_press`
  - Action type: `note_cleanup`, `dedupe_or_consolidation`
  - Action: Keep as the canonical basic compression/powder molding press.
  - Queue task: Update notes to define `molding_press_basic` as a basic hydraulic compression/powder molding press with force/platens/mold support; reconcile duplicate molding press items around this canonical role.

- [ ] Decision ID: `molding_press_basic.split_by_material_process`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split or route polymer compression, rubber/silicone heated molding, powder/ceramic compaction, and injection molding to different resources where needed.
  - Queue task: Audit current uses of `molding_press_basic`; assign compression molding, heated-platen rubber/silicone/thermoset work, powder compaction, and injection molding to distinct machine/tooling resources if process physics require it.

- [ ] Decision ID: `molding_press_basic.no_action`
  - Action type: `no_action`
  - Action: Leave `molding_press_basic` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `molding_press_basic.add_heated_platen_capability`
  - Action type: `bom_or_recipe_update`, `process_requirement_update`
  - Action: Add heated platen, temperature control, cure timing, and insulation if rubber, silicone, thermoset, or composite molding needs heat.
  - Queue task: Update BOM/notes and process requirements for heated compression molding where selected.

- [ ] Decision ID: `molding_press_basic.add_powder_compaction_tooling`
  - Action type: `consumable_or_tooling_modeling`, `bom_or_recipe_update`
  - Action: Add die/punch/ejector tooling, fill mass control, lubrication, and pressure capacity for powder/ceramic green pressing.
  - Queue task: Ensure powder metallurgy and ceramic pressing processes require appropriate die/punch/ejector tooling and realistic force/platen assumptions.

- [ ] Decision ID: `molding_press_basic.route_injection_molded_parts`
  - Action type: `process_requirement_update`, `reference_migration`
  - Action: Do not use this press for thermoplastic injection-molded housings unless process is intentionally compression molded.
  - Queue task: Review `plastic_housing_molding_v0` and other polymer housing processes; route true injection molding to an injection molding machine or revise process wording to compression molding.

- [ ] Decision ID: `molding_press_basic.add_force_platen_specs`
  - Action type: `note_cleanup`
  - Action: Add force/tonnage and platen size assumptions for the 300 kg press.
  - Queue task: Document tonnage, daylight, stroke, platen size, parallelism, and load measurement assumptions.

- [ ] Decision ID: `molding_press_basic.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## mre_reactor_v0

Source review: `research/machines/mre_reactor_v0.md`

Current interpretation: Real experimental/pilot molten regolith electrolysis reactor technology. It should remain distinct from ordinary electrolysis cells, furnaces, and generic reactors, with high technical uncertainty explicit.

### Primary Path - Choose One

- [ ] Decision ID: `mre_reactor_v0.keep_advanced_isru_reactor`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep as advanced experimental ISRU equipment for molten regolith electrolysis.
  - Queue task: Expand display name to "Molten regolith electrolysis reactor"; document that it is plausible but high-risk, not a mature commodity machine, and probably not first-generation local manufacturing.

- [ ] Decision ID: `mre_reactor_v0.decompose_into_subsystems`
  - Action type: `infrastructure_or_subsystem_modeling`, `bom_or_recipe_update`
  - Action: Make reactor subsystems explicit if the KB needs higher fidelity.
  - Queue task: Split or explicitly model refractory vessel, electrode set, high-current power supply/feedthroughs, high-temperature sensors, oxygen collection, thermal management, feed handling, product removal, and slag/residue handling.

- [ ] Decision ID: `mre_reactor_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `mre_reactor_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `mre_reactor_v0.keep_distinct_from_generic_electrolysis`
  - Action type: `process_requirement_update`, `dedupe_or_consolidation`
  - Action: Keep MRE separate from `electrolysis_cell_unit_v0` and generic chemical reactors.
  - Queue task: Audit molten-regolith oxygen and crude-metal processes; require `mre_reactor_v0` rather than generic electrolysis cells unless the process is explicitly an abstraction.

- [ ] Decision ID: `mre_reactor_v0.model_electrode_lifetime`
  - Action type: `consumable_or_tooling_modeling`, `process_requirement_update`
  - Action: Model electrode sets as consumable or maintenance-limited where lifetime is uncertain.
  - Queue task: Add electrode material/lifetime assumptions for MRE, including whether graphite, inert, or refractory-metal electrodes are used and how replacement is represented.

- [ ] Decision ID: `mre_reactor_v0.clarify_heating_architecture`
  - Action type: `note_cleanup`, `infrastructure_or_subsystem_modeling`
  - Action: Clarify whether the reactor uses cold-wall Joule heating, external furnace heating, or both.
  - Queue task: Document reactor heating architecture and update requirements for `furnace_high_temp`, thermal insulation, power supply, or cold-wall design as needed.

- [ ] Decision ID: `mre_reactor_v0.add_product_removal_assumptions`
  - Action type: `process_requirement_update`, `bom_or_recipe_update`
  - Action: Add assumptions for oxygen bubbles, molten metal products, slag/regolith residue, and product handling.
  - Queue task: Update process/BOM notes for oxygen collection, metal tapping/removal, slag/residue handling, and feedstock loading.

- [ ] Decision ID: `mre_reactor_v0.clarify_mass_scope`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Clarify whether 1254.5 kg includes power electronics, oxygen collection, feed handling, and thermal insulation.
  - Queue task: Document item mass boundaries and move separate subsystems out of the reactor mass if selected.

- [ ] Decision ID: `mre_reactor_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## multimeter_set

Source review: `research/machines/multimeter_set.md`

Current interpretation: Real reusable electrical diagnostic/test instrument bundle for voltage, current, resistance, continuity, and basic assembly troubleshooting.

### Primary Path - Choose One

- [ ] Decision ID: `multimeter_set.keep_reusable_dmm_bundle`
  - Action type: `note_cleanup`
  - Action: Keep as a reusable multimeter/test tool bundle for basic electrical testing.
  - Queue task: Clarify `multimeter_set` as handheld DMMs plus leads/probes/fuses/case/accessories for field and assembly testing, not a full electronics bench suite or calibration lab.

- [ ] Decision ID: `multimeter_set.merge_into_test_equipment_electronics`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Consolidate into broader electronics test equipment if separate DMM-only capacity is unnecessary.
  - Queue task: Compare `multimeter_set`, `test_equipment_basic`, `test_equipment_electronics`, and `measurement_equipment`; consolidate or preserve scope boundaries based on process needs.

- [ ] Decision ID: `multimeter_set.no_action`
  - Action type: `no_action`
  - Action: Leave `multimeter_set` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `multimeter_set.consolidate_multimeter_digital_refs`
  - Action type: `reference_migration`, `dedupe_or_consolidation`
  - Action: Consolidate lingering `multimeter_digital` import references into `multimeter_set` unless a single imported DMM is intentionally separate.
  - Queue task: Search recipes/BOMs for `multimeter_digital`; migrate to `multimeter_set` or document why a separate imported DMM remains.

- [ ] Decision ID: `multimeter_set.keep_calibration_standards_separate`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Model high-accuracy calibration standards separately from ordinary meters.
  - Queue task: Add or preserve separate voltage references, resistance standards, current sources, calibration sources, and traceability assumptions for processes requiring calibrated measurements.

- [ ] Decision ID: `multimeter_set.decide_import_vs_local_build`
  - Action type: `deferred_schema_or_modeling_decision`, `bom_or_recipe_update`
  - Action: Decide whether the self-reproducing set imports safety-rated DMMs indefinitely or models locally buildable basic/analog meters.
  - Queue task: Add notes or variant items for safety-rated imported digital multimeters versus lower-accuracy locally buildable multimeters if selected.

- [ ] Decision ID: `multimeter_set.reclassify_as_reusable_tool`
  - Action type: `consumable_or_tooling_modeling`
  - Action: Reclassify as reusable test equipment/tooling if schema supports it.
  - Queue task: Move or document `multimeter_set` as reusable test equipment rather than powered production machinery.

- [ ] Decision ID: `multimeter_set.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## oscilloscope_basic

Source review: `research/machines/oscilloscope_basic.md`

Current interpretation: Real imported electronics test instrument for voltage-waveform observation. It should remain available as either a distinct instrument or a component of a broader electronics test bench.

### Primary Path - Choose One

- [ ] Decision ID: `oscilloscope_basic.keep_standalone_imported_instrument`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep `oscilloscope_basic` as a distinct imported instrument where processes specifically require waveform observation.
  - Queue task: Clarify `oscilloscope_basic` as a 2-4 channel, 20-100 MHz class imported oscilloscope with probes/accessories for electronics debugging, commissioning, and calibration.

- [ ] Decision ID: `oscilloscope_basic.bundle_into_electronics_test_bench`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Treat oscilloscope as a component of `test_equipment_electronics` or `test_bench_electrical` for process-resource requirements.
  - Queue task: Decide whether processes should require `oscilloscope_basic` directly or require a bundled electronics test bench that includes it; migrate references accordingly without deleting the oscilloscope concept.

- [ ] Decision ID: `oscilloscope_basic.no_action`
  - Action type: `no_action`
  - Action: Leave `oscilloscope_basic` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `oscilloscope_basic.preserve_import_boundary`
  - Action type: `reference_migration`, `note_cleanup`
  - Action: Keep precision ADCs, analog front ends, timing references, probes, displays, shielding, firmware, and calibration as imported or advanced electronics assumptions unless closure work is explicit.
  - Queue task: Add notes that local oscilloscope manufacture is out of scope unless electronics closure becomes a priority.

- [ ] Decision ID: `oscilloscope_basic.resolve_analog_variant`
  - Action type: `dedupe_or_consolidation`, `deferred_schema_or_modeling_decision`
  - Action: Decide whether `oscilloscope_analog_v0` is a real alternative, deprecated experimental item, or lower-capability local-manufacturing placeholder.
  - Queue task: Compare `oscilloscope_basic` and `oscilloscope_analog_v0`; define relationship, capability limits, import/local status, and process routing.

- [ ] Decision ID: `oscilloscope_basic.add_calibration_standards`
  - Action type: `infrastructure_or_subsystem_modeling`, `process_requirement_update`
  - Action: Add calibration reference standards if electronics test equipment closure becomes important.
  - Queue task: Add or link voltage/timebase/reference standards and calibration procedures for oscilloscope/test-bench workflows where needed.

- [ ] Decision ID: `oscilloscope_basic.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## pcb_development_station

Source review: `research/machines/pcb_development_station.md`

Current interpretation: Real PCB photoresist development/wet-process station, but it is a submodule of PCB fabrication rather than an independent board factory.

### Primary Path - Choose One

- [ ] Decision ID: `pcb_development_station.keep_as_pcb_wet_process_submodule`
  - Action type: `note_cleanup`, `infrastructure_or_subsystem_modeling`
  - Action: Keep as a PCB photoresist develop/rinse station or wet-process submodule.
  - Queue task: Rename or annotate as "PCB photoresist development station" or "PCB develop/rinse station"; document that it handles exposed photoresist development and wet handling/rinsing, not etching/drilling/tinning/full board fabrication.

- [ ] Decision ID: `pcb_development_station.bundle_into_pcb_fab_equipment`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Treat as a component of `pcb_fab_equipment` unless separate capacity modeling is needed.
  - Queue task: Review process/resource references; use `pcb_fab_equipment` as the process resource where a full PCB fabrication capability is intended and keep `pcb_development_station` as an internal BOM component.

- [ ] Decision ID: `pcb_development_station.no_action`
  - Action type: `no_action`
  - Action: Leave `pcb_development_station` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `pcb_development_station.clarify_station_type_and_mass`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Clarify whether this is a tray station, spray system, or enclosed wet bench, and justify or reduce the 200 kg mass.
  - Queue task: Update notes/BOM to match the selected scale, from minimal manual trays to enclosed pumped wet bench.

- [ ] Decision ID: `pcb_development_station.model_chemicals_and_waste`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Ensure developer chemistry, rinse water, etchant/waste treatment, PPE, ventilation, and containment are modeled elsewhere.
  - Queue task: Audit PCB photolithography/wet-process recipes and add consumables/hazard-handling requirements for developer, rinse, waste, fumes, ventilation, and secondary containment.

- [ ] Decision ID: `pcb_development_station.keep_distinct_from_etching_and_drilling`
  - Action type: `process_requirement_update`, `dedupe_or_consolidation`
  - Action: Keep etching tanks, UV exposure, drilling, tinning/plating, and full fab equipment distinct where process details matter.
  - Queue task: Ensure PCB process steps require the appropriate UV exposure, developer, etch, drill/router, and finishing resources rather than using the development station as a catch-all.

- [ ] Decision ID: `pcb_development_station.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## pcb_fab_equipment

Source review: `research/machines/pcb_fab_equipment.md`

Current interpretation: Real aggregated small PCB prototyping/fabrication station for simple single- and double-sided boards, not an advanced multilayer industrial PCB factory or semiconductor manufacturing capability.

### Primary Path - Choose One

- [ ] Decision ID: `pcb_fab_equipment.keep_aggregate_simple_pcb_station`
  - Action type: `note_cleanup`, `deferred_schema_or_modeling_decision`
  - Action: Keep as an aggregated PCB lab/tool bundle for coarse KB modeling.
  - Queue task: Add notes defining `pcb_fab_equipment` as a small PCB prototyping/fabrication station with exposure, develop/etch, drilling, and surface finish equipment for simple single/double-sided boards with coarse traces.

- [ ] Decision ID: `pcb_fab_equipment.split_into_process_stations`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split into UV exposure, development, etching, drilling, tinning/plating, and inspection/test stations only if separate capacity/mass/consumables matter.
  - Queue task: Create or route process requirements to `uv_exposure_unit`, `pcb_development_station`, `pcb_etching_tank_set`, `pcb_drilling_station`, `pcb_tinning_plating_bath`, and `pcb_inspection_test_station` where selected.

- [ ] Decision ID: `pcb_fab_equipment.no_action`
  - Action type: `no_action`
  - Action: Leave `pcb_fab_equipment` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `pcb_fab_equipment.resolve_pcb_fab_station_duplicate`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Decide whether `pcb_fab_station` duplicates `pcb_fab_equipment` or represents a different abstraction.
  - Queue task: Compare `pcb_fab_equipment` and `pcb_fab_station`; consolidate, alias, or document complete-station versus component relationships.

- [ ] Decision ID: `pcb_fab_equipment.model_consumables_and_waste`
  - Action type: `consumable_or_tooling_modeling`, `process_requirement_update`
  - Action: Model etchants, developers, photoresist, copper-clad laminate, drill bits, rinse water, waste treatment, ventilation, and PPE where needed.
  - Queue task: Audit PCB fabrication processes and add consumable/hazard-handling requirements.

- [ ] Decision ID: `pcb_fab_equipment.clarify_board_capabilities`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Clarify whether plated through holes, soldermask, silkscreen, electrical test, and multilayer boards are supported.
  - Queue task: Document board capability limits and route unsupported features to advanced/industrial PCB fabrication resources or imports.

- [ ] Decision ID: `pcb_fab_equipment.review_solar_cell_photolithography_use`
  - Action type: `process_requirement_update`, `research_or_design_followup`
  - Action: Check whether solar-cell photolithography can share this station or needs a cleaner/specialized process station.
  - Queue task: Review `solar_cell_fabrication_v0` and related photolithography requirements; add separate clean process station if PCB lab equipment is insufficient.

- [ ] Decision ID: `pcb_fab_equipment.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## pellet_press

Source review: `research/machines/pellet_press.md`

Current interpretation: Real powder pellet/tablet press category, but current KB implementation is an incomplete 22 kg frame-only stub rather than a complete functional press.

### Primary Path - Choose One

- [ ] Decision ID: `pellet_press.complete_lab_pilot_powder_press`
  - Action type: `bom_or_recipe_update`, `note_cleanup`
  - Action: Keep as a laboratory/pilot powder pellet press and complete the BOM/scope.
  - Queue task: Update `pellet_press` as a laboratory/pilot powder pellet press with press frame, hydraulic/screw/pneumatic actuator, hardened die set(s), load or pressure measurement, ejector/demolding tools, optional hopper, controls if automatic, and safety guarding.

- [ ] Decision ID: `pellet_press.split_high_throughput_pelletizing`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split bulk pellet mills or briquetting presses from the lab/pilot pellet press if high throughput is needed.
  - Queue task: Review catalyst, regolith, and powder metallurgy uses; create or route high-throughput bulk pelletizing to `pellet_mill` or `briquetting_press` if the needed mechanism is roller-die, extrusion, or production compaction rather than lab die pressing.

- [ ] Decision ID: `pellet_press.consolidate_to_molding_or_hydraulic_press`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Consolidate to `molding_press_basic` or `hydraulic_press` plus die tooling if a separate pellet press is unnecessary.
  - Queue task: Compare pellet pressing uses with `molding_press_basic` and `hydraulic_press`; migrate references if a general press plus pellet die set captures the process adequately.

- [ ] Decision ID: `pellet_press.no_action`
  - Action type: `no_action`
  - Action: Leave the current pellet press stub unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `pellet_press.model_die_sets`
  - Action type: `consumable_or_tooling_modeling`, `bom_or_recipe_update`
  - Action: Model dies as separate tooling per pellet shape/material if needed.
  - Queue task: Add or link hardened die sleeve/punch/ejector tooling, with shape/material-specific variants where pellet diameter, pressure, wear, or contamination matters.

- [ ] Decision ID: `pellet_press.add_process_parameters`
  - Action type: `process_requirement_update`, `note_cleanup`
  - Action: Add pellet diameter, pressure, dwell time, throughput, binder, and powder-prep assumptions.
  - Queue task: Audit pellet pressing processes and document pressing pressure, pellet size, dwell, throughput, binder content, powder preparation, and ejection assumptions.

- [ ] Decision ID: `pellet_press.add_downstream_steps`
  - Action type: `process_requirement_update`
  - Action: Add drying, calcination, sintering, or screening where pellets require post-processing.
  - Queue task: Review catalyst, regolith cathode, ceramic, and powder metallurgy pellet workflows; add downstream drying/calcination/sintering/screening requirements where needed.

- [ ] Decision ID: `pellet_press.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## plastic_extruder

Source review: `research/machines/plastic_extruder.md`

Current interpretation: Real small single-screw plastic extruder for shop/lab production of profiles, simple sheet/gasket stock, and coarse filament/profile output.

### Primary Path - Choose One

- [ ] Decision ID: `plastic_extruder.keep_generic_single_screw_extruder`
  - Action type: `note_cleanup`
  - Action: Keep as a generic small single-screw plastic extruder.
  - Queue task: Clarify item notes to "small single-screw plastic extruder" with feed hopper, heated barrel, screw, motor/gearbox, die/head, heating/cooling, controls, and instrumentation.

- [ ] Decision ID: `plastic_extruder.split_by_extrusion_line_type`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split only if desktop filament, pipe/profile, sheet line, and recycled-plastic beam extrusion need different capacities.
  - Queue task: Audit extrusion processes and route to specific extruder/line variants where throughput, die, downstream cooling/pulling, or product geometry differ materially.

- [ ] Decision ID: `plastic_extruder.no_action`
  - Action type: `no_action`
  - Action: Leave `plastic_extruder` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `plastic_extruder.add_downstream_line_equipment`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Add cooling bath/table, haul-off/puller, cutter, winder, sheet calendar/roll stack, and diameter/thickness measurement where needed.
  - Queue task: Audit sheet, gasket, filament, projection-screen, and profile extrusion processes and add downstream line equipment beyond the bare extruder.

- [ ] Decision ID: `plastic_extruder.preserve_critical_components`
  - Action type: `bom_or_recipe_update`
  - Action: Preserve screw/barrel, extruder head/die, heaters, motor/gearbox, controls, and sensors as critical components for manufacturing closure.
  - Queue task: Review BOM and recipes so the extruder is not collapsed into vague mass if later local manufacturing closure work needs detail.

- [ ] Decision ID: `plastic_extruder.review_heater_resource`
  - Action type: `bom_or_recipe_update`, `reference_migration`
  - Action: Check whether `heating_plate_induction_heater` is the right heater component for extruder barrel heating.
  - Queue task: Replace generic heating-plate/induction heater references with barrel heaters, band heaters, or heating jackets if more accurate.

- [ ] Decision ID: `plastic_extruder.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## plate_rolling_mill

Source review: `research/machines/plate_rolling_mill.md`

Current interpretation: Real canonical flat rolling/reduction mill for plate, sheet, strip, and bar stock. The name can be confused with roll-bending machines for curved shells.

### Primary Path - Choose One

- [ ] Decision ID: `plate_rolling_mill.keep_canonical_flat_rolling_mill`
  - Action type: `note_cleanup`, `dedupe_or_consolidation`
  - Action: Keep as the canonical rolling mill for flat rolling/reduction operations.
  - Queue task: Update notes/display wording to clarify that `plate_rolling_mill` is a flat rolling/reduction mill with work rolls, frame, drive, roll adjustment, and alignment, not primarily a plate roll-bending machine.

- [ ] Decision ID: `plate_rolling_mill.split_rolling_by_scale_or_type`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split only if hot rolling, cold rolling, thin strip, bar, or heavy plate require materially different mills.
  - Queue task: Audit rolling processes and create or route to separate rolling mill variants only where stock size, temperature, roll force, roll count, stiffness, or surface quality requires it.

- [ ] Decision ID: `plate_rolling_mill.no_action`
  - Action type: `no_action`
  - Action: Leave `plate_rolling_mill` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `plate_rolling_mill.keep_roll_bending_distinct`
  - Action type: `process_requirement_update`, `dedupe_or_consolidation`
  - Action: Use `press_brake` for straight-line bending and a plate roller/roll bender for cylindrical shell forming if that becomes distinct.
  - Queue task: Audit sheet/plate forming processes and separate flat reduction from bending/curving operations where geometry matters.

- [ ] Decision ID: `plate_rolling_mill.review_mass_and_capacity`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Review 1501 kg mass against target width, thickness, roll diameter, material, and stock temperature.
  - Queue task: Document maximum sheet/plate width/thickness, material classes, hot/cold rolling assumptions, and whether 1501 kg represents a small/light mill only.

- [ ] Decision ID: `plate_rolling_mill.add_roll_quality_notes`
  - Action type: `bom_or_recipe_update`, `note_cleanup`
  - Action: Preserve hardened/ground rolls, bearings, frame stiffness, alignment, and roll-set quality as realism-critical.
  - Queue task: Update BOM/notes for roll hardness, grinding, surface finish, bearings, frame stiffness, alignment, and roll adjustment.

- [ ] Decision ID: `plate_rolling_mill.separate_reheating_capacity`
  - Action type: `process_requirement_update`
  - Action: Keep reheating/annealing furnace capacity separate from the rolling mill.
  - Queue task: Ensure hot rolling processes require appropriate heating/reheating furnaces and do not imply the mill itself heats stock.

- [ ] Decision ID: `plate_rolling_mill.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## powder_mixer

Source review: `research/machines/powder_mixer.md`

Current interpretation: Real small powder blender for metal/ceramic powders, binders, lubricants, and powder-metallurgy feedstock preparation. It overlaps with `mixer_or_blender` but has powder-specific cleanliness and uniformity concerns.

### Primary Path - Choose One

- [ ] Decision ID: `powder_mixer.keep_distinct_powder_blender`
  - Action type: `note_cleanup`, `dedupe_or_consolidation`
  - Action: Keep as a distinct small powder blender where dry powder uniformity, dust containment, binder/lubricant addition, or powder metallurgy quality matters.
  - Queue task: Clarify `powder_mixer` as a small powder blender for metal/ceramic powders, with notes on powder uniformity, contamination control, dust containment, and cleanout.

- [ ] Decision ID: `powder_mixer.consolidate_to_mixer_or_blender`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Consolidate into `mixer_or_blender` if the KB wants one generic small mixer category.
  - Queue task: Compare `powder_mixer` and `mixer_or_blender`; migrate references if powder-specific behavior is not modeled separately.

- [ ] Decision ID: `powder_mixer.no_action`
  - Action type: `no_action`
  - Action: Leave `powder_mixer` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `powder_mixer.specify_subtype`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Specify whether this is a ribbon blender, tumbler/V blender, conical screw mixer, or other small powder blender.
  - Queue task: Update notes/BOM to match selected subtype, including vessel/drum/trough, agitator/ribbon/tumble mechanism, seals, discharge, motor/drive, and controls.

- [ ] Decision ID: `powder_mixer.add_dust_and_safety_requirements`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Add dust sealing, ventilation, contamination control, and cleaning requirements where powder safety matters.
  - Queue task: Audit powder processes and add containment, dust collection, PPE/ventilation, explosion/reactivity precautions, and cleaning/changeover assumptions as needed.

- [ ] Decision ID: `powder_mixer.split_high_shear_granulation`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Do not assume a low-shear powder mixer covers binder granulation or agglomerate breakdown.
  - Queue task: Add or route binder addition/granulation processes to a high-shear mixer/granulator where selected.

- [ ] Decision ID: `powder_mixer.keep_distinct_from_cement_mixer`
  - Action type: `dedupe_or_consolidation`, `process_requirement_update`
  - Action: Keep separate from `cement_mixer_small` because concrete/cement mixing differs from powder-metallurgy blending.
  - Queue task: Ensure abrasive aggregate/cement/castable processes use cement/refractory mixers and powder-metallurgy feedstock uses powder-specific blending resources.

- [ ] Decision ID: `powder_mixer.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## power_conditioning_equipment

Source review: `research/machines/power_conditioning_equipment.md`

Current interpretation: Real integrated electrical power-conditioning subsystem/cabinet for conversion, regulation, protection, filtering, and controls. It is active electrical equipment, not labor/tooling.

### Primary Path - Choose One

- [ ] Decision ID: `power_conditioning_equipment.keep_integrated_cabinet`
  - Action type: `note_cleanup`, `infrastructure_or_subsystem_modeling`
  - Action: Keep as an integrated system-level power-conditioning cabinet for coarse solar/thermionic generation modeling.
  - Queue task: Update notes to define `power_conditioning_equipment` as an integrated cabinet including inverters, DC/DC conversion, voltage regulation, protection, filters, thermal management, monitoring, and controls.

- [ ] Decision ID: `power_conditioning_equipment.split_by_electrical_function`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split by power function and power level where recipes require specific electrical behavior.
  - Queue task: Route process requirements to specific items such as `inverter_dc_to_ac_v0`, `power_supply_dc_high_current_v0`, rectifier, DC/DC converter, voltage regulator, UPS/line conditioner, or thermionic converter power electronics where needed.

- [ ] Decision ID: `power_conditioning_equipment.no_action`
  - Action type: `no_action`
  - Action: Leave `power_conditioning_equipment` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `power_conditioning_equipment.clarify_power_rating_outputs`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Add power rating and output assumptions for the 80 kg item.
  - Queue task: Document power rating, input source, AC/DC outputs, voltage/current ranges, duty cycle, cooling, and enclosure scope.

- [ ] Decision ID: `power_conditioning_equipment.split_thermionic_from_solar`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Separate thermionic converter power conditioning from solar PV/grid-style conditioning if requirements differ.
  - Queue task: Review thermionic power recipes and solar generation processes; split source/load matching and conversion hardware if thermionic output needs distinct DC/DC/regulation behavior.

- [ ] Decision ID: `power_conditioning_equipment.define_module_vs_cabinet`
  - Action type: `infrastructure_or_subsystem_modeling`, `dedupe_or_consolidation`
  - Action: Decide whether `power_conditioning_module` is the reusable subcomponent and this item is the assembled cabinet.
  - Queue task: Compare `power_conditioning_module` and `power_conditioning_equipment`; document component/cabinet relationship or consolidate duplicates.

- [ ] Decision ID: `power_conditioning_equipment.preserve_active_machine_requirement`
  - Action type: `process_requirement_update`
  - Action: Do not replace this with labor bot plus tools; labor only installs, wires, and commissions it.
  - Queue task: Ensure processes requiring power conversion/regulation require active electrical equipment, with labor/tooling listed only for installation and commissioning.

- [ ] Decision ID: `power_conditioning_equipment.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## power_distribution_bus

Source review: `research/machines/power_distribution_bus.md`

Current interpretation: Real high-current electrical distribution infrastructure/equipment, best understood as a busbar cabinet or distribution assembly rather than a material-processing machine.

### Primary Path - Choose One

- [ ] Decision ID: `power_distribution_bus.keep_busbar_distribution_assembly`
  - Action type: `note_cleanup`, `infrastructure_or_subsystem_modeling`
  - Action: Keep as a power distribution busbar cabinet/assembly.
  - Queue task: Rename or annotate as "power distribution busbar cabinet" or "busbar distribution assembly" with copper/aluminum conductors, insulators, supports, terminals, enclosure/guarding, and safe high-current distribution role.

- [ ] Decision ID: `power_distribution_bus.bundle_into_switchgear_panel`
  - Action type: `split_item`, `infrastructure_or_subsystem_modeling`
  - Action: Treat busbars as part of broader electrical distribution panel/switchgear if protection and controls are bundled.
  - Queue task: Decide whether to create or route to a broader switchgear/distribution-panel item including breakers, disconnects, protection, metering, grounding, enclosures, and busbars.

- [ ] Decision ID: `power_distribution_bus.no_action`
  - Action type: `no_action`
  - Action: Leave `power_distribution_bus` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `power_distribution_bus.keep_distinct_from_power_conditioning`
  - Action type: `dedupe_or_consolidation`, `process_requirement_update`
  - Action: Keep power distribution distinct from inverters, rectifiers, and control electronics.
  - Queue task: Audit power processes and ensure busbar distribution is not substituted for `power_conditioning_equipment` or high-current power supplies; busbars distribute power, they do not condition it.

- [ ] Decision ID: `power_distribution_bus.add_voltage_current_rating`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Add AC/DC, voltage, current, thermal, short-circuit, and environment ratings.
  - Queue task: Document whether the bus is AC, DC, or both; size by chloralkali electrolysis and seed-system current/voltage needs.

- [ ] Decision ID: `power_distribution_bus.add_protection_and_grounding`
  - Action type: `bom_or_recipe_update`, `infrastructure_or_subsystem_modeling`
  - Action: Add fuses/breakers, disconnects, grounding bars, enclosures, clearances, and testing if high-current realism matters.
  - Queue task: Update BOM/notes to include protection devices, grounding, creepage/clearance, insulation, enclosure, thermal management, and short-circuit force tolerance.

- [ ] Decision ID: `power_distribution_bus.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## power_hammer_or_press

Source review: `research/machines/power_hammer_or_press.md`

Current interpretation: Real assisted hot-forging machine category, but current ID is ambiguous. The BOM reads more like a forging power hammer than a generic press.

### Primary Path - Choose One

- [ ] Decision ID: `power_hammer_or_press.rename_as_forging_power_hammer`
  - Action type: `rename_or_alias`, `note_cleanup`
  - Action: Interpret and rename/rescope as `forging_power_hammer_basic`.
  - Queue task: Update name/notes to reflect hammer frame, hammer head, drive motor, anvil block, controls, and repeated impact forging role; preserve use with `induction_forge_v0` and `anvil_or_die_set`.

- [ ] Decision ID: `power_hammer_or_press.keep_coarse_hammer_or_press_abstraction`
  - Action type: `deferred_schema_or_modeling_decision`, `note_cleanup`
  - Action: Keep as a coarse low-volume assisted hot-forging abstraction covering hammer or press.
  - Queue task: Document that this item is a temporary broad forging-force resource and should be specialized if impact versus sustained pressure matters.

- [ ] Decision ID: `power_hammer_or_press.split_hammer_and_forging_press`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split impact hammering from sustained-pressure forging.
  - Queue task: Route impact forging to `forging_power_hammer_basic` and sustained/closed-die press forging to `forging_press_v0`, `forging_press_basic`, or `hydraulic_press` after dedupe review.

- [ ] Decision ID: `power_hammer_or_press.no_action`
  - Action type: `no_action`
  - Action: Leave `power_hammer_or_press` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `power_hammer_or_press.dedupe_v0_references`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Review `power_hammer_or_press_v0` references and recipes for migration/deprecation.
  - Queue task: Search for `power_hammer_or_press_v0`; migrate, alias, or deprecate in favor of the selected canonical item.

- [ ] Decision ID: `power_hammer_or_press.define_forging_equipment_hierarchy`
  - Action type: `dedupe_or_consolidation`, `deferred_schema_or_modeling_decision`
  - Action: Define the relationship among `power_hammer_or_press`, `forging_press_v0`, and `hydraulic_press`.
  - Queue task: Document a clear hierarchy: general hydraulic press, forging press for sustained hot forging, and power hammer for impact forging.

- [ ] Decision ID: `power_hammer_or_press.add_safety_foundation_tooling`
  - Action type: `bom_or_recipe_update`, `note_cleanup`
  - Action: Add foundation stiffness, guarding, controls, die alignment, and anvil/die tooling assumptions.
  - Queue task: Update BOM/notes for safety guarding, foundation/anvil mass, die retention, controls, and alignment requirements.

- [ ] Decision ID: `power_hammer_or_press.preserve_active_machine_requirement`
  - Action type: `process_requirement_update`
  - Action: Do not replace with labor bot plus hand tools.
  - Queue task: Ensure hot-forging processes keep an active high-force impact/press resource; labor may cover setup, heating, and manipulation only.

- [ ] Decision ID: `power_hammer_or_press.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## power_supply_benchtop

Source review: `research/machines/power_supply_benchtop.md`

Current interpretation: Real low-power regulated DC bench instrument for electronics testing, calibration, and small experimental rigs. It should stay distinct from high-current process supplies.

### Primary Path - Choose One

- [ ] Decision ID: `power_supply_benchtop.keep_low_power_bench_supply`
  - Action type: `note_cleanup`
  - Action: Keep as a representative small adjustable DC bench supply.
  - Queue task: Clarify `power_supply_benchtop` as a low-power CV/CC bench supply, e.g. representative 0-30 V and 0-3 A if acceptable, for circuit bring-up and calibration.

- [ ] Decision ID: `power_supply_benchtop.consolidate_with_power_supply_bench`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Merge with `power_supply_bench` if both represent the same instrument.
  - Queue task: Compare `power_supply_benchtop` and `power_supply_bench`; consolidate, alias, or define scope differences.

- [ ] Decision ID: `power_supply_benchtop.no_action`
  - Action type: `no_action`
  - Action: Leave `power_supply_benchtop` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `power_supply_benchtop.resolve_path_kind_mismatch`
  - Action type: `note_cleanup`, `deferred_schema_or_modeling_decision`
  - Action: Resolve or document that file path is under `parts` while `kind` is `machine`.
  - Queue task: Move/reclassify if schema policy requires consistency, or add notes explaining machine-kind as reusable test equipment despite item path.

- [ ] Decision ID: `power_supply_benchtop.keep_high_current_supplies_distinct`
  - Action type: `process_requirement_update`, `dedupe_or_consolidation`
  - Action: Keep distinct from electrolysis, welding, furnace, hot-wire, and high-current process supplies.
  - Queue task: Audit references and route process equipment power needs to `high_temperature_power_supply_v0`, `power_supply_dc_high_current`, `welding_power_supply_v0`, or other appropriate supplies.

- [ ] Decision ID: `power_supply_benchtop.add_output_noise_calibration`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Add output range, ripple/noise, current-limit, and calibration assumptions if test processes need them.
  - Queue task: Document voltage/current range, ripple/noise, regulation, current limit, and whether calibration standards are separate.

- [ ] Decision ID: `power_supply_benchtop.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## precision_lathe

Source review: `research/machines/precision_lathe.md`

Current interpretation: Real toolroom/precision lathe, plausibly 1200 kg, for accurate turning, boring, threading, leadscrews, ball screws, shafts, headstocks, and valve bores.

### Primary Path - Choose One

- [ ] Decision ID: `precision_lathe.keep_high_precision_turning_machine`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep distinct from `lathe_engine_v0` and milling machines as a higher-precision turning resource.
  - Queue task: Clarify `precision_lathe` as a toolroom/precision lathe used where spindle runout, bed straightness, feed accuracy, rigidity, and concentricity are critical; preserve separate lower-tier engine-lathe capability.

- [ ] Decision ID: `precision_lathe.add_cnc_turning_center_variant`
  - Action type: `split_item`, `deferred_schema_or_modeling_decision`
  - Action: Add/map a separate CNC turning center if CNC capability matters later.
  - Queue task: Do not silently upgrade `precision_lathe` to CNC; create or route to a CNC lathe/turning center only where programmed repeated turning capability is required.

- [ ] Decision ID: `precision_lathe.no_action`
  - Action type: `no_action`
  - Action: Leave `precision_lathe` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `precision_lathe.add_tolerance_assumptions`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Add intended tolerance tier, such as 0.01 mm, 0.005 mm, or better.
  - Queue task: Document tolerance/roundness/runout assumptions and route processes exceeding turning capability to grinding/lapping.

- [ ] Decision ID: `precision_lathe.require_metrology_tooling_coolant`
  - Action type: `process_requirement_update`, `consumable_or_tooling_modeling`
  - Action: Require precision metrology, cutting tools, workholding, coolant, and possibly grinding/lapping for highest-accuracy components.
  - Queue task: Audit precision turning processes and add requirements for chucks/collets/centers, cutting tools, coolant, indicators, micrometers, gauge blocks, surface plate, and grinding/lapping where needed.

- [ ] Decision ID: `precision_lathe.mark_local_build_as_advanced`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Treat local manufacture as advanced machine-tool reproduction, not a simple assembly task.
  - Queue task: Add notes/BOM requirements for cast/stress-relieved bed, scraped/ground ways, spindle bearings, leadscrew accuracy, alignment, calibration, and recursive machine-tool/metrology dependencies.

- [ ] Decision ID: `precision_lathe.review_screw_manufacturing_route`
  - Action type: `process_requirement_update`, `research_or_design_followup`
  - Action: Decide whether ballscrews/leadscrews are cut on the lathe alone or finished by grinding/lapping.
  - Queue task: Review ballscrew and leadscrew fabrication processes and add finishing/metrology requirements where precision exceeds lathe-only cutting.

- [ ] Decision ID: `precision_lathe.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## precision_levels

Source review: `research/machines/precision_levels.md`

Current interpretation: Real calibrated metrology tooling for machine leveling and alignment, not powered production machinery. Accuracy target of 0.02 mm/m is commercially realistic.

### Primary Path - Choose One

- [ ] Decision ID: `precision_levels.keep_separate_alignment_metrology`
  - Action type: `note_cleanup`, `consumable_or_tooling_modeling`
  - Action: Keep separate from broad inspection tools because machine-tool alignment is a core process.
  - Queue task: Rename or annotate as `precision_level_set` or `precision_machinist_levels`; describe as calibrated metrology tooling for machine-frame leveling, way alignment, shimming, and angular verification.

- [ ] Decision ID: `precision_levels.consolidate_into_measurement_equipment`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Consolidate into `measurement_equipment` if the KB does not need a separate machine-alignment tool ID.
  - Queue task: Compare `precision_levels`, `alignment_tools`, and `measurement_equipment`; migrate references or define a clear separate alignment-metrology role.

- [ ] Decision ID: `precision_levels.no_action`
  - Action type: `no_action`
  - Action: Leave `precision_levels` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `precision_levels.add_realistic_components`
  - Action type: `bom_or_recipe_update`
  - Action: Add precision vial or electronic tilt sensor, adjustment hardware, protective case, and calibration/reference requirements.
  - Queue task: Update BOM/recipe to include spirit vial or electronic sensor module, adjustment screws/locking hardware, stable base/body, protective case, and calibration procedure.

- [ ] Decision ID: `precision_levels.fix_recipe_material_mismatch`
  - Action type: `bom_or_recipe_update`
  - Action: Fix aluminum inputs producing `machined_steel_part_precision`.
  - Queue task: Correct recipe output/material assumptions so aluminum stock does not produce a steel precision part, or change inputs/output to the intended material.

- [ ] Decision ID: `precision_levels.specify_variant`
  - Action type: `note_cleanup`, `deferred_schema_or_modeling_decision`
  - Action: Decide whether the item is a spirit level, electronic inclinometer, or kit containing both.
  - Queue task: Document selected variant and calibration standard available in the self-reproduction chain.

- [ ] Decision ID: `precision_levels.route_higher_precision_alignment`
  - Action type: `process_requirement_update`
  - Action: Use optical metrology or laser alignment for larger or higher-precision tasks where levels are insufficient.
  - Queue task: Audit precision alignment processes and route high-end work to `optical_metrology_tools`, laser alignment systems, autocollimators, surface plates, or straightedges as needed.

- [ ] Decision ID: `precision_levels.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## precision_tooling_set

Source review: `research/machines/precision_tooling_set.md`

Current interpretation: Real precision machine-tool cutter/toolholder inventory for lathes, mills, drills, and CNC machines. It is tooling and partly consumable, not an active machine.

### Primary Path - Choose One

- [ ] Decision ID: `precision_tooling_set.keep_precision_machine_tooling`
  - Action type: `consumable_or_tooling_modeling`, `note_cleanup`
  - Action: Keep as precision tooling for machine-tool operations, distinct from broad manual cutting tools.
  - Queue task: Clarify `precision_tooling_set` as end mills, drills, reamers, taps, boring bars, inserts, holders, and related precision cutters for machine tools; keep `cutting_tools_general` for broad manual/basic cutting.

- [ ] Decision ID: `precision_tooling_set.split_specialty_tooling`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Add explicit specialty tooling where processes require gear hobs, broaches, thread taps, boring heads, carbide inserts, or form tools.
  - Queue task: Audit precision machining processes and add specialized cutter/toolholder requirements where generic precision tooling is too broad.

- [ ] Decision ID: `precision_tooling_set.no_action`
  - Action type: `no_action`
  - Action: Leave `precision_tooling_set` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `precision_tooling_set.reclassify_as_tooling`
  - Action type: `consumable_or_tooling_modeling`
  - Action: Reclassify or document as tooling/consumables rather than machine.
  - Queue task: Resolve or document `kind: machine` for a tooling set under `kb/items/parts`; preserve reusable process-resource semantics.

- [ ] Decision ID: `precision_tooling_set.model_tool_wear`
  - Action type: `consumable_or_tooling_modeling`
  - Action: Treat cutting tool wear, chipping, sharpening, and replacement as consumable behavior if process accounting becomes detailed.
  - Queue task: Add conservative wear/replacement assumptions or notes for end mills, drills, taps, reamers, inserts, and HSS bits.

- [ ] Decision ID: `precision_tooling_set.limit_local_carbide_claims`
  - Action type: `bom_or_recipe_update`, `note_cleanup`
  - Action: Avoid implying carbide inserts and coated tools are easy local products.
  - Queue task: Update recipe/notes so HSS tooling is locally plausible with heat treatment and grinding, while carbide/coated/specialty tooling requires powder metallurgy, sintering, grinding, coatings, or import/advanced chains.

- [ ] Decision ID: `precision_tooling_set.decide_toolholders_collets_vises`
  - Action type: `consumable_or_tooling_modeling`, `bom_or_recipe_update`
  - Action: Decide whether toolholders, collets, chucks, vises, and workholding are included or separate.
  - Queue task: Document or split toolholding/workholding items so process requirements are not hidden inside the cutter set.

- [ ] Decision ID: `precision_tooling_set.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## press_brake

Source review: `research/machines/press_brake.md`

Current interpretation: Real specialized sheet/plate bending machine for straight-line matched punch-and-die bends. It should not be a catch-all forming press.

### Primary Path - Choose One

- [ ] Decision ID: `press_brake.keep_specialized_straight_bending_machine`
  - Action type: `note_cleanup`, `dedupe_or_consolidation`
  - Action: Keep as a specialized forming resource distinct from `plate_rolling_mill`, `hydraulic_press`, and `stamping_press_basic`.
  - Queue task: Preserve notes that `press_brake` is for straight-line sheet/plate bending with interchangeable punch/die tooling; use generic presses, rollers, or stamping presses for other forming mechanics.

- [ ] Decision ID: `press_brake.consolidate_for_coarse_forming`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Consolidate into broader forming resources only if straight-bend fidelity is intentionally out of scope.
  - Queue task: Review `press_brake` process references and migrate to `metal_forming_basic_v0` or `hydraulic_press` only if matched punch/die bending does not matter.

- [ ] Decision ID: `press_brake.no_action`
  - Action type: `no_action`
  - Action: Leave `press_brake` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `press_brake.keep_die_set_separate`
  - Action type: `consumable_or_tooling_modeling`, `bom_or_recipe_update`
  - Action: Keep `press_brake_die_set` as separate tooling.
  - Queue task: Ensure press-brake processes require punch/die tooling separately where bend radius, material thickness, or geometry matters.

- [ ] Decision ID: `press_brake.add_tonnage_bend_length`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Add tonnage and bend-length assumptions for the 846 kg machine.
  - Queue task: Document target bend length, material thickness, tonnage, daylight/stroke, and whether this is light industrial versus benchtop/shop scale.

- [ ] Decision ID: `press_brake.audit_process_fit`
  - Action type: `process_requirement_update`
  - Action: Check whether fastener and motor-housing processes truly need press-brake bending or could use simpler manual brake/folder.
  - Queue task: Review current process uses and route small/simple bends to simpler sheet-metal brake/folder resources if selected.

- [ ] Decision ID: `press_brake.review_size_variants`
  - Action type: `split_item`, `deferred_schema_or_modeling_decision`
  - Action: Add larger press-brake size only if future plate-thickness or throughput needs exceed Conservative Mode reuse.
  - Queue task: Compare required bend capacity against 5x reuse rule before introducing size variants.

- [ ] Decision ID: `press_brake.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## press_brake_die_set

Source review: `research/machines/press_brake_die_set.md`

Current interpretation: Real interchangeable press brake punch/die tooling set. It is necessary tooling for sheet-metal bending, not a standalone powered machine.

### Primary Path - Choose One

- [ ] Decision ID: `press_brake_die_set.keep_separate_tooling`
  - Action type: `consumable_or_tooling_modeling`, `note_cleanup`
  - Action: Keep separate from `press_brake` as a tooling set.
  - Queue task: Rename or annotate as `press_brake_tooling_set`; preserve separate process requirement because a press brake without matched punches/dies is incomplete.

- [ ] Decision ID: `press_brake_die_set.bundle_into_press_brake`
  - Action type: `dedupe_or_consolidation`, `bom_or_recipe_update`
  - Action: Bundle into `press_brake` only if the KB deliberately treats standard tooling as included with the machine.
  - Queue task: Decide whether standard punch/die set is included in `press_brake`; if bundled, update BOM/process references so tooling availability remains explicit.

- [ ] Decision ID: `press_brake_die_set.no_action`
  - Action type: `no_action`
  - Action: Leave `press_brake_die_set` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `press_brake_die_set.reclassify_as_tooling`
  - Action type: `consumable_or_tooling_modeling`
  - Action: Change or document `kind: machine` as tooling/part classification when schema support allows it.
  - Queue task: Move or annotate as tooling while preserving process-resource semantics.

- [ ] Decision ID: `press_brake_die_set.define_tooling_standard`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Define the assumed tooling interface standard or state that it is abstract-compatible with the modeled press brake.
  - Queue task: Document American, European, WILA/Trumpf-style, or abstract compatible punch/die interface assumptions.

- [ ] Decision ID: `press_brake_die_set.add_special_bend_tooling_variants`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Add bend-specific tooling only for tight-radius, hemming, offset, box forming, or surface-sensitive operations.
  - Queue task: Audit bending processes and add specialized dies/punches only where process geometry or surface finish requires them.

- [ ] Decision ID: `press_brake_die_set.preserve_precision_manufacturing_route`
  - Action type: `bom_or_recipe_update`, `note_cleanup`
  - Action: Preserve tool steel, machining, heat treatment, precision grinding, and inspection requirements.
  - Queue task: Ensure recipe does not reduce press brake tooling to simple cutting/welded fabrication; retain heat-treatment and grinding realism.

- [ ] Decision ID: `press_brake_die_set.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## press_ram_set

Source review: `research/machines/press_ram_set.md`

Current interpretation: Real press ram/adapter/tooling set that transfers force from a press to workpieces or dies. It is not a standalone press or powered machine.

### Primary Path - Choose One

- [ ] Decision ID: `press_ram_set.keep_as_press_tooling_accessory`
  - Action type: `consumable_or_tooling_modeling`, `note_cleanup`
  - Action: Keep as press ram/adapters/tooling only where geometry affects process capability.
  - Queue task: Clarify `press_ram_set` as press tooling/accessories that must be paired with `hydraulic_press` or another actual press; document whether 30 kg is adapters or a major moving ram/platen subassembly.

- [ ] Decision ID: `press_ram_set.fold_into_pressing_tooling`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Fold into `pressing_mold_set` or generic press tooling if it is only adapter inventory.
  - Queue task: Review `pressing_operations_basic_v0`; remove separate `press_ram_set` requirement if the basic hydraulic press/tooling already includes ordinary rams/platens/adapters.

- [ ] Decision ID: `press_ram_set.no_action`
  - Action type: `no_action`
  - Action: Leave `press_ram_set` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `press_ram_set.reclassify_as_tooling`
  - Action type: `consumable_or_tooling_modeling`
  - Action: Reclassify or document as part/tooling when schema support allows.
  - Queue task: Move or annotate `press_ram_set` as tooling/accessory rather than machine while preserving process-resource semantics.

- [ ] Decision ID: `press_ram_set.audit_specific_ram_geometry`
  - Action type: `process_requirement_update`
  - Action: Retain separate ram tooling only where broaching, stamping, coining, or special press work requires specific geometry.
  - Queue task: Audit press processes for actual ram/plunger/adapter geometry requirements; add specific tooling only where needed.

- [ ] Decision ID: `press_ram_set.preserve_material_finish_requirements`
  - Action type: `bom_or_recipe_update`
  - Action: Preserve hardened steel, finish, straightness, and fit requirements.
  - Queue task: Ensure the recipe models hardened/finished ram adapters and does not imply manufacturing hydraulic cylinders or the entire press.

- [ ] Decision ID: `press_ram_set.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## pressing_mold_set

Source review: `research/machines/pressing_mold_set.md`

Current interpretation: Real powder/ceramic/ferrite/regolith pressing mold and die tooling set. It does not provide pressing force and should stay separate from press machines.

### Primary Path - Choose One

- [ ] Decision ID: `pressing_mold_set.keep_generic_press_tooling`
  - Action type: `consumable_or_tooling_modeling`, `note_cleanup`
  - Action: Keep as a generic reusable pressing mold/die set for coarse modeling.
  - Queue task: Clarify `pressing_mold_set` as dies, punches, cavity plates, ejectors, and mold frames used with a hydraulic, pellet, molding, or hot press.

- [ ] Decision ID: `pressing_mold_set.split_geometry_specific_molds`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Add part-specific molds where geometry matters.
  - Queue task: Audit ferrite toroids, regolith bricks, battery electrodes, ceramic blocks, reactor linings, and pellet processes; add dedicated mold/die tooling where shape, clearance, ejection, or compaction pressure matters.

- [ ] Decision ID: `pressing_mold_set.no_action`
  - Action type: `no_action`
  - Action: Leave `pressing_mold_set` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `pressing_mold_set.reclassify_as_tooling`
  - Action type: `consumable_or_tooling_modeling`
  - Action: Reclassify or document as tooling/part set when schema support allows.
  - Queue task: Move or annotate `pressing_mold_set` as reusable tooling rather than machine while preserving process-resource semantics.

- [ ] Decision ID: `pressing_mold_set.distinguish_hot_press_dies`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Distinguish cold powder pressing dies from hot-press dies if temperature/material compatibility matters.
  - Queue task: Add graphite, silicon nitride, refractory, or high-temperature die tooling for hot pressing where steel dies are unsuitable.

- [ ] Decision ID: `pressing_mold_set.model_die_wear`
  - Action type: `consumable_or_tooling_modeling`
  - Action: Model die wear/replacement for abrasive regolith, ceramics, and high-pressure powder metallurgy if needed.
  - Queue task: Add wear/lifetime notes or consumable assumptions for abrasive powders and repeated high-pressure compaction.

- [ ] Decision ID: `pressing_mold_set.preserve_precision_tooling_route`
  - Action type: `bom_or_recipe_update`, `note_cleanup`
  - Action: Preserve precision machining, heat treatment, surface finish, clearances, ejector design, and strength requirements.
  - Queue task: Ensure recipe models hardened/wear-resistant materials, polished cavity surfaces, controlled clearances, lubrication/venting, and ejection details where appropriate.

- [ ] Decision ID: `pressing_mold_set.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## pyrolysis_chamber_v0

Source review: `research/machines/pyrolysis_chamber_v0.md`

Current interpretation: Real methane pyrolysis reactor/chamber concept, but specialized and underspecified. It should not be treated as a generic high-temperature reactor without gas, hydrogen, and carbon handling.

### Primary Path - Choose One

- [ ] Decision ID: `pyrolysis_chamber_v0.rename_methane_pyrolysis_reactor`
  - Action type: `rename_or_alias`, `note_cleanup`
  - Action: Rename or document as `methane_pyrolysis_reactor_v0` if methane pyrolysis is its only current use.
  - Queue task: Update notes/name to describe a small experimental/pilot methane pyrolysis reactor operating around 800-1200 C with refractory lining, heating, gas feed, seals, product handling, and safety controls.

- [ ] Decision ID: `pyrolysis_chamber_v0.keep_generic_pyrolysis_chamber`
  - Action type: `deferred_schema_or_modeling_decision`, `note_cleanup`
  - Action: Keep generic pyrolysis chamber only if future polymer, ceramic, mineral, or gas pyrolysis processes need a shared abstraction.
  - Queue task: Document excluded/variable requirements by feedstock: temperature, atmosphere, pressure, gas products, condensables, solids, carbon deposition, and residue handling.

- [ ] Decision ID: `pyrolysis_chamber_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `pyrolysis_chamber_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `pyrolysis_chamber_v0.add_gas_carbon_handling`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Add methane feed, purge/inerting, hydrogen handling/purification, carbon collection/removal, filters/traps, and exhaust treatment.
  - Queue task: Update `methane_pyrolysis_v0` requirements so reactor output handling and flammable gas safety are not hidden inside a simple chamber item.

- [ ] Decision ID: `pyrolysis_chamber_v0.specify_reactor_design`
  - Action type: `research_or_design_followup`, `process_requirement_update`
  - Action: Decide whether reactor mechanism is thermal, catalytic, plasma, molten-metal, or fluidized-bed pyrolysis.
  - Queue task: Add a design followup or process note selecting pyrolysis mechanism and associated equipment requirements.

- [ ] Decision ID: `pyrolysis_chamber_v0.clarify_carbon_product`
  - Action type: `process_requirement_update`, `note_cleanup`
  - Action: Clarify whether product is carbon black, graphite-like carbon, or generic solid carbon.
  - Queue task: Update product/process notes and downstream handling assumptions for the selected carbon form.

- [ ] Decision ID: `pyrolysis_chamber_v0.keep_separate_from_generic_reactors`
  - Action type: `dedupe_or_consolidation`, `process_requirement_update`
  - Action: Keep separate from `chemical_reactor_basic` because high-temperature methane gas/carbon handling is distinct.
  - Queue task: Audit reactor references and avoid routing methane pyrolysis to a generic reactor unless all gas/carbon/safety requirements are explicitly modeled.

- [ ] Decision ID: `pyrolysis_chamber_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## quench_tank

Source review: `research/machines/quench_tank.md`

Current interpretation: Real small controlled quench tank/equipment for heat-treatment cooling, not merely a passive bucket. Medium choice drives safety and process behavior.

### Primary Path - Choose One

- [ ] Decision ID: `quench_tank.keep_generic_controlled_quench_tank`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep as a generic controlled quench tank covering water, oil, or polymer media at coarse KB scale.
  - Queue task: Clarify `quench_tank` as a small controlled tank with shell, agitation, lid/basket, sensors, and controls; document medium-specific assumptions at the process level.

- [ ] Decision ID: `quench_tank.split_medium_specific_variants`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split simple water, heated/agitated oil, and polymer quench tanks if heat-treatment realism requires it.
  - Queue task: Review heat-treatment processes and create or route to medium-specific quench resources where fire safety, agitation, temperature control, concentration, or cooling rate differ materially.

- [ ] Decision ID: `quench_tank.no_action`
  - Action type: `no_action`
  - Action: Leave `quench_tank` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `quench_tank.model_quenchant_inventory`
  - Action type: `consumable_or_tooling_modeling`, `process_requirement_update`
  - Action: Decide whether water, oil, polymer, or salt quenchant inventory is modeled as contained/consumed material.
  - Queue task: Add quenchant inventory, replenishment, contamination, and disposal assumptions if process accounting needs them.

- [ ] Decision ID: `quench_tank.add_fire_safety_ventilation`
  - Action type: `infrastructure_or_subsystem_modeling`, `note_cleanup`
  - Action: Add fire safety and ventilation for oil quench tasks.
  - Queue task: Add lid, overtemperature protection, ventilation/fire controls, safe tank arrangement, and ignition-risk notes for oil quenching.

- [ ] Decision ID: `quench_tank.add_agitation_temperature_control`
  - Action type: `bom_or_recipe_update`, `process_requirement_update`
  - Action: Add agitation/temperature control assumptions for water/polymer/oil uniformity.
  - Queue task: Update BOM/notes for pump/impeller agitation, heater/cooler if needed, temperature sensors, flow through load, and basket/elevator support.

- [ ] Decision ID: `quench_tank.review_capacity`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Check 200 kg tank capacity against largest heat-treated part or batch.
  - Queue task: Document volume/load capacity and audit heat-treatment processes for batch sizes beyond this small controlled tank.

- [ ] Decision ID: `quench_tank.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## reduction_furnace_v0

Source review: `research/machines/reduction_furnace_v0.md`

Current interpretation: Real compact controlled-atmosphere metal-oxide reduction furnace category. It should remain distinct from a generic high-temperature furnace because reductant delivery, atmosphere control, offgas handling, and reaction products matter.

### Primary Path - Choose One

- [ ] Decision ID: `reduction_furnace_v0.keep_compact_controlled_atmosphere_furnace`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep as a pilot-scale controlled-atmosphere reduction furnace.
  - Queue task: Update notes to narrow the description to "compact controlled-atmosphere reduction furnace" or "pilot-scale metal oxide reduction furnace" with refractory lining, reductant delivery, gas handling, offgas manifold, cooling, sensing, and controls.

- [ ] Decision ID: `reduction_furnace_v0.split_by_reduction_route`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split batch/tube oxide reduction, rotary/continuous regolith reduction, shaft furnace, and solar carbothermal reactor where process routes differ.
  - Queue task: Audit current reduction processes and route hydrogen/CO tube/batch reduction, granular ore/regolith continuous reduction, DRI shaft scale, and solar carbothermal regolith concepts to separate resources if needed.

- [ ] Decision ID: `reduction_furnace_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `reduction_furnace_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `reduction_furnace_v0.keep_distinct_from_furnace_high_temp`
  - Action type: `dedupe_or_consolidation`, `process_requirement_update`
  - Action: Keep separate from `furnace_high_temp` when chemistry requires controlled atmosphere and offgas/reductant systems.
  - Queue task: Audit high-temperature reduction references and ensure `furnace_high_temp` is not used alone where reductant, sealed gas handling, or offgas/product management is required.

- [ ] Decision ID: `reduction_furnace_v0.specify_primary_chemistry`
  - Action type: `research_or_design_followup`, `process_requirement_update`
  - Action: Specify whether primary self-reproduction route is hydrogen, CO, methane/carbothermal, direct carbon, vacuum, or silicon refining.
  - Queue task: Add process notes or design followup selecting primary reduction chemistry and corresponding gas/solid handling resources.

- [ ] Decision ID: `reduction_furnace_v0.add_gas_recycling_and_safety`
  - Action type: `infrastructure_or_subsystem_modeling`, `process_requirement_update`
  - Action: Add pressure, seals, feedthroughs, gas recycling, purge logic, relief, monitoring, and interlocks where needed.
  - Queue task: Update process/furnace requirements for gas-tight seals, valves, sensors, purge, pressure relief, combustible/toxic gas safety, and offgas treatment.

- [ ] Decision ID: `reduction_furnace_v0.model_liner_heater_wear`
  - Action type: `consumable_or_tooling_modeling`, `bom_or_recipe_update`
  - Action: Model high-wear refractory liners and heating elements as maintenance consumables where needed.
  - Queue task: Add liner/heater lifetime, replacement, and refractory compatibility assumptions.

- [ ] Decision ID: `reduction_furnace_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## refractory_installation_tools

Source review: `research/machines/refractory_installation_tools.md`

Current interpretation: Real specialized refractory lining toolkit/equipment bundle, not a single autonomous machine. Current 10 kg mass is plausible for hand tools, but not if it includes a real cement/refractory mixer.

### Primary Path - Choose One

- [ ] Decision ID: `refractory_installation_tools.keep_as_toolkit`
  - Action type: `consumable_or_tooling_modeling`, `note_cleanup`
  - Action: Rename or interpret as `refractory_installation_toolkit` or "refractory lining tool kit."
  - Queue task: Clarify this item as refractory trowels, brushes, cutters, forms, anchor installation tools, and small hand tools for lining installation, used with labor.

- [ ] Decision ID: `refractory_installation_tools.split_specialized_equipment`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split mixers, vibrators, rammers, gunning machines, and anchor/stud tools into separate resources where needed.
  - Queue task: Audit `refractory_lining_installation_v0` and `refractory_casting_v0`; add separate `refractory_gunning_machine`, `refractory_vibrator`, `refractory_rammer`, mixer, or anchor/stud equipment if installation method requires them.

- [ ] Decision ID: `refractory_installation_tools.no_action`
  - Action type: `no_action`
  - Action: Leave `refractory_installation_tools` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `refractory_installation_tools.remove_mixer_from_kit_mass`
  - Action type: `bom_or_recipe_update`, `process_requirement_update`
  - Action: Remove `cement_mixer_small` from the 10 kg kit mass or treat it as a separate required machine/resource.
  - Queue task: Reconcile BOM and mass accounting so the toolkit does not include a full mixer unless mass is updated accordingly.

- [ ] Decision ID: `refractory_installation_tools.require_labor`
  - Action type: `process_requirement_update`
  - Action: Keep `labor_bot_general_v0` or equivalent labor in refractory installation processes.
  - Queue task: Ensure refractory processes require labor plus tools; the toolkit does not install linings autonomously.

- [ ] Decision ID: `refractory_installation_tools.clarify_installation_method`
  - Action type: `process_requirement_update`, `note_cleanup`
  - Action: Clarify whether refractory work is hand casting/troweling, gunning, ramming, vibration, or module/anchor installation.
  - Queue task: Add process notes and resource requirements for selected installation method and dryout/quality constraints.

- [ ] Decision ID: `refractory_installation_tools.use_existing_welding_for_anchors`
  - Action type: `process_requirement_update`, `dedupe_or_consolidation`
  - Action: Decide whether anchor welding requires separate stud tools or existing welding equipment plus anchor kit.
  - Queue task: Audit anchor installation requirements and route to existing welding equipment where sufficient.

- [ ] Decision ID: `refractory_installation_tools.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## resource_3d_printer_cartesian_v0_machine

Source review: `research/machines/resource_3d_printer_cartesian_v0_machine.md`

Current interpretation: Real Cartesian FDM/FFF polymer 3D printer concept, with duplicate/naming issues and possible special embedded-SMA capability.

### Primary Path - Choose One

- [ ] Decision ID: `resource_3d_printer_cartesian_v0_machine.dedupe_to_canonical_basic_fdm`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Use one canonical basic FDM/FFF printer unless the `resource_` prefix has schema meaning.
  - Queue task: Compare `3d_printer_basic_v0`, `resource_3d_printer_basic_v0`, `resource_3d_printer_cartesian_v0_machine`, and related printer items; select one canonical basic Cartesian/FDM printer and migrate/alias duplicates.

- [ ] Decision ID: `resource_3d_printer_cartesian_v0_machine.keep_as_cartesian_sma_variant`
  - Action type: `note_cleanup`, `split_item`
  - Action: Reserve this item for a specific Cartesian printer with embedded SMA or other special toolheads.
  - Queue task: Document special toolheads/process controls for embedded SMA printing and keep standard polymer FDM on the canonical basic printer item.

- [ ] Decision ID: `resource_3d_printer_cartesian_v0_machine.no_action`
  - Action type: `no_action`
  - Action: Leave printer items unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `resource_3d_printer_cartesian_v0_machine.use_multi_material_printer_for_multi_material`
  - Action type: `process_requirement_update`, `reference_migration`
  - Action: Use `resource_3d_printer_multi_material_v0` for real multi-material deposition capability.
  - Queue task: Audit embedded SMA/multi-material processes and route them to a multi-material printer if wire embedding, multiple toolheads, or material switching is required.

- [ ] Decision ID: `resource_3d_printer_cartesian_v0_machine.replace_generic_drive_components`
  - Action type: `bom_or_recipe_update`
  - Action: Replace generic drive motors/gearboxes with stepper or servo motion components where appropriate.
  - Queue task: Update BOM to use realistic printer motion components such as stepper motors, drivers, belts/screws/rails, controller board, hot end, extruder, bed heater, sensors, and power supply.

- [ ] Decision ID: `resource_3d_printer_cartesian_v0_machine.clarify_printer_scale`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Clarify whether 120 kg represents desktop, large-format, enclosed industrial, ruggedized, or high-temperature printer scale.
  - Queue task: Document printer size/enclosure/material-temperature capability and adjust mass/BOM if needed.

- [ ] Decision ID: `resource_3d_printer_cartesian_v0_machine.preserve_open_source_buildability`
  - Action type: `note_cleanup`
  - Action: Preserve the concept as real and self-reproduction-relevant, not a placeholder.
  - Queue task: Add notes on RepRap/Prusa-style local buildability while preserving imported/advanced dependencies for precision rails/rods, motors, electronics, nozzles, heaters, and sensors.

- [ ] Decision ID: `resource_3d_printer_cartesian_v0_machine.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## rock_crusher_basic

Source review: `research/machines/rock_crusher_basic.md`

Current interpretation: Real canonical compact coarse crusher for regolith/ore/rock primary size reduction. Current BOM and recipe are most consistent with a small jaw crusher.

### Primary Path - Choose One

- [ ] Decision ID: `rock_crusher_basic.keep_canonical_small_jaw_crusher`
  - Action type: `note_cleanup`, `dedupe_or_consolidation`
  - Action: Keep as canonical coarse crusher and clarify as small jaw crusher if BOM remains jaw-crusher shaped.
  - Queue task: Update notes/display text to describe `rock_crusher_basic` as a compact/light jaw crusher for primary crushing, with jaw plates, frame, flywheel/shaft, bearings, motor/drive, hopper, and guards.

- [ ] Decision ID: `rock_crusher_basic.keep_broad_jaw_or_cone_abstraction`
  - Action type: `deferred_schema_or_modeling_decision`, `note_cleanup`
  - Action: Keep broad jaw-or-cone abstraction for coarse KB modeling.
  - Queue task: Document that this is a generic primary crusher placeholder and that component details are jaw-crusher shaped unless later specialized.

- [ ] Decision ID: `rock_crusher_basic.no_action`
  - Action type: `no_action`
  - Action: Leave `rock_crusher_basic` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `rock_crusher_basic.migrate_deprecated_refs`
  - Action type: `reference_migration`, `dedupe_or_consolidation`
  - Action: Migrate remaining `jaw_crusher_v0` and `crusher_basic` references into `rock_crusher_basic`.
  - Queue task: Search for deprecated crusher references and update/alias according to existing dedupe notes.

- [ ] Decision ID: `rock_crusher_basic.review_throughput_vs_mass`
  - Action type: `process_requirement_update`, `note_cleanup`
  - Action: Treat 500 kg as compact/light crusher capacity and review process throughput assumptions.
  - Queue task: Audit crushing processes and rates; add notes or larger variant only if throughput exceeds the compact crusher's plausible capacity beyond Conservative Mode reuse.

- [ ] Decision ID: `rock_crusher_basic.model_wear_parts`
  - Action type: `consumable_or_tooling_modeling`, `bom_or_recipe_update`
  - Action: Model wear-resistant jaw plates, liners, bearings, guards, and maintenance if needed.
  - Queue task: Add wear/lifetime assumptions for jaw plates/liners and preserve wear-resistant material requirements.

- [ ] Decision ID: `rock_crusher_basic.keep_grinding_separate`
  - Action type: `dedupe_or_consolidation`, `process_requirement_update`
  - Action: Keep crushing distinct from grinding/milling stages.
  - Queue task: Ensure processes use `ball_mill_v0` or other mills for grinding after primary crushing where particle size requires it.

- [ ] Decision ID: `rock_crusher_basic.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## rolling_mill_v0

Source review: `research/machines/rolling_mill_v0.md`

Current interpretation: Real rolling mill concept, but likely redundant with canonical `plate_rolling_mill` unless intentionally scoped as a smaller shop/lab rolling mill.

### Primary Path - Choose One

- [ ] Decision ID: `rolling_mill_v0.consolidate_to_plate_rolling_mill`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Use `plate_rolling_mill` as the canonical flat rolling/reduction resource.
  - Queue task: Migrate active process references from `rolling_mill_v0` to `plate_rolling_mill` where they mean flat rolling/reduction of ingots, billets, sheet, plate, strip, or bar; preserve existing dedupe notes.

- [ ] Decision ID: `rolling_mill_v0.keep_as_shop_lab_variant`
  - Action type: `note_cleanup`, `split_item`
  - Action: Keep only if explicitly defined as a smaller shop/lab rolling mill for limited stock sizes.
  - Queue task: Add notes distinguishing `rolling_mill_v0` from `plate_rolling_mill`, including roll width, roll force, hot/cold use, product thickness range, and intended process scope.

- [ ] Decision ID: `rolling_mill_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `rolling_mill_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `rolling_mill_v0.audit_precision_cold_rolling`
  - Action type: `process_requirement_update`
  - Action: Check whether any process needs 4-high/precision cold rolling rather than a generic 2-high mill.
  - Queue task: Review electrical steel, strip, and sheet processes for gauge-control requirements; add specific cold rolling or precision mill resources if needed.

- [ ] Decision ID: `rolling_mill_v0.review_electrical_steel_support`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Check whether electrical steel production needs annealing, pickling/descaling, insulation coating, and gauge-control equipment beyond rolling.
  - Queue task: Audit `electrical_steel_production_v0` and add non-rolling support steps/resources where required.

- [ ] Decision ID: `rolling_mill_v0.keep_roll_bending_distinct`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Do not confuse flat rolling/reduction with plate roll-bending machines for cylinders.
  - Queue task: Ensure process notes distinguish rolling to reduce thickness from rolling/bending plate into curved shells.

- [ ] Decision ID: `rolling_mill_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## sand_casting_flask_set

Source review: `research/machines/sand_casting_flask_set.md`

Current interpretation: Real reusable cope/drag foundry flask tooling for sand casting. It holds molding sand and aligns mold halves but is not a powered machine.

### Primary Path - Choose One

- [ ] Decision ID: `sand_casting_flask_set.keep_reusable_foundry_tooling`
  - Action type: `consumable_or_tooling_modeling`, `note_cleanup`
  - Action: Keep as reusable foundry tooling for sand casting.
  - Queue task: Rename or annotate as "Reusable cope/drag flask tooling for sand casting; not consumed by the process" and preserve use as a process resource where sand casting requires flasks.

- [ ] Decision ID: `sand_casting_flask_set.fold_into_casting_mold_set`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Bundle into `casting_mold_set` only if the KB deliberately treats all casting tooling as one coarse resource.
  - Queue task: Compare `sand_casting_flask_set` and `casting_mold_set`; bundle only if reusable flask versus part-specific mold/pattern distinction is intentionally out of scope.

- [ ] Decision ID: `sand_casting_flask_set.no_action`
  - Action type: `no_action`
  - Action: Leave `sand_casting_flask_set` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `sand_casting_flask_set.reclassify_as_tooling`
  - Action type: `consumable_or_tooling_modeling`
  - Action: Reclassify or document as tooling/part if schema support allows.
  - Queue task: Move or annotate `sand_casting_flask_set` as reusable tooling while preserving process-resource semantics.

- [ ] Decision ID: `sand_casting_flask_set.decompose_generic_casting_molds`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Decompose generic casting molds into reusable flask tooling plus part-specific molds/patterns where realism matters.
  - Queue task: Review `casting_mold_set` and casting recipes; preserve flasks as reusable tooling and add part-specific patterns/mold cavities where geometry matters.

- [ ] Decision ID: `sand_casting_flask_set.add_size_notes`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep one generic flask set under Conservative Mode but note casting size limits.
  - Queue task: Document whether 40 kg covers one medium steel flask or several sizes; add size notes to casting processes rather than creating size variants immediately.

- [ ] Decision ID: `sand_casting_flask_set.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## saw_or_cutting_tool

Source review: `research/machines/saw_or_cutting_tool.md`

Current interpretation: Real low-mass manual cutting tool, best interpreted as a hand hacksaw/manual metal-cutting saw with replaceable blades. Name is too broad for all cutting operations.

### Primary Path - Choose One

- [ ] Decision ID: `saw_or_cutting_tool.rename_as_hand_hacksaw`
  - Action type: `rename_or_alias`, `note_cleanup`
  - Action: Rename or annotate as "Hand hacksaw" or "Manual metal-cutting saw."
  - Queue task: Clarify that this 1 kg item is a manual saw/frame with replaceable blades, grip, and tensioning hardware for low-throughput manual cuts.

- [ ] Decision ID: `saw_or_cutting_tool.consolidate_into_cutting_tools_general`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Collapse into `cutting_tools_general` if separate saw availability is unnecessary.
  - Queue task: Compare direct process uses and BOM uses; migrate to `cutting_tools_general` if a broad manual cutting kit is the intended resource.

- [ ] Decision ID: `saw_or_cutting_tool.no_action`
  - Action type: `no_action`
  - Action: Leave `saw_or_cutting_tool` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `saw_or_cutting_tool.keep_heavy_cutting_distinct`
  - Action type: `process_requirement_update`, `dedupe_or_consolidation`
  - Action: Use `metal_shear_or_saw` for heavier shop cutting, thick stock, higher throughput, or better accuracy.
  - Queue task: Audit `cutting_basic_v0` and related processes to ensure thick plate, heavy stock, precision kerf, or production cuts are not assigned to a hand saw.

- [ ] Decision ID: `saw_or_cutting_tool.review_gasket_cutting`
  - Action type: `process_requirement_update`, `consumable_or_tooling_modeling`
  - Action: Check whether gasket sheet cutting needs utility knife, die cutter, punch, or blade item instead of a hacksaw.
  - Queue task: Audit gasket cutting processes and route to knife/die/punch tooling where material and cut geometry warrant it.

- [ ] Decision ID: `saw_or_cutting_tool.model_blade_consumables`
  - Action type: `consumable_or_tooling_modeling`
  - Action: Model replaceable saw blades/blade wear if needed.
  - Queue task: Add spare HSS/bi-metal blades and wear/replacement notes for manual cutting.

- [ ] Decision ID: `saw_or_cutting_tool.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## screening_equipment

Source review: `research/machines/screening_equipment.md`

Current interpretation: Real compact vibratory screen/sieve classifier for regolith, aggregate, and powder size fractions. It should not be reduced to labor plus a hand sieve for repeatable processing.

### Primary Path - Choose One

- [ ] Decision ID: `screening_equipment.keep_generic_compact_screener`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep as a generic compact vibratory screen/sieve classifier.
  - Queue task: Clarify `screening_equipment` as a compact vibratory screen/sieve classifier with screen decks/mesh, frame, vibration drive, hoppers/bins, and dust control for regolith, aggregate, and powder size fractions.

- [ ] Decision ID: `screening_equipment.split_powder_grade_sieving`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split fine powder/metal-powder sieving where inert atmosphere, contamination control, ultrasonic assist, or fine mesh matters.
  - Queue task: Route specialized powder processing to `metal_powder_sieving_system_v0` or another powder-grade subsystem if current generic screening is insufficient.

- [ ] Decision ID: `screening_equipment.no_action`
  - Action type: `no_action`
  - Action: Leave `screening_equipment` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `screening_equipment.review_scale`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Decide whether 56 kg represents a lab-scale sieve shaker or process-scale compact screener.
  - Queue task: Document scale, throughput, particle size range, deck area, number of decks, and collection fractions.

- [ ] Decision ID: `screening_equipment.model_screen_deck_wear`
  - Action type: `consumable_or_tooling_modeling`, `bom_or_recipe_update`
  - Action: Model screen decks/mesh as replaceable wear/blinding components if needed.
  - Queue task: Add replacement screen decks, mesh sizes, wear/blinding, cleaning, and maintenance assumptions.

- [ ] Decision ID: `screening_equipment.add_dust_collection_requirement`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Add dust collection/containment for regolith and fine powders where needed.
  - Queue task: Review screening/sieving processes and link to `dust_collection_system` or containment where dusty feedstock is processed.

- [ ] Decision ID: `screening_equipment.keep_distinct_from_gravity_separator`
  - Action type: `dedupe_or_consolidation`, `note_cleanup`
  - Action: Keep size separation distinct from density separation.
  - Queue task: Ensure process notes distinguish screening/sieving by particle size from gravity separation by density/specific gravity.

- [ ] Decision ID: `screening_equipment.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## sintering_furnace_v0

Source review: `research/machines/sintering_furnace_v0.md`

Current interpretation: Real sintering furnace category, but current KB state is inconsistent: item is deprecated into `furnace_basic` while many active processes still require it.

### Primary Path - Choose One

- [ ] Decision ID: `sintering_furnace_v0.finish_consolidation_to_generic_furnaces`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Replace references with `furnace_basic` or `furnace_high_temp` if current sintering processes can tolerate generic heat sources.
  - Queue task: Audit all `sintering_furnace_v0` process references; migrate to `furnace_basic` or `furnace_high_temp` where atmosphere/vacuum/clean-hot-zone requirements do not matter, and then preserve deprecation consistently.

- [ ] Decision ID: `sintering_furnace_v0.retain_controlled_atmosphere_sintering`
  - Action type: `rename_or_alias`, `process_requirement_update`, `bom_or_recipe_update`
  - Action: Retain as `controlled_atmosphere_sintering_furnace_v0` or `vacuum_sintering_furnace_v0`.
  - Queue task: Remove/deprecate-note conflict, rename/rescope as a compact batch controlled-atmosphere/vacuum-capable sintering furnace, and preserve it for ferrites, NdFeB, tungsten, ceramics, powder metallurgy, or clean hot-zone processes that need it.

- [ ] Decision ID: `sintering_furnace_v0.no_action`
  - Action type: `no_action`
  - Action: Leave deprecated-but-used state unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `sintering_furnace_v0.audit_material_specific_needs`
  - Action type: `process_requirement_update`
  - Action: Check whether ferrite, NdFeB, tungsten, alumina, porcelain, and regolith sintering can share one furnace.
  - Queue task: Review sintering recipes and record temperature, atmosphere, contamination, cycle, and fixture requirements by material.

- [ ] Decision ID: `sintering_furnace_v0.add_vacuum_gas_hardware`
  - Action type: `bom_or_recipe_update`, `infrastructure_or_subsystem_modeling`
  - Action: Add vacuum pump, retort/gas-tight chamber, process gas delivery, hydrogen/inert safety, and clean hot-zone details if retained.
  - Queue task: Update BOM/notes to include gas delivery, vacuum hardware, seals, safety interlocks, and compatible trays/setters/boats where needed.

- [ ] Decision ID: `sintering_furnace_v0.keep_hot_pressing_separate`
  - Action type: `process_requirement_update`, `dedupe_or_consolidation`
  - Action: Use `hot_press_v0` where pressure during heating is required.
  - Queue task: Audit `sintering_and_hot_pressing_v0` and related processes; route simultaneous pressure-and-heat consolidation to `hot_press_v0`.

- [ ] Decision ID: `sintering_furnace_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## solar_array_v0

Source review: `research/machines/solar_array_v0.md`

Current interpretation: Real installed PV power infrastructure/equipment, not a manufacturing machine. Current split of imported PV modules plus local mount/BOS is realistic.

### Primary Path - Choose One

- [ ] Decision ID: `solar_array_v0.keep_installed_pv_array_with_bos`
  - Action type: `note_cleanup`, `infrastructure_or_subsystem_modeling`
  - Action: Keep as a small installed PV array with balance-of-system components.
  - Queue task: Clarify `solar_array_v0` as installed PV infrastructure with imported PV modules, mounting/racking, wiring, power conditioning/control, sensors, fasteners, and balance-of-system assumptions.

- [ ] Decision ID: `solar_array_v0.split_modules_racking_power_conditioning`
  - Action type: `split_item`, `infrastructure_or_subsystem_modeling`
  - Action: Split into PV modules, racking/mount, power conditioning, wiring/protection, and installation if separate accounting matters.
  - Queue task: Route `pv_module_imported`, array mount structure, `power_conditioning_equipment`, bus/protection, and installation resources separately if needed.

- [ ] Decision ID: `solar_array_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `solar_array_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `solar_array_v0.preserve_pv_module_import`
  - Action type: `reference_migration`, `note_cleanup`
  - Action: Keep PV modules imported unless a serious photovoltaic manufacturing chain is added.
  - Queue task: Document that local work covers support structure, wiring, assembly, installation, and testing, while PV modules remain imported.

- [ ] Decision ID: `solar_array_v0.add_power_rating`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Add intended power rating for the 400 kg array.
  - Queue task: Estimate or document module count, wattage, voltage/current, array area, expected output, and solar conditions.

- [ ] Decision ID: `solar_array_v0.add_bos_protection_storage`
  - Action type: `infrastructure_or_subsystem_modeling`, `bom_or_recipe_update`
  - Action: Add combiner/disconnects, wiring, grounding, fuses/breakers, optional batteries/storage, and monitoring where needed.
  - Queue task: Update BOM/notes or linked resources for electrical BOS and storage assumptions.

- [ ] Decision ID: `solar_array_v0.add_lunar_environment_assumptions`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Add dust, degradation, cleaning, anchoring, insolation, angle, and day/night cycle assumptions for lunar/regolith-heavy use.
  - Queue task: Add operational reliability notes or resources such as cleaning brushes, dust mitigation, tracking/tilt, and storage sizing if lunar conditions are modeled.

- [ ] Decision ID: `solar_array_v0.keep_distinct_from_power_conditioning`
  - Action type: `dedupe_or_consolidation`
  - Action: Do not over-collapse PV generation with power conditioning.
  - Queue task: Preserve distinction between solar generation hardware and active conversion/regulation equipment.

- [ ] Decision ID: `solar_array_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## solar_tracking_optional

Source review: `research/machines/solar_tracking_optional.md`

Current interpretation: Real optional solar tracking infrastructure/equipment, best interpreted as a small PV array tracker unless concentrator tracking is explicitly needed.

### Primary Path - Choose One

- [ ] Decision ID: `solar_tracking_optional.keep_small_single_axis_tracker`
  - Action type: `note_cleanup`, `infrastructure_or_subsystem_modeling`
  - Action: Scope as a small single-axis PV tracker or optional mount upgrade.
  - Queue task: Rename or annotate as `solar_tracker_single_axis_small`; preserve optional role in `solar_power_generation_basic_v0` and document structure, pivot/bearings, actuator/drive, controller, sensors, stow behavior, and maintenance.

- [ ] Decision ID: `solar_tracking_optional.split_pv_and_concentrator_tracking`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split PV tracking from dual-axis concentrator/heliostat tracking if both are needed.
  - Queue task: Route PV panel pointing, thermal concentrator tracking, and heliostat aiming to distinct resources if precision, structure, control, or maintenance differs.

- [ ] Decision ID: `solar_tracking_optional.bundle_into_solar_array`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Bundle tracker into `solar_array_v0` only if optional yield upgrades are not modeled separately.
  - Queue task: Decide whether simulator benefits from separate optional tracker resource; if not, fold into array mount/BOS notes while retaining fixed-tilt as lower-complexity path.

- [ ] Decision ID: `solar_tracking_optional.no_action`
  - Action type: `no_action`
  - Action: Leave `solar_tracking_optional` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `solar_tracking_optional.add_operational_assumptions`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Add stow position, dust/abrasion tolerance, lubrication/bearing life, actuator sealing, and maintenance access.
  - Queue task: Update notes/process assumptions for reliability in terrestrial/lunar outdoor environments.

- [ ] Decision ID: `solar_tracking_optional.review_lunar_tracking_economics`
  - Action type: `research_or_design_followup`, `process_requirement_update`
  - Action: Check whether lunar setting favors active tracking, fixed mounts, or seasonally adjustable mounts.
  - Queue task: Review lunar day/night cycle, polar illumination, dust, maintenance, and power-yield assumptions before relying on active tracking.

- [ ] Decision ID: `solar_tracking_optional.verify_generation_bonus`
  - Action type: `deferred_schema_or_modeling_decision`
  - Action: Confirm whether simulation applies a generation bonus for including this optional tracker.
  - Queue task: If no simulation effect exists, add a modeling task or note so the optional tracker has clear value or can be omitted.

- [ ] Decision ID: `solar_tracking_optional.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## soldering_station

Source review: `research/machines/soldering_station.md`

Current interpretation: Real reusable temperature-controlled hand soldering bench station for wiring, through-hole work, PCB touch-up, sensor wiring, and low-volume electronics assembly.

### Primary Path - Choose One

- [ ] Decision ID: `soldering_station.keep_hand_soldering_station`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep as a temperature-controlled hand soldering station, distinct from full PCB production equipment.
  - Queue task: Clarify `soldering_station` as base controller, heating handpiece, tips, stand, temperature feedback, ESD-safe setup, and accessories for low-volume electronics and wiring work.

- [ ] Decision ID: `soldering_station.bundle_into_electronics_tool_station`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Bundle into broader circuit board tools or electronics assembly station if separate capacity is unnecessary.
  - Queue task: Compare `soldering_station`, `circuit_board_tools`, `hand_tools_electrical`, and electronics test/assembly stations; consolidate or preserve scope boundaries.

- [ ] Decision ID: `soldering_station.no_action`
  - Action type: `no_action`
  - Action: Leave `soldering_station` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `soldering_station.keep_reflow_wave_distinct`
  - Action type: `process_requirement_update`, `dedupe_or_consolidation`
  - Action: Keep hand soldering distinct from reflow ovens, wave soldering, pick-and-place, and production PCB assembly.
  - Queue task: Audit SMT and production-board processes and require solder paste/reflow or wave soldering equipment where hand soldering is insufficient.

- [ ] Decision ID: `soldering_station.add_rework_variant`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Add hot-air rework/desoldering station separately if SMT rework, QFP/BGA work, or desoldering requires it.
  - Queue task: Decide whether hot-air/rework/desoldering is included in this item or represented by a separate rework station.

- [ ] Decision ID: `soldering_station.model_consumables_fumes`
  - Action type: `consumable_or_tooling_modeling`, `infrastructure_or_subsystem_modeling`
  - Action: Model solder tips, solder wire/paste, flux, cleaning supplies, and fume extraction if needed.
  - Queue task: Add consumables and fume extraction/ventilation requirements for soldering processes.

- [ ] Decision ID: `soldering_station.review_mass`
  - Action type: `note_cleanup`
  - Action: Decide whether 8 kg represents compact station only or station plus rugged bench/accessories.
  - Queue task: Update mass notes if necessary.

- [ ] Decision ID: `soldering_station.require_labor_plus_station`
  - Action type: `process_requirement_update`
  - Action: Pair with `labor_bot_general_v0` or electronics assembly labor; station only provides controlled heat.
  - Queue task: Ensure soldering processes model manipulation/inspection labor separately from the soldering station.

- [ ] Decision ID: `soldering_station.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## spinning_machine_v0

Source review: `research/machines/spinning_machine_v0.md`

Current interpretation: Real textile/fiber/yarn spinning machine, but KB usage is overloaded with metal spinning. Metal spinning needs a separate lathe-like forming machine.

### Primary Path - Choose One

- [ ] Decision ID: `spinning_machine_v0.split_textile_and_metal_spinning`
  - Action type: `split_item`, `process_requirement_update`, `reference_migration`
  - Action: Keep `spinning_machine_v0` for textile/fiber/yarn spinning and add/reuse a separate metal spinning machine.
  - Queue task: Create or route metal spinning to `metal_spinning_lathe_v0`, `cnc_metal_spinning_machine_v0`, or another forming-lathe resource; update `metal_spinning_process_v0` and tank-shell recipes away from textile `spinning_machine_v0`.

- [ ] Decision ID: `spinning_machine_v0.keep_overloaded_temporarily`
  - Action type: `deferred_schema_or_modeling_decision`, `note_cleanup`
  - Action: Keep current overloaded ID temporarily but document the semantic conflict.
  - Queue task: Add warning notes that textile spinning and metal spinning are different machine classes and should be separated later.

- [ ] Decision ID: `spinning_machine_v0.no_action`
  - Action type: `no_action`
  - Action: Leave overloaded usage unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `spinning_machine_v0.audit_tank_shell_scale`
  - Action type: `process_requirement_update`, `research_or_design_followup`
  - Action: Check whether tank shells are small enough for a general lathe with spinning tooling or require a dedicated large metal spinning machine.
  - Queue task: Review tank shell recipes and determine required diameter, material thickness, force, mandrel size, tailstock/pressure support, and roller tooling.

- [ ] Decision ID: `spinning_machine_v0.consider_existing_machine_tool_reuse`
  - Action type: `dedupe_or_consolidation`, `process_requirement_update`
  - Action: Reuse `precision_lathe`, `milling_machine_general_v0`, or `steel_forming_press` only if notes/tooling make metal-spinning capability explicit.
  - Queue task: Avoid new machine creation if an existing lathe/forming resource can plausibly support the metal spinning process with mandrels, rollers, and tooling.

- [ ] Decision ID: `spinning_machine_v0.decompose_textile_process_later`
  - Action type: `deferred_schema_or_modeling_decision`
  - Action: Consider later textile decomposition into spinning, weaving/knitting, and tension-control machines if fabric production becomes important.
  - Queue task: Add a future modeling note for textile manufacturing decomposition only if needed.

- [ ] Decision ID: `spinning_machine_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## stamping_press_basic

Source review: `research/machines/stamping_press_basic.md`

Current interpretation: Real low-end stamping press for repetitive die-based blanking/punching/forming of sheet metal. Distinct from generic hydraulic pressing because stamping requires die alignment and repeatable stroke behavior.

### Primary Path - Choose One

- [ ] Decision ID: `stamping_press_basic.keep_generic_basic_stamping_press`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep as a generic basic stamping capability while abstracting drive type/tonnage.
  - Queue task: Clarify `stamping_press_basic` as a low-end hydraulic/mechanical stamping press for sheet blanking/punching/forming, not a complete high-speed motor lamination line.

- [ ] Decision ID: `stamping_press_basic.rename_as_c_frame_hydraulic_press`
  - Action type: `rename_or_alias`, `bom_or_recipe_update`
  - Action: Rename/rescope as `c_frame_stamping_press_basic` or `hydraulic_stamping_press_basic` if current welded-frame hydraulic recipe is intended.
  - Queue task: Align name, BOM, and recipe around the specific C-frame/hydraulic low-speed press architecture.

- [ ] Decision ID: `stamping_press_basic.split_motor_lamination_line`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Add specialized motor lamination press line if production lamination throughput/quality is intended.
  - Queue task: Create or route motor-core lamination production to `motor_lamination_press_line` or equivalent if feeder, high-tonnage press, stacker, and scrap handling are required.

- [ ] Decision ID: `stamping_press_basic.no_action`
  - Action type: `no_action`
  - Action: Leave `stamping_press_basic` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `stamping_press_basic.keep_distinct_from_hydraulic_press`
  - Action type: `dedupe_or_consolidation`, `process_requirement_update`
  - Action: Do not merge into `hydraulic_press` if die alignment/repeatable stroke matters.
  - Queue task: Preserve stamping-specific requirements where processes need blanking/punching dies, guidance, guarding, and repeatability.

- [ ] Decision ID: `stamping_press_basic.add_lamination_die_tooling`
  - Action type: `consumable_or_tooling_modeling`, `process_requirement_update`
  - Action: Add `lamination_stamping_die_set`, die fabrication/import, and wear assumptions where laminations matter.
  - Queue task: Audit `lamination_stamping_v0` and `iron_core_lamination_basic_v0`; add die tooling, die alignment, sharpening/wear, and import/local fabrication decisions.

- [ ] Decision ID: `stamping_press_basic.add_feeder_stacker_scrap`
  - Action type: `infrastructure_or_subsystem_modeling`, `process_requirement_update`
  - Action: Add sheet feeder, stacker, and scrap handling for production rates such as 20 kg/hr if labor loading is insufficient.
  - Queue task: Determine whether lamination processes use labor loading or automated feeding/stacking; update requirements accordingly.

- [ ] Decision ID: `stamping_press_basic.add_capacity_specs`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Document press tonnage, stroke, bed size, sheet thickness, lamination size, and rate assumptions.
  - Queue task: Update item/process notes so 1000 kg basic press is not overused as a production line.

- [ ] Decision ID: `stamping_press_basic.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## steel_forming_press

Source review: `research/machines/steel_forming_press.md`

Current interpretation: Real generic hydraulic metal-forming press for low-volume steel sheet/shell forming. It is plausible, but overlaps with `hydraulic_press`, `press_brake`, and `stamping_press_basic` depending on actual operation.

### Primary Path - Choose One

- [ ] Decision ID: `steel_forming_press.keep_generic_hydraulic_metal_forming_press`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep as a generic hydraulic metal-forming press for current coarse steel shell/sheet forming.
  - Queue task: Rename or annotate as `hydraulic_metal_forming_press`; document that it is for low-volume bending/forming/stamping of steel sheet and shell parts, not a specific commercial model.

- [ ] Decision ID: `steel_forming_press.consolidate_to_hydraulic_press`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Consolidate with `hydraulic_press` if current operations are generic pressing/straightening/simple forming.
  - Queue task: Review steel forming processes and migrate to `hydraulic_press` plus tooling if a steel-specific forming press does not add process capability.

- [ ] Decision ID: `steel_forming_press.route_to_specific_forming_machines`
  - Action type: `reference_migration`, `process_requirement_update`
  - Action: Route straight bends, high-rate stamping, deep drawing, or hot forging to specific machines.
  - Queue task: Audit steel shell and sheet-forming processes; use `press_brake` for straight bends, `stamping_press_basic` for repetitive die stamping, future `deep_draw_press` for deep drawing, and `forging_press_v0` for hot forging.

- [ ] Decision ID: `steel_forming_press.no_action`
  - Action type: `no_action`
  - Action: Leave `steel_forming_press` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `steel_forming_press.add_operation_notes`
  - Action type: `process_requirement_update`, `note_cleanup`
  - Action: Clarify whether current operations are press-brake bending, stamping, deep drawing, straightening, or general shop pressing.
  - Queue task: Add operation-specific notes and tooling requirements for each process.

- [ ] Decision ID: `steel_forming_press.add_capacity_specs`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Add capacity assumptions for 3 mm steel sheet/shell work.
  - Queue task: Document tonnage, bed/platen size, stroke, tooling, shell dimensions, and whether 670 kg is sufficient for current parts.

- [ ] Decision ID: `steel_forming_press.fix_resource_qty_units`
  - Action type: `process_requirement_update`
  - Action: Review inconsistent `resource_requirements` units using both `count` and `unit`.
  - Queue task: Inspect `steel_shell_thick_forming_v0`, `sheet_metal_forming_process_v0`, and `electrolysis_cell_unit_shell_fabrication_v0`; normalize resource requirement units if inconsistent with schema.

- [ ] Decision ID: `steel_forming_press.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## surface_grinder

Source review: `research/machines/surface_grinder.md`

Current interpretation: Real precision flat-surface grinding machine, plausibly 950 kg. It should remain distinct from cylindrical, bearing, ball, bench, and polishing/lapping equipment.

### Primary Path - Choose One

- [ ] Decision ID: `surface_grinder.keep_default_flat_surface_grinder`
  - Action type: `note_cleanup`, `dedupe_or_consolidation`
  - Action: Preserve as the default flat-surface precision grinder.
  - Queue task: Clarify `surface_grinder` as the machine for precision flat grinding with abrasive wheel, table motion, magnetic chuck/workholding, coolant, spindle, and alignment.

- [ ] Decision ID: `surface_grinder.split_manual_hydraulic_cnc_variants`
  - Action type: `split_item`, `deferred_schema_or_modeling_decision`
  - Action: Split only if manual, hydraulic automatic, and CNC grinder distinctions matter.
  - Queue task: Decide whether imported compute/control should be optional for a manual variant and whether automatic/CNC capability is required by current processes.

- [ ] Decision ID: `surface_grinder.no_action`
  - Action type: `no_action`
  - Action: Leave `surface_grinder` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `surface_grinder.keep_wheels_separate`
  - Action type: `consumable_or_tooling_modeling`, `process_requirement_update`
  - Action: Keep `grinding_wheels` as required consumable/tooling.
  - Queue task: Ensure grinding processes require appropriate wheels, dressing/truing, and replacement assumptions separately from the grinder.

- [ ] Decision ID: `surface_grinder.route_nonflat_grinding`
  - Action type: `process_requirement_update`, `reference_migration`
  - Action: Use cylindrical/bearing/ball/internal grinders where geometry matters.
  - Queue task: Audit processes involving shafts, bearing races, balls, rolls, or internal/external diameters; route to appropriate geometry-specific grinders if needed.

- [ ] Decision ID: `surface_grinder.add_dresser_coolant_sludge_metrology`
  - Action type: `bom_or_recipe_update`, `process_requirement_update`
  - Action: Add wheel dresser, guards, coolant filtration, sludge/dust handling, and metrology dependencies.
  - Queue task: Update BOM/notes and process requirements for dressing, guarding, coolant/sludge, wheel balance, magnetic chuck maintenance, and precision metrology.

- [ ] Decision ID: `surface_grinder.review_polishing_processes`
  - Action type: `process_requirement_update`
  - Action: Check whether `mirror_polishing_v0` and finish processes need lapping/polishing after grinding.
  - Queue task: Audit polishing and mirror-finishing processes and add lapping/polishing equipment if surface grinding is insufficient.

- [ ] Decision ID: `surface_grinder.mark_local_build_as_advanced`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Treat local manufacture as advanced precision machine-tool reproduction.
  - Queue task: Add notes on stable base, precision ways, low-runout spindle, bearings, feeds, magnetic chuck, scraping/alignment, and metrology requirements.

- [ ] Decision ID: `surface_grinder.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## surface_treatment_station

Source review: `research/machines/surface_treatment_station.md`

Current interpretation: Real compact wet-chemical surface-treatment station for cleaning, etching, pickling, passivation, anodizing, and coating preparation.

### Primary Path - Choose One

- [ ] Decision ID: `surface_treatment_station.keep_generic_wet_process_station`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep as generic wet-chemical surface-treatment station.
  - Queue task: Define scope as wet chemical cleaning, etching, pickling, passivation, anodizing support, and coating preparation with chemical tanks, agitation, ventilation, circulation, controls, frame, and part racks/fixtures.

- [ ] Decision ID: `surface_treatment_station.split_process_specific_lines`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split anodizing, plating/electropolishing, passivation/pickling, and cleaning lines if process-specific requirements matter.
  - Queue task: Create or route to process-specific wet lines where rectifiers, electrodes, bath chemistry, temperature control, fumes, or wastewater differ materially.

- [ ] Decision ID: `surface_treatment_station.no_action`
  - Action type: `no_action`
  - Action: Leave `surface_treatment_station` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `surface_treatment_station.keep_coatings_distinct`
  - Action type: `process_requirement_update`, `dedupe_or_consolidation`
  - Action: Avoid using this item for paint, epoxy, powder coating, spray coating, drying/curing, or photoresist spin coating.
  - Queue task: Audit `surface_treatment_basic_v0` and related processes; route coating application to `coating_station`, drying/curing to oven resources, and photoresist spin coating to `spin_coating_station_v0`.

- [ ] Decision ID: `surface_treatment_station.add_anodizing_rectifier`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Add DC rectifier, electrodes, bus bars, contacts, and process chemistry for anodizing/plating.
  - Queue task: Review `surface_treatment_anodizing_v0`; require explicit electrical and chemistry components or create an `anodizing_line` variant.

- [ ] Decision ID: `surface_treatment_station.add_waste_ventilation_containment`
  - Action type: `infrastructure_or_subsystem_modeling`, `process_requirement_update`
  - Action: Add acid waste neutralization, wastewater treatment, fume extraction, secondary containment, and rinse management.
  - Queue task: Add or link waste/ventilation/containment resources for acid/metal-bearing effluent and fuming chemistries.

- [ ] Decision ID: `surface_treatment_station.review_mass_and_throughput`
  - Action type: `note_cleanup`
  - Action: Keep 300 kg as compact manual multi-tank station; model larger automated lines separately.
  - Queue task: Document station size, tank count, manual/automated operation, and throughput limits.

- [ ] Decision ID: `surface_treatment_station.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## temperature_sensing

Source review: `research/machines/temperature_sensing.md`

Current interpretation: Real instrumentation category, but deprecated generic bundle. It should not remain in imported-machine lists as a machine once references migrate to specific sensor/controller items.

### Primary Path - Choose One

- [ ] Decision ID: `temperature_sensing.finish_migration_to_specific_sensors`
  - Action type: `reference_migration`, `dedupe_or_consolidation`
  - Action: Remove from active/imported machine usage after migration to specific sensor assemblies.
  - Queue task: Search for live `temperature_sensing` references; replace with `thermocouple_contact_temperature_sensor_v0`, `rtd_contact_temperature_sensor_v0`, `optical_pyrometer_temperature_sensor_v0`, and/or `temperature_controller_module` as appropriate.

- [ ] Decision ID: `temperature_sensing.keep_deprecated_alias`
  - Action type: `deferred_schema_or_modeling_decision`, `note_cleanup`
  - Action: Preserve only as a deprecated migration alias for backward compatibility.
  - Queue task: Ensure deprecated status and replacement mapping are explicit and that queue/indexer behavior treats it as superseded.

- [ ] Decision ID: `temperature_sensing.no_action`
  - Action type: `no_action`
  - Action: Leave deprecated generic bundle unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `temperature_sensing.apply_sensor_selection_rules`
  - Action type: `process_requirement_update`
  - Action: Use thermocouples for ordinary high-temperature contact feedback, RTDs for low/medium precision monitoring, and pyrometers for molten/inaccessible/very high-temperature targets.
  - Queue task: Audit furnace, hot press, reactor, drying, chiller, and molten-material processes and assign appropriate sensor types plus controller/DAQ requirements.

- [ ] Decision ID: `temperature_sensing.keep_controller_separate`
  - Action type: `dedupe_or_consolidation`, `process_requirement_update`
  - Action: Keep `temperature_controller_module` separate from probe/sensor technology.
  - Queue task: Ensure processes requiring closed-loop control include controller electronics as distinct from thermocouple/RTD/pyrometer probes.

- [ ] Decision ID: `temperature_sensing.preserve_import_boundary_for_pyrometers_rtds`
  - Action type: `reference_migration`, `note_cleanup`
  - Action: Keep pyrometers and high-quality RTDs as imports unless precision optics/detectors/calibration or RTD fabrication chains exist.
  - Queue task: Add notes or import assumptions for optical pyrometers, precision RTDs, and calibration references.

- [ ] Decision ID: `temperature_sensing.review_temperature_modeling_depth`
  - Action type: `deferred_schema_or_modeling_decision`
  - Action: Decide whether simulation distinguishes measured process temperature, heater feedback, shell/guard temperature, and DAQ-only measurement.
  - Queue task: Add modeling followup if temperature sensing/control granularity needs improvement.

- [ ] Decision ID: `temperature_sensing.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## tension_control_system

Source review: `research/machines/tension_control_system.md`

Current interpretation: Real fiber/wire/web tension-control subsystem using sensing, controller, and brake/drive actuator feedback. It should not be replaced by labor during production.

### Primary Path - Choose One

- [ ] Decision ID: `tension_control_system.keep_generic_subsystem`
  - Action type: `note_cleanup`, `infrastructure_or_subsystem_modeling`
  - Action: Keep as a generic compact tension-control subsystem for fiber/wire/web handling.
  - Queue task: Rename or annotate as `tension_control_subsystem`; document sensing, controller, brake/drive actuator, dancer/idler mechanics, calibration, and use in fiber drawing/winding.

- [ ] Decision ID: `tension_control_system.decompose_components`
  - Action type: `split_item`, `bom_or_recipe_update`
  - Action: Decompose into load cell/tension sensor, controller, brake/drive actuator, and dancer/idler components if needed.
  - Queue task: Split or explicitly model `tension_sensor_or_load_cell`, `tension_controller`, `brake_or_drive_actuator`, and `dancer_arm_or_idler` where component-level closure matters.

- [ ] Decision ID: `tension_control_system.bundle_into_fiber_drawing_tower`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Treat as an internal subsystem of `fiber_drawing_tower` only if separate process capacity is unnecessary.
  - Queue task: Decide whether `fiber_drawing_basic_v0` should require a separate tension-control resource or rely on the draw tower BOM; update references accordingly.

- [ ] Decision ID: `tension_control_system.no_action`
  - Action type: `no_action`
  - Action: Leave `tension_control_system` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `tension_control_system.preserve_active_feedback_requirement`
  - Action type: `process_requirement_update`
  - Action: Do not replace with labor bot alone because fiber drawing/winding needs continuous feedback and actuator response.
  - Queue task: Ensure fiber/wire/winding processes keep active tension-control equipment; labor may install, calibrate, load, and inspect only.

- [ ] Decision ID: `tension_control_system.add_tension_range`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Add tension range, speed, fiber/web size, and accuracy assumptions.
  - Queue task: Document whether 25 kg subsystem is appropriate for current fiber drawing/winding loads and whether size variants are needed.

- [ ] Decision ID: `tension_control_system.align_recipe_bom_terms`
  - Action type: `bom_or_recipe_update`
  - Action: Align recipe component names with BOM concepts.
  - Queue task: Review recipe/BOM for duplicate or inconsistent control-board/sensor/brake/actuator terms and normalize.

- [ ] Decision ID: `tension_control_system.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## tension_gauge

Source review: `research/machines/tension_gauge.md`

Current interpretation: Real portable or fixture-mounted measurement instrument for belt, cable, wire, or fiber tension. It measures tension; it does not actively regulate it.

### Primary Path - Choose One

- [ ] Decision ID: `tension_gauge.keep_generic_measurement_tool`
  - Action type: `consumable_or_tooling_modeling`, `note_cleanup`
  - Action: Keep as one generic tension measurement tool at coarse modeling precision.
  - Queue task: Clarify `tension_gauge` as a portable measurement/calibration instrument for setup and verification, distinct from `tension_control_system`.

- [ ] Decision ID: `tension_gauge.split_by_measurement_type`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split into `belt_tension_meter`, `wire_tension_meter`, and `cable_tension_meter` only where tension ranges or methods are incompatible.
  - Queue task: Audit belt, wire, cable, and fiber processes and add specific tension instruments if required by range or measurement method.

- [ ] Decision ID: `tension_gauge.bundle_into_assembly_tools`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Bundle into `assembly_tools_basic` or maintenance toolkit if separate process resource is unnecessary.
  - Queue task: Review `belt_installation_and_tensioning_v0`; decide whether a standalone tension gauge is needed or should be included in a broader setup/tool kit.

- [ ] Decision ID: `tension_gauge.no_action`
  - Action type: `no_action`
  - Action: Leave `tension_gauge` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `tension_gauge.reclassify_as_instrument`
  - Action type: `consumable_or_tooling_modeling`
  - Action: Reclassify or document as tool/instrument rather than machine.
  - Queue task: Resolve or document `kind: machine` for `kb/items/parts/tension_gauge.yaml` while preserving resource semantics.

- [ ] Decision ID: `tension_gauge.keep_as_tension_control_component`
  - Action type: `bom_or_recipe_update`, `dedupe_or_consolidation`
  - Action: Keep as a component of `tension_control_system` where continuous feedback is needed.
  - Queue task: Preserve distinction between portable gauge and active controller; use gauge/load-cell sensing inside the control system where appropriate.

- [ ] Decision ID: `tension_gauge.add_range_calibration`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Add tension range and calibration/reference weight assumptions.
  - Queue task: Document expected tension range for belt drives versus wire/fiber handling and whether calibration weights or force references are required.

- [ ] Decision ID: `tension_gauge.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## test_bench_electrical

Source review: `research/machines/test_bench_electrical.md`

Current interpretation: Real electrical/electronics test workstation, but current KB scope is ambiguous between bench infrastructure and full canonical instrument suite.

### Primary Path - Choose One

- [ ] Decision ID: `test_bench_electrical.scope_as_bench_infrastructure`
  - Action type: `rename_or_alias`, `process_requirement_update`
  - Action: Treat as bench infrastructure while keeping instruments separately required.
  - Queue task: Rename or annotate as `electrical_test_bench_infrastructure`; keep process requirements for instruments such as `multimeter_set`, `power_supply_benchtop`, `oscilloscope_basic`, loads, and signal generators separate where needed.

- [ ] Decision ID: `test_bench_electrical.scope_as_full_test_capability`
  - Action type: `bom_or_recipe_update`, `dedupe_or_consolidation`
  - Action: Treat as canonical full electrical/electronics test capability that includes or references the core instruments.
  - Queue task: Update BOM/modeling to include or reference `multimeter_set`, `power_supply_benchtop`, `oscilloscope_basic`, test leads, electronic loads, signal generation, fixtures, and calibration references as appropriate.

- [ ] Decision ID: `test_bench_electrical.no_action`
  - Action type: `no_action`
  - Action: Leave current ambiguous scope unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `test_bench_electrical.preserve_simple_instruments`
  - Action type: `dedupe_or_consolidation`, `process_requirement_update`
  - Action: Keep simple instruments available separately for simple processes.
  - Queue task: Use `multimeter_set` and `power_supply_benchtop` directly for simple testing; reserve the full bench for integrated testing, burn-in, commissioning, and electronics workflows.

- [ ] Decision ID: `test_bench_electrical.add_safety_requirements`
  - Action type: `infrastructure_or_subsystem_modeling`, `note_cleanup`
  - Action: Add mains isolation, fusing/breakers, grounding, ESD control, high-voltage guarding, and load dissipation.
  - Queue task: Update notes/BOM/process requirements for electrical safety and thermal/load handling.

- [ ] Decision ID: `test_bench_electrical.split_by_voltage_power_domain`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split high-voltage, motor-load, and electronics signal benches if one bench is too broad.
  - Queue task: Audit burn-in, load testing, motor testing, wiring, and electronics signal tests and split by voltage/power domain only where needed.

- [ ] Decision ID: `test_bench_electrical.add_calibration_traceability`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Decide whether self-reproduction needs calibrated measurements or only functional pass/fail testing.
  - Queue task: Add calibration standards and traceability requirements if measurements drive acceptance criteria.

- [ ] Decision ID: `test_bench_electrical.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## tube_bender

Source review: `research/machines/tube_bender.md`

Current interpretation: Real light-industrial tube bending machine for controlled bends in tubing/piping, distinct from sheet-metal press-brake bending.

### Primary Path - Choose One

- [ ] Decision ID: `tube_bender.keep_distinct_tube_bending_machine`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep as a distinct tube bending machine with 200 kg light-industrial default.
  - Queue task: Clarify `tube_bender` as a tube/pipe bending machine for controlled bends in metal tube, with limits by OD, wall thickness, bend radius, material, bend angle, tooling, and repeatability.

- [ ] Decision ID: `tube_bender.split_by_bender_type`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split hand, benchtop, hydraulic, mandrel, and CNC tube benders only if scale/tolerance requires it.
  - Queue task: Audit tube processes and add variants where process scale, thin wall, tight radius, or repeatable multi-bend geometry exceeds the generic bender.

- [ ] Decision ID: `tube_bender.no_action`
  - Action type: `no_action`
  - Action: Leave `tube_bender` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `tube_bender.add_die_mandrel_tooling`
  - Action type: `consumable_or_tooling_modeling`, `process_requirement_update`
  - Action: Add tube bending die sets, mandrels, wiper dies, follower dies, clamps, and lubrication where bend quality matters.
  - Queue task: Update tube forming processes with tube-specific tooling requirements based on wall thickness and bend radius.

- [ ] Decision ID: `tube_bender.keep_sheet_bending_distinct`
  - Action type: `dedupe_or_consolidation`, `process_requirement_update`
  - Action: Keep separate from `press_brake` and sheet forming machines.
  - Queue task: Ensure tube bending and sheet/plate bending processes route to appropriate equipment.

- [ ] Decision ID: `tube_bender.add_cut_deburr_leak_test`
  - Action type: `process_requirement_update`, `consumable_or_tooling_modeling`
  - Action: Pair with cutting/deburring tools and leak testing for piping assemblies where needed.
  - Queue task: Audit piping/tube assembly processes and add `metal_shear_or_saw`, deburring tools, fittings, and pressure/leak test equipment as appropriate.

- [ ] Decision ID: `tube_bender.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## uv_exposure_unit

Source review: `research/machines/uv_exposure_unit.md`

Current interpretation: Real UV exposure station for simple PCB/photoresist photolithography. It is one PCB fab submodule, not full semiconductor lithography.

### Primary Path - Choose One

- [ ] Decision ID: `uv_exposure_unit.keep_pcb_photoresist_exposure`
  - Action type: `note_cleanup`, `process_requirement_update`
  - Action: Keep as controlled UV exposure equipment for simple PCB/photoresist work.
  - Queue task: Clarify `uv_exposure_unit` as UV lamp/LED exposure equipment with enclosure, timer/controller, mask-contact surface, shielding, and photoresist exposure role.

- [ ] Decision ID: `uv_exposure_unit.bundle_into_pcb_fab_equipment`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Treat as an internal component of `pcb_fab_equipment` where full PCB fabrication is abstracted.
  - Queue task: Decide whether processes should require `uv_exposure_unit` separately or rely on `pcb_fab_equipment` BOM; update references consistently.

- [ ] Decision ID: `uv_exposure_unit.no_action`
  - Action type: `no_action`
  - Action: Leave `uv_exposure_unit` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `uv_exposure_unit.add_alignment_vacuum_features`
  - Action type: `bom_or_recipe_update`, `process_requirement_update`
  - Action: Add mask/contact frame, registration, vacuum hold-down, double-sided alignment, timer, and intensity calibration where precision matters.
  - Queue task: Audit PCB photolithography process requirements and update BOM/notes for selected exposure accuracy.

- [ ] Decision ID: `uv_exposure_unit.review_mass_scale`
  - Action type: `note_cleanup`, `bom_or_recipe_update`
  - Action: Decide whether 100 kg is semi-industrial enclosed station or should be reduced for desktop/prototype exposure box.
  - Queue task: Document or adjust mass based on target PCB workflow and enclosure/vacuum/alignment features.

- [ ] Decision ID: `uv_exposure_unit.add_wavelength_resist_assumptions`
  - Action type: `process_requirement_update`, `note_cleanup`
  - Action: Add UV wavelength and photoresist type assumptions.
  - Queue task: Document assumed UV wavelength/intensity and compatible resist/dry-film/solder-mask process.

- [ ] Decision ID: `uv_exposure_unit.keep_semiconductor_lithography_distinct`
  - Action type: `process_requirement_update`, `dedupe_or_consolidation`
  - Action: Do not use this item to imply semiconductor-grade lithography.
  - Queue task: Add notes or process guards that this supports simple PCB photolithography only.

- [ ] Decision ID: `uv_exposure_unit.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## vacuum_pump_small

Source review: `research/machines/vacuum_pump_small.md`

Current interpretation: Real canonical small roughing/medium-vacuum pump. It should not imply clean high vacuum, ultra-high vacuum, high throughput, or corrosive gas compatibility without extra equipment.

### Primary Path - Choose One

- [ ] Decision ID: `vacuum_pump_small.keep_canonical_roughing_pump`
  - Action type: `note_cleanup`, `dedupe_or_consolidation`
  - Action: Keep as canonical small roughing/medium-vacuum pump.
  - Queue task: Clarify `vacuum_pump_small` as oil-sealed rotary-vane or equivalent small roughing/medium-vacuum pump, with 22.3 kg mass and boundaries around pressure, throughput, gas compatibility, and cleanliness.

- [ ] Decision ID: `vacuum_pump_small.split_by_pump_type`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split oil rotary vane, chemistry diaphragm, dry scroll, and turbomolecular-backed stations only where process needs differ.
  - Queue task: Audit vacuum processes and route chemistry/corrosive vapor, clean dry pumping, high-vacuum, and roughing applications to appropriate pump/station variants.

- [ ] Decision ID: `vacuum_pump_small.no_action`
  - Action type: `no_action`
  - Action: Leave `vacuum_pump_small` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `vacuum_pump_small.add_vacuum_level_requirements`
  - Action type: `process_requirement_update`, `note_cleanup`
  - Action: Make processes specify rough, medium, high, or ultra-high vacuum capability where relevant.
  - Queue task: Audit vacuum tube, furnace, glovebox, controlled atmosphere, and leak-test processes and document ultimate pressure/pump-down requirements.

- [ ] Decision ID: `vacuum_pump_small.require_high_vacuum_stage_where_needed`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Add high-vacuum pump stages, gauges, valves, traps/filters, and bakeout/cleaning where vacuum tube or clean furnace work needs them.
  - Queue task: Ensure high-vacuum applications do not rely on the small roughing pump alone.

- [ ] Decision ID: `vacuum_pump_small.keep_station_distinct`
  - Action type: `dedupe_or_consolidation`, `reference_migration`
  - Action: Keep separate from `vacuum_pump_station`, which should represent an integrated skid with gauges, valves, traps, controls, and chamber fittings.
  - Queue task: Review references to pump versus pump station and clarify component/station relationship.

- [ ] Decision ID: `vacuum_pump_small.model_capacity_pumpdown`
  - Action type: `deferred_schema_or_modeling_decision`, `process_requirement_update`
  - Action: Decide whether pump capacity should be modeled by chamber volume and pump-down time.
  - Queue task: Add future modeling note or process assumptions for pump speed, chamber size, and pump-down duration if needed.

- [ ] Decision ID: `vacuum_pump_small.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## vapor_capture_system_v0

Source review: `research/machines/vapor_capture_system_v0.md`

Current interpretation: Real vapor transport/cold-trap/condensation subsystem. It is plausible for lunar water extraction, but too generic for all volatile species without material and temperature constraints.

### Primary Path - Choose One

- [ ] Decision ID: `vapor_capture_system_v0.scope_as_water_cold_trap`
  - Action type: `rename_or_alias`, `note_cleanup`
  - Action: Scope as water vapor capture and cold-trap condensation system for thermal regolith extraction.
  - Queue task: Rename or annotate as "water vapor capture and cold-trap condensation system" with vapor transport, pressure control, cold trap, heat rejection, reservoir management, sensors, and dust handling.

- [ ] Decision ID: `vapor_capture_system_v0.keep_generic_vapor_capture`
  - Action type: `deferred_schema_or_modeling_decision`, `note_cleanup`
  - Action: Keep generic vapor capture only if process-specific compatibility is documented.
  - Queue task: Add notes that water, ammonia, HCl, magnesium vapor, phosphorus, and mixed volatiles have different condensation temperatures, corrosion constraints, filters, and capture chemistry.

- [ ] Decision ID: `vapor_capture_system_v0.split_by_volatile_class`
  - Action type: `split_item`, `process_requirement_update`
  - Action: Split water cold traps, ammonia recovery, acid gas capture, and metal-vapor condensers where requirements differ.
  - Queue task: Audit current uses and route to process-specific vapor capture/condensation/scrubber resources based on vapor species, temperature, pressure, and materials compatibility.

- [ ] Decision ID: `vapor_capture_system_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `vapor_capture_system_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `vapor_capture_system_v0.define_component_relationship`
  - Action type: `dedupe_or_consolidation`, `bom_or_recipe_update`
  - Action: Decide whether `vapor_condenser_cold_trap` and `cold_trap_module_v0` are components of this system or parallel machines.
  - Queue task: Normalize relationships among vapor capture system, condenser/cold trap, cold-trap module, cryogenic chiller, and vacuum pump.

- [ ] Decision ID: `vapor_capture_system_v0.add_dust_demister_filters`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Add filters/demisters to prevent dust transport into cold traps for polar regolith extraction.
  - Queue task: Update water extraction process requirements for dust control, vapor line protection, and cold-trap fouling prevention.

- [ ] Decision ID: `vapor_capture_system_v0.add_pressure_heat_rejection`
  - Action type: `process_requirement_update`, `infrastructure_or_subsystem_modeling`
  - Action: Add pressure control, heat rejection, coolant/cryogenic chilling, and reservoir/ice removal assumptions.
  - Queue task: Ensure vapor capture is modeled as active system, not passive condenser only.

- [ ] Decision ID: `vapor_capture_system_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## vibrating_screen_v0

Source review: `research/machines/vibrating_screen_v0.md`

Current interpretation: Real practical vibrating-deck screening machine for granular particle-size separation. The main decision is whether it should remain a concrete subtype alongside broader `screening_equipment` or be consolidated into that generic screening item.

### Primary Path - Choose One

- [ ] Decision ID: `vibrating_screen_v0.keep_distinct_vibrating_screen`
  - Action type: `kb_semantics`
  - Action: Keep `vibrating_screen_v0` as the concrete vibrating deck/screen machine and clarify `screening_equipment` as a broader screening kit/station category.
  - Queue task: Update `vibrating_screen_v0` and `screening_equipment` descriptions/usages so `vibrating_screen_v0` is the reusable vibrating-deck machine and `screening_equipment` is only used where the process does not require a specific screen subtype.

- [ ] Decision ID: `vibrating_screen_v0.consolidate_into_screening_equipment`
  - Action type: `kb_consolidation`
  - Action: Treat `screening_equipment` as the canonical vibrating screen and migrate references from `vibrating_screen_v0` where appropriate.
  - Queue task: Review all references to `vibrating_screen_v0` and `screening_equipment`; consolidate onto the chosen canonical screening machine, preserving any subtype-specific BOM notes such as screen deck, vibration drive, springs, frame, and controls.

- [ ] Decision ID: `vibrating_screen_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `vibrating_screen_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `vibrating_screen_v0.add_screening_parameters`
  - Action type: `kb_detail`
  - Action: Add or verify screen parameters: mesh/cut size, deck area, throughput, number of decks, and expected particle-size fractions.
  - Queue task: Add notes or structured fields, using existing KB conventions, for mesh size/cut points, deck area, throughput, and product fractions for `vibrating_screen_v0` and processes that rely on it.

- [ ] Decision ID: `vibrating_screen_v0.add_lunar_dust_and_blinding_constraints`
  - Action type: `kb_detail`
  - Action: Capture regolith-specific risks including dust containment, screen blinding, wear, electrostatic effects, and vacuum-compatible bearings/actuation.
  - Queue task: Add KB notes or process constraints for `vibrating_screen_v0` covering lunar/regolith dust containment, screen blinding mitigation, abrasive wear, electrostatic behavior, and vacuum-compatible moving parts.

- [ ] Decision ID: `vibrating_screen_v0.review_alternative_classifiers`
  - Action type: `kb_option`
  - Action: Where a process does not specifically require vibrating screening, consider alternatives such as static screens, trommels, gyratory screens, or air classifiers.
  - Queue task: Review processes using `vibrating_screen_v0` or `screening_equipment`; keep the vibrating screen where required, and add alternate-machine notes for static, trommel, gyratory, or air-classifier separation where compatible.

- [ ] Decision ID: `vibrating_screen_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## vibratory_feeder_v0

Source review: `research/machines/vibratory_feeder_v0.md`

Current interpretation: Real practical bulk-material vibratory feeder for controlled metering of regolith or granular feedstock. The review recommends clarifying that this is a trough/pan feeder, not a small parts-orienting bowl feeder.

### Primary Path - Choose One

- [ ] Decision ID: `vibratory_feeder_v0.rename_or_annotate_bulk_material_feeder`
  - Action type: `kb_semantics`
  - Action: Keep the item and update name/description to "Bulk-material vibratory feeder" or "Vibratory trough feeder."
  - Queue task: Update `vibratory_feeder_v0` display text and description so it is clearly a bulk-material trough/pan feeder for metering granular regolith into downstream equipment, not a discrete-parts bowl feeder.

- [ ] Decision ID: `vibratory_feeder_v0.keep_current_name_add_notes`
  - Action type: `kb_detail`
  - Action: Keep the existing ID/name but add notes that resolve the interpretation ambiguity.
  - Queue task: Add clarifying notes to `vibratory_feeder_v0` and its referenced processes that the machine meters bulk granular feedstock into separators/sinterers and does not sort or orient individual parts.

- [ ] Decision ID: `vibratory_feeder_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `vibratory_feeder_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `vibratory_feeder_v0.keep_current_bom_structure`
  - Action type: `kb_validation`
  - Action: Preserve the BOM categories: trough, vibration motor set, welded support frame, controller/sensor package, power conditioning, and fasteners.
  - Queue task: Review `vibratory_feeder_v0` BOM and retain its existing subsystem structure unless validation requires schema-only cleanup.

- [ ] Decision ID: `vibratory_feeder_v0.add_throughput_scaling_notes`
  - Action type: `kb_detail`
  - Action: Add notes that feeder mass and motor power should scale with required kg/hr, trough dimensions, liner, and abrasion allowance.
  - Queue task: Add throughput/sizing notes to `vibratory_feeder_v0`, including target feed rate, trough size, motor/control scaling, and when a separate feeder size should be introduced under the 5x Conservative Mode rule.

- [ ] Decision ID: `vibratory_feeder_v0.add_lunar_wear_and_vacuum_constraints`
  - Action type: `kb_detail`
  - Action: Capture lunar dust abrasion, replaceable liners, sealed bearings, and vacuum-compatible motor/control packaging.
  - Queue task: Add KB notes or requirements for `vibratory_feeder_v0` covering abrasive regolith wear, replaceable liners, dust sealing, bearing protection, and vacuum-compatible actuation/control packaging.

- [ ] Decision ID: `vibratory_feeder_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## welding_consumables

Source review: `research/machines/welding_consumables.md`

Current interpretation: Real welding supply inventory. The issue is not literal machine-ness; it is whether the KB item should be modeled as reusable equipment/storage, consumable filler/material inventory, or split into process/material-specific consumables.

### Primary Path - Choose One

- [ ] Decision ID: `welding_consumables.reclassify_as_consumable_inventory`
  - Action type: `kb_reclassification`
  - Action: Model `welding_consumables` as consumable welding filler/material inventory that recipes draw down by mass or weld length.
  - Queue task: Reclassify or remodel `welding_consumables` so welding recipes consume it as filler/electrode/flux inventory rather than treating the whole 25 kg item as reusable equipment.

- [ ] Decision ID: `welding_consumables.keep_as_reusable_supply_kit`
  - Action type: `kb_semantics`
  - Action: Keep `welding_consumables` in the machine/tooling area as a reusable supply kit or managed inventory container, while separately modeling the consumable contents.
  - Queue task: Update `welding_consumables` to represent the reusable storage/management kit, and create or reference separate consumable materials for rods, wire, flux, electrodes, and gases as needed.

- [ ] Decision ID: `welding_consumables.split_by_process_and_material`
  - Action type: `kb_split`
  - Action: Replace the coarse inventory with specific consumables by welding process and base material.
  - Queue task: Split `welding_consumables` into process/material-compatible consumables such as steel stick electrodes, TIG filler rods, MIG wire, aluminum filler wire, stainless filler, tungsten electrodes, flux, and shielding gas where recipes require that specificity.

- [ ] Decision ID: `welding_consumables.no_action`
  - Action type: `no_action`
  - Action: Leave `welding_consumables` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `welding_consumables.remove_aluminum_as_generic_filler`
  - Action type: `kb_correction`
  - Action: Stop using aluminum wire as a generic filler placeholder except for aluminum-compatible welding.
  - Queue task: Review `welding_consumables` BOM and dependent recipes; remove or qualify aluminum wire as a generic filler substitute unless the weld is actually aluminum-compatible.

- [ ] Decision ID: `welding_consumables.add_storage_constraints`
  - Action type: `kb_detail`
  - Action: Add dry storage, rod oven, redrying, and moisture-control constraints for low-hydrogen electrodes or flux where weld quality matters.
  - Queue task: Add storage/handling requirements for welding consumables, especially low-hydrogen electrodes and fluxes, including moisture-proof storage or rod oven support where required.

- [ ] Decision ID: `welding_consumables.define_consumption_basis`
  - Action type: `kb_schema_detail`
  - Action: Decide whether weld recipes consume filler by deposited mass, weld length, joint type, or process-specific rule.
  - Queue task: Update welding recipe notes or inputs to consume filler/electrode inventory by an explicit basis such as deposited mass, weld length, or process-specific estimate.

- [ ] Decision ID: `welding_consumables.separate_shielding_gas`
  - Action type: `kb_split`
  - Action: Treat shielding gas as a separate material/resource rather than bundling it into all welding consumables.
  - Queue task: Review welding processes and create or reference separate shielding gas resources/materials where TIG/MIG processes require them, rather than hiding gas inside `welding_consumables`.

- [ ] Decision ID: `welding_consumables.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## welding_power_supply_v0

Source review: `research/machines/welding_power_supply_v0.md`

Current interpretation: Real arc-welding power source. The main decision is whether this item is a bare CC/CV electrical power source or a complete basic welding package with leads/torch/clamp, while keeping process-specific systems separate.

### Primary Path - Choose One

- [ ] Decision ID: `welding_power_supply_v0.define_as_general_cc_cv_power_source`
  - Action type: `kb_semantics`
  - Action: Define as a general CC/CV arc-welding power source for basic structural welding; auxiliary equipment must be separately required.
  - Queue task: Update `welding_power_supply_v0` description and process references so it provides controlled arc-welding electrical output only, and does not by itself imply shielding gas, wire feed, TIG torch, coolant, PPE, fixturing, or qualified weld procedures.

- [ ] Decision ID: `welding_power_supply_v0.define_as_basic_arc_welding_package`
  - Action type: `kb_semantics`
  - Action: Define as a compact basic arc-welding package including power source, leads, holder/torch, clamp, controls, and simple accessories.
  - Queue task: Update `welding_power_supply_v0` and its BOM to explicitly represent a basic arc-welding package, then ensure process-specific requirements such as gas, wire feed, coolant, TIG controls, and PPE remain separate where needed.

- [ ] Decision ID: `welding_power_supply_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `welding_power_supply_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `welding_power_supply_v0.add_output_specs`
  - Action type: `kb_detail`
  - Action: Add output current/voltage range, duty cycle, input power, CC/CV modes, and transformer-vs-inverter basis.
  - Queue task: Add practical welding power-source parameters to `welding_power_supply_v0`, including amperage/voltage range, duty cycle, input power requirements, CC/CV support, and whether the reference implementation is transformer/rectifier or inverter based.

- [ ] Decision ID: `welding_power_supply_v0.keep_tig_and_spot_separate`
  - Action type: `kb_boundary`
  - Action: Keep complete TIG/GTAW systems and resistance spot welders as separate items with different requirements.
  - Queue task: Review welding process requirements and preserve separate machine requirements for `welding_tig_unit_v0` and any spot-welding equipment where gas handling, high-frequency start, coolant, precision controls, or resistance-welding mechanics are required.

- [ ] Decision ID: `welding_power_supply_v0.review_local_manufacturability`
  - Action type: `kb_manufacturing_note`
  - Action: Note that rugged transformer/rectifier units are more locally buildable than high-performance inverter welders if advanced electronics are scarce.
  - Queue task: Add manufacturability notes to `welding_power_supply_v0` distinguishing locally plausible transformer/rectifier construction from imported or higher-dependency inverter power electronics.

- [ ] Decision ID: `welding_power_supply_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## welding_tig_unit_v0

Source review: `research/machines/welding_tig_unit_v0.md`

Current interpretation: Real complete TIG/GTAW welding station for precision, clean, leak-tight welds. It should remain distinct from general welding power supplies, generic welding tools, and consumable filler inventory.

### Primary Path - Choose One

- [ ] Decision ID: `welding_tig_unit_v0.define_as_complete_tig_station`
  - Action type: `kb_semantics`
  - Action: Keep and describe as a complete TIG/GTAW welding station with power source, torch, shielding gas handling, controls, and optional cooler.
  - Queue task: Update `welding_tig_unit_v0` display text/description to make it a complete TIG/GTAW station for precision welding, while leaving generic `welding_power_supply_v0`, `welding_tools_set`, and `welding_consumables` as separate supporting items.

- [ ] Decision ID: `welding_tig_unit_v0.reduce_to_tig_addon_package`
  - Action type: `kb_boundary`
  - Action: Treat the item as TIG-specific torch/gas/control/cooling additions that depend on a separate `welding_power_supply_v0`.
  - Queue task: Refactor `welding_tig_unit_v0` so it represents TIG-specific station hardware layered on a separate welding power supply, and update recipes/processes to require both where appropriate.

- [ ] Decision ID: `welding_tig_unit_v0.no_action`
  - Action type: `no_action`
  - Action: Leave `welding_tig_unit_v0` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `welding_tig_unit_v0.model_shielding_gas_supply`
  - Action type: `kb_resource_model`
  - Action: Decide whether argon/helium shielding gas is consumable/imported, locally produced, recovered, or part of a closed-loop gas system.
  - Queue task: Review TIG welding processes and add explicit shielding gas requirements, distinguishing gas cylinders/reusable handling hardware from consumed or recovered argon/helium supply.

- [ ] Decision ID: `welding_tig_unit_v0.add_material_specific_gas_notes`
  - Action type: `kb_detail`
  - Action: Add material compatibility notes for shielding gases; do not imply nitrogen is a universal TIG shielding substitute.
  - Queue task: Add TIG process notes specifying acceptable shielding gases by material class, especially argon/helium for common TIG use and limitations on nitrogen substitution.

- [ ] Decision ID: `welding_tig_unit_v0.decide_air_vs_water_cooled`
  - Action type: `kb_option`
  - Action: Decide whether water cooler/pump is always included or only required for high-duty-cycle/high-current TIG.
  - Queue task: Review `welding_tig_unit_v0` BOM and TIG process requirements; either keep the coolant loop as part of a complete station or condition it on high-duty-cycle/high-current operation.

- [ ] Decision ID: `welding_tig_unit_v0.ensure_tig_consumables_separate`
  - Action type: `kb_boundary`
  - Action: Ensure tungsten electrodes, cups, collets, filler rods, and shielding gas are modeled as consumables/spares rather than hidden in the reusable station.
  - Queue task: Review TIG recipes and related items so tungsten electrodes, filler rods, cups/collets, and shielding gas are explicit consumables or spare inputs, not silently included forever in `welding_tig_unit_v0`.

- [ ] Decision ID: `welding_tig_unit_v0.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## welding_tools_set

Source review: `research/machines/welding_tools_set.md`

Current interpretation: Real reusable welding support kit containing PPE, holders, clamps, cleaning tools, gauges, and accessories. It is valid as reusable tooling, but it must not be the only item providing welding process capability.

### Primary Path - Choose One

- [ ] Decision ID: `welding_tools_set.keep_as_support_tooling_kit`
  - Action type: `kb_semantics`
  - Action: Keep as welding tools/PPE/accessory kit and require a separate welding machine or power source for actual welding.
  - Queue task: Update `welding_tools_set` description and dependent processes so it is a manual support/PPE/accessory kit used with a separate welding machine such as `welding_tig_unit_v0`, `welding_arc_welder_v0`, or `welding_power_supply_v0`.

- [ ] Decision ID: `welding_tools_set.split_ppe_from_accessories`
  - Action type: `kb_split`
  - Action: Split PPE from electrode holders, clamps, leads, cleaning tools, and inspection gauges.
  - Queue task: Split `welding_tools_set` into PPE and welding accessory/tooling items if process modeling benefits from separate safety gear, current-carrying accessories, and inspection/cleanup tools.

- [ ] Decision ID: `welding_tools_set.no_action`
  - Action type: `no_action`
  - Action: Leave `welding_tools_set` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `welding_tools_set.ensure_processes_require_welder`
  - Action type: `kb_validation`
  - Action: Verify no welding process relies on `welding_tools_set` alone for welding capability.
  - Queue task: Review all processes using `welding_tools_set`; ensure each welding operation also requires an appropriate welding power source or welding machine.

- [ ] Decision ID: `welding_tools_set.add_leads_and_current_ratings`
  - Action type: `kb_detail`
  - Action: Add or verify welding leads/cables, electrode holders, ground clamps, insulation, springs, and current-rating constraints.
  - Queue task: Update `welding_tools_set` BOM/notes to include current-rated leads, electrode holders, ground clamps, conductive contacts, insulation, and relevant current/heat limits.

- [ ] Decision ID: `welding_tools_set.review_ppe_optics_manufacturability`
  - Action type: `kb_manufacturing_note`
  - Action: Treat helmet filter lenses or auto-darkening modules as imported or specialized unless the KB has credible optical filter materials/processes.
  - Queue task: Review `welding_tools_set` manufacturing recipe and add requirements or import assumptions for certified shade/filter lenses, auto-darkening modules, gloves, and heat-resistant protective materials.

- [ ] Decision ID: `welding_tools_set.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## winding_drums

Source review: `research/machines/winding_drums.md`

Current interpretation: Real reusable winding drum/spindle subassembly with shafts and bearings. It supports winding but does not by itself provide a complete winding machine unless paired with drive, traverse, tension, controls, and process-specific upstream equipment.

### Primary Path - Choose One

- [ ] Decision ID: `winding_drums.keep_as_subassembly`
  - Action type: `kb_semantics`
  - Action: Keep `winding_drums` as a subassembly/tooling set used by complete winding machines or stations.
  - Queue task: Update `winding_drums` description/usages so it is a drum/spindle subassembly with shafts/bearings, not a complete winding machine; ensure full winding processes also require drive, traverse, tension control, and controls as needed.

- [ ] Decision ID: `winding_drums.reclassify_as_part_or_subassembly`
  - Action type: `kb_reclassification`
  - Action: Reclassify from machine to part/subassembly when schema support allows.
  - Queue task: Move or reclassify `winding_drums` as a part/subassembly under the repo's current schema conventions, preserving recipes/BOM references for `winding_machine_v0` and related processes.

- [ ] Decision ID: `winding_drums.fold_into_winding_machine`
  - Action type: `kb_consolidation`
  - Action: Do not model drums separately except as internal BOM components of `winding_machine_v0` or other complete winders.
  - Queue task: Review references to `winding_drums`; where standalone use incorrectly grants winding capability, replace with `winding_machine_v0` or process-specific complete winding equipment and keep drums only as BOM components.

- [ ] Decision ID: `winding_drums.no_action`
  - Action type: `no_action`
  - Action: Leave `winding_drums` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `winding_drums.review_spool_winding_requirements`
  - Action type: `kb_validation`
  - Action: Check whether `spool_winding_basic_v0` should require a complete winding machine instead of only drums.
  - Queue task: Review `spool_winding_basic_v0`; add missing requirements for motor/drive, traverse guide, tension control, braking, spool mounting, guarding, and controls if currently relying only on `winding_drums`.

- [ ] Decision ID: `winding_drums.add_basalt_fiber_context`
  - Action type: `kb_detail`
  - Action: For basalt fiber, pair drums with tension control, traverse, speed control, and upstream fiber production equipment.
  - Queue task: Update basalt fiber process notes or requirements so `winding_drums` are paired with tension/traverse/speed controls and upstream fiber-forming equipment, rather than treated as a complete fiber winding station.

- [ ] Decision ID: `winding_drums.use_coil_winder_for_electrical_coils`
  - Action type: `kb_boundary`
  - Action: Use `coil_winding_machine` or equivalent complete coil winder for electrical coils, not bare winding drums.
  - Queue task: Review coil-related processes and references; replace bare `winding_drums` with `coil_winding_machine` or complete coil-winding equipment where precision electrical coil production is intended.

- [ ] Decision ID: `winding_drums.define_driven_vs_passive`
  - Action type: `kb_detail`
  - Action: Specify whether the drum set is driven, braked, passive, or includes traverse/tension mechanisms.
  - Queue task: Add notes or fields to `winding_drums` clarifying driven/passive/braked behavior and whether traverse/tension mechanisms are included or separate items.

- [ ] Decision ID: `winding_drums.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## wire_crimping_tools

Source review: `research/machines/wire_crimping_tools.md`

Current interpretation: Real reusable tool kit/station for electrical crimp terminations. It can remain a capacity provider for wiring integration, but should read as low-volume hand/pneumatic tooling rather than a high-volume harness-production machine.

### Primary Path - Choose One

- [ ] Decision ID: `wire_crimping_tools.rename_as_tool_kit`
  - Action type: `kb_semantics`
  - Action: Keep the item and update name/notes to "wire crimping tool kit" or "hand/pneumatic crimping tools."
  - Queue task: Update `wire_crimping_tools` display text/description so it is clearly a reusable hand/pneumatic crimping tool kit for low-volume wiring integration, not a standalone automatic crimping machine.

- [ ] Decision ID: `wire_crimping_tools.keep_generic_capacity_provider`
  - Action type: `kb_semantics`
  - Action: Keep as a generic crimping capacity provider with connector-specific die precision noted but not split.
  - Queue task: Preserve `wire_crimping_tools` as one generic wiring-integration requirement, and add notes that interchangeable dies must match terminal/contact families and wire ranges.

- [ ] Decision ID: `wire_crimping_tools.split_for_high_volume_harness_production`
  - Action type: `kb_split`
  - Action: Add separate crimp presses or cut-strip-crimp machines only if the KB models medium/high-volume harness production.
  - Queue task: If harness production throughput warrants it, introduce a separate bench crimp press or automatic cut-strip-crimp machine; otherwise keep `wire_crimping_tools` as low-volume tooling.

- [ ] Decision ID: `wire_crimping_tools.no_action`
  - Action type: `no_action`
  - Action: Leave `wire_crimping_tools` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `wire_crimping_tools.preserve_die_and_ratchet_bom`
  - Action type: `kb_validation`
  - Action: Preserve crimping dies, crimper frame/handles, ratchet/full-cycle mechanism, and fasteners as functionally important BOM components.
  - Queue task: Review `wire_crimping_tools` BOM and retain die geometry, ratchet/full-cycle mechanism, frame/handles, and fasteners unless schema cleanup requires renaming.

- [ ] Decision ID: `wire_crimping_tools.add_connector_specific_die_notes`
  - Action type: `kb_detail`
  - Action: Add connector-specific die, crimp-height, strip-length, wire-range, and terminal-compatibility notes.
  - Queue task: Add notes to `wire_crimping_tools` or wiring processes that reliable crimps require terminal-compatible dies, crimp-height control, strip-length control, wire-range matching, and pull-force/visual acceptance criteria.

- [ ] Decision ID: `wire_crimping_tools.add_inspection_and_test_pairing`
  - Action type: `kb_process_requirement`
  - Action: Pair crimping with inspection/test resources such as pull tester, multimeter, or visual inspection where wiring reliability matters.
  - Queue task: Review `wiring_and_electronics_integration_v0` and related processes; add inspection/test requirements for crimped terminations where appropriate, such as pull testing, continuity checks, or visual inspection.

- [ ] Decision ID: `wire_crimping_tools.decide_manual_vs_pneumatic_scope`
  - Action type: `kb_option`
  - Action: Decide whether the 5 kg item includes pneumatic tooling or should be limited to manual hand tools.
  - Queue task: Review `wire_crimping_tools` mass/BOM and either limit it to manual ratcheting tools or explicitly include a small pneumatic hand tool with air/power support assumptions.

- [ ] Decision ID: `wire_crimping_tools.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## wire_drawing_die_set

Source review: `research/machines/wire_drawing_die_set.md`

Current interpretation: Real passive precision tooling for wire drawing, but likely a duplicate or near-duplicate of `drawing_die_set_basic`. The die set does not provide pulling force, lubrication, payoff, cooling, or take-up by itself.

### Primary Path - Choose One

- [ ] Decision ID: `wire_drawing_die_set.consolidate_into_drawing_die_set_basic`
  - Action type: `kb_consolidation`
  - Action: Use `drawing_die_set_basic` as the canonical generic wire drawing die set unless a distinct aluminum-specific/light-duty scope is needed.
  - Queue task: Review references to `wire_drawing_die_set`; migrate generic wire-drawing uses to `drawing_die_set_basic`, preserve recipe/BOM information as needed, and retire or alias `wire_drawing_die_set` if it is accidental duplication.

- [ ] Decision ID: `wire_drawing_die_set.keep_as_aluminum_or_light_duty_variant`
  - Action type: `kb_semantics`
  - Action: Retain `wire_drawing_die_set` only as a smaller/light-duty or aluminum-specific die set, with scope documented.
  - Queue task: Update `wire_drawing_die_set` description, recipe, and references so it clearly represents an aluminum-compatible or light-duty die set distinct from `drawing_die_set_basic`; explain why the 2 kg versus 5 kg size difference matters.

- [ ] Decision ID: `wire_drawing_die_set.reclassify_as_tooling_part`
  - Action type: `kb_reclassification`
  - Action: Reclassify conceptually as reusable tooling/part rather than an active machine when schema support allows.
  - Queue task: Reclassify or annotate `wire_drawing_die_set` as passive reusable tooling, not an active machine, while preserving its ability to satisfy process resource requirements under current KB conventions.

- [ ] Decision ID: `wire_drawing_die_set.no_action`
  - Action type: `no_action`
  - Action: Leave `wire_drawing_die_set` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `wire_drawing_die_set.require_drawing_machine_and_lubrication`
  - Action type: `kb_process_requirement`
  - Action: Ensure wire drawing processes require a draw bench/capstan/drawing machine plus lubricant/cooling/payoff/take-up as needed.
  - Queue task: Review `wire_drawing_aluminum_v0` and related wire drawing processes; ensure the die set is paired with drawing force equipment, lubrication, payoff, take-up, and cooling where appropriate.

- [ ] Decision ID: `wire_drawing_die_set.add_die_material_variants`
  - Action type: `kb_option`
  - Action: Add die material notes or variants only where material/wear requirements justify them.
  - Queue task: Add notes or variants for hardened steel, tungsten carbide, PCD/diamond, or other die materials only where wire material, tolerance, or wear conditions require more specificity.

- [ ] Decision ID: `wire_drawing_die_set.verify_local_manufacturability`
  - Action type: `kb_manufacturing_note`
  - Action: Note that reliable dies require precise bore geometry, hard materials, polishing, heat treatment or inserts, lubrication, and wear control.
  - Queue task: Review `recipe_wire_drawing_die_set_v0`; add manufacturing constraints for precision bore geometry, polishing/grinding, suitable die material, heat treatment or carbide/diamond inserts, and wear/lubrication considerations.

- [ ] Decision ID: `wire_drawing_die_set.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## wire_stripper_set

Source review: `research/machines/wire_stripper_set.md`

Current interpretation: Real reusable electrical hand-tool set for removing insulation to controlled strip length without conductor damage. It can remain distinct where wire preparation is modeled explicitly, or fold into broader electrical hand tools for coarse processes.

### Primary Path - Choose One

- [ ] Decision ID: `wire_stripper_set.keep_separate_for_wire_preparation`
  - Action type: `kb_semantics`
  - Action: Keep `wire_stripper_set` as a specific reusable tool set for wire/cable preparation.
  - Queue task: Update or preserve `wire_stripper_set` as a manual/automatic hand-tool set for stripping conductors in wiring, cable harness, power cable, and crimp termination processes.

- [ ] Decision ID: `wire_stripper_set.fold_into_hand_tools_electrical`
  - Action type: `kb_consolidation`
  - Action: Fold into `hand_tools_electrical` where explicit wire preparation does not need a separate capacity provider.
  - Queue task: Review references to `wire_stripper_set`; consolidate into `hand_tools_electrical` for coarse electrical assembly processes, while preserving separate stripping requirements only where strip length or conductor damage is explicitly modeled.

- [ ] Decision ID: `wire_stripper_set.split_power_cable_vs_electronics`
  - Action type: `kb_split`
  - Action: Split large power-cable stripping from small electronics-wire stripping if size/material differences matter.
  - Queue task: If cable scale differs enough to justify it, split `wire_stripper_set` into small electronics wire strippers and large power-cable jacket/insulation strippers; otherwise keep one shared set under Conservative Mode.

- [ ] Decision ID: `wire_stripper_set.no_action`
  - Action type: `no_action`
  - Action: Leave `wire_stripper_set` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `wire_stripper_set.add_strip_quality_notes`
  - Action type: `kb_detail`
  - Action: Add strip-length accuracy, blade/gauge sizing, and conductor-nick/damage avoidance notes for critical harnesses.
  - Queue task: Add notes to wire stripping and harness processes describing controlled strip length, appropriate gauge/blade selection, and conductor damage avoidance where wiring reliability matters.

- [ ] Decision ID: `wire_stripper_set.keep_manual_recipe_scope`
  - Action type: `kb_manufacturing_note`
  - Action: Keep the local recipe scoped to manual tools: hardened jaws/blades, gauge notches or stops, pivots, springs, handles, and insulation.
  - Queue task: Review `wire_stripper_set` recipe/BOM and keep it aligned with plausible manual wire-stripper fabrication unless powered stripping equipment is selected separately.

- [ ] Decision ID: `wire_stripper_set.add_powered_stripping_machine_only_if_needed`
  - Action type: `kb_option`
  - Action: Add a powered bench stripping machine only for high-volume harness production or scrap-wire processing.
  - Queue task: If high-volume harness production or scrap-wire recovery is modeled, add a separate powered wire/cable stripping machine; do not treat it as equivalent to the 1.5 kg hand-tool set.

- [ ] Decision ID: `wire_stripper_set.consider_harness_tool_kit_bundle`
  - Action type: `kb_option`
  - Action: Consider bundling wire strippers and crimp tools into a harness assembly kit if that better matches process modeling.
  - Queue task: Review `wire_stripper_set`, `wire_crimping_tools`, and harness assembly processes; decide whether to keep separate tools or create a reusable harness assembly toolkit wrapper.

- [ ] Decision ID: `wire_stripper_set.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

## work_rest_adjustable

Source review: `research/machines/work_rest_adjustable.md`

Current interpretation: Real reusable tooling/accessory for supporting work during grinding or polishing. It is a physical safety and accuracy component, not a powered standalone machine. Lathe support should be split if that function is intended.

### Primary Path - Choose One

- [ ] Decision ID: `work_rest_adjustable.keep_as_grinder_polisher_work_rest`
  - Action type: `kb_semantics`
  - Action: Keep the current ID but clarify it as an adjustable grinder/polisher work rest.
  - Queue task: Update `work_rest_adjustable` description/usages to "adjustable grinder/polisher work rest" and ensure it is modeled as reusable tooling/accessory for bench grinders, polishing stations, belt/disk grinders, or similar abrasive processes.

- [ ] Decision ID: `work_rest_adjustable.split_lathe_steady_rest`
  - Action type: `kb_split`
  - Action: Split lathe/cylindrical-work support into a separate `steady_rest_adjustable` or `follow_rest_adjustable` item.
  - Queue task: If turning or cylindrical grinding support is intended, create or reference a separate steady/follow rest item and remove lathe-support ambiguity from `work_rest_adjustable`.

- [ ] Decision ID: `work_rest_adjustable.reclassify_as_tooling_accessory`
  - Action type: `kb_reclassification`
  - Action: Reclassify conceptually as tooling/accessory component rather than independent powered machine when schema support allows.
  - Queue task: Reclassify or annotate `work_rest_adjustable` as a small fabricated tooling/accessory component while preserving its use as a required support item under current process resource conventions.

- [ ] Decision ID: `work_rest_adjustable.no_action`
  - Action type: `no_action`
  - Action: Leave `work_rest_adjustable` unchanged.
  - Queue task: No KB edit task should be enqueued for this machine unless another selected decision in this block requires it.

### Compatible Followups - Choose All That Apply

- [ ] Decision ID: `work_rest_adjustable.review_grinding_process_requirements`
  - Action type: `kb_process_requirement`
  - Action: Check whether `grinding_and_finishing_v0` should require the grinder/polisher machine and list the work rest as tooling rather than separate machine capability.
  - Queue task: Review `grinding_and_finishing_v0`, `bench_grinder`, and `polishing_station_v0` references so the work rest is paired with the actual grinder/polisher equipment and does not imply process capability by itself.

- [ ] Decision ID: `work_rest_adjustable.add_safety_gap_and_rigidity_notes`
  - Action type: `kb_detail`
  - Action: Add safety/accuracy notes: rigid adjustable rest, secure clamping, small wheel gap, repeatable angle setting, vibration resistance.
  - Queue task: Add notes to `work_rest_adjustable` and grinder/polisher processes covering rigid adjustment, clamping, wheel-gap control, angle repeatability, and vibration resistance.

- [ ] Decision ID: `work_rest_adjustable.add_wear_surface_details`
  - Action type: `kb_detail`
  - Action: Add replaceable contact plates, hardened wear strips, or similar contact-surface details where wear matters.
  - Queue task: Review `work_rest_adjustable` BOM/recipe and add replaceable contact plate or wear-strip components if needed for abrasive service.

- [ ] Decision ID: `work_rest_adjustable.note_local_fabricability`
  - Action type: `kb_manufacturing_note`
  - Action: Note that this is likely locally fabricated once basic machining, fasteners, and steel/cast iron are available.
  - Queue task: Add manufacturability notes to `work_rest_adjustable` indicating steel/cast iron base, slotted or sliding adjustment, locking screws/clamps/cam levers, and basic shop fabrication requirements.

- [ ] Decision ID: `work_rest_adjustable.custom_user_instruction`
  - Action type: `custom_user_instruction`
  - Action: User-provided instruction overrides or narrows this block.
  - Queue task: Use the freeform instruction below as the controlling KB edit request.

Freeform instructions:

```text

```

<!-- APPEND_NEXT_MACHINE_BELOW -->
