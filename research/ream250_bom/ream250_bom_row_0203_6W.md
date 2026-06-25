---
row_identity:
  item: "6W"
  cad_file: "6W_connection_linear_guide_back"
  source_row_number: 203
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Stainless-steel back-side connection bracket for the reAM250 linear-guide/motor-drive group, providing a rigid mounting link between the back linear guide hardware and adjacent support or drive structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0203_6W__views_2x2.png"
    cited_fact_or_basis: "BOM row 203 names item 6W as '6W_connection_linear_guide_back' with quantity 1. Manifest row 203 maps the same item to a matched part STEP file. Neighboring BOM rows include SMC back linear-guide carriage/rail rows, belt/pulley rows, motor-mount connection rows, and row 204 '6X_connection_linear_guide_top'. The CAD preview shows a compact bracket/link with mounting holes and a 56.00 x 39.00 x 93.00 mm envelope."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name and adjacent BOM context identify this as a connection bracket for the back linear guide rather than the vendor linear guide carriage or rail itself."
  uncertainty_notes:
    - "The BOM does not name the exact mating fastener pattern or connected faces, so the precise interface assignment within the back guide assembly remains approximate."
mass:
  value_kg: 0.356
  basis: "Per-unit mass estimate is 0.356 kg from FreeCAD STEP volume 44506.755 mm^3 = 4.4506755e-5 m^3 multiplied by the assembly STEP material density 8000 kg/m^3 for Stainless Steel, Austenitic. BOM quantity is 1, so the row total is also about 0.356 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6W_connection_linear_guide_back.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 44506.755 mm^3, area 21505.283 mm^2, and bounding box 56.00 x 39.00 x 93.00 mm. Local assembly STEP material extraction for product 6W_connection_linear_guide_back returned material 'Stainless Steel, Austenitic' with density 8000.0 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The per-part STEP solid volume represents one physical 6W bracket and includes the main load-bearing geometry."
    - "The assembly STEP density is treated as kg/m^3-like material density, consistent with the extractor note for this reAM250 export."
  uncertainty_notes:
    - "STEP export fidelity and any unmodeled small features, fasteners, surface finish, or post-machining stock allowance are not separately resolved; mass should be treated as a CAD-derived planning estimate."
material:
  primary_material: "Austenitic stainless steel."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 6W_connection_linear_guide_back returned material 'Stainless Steel, Austenitic' and density 8000.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is modeled at the austenitic stainless family level because the STEP metadata does not name a specific alloy grade such as 304 or 316."
  uncertainty_notes:
    - "Exact stainless grade, heat treatment, and surface finish are unspecified."
how_to_make:
  summary: "Fabricate as a simple stainless guide-connection bracket: cut or rough-machine the near-net bracket form from austenitic stainless stock, machine the locating faces and mounting holes, deburr/passivate, and inspect fit against the back linear-guide assembly"
  manufacturing_steps:
    - "Start from stainless plate/block stock sized for the roughly 56 x 39 x 93 mm envelope."
    - "Cut, mill, or waterjet/laser rough the bracket profile, including the tall back lug and transverse mounting flanges."
    - "Machine or drill the mounting holes and any datum faces needed to locate the back linear-guide hardware."
    - "Deburr and clean or passivate the part, then inspect hole spacing, flatness, and fit in the linear-guide/motor-drive assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6W_connection_linear_guide_back.step; research/ream250_bom/ream250_bom_row_0203_6W__views_2x2.png"
    cited_fact_or_basis: "CAD geometry shows a compact stainless bracket with flat flanges, a taller rear lug/web, and multiple mounting holes. The detailed fabrication sequence is inferred from the geometry and material, not directly stated by a vendor or drawing. targeted_web_search: queries tried included '\"6W_connection_linear_guide_back\"', '\"connection linear guide back\" reAM250', and '\"reAM250\" \"6W\" \"connection_linear_guide_back\"'; results found mirrored BOM listings or generic linear-guide information, not a row-specific manufacturing source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The geometry is practical as a fabricated or machined stainless bracket rather than a calibrated module"
    - "Separate fasteners, rails, carriages, and belt-drive components are represented by neighboring BOM rows and are not part of this row's per-unit item."
  uncertainty_notes:
    - "The fabrication route does not resolve original tolerances, datum scheme, or whether the source part was machined from solid, cut from plate plus secondary machining, or made by another near-net process."
kb_implications:
  - "item_granularity: simple_part - Model 6W as a reusable austenitic stainless linear-guide connection bracket; keep the SMC guide rail/carriage and drive components as separate neighboring BOM items."
---
