# reAM250 BOM to KB: Lunarized Closure Abstraction

## 1. Purpose

This document summarizes the decision framework for converting the reAM250 BOM research results into the SERES KB.

The goal is to use the real BOM as an evidence source, then build a lunarized closure abstraction that can support simulation and closure analysis. Faithfully reproducing the commercial machine BOM or fully redesigning a lunar reAM250 is outside this pass.

This abstraction avoids two extremes:

- Overly literal commercial BOM modeling: the KB becomes dominated by vendor SKUs, commercial standard parts, procurement interfaces, and Earth-specific design choices.
- Overly free redesign: the model becomes simpler, but may hide hard constraints such as precision, sealing, powder handling, thermal management, calibration, and inspection.

For this BOM to KB pass, the goals are:

- Preserve the reAM250 BOM as an evidence layer.
- Map BOM rows to lunarized closure abstraction layer.
- Keep as much useful detail as possible without breaking closure analysis.
- Explicitly mark design substitution, item merging, process abstraction, and import assumptions.

This strategy is valid if SERES is currently testing whether a lunar industrial chain can close under explicit assumptions, not trying to reproduce the exact original reAM250 supply chain.

## 2. Item Identity

In the current framework, whether something should be treated as a distinct item is mainly determined by four properties:

1. Functional purpose
2. Material
3. Scale or capacity
4. Geometry form

Manufacturing method usually should not define item identity by itself. An aluminum screw does not become a different item just because it was made by a different route. A steel screw and an aluminum screw usually are different items because the material changes. A solid aluminum bar, hollow aluminum bar, and aluminum extrusion may also be different items because geometry form changes.

Manufacturing method can still affect identity indirectly. If the process changes strength, precision, surface condition, heat treatment state, sealing capability, or material microstructure, then the output may no longer be the same closure item.

The recommended KB approach is: keep original manufacturing method in the evidence, recipe, or process layer. Let it affect item identity only when it changes the output specification.

## 3. What Drives Complexity in Closure Analysis

From the perspective of the current KB closure analysis, the most direct drivers of complexity are:

- Material diversity
- Process diversity (Machine needed)
- Process flexibility

Material diversity matters because closure analysis follows material requirements upstream. If a machine BOM needs aluminum, steel, copper, glass, ceramics, rubber, and electronic materials, each material may require a different production recipe, source, substitution strategy, or import assumption. The more material types the model uses, the more supply chains the closure graph must explain.

Process diversity matters because different processes usually correspond to different provider machines. Even if two parts use the same material, if one requires extrusion, one requires CNC machining, and one requires laser powder bed fusion, closure analysis must show that each process can be executed.

Process flexibility matters because a single process can cover very different ranges of parts. CNC, general additive manufacturing, and manual assembly with general tools can often cover many geometry variants. Processes that require a dedicated mold, die, fixture, or forming tool for each part family add hidden dependencies whenever the part set changes. Closure analysis should prefer processes that can cover many parts.

Therefore, merging should not mean "combine things that look similar." The better question is: after merging, does closure analysis need to track fewer material types, process types, provider machine types, or a higher share of reusable processes? If not, the merge is mostly naming cleanup. If yes, the merge genuinely reduces closure complexity.

## 4. Proposed BOM to KB Workflow

The required operations include:

- Preserve environment-control source roles.
- Decompose items and decide which ones remain imports.
- Abstract processes into shared lunar closure buckets.
- Merge items.

All of these operations matter, but formal merging does not need a separate candidate-group step, and it does not need a separate coarse functional-classification layer. The simpler approach is to use the precise function descriptions in the BOM research to preserve environment-control roles, decompose complex items, apply lunarized process abstraction, and then merge items that have actually converged.

### Step 1: Preserve Original BOM Evidence

Do not directly rewrite each BOM row into a lunar design. Keep the original function, mass, material, how_to_make, and uncertainty. This layer preserves traceability to reality.

### Step 2: Decompose Complex Items

Before process abstraction and merging, handle complex modules, vendor assemblies, electronics/control modules, motor/gearbox assemblies, laser/optics subassemblies, powder handling modules, and similar complex items.

The goal is to expose internal closure dependencies so later process abstraction, merging, and import/local decisions can act on them. Decomposition should stop at the level useful for closure analysis and avoid expanding back into full vendor BOM or CAD part granularity.

### Step 3: Apply Lunarized Process Abstraction

Read the function, material, and how_to_make fields from the BOM research directly, then place each item into the simplest compatible lunarized process bucket. The key question is whether the closure model can cover these items with fewer process types and provider machines. The original BOM process is supporting evidence.

Use these shared process buckets:

- `general_metal_additive_with_finish_machining`
- `general_subtractive_machining`
- `sheet_plate_cutting_drilling`
- `structural_profile_stock_fabrication_cutting`
- `polymer_elastomer_forming_dispensing`
- `manual_assembly_with_general_tools`
- `fastener_forming_thread_rolling`
- `plumbing_connector_fabrication_testing`
- `precision_component_import_decompose_later`

During process abstraction, first check whether the selected bucket can meet the tolerance, surface finish, sealing quality, and alignment accuracy required by the item function. The primary bucket is only the main closure handle. Record supporting processes such as cutting, drilling, finishing, leak testing, calibration, and inspection when the row needs them.

Process abstraction should also reference existing KB processes when they are relevant. These references are candidates for later staging, not final recipes.

Process abstraction does not perform formal merging yet. It answers one question: can items that originally used different processes use the same shared process bucket in the lunarized closure model?

### Step 4: Merge Items That Have Converged

After process abstraction, first find items with the same functional purpose and mass or scale within a 2x range. Then judge whether material, process, and geometry form can be adjusted into the same closure item through lunarized design. Finally, check whether machining precision prevents the merge.

Machining precision is a merge guardrail. If the item function depends on significantly different tolerance, surface finish, sealing quality, or alignment accuracy, keep a separate item or record the risk in notes.

Example:

- Original BOM: aluminum extrusion, aluminum bar, simple CNC bracket.
- Lunarized strategy: local metal forming plus post-processing.
- KB closure item: `structural_profile_aluminum_medium` or `mounting_bracket_aluminum_small`.
- Conclusion: merge is acceptable, but mark geometry substitution assumed.

### Step 5: Decide Import vs Local Manufacture

Import decisions should come after the lunarized strategy and formal merging, because we first need to understand whether a local manufacturing path is plausible and which items have already been merged into the same closure item.

Early import candidates include:

- high precision laser source
- advanced optics
- complex electronics and control modules
- sensors requiring specialized semiconductor fabrication
- precision metrology devices
- components whose manufacturing chain would dominate the model

This recommendation is valid if the current KB pass focuses on the main lunar industrial chain. Full semiconductor, optics, or laser manufacturing closure can be handled in a later scope.

### Step 6: Write KB Entries and Preserve Assumptions

Only then should we create or update KB items, recipes, processes, and BOM mappings. Important merges or substitutions should include notes recording:

- What the original BOM used.
- What the KB abstracts it into.
- Which identity properties support the merge: function, material, scale, or geometry.
- Which differences are considered closure-insignificant.
- Which differences remain assumptions.

## 5. Examples

### Structural Members

Aluminum bars, hollow aluminum bars, and aluminum extrusions can often be abstracted as `structural_profile_aluminum_medium` at the closure layer. This item name preserves functional purpose, material, scale, and geometry form.

However, if an extrusion provides a T-slot modular interface, precision rail reference, sealing frame, torsion-resistant section, or calibration reference, it should not be merged unconditionally.

### Brackets and Mounting Plates

Many simple brackets and mounting plates can be merged into `mounting_bracket_aluminum_small`, `mounting_bracket_steel_small`, or `mounting_plate_aluminum_small`. Whether the original part was CNC-machined, sheet metal, cast, or printed does not necessarily require a distinct item unless the output specification differs.

### Vacuum, Gas Handling, and Environment-Control Components

For this pass, vacuum-specific components are not automatically excluded from the lunarized closure KB. Treat them as ordinary environment-control, gas/fluid handling, sealing, and contamination-control evidence until later review decides the abstraction.

### Electronics

Terminal blocks, PLC modules, sensors, and power supplies should usually not be modeled at vendor SKU granularity. At the closure layer, they can initially be abstracted into control electronics, terminal block sets, sensor suites, and similar items, with import or future-localization assumptions.
