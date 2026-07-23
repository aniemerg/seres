---
row_identity:
  item: "6R"
  cad_file: "6R_belt"
  source_row_number: 196
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small closed-loop rubber belt, likely a drive or timing belt used with the neighboring belt pulley rows in the reAM250 row-6 motion assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0196_6R__views_2x2.png"
    cited_fact_or_basis: "BOM row 196 lists item 6R, quantity 3, CAD file 6R_belt. Manifest row 196 maps 6R_belt to gold_export/parts/6R_belt.step with matched_existing part status. The rendered CAD preview shows a thin closed loop; nearby BOM rows list GT2 belt pulleys and pulley mounts."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name, closed-loop CAD shape, and adjacent pulley rows are interpreted together as a motion-transmission belt rather than a static seal."
  uncertainty_notes:
    - "The exact belt standard, pitch, tooth profile, and intended pulley pairing are not stated in row 196."
mass:
  value_kg: 0.00402
  basis: "FreeCAD measured volume 4323.217 mm^3. Assembly STEP material metadata reports Rubber with density 930 kg/m^3. Computed mass: 4323.217 mm^3 x 1e-9 m^3/mm^3 x 930 kg/m^3 = 0.00402 kg per belt."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6R_belt.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 4323.217 mm^3, area 9383.064 mm^2, and bounding box 77.00 x 130.43 x 10.00 mm. Local STEP material extraction for product 6R_belt found material Rubber and density 930.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP volume is treated as the physical belt volume and the assembly material density is applied uniformly to the part."
  uncertainty_notes:
    - "Any embedded cords, fabric reinforcement, or tooth-detail volume not represented distinctly in the STEP would change the true purchased belt mass."
material:
  primary_material: "rubber"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local STEP material extraction for product 6R_belt found material Rubber with density 930.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local metadata gives only a broad Rubber material name, not a specific compound such as neoprene, polyurethane, nitrile rubber, silicone rubber, or a reinforcement material."
how_to_make:
  summary: "Model as a external or cut-to-length rubber belt stock item unless later KB work needs detailed belt manufacturing; form a reinforced rubber belt loop by extrusion or calendaring, curing, and joining/molding to final loop geometry"
  manufacturing_steps:
    - "Select rubber belt stock or compound compatible with the pulley geometry and operating environment."
    - "Form a strip by extrusion, calendaring, or molding; include cord or fabric reinforcement if required by the drive load."
    - "Cure/vulcanize the rubber and join or mold the strip into the closed loop."
    - "Trim and inspect loop width, thickness, length, and fit against the pulley set."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6R_belt.step; research/ream250_bom/ream250_bom_row_0196_6R__views_2x2.png"
    cited_fact_or_basis: "The CAD part is a single thin closed-loop rubber belt with measured bounding box 77.00 x 130.43 x 10.00 mm. targeted_web_search: searched \"6R_belt reAM250\", \"6R_belt reAM250 rubber belt\", \"6R_belt CAD belt\", \"6R_belt GT2\", and \"reAM250 6R_belt GT2\" results only duplicated BOM text or unrelated belt pages and did not provide a row-specific vendor or manufacturing specification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The route is inferred from the belt geometry and broad rubber material metadata, not from a row-specific vendor drawing."
    - "For near-term KB modeling, this should be treated as a external belt or stock belt part because the exact profile and compound are unspecified"
  uncertainty_notes:
    - "Without a belt designation or vendor page, the manufacturing route cannot specify tooth pitch, reinforcement, compound, splice method, or curing parameters."
kb_implications:
  - "item_granularity: simple_part - This is a replaceable rubber belt-like motion component; model as a purchased/stock belt unless later work resolves the exact standard and compound."
---

Research result for reAM250 BOM row 196, item 6R.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0196_6R.md
source_research_sha256: "5cdc63b3271fc6f9b3c6368df5ceaa90213dd519adfcd7568dbdc4e76b2146c2"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the small closed-loop belt function, 0.00402 kg per-belt mass with BOM quantity 3 and 0.01206 kg row total, rubber material metadata, inferred belt-forming route, KB implication, and CAD preview showing a thin closed loop near pulley rows."
decomposition:
  decision: simple_part
  rationale: "The row is a replaceable belt-like motion component with no module internals modeled at this stage; reinforcement and tooth form are unresolved material/process guardrails."
  proposed_subparts: []
process_abstraction:
  original_process_family: rubber_belt_loop_forming
  primary_process_bucket: polymer_elastomer_forming_dispensing
  supporting_processes:
    - elastomer_forming
    - extrusion
    - forming
    - curing
    - joining
    - cutting
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: conveyor_belt_loop_fabrication_v0
      fit: partial
      reason: "Captures rubber belt loop fabrication at a coarse level, though this row is a small motion belt with unresolved tooth profile."
    - process_id: elastomer_molding_basic_v0
      fit: partial
      reason: "Relevant to forming rubber components but not sufficient for reinforced timing-belt details."
    - process_id: silicone_rubber_vulcanization_v0
      fit: poor_fit
      reason: "Anchors elastomer curing concepts, but the row material is broad rubber and not specifically silicone."
    - process_id: cutting_basic_v0
      fit: supporting
      reason: "Relevant to trimming belt stock to width and length before loop joining."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers fit checks for loop length, width, thickness, and pulley compatibility."
  abstraction_decision: substitute_process_family
  rationale: "The exact vendor belt standard is unknown, so closure should use a generic elastomer belt-loop forming path with reinforcement, pitch, and pulley fit left as guardrails."
  process_guardrails:
    tolerance: review
    surface_finish: belt_tooth_surface_review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: "closed-loop belt for transmitting motion between pulleys"
  material: rubber_with_unresolved_reinforcement
  scale_or_capacity:
    mass_kg: 0.00402
    bom_quantity: 3
    row_total_mass_kg: 0.01206
    scale_class: small
  geometry_form: small_closed_loop_belt_profile
merge_pool:
  eligible: true
  functional_purpose_key: motion_transmission
  precision_guardrails:
    - belt_pitch
    - tooth_profile
    - reinforcement_material
    - loop_length
    - pulley_compatibility
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - polymer_elastomer_forming_dispensing
  import_risk_factors:
    - "Exact belt standard, compound, reinforcement, pitch, tooth profile, and splice method are unresolved."
    - "Small drive belts may remain simpler as imported stock if local elastomer belt production is not already in scope."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this with other belts and pulley-drive components."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely candidate for a generic small rubber motion belt only if pitch and reinforcement guardrails converge."
assumptions:
  - "BOM quantity is 3, mass is 0.00402 kg per belt, and row total mass is 0.01206 kg."
  - "Rubber metadata is accepted as broad material evidence, while reinforcement is left unresolved."
  - "Adjacent pulley rows support interpreting the closed loop as a drive belt rather than a static gasket."
unresolved:
  - "Belt pitch, tooth geometry, compound, reinforcement material, splice method, vendor standard, and load rating are unknown."
  - "Whether this should merge with generic timing belts versus remain a stock import depends on pulley compatibility."
```
