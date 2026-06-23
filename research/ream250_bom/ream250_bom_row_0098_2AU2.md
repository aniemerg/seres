---
row_identity:
  item: "2AU2"
  cad_file: "2AU2_nut_M12x1"
  source_row_number: 98
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Thin M12 x 1 hex mounting/lock nut for a Balluff BES01H6 / BES 516-356-S4-C cylindrical inductive proximity sensor, used to clamp or position the threaded sensor body in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AU2_nut_M12x1.step; research/ream250_bom/ream250_bom_row_0098_2AU2__views_2x2.png; https://www.balluff.com/en-us/products/BES01H6; https://www.balluff.com/en-us/products/BAM042Z"
    cited_fact_or_basis: "BOM row 98 identifies item 2AU2 as quantity 2 of 'Nut M12 x 1 BALLUFF BES 516-356-S4-C_1'. The Balluff BES01H6 page identifies BES 516-356-S4-C as an M12x1 cylindrical inductive proximity sensor. The Balluff BAM042Z page identifies a nut accessory for M12 sensors. FreeCAD measured one solid and the rendered contact sheet shows a thin hex nut with a central threaded hole."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row nut is the mounting/locking nut for the nearby Balluff M12x1 sensor rather than a separate unrelated M12 fastener."
  uncertainty_notes:
    - "The BOM row does not provide a direct Balluff nut accessory order code, so the function is tied to the row description, M12x1 CAD geometry, and Balluff's M12 sensor/nut product-family evidence."
mass:
  value_kg: 0.00488
  basis: "Per-unit estimate for one physical nut. FreeCAD measured CAD volume 609.594 mm^3, equal to 6.09594e-7 m^3. Using the local stainless_steel density constant of 8000 kg/m^3 gives 0.0048768 kg, rounded to 0.00488 kg per nut. BOM quantity is 2, so the row total is about 0.00975 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AU2_nut_M12x1.step; kb/materials/properties.yaml; https://www.balluff.com/en-us/products/BAM042Z"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 609.594 mm^3, surface area 648.760 mm^2, and bounding box about 4.00 x 19.63 x 19.63 mm; the preview metadata reports a 4.00 mm thickness, 19.63 mm across-corners span, and 17.00 mm across-flats span. Balluff's M12 sensor nut accessory page lists material as stainless steel. kb/materials/properties.yaml lists stainless_steel density 8000 kg/m^3."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The STEP solid volume is treated as the physical solid volume of one nut."
    - "The Balluff M12 sensor nut accessory material is applied to this row's Balluff M12x1 sensor nut."
    - "The local stainless_steel density value is used as the calculation constant."
  uncertainty_notes:
    - "No catalog net weight was found for the exact row nut; the estimate depends on the supplied CAD solid matching the physical nut and on the Balluff M12 sensor-nut material match."
material:
  primary_material: "stainless steel"
  source:
    url_or_path: "https://www.balluff.com/en-us/products/BAM042Z; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Balluff's BAM042Z nut accessory page lists use for M12 sensors and material as stainless steel. Assembly STEP material extraction for 2AU2_nut_M12x1 returned only material 'Generic' with density 1000.0, which is placeholder metadata and was not used to resolve material."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The Balluff M12 sensor nut accessory material applies to this row because the BOM describes an M12x1 nut for the Balluff BES 516-356-S4-C sensor and the CAD geometry is a matching thin M12 hex nut."
  uncertainty_notes:
    - "Exact stainless grade is not resolved by the row evidence; downstream KB modeling should use a stainless-steel family unless a Balluff drawing or order record identifies the specific nut grade."
how_to_make:
  summary: "Procure as Balluff-compatible M12x1 stainless sensor mounting hardware; a plausible local route is to machine or cold-form a thin stainless hex nut, cut/form the M12x1 internal thread, deburr/passivate, and inspect thread fit and wrench flats."
  manufacturing_steps:
    - "Use stainless hex bar/near-net nut blanks or cold-formed stainless nut blanks sized for an M12x1 thin hex nut."
    - "Drill and tap or thread-form the M12x1 internal thread."
    - "Face to the roughly 4 mm nut thickness and form/finish the hex flats if not using pre-hex stock."
    - "Deburr, clean, and passivate for corrosion-resistant machine use."
    - "Inspect M12x1 thread fit on the Balluff sensor body and verify across-flats/wrench geometry."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0098_2AU2__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AU2_nut_M12x1.step; https://www.balluff.com/en-us/products/BAM042Z"
    cited_fact_or_basis: "The CAD preview shows a thin hex nut with a central threaded hole; FreeCAD measured a 4.00 mm thick one-solid nut. Balluff identifies the matching M12 sensor nut accessory class and stainless material, but does not state the nut manufacturing process. targeted_web_search: searched 'Balluff M12x1 fastening nut stainless steel BES sensor nut', 'Balluff BES M12x1 fastening nut material stainless steel', and 'M12x1 fastening nut Balluff stainless steel'; found Balluff product/material facts for M12 sensor nuts but no row-specific manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local manufacturing route is inferred from the one-piece stainless hex-nut geometry and standard nut fabrication practice."
    - "For low-volume KB planning, machining from stainless hex stock is acceptable even if commercial production may use cold forming."
  uncertainty_notes:
    - "The sources do not specify Balluff's factory process, tolerance class, surface finish, or exact stainless grade for this nut."
kb_implications:
  - "item_granularity: simple_part - finished standard-like M12x1 stainless sensor mounting nut; later KB work should reuse or create generic sensor-nut/fastener hardware rather than model it as a purchased module or raw stock."
---

Research result for the leased reAM250 BOM row only.
