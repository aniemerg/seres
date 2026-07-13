---
row_identity:
  item: "6G"
  cad_file: "6G_powder_container_extension_front"
  source_row_number: 181
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Single front-side extension plate for the reAM250 recoater powder-container assembly, likely extending or closing the front powder-container edge near the adjacent back extensions, powder chute, seal, and clamping-plate rows."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6G_powder_container_extension_front.step; research/ream250_bom/ream250_bom_row_0181_6G__views_2x2.png"
    cited_fact_or_basis: "BOM row 181 lists item 6G, quantity 1, CAD file 6G_powder_container_extension_front. Manifest row 181 maps it to a matched existing part STEP. Neighboring BOM rows name powder-container back extensions, a powder chute, top seal, bottom brush seal, and front/back clamping plates. FreeCAD measured one solid with bounding box 37.75 x 118.50 x 3.00 mm, and the rendered preview shows a thin asymmetric plate or faceted extension piece."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name and neighboring powder-container rows are interpreted as the local assembly context for this front extension plate."
  uncertainty_notes:
    - "The BOM and STEP do not expose mating constraints, so the exact front-edge interface and whether the part primarily acts as a spacer, wall extension, or retaining lip remain inferred."
mass:
  value_kg: 0.0287
  basis: "Per-unit estimate for one physical 6G extension. FreeCAD volume is 10632.268 mm^3 = 1.0632268e-5 m^3. Assembly STEP material metadata gives Aluminum 6061 density 2700 kg/m^3, so computed mass is 1.0632268e-5 m^3 * 2700 kg/m^3 = 0.02871 kg per unit. BOM quantity is 1, so the row total is also about 0.0287 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6G_powder_container_extension_front.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 10632.268 mm^3, area 8069.065 mm^2, and bounding box 37.75 x 118.50 x 3.00 mm. Local assembly STEP material extraction matched product 6G_powder_container_extension_front to material Aluminum 6061 with density 2700.0. kb/materials/properties.yaml lists aluminum density 2700 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the finished volume of one extension plate."
    - "The assembly STEP density value is interpreted as kg/m^3-like density, consistent with the local extractor note for this reAM250 export."
  uncertainty_notes:
    - "Mass excludes any separate fasteners, seals, adhesive, or neighboring powder-container pieces that are separate BOM rows."
material:
  primary_material: "Aluminum 6061"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product 6G_powder_container_extension_front to material Aluminum 6061 with density 2700.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local metadata gives the alloy family/grade but not temper, surface treatment, or finish."
how_to_make:
  summary: "Make as a custom Aluminum 6061 powder-container extension plate: cut or mill the thin profile from 3 mm aluminum stock, machine the asymmetric edges and relief geometry, deburr, clean, and inspect fit against the powder-container front assembly."
  manufacturing_steps:
    - "Start from Aluminum 6061 sheet or plate stock near the 3.00 mm finished thickness."
    - "CNC profile-cut or mill the asymmetric outline and any edge reliefs shown by the STEP geometry."
    - "Machine shallow face/rib geometry if the STEP features are not achievable by simple cutting alone."
    - "Deburr and clean all powder-contact or assembly-contact edges."
    - "Inspect thickness, outline, and fit against the front powder-container extension location."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6G_powder_container_extension_front.step; research/ream250_bom/ream250_bom_row_0181_6G__views_2x2.png"
    cited_fact_or_basis: "The STEP geometry is one thin Aluminum 6061 solid with a 37.75 x 118.50 x 3.00 mm envelope; the rendered contact sheet shows an asymmetric flat/faceted extension plate without purchased-module features. targeted_web_search: tried '\"6G_powder_container_extension_front\"', '\"reAM250\" \"powder container\" extension front aluminum 6061', and '\"6G_powder_container_extension_front\" material'; results only duplicated BOM row identity or generic Aluminum 6061 pages, with no row-specific fabrication drawing or manufacturing-process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "CNC cutting/milling from 3 mm Aluminum 6061 stock is the most plausible Manufacturing route for the observed one-piece thin plate geometry."
    - "Powder-container service requires clean, deburred edges to reduce powder hangups and contamination."
  uncertainty_notes:
    - "No row-specific drawing was found, so bend radii, flatness, tolerances, fastener interfaces, and surface-finish requirements remain unresolved."
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable custom Aluminum 6061 thin plate/extension piece for the powder-container assembly, not as a purchased module."
---

Research result for the leased reAM250 BOM row only.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0181_6G.md
source_research_sha256: "a79e80eaa5939900a8d28617aeaa896fbdf090ada97ef8259c550e3290156d8e"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the powder-container extension function, CAD-derived mass basis, Aluminum 6061 material metadata, thin-plate machining route, KB implication, and CAD preview showing a small asymmetric faceted plate."
decomposition:
  decision: simple_part
  rationale: "The row is one thin aluminum extension plate in the powder-container assembly and has no internal module dependencies."
  proposed_subparts: []
process_abstraction:
  original_process_family: aluminum_sheet_plate_profile_cutting
  primary_process_bucket: sheet_plate_cutting_drilling
  supporting_processes:
    - stock_preparation
    - cutting
    - precision_machining
    - deburring
    - cleaning
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: sheet_metal_cutting_v0
      fit: partial
      reason: "Covers the thin profile cutting, though this aluminum plate has local asymmetric relief geometry."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Relevant to faceted edges and shallow features after profile cutting."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Useful if powder-container fit, flatness, and edge geometry need tighter control."
    - process_id: cleaning_basic_v0
      fit: supporting
      reason: "Supports powder-contact cleanliness after cutting and deburring."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers thickness, outline, and fit inspection."
  abstraction_decision: keep_original_family
  rationale: "The inferred source route is already sheet/plate cutting with local machining; the canonical plate bucket is appropriate for this shallow powder-container part."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: powder-container edge extension and local containment surface
  material: aluminum_6061
  scale_or_capacity:
    mass_kg: 0.0287
    bom_quantity: 1
    row_total_mass_kg: 0.0287
    scale_class: tiny
  geometry_form: small_asymmetric_three_mm_aluminum_plate_with_faceted_edge_relief
merge_pool:
  eligible: true
  functional_purpose_key: powder_containment
  precision_guardrails:
    - powder_contact_surface_finish
    - edge_relief_geometry
    - front_container_fit
    - flatness
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - sheet_plate_cutting_drilling
  import_risk_factors:
    - "Powder-contact finish and fit against neighboring seals and clamp plates are unresolved."
    - "Small geometry is locally manufacturable, but exact tolerance and surface treatment are unknown."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares powder-container extension, chute, and clamping plate rows."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely candidate for a generic small aluminum powder-containment plate if surface and fit guardrails align."
assumptions:
  - "The front placement label is assembly context and should not by itself create a unique closure item."
  - "Aluminum 6061 metadata from the assembly STEP is accepted for row-level staging."
unresolved:
  - "Exact mating interfaces, flatness, surface finish, coating, fastener method, and powder-cleanliness requirement remain unresolved."
```
