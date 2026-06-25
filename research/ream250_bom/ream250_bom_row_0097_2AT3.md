---
row_identity:
  item: "2AT3"
  cad_file: "2AT3_sensor"
  source_row_number: 97
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.balluff.com/de-de/products/BES01H6"
function:
  summary: "Bottom inductive proximity sensor for detecting nearby metal targets; Balluff BES01H6 / BES 516-356-S4-C, M12x1 cylindrical non-flush PNP normally-open sensor with 4 mm sensing range and M12 4-pin connector."
  source:
    url_or_path: "https://www.balluff.com/de-de/products/BES01H6"
    cited_fact_or_basis: "The BOM row identifies item 2AT3 as Balluff part BES01H6. The Balluff page identifies BES01H6 as BES 516-356-S4-C, an inductive proximity switch in cylindrical M12x1 form, non-flush installation, 4 mm range, PNP normally-open output, and M12x1 4-pin connector."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row description 'inductive sensor bottom' is interpreted as this sensor's placement in the reAM250 assembly, not as a different product variant."
  uncertainty_notes: []
mass:
  value_kg: 0.03
  basis: "Official Balluff regional product information for the row-matched BES01H6 gives 30 g. Local CAD evidence is consistent with the same product envelope: FreeCAD measured one solid, 6924.053 mm^3 volume, 3114.605 mm^2 area, and a 70.00 x 12.00 x 12.00 mm bounding box. The rendered contact sheet shows a threaded cylindrical M12-style sensor body with connector end."
  source:
    url_or_path: "https://www.balluff.com/en-us/products/BES01H6"
    cited_fact_or_basis: "Official Balluff product route for BES01H6 / BES 516-356-S4-C lists weight 30 g and dimensions Ø 12 x 70 mm; local STEP geometry for 2AT3_sensor measures 70.00 x 12.00 x 12.00 mm."
    evidence_basis: "bom_provided"
  assumptions:
    - "The official Balluff regional product page is treated as the same BOM-provided product route because it is the same manufacturer domain and exact product ID as the BOM URL."
    - "The catalog weight is preferred over density-from-CAD because the STEP is a product-envelope solid for a multi-material electronic sensor."
  uncertainty_notes:
    - "The local STEP does not expose separate stainless, PBT, electronics, connector, and potting volumes, so CAD volume is useful for identity and envelope checks but not for a reliable density-derived mass."
material:
  primary_material: "stainless steel housing with PBT sensing face; internal electronics, connector contacts, and potting are present but not material-resolved"
  source:
    url_or_path: "https://publications.balluff.com/pdfengine/pdf?con=de&id=305144&type=pdb"
    cited_fact_or_basis: "The Balluff datasheet for BES 516-356-S4-C / BES01H6 lists housing material as Edelstahl/stainless steel and active sensing face material as PBT."
    evidence_basis: "bom_provided"
  assumptions:
    - "The material value is reported as a purchased sensor composition rather than collapsed into one primary structural material because the vendor specifies different housing and sensing-face materials."
  uncertainty_notes:
    - "The vendor-accessible evidence resolves only the external housing and sensing face materials; internal coil, PCB, connector, and encapsulant materials are not specified."
how_to_make:
  summary: "Treat as a purchased/imported calibrated inductive proximity sensor module. A local production model would require a stainless M12 threaded housing, PBT sensing face, coil and oscillator/switching electronics, M12 4-pin connector, sealing/potting, electrical calibration, IP68 sealing validation, and functional test."
  manufacturing_steps:
    - "Machine or source an M12x1 stainless cylindrical sensor housing with connector-end geometry."
    - "Mold or source the PBT sensing face and integrate it with the sensing end."
    - "Assemble the inductive coil, oscillator/switching electronics, LED/function indication, and M12 4-pin connector."
    - "Pot and seal the assembly for IP68 service, then calibrate switching distance and verify electrical output."
  source:
    url_or_path: "https://www.balluff.com/de-de/products/BES01H6"
    cited_fact_or_basis: "The BOM-provided Balluff page identifies a BES01H6 inductive proximity sensor with M12x1 stainless/PBT construction, M12 4-pin connector, 10...30 VDC operation, IP68 rating, and 4 mm sensing range. targeted_web_search: searched 'BES01H6 BES 516-356-S4-C weight mass', 'BES 516-356-S4-C Gewicht', and 'Balluff BES01H6 weight'; results confirmed row-matched catalog/distributor data but did not provide a manufacturing process specification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Manufacturing steps are inferred from the sourced sensor type, connectorized cylindrical form, material callouts, and normal inductive proximity sensor construction."
    - "Because this is a calibrated electronic sensing module, KB modeling should initially import or purchase it rather than decompose it into a local sub-BOM."
  uncertainty_notes:
    - "The exact internal electronics, coil geometry, potting compound, connector contact plating, and factory calibration process are not disclosed by the row evidence."
kb_implications:
  - "item_granularity: complex_module - row is a complete calibrated Balluff inductive proximity sensor, best treated as an imported sensing module until a detailed sensor electronics sub-BOM and calibration workflow are modeled.; defer internal decomposition until a focused sub-BOM and manufacturing workflow are modeled."
---

CAD preview: `research/ream250_bom/ream250_bom_row_0097_2AT3__views_2x2.png`
