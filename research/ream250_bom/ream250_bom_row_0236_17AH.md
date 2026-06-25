---
row_identity:
  item: "17AH"
  cad_file: "17AH_profile_60x60_350"
  source_row_number: 236
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Cut 350 mm length of 60 x 60 mm slotted structural profile, likely used as a stiff modular frame rail or spacer/member in the reAM250 structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0236_17AH__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/instances/17AH_profile_60x60_350__94_profile_60x60_350.step"
    cited_fact_or_basis: "BOM row 236 lists item 17AH, quantity 2, cad_file 17AH_profile_60x60_350. Manifest row 236 records no canonical 17AH STEP but lists two ambiguous similar 60x60x350 profile instances. FreeCAD measured the alternate instance as one solid with bounding box 350.00 x 60.00 x 60.00 mm, and the contact-sheet preview shows a long square slotted extrusion."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is interpreted as a cut-to-length modular structural profile rather than a machined solid bar because the BOM filename and ambiguous CAD preview both indicate a 60x60 slotted profile."
  uncertainty_notes:
    - "The manifest says no 17AH-prefixed product was found in the raw STEP and the measured STEP instance is an ambiguous similar item 94 profile, so the frame-member function is likely but not proven from a canonical 17AH CAD file."
mass:
  value_kg: 1.37
  basis: "Per-unit estimate. The ambiguous alternate STEP volume is 506015.224 mm^3, or 0.000506015 m^3. Using aluminum density 2700 kg/m^3 from kb/materials/properties.yaml gives 1.366 kg per 350 mm profile. This corresponds to 3.90 kg/m, close to published heavy 60x60 aluminum-profile values around 3.6-3.923 kg/m; using 3.923 kg/m for 0.350 m gives 1.373 kg. BOM quantity is 2, so row total is about 2.74 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/instances/17AH_profile_60x60_350__94_profile_60x60_350.step; kb/materials/properties.yaml; https://www.item24.com/en-ro/profile-6-60x60-natural-41903; https://www.myaluprofil.de/Aluminium-profile-60x60-Heavy-groove-10-B-type.html?language=en; https://haluminium.com/Products/60-series-t-slot-aluminium-extrusion-profile/"
    cited_fact_or_basis: "FreeCAD measured the ambiguous alternate STEP volume as 506015.224 mm^3 and bounding box as 350.00 x 60.00 x 60.00 mm. The local density table lists aluminum density 2700 kg/m^3. Item24 lists a 60x60 anodized aluminum profile at 3.6 kg/m. myaluprofil lists a heavy 60x60 B-type aluminum profile at 3.923 kg/m. Hoonly lists 60x60 T-slot profile variants from 2.80 to 4.20 kg/m. targeted_web_search: searched '17AH profile_60x60_350', '17AH 60x60 aluminium profile', '60x60 aluminium extrusion profile weight per meter material', and 'aluminium profile 60x60 slot 8 weight kg/m 350 mm'; no row-specific 17AH vendor mass was found, only standard 60x60 aluminum-profile family data."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The ambiguous similar STEP profile is used as the best available geometry proxy for the missing canonical 17AH CAD."
    - "The row item is an aluminum T-slot/profile extrusion, consistent with the CAD shape and standard 60x60 machine-frame profile convention."
  uncertainty_notes:
    - "If 17AH was a lighter or heavier proprietary profile than the ambiguous CAD proxy, per-unit mass could vary across roughly 1.0-1.5 kg for this 350 mm length based on common 60x60 profile variants."
material:
  primary_material: "anodized aluminum extrusion, exact alloy not specified"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0236_17AH__views_2x2.png; https://www.item24.com/en-ro/profile-6-60x60-natural-41903; https://www.myaluprofil.de/Aluminium-profile-60x60-Heavy-groove-10-B-type.html?language=en; https://haluminium.com/Products/60-series-t-slot-aluminium-extrusion-profile/"
    cited_fact_or_basis: "The assembly STEP material extractor found no product-name match for 17AH_profile_60x60_350. The contact-sheet preview shows a slotted machine-frame extrusion. Item24 describes a 60x60 profile as anodized aluminum. myaluprofil lists a 60x60 heavy profile as AlMgSi0.5F25 natural anodized. Hoonly identifies 60-series T-slot profiles as aluminum extrusion profiles. targeted_web_search: searched '17AH profile_60x60_350 material', '17AH 60x60 aluminium profile', and '60x60 aluminium extrusion profile material'; no row-specific 17AH material source was found, but standard 60x60 machine-frame profiles are consistently aluminum/anodized aluminum."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The 60x60 slotted profile convention is applicable to this row despite the missing canonical CAD and missing manufacturer field."
  uncertainty_notes:
    - "Exact alloy, temper, and anodize specification are unresolved; downstream KB modeling should use aluminum/anodized aluminum rather than a specific alloy grade unless a later source identifies the 17AH supplier."
how_to_make:
  summary: "Prepare as a standard 60 x 60 mm anodized aluminum machine-frame profile cut to 350 mm, or locally make by aluminum extrusion, straightening/aging, anodizing, saw cutting, and deburring"
  manufacturing_steps:
    - "Cut two 350 mm lengths for the BOM row"
    - "Manufacturing route: extrude aluminum alloy through a die forming the 60 x 60 mm slotted cross-section."
    - "Straighten and age or stress-relieve according to alloy/process practice, then anodize for the standard corrosion-resistant surface."
    - "Saw-cut to 350 mm, deburr the ends, and add any required end tapping or drilled features if later assembly evidence requires them."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0236_17AH__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/instances/17AH_profile_60x60_350__94_profile_60x60_350.step; https://www.item24.com/en-ro/profile-6-60x60-natural-41903; https://haluminium.com/Products/60-series-t-slot-aluminium-extrusion-profile/"
    cited_fact_or_basis: "The CAD proxy and preview show a 350 x 60 x 60 mm slotted extrusion. Item24 describes 60x60 anodized aluminum construction profiles delivered as individual/cut lengths. Hoonly describes 60-series T-slot aluminum extrusion profiles used for machine frames, safety guards, workstations, conveyors, and multi-axis positioning systems. The detailed extrusion, straightening, anodizing, cutting, and deburring sequence is inferred from the standard profile geometry and material rather than stated for row 17AH. targeted_web_search: searched '17AH profile_60x60_350 manufacturing', '60x60 aluminium extrusion profile cut to length', and '60 series T-slot aluminium extrusion profile machine frame'; results supported standard profile procurement/use but did not provide a row-specific factory route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "For later KB modeling, the base item should be a reusable cut-to-length 60x60 aluminum profile rather than a unique reAM250-only machined component."
    - "End features are not modeled because the row name and ambiguous CAD preview do not show or encode specific tapping/drilling requirements."
  uncertainty_notes:
    - "A later canonical drawing or vendor row could change the exact profile series, slot size, alloy, or end machining while preserving the same broad extrusion-and-cut manufacturing route."
kb_implications:
  - "item_granularity: simple_part - model as a reusable cut-to-length 60x60 anodized aluminum structural profile, with length and any end machining captured in BOM/recipe notes instead of creating a unique item for every profile length."
---

# reAM250 BOM Row 236 - 17AH

Research result for the leased reAM250 BOM row.
