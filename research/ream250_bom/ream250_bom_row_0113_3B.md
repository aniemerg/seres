---
row_identity:
  item: "3B"
  cad_file: "3B_valve_ISO_K_DN63_310VEP063-01"
  source_row_number: 113
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/310VEP063_02"
function:
  summary: "Pfeiffer EVB 063 PA DN 63 ISO-K electro-pneumatic angle valve used as a vacuum shut-off/isolation valve in the reAM250 vacuum plumbing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.pfeiffer-vacuum.com/global/de/shop/products/310VEP063_02; https://www.vacuum-shop.com/shop/en_US/category/2073371/product/310vep06302/%7B%7Bresult.url%7D%7D; https://vacuum-shop.com/2075819/downloads/manuals/vp0002ben.pdf"
    cited_fact_or_basis: "BOM row 113 identifies item 3B as Pfeiffer Vacuum product 310VEP063 with link URL for 310VEP063_02. The Pfeiffer online shop route identifies 310VEP063-02 as an EVB 063 PA angle valve with DN 63 ISO-K connection, electro-pneumatic actuator, normally closed behavior, visual position indicator, and 24 V DC input. The operating instructions state the angle valve is used as a shut-off or venting device. official_alternate_route_check: the BOM URL is on pfeiffer-vacuum.com for product 310VEP063_02; the vacuum-shop.com page is an official Pfeiffer Vacuum online shop page showing Pfeiffer Vacuum contact/copyright and the same row-matched order number 310VEP063-02."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM description_or_product_id 310VEP063 maps to the linked 310VEP063-02 24 V DC variant because the row link URL and CAD filename both carry the same 310VEP063 product family."
  uncertainty_notes:
    - "The local row STEP is a simplified 5.8 x 8.5 x 8.5 mm proxy shape and is not dimensionally representative of the full DN 63 valve body."
mass:
  value_kg: 3.9
  basis: "Per-unit vendor weight for one 310VEP063-02 EVB 063 PA valve is 3.9 kg. BOM quantity is 1, so the row total is also about 3.9 kg. FreeCAD measured the local row STEP as one solid with volume 257.185 mm^3 and bounding box about 5.80 x 8.50 x 8.50 mm, which is inconsistent with the vendor DN 63 valve dimensions and was not used for the physical valve mass."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/310VEP063_02; https://www.vacuum-shop.com/shop/en_US/category/2073371/product/310vep06302/%7B%7Bresult.url%7D%7D; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3B_valve_ISO_K_DN63_310VEP063-01.step"
    cited_fact_or_basis: "The Pfeiffer online shop route lists weight 3.9 kg for order number 310VEP063-02. Local FreeCAD geometry check measured only a tiny proxy solid, so the vendor product weight is the controlling mass fact. official_alternate_route_check: the original BOM URL points to Pfeiffer product 310VEP063_02; the vacuum-shop.com page is an official Pfeiffer Vacuum shop route for the same order number and exposes the weight field."
    evidence_basis: "bom_provided"
  assumptions:
    - "The vendor catalog weight includes the complete valve assembly, including actuator, position indicator, pilot/control valve hardware, seals, and housing."
  uncertainty_notes:
    - "The CAD package cannot independently verify mass because the exported per-row STEP is not the full-size valve geometry."
material:
  primary_material: "Aluminum housing with stainless steel bellows feedthrough, FKM seal, microswitch/position-indicator and electro-pneumatic actuator materials not further resolved."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/310VEP063_02; https://www.vacuum-shop.com/shop/en_US/category/2073371/product/310vep06302/%7B%7Bresult.url%7D%7D; .venv/bin/python queue_tasks/research_pack/ream250_bom_research/research_scripts/extract_step_materials.py --step design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step --product-name 3B_valve_ISO_K_DN63_310VEP063-01"
    cited_fact_or_basis: "The Pfeiffer online shop route lists housing as Aluminum, feedthrough as Bellows/Stainless steel, and seal as FKM. Local assembly STEP material extraction returned only Generic with density 1000.0 for this product, so it was treated as placeholder metadata. official_alternate_route_check: the BOM URL is the Pfeiffer product route for 310VEP063_02; the vacuum-shop.com page is an official Pfeiffer Vacuum shop page and matches order number 310VEP063-02."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Electrical and pneumatic actuator subcomponent materials are not itemized by the accessible product facts, so the material set is partial but adequate for coarse BOM modeling."
how_to_make:
  summary: "Treat as a purchased Pfeiffer Vacuum valve module for near-term KB closure; install it into the ISO-K vacuum line with compatible DN 63 hardware, clean sealing practice, compressed-air supply, and 24 V DC electrical connection."
  manufacturing_steps:
    - "Procure Pfeiffer 310VEP063-02 / EVB 063 PA DN 63 ISO-K electro-pneumatic angle valve as a complete tested valve module."
    - "Inspect product identity and sealing surfaces, keeping protective covers in place until installation."
    - "Mount to clean ISO-K counter flanges using suitable ISO-K connection components."
    - "Connect clean dry or slightly oiled compressed air in the specified pressure range and connect the 24 V DC pilot valve/position-indicator wiring."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/310VEP063_02; https://www.vacuum-shop.com/shop/en_US/category/2073371/product/310vep06302/%7B%7Bresult.url%7D%7D; https://vacuum-shop.com/2075819/downloads/manuals/vp0002ben.pdf"
    cited_fact_or_basis: "The Pfeiffer shop route identifies 310VEP063-02 as a purchasable EVB 063 PA angle valve with DN 63 ISO-K connection, electro-pneumatic actuator, 24 V DC input, and compressed-air requirement. The operating instructions state scope of delivery as one angle valve plus operating instructions and describe installation on a system with appropriate ISO-K flange components, clean sealing surfaces, compressed air, and electrical connection. official_alternate_route_check: the BOM-provided Pfeiffer URL identifies the 310VEP063_02 product route; the vacuum-shop.com page and manual are official Pfeiffer Vacuum routes for the same product family/order number."
    evidence_basis: "bom_provided"
  assumptions:
    - "No local sub-BOM or calibration workflow is available, so procurement and installation is the appropriate route for this research row."
  uncertainty_notes:
    - "A self-manufacturing route would require a separate decomposition of valve body machining, bellows/feedthrough manufacture, sealing surfaces, actuator, pilot valve, microswitch, leak testing, and qualification."
kb_implications:
  - "item_granularity: purchased_module - Model as a vendor valve module for now because it is a calibrated multi-material vacuum component with actuator, seals, feedthrough, and position-indicator hardware; later self-manufacturing would need a sub-BOM and leak-test workflow."
---

Research result for reAM250 BOM row 113.
