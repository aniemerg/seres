---
row_identity:
  item: "6M2"
  cad_file: "6M2_rail_LEFG32-S-600N"
  source_row_number: 190
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.smcpneumatics.com/LEFG32-S-600.html"
function:
  summary: "Passive SMC LEFG32-S-600 support-guide rail for the top linear guide axis; it supports an overhanging workpiece/platform and shares the LEF body envelope for pairing with a driven LEF slider."
  source:
    url_or_path: "https://www.smcusa.com/products/electric-actuators/sliders/support-guide~137707; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0190_6M2__views_2x2.png"
    cited_fact_or_basis: "BOM row 190 names item 6M2 as 'linear guide top' from SMC Pneumatics with product route LEFG32-S-600. SMC USA describes LEFG as a motorless support guide with LEFS/LEFB-compatible dimensions for supporting significantly overhanging workpieces. CAD preview shows a long rail/profile body with support-guide geometry. official_alternate_route_check: original BOM URL is https://www.smcpneumatics.com/LEFG32-S-600.html; direct browser fetch was blocked, but the URL/search route identified exact part LEFG32-S-600, and the SMC USA manufacturer support-guide page matches the same LEFG product family and function."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row's 'rail' CAD export represents the fixed/support-guide body of the LEFG32-S-600 rather than the separate moving carriage captured in row 189."
  uncertainty_notes: []
mass:
  value_kg: 2.88
  basis: "Best row-level mass is 2.88 kg for quantity 1. The SMC LEFG/11-LEFG support-guide catalog weight table lists the size-32, S mounting-pitch, 600 mm stroke entry as 2.88 kg. Local CAD measurement gives one solid, volume 2100746.154 mm^3, area 187894.453 mm^2, and bounding box 70.00 x 49.82 x 750.00 mm; the 750 mm CAD length matches the catalog LEFG32-S-600 overall length."
  source:
    url_or_path: "https://content2.smcetech.com/pdf/11_LEFG.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6M2_rail_LEFG32-S-600N.step"
    cited_fact_or_basis: "SMC support-guide catalog weight table reports 2.88 kg for 11-LEFG32-S at 600 mm stroke and dimensions L=750, A=607, B=730 for 11-LEFG32-S-600. FreeCAD measured the row STEP as one solid with 2100746.154 mm^3 volume and 70.00 x 49.82 x 750.00 mm bounding box. bom_url_route_check: the BOM URL identifies exact product LEFG32-S-600 but was not directly fetchable; the SMC catalog route supplies the row-matched size, mounting pitch, stroke, dimensions, and weight used here."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The clean-series 11-LEFG32-S-600 catalog mass is an acceptable proxy for the BOM's LEFG32-S-600N row because the row CAD length and SMC family dimensions match; any clean/vacuum-port variant difference is treated as second-order for this BOM estimate."
  uncertainty_notes:
    - "The row STEP is a simplified vendor-component solid and the assembly STEP material metadata is only placeholder Generic at density 1000, so CAD volume was used for geometry confirmation rather than density-derived mass."
material:
  primary_material: "Aluminum-alloy actuator/support-guide body with steel guide/seal hardware and polymer or elastomer sealing components."
  source:
    url_or_path: "https://www.smcworld.com/assets/manual/en-jp/files/LEF-OM002xx.pdf; https://content2.smcetech.com/pdf/11_LEFG.pdf"
    cited_fact_or_basis: "SMC LEF series construction tables list the slider body and table as aluminum alloy/anodized, seal-band holders and slide bearings as synthetic resin, rubber bushing as NBR, and band stopper/dust seal band/roller shaft as stainless steel; rail guide and bearings are listed as separate guide hardware without a grade. The SMC 11-LEFG catalog identifies the support guide as the same LEF-family support guide with seal bands. bom_url_route_check: the BOM URL names the exact LEFG32-S-600 but did not expose material data in the fetchable route; manufacturer catalog/manual routes for the same LEF/LEFG family were used for material-family evidence."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row's rail/support-guide body uses the LEF/LEFG family material stack rather than a row-specific custom material."
  uncertainty_notes:
    - "No row-specific material metadata was present in the STEP package beyond placeholder Generic; exact alloy grade, rail steel grade, and seal polymer grade remain unspecified."
how_to_make:
  summary: "Aluminum extrusion or machined/anodized body production, precision steel guide/rail and bearing hardware production or grinding, seal-band installation, and final alignment/inspection as a linear-guide support module"
  manufacturing_steps:
    - "Local-manufacturing route: make or source the aluminum support-guide body/profile, machine mounting features, anodize the aluminum surfaces, fit precision steel guide/bearing hardware, install stainless or polymer seal-band components, then align and inspect against the mating LEF driven axis."
  source:
    url_or_path: "https://www.smcusa.com/products/electric-actuators/sliders/support-guide~137707; research/ream250_bom/ream250_bom_row_0190_6M2__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6M2_rail_LEFG32-S-600N.step"
    cited_fact_or_basis: "SMC describes the LEFG as a motorless support guide sharing LEFS/LEFB dimensions and using a seal band. CAD preview/STEP geometry show a long rail-like support body with mounting features. The detailed local fabrication sequence is inferred from the observed geometry and material family, not directly stated by the cited catalog. targeted_web_search: queries tried included 'SMC LEFG support guide material aluminum steel seal band', 'LEFG32-S-600 weight LEFG32-S 600 kg catalog', and 'SMC LEFG32-S-600 linear guide actuator specifications material weight'; results resolved product family, dimensions, mass, and broad material stack but did not provide a row-specific manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "For KB planning, this row is better represented initially as a external SMC linear-support module unless a detailed sub-BOM for guide rail, carriage, seals, bearings, and alignment operations is later introduced"
  uncertainty_notes:
    - "The manufacturing route omits precision tolerances, preload/bearing details, and vendor quality-control steps that would matter for a self-manufactured replacement."
kb_implications:
  - "item_granularity: simple_part - Treat 6M2 as the rail/body portion of the SMC LEFG32-S-600 support-guide pair; keep the complete LEFG support guide as a later module only if rows 6M1, 6M2, seal-band parts, and guide hardware are explicitly recombined."
---
