---
row_identity:
  item: "8D1"
  cad_file: "8D1_flexible_pipe_part_1"
  source_row_number: 210
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0250"
function:
  summary: "Thin annular end/flange component for the Pfeiffer Vacuum 120SWG040-0250 DN 40 ISO-KF flexible pipe assembly, providing the circular connection interface at one end of the vacuum hose."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8D1_flexible_pipe_part_1.step; research/ream250_bom/ream250_bom_row_0210_8D1__views_2x2.png; https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0250"
    cited_fact_or_basis: "BOM row 210 identifies item 8D1 as Pfeiffer Vacuum 'part 1 120SWG040-0250: flexible pipe'; the CAD export is one solid with an annular 5.32 x 56.28 x 56.28 mm bounding box, and the rendered preview shows a thin circular ring/end feature for the DN 40 flexible-pipe product route."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row-specific CAD part is interpreted as one end/flange part of the larger 120SWG040-0250 flexible pipe because the BOM splits neighboring row 8D2 as part 2 of the same vendor product."
  uncertainty_notes:
    - "The CAD part represents an exported subcomponent of the flexible pipe, so the function is for this annular end part rather than the complete hose assembly."
mass:
  value_kg: 0.00249
  basis: "Per-unit mass for one CAD part. FreeCAD measured volume 309.686 mm^3, converted to 3.09686e-7 m^3; using local stainless_steel_304 density 8030 kg/m^3 gives 0.00249 kg. BOM quantity is 1, so the row total is also about 0.00249 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8D1_flexible_pipe_part_1.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 309.686 mm^3 for 8D1_flexible_pipe_part_1.step; kb/materials/properties.yaml lists stainless_steel_304 density as 8030 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the physical volume of one row item."
    - "The annular end part uses the stainless 304/1.4301 flange material from the matched Pfeiffer flexible-pipe product family."
  uncertainty_notes:
    - "If the CAD export omits small weld beads, rolled edges, or other nonmodeled end-piece details, the true mass may be modestly higher."
material:
  primary_material: "Stainless steel flange/end-ring material, consistent with Pfeiffer's 1.4301 / AISI 304 flange material for this DN 40 flexible pipe family; the complete flexible pipe also uses 316L stainless bellows."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0250; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The BOM-provided Pfeiffer product route identifies the 120SWG040-0250 flexible-pipe family; local assembly STEP material extraction for this CAD product returns only Generic material with density 1000, which does not resolve material, so material is taken from the matched Pfeiffer product-family specification."
    evidence_basis: "bom_provided"
  assumptions:
    - "Because the rendered row CAD is the end-ring/flange-like subpart, the flange material is more applicable to this row than the bellows material."
  uncertainty_notes:
    - "The local STEP file does not carry a real material assignment for this subpart; material assignment depends on the row-matched vendor product family."
how_to_make:
  summary: "Best route for the current KB is procurement as the Pfeiffer Vacuum 120SWG040-0250 DN 40 ISO-KF flexible pipe/end component, followed by receipt inspection and assembly into the reAM250 vacuum line."
  manufacturing_steps:
    - "Procure the row-matched Pfeiffer 120SWG040-0250 flexible-pipe product or spare/end component through the BOM-provided vendor route."
    - "Inspect the annular end/flange geometry and sealing interface against the CAD preview and DN 40 ISO-KF installation envelope."
    - "Install the part as part of the flexible vacuum pipe connection in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0250"
    cited_fact_or_basis: "BOM row 210 gives Pfeiffer Vacuum and product route 120SWG040-0250 for the flexible pipe; the CAD and manifest map this row to 8D1_flexible_pipe_part_1."
    evidence_basis: "bom_provided"
  assumptions:
    - "Until a local vacuum-hose fabrication workflow is modeled, this vendor flexible-pipe/end component should be treated as a procured standard vacuum component."
  uncertainty_notes:
    - "Local manufacture would require additional process data for stainless bellows forming and end fitting fabrication that is outside this row's BOM-side evidence."
kb_implications:
  - "item_granularity: simple_part - Model row 8D1 as a simple stainless annular end/flange part of a standard flexible vacuum pipe assembly, with the complete vendor hose handled separately if needed."
---
