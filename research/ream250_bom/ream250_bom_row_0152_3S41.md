---
row_identity:
  item: "3S41"
  cad_file: "3S41_part_1"
  source_row_number: 152
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom gas outlet segment, part 1 of the 3S41-3S48 gas outlet group; the CAD shows a long thin-wall rectangular/duct-like piece used as one structural wall or flow-guide segment in the outlet path."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S41_part_1.step; research/ream250_bom/ream250_bom_row_0152_3S41__views_2x2.png"
    cited_fact_or_basis: "BOM row 152 lists item 3S41, quantity 1, CAD file 3S41_part_1, description 'gas outlet: part 1'. The manifest maps row 152 to one matched_existing part STEP. FreeCAD measured one solid with volume 64568.000 mm^3 and a 50.00 x 460.00 x 44.00 mm bounding box; the rendered preview shows a long thin rectangular/duct-like segment."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is interpreted within neighboring BOM rows 3S41 through 3S48, which are sequential 'gas outlet' parts, so this is one custom segment of the larger outlet rather than a standalone fitting."
  uncertainty_notes:
    - "The BOM and isolated part CAD do not show the complete outlet assembly, so the exact mating faces and gas-flow role are inferred from the row group and visible geometry."
mass:
  value_kg: 0.507
  basis: "FreeCAD volume 64568.000 mm^3 = 6.4568e-5 m^3. Using the local generic steel density of 7850 kg/m^3 gives 0.5069 kg per part, rounded to 0.507 kg. Stainless steel at 8000 kg/m^3 would give about 0.517 kg. BOM quantity is 1, so per-unit mass and row total are the same."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S41_part_1.step; kb/materials/properties.yaml; web targeted search"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 64568.000 mm^3, area 130394.000 mm^2, and bounding box 50.00 x 460.00 x 44.00 mm. The local density table lists steel at 7850 kg/m^3 and stainless_steel at 8000 kg/m^3. targeted_web_search: searched \"3S41 gas outlet reAM250 material\", \"3S41_part_1\", \"reAM250 gas outlet material\", and \"3S41_part_1 gas outlet material\"; results were duplicate/public BOM listings only and did not provide row-specific material or catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is treated as the physical material volume for one gas-outlet segment."
    - "Generic steel density is used as a conservative metal outlet estimate because neither the BOM nor STEP metadata resolves the alloy."
  uncertainty_notes:
    - "Material is not directly specified; if this segment is aluminum, the same CAD volume would be about 0.174 kg using the local aluminum density of 2700 kg/m^3."
material:
  primary_material: "unknown metal/alloy sheet"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0152_3S41__views_2x2.png; web targeted search"
    cited_fact_or_basis: "BOM row 152 identifies the part as 'gas outlet: part 1' but provides no material, manufacturer, product ID, or link URL. Local assembly STEP material extraction for 3S41_part_1 returned only placeholder material 'Generic' with density 1000.0. The rendered preview shows a rigid thin-wall outlet segment. targeted_web_search: searched \"3S41 gas outlet reAM250 material\", \"3S41_part_1\", \"reAM250 gas outlet material\", and \"3S41_part_1 gas outlet material\"; results were duplicate/public BOM listings only and did not resolve material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A gas outlet segment in this machine is modeled as sheet metal because the CAD geometry is a rigid thin-wall duct-like form and the row sits among other gas/vacuum outlet hardware."
  uncertainty_notes:
    - "No source resolves the exact material family or grade; later KB modeling should keep this as a broad metal/alloy sheet part unless a drawing or assembly material note identifies the alloy."
how_to_make:
  summary: "Make as a custom sheet-metal gas-outlet segment: cut a long sheet blank, form or bend the thin-wall outlet geometry, join any seams or edges required by the surrounding outlet assembly, then deburr, clean, and inspect for fit."
  manufacturing_steps:
    - "Cut the long sheet-metal blank or profile from metal sheet using laser, waterjet, or CNC shear/profile cutting."
    - "Bend or form the blank to the approximately 50 x 460 x 44 mm outlet-segment geometry shown in CAD."
    - "Join seams or mating edges by welding, brazing, folded seams, or sealed fastening according to the gas-tightness requirement of the complete outlet."
    - "Deburr, clean, and inspect the long edges and end interfaces before assembling with neighboring gas outlet parts."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S41_part_1.step; research/ream250_bom/ream250_bom_row_0152_3S41__views_2x2.png; web targeted search"
    cited_fact_or_basis: "FreeCAD measured one solid with a 50.00 x 460.00 x 44.00 mm bounding box. The preview shows a long thin rectangular/duct-like segment without visible standard fitting, shaft, or calibrated module features. targeted_web_search: searched \"3S41 gas outlet reAM250 manufacturing\", \"3S41_part_1 drawing\", \"reAM250 gas outlet material\", and \"3S41_part_1 gas outlet material\" results were duplicate/public BOM listings only and did not provide a row-specific fabrication drawing or process note."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The visible thin-wall geometry is treated as sheet-metal fabrication rather than casting or billet machining."
    - "Final sealing and joining are handled at the larger gas outlet assembly level because this row is only part 1 of the outlet group."
  uncertainty_notes:
    - "The CAD and BOM do not state wall thickness callouts, bend allowances, tolerances, surface finish, or gas-tightness class; those details determine the final seam and inspection requirements."
kb_implications:
  - "item_granularity: simple_part - Model as one custom fabricated sheet-metal gas outlet segment, with assembly-level joining handled by the larger 3S outlet group."
---

Research result for reAM250 BOM row 152.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0152_3S41.md
source_research_sha256: "a07d70d7f9ba2835a85a44f826eb796c5ae9db8825663ecac20db6b12317e686"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the gas-outlet part 1 identity, long thin-wall duct-like CAD form, generic steel mass estimate with material uncertainty, sheet-metal fabrication route, and simple-part KB implication."
decomposition:
  decision: simple_part
  rationale: "The row is one fabricated segment of a larger gas outlet group. It should remain a simple part during row conversion, with larger outlet joining and leak checks handled at assembly staging."
  proposed_subparts: []
process_abstraction:
  original_process_family: sheet_metal_gas_outlet_segment_fabrication
  primary_process_bucket: plumbing_connector_fabrication_testing
  supporting_processes:
    - cutting
    - forming
    - joining
    - deburring
    - cleaning
    - leak_testing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: sheet_metal_fabrication_v0
      fit: partial
      reason: "Covers cutting, bending, forming, and deburring the thin-wall outlet segment from sheet stock."
    - process_id: sheet_metal_bending_and_forming_v0
      fit: supporting
      reason: "Relevant to forming the long rectangular duct-like segment after blank cutting."
    - process_id: plumbing_and_pneumatics_v0
      fit: supporting
      reason: "Relevant to later assembly of the outlet group into a gas-handling path."
    - process_id: leak_testing_v0
      fit: supporting
      reason: "Relevant once this segment is joined into the larger outlet assembly and gas-tightness is required."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional and fit checks at the long edges and end interfaces."
  abstraction_decision: substitute_process_family
  rationale: "The source route is sheet-metal fabrication, but the closure-relevant role is a gas outlet path segment. Plumbing connector fabrication with sheet forming support better preserves the gas-handling function and downstream leak-test guardrails."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: gas outlet path segment for guiding process gas flow through the outlet assembly
  material: unknown_metal_alloy_sheet
  scale_or_capacity:
    mass_kg: 0.507
    bom_quantity: 1
    row_total_mass_kg: 0.507
    scale_class: small
  geometry_form: long_thin_wall_rectangular_duct_like_sheet_segment
merge_pool:
  eligible: true
  functional_purpose_key: gas_flow_path
  precision_guardrails:
    - gas_path_fit
    - seam_joining_quality
    - leak_tightness_after_assembly
    - material_family_unresolved
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - plumbing_connector_fabrication_testing
  import_risk_factors:
    - "Material family is unresolved, with aluminum, steel, and stainless scenarios changing mass and joining details."
    - "Gas-tightness class is unknown and may require assembly-level joining plus leak testing beyond simple sheet forming."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares the 3S gas outlet segments and decides whether they stage as separate formed sheet parts behind one outlet assembly."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review across the 3S41-3S48 gas outlet group before assigning final closure item IDs."
assumptions:
  - "The row belongs to a multi-part gas outlet group, so sealing and joining should be assessed at the larger outlet assembly level."
  - "Generic steel mass is a conservative planning estimate until the sheet alloy is resolved."
unresolved:
  - "Exact material family, wall thickness callouts, bend allowances, seam details, tolerance, surface finish, and gas-tightness requirement remain unresolved."
```
