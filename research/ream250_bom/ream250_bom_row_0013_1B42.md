---
row_identity:
  item: "1B42"
  cad_file: "1B42_seal"
  source_row_number: 13
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.lisema.eu/"
function:
  summary: "Thin rectangular frame seal/gasket, probably used as a compressible perimeter seal between two flat mating faces in the reAM250 optical/chamber door area."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B42_seal.step; research/ream250_bom/ream250_bom_row_0013_1B42__views_2x2.png; https://lisema.eu/Flachdichtungen"
    cited_fact_or_basis: "BOM row 13 names item 1B42 as 1B42_seal from LiSEMA with quantity 2; CAD is one 210.00 x 297.00 x 3.00 mm solid, volume 11976.000 mm^3, rendered as a thin rectangular frame with a large central opening; LiSEMA's flat-gasket page describes custom flat gaskets."
    evidence_basis: "bom_provided"
  assumptions:
    - "The file name and flat frame geometry indicate a gasket/seal rather than a structural spacer."
  uncertainty_notes:
    - "The row does not state the mating interface or exact subsystem, so the specific sealed medium and compression requirement are not resolved."
mass:
  value_kg: 0.0144
  basis: "Per-unit estimate for one seal. FreeCAD measured volume 11976.000 mm^3 = 0.000011976 m^3. Using a representative silicone-rubber density of 1200 kg/m^3 from kb/materials/properties.yaml gives 0.0143712 kg per seal. BOM quantity is 2, so the row total would be about 0.0287 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B42_seal.step; kb/materials/properties.yaml; https://lisema.eu/Werkstoffe; https://lisema.eu/Flachdichtungen"
    cited_fact_or_basis: "FreeCAD measured volume 11976.000 mm^3; local density table lists silicone_rubber at 1200 kg/m^3; LiSEMA material pages show flat gaskets are supplied from multiple gasket/elastomer families but do not identify the 1B42 compound. targeted_web_search: queries tried: 'Lisema 1B42 seal', 'Lisema 1B42 Dichtung seal', 'site:lisema.eu 1B42 seal Lisema'; result: no row-specific public mass or exact material source found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Representative solid silicone density is used as a planning estimate because the STEP material metadata is Generic at density 1000.0 and the BOM row gives no compound."
  uncertainty_notes:
    - "If this seal is foam, PTFE, fiber, graphite, FKM, or another LiSEMA flat-gasket material, true mass could differ substantially; CAD volume is row-specific but density is not."
material:
  primary_material: "unknown LiSEMA flat-gasket material; plausible family is elastomeric or gasket-sheet stock such as silicone, silicone foam, EPDM, NBR, CR, FKM/Viton, PTFE, PU, PVC/PMMA, graphite, fiber, or mica-based gasket material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://lisema.eu/Flachdichtungen; https://lisema.eu/Werkstoffe; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row gives manufacturer LiSEMA and item name 1B42_seal; LiSEMA's flat-gasket and materials pages list many possible supplied gasket materials; assembly STEP material extraction for product 1B42_seal returned only placeholder Generic with density 1000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Exact compound, hardness, color, certification, and temperature rating are not in the BOM row, CAD metadata, or public row-specific search results."
how_to_make:
  summary: "Cut the rectangular frame from selected gasket sheet or elastomer stock and inspect thickness, perimeter, and compression fit"
  manufacturing_steps:
    - "Select gasket sheet or elastomer stock matching the service temperature, atmosphere, compression set, and chemical compatibility requirements."
    - "Cut the outside rectangle and central window from 3 mm sheet using die cutting, waterjet/knife cutting, CNC routing, or laser where compatible with the selected material."
    - "Deburr or clean cut edges if needed, then inspect overall 210 x 297 x 3 mm geometry and trial-fit between mating faces."
    - "Prepare from LiSEMA or an equivalent gasket fabricator when exact compound and compression performance must be guaranteed"
  source:
    url_or_path: "https://lisema.eu/Flachdichtungen; https://lisema.eu/Flachdichtungskonfigurator; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B42_seal.step"
    cited_fact_or_basis: "LiSEMA pages support custom flat-gasket supply/configuration and multiple flat-gasket material choices; CAD supplies the 210 x 297 x 3 mm rectangular-frame geometry. targeted_web_search: queries tried: 'Lisema 1B42 seal', 'Lisema 1B42 Dichtung seal', 'site:lisema.eu 1B42 seal Lisema'; result: no row-specific manufacturing drawing or compound found, so local cutting steps are inferred from the flat sheet gasket geometry."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row can be modeled as a replaceable flat gasket cut from sheet stock rather than a molded multi-part seal."
  uncertainty_notes: []
kb_implications:
  - "item_granularity: simple_part - Model as one replaceable custom flat gasket/seal replaceable or applied part; preserve dimensions, quantity 2, and unknown LiSEMA material family in notes rather than decomposing into subparts."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0013_1B42.md
source_research_sha256: "04450f10c7de07b6bf5b59e30d2b7f5dce976288596009e03fae27c7817a856d"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed flat gasket function, silicone-density planning mass and row total, unresolved LiSEMA material family, sheet-cutting route, and CAD preview showing a thin rectangular frame with central opening."
decomposition:
  decision: simple_part
  rationale: "The row is a single-piece flat gasket repeated twice, with no internal module structure."
  proposed_subparts: []
process_abstraction:
  original_process_family: gasket_sheet_cutting
  primary_process_bucket: polymer_elastomer_forming_dispensing
  supporting_processes:
    - elastomer_forming
    - cutting
    - deburring
    - cleaning
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: gasket_sheet_cut_to_part_v0
      fit: direct
      reason: "Directly matches cutting gasket sheet into a flat gasket part."
    - process_id: gasket_sheet_material_extrusion_v0
      fit: supporting
      reason: "Relevant upstream process if local closure includes making polymer gasket sheet stock."
    - process_id: seal_installation_v0
      fit: supporting
      reason: "Relevant downstream process for installing the finished gasket between mating faces."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional and fit checks for thickness, perimeter, and central opening."
  abstraction_decision: substitute_process_family
  rationale: "The row-specific route is flat gasket cutting, but the closure handle should group it with polymer/elastomer gasket stock preparation and shaping."
  process_guardrails:
    tolerance: review
    surface_finish: low
    sealing_quality: high
    alignment_accuracy: low
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: compressible perimeter seal between flat mating faces
  material: gasket_elastomer_material_unresolved
  scale_or_capacity:
    mass_kg: 0.0144
    bom_quantity: 2
    row_total_mass_kg: 0.0287
    scale_class: small
  geometry_form: flat_rectangular_frame_gasket_210x297x3mm
merge_pool:
  eligible: true
  functional_purpose_key: interface_sealing
  precision_guardrails:
    - compression_set
    - thickness
    - perimeter_geometry
    - material_compatibility
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - polymer_elastomer_forming_dispensing
  import_risk_factors:
    - "Exact gasket compound, hardness, temperature rating, and chemical compatibility are unresolved."
    - "Seal performance may depend on material properties not available in the row evidence."
  post_merge_decision_notes: "Final import/local decision is deferred until after merge review; compare with other flat gasket and interface-sealing rows before assigning a closure item."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely reusable as a custom flat gasket family if material and compression guardrails can be unified."
assumptions:
  - "Representative silicone rubber density is retained only for mass scale because exact compound is unknown."
  - "The gasket is modeled as cut sheet stock rather than a molded multi-part seal."
  - "The sealed medium is not used as a merge-key axis because the row evidence does not identify it."
unresolved:
  - "Exact material compound, hardness, compression set, temperature rating, color, certification, and sealed medium remain unknown."
```
