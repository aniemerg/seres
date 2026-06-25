---
row_identity:
  item: "8D1"
  cad_file: "8D1_flexible_pipe_part_1"
  source_row_number: 210
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0250"
function:
  summary: "Thin annular end/flange component for the Pfeiffer Vacuum 120SWG040-0250 DN 40 ISO-KF flexible pipe assembly, providing one circular vacuum connection interface rather than representing the full hose."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8D1_flexible_pipe_part_1.step; research/ream250_bom/ream250_bom_row_0210_8D1__views_2x2.png"
    cited_fact_or_basis: "BOM row 210 identifies item 8D1 as Pfeiffer Vacuum 'part 1 120SWG040-0250: flexible pipe'; the manifest maps row 210 to 8D1_flexible_pipe_part_1.step; FreeCAD measured one solid with an approximately 5.32 x 56.28 x 56.28 mm bounding box; the rendered preview shows a thin circular ring/end feature."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row-specific CAD part is interpreted as one end/flange part of the 120SWG040-0250 flexible pipe because the BOM splits neighboring row 8D2 as part 2 of the same vendor product."
  uncertainty_notes:
    - "The CAD part represents an exported subcomponent of the flexible pipe, so the function is for this annular end part rather than the complete hose assembly."
mass:
  value_kg: 0.00249
  basis: "Per-unit mass for one CAD part. FreeCAD measured volume 309.686 mm^3, converted to 3.09686e-7 m^3; using local stainless_steel_304 density 8030 kg/m^3 gives 0.00249 kg. BOM quantity is 1, so the row total is also about 0.00249 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8D1_flexible_pipe_part_1.step; kb/materials/properties.yaml; https://vacuum-shop.com/2074220/downloads/datasheets/Datasheet_120SWG040-0250_en.pdf"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 309.686 mm^3 for 8D1_flexible_pipe_part_1.step; kb/materials/properties.yaml lists stainless_steel_304 density as 8030 kg/m^3; the row-matched 120SWG040-0250 datasheet identifies the DN 40 ISO-KF flexible hose flange material as stainless steel 1.4301/304. official_alternate_route_check: the original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0250 returned HTTP 403 to curl; the alternate PDF is a Pfeiffer Vacuum datasheet for the same 120SWG040-0250 product and same DN 40 ISO-KF family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the physical volume of one row item."
    - "The annular end part uses the stainless 304/1.4301 flange material from the matched 120SWG040-0250 flexible-pipe product family."
  uncertainty_notes:
    - "If the CAD export omits small weld beads, rolled edges, or other nonmodeled end-piece details, the true mass may be modestly higher."
material:
  primary_material: "Stainless steel 1.4301 / AISI 304 flange/end-ring material; the complete 120SWG040-0250 flexible pipe family also uses 316L stainless bellows."
  source:
    url_or_path: "https://vacuum-shop.com/2074220/downloads/datasheets/Datasheet_120SWG040-0250_en.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The row-matched 120SWG040-0250 datasheet identifies a DN 40 ISO-KF stainless flexible hose and lists flange material as stainless steel 1.4301/304 with 316L bellows; local assembly STEP material extraction for this CAD product returns only Generic material with density 1000, which does not resolve material. official_alternate_route_check: the original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0250 returned HTTP 403 to curl; the alternate PDF is a Pfeiffer Vacuum datasheet for the same 120SWG040-0250 product and same DN 40 ISO-KF family."
    evidence_basis: "bom_provided"
  assumptions:
    - "Because the rendered row CAD is the end-ring/flange-like subpart, the flange material is more applicable to this row than the bellows material."
  uncertainty_notes:
    - "The local STEP file does not carry a real material assignment for this subpart; material assignment depends on matching the row to the vendor product family."
how_to_make:
  summary: "Locally, model this as a stainless 304 annular ISO-KF end/flange part: cut or turn a ring blank, machine the vacuum sealing/profile features, deburr and clean for vacuum service, then weld or join it to the flexible hose assembly during later hose fabrication."
  manufacturing_steps:
    - "Start from stainless 304 / 1.4301 bar, tube, or near-net ring stock sized for the approximately 56 mm outside diameter and 5 mm axial thickness."
    - "Turn the outer diameter, inner bore, and side faces on a lathe; add the small flange/end profile features indicated by the CAD preview."
    - "Deburr, passivate or clean for vacuum service, and inspect the DN 40 ISO-KF sealing/interface geometry."
    - "Join to the stainless bellows or hose body in the later flexible-pipe assembly workflow."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8D1_flexible_pipe_part_1.step; research/ream250_bom/ream250_bom_row_0210_8D1__views_2x2.png; https://vacuum-shop.com/2074220/downloads/datasheets/Datasheet_120SWG040-0250_en.pdf"
    cited_fact_or_basis: "CAD evidence shows a one-piece thin annular geometry; the row-matched datasheet identifies the product family as a DN 40 ISO-KF flexible stainless hose and gives stainless 1.4301/304 flange material. targeted_web_search: queries tried included '120SWG040-0250 manufacturing flange', 'Pfeiffer 120SWG040-0250 datasheet flange material', and 'ISO-KF stainless flange manufacturing machining'; no row-specific source stated the manufacturing process for this exported subpart, so the route is inferred from geometry and material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A machined stainless ring is the simplest local route for this exported end/flange subpart at the BOM-row level."
    - "The eventual complete flexible pipe would need separate bellows forming and joining steps; those are outside this row's part-1 CAD scope."
  uncertainty_notes:
    - "Actual vendor production may use forming, stamping, or welded subfeatures not visible in the single exported STEP solid."
kb_implications:
  - "item_granularity: simple_part - Model row 8D1 as a simple stainless annular end/flange part of a standard flexible vacuum pipe assembly; represent hose length and complete bellows assembly behavior in related rows or later BOM notes rather than as a separate granularity label for this row."
---
