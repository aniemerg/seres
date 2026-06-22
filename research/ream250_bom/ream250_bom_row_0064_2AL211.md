---
row_identity:
  item: "2AL211"
  cad_file: "2AL211_motor"
  source_row_number: 64
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.br-automation.com/en/products/80mpf5500d114-01/"
function:
  summary: "B&R 80MPF5.500D114-01 2-phase hybrid stepper motor module with 60 mm flange, incremental encoder, and holding brake, used as an actuated motion source in the reAM250."
  source:
    url_or_path: "https://www.br-automation.com/en/products/80mpf5500d114-01/; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AL211_motor.step; research/ream250_bom/ream250_bom_row_0064_2AL211__views_2x2.png"
    cited_fact_or_basis: "BOM row 64 identifies item 2AL211 as quantity 1, CAD file 2AL211_motor, manufacturer B&R, and link URL for 80MPF5.500D114-01. The B&R page identifies 80MPF5.500D114-01 as a stepper motor with 60 mm flange, length 184.4 mm, incremental encoder and brake; it also lists 3.5 Nm holding torque, 2.5 Nm stall torque, and 24 VDC brake data. FreeCAD measured one solid with bounding box 204.40 x 60.00 x 78.20 mm, and the preview shows a long rectangular motor body with square flange and shaft."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied CAD, manifest row, and B&R URL describe the same physical motor despite the BOM text containing extra 'elastomer jaw coupling GN 2240-' wording."
  uncertainty_notes:
    - "The CSV description appears to include conflicting trailing coupling text, but the manufacturer, product URL, CAD filename, CAD geometry, and B&R product page all match the stepper motor identity."
mass:
  value_kg: 1.8
  basis: "Per-unit mass for quantity 1. The B&R mechanical properties table gives weight as 1,800 g, so the BOM row total is also 1.8 kg. FreeCAD measured CAD volume 556244.165 mm^3; using the vendor weight implies an effective packaged motor density of about 3236 kg/m^3, plausible for a motor assembly with metal, copper, magnet, air gaps, encoder, and brake."
  source:
    url_or_path: "https://www.br-automation.com/en/products/80mpf5500d114-01/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AL211_motor.step"
    cited_fact_or_basis: "The B&R page lists mechanical weight as 1,800 g and length 184.4 mm. FreeCAD measured one solid with volume 556244.165 mm^3 and bounding box 204.40 x 60.00 x 78.20 mm."
    evidence_basis: "bom_provided"
  assumptions:
    - "The vendor listed weight is used as the mass of one complete motor module represented by the row."
  uncertainty_notes:
    - "The CAD length is slightly longer than the B&R listed motor length, likely because the per-row CAD includes shaft/flange detail; the vendor weight remains the best mass basis for the complete row item."
material:
  primary_material: "multi-material electromechanical motor module: unknown metal housing/frame and shaft, magnetic steel laminations/rotor, permanent magnet material, copper windings/coils, brake and encoder components"
  source:
    url_or_path: "https://www.br-automation.com/en/products/80mpf5500d114-01/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AL211_motor.step"
    cited_fact_or_basis: "The B&R page identifies the row product as a 2-phase hybrid stepper motor with incremental encoder and brake, but does not state material grades. Assembly STEP material extraction for product 2AL211_motor returned only material 'Generic' with density 1000.0, which is placeholder metadata. FreeCAD and the preview show a motor-like module but no material split. targeted_web_search: tried 'B&R 80MPF5.500D114-01 material housing copper winding magnet', '80MPF5.500D114-01 datasheet material housing', and '2-phase hybrid stepper motor construction materials copper windings permanent magnet'; results found row-matched motor specifications and general hybrid-stepper construction references, but no row-specific B&R material or grade list."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The broad material set follows from the B&R row identity as a hybrid stepper motor with brake and encoder, combined with standard motor construction requirements."
  uncertainty_notes:
    - "No row-specific source resolves housing alloy, shaft alloy, magnet grade, winding mass, brake friction material, or encoder/electronics material splits, so downstream KB modeling should treat this as a purchased electromechanical module until a teardown or manufacturer material declaration is available."
how_to_make:
  summary: "Procure as a calibrated B&R stepper motor with encoder and brake; for KB planning, treat local production as a future sub-BOM problem covering motor laminations, windings, rotor/magnets, bearings, encoder, brake, housing, shaft, assembly, and electrical test."
  manufacturing_steps:
    - "Procure B&R 80MPF5.500D114-01 or an equivalent 60 mm flange hybrid stepper motor with encoder and brake matching the row interface."
    - "Verify nameplate/specification match: 5 A parallel wiring, 3.5 Nm holding torque, 2.5 Nm stall torque, ABR 24 VDC encoder, and 24 VDC brake."
    - "Inspect the CAD/interface envelope against the reAM250 mounting location before installation."
    - "If later localized, decompose into a dedicated motor sub-BOM and process chain for laminated stator/rotor stack, copper winding, shaft and bearing assembly, permanent magnet rotor, brake, encoder, housing, calibration, and test."
  source:
    url_or_path: "https://www.br-automation.com/en/products/80mpf5500d114-01/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AL211_motor.step; research/ream250_bom/ream250_bom_row_0064_2AL211__views_2x2.png"
    cited_fact_or_basis: "The B&R page provides the row-matched product identity and specifications: 80MPF5.500D114-01, 2-phase hybrid stepper motor, 60 mm flange, incremental encoder and brake, 5 A parallel wiring, 3.5 Nm holding torque, 2.5 Nm stall torque, and brake electrical data. CAD preview and FreeCAD geometry confirm a complete motor module envelope rather than a simple one-piece bracket or stock material."
    evidence_basis: "bom_provided"
  assumptions:
    - "Procurement is the appropriate near-term route because the row is a calibrated vendor electromechanical module, not a simple mechanical part."
  uncertainty_notes:
    - "The B&R page supports procurement and interface planning, but not a manufacturable internal sub-BOM, calibration procedure, or process route for self-manufacturing the motor."
kb_implications:
  - "item_granularity: purchased_module - model as a purchased/calibrated stepper motor module for now; split into a motor sub-BOM only when local electromechanical manufacturing and calibration details are intentionally added."
---

Result generated for the leased reAM250 BOM row only.
