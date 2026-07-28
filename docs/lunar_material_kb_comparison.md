# Lunar Material Availability vs Current KB

Date: 2026-07-21

This document compares the source-derived lunar material availability notes with
the current KB. It is intended to guide future machine-design additions and KB
material modeling work.

Primary source inventory: `/home/eastrolinux/papers/ISRU/Knowledge_from_papers/lunar_materials_inventory.md`.

## Current Raw Material Coverage

The KB currently has these explicit in-situ or environmental source items in
`kb/items/raw_materials/`:

| Raw item | Current role | Coverage assessment |
|---|---|---|
| `lunar_regolith_in_situ` | Generic in-place regolith | Useful generic source, but less composition-specific than mare/highland items. |
| `regolith_lunar_mare` | Iron/titanium-rich mare regolith | Covers mare feedstock for ilmenite, iron, titanium, oxygen, basaltic processing. |
| `regolith_lunar_highlands` | Aluminum/calcium-rich highland regolith | Covers anorthite/alumina/aluminum/calcium/silica paths. |
| `regolith_lunar_polar` | Polar regolith, potentially ice-bearing | Broad polar source. |
| `regolith_polar_psc` | Ice-bearing permanently shadowed crater regolith | Good specific source for water extraction. |
| `regolith_carbonaceous` | Carbonaceous chondrite impact material | Good source concept for carbon and volatiles, but site-limited. |
| `nife_meteorite_material` | Nickel-iron meteoritic metal | Good source concept for Ni/Fe and trace refractory metals. |
| `solar_irradiance` | Solar energy | Energy source, not a material feedstock. |
| `solar_radiation` | Solar energy | Energy source, not a material feedstock. |

## Coverage Table

| Source-derived material family | KB coverage | Status | Recommendation |
|---|---|---|---|
| Bulk lunar regolith | `lunar_regolith_in_situ`, `regolith_lunar_mare`, `regolith_lunar_highlands`, `regolith_lunar_polar` | Strong | Use existing raw items. Do not create generic duplicates. |
| Mare regolith / mare basalt | `regolith_lunar_mare`, `basalt_aggregate`, `basalt_molten`, `basalt_fiber`, `molten_basalt` | Mostly covered | Use `regolith_lunar_mare` for source closure. Add a dedicated mare basalt source only if a recipe needs rock/basalt distinct from regolith. |
| Pyroclastic / impact glass / agglutinates | General glass and basalt materials exist; no dedicated raw source | Partial | Use existing glass/basalt route unless deposit-specific sourcing matters. Add `pyroclastic_glass` only for a design or process that depends on glass-rich deposits. |
| Highland regolith / anorthosite | `regolith_lunar_highlands`, `anorthite_ore`, `plagioclase_feldspar` | Strong | Use existing highland/anorthite route. Add source tags/provenance when touched. |
| Polar PSC water ice | `regolith_polar_psc`, `water`, `polar_water_ice_extraction_v0` | Strong | Use as `site_sensitive`; do not hide water dependence in generic materials. |
| Carbonaceous impact material | `regolith_carbonaceous`, `carbon_reductant` routes | Moderate | Useful for carbon, but mark as localized and scarce in design notes. |
| NiFe meteorite material | `nife_meteorite_material`, `meteorite_iron`, `nickel_metal`, `tungsten_concentrate` routes | Moderate | Watch for overlap between `nife_meteorite_material` and `meteorite_iron`; consolidate references over time if one becomes canonical. |
| Anorthite / plagioclase | `anorthite_ore`, `plagioclase_feldspar`, anorthite extraction processes | Strong | Preferred highland source for Al/Ca/Si/O materials. |
| Pyroxene | `pyroxene_concentrate`, `enstatite` | Moderate | Present as concentrate; keep as secondary feedstock unless a machine design specifically needs it. |
| Olivine | `olivine_concentrate`, `olivine_powder`, Mg/Si routes | Moderate | Good for Mg/Si/O concepts; use with site and beneficiation assumptions. |
| Ilmenite | `ilmenite_concentrate`, `iron_ore_or_ilmenite`, Fe/Ti/O routes | Strong | Preferred mare route for Fe/Ti/O. Keep high-Ti mare assumption explicit. |
| Oxygen | `oxygen_gas`, MRE/carbothermal/water electrolysis paths | Strong | Good local-derived material, usually process coproduct. |
| Silica / silicon | `silica_purified`, `fused_silica`, `silicon_metal_v0`, silicon purification routes | Strong for industrial use | Treat semiconductor-grade silicon as advanced unless closure proves purification and dopants. |
| Aluminum / alumina | `alumina_crude`, `alumina_powder`, `alumina_ceramic_v0`, `aluminum_metal_pure`, `aluminum_ingot` | Strong conceptually | Good design family; verify specific recipe path and energy model for candidate machines. |
| Iron / steel-like materials | `iron_metal`, `iron_metal_pure`, `iron_pig_or_ingot`, many steel stock items | Strong but carbon-limited | Prefer low-carbon iron/steel-like designs. True steel quality depends on scarce carbon/alloy inputs. |
| Titanium / titania | `titanium_metal`, `titanium_oxide`, `ferrotitanium_alloy`, ilmenite FFC routes | Moderate to strong | Good for selected components; not the default bulk structure unless justified. |
| Magnesium / magnesia | `magnesium_oxide`, `magnesium_metal_v0`, `magnesia_refractory_v0`, Mg-Si routes | Moderate | Useful for refractories and cement chemistry; avoid Mg metal where vacuum/outgassing concerns matter. |
| Calcium / quicklime | `calcium_oxide`, `calcium_metal`, `calcium_hydroxide`, anorthite/CaO processes | Moderate to strong | Useful for cement/ceramic chemistry; prefer CaO/lime over calcium metal unless required. |
| Spinel | `spinel_ore`, `spinel_ceramic_v0` | Present | Keep as moderate/specialty ceramic; add measured route detail only if a design needs it. |
| Chromite / chromium | `chromite_refractory_v0`, `chromium_metal`, `chromium_metal_pure` import | Weak to moderate | Treat as scarce/specialty. Do not use chromium-heavy alloys as a baseline. |
| Manganese | Mentioned in generic alloy/ferrite contexts, but no strong source route found | Weak | Avoid Mn-dependent alloys or MnZn ferrites as baseline local materials. |
| KREEP / REE / P / U / Th | `ree_extraction_kreep_v0`, `phosphorus_white`, `orthoclase_feldspar` currently import | Partial | Add dedicated `kreep_basalt` or `apatite_bearing_regolith` only when KREEP-dependent designs need explicit site closure. |
| Potassium | `orthoclase_feldspar`, `potassium_chloride`, `potassium_hydroxide`, `potassium_nitrate` | Partial | Existing chemistry is useful, but source locality is KREEP/orthoclase-sensitive. Treat K compounds as recycle-critical. |
| Water / hydrogen | `water`, `hydrogen_gas`, polar and electrolysis processes | Strong but site-sensitive | Design for recycle. Avoid open-loop water/hydrogen consumption in generic machine BOMs. |
| Carbon / CO / CO2 / CH4 | Carbon and syngas materials/processes exist | Moderate but scarce | Treat as `scarce_trace` or `site_sensitive`. Minimize polymers, carbon reductant losses, and carbon-bearing consumables. |
| Nitrogen / ammonia | `nitrogen_gas_regolith`, `ammonia_gas`, Haber/Ostwald/Solvay-related routes | Moderate but scarce | Mark as recycle-critical; do not make nitrogen consumables casual BOM items. |
| Sulfur / H2S / troilite | `troilite`, `sulfur_elemental`, `hydrogen_sulfide_gas`, Claus route | Moderate but localized | Useful chemical family, but mark as site/meteorite dependent. |
| Helium / helium-3 / noble gases | `helium_mixed_isotopes`, `helium_3_gas`, `helium_4_gas`, `noble_gas_extraction_v0` | Present but low practical value | Keep as advanced/niche. Do not use for near-term machine design assumptions. |
| Copper | `copper_rod_ingot` is import; many copper downstream materials exist | Weak | Avoid copper-heavy baseline designs. Keep copper explicit as import unless a local route is intentionally modeled. |
| Zinc | `zinc_metal_v0` is import | Weak | Avoid brass/galvanized designs unless import is acceptable. |
| Sodium / chlorine / fluorine | Sodium/chloride materials and fluorite placeholder exist | Weak to moderate | Review abundance assumptions. Treat salts and halogens as recycle-critical, not bulk expendables. |
| Niobium / tantalum / refractory trace metals | Tungsten routes exist; Ta/Nb mostly appear in part notes or specialty contexts | Weak | Do not create baseline W/Ta/Nb dependence. Use only for low-mass critical components with explicit closure/import. |
| Lithium / boron / zirconium | Lithium appears in battery notes, boron mostly in NdFeB/borosilicate context, zirconia exists as ceramic item | Weak | Treat Li, B, Zr/Y-derived zirconia as import/research unless a dedicated source route is modeled. |
| Mercury | Mentioned as volatile/special-use context; no mainstream material route | Weak | Treat as contaminant or niche trace material, not a machine design feedstock. |
| PGM / platinum catalysts | Platinum appears in catalyst/curing contexts but no robust lunar route | Weak | Prefer lunar alternatives such as nickel/tungsten-carbide catalysts when modeled; otherwise import explicitly. |
| Ferrites / magnetite | `magnetite_ore`, `mnzn_ferrite_v0`, `nife2o4_soft_ferrite_v0`, `cofe2o4_hard_ferrite_v0`, ferrite core parts/processes | Partial | Iron-oxide ferrites are plausible; Ni/Zn/Co ferrites inherit trace-material risk. Treat high-performance ferrites as advanced. |
| Kovar / Alnico / permalloy / supermalloy | `kovar_alloy_fe_ni_co_v0`, `alnico_*`, `permalloy_high_permeability_v0`, `supermalloy` | Partial | These are useful seeds but depend on Ni/Co and sometimes Cu/Mo/Mn. Avoid as hidden baseline dependencies. |
| Quartz / fused silica | `fused_silica`, `quartz_crystal`, quartz sensor/envelope recipes | Moderate | Fused silica is a good local-derived material; high-purity quartz crystals/sensors need separate closure confidence. |
| Polymers / elastomers / lubricants | Many are imports or depend on scarce volatile chemistry | Weak | Keep explicit in BOMs. Prefer ceramic/metal alternatives where practical. |

## Main Findings

The KB already covers the major lunar engineering families well enough for
machine design screening:

- regolith, mare regolith, highland regolith, polar PSC regolith
- anorthite/plagioclase, ilmenite, olivine, pyroxene
- oxygen, water, silica/silicon, alumina/aluminum, iron, titanium, magnesium,
  calcium, glass, ceramics, sintered regolith

The KB is weaker where the source notes also advise caution:

- KREEP-specific feedstocks are not first-class source items yet.
- Pyroclastic glass, impact glass, agglutinates, and basaltic rock are mostly
  represented through derived basalt/glass materials, not dedicated site/source
  items.
- Copper, zinc, sodium, halogens, chromium, manganese, REE, noble gases,
  helium-3, carbon, nitrogen, sulfur, Li, B, Zr, Nb, Ta, W, and PGM need stronger
  scarcity/site notes if they become important to a machine design.
- Magnetic and electronic materials exist as useful seeds, but many depend on
  scarce trace elements: Kovar/Alnico/permalloy on Ni/Co, MnZn ferrites on Mn/Zn,
  NdFeB on REE/B, zirconia ceramics on Zr/Y, and refractory electrodes on W/Ta.
- Several routes are placeholders or optimistic closure aids. They should not be
  treated as equal to high-confidence bulk materials.

## Recommended KB Policy

Do not add a blanket `available_on_moon: true` field to materials. It would hide
the distinction between abundance, site access, processing difficulty, and KB
closure.

Instead:

1. Use `docs/lunar_material_availability_guide.md` when choosing materials for
   new machine designs.
2. Put material rationale in machine/BOM `notes`.
3. Use explicit local raw materials and recipes for closure-critical materials.
4. Mark imports explicitly with `is_import: true` when the KB route is absent or
   not worth modeling yet.
5. Add source-specific raw materials only when a machine or process actually
   needs that distinction.

## Candidate Future Additions

These are not recommended as immediate bulk additions. Add them only when a
specific machine design, process, or scenario needs them.

| Candidate item | Why it may help | Conservative alternative |
|---|---|---|
| `kreep_basalt` | Makes REE/P/K source locality explicit | Continue using `basalt_aggregate` with KREEP notes in advanced recipes. |
| `apatite_bearing_regolith` | Better source for phosphorus, F/Cl-bearing apatite | Keep phosphorus extraction notes tied to KREEP until needed. |
| `pyroclastic_glass` | Useful for glass-rich volcanic deposits | Use `regolith_lunar_mare` or `basalt_aggregate` unless glass deposit matters. |
| `impact_glass_or_agglutinate` | Captures impact-melt/agglutinate glass feedstock and possible siderophile enrichment | Use existing glass/basalt routes unless trace-metal enrichment matters. |
| `mare_basaltic_rock` | Distinguishes rock/aggregate from granular regolith | Use `regolith_lunar_mare` feeding `basalt_aggregate` for now. |
| `chromite_bearing_regolith` | Better source for chromite/chromium route | Keep `chromite_refractory_v0` as specialty placeholder. |
| `orthoclase_or_k_feldspar_source` | Clarifies potassium/KREEP sourcing for KCl/KOH routes | Keep `orthoclase_feldspar` import until a KREEP source is needed. |
| `volatile_bearing_regolith` | Generic non-PSC volatile source | Use `regolith_lunar_polar`, `regolith_polar_psc`, or explicit volatile processes. |

## Machine Design Workflow

When adding a new machine:

1. Draft the BOM using preferred baseline materials from the guide.
2. Run:

```bash
python -m src.cli closure --machine <machine_id>
```

3. Label critical materials:
   `local_raw`, `local_derived`, `site_sensitive`, `scarce_trace`,
   `import_or_recycle`, or `unknown_in_kb`.
4. If a critical material is `unknown_in_kb`, either redesign around an existing
   material or add a research task before creating new source/process items.
5. If a critical material is `import_or_recycle`, keep it explicit in the BOM so
   import mass remains visible.
