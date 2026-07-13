---
row_identity:
  item: "1A42"
  cad_file: "1A42_flange_schlieren_imaging"
  source_row_number: 6
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom schlieren-imaging flange or optical interface bracket for the reAM250 1A-side schlieren imaging assembly; CAD shows a bolted rectangular flange face with a protruding cylindrical/conical optical tube feature."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A42_flange_schlieren_imaging.step; research/ream250_bom/ream250_bom_row_0006_1A42__views_2x2.png"
    cited_fact_or_basis: "BOM row 6 states item 1A42, quantity 1, CAD file 1A42_flange_schlieren_imaging. The manifest maps the row to gold_export/parts/1A42_flange_schlieren_imaging.step as a matched part export. FreeCAD measured one solid with bounding box 80.00 x 114.40 x 160.00 mm. The rendered contact sheet shows a rectangular bolted frame/flange face and an angled cylindrical/conical tube feature."
    evidence_basis: "bom_provided"
  assumptions:
    - "The name flange_schlieren_imaging and visible tube/flange geometry are interpreted as an optical mount or interface for the schlieren imaging path."
  uncertainty_notes:
    - "The BOM/CAD evidence identifies the local mechanical role, but not the exact mating optic, adapter, or sealing interface."
mass:
  value_kg: 0.39
  basis: "FreeCAD volume 144446.714 mm^3 equals 0.000144447 m^3. Nominal value uses aluminum density 2700 kg/m^3 from kb/materials/properties.yaml, giving 0.390 kg. If the same CAD volume were generic steel at 7850 kg/m^3, mass would be about 1.13 kg; stainless steel at 8000 kg/m^3 would be about 1.16 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A42_flange_schlieren_imaging.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 144446.714 mm^3, area 51677.320 mm^2, and bounding box 80.00 x 114.40 x 160.00 mm. The local density table lists aluminum density 2700 kg/m^3, steel density 7850 kg/m^3, and stainless_steel density 8000 kg/m^3. targeted_web_search: searched \"1A42_flange_schlieren_imaging material\", \"1A42 flange schlieren imaging material\", \"reAM250 1A42 schlieren\", and \"ream250 flange_schlieren_imaging\"; found duplicate BOM text and general schlieren references but no row-specific mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one manufactured part."
    - "Aluminum is used as the nominal scenario because optical mounts and custom machine brackets are commonly aluminum, and the part geometry is a lightened custom flange rather than a heavy vacuum clamp."
  uncertainty_notes:
    - "Mass depends directly on unresolved material; use 0.39 kg as an aluminum-scenario estimate, with steel or stainless construction around 1.1-1.2 kg."
material:
  primary_material: "unknown structural metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A42_flange_schlieren_imaging.step"
    cited_fact_or_basis: "BOM row 6 has blank material fields. The assembly STEP material extractor matched 1A42_flange_schlieren_imaging but returned material Generic and density 1000.0, which the task workflow treats as placeholder rather than resolved material evidence. CAD geometry is a bolted flange/tube mechanical bracket. targeted_web_search: searched \"1A42_flange_schlieren_imaging material\", \"1A42 flange schlieren imaging material\", \"reAM250 1A42 schlieren\", and \"ream250 flange_schlieren_imaging\"; found duplicate BOM text and general schlieren references but no row-specific material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A structural metal/alloy family is inferred from the flange/bracket role, bolted rectangular face, optical tube feature, and machine-frame context."
  uncertainty_notes:
    - "The specific alloy or grade is not identified; aluminum alloy is plausible for an optical bracket, while steel or stainless steel remain possible if stiffness, vacuum, or thermal requirements dominate."
how_to_make:
  summary: "Fabricate as a machined metal optical flange/bracket from the resolved alloy, using CNC milling/boring for the flange face, bolt pattern, angled tube feature, and mating surfaces."
  manufacturing_steps:
    - "Select structural metal billet, thick plate, or near-net blank in the resolved alloy."
    - "CNC mill the rectangular flange/frame outline, bolt holes, and lightening or relief features visible on the face."
    - "Bore or machine the cylindrical/conical optical tube feature and its angled transition to the flange body."
    - "Finish-machine optical or sealing mating faces, then deburr and inspect hole positions, flatness, and tube alignment."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A42_flange_schlieren_imaging.step; research/ream250_bom/ream250_bom_row_0006_1A42__views_2x2.png"
    cited_fact_or_basis: "CAD and preview show one 80.00 x 114.40 x 160.00 mm solid with a rectangular bolted flange/frame, diagonal/lightened face members, and a protruding cylindrical/conical tube feature. targeted_web_search: searched \"1A42_flange_schlieren_imaging material\", \"1A42 flange schlieren imaging material\", \"reAM250 1A42 schlieren\", and \"ream250 flange_schlieren_imaging\" no row-specific manufacturing drawing, material callout, or process note was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a custom machined simple part because the BOM row has no manufacturer/product ID and the CAD name is a custom assembly-specific flange"
    - "Subtractive machining is assumed from the visible flange/tube geometry and expected need for accurate optical alignment or mating surfaces."
  uncertainty_notes:
    - "The CAD/BOM evidence does not specify tolerances, surface finish, coating/anodizing, or whether the tube feature is machined from one piece or joined from a separate tube."
kb_implications:
  - "item_granularity: simple_part - custom structural/optical flange likely modeled as one machined metal part, with material grade unresolved until a drawing or designer note identifies it."
---

Research result for reAM250 BOM row 6.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0006_1A42.md
source_research_sha256: 1e2d56174dbaaa5dfdefd64f5f9ff8248d511fe14a4f22eff270269b5a95b567
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Reviewed the schlieren-imaging flange function, CAD-volume mass estimate, unresolved structural-metal material
    evidence, inferred CNC machining route, KB implication, and CAD preview showing a bolted rectangular optical interface
    with a protruding tube feature.
decomposition:
  decision: simple_part
  rationale: The row is a single custom mechanical flange and optical interface bracket with no internal vendor module,
    electronics package, optics package, and fastener set to expose during row conversion.
  proposed_subparts: []
process_abstraction:
  original_process_family: cnc_milling_boring
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
  - stock_preparation
  - precision_machining
  - drilling
  - deburring
  - surface_finishing
  - dimensional_inspection
  candidate_existing_processes:
  - process_id: machining_basic_v0
    fit: partial
    reason: Covers general stock removal for a custom metal bracket, but the optical tube and mating features need more
      specific finish and alignment guardrails.
  - process_id: machining_precision_v0
    fit: supporting
    reason: Relevant where flange flatness, bore geometry, tube alignment, and optical-interface surfaces require tighter
      machining than basic bracket work.
  - process_id: machining_process_boring_v0
    fit: supporting
    reason: Relevant to the cylindrical/conical tube feature and any controlled optical bore.
  - process_id: drilling_basic_v0
    fit: supporting
    reason: Covers the bolted rectangular flange hole pattern.
  - process_id: surface_finishing_v0
    fit: supporting
    reason: Covers deburring and finish work on mating, optical, and possible sealing surfaces.
  - process_id: inspection_basic_v0
    fit: supporting
    reason: Covers dimensional checks before later staging selects a final recipe.
  abstraction_decision: keep_original_family
  rationale: The original route is already a CNC milling and boring route for a non-sheet custom flange/tube geometry, so
    the shared subtractive machining bucket is the simplest compatible closure handle.
  process_guardrails:
    tolerance: review flange flatness, bolt pattern, bore geometry, and tube alignment against the schlieren optical path
    surface_finish: review mating, optical-interface, and possible sealing faces; deburr all machined edges
    sealing_quality: review because the exact mating adapter and chamber interface are not identified
    alignment_accuracy: optical tube axis and flange face alignment may be function-critical
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: mount and interface the schlieren imaging path to the machine through a bolted optical flange
  material: unknown_structural_metal_alloy
  scale_or_capacity:
    mass_kg: 0.39
    bom_quantity: 1
    row_total_mass_kg: 0.39
    scale_class: small
  geometry_form: machined_rectangular_flange_with_protruding_optical_tube
merge_pool:
  eligible: true
  functional_purpose_key: optical_interface_mount
  precision_guardrails:
  - optical_axis_alignment
  - flange_flatness
  - bolt_hole_pattern
  - bore_geometry
  - possible_sealing_surface
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - general_subtractive_machining
  import_risk_factors:
  - Exact alloy is unresolved, so aluminum, steel, and stainless assumptions change mass and thermal behavior.
  - The optical alignment and possible sealing requirements are not specified by the row evidence.
  post_merge_decision_notes: Final import/local decision is deferred until merge review compares this with other optical
    mounts, interface flanges, and chamber adapter brackets.
kb_staging:
  proposed_item_id: null
  notes: Leave final item ID open for merge review; this may converge with other machined optical interface mounts if
    material and alignment guardrails are compatible.
assumptions:
- The STEP solid represents the complete per-unit row item and excludes separate optics, seals, and fasteners.
- Aluminum alloy is plausible for mass planning, but the conversion keeps the material broad because the evidence does
  not resolve alloy grade.
- Subtractive machining remains the primary closure abstraction because the geometry is not a simple flat plate plus stock
  profile.
unresolved:
- Exact material grade, surface treatment, tolerances, and surface finish are unknown.
- The mating optic, adapter, seal, and chamber interface served by the tube/flange feature are not identified.
- It is unclear whether the protruding tube is truly one-piece with the flange rather than a joined feature in production.
```
