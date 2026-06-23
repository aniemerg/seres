---
row_identity:
  item: "63"
  cad_file: "63_retaining_ring_DIN 471 - 5x0,6"
  source_row_number: 269
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small DIN 471 external retaining ring for a 5 mm shaft/groove interface; it acts as a removable axial shoulder to retain a mating component on a shaft."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/63_retaining_ring_DIN 471 - 5x0,6.step; research/ream250_bom/ream250_bom_row_0269_63__views_2x2.png"
    cited_fact_or_basis: "BOM row 269 lists item 63, quantity 1, CAD file '63_retaining_ring_DIN 471 - 5x0,6', and description 'spring retaining ring'. The manifest maps the same row to a matched part STEP. FreeCAD measured one solid with a 6.65 x 8.45 x 0.60 mm bounding box, and the rendered preview shows a thin split external circlip with lug holes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The DIN 471 - 5x0,6 text is interpreted as the standard external shaft retaining-ring designation and nominal size."
  uncertainty_notes: []
mass:
  value_kg: 0.0000971
  basis: "FreeCAD volume 12.365 mm^3 equals 1.2365e-8 m^3. Assembly STEP material metadata reports Steel, Mild with density 7850 kg/m^3 for this product, giving 1.2365e-8 m^3 * 7850 kg/m^3 = 0.0000971 kg per retaining ring. BOM quantity is 1, so the row total is also about 0.0000971 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/63_retaining_ring_DIN 471 - 5x0,6.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 12.365 mm^3, area 67.203 mm^2, and bounding box 6.65 x 8.45 x 0.60 mm. The local STEP material extractor matched product 63_retaining_ring_DIN 471 - 5x0,6 and reported material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP volume is treated as the complete solid volume for one physical retaining ring."
    - "The STEP density is used as the calculation constant for the row-level mass estimate."
  uncertainty_notes:
    - "The CAD-derived value is very small and sensitive to whether the STEP geometry includes every edge radius/chamfer, but it is appropriate for BOM-scale mass accounting."
material:
  primary_material: "steel family; local STEP metadata labels the row material as Steel, Mild, while DIN 471 retaining rings are commonly spring-steel hardware"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://ametric.com/Images/document/RetainingRings-Metric.pdf; https://www.fastenermart.com/din-471-external-retaining-rings.html"
    cited_fact_or_basis: "The local STEP material extractor reports Steel, Mild and density 7850.0 for the row product. Ametric's DIN 471 retaining-ring catalog table lists hardened spring steel C60-DIN/AISI 1060 with phosphate finish for external retaining rings, and Fastener Mart describes DIN 471 as external retaining rings for shafts."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "For KB planning, model this as steel-family retaining-ring hardware rather than encoding mild steel as a functional spring grade."
  uncertainty_notes:
    - "The row-specific CAD metadata gives a steel family but may be a generic CAD material assignment; exact grade, heat treatment, and finish are not resolved for this specific BOM row."
how_to_make:
  summary: "Procure as a standard DIN 471 external retaining ring; a plausible local route is blanking/stamping the ring profile from spring-steel strip, heat treating if not supplied pre-hardened, finishing/coating, and inspecting shaft-groove fit."
  manufacturing_steps:
    - "Select steel strip or spring-steel stock at about 0.6 mm thickness for the small DIN 471 ring size."
    - "Blank or stamp the split-ring outline, lug ends, and plier holes."
    - "Deburr edges and heat treat or stress relieve as needed for spring retention behavior."
    - "Apply a corrosion-protection finish if required, then inspect free shape, thickness, lug holes, and fit in the mating shaft groove."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0269_63__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/63_retaining_ring_DIN 471 - 5x0,6.step; https://www.huyett.com/dsh-010-zc; https://ametric.com/Images/document/RetainingRings-Metric.pdf"
    cited_fact_or_basis: "The CAD preview shows a thin stamped-looking split retaining ring with lug holes. Huyett's DIN 471 snap-ring page for the same family lists Type: Snap Rings External, material Carbon Spring Steel, and Style: Stamped. Ametric's DIN 471 table lists hardened spring steel for external retaining rings. targeted_web_search: searched 'DIN 471 retaining ring 5 x 0.6 material spring steel stainless steel', 'DIN 471 external retaining ring function shaft groove spring steel', and 'DIN 471 retaining ring manufacturing stamped spring steel'; results resolved standard retaining-ring function, common material family, and a stamped style for comparable DIN 471 rings, but did not provide a row-specific factory process for this exact reAM250 item."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local manufacturing route is inferred from the standard ring geometry, thin sheet/strip thickness, and comparable catalog description of DIN 471 rings as stamped external snap rings."
    - "Procurement is the near-term route because this is standard small hardware."
  uncertainty_notes:
    - "The cited sources do not specify the actual supplier or process used for the reAM250 row, so heat treatment and finish remain planning assumptions."
kb_implications:
  - "item_granularity: simple_part - standard small external retaining-ring hardware; later KB modeling should reuse or parameterize a generic DIN 471 steel retaining ring rather than create a machine-specific custom part."
---

Research result for reAM250 BOM row 269.
