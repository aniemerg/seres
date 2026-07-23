---
row_identity:
  item: "3X3"
  cad_file: "3X3_valve_part_3"
  source_row_number: 166
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html"
function:
  summary: "Manual ISO-KF DN40 disc valve used to open, close, or throttle powder/fluid flow at a DN40 clamp-flange interface in the reAM250 powder handling path."
  source:
    url_or_path: "https://www.amproved.com/iso-kf-dn-40-scheibenventil.html"
    cited_fact_or_basis: "AMPROVED describes the ISO-KF DN40 Scheibenventil as a manual valve for controlling fluid streams in pipework, suitable for closing powder bottles, overflows, and filling ports in AM machines; the delivered item has 3 detent positions. official_alternate_route_check: BOM URL https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html resolves to the same AMPROVED product family/page title and row-matched DN40 disc-valve description at https://www.amproved.com/iso-kf-dn-40-scheibenventil.html."
    evidence_basis: "bom_provided"
  assumptions:
    - "The reAM250 row label 3X3 refers to this purchased AMPROVED DN40 valve, not to a separate locally designed subpart."
  uncertainty_notes:
    - "The BOM does not name the exact reAM250 subsystem, so the powder-handling placement is inferred from AMPROVED's stated AM-machine use case and the DN40 valve geometry."
mass:
  value_kg: 1.23
  basis: "Per unit for BOM quantity 1. FreeCAD measured one STEP solid with volume 153137.310 mm3 and bounding box 72.00 x 97.00 x 97.00 mm. Treating the modeled volume as mostly stainless steel and using the local stainless_steel density constant 8000 kg/m3 gives 153137.310e-9 m3 * 8000 kg/m3 = 1.225 kg, rounded to 1.23 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3X3_valve_part_3.step; kb/materials/properties.yaml; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "FreeCAD measured 1 solid, 153137.310197 mm3 volume, 44760.363860 mm2 area, and 72.0 x 97.000166 x 97.0 mm bounding box. The BOM row description says _aisi_316l-1_4404_-_epdm: part 3. kb/materials/properties.yaml lists stainless_steel density as 8000 kg/m3. targeted_web_search: queries tried 'AMPROVED ISO-KF DN 40 Scheibenventil weight' and 'AMPROVED DN40 disc valve 316L EPDM weight'; no row-specific AMPROVED mass was found, while a similar DN40 316/EPDM valve page listed 1.61 kg and was used only as a sanity check, not as the row mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid represents the physical envelope/volume of the purchased valve closely enough for a coarse BOM mass estimate."
    - "The valve is treated as predominantly stainless steel; EPDM seal volume is present but not separately modeled."
  uncertainty_notes:
    - "STEP assembly material metadata for this product returned only Generic at density 1000.0, which is a placeholder and was not used."
    - "Because the valve is a multi-material purchased component and the CAD does not split stainless and EPDM volumes, the per-unit mass is an engineering estimate rather than a catalog weight."
material:
  primary_material: "AISI 316L / EN 1.4404 stainless steel body and valve hardware with EPDM sealing element."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "BOM row 166 description/product ID field states '_aisi_316l-1_4404_-_epdm: part 3' for item 3X3 from AMPROVED."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local STEP material extractor returned only Generic/1000.0 metadata, so it did not independently confirm the BOM material text."
    - "The BOM text gives the material set but not the exact fraction or grade certification for each valve subcomponent."
how_to_make:
  summary: "Treat as a external ISO-KF DN40 manual valve module for KB planning. A plausible manufacturing route is machining/forming 316L stainless valve body and KF flange features, fitting the rotating disc/shaft and detent handle, installing an EPDM seal, then leak/function testing as a row-matched assembly"
  manufacturing_steps:
    - "Fabricate 316L/1.4404 stainless valve body, DN40 KF flange geometry, disc, shaft, handle, and fasteners"
    - "Machine sealing, bore, clamp, and detent features; deburr and clean for powder/vacuum service."
    - "Install EPDM seal and rotating disc/handle assembly."
    - "Perform manual actuation, sealing, and leak/function checks before installation in the reAM250 assembly."
  source:
    url_or_path: "https://www.amproved.com/iso-kf-dn-40-scheibenventil.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv"
    cited_fact_or_basis: "The manifest classifies the row CAD as a vendor_component; AMPROVED sells the ISO-KF DN40 disc valve as a delivered product with 3 detent positions. official_alternate_route_check: BOM URL https://www.amproved.com/amproved-produkte1/iso-kf-dn-40-scheibenventil.html and alternate AMPROVED URL https://www.amproved.com/iso-kf-dn-40-scheibenventil.html are same manufacturer/domain and same DN40 Scheibenventil product."
    evidence_basis: "bom_provided"
  assumptions:
    - "For near-term KB closure, buying this as a valve module is more appropriate than modeling every valve subcomponent."
  uncertainty_notes:
    - "The AMPROVED page provides product/function facts but not a full manufacturing process sheet; manufacturing steps are a plausible route for a 316L/EPDM manual valve."
kb_implications:
  - "item_granularity: complex_module - Model 3X3 as one DN40 316L/EPDM manual disc valve module rather than separate flange, disc, handle, and seal parts unless valve manufacturing becomes a priority.; defer internal decomposition until a focused sub-BOM and manufacturing workflow are modeled."
---

