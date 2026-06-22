---
row_identity:
  item: "3K"
  cad_file: "3K_flexible_pipe_ISO_K_DN63_320SWN063-0250"
  source_row_number: 122
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320SFK063_130"
function:
  summary: "Flexible corrugated ISO-K DN 63 vacuum hose used to connect vacuum components while allowing short run misalignment or vibration compliance."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3K_flexible_pipe_ISO_K_DN63_320SWN063-0250.step; https://www.pfeiffer-vacuum.com/global/en/shop/products/320SWN063_0250"
    cited_fact_or_basis: "BOM row 122 identifies item 3K as a Pfeiffer Vacuum flexible pipe, and the CAD filename contains 320SWN063-0250. The official Pfeiffer/Busch product page for 320SWN063-0250 identifies a corrugated hose, flexible, stainless steel, DN 63 ISO-K, length 250 mm. FreeCAD measured the row STEP bounding box as 250.00 x 105.13 x 105.13 mm. bom_url_route_check: the BOM link points to 320SFK063_130, a related Pfeiffer flexible-pipe route that does not match the row CAD suffix 320SWN063-0250 or 250 mm length; the official exact-product page was used because it matches the row CAD filename and raw row text."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The required preview render did not produce a contact sheet before timeout, so visual confirmation is limited to STEP geometry measurements and product identity rather than rendered shape triage."
mass:
  value_kg: 1.055
  basis: "FreeCAD measured one CAD solid volume as 131815.947 mm^3. Treating the hose as stainless steel and using the local generic stainless_steel density 8000 kg/m^3 gives 131815.947e-9 m^3 * 8000 kg/m^3 = 1.055 kg per flexible hose. BOM quantity is 1, so the row total is also about 1.055 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3K_flexible_pipe_ISO_K_DN63_320SWN063-0250.step; kb/materials/properties.yaml; https://www.pfeiffer-vacuum.com/global/en/shop/products/320SWN063_0250"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 131815.947 mm^3, area 343748.725 mm^2, and bounding box 250.00 x 105.13 x 105.13 mm. The official exact-product page identifies the row-matched item as stainless steel; the local density table gives generic stainless_steel as 8000 kg/m^3. bom_url_route_check: the BOM URL did not resolve the exact row length/order number, so the official 320SWN063-0250 page matching the CAD filename was used for material family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the per-unit metal volume for the physical corrugated hose."
    - "A single generic stainless density is adequate because the sourced flange and bellows stainless grades have similar densities at this planning precision."
  uncertainty_notes:
    - "This is a CAD-derived part mass, not a catalog shipping or weighed mass; weld details, flange-face finish, or CAD simplifications may shift the real mass."
    - "The preview render timeout prevented visual checking for omitted small features, but the STEP volume and bounding box were readable."
material:
  primary_material: "stainless steel: flange 1.4301 / AISI 304; bellows 316L"
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/en/shop/products/320SWN063_0250; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The official row-matched product route identifies the part as a stainless steel DN 63 ISO-K corrugated hose. Pfeiffer-family technical data for 320SWN063 corrugated hoses states material as stainless steel with flange 1.4301/304 and bellows 316L. bom_url_route_check: the BOM URL points to 320SFK063_130 and did not resolve the exact 320SWN063-0250 row; the exact official product route was selected from the CAD filename and raw row text."
    evidence_basis: "bom_provided"
  assumptions:
    - "The 320SWN063 corrugated-hose family material statement applies to the 250 mm length variant represented by this row."
  uncertainty_notes:
    - "Assembly STEP material metadata for this CAD object is only 'Generic' at density 1000, so embedded CAD material is not usable."
how_to_make:
  summary: "Procure as Pfeiffer 320SWN063-0250, or manufacture locally as a stainless corrugated vacuum hose with DN 63 ISO-K stainless flanges welded to a 316L bellows tube, followed by cleaning and leak testing."
  manufacturing_steps:
    - "Form or source a thin-wall 316L stainless corrugated bellows tube to the 250 mm nominal hose length."
    - "Machine or form stainless 1.4301/304 ISO-K DN 63 flange end pieces."
    - "Weld or braze the flange ends to the bellows tube while controlling heat input and preserving vacuum-clean internal surfaces."
    - "Clean, passivate if required, inspect ISO-K sealing dimensions, and helium leak-test for high-vacuum service."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3K_flexible_pipe_ISO_K_DN63_320SWN063-0250.step; https://www.pfeiffer-vacuum.com/global/en/shop/products/320SWN063_0250"
    cited_fact_or_basis: "The official exact-product route identifies a DN 63 ISO-K stainless flexible corrugated hose with 250 mm length, and the STEP measurement confirms a 250 mm long, roughly DN 63 hose envelope. targeted_web_search: searched 'Pfeiffer 320SWN063-0250 manufacturing corrugated hose stainless bellows', '320SWN063-0250 datasheet material flange bellows', and 'ISO-K DN63 corrugated hose manufacturing stainless bellows welded flange'; found row-matched product/material facts but no Pfeiffer factory process sheet for this row."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local route follows common stainless vacuum bellows hose fabrication practice inferred from the product geometry and material, not a Pfeiffer-published operation sheet."
    - "The row is better procured as a standard vendor vacuum component unless local bellows forming, weld cleanliness, and leak-test capability are modeled."
  uncertainty_notes:
    - "Exact factory details such as hydroforming versus mechanical convolution forming, weld type, and post-weld cleaning specification are not resolved."
kb_implications:
  - "item_granularity: simple_part - Model as reusable ISO-K DN 63 stainless corrugated hose hardware with length variants, not as a reAM250-specific assembly."
---
