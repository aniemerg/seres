---
row_identity:
  item: "65"
  cad_file: "65_retaining_ring_DIN 471 - 10x1"
  source_row_number: 271
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "External DIN 471 retaining ring for a 10 mm shaft groove; it forms a removable axial shoulder that retains a nearby component on a shaft."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/65_retaining_ring_DIN 471 - 10x1.step; research/ream250_bom/ream250_bom_row_0271_65__views_2x2.png; https://www.fastenermart.com/din-471-external-retaining-rings.html"
    cited_fact_or_basis: "BOM row 271 states item 65, quantity 1, CAD file 65_retaining_ring_DIN 471 - 10x1, and description spring retaining ring. The manifest maps the row to gold_export/parts/65_retaining_ring_DIN 471 - 10x1.step as a matched part export. FreeCAD measured one solid with bounding box 12.70 x 14.89 x 1.00 mm. The rendered contact sheet shows a split retaining ring with lug holes. Fastener Mart describes DIN 471 external retaining rings as shaft rings installed into a machined groove to create a removable shoulder retaining components."
    evidence_basis: "bom_provided"
  assumptions:
    - "The DIN 471 - 10x1 designation is interpreted as the normal external retaining-ring standard size for a 10 mm shaft and 1 mm ring thickness."
  uncertainty_notes:
    - "The exact shaft, groove, or retained component in the reAM250 assembly is not identified by this row."
mass:
  value_kg: 0.000482
  basis: "FreeCAD volume 61.453 mm^3 equals 0.000000061453 m^3. Row-specific assembly STEP material extraction returned Steel, Mild with density 7850 kg/m^3, giving 0.000482 kg, about 0.482 g, for one ring. BOM quantity is 1, so row total is also about 0.000482 kg. DIN 471 catalog tables cross-check this order of magnitude with 10 mm nominal weights around 0.34-0.42 g per ring."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/65_retaining_ring_DIN 471 - 10x1.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml; https://www.beneri.com/en/prodotto/din-471; https://www.fasteners.eu/standards/din/471/"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 61.453 mm^3, area 211.265 mm^2, and bounding box 12.70 x 14.89 x 1.00 mm. The local assembly STEP material extractor matched this product name to material Steel, Mild and density 7850.0. The local density table lists steel density 7850 kg/m^3. Beneri and Fasteners.eu DIN 471 tables list 10 mm retaining-ring weights in kg per 1000 pieces as an external cross-check."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume represents one physical retaining ring."
    - "The extracted STEP density is used as the density for the whole one-piece ring."
  uncertainty_notes:
    - "The CAD-derived mass is about 15-40 percent higher than the checked DIN 471 catalog weights for a 10 mm ring, so use it as a row-specific estimate rather than a catalog-standard exact mass."
material:
  primary_material: "Steel, Mild"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.fasteners.eu/standards/din/471/; https://www.keller-kalmbach.com/products/fasteners/safety-elements/retaining-rings-and-washers/din-471-circlip/p/10047110"
    cited_fact_or_basis: "The local assembly STEP material extractor returned row-specific material Steel, Mild and density 7850.0 for product 65_retaining_ring_DIN 471 - 10x1. Fasteners.eu lists DIN 471 steel making as spring steel, and Keller & Kalmbach lists a DIN 471 10x1 circlip as spring steel, phosphated; these are standard-part cross-checks rather than the row-specific material source."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The row-specific CAD metadata resolves the material family as steel but may not preserve the exact production spring-steel grade, hardness, or coating used for a real DIN 471 retaining ring."
how_to_make:
  summary: "Procure as a standard DIN 471 10x1 external retaining ring where possible; a plausible local route is to make it from spring-steel strip by blanking the ring profile and lug holes, hardening/tempering for spring behavior, deburring, and applying a corrosion-protection finish."
  manufacturing_steps:
    - "Use a standard DIN 471 10x1 ring as the preferred purchased hardware item or reference geometry."
    - "For local production, start from spring-steel sheet or strip near 1 mm thickness."
    - "Blank, punch, fineblank, or laser-cut the split ring profile and two plier holes."
    - "Heat treat and temper to obtain the needed spring behavior, then deburr edges and inspect free diameter, thickness, lug-hole geometry, and fit in the shaft groove."
    - "Apply phosphate/oil, black oxide, zinc, or another finish only when the machine environment requires it."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/65_retaining_ring_DIN 471 - 10x1.step; research/ream250_bom/ream250_bom_row_0271_65__views_2x2.png; https://www.keller-kalmbach.com/products/fasteners/safety-elements/retaining-rings-and-washers/din-471-circlip/p/10047110; https://www.huyett.com/dsh-010-zc"
    cited_fact_or_basis: "CAD and preview show a flat 1 mm split ring with lug holes. Keller & Kalmbach identifies a DIN 471 10x1 circlip as spring steel and phosphated. Huyett search result for an M10 DIN 471 retaining ring reports carbon spring steel, 1.00 mm thickness, and stamped style. targeted_web_search: searched \"DIN 471 retaining ring 10x1 material\", \"DIN 471 retaining ring manufacturing stamped\", \"DIN 471 external retaining ring spring steel\", and \"DIN 471 10x1 circlip phosphated\"; found standard/vendor pages confirming DIN 471 identity and spring-steel/phosphated/stamped conventions, but no row-specific manufacturing drawing for this reAM250 instance."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row should be treated as standard hardware rather than a custom machined part because the CAD filename carries the DIN 471 standard designation and the geometry matches a catalog retaining ring."
    - "The local manufacturing route is inferred from retaining-ring geometry and standard-part vendor descriptions; exact tooling, heat treatment, and finish are not specified by the BOM."
  uncertainty_notes:
    - "The local route is process-plausible but not sourced from the reAM250 BOM package; production-grade spring properties and coating should be specified before substituting a locally made ring for purchased hardware."
kb_implications:
  - "item_granularity: simple_part - model as reusable standard retaining-ring hardware, likely shared with a generic circlip or retaining-ring kit rather than as a machine-specific custom item."
---

Research result for reAM250 BOM row 271.
