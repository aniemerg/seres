---
row_identity:
  item: "1A51"
  cad_file: "1A51_seal"
  source_row_number: 7
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.lisema.eu/"
function:
  summary: "Thin rectangular frame seal/gasket for a small flat mating interface in the reAM250 1A-side assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A51_seal.step; research/ream250_bom/ream250_bom_row_0007_1A51__views_2x2.png; https://lisema.eu/"
    cited_fact_or_basis: "BOM row 7 states item 1A51, quantity 1, CAD file 1A51_seal, manufacturer LiSEMA, and link https://www.lisema.eu/. The manifest maps the row to gold_export/parts/1A51_seal.step as a matched vendor_component export. FreeCAD measured one solid with bounding box 92.00 x 62.00 x 3.00 mm. The rendered contact sheet shows a thin rectangular perimeter frame with rounded corner regions. LiSEMA's homepage identifies the company with custom gaskets, silicone profiles, silicone foam profiles, molded silicone parts, and seals."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name seal and thin closed-frame geometry are interpreted as a compressible gasket between mating faces, not as a structural spacer."
  uncertainty_notes:
    - "The BOM/CAD evidence does not identify the exact mating assembly, sealed medium, or compression requirement."
mass:
  value_kg: 0.0042
  basis: "Per-unit estimate for one physical seal. FreeCAD measured volume 3473.097 mm^3 = 0.000003473097 m^3. Using the representative silicone_rubber density of 1200 kg/m^3 from kb/materials/properties.yaml gives 0.0041677 kg, rounded to 0.0042 kg. BOM quantity is 1, so row total is also about 0.0042 kg. For sensitivity, the same CAD volume would be about 0.0038 kg at NBR density 1100 kg/m^3 or 0.0063 kg at FKM density 1800 kg/m^3 from the local table."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A51_seal.step; kb/materials/properties.yaml; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://lisema.eu/"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 3473.097 mm^3, area 4036.496 mm^2, and bounding box 92.00 x 62.00 x 3.00 mm. The local density table lists silicone_rubber at 1200 kg/m^3, NBR at 1100 kg/m^3, and FKM at 1800 kg/m^3. Assembly STEP material extraction for 1A51_seal returned only placeholder material Generic with density 1000.0. LiSEMA's homepage supports the row as a custom gasket/seal supplier but does not identify this row's mass or compound. targeted_web_search: queries tried: 'Lisema 1A51 seal', 'Lisema 1A51 Dichtung seal', 'site:lisema.eu 1A51 Lisema seal', and '1A51_seal material'; result: no row-specific public mass, drawing, or material source found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one seal."
    - "A representative solid silicone-rubber density is used as a planning constant because the row is a LiSEMA seal and exact compound is not resolved."
  uncertainty_notes:
    - "The CAD volume is row-specific, but the density is not; if the part is foam, NBR, EPDM, FKM, PTFE, or another gasket material, true mass may differ."
material:
  primary_material: "unknown elastomeric gasket or seal material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://lisema.eu/"
    cited_fact_or_basis: "BOM row 7 names the part 1A51_seal and manufacturer LiSEMA but leaves product ID and material fields blank. LiSEMA's homepage lists custom gaskets/seals and categories including silicone profiles, silicone foam profiles, flat gaskets, EPDM/NBR/CR rubber profiles, and FKM/Viton foam rubber products. Assembly STEP material extraction for product 1A51_seal returned only placeholder material Generic with density 1000.0. targeted_web_search: queries tried: 'Lisema 1A51 seal', 'Lisema 1A51 Dichtung seal', 'site:lisema.eu 1A51 Lisema seal', and '1A51_seal material'; result: no row-specific material grade, hardness, color, or datasheet found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The material is kept broad because the evidence supports a seal/gasket family but not a specific compound."
  uncertainty_notes:
    - "Exact compound, hardness, temperature rating, chemical compatibility, and compression-set behavior remain unresolved."
how_to_make:
  summary: "Cut or mold a 92 x 62 x 3 mm rectangular frame from the selected gasket/elastomer material and inspect fit and compression"
  manufacturing_steps:
    - "Select elastomeric gasket sheet, foam sheet, or molded seal compound according to the service temperature, atmosphere, compression, and chemical requirements."
    - "Cut the outer rectangle and central opening from 3 mm stock using die cutting, CNC knife cutting, waterjet cutting, or another material-compatible profile-cutting process."
    - "Form or finish rounded corner regions as required by the drawing, then clean edges and inspect the 92 x 62 x 3 mm profile."
    - "Prepare from LiSEMA or an equivalent gasket fabricator when certified compound, hardness, and compression performance are required"
  source:
    url_or_path: "https://lisema.eu/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A51_seal.step; research/ream250_bom/ream250_bom_row_0007_1A51__views_2x2.png"
    cited_fact_or_basis: "LiSEMA's homepage supports custom gaskets, profiles, molded silicone parts, and seals as supplied product categories. CAD and preview show one thin 92.00 x 62.00 x 3.00 mm rectangular frame seal. targeted_web_search: queries tried: 'Lisema 1A51 seal', 'Lisema 1A51 Dichtung seal', 'site:lisema.eu 1A51 Lisema seal', and '1A51_seal material'; result: no row-specific manufacturing drawing, compound, or process note found, so local cutting/molding steps are inferred from the seal geometry and vendor category."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row is treated as a replaceable custom gasket/seal rather than a calibrated module or multi-part assembly."
    - "Flat profile cutting is the preferred Manufacturing route unless a later drawing shows molded cross-section features that require tooling."
  uncertainty_notes:
    - "Without a row-specific drawing or material callout, the manufacturing route is suitable for planning but not enough to qualify the seal for vacuum, thermal, or chemical service."
kb_implications:
  - "item_granularity: simple_part - Model as one replaceable custom gasket/seal replaceable or applied part with dimensions and unknown LiSEMA elastomer material preserved in notes."
---

Research result for reAM250 BOM row 7.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0007_1A51.md
source_research_sha256: "e2f906195e696a1c90e58d984a6ed6a9569f43234f14a291485f8c7f9f04facf"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the gasket function, CAD-derived mass basis, unresolved elastomer evidence, cut/molded seal route, KB implications, and CAD preview before conversion."
decomposition:
  decision: simple_part
  rationale: "The row is one replaceable rectangular frame gasket. It should stay a simple seal item while compound, hardness, and compression requirements remain guardrails."
  proposed_subparts: []
process_abstraction:
  original_process_family: elastomer_gasket_profile_cutting
  primary_process_bucket: polymer_elastomer_forming_dispensing
  supporting_processes:
    - cutting
    - elastomer_forming
    - cleaning
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: gasket_sheet_cut_to_part_v0
      fit: direct
      reason: "Covers cutting gasket sheet into a profile part matching this flat frame geometry."
    - process_id: seal_installation_v0
      fit: supporting
      reason: "Relevant when the gasket is installed into the mating interface."
    - process_id: sealing_and_assembly_basic_v0
      fit: supporting
      reason: "Covers sealed assembly handling and cleanliness checks."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers profile, thickness, continuity, and fit checks."
  abstraction_decision: keep_original_family
  rationale: "The row evidence points to a custom elastomer gasket made by profile cutting with possible molding; this matches the polymer/elastomer forming and dispensing bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: not_applicable
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: seal a small flat mating interface with a replaceable frame gasket
  material: unknown_elastomer
  scale_or_capacity:
    mass_kg: 0.0042
    bom_quantity: 1
    row_total_mass_kg: 0.0042
    scale_class: tiny
  geometry_form: thin_rectangular_frame_gasket
merge_pool:
  eligible: true
  functional_purpose_key: joint_sealing
  precision_guardrails:
    - gasket_thickness
    - compression_set
    - chemical_compatibility
    - temperature_rating
    - profile_fit
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - polymer_elastomer_forming_dispensing
  import_risk_factors:
    - "Exact elastomer compound, hardness, compression-set behavior, temperature rating, and chemical compatibility are unresolved."
    - "Certified gasket performance may require imported compound sheet if local elastomer formulation is outside current scope."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review groups this with other gasket and seal rows."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely reusable custom frame gasket family with material-specific variants."
assumptions:
  - "The CAD solid represents one physical gasket with applied planning mass 0.0042 kg."
  - "Silicone-rubber density is a planning proxy only; final material remains unresolved."
  - "A cut gasket route is acceptable unless later drawings show molded cross-section features."
unresolved:
  - "Exact elastomer compound, hardness, compression requirement, sealed medium, service temperature, and chemical exposure are not resolved by row evidence."
```
