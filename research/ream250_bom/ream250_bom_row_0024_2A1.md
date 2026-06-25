---
row_identity:
  item: "2A1"
  cad_file: "2A1_bottom"
  source_row_number: 24
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom bottom/base plate for the reAM250 2A motion or support subassembly; CAD shows a square, shallow structural plate with a perimeter frame, recessed/lightened center area, and mounting features for neighboring guide, side-plate, support-plate, or bearing components."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A1_bottom.step; research/ream250_bom/ream250_bom_row_0024_2A1__views_2x2.png"
    cited_fact_or_basis: "BOM row 24 states item 2A1, quantity 1, CAD file 2A1_bottom. The manifest maps the row to gold_export/parts/2A1_bottom.step as a matched_existing part export. Nearby BOM rows on the same page include 2A2_back_plate, Hiwin linear guide slides and rails, side plates, distance pieces, support plates, and axis-bearing-bottom parts. FreeCAD measured one solid with bounding box 398.00 x 398.00 x 35.00 mm. The rendered contact sheet shows a square shallow base/bottom plate with a perimeter frame and recessed or lightened internal rib/pocket geometry."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name 'bottom', large square footprint, and neighboring 2A guide/bearing/support rows are interpreted as a base or lower support plate for that subassembly."
  uncertainty_notes:
    - "The BOM/CAD evidence does not state the exact mating interfaces, load path, or which of the adjacent 2A components fasten directly to this bottom plate."
mass:
  value_kg: 13.8
  basis: "Per unit for BOM quantity 1. FreeCAD volume 5111786.843 mm^3 equals 0.005111787 m^3. Assembly STEP material metadata reports Aluminum 6061 with density 2700 kg/m^3, giving 13.802 kg; rounded planning mass is 13.8 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A1_bottom.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 5111786.843 mm^3, area 402613.743 mm^2, and bounding box 398.00 x 398.00 x 35.00 mm. Local assembly STEP material extraction for product 2A1_bottom returned material Aluminum 6061 and density 2700.0, with the export using kg/m^3-like material densities."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one manufactured bottom plate."
    - "The assembly STEP material density is treated as applicable to the whole single-solid part."
  uncertainty_notes:
    - "Mass depends on CAD export fidelity and whether the STEP solid includes all cutouts, holes, and pockets exactly as manufactured."
material:
  primary_material: "Aluminum 6061"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 2A1_bottom matched the row-specific product definition and returned material Aluminum 6061 with density 2700.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata identifies the alloy family/grade but does not state temper, heat treatment, coating, or surface finish."
how_to_make:
  summary: "Fabricate as a custom CNC-machined 6061 aluminum base plate from thick plate or billet stock, with pocketing/lightening, perimeter features, mounting holes, deburring, and inspection for flatness and hole locations."
  manufacturing_steps:
    - "Select Aluminum 6061 plate or billet stock larger than the 398.00 x 398.00 x 35.00 mm finished envelope."
    - "Rough cut or saw the square blank, then face mill the top and bottom surfaces to establish thickness and flat datum faces."
    - "CNC mill the perimeter frame, recessed/lightened internal pocket or rib pattern, edge features, and visible mounting holes or slots."
    - "Deburr all machined edges and clean the part for assembly."
    - "Inspect overall dimensions, flatness, pocket depths, and mounting-feature positions against the CAD model before installing adjacent 2A guide, support, or bearing hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A1_bottom.step; research/ream250_bom/ream250_bom_row_0024_2A1__views_2x2.png; web search results for row-specific and 6061 machining queries"
    cited_fact_or_basis: "CAD and preview show one 398.00 x 398.00 x 35.00 mm square, shallow aluminum part with a perimeter frame, recessed/lightened center geometry, and mounting features. targeted_web_search: searched \"2A1_bottom reAM250\", \"reAM250 2A1 bottom aluminum\", and \"Aluminum 6061 CNC machined plate pockets\" results found duplicate BOM text for the row and general 6061 CNC machining references, but no row-specific drawing or manufacturing-process specification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Subtractive CNC machining from 6061 plate or billet is inferred from the large flat-plate geometry, resolved aluminum alloy, pockets, and mounting features."
    - "The part is treated as one custom simple part because the BOM row has no manufacturer, product ID, or supplier link"
  uncertainty_notes:
    - "The sources do not specify actual production tooling, tolerances, flatness requirement, surface finish, anodizing, or whether any features are made in multiple setups."
kb_implications:
  - "item_granularity: simple_part - Model as one custom machined Aluminum 6061 base/bottom plate, reusable with generic plate-machining and pocketing operations rather than as a vendor module."
---

Research result for reAM250 BOM row 24.
