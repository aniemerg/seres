---
row_identity:
  item: "6V"
  cad_file: "6V_connection_motor_mount"
  source_row_number: 202
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Stainless-steel connection bracket in the reAM250 motor-mount group, linking the NEMA 23 motor mount/support structure to adjacent belt or linear-guide hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0202_6V__views_2x2.png"
    cited_fact_or_basis: "BOM row 202 names item 6V as '6V_connection_motor_mount' with quantity 3. Neighboring BOM rows 197-205 are motor-mount supports, a NEMA 23 motor, a GT2 pulley, connection parts for linear guides, and an 11 mm spacer. The CAD preview shows a compact angled bracket/link plate with mounting holes and a 59.00 x 40.00 x 55.02 mm envelope."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name and adjacent BOM context identify the bracket as a motor-mount connection part rather than a standalone motor or vendor module."
  uncertainty_notes:
    - "The exact mating faces and fastener pattern are not named in the BOM, so the specific connected subcomponents remain approximate."
mass:
  value_kg: 0.101
  basis: "Per-unit mass estimate is 0.101 kg from FreeCAD STEP volume 12629.611 mm^3 = 1.2629611e-5 m^3 multiplied by the assembly STEP material density 8000 kg/m^3 for Stainless Steel. BOM quantity is 3, giving an optional row total of about 0.303 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6V_connection_motor_mount.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 12629.611 mm^3, area 10314.514 mm^2, and bounding box 59.00 x 40.00 x 55.02 mm. Local assembly STEP material extraction for product 6V_connection_motor_mount returned material 'Stainless Steel' with density 8000.0 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The per-part STEP solid volume represents one physical 6V bracket and does not omit major internal features."
    - "The assembly STEP density is treated as kg/m^3-like material density, consistent with the extractor note for this reAM250 export."
  uncertainty_notes:
    - "STEP volume fidelity, tessellation/export simplification, and any unmodeled fasteners or finish are not separately resolved; mass should be treated as a CAD-derived planning estimate."
material:
  primary_material: "Stainless steel."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 6V_connection_motor_mount returned material 'Stainless Steel' and density 8000.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row uses a generic stainless-steel family rather than a known specific alloy grade because the STEP metadata does not name an alloy such as 304 or 316."
  uncertainty_notes:
    - "Exact stainless grade, heat treatment, and surface finish are unspecified."
how_to_make:
  summary: "Fabricate as a simple stainless-steel bracket/link: cut or laser/waterjet the bracket blank from stainless stock, machine or drill the mounting holes and locating faces, deburr, finish, and inspect against the motor-mount assembly"
  manufacturing_steps:
    - "Cut the angled bracket profile from stainless-steel plate or near-net stock sized for the roughly 59 x 40 x 55 mm envelope."
    - "Machine or drill mounting holes, slots, and mating faces to match the motor-mount and adjacent guide/belt hardware."
    - "Deburr edges, clean or passivate as needed, then inspect hole spacing, flatness, and fit in the motor-mount assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6V_connection_motor_mount.step; research/ream250_bom/ream250_bom_row_0202_6V__views_2x2.png"
    cited_fact_or_basis: "CAD geometry shows a compact stainless bracket/link with flat faces, angled web geometry, and mounting holes. The detailed fabrication sequence is inferred from the geometry and material, not directly stated by a vendor or drawing. targeted_web_search: queries tried included '\"6V_connection_motor_mount\"', '\"reAM250\" \"6V\" \"connection motor mount\"', and '\"connection motor mount\" stainless steel 59 40 55'; results found mirrored BOM listings or non-matching generic motor mounts, not a row-specific manufacturing source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The geometry is practical as a machined or cut stainless bracket rather than a calibrated module"
    - "Fasteners are handled elsewhere in the motor-mount assembly and are not part of this row's per-unit item."
  uncertainty_notes:
    - "The fabrication route does not resolve tolerances, exact stock form, or whether the original part was welded, bent, or machined from solid."
kb_implications:
  - "item_granularity: simple_part - Model 6V as a reusable stainless motor-mount connection bracket; do not create a purchased module unless later evidence shows it is a vendor subsystem."
---
