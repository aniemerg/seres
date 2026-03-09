# SRM2 BOM Research Prompts

Purpose:
- Prompts to run in a research agent (e.g., ChatGPT) to gather BOM-quality detail for high-interest KB gaps before authoring machine BOMs/recipes.
- Focus: physically manufacturable, lunar self-replication context, with traceable assumptions.

How to use:
- Run each prompt separately.
- Ask for structured output in the schema provided.
- Require explicit uncertainty/confidence tags and source quality notes.

## Global System Prompt (use for all prompts)
You are a technical research assistant supporting a lunar self-replication knowledge base.
Constraints:
- Prioritize physically realizable designs that can be staged on the Moon.
- Favor modularity, repairability, and first-generation ISRU feasibility.
- Distinguish first-generation (high confidence) vs second-generation (advanced/optional).
- Provide concise but specific engineering detail suitable for machine BOM and process recipe drafting.
Output format:
1. `System boundary`
2. `Functional decomposition`
3. `Candidate architecture options (A/B/C)`
4. `Recommended architecture`
5. `BOM draft` (component, material, qty, unit, rationale, manufacturability)
6. `Manufacturing route draft` (ordered process steps with inputs/outputs)
7. `Test/verification steps`
8. `Failure modes and maintenance plan`
9. `Assumptions and uncertainties`
10. `Sources and confidence` (high/medium/low confidence per major claim)

## Prompt 1: Prospecting Module for Rover
Research a rover-attachable `prospecting_module` for lunar resource prospecting.
Requirements:
- Module should attach to a small rover platform (Kapvik-like class).
- Should support mineral targeting and site qualification for downstream extraction.
- Prefer modular subtools (e.g., magnetometer payload, shallow coring/sampling head).
Deliverables:
- Recommended module architecture.
- Submodule BOM and likely mass ranges.
- Mechanical/electrical interfaces needed between rover and module.
- Suggested maintenance/replacement strategy (swap-in field service).
- First-gen vs second-gen capability split.

## Prompt 2: Magnetometer Payload
Research a practical `magnetometer_payload` suitable for lunar rover prospecting.
Requirements:
- Lightweight, robust against thermal cycling and dust.
- Sufficient for detecting magnetic anomalies relevant to NiFe/troilite prospects.
- Include calibration approach in vacuum/thermal extremes.
Deliverables:
- Sensor stack options (fluxgate, Hall, etc.) with tradeoffs.
- Electronics and shielding requirements.
- BOM draft with likely manufacturable vs imported components.
- Data-quality constraints that affect process gating decisions.

## Prompt 3: Electrostatic Separator Machine
Research a lunar `electrostatic_separator` machine concept for regolith beneficiation.
Requirements:
- Compatible with dry, vacuum-dominant operations.
- Designed to separate non-magnetic mineral fractions after comminution.
- Integrates with existing magnetic/gravity beneficiation chain.
Deliverables:
- Machine architecture options and recommended baseline.
- Power, throughput, and feed-size assumptions.
- BOM draft including electrodes, HV supply, insulation, housings, conveyance.
- Manufacturing route and commissioning tests.
- Failure modes (dust fouling, arcing, electrode wear).

## Prompt 4: Electrostatic Beneficiation Process Recipe
Research a process recipe for `electrostatic_beneficiation` of crushed regolith.
Requirements:
- Provide plausible feed and product splits for highlands-like feed.
- Include preconditioning requirements (size/moisture/charge prep).
- Show integration points with magnetic separation and downstream chemistry.
Deliverables:
- Stepwise process flow with candidate I/O streams.
- Machine requirements and process controls.
- Byproducts/tailings handling recommendations.
- Sensitivity parameters (feed PSD, mineralogy, charge distribution).

## Prompt 5: Liquation Separation (Fe vs TiO2)
Research `liquation_fe_tio2_separation` after ilmenite reduction.
Requirements:
- Separate metallic iron fraction from titanium oxide-rich fraction.
- Prefer realistic thermal envelope and achievable equipment complexity.
Deliverables:
- Process options and recommended route.
- Required furnaces/reactors and ancillary equipment.
- Expected phase behavior assumptions and outputs.
- Quality/purity checkpoints for Fe and TiO2 products.

## Prompt 6: Quartz Piezo Sensor Fabrication
Research a manufacturable `quartz_piezo_sensor_fabrication` route.
Requirements:
- Build from quartz crystal and lunar-compatible electrode/insulation options.
- Prioritize pressure/tactile sensing utility for robotics.
Deliverables:
- Sensor architecture options (element geometry, electrode approach).
- BOM-level parts/materials list.
- Assembly and calibration steps.
- Expected performance bounds and uncertainty.

## Prompt 7: Wheatstone Bridge Module
Research a practical `wheatstone_bridge_module` for strain/pressure sensing.
Requirements:
- Should integrate with strain-gauge elements and rover/industrial instrumentation.
- Emphasize rugged, reparable implementation over miniaturization.
Deliverables:
- Circuit/module architecture, packaging, connectors.
- BOM draft and production sequence.
- Calibration/test procedure and drift mitigation plan.

## Prompt 8: Selective Solar Sinterer
Research a machine concept for `selective_solar_sinterer`.
Requirements:
- Uses concentrator-delivered thermal input.
- Targets ceramic or regolith-derived feedstocks.
- Must fit staged lunar manufacturing maturity.
Deliverables:
- Opto-thermal architecture, scan strategy, feed handling.
- BOM and likely sourced subsystems.
- Process limits (resolution, throughput, thermal gradients).
- Maintenance plan for optics and motion subsystems.

## Prompt 9: EBAM Printer (Electron Beam Additive)
Research a lunar-viable `ebam_printer` concept for metal deposition.
Requirements:
- Vacuum-compatible electron beam source and motion system.
- Focus on manufacturability with existing vacuum-tube/high-voltage chains where possible.
Deliverables:
- Architecture options and recommended baseline.
- BOM draft (electron gun, HV, vacuum chamber integration, feedstock delivery).
- Safety/interlock requirements.
- Qualification tests for deposition quality.

## Prompt 10: Multi-Material 3D Printer
Research a staged `multi_material_3d_printer` concept aligned with lunar self-replication.
Requirements:
- Support at least metal + ceramic/polymer-like insulation pathways.
- Modular toolheads preferred (printing + milling + simple assembly wrist as extensions).
Deliverables:
- Capability roadmap by generation.
- Core BOM + toolhead BOMs.
- Process routes and handoff logic between toolheads.
- Reliability and maintainability strategy.

## Prompt 11: Grinding Media (Alumina and Silumin)
Research manufacturable grinding media options:
- `alumina_grinding_media`
- `silumin_grinding_media`
Requirements:
- Compatible with regolith comminution and contamination constraints.
- Include life/wear characteristics and replacement planning.
Deliverables:
- Material property comparison.
- Production route options and recommended baseline for each media type.
- QA checks and expected wear/failure behavior.

## Prompt 12: Electrical Insulation Form Factors
Research three insulation candidates for lunar electromechanical systems:
- `glass_fiber_cloth_insulation`
- `porcelain_insulator`
- `enamel_glass_insulation`
Requirements:
- Compare against existing generic ceramic/insulator entries.
- Focus on where each form factor is uniquely useful.
Deliverables:
- Use-case matrix and substitution guidance.
- BOM/manufacturing route sketches.
- Lifecycle/repair considerations and failure modes.

## Prompt 13: PMT Localization Feasibility (Optional Advanced)
Assess whether `photomultiplier_tube` should remain import-only or gain a local variant.
Requirements:
- Distinguish minimum viable local PMT from full high-performance PMT.
- Identify showstopper dependencies and likely import bottlenecks.
Deliverables:
- Decision recommendation: import-only / hybrid / local variant.
- If hybrid/local, provide minimal local BOM and process chain.
- Explicit confidence score and top unknowns.

## Prompt 14: Kovar Wire Form-Factor
Research converting existing `kovar_alloy_fe_ni_co_v0` into a useful wire form factor (`kovar_wire`).
Requirements:
- Define why wire form is needed beyond bulk alloy in this system.
- Include drawability/processability constraints and insulation compatibility.
Deliverables:
- Proposed form-factor spec.
- Manufacturing steps from alloy to wire.
- Required machine/tooling and QA checks.

## Standard Output Table (append to each answer)
Please append this table:

| Candidate | Existing equivalent likely? | Net new IDs recommended | BOM confidence (H/M/L) | Key blockers | Suggested generation |
|---|---|---|---|---|---|

