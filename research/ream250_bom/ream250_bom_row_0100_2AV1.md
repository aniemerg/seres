---
row_identity:
  item: "2AV1"
  cad_file: "2AV1_DIN 912 - M5x0,8x30x22"
  source_row_number: 100
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "DIN 912 M5 x 0.8 x 30 cylinder-head/socket-head cap screw used as standard fastening hardware in the reAM250 assembly; BOM quantity is 10."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV1_DIN 912 - M5x0,8x30x22.step; research/ream250_bom/ream250_bom_row_0100_2AV1__views_2x2.png"
    cited_fact_or_basis: "BOM row 100 lists item 2AV1, quantity 10, CAD file '2AV1_DIN 912 - M5x0,8x30x22', and description 'cylinder head cap screw'. The manifest maps the row to the matched part STEP. FreeCAD measured one solid with a 35.00 x 9.20 x 9.20 mm bounding box, and the rendered preview shows a socket-head screw form with a cylindrical shank/threaded end and larger head."
    evidence_basis: "bom_provided"
  assumptions:
    - "The DIN 912 designation is interpreted as the standard socket-head cap screw form represented by the row's CAD and description."
  uncertainty_notes:
    - "The row does not expose the mating part or exact fastening location, so the function is limited to standard mechanical fastening hardware."
mass:
  value_kg: 0.0065
  basis: "Per unit. BOM quantity is 10, so the row total is about 0.0650 kg. FreeCAD measured CAD volume 827.865 mm^3 = 0.000000827865 m^3. Assembly STEP metadata reports Steel, Mild with density 7850 kg/m^3; computed mass = 0.000000827865 m^3 * 7850 kg/m^3 = 0.006499 kg per screw, rounded to 0.0065 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV1_DIN 912 - M5x0,8x30x22.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 827.865 mm^3, area 744.656 mm^2, and bounding box 35.00 x 9.20 x 9.20 mm. The local assembly STEP material extractor matched product '2AV1_DIN 912 - M5x0,8x30x22' to material Steel, Mild with density 7850.0. The local density table lists steel density_kg_per_m3: 7850."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the finished physical volume for one screw."
    - "The assembly STEP density is interpreted as kg/m^3-like density, consistent with the local extractor note for this reAM250 export."
  uncertainty_notes:
    - "The CAD-derived mass may differ from catalog screw weight if the thread model, socket recess, or head detail is simplified, but the estimate is adequate for BOM-level mass accounting."
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product '2AV1_DIN 912 - M5x0,8x30x22' to material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local material metadata gives a steel family but not a property class, coating, strength grade, or heat treatment."
how_to_make:
  summary: "Prepare as a standard DIN 912 M5 x 0.8 x 30 mild-steel socket-head cap screw; for assembly, specify the standard designation, draw from locally manufactured standard hardware stock, inspect the thread/head fit, and install as one of the ten row fasteners"
  manufacturing_steps:
    - "Specify DIN 912 M5 x 0.8 x 30 cylinder-head/socket-head cap screw, compatible with the row CAD envelope and mild-steel material metadata."
    - "Machine-specific custom part"
    - "On receipt or before assembly, verify thread size, screw length, head/socket form, and material/coating requirements against the assembly need."
    - "Install as standard reusable fastening hardware in the relevant reAM250 subassembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV1_DIN 912 - M5x0,8x30x22.step; research/ream250_bom/ream250_bom_row_0100_2AV1__views_2x2.png"
    cited_fact_or_basis: "The BOM row names a DIN 912 M5 x 0.8 x 30 cylinder head cap screw, and the CAD preview/STEP geometry show the corresponding socket-head screw shape with a 35.00 mm overall CAD envelope along the screw axis. The route is a procurement/standard-hardware-stock route, not a claimed screw factory manufacturing process."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "If local screw manufacture is later modeled, the production process would need separate evidence for heading, socket forming, thread rolling, heat treatment, and coating; those operations are not specified by this row."
kb_implications:
  - "item_granularity: simple_part - model as reusable standard M5 DIN 912 steel screw hardware, not as a purchased module or machine-specific custom assembly."
---

Research result for reAM250 BOM row 100.
