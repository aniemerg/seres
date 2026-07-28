# Lunar Material Availability Guide

Date: 2026-07-21

Purpose: guide material choices when adding new lunar machine designs to the KB.
This is a design aid, not a schema extension. A material being present on the
Moon does not mean the current KB can already close a local manufacturing path
to it.

Primary source inventory: `/home/eastrolinux/papers/ISRU/Knowledge_from_papers/lunar_materials_inventory.md`.

## Modeling Rule

Use three different questions when choosing materials:

1. Is the material naturally present on the Moon?
2. Is it available at the intended site and at useful concentration?
3. Does the KB have a recipe/process path from an in-situ raw material to the
   material required by the machine BOM?

For machine design, question 3 is authoritative. If closure cannot trace a BOM
material to `kb/items/raw_materials/` or to an explicit import, the design has an
unproven supply path in the current KB.

## Availability Classes

Use these labels in design notes and comparison tables:

| Label | Meaning | Design implication |
|---|---|---|
| `local_raw` | Direct in-situ source item exists in `kb/items/raw_materials/` | Good baseline input. |
| `local_derived` | Recipe/process route exists from local raw material | Good if the process equipment is acceptable. |
| `site_sensitive` | Availability depends strongly on mare, highland, polar PSC, KREEP, or impact-site access | Use only when site assumption is explicit. |
| `scarce_trace` | Present at trace or localized levels | Avoid large BOM mass; use only for critical low-mass functions. |
| `import_or_recycle` | Early lunar route is weak or absent | Treat as import unless closure proves otherwise. |
| `unknown_in_kb` | Literature suggests possible availability, but KB lacks a clear source or route | Add research task or source item only when needed. |

## Design Tiers

### Preferred Baseline Materials

Use these first for early lunar machine designs:

| Material family | Availability | Typical machine-design uses |
|---|---|---|
| Bulk regolith | `local_raw` | Shielding, thermal mass, sintered bricks, ceramic feedstock. |
| Sintered regolith / regolith ceramic | `local_derived` | Compression structures, foundations, low-precision tooling. |
| Silica / glass / aluminosilicate glass | `local_derived` | Insulators, windows, lenses, tubes, refractory-compatible parts. |
| Alumina ceramic | `local_derived` | Electrical insulation, wear parts, furnace linings, refractory parts. |
| Iron / low-alloy steel-like stock | `local_derived` | Frames, housings, shafts, brackets, magnetic structures. |
| Aluminum / alumina chain products | `local_derived`, highland-favored | Lightweight frames, reflectors, conductors, robot links. |
| Calcium oxide / lime | `local_derived`, highland-favored | Cement chemistry, fluxes, refractory and ceramic additions. |
| Titanium oxide / ferrotitanium products | `local_derived`, mare-favored | Coatings, ceramics, corrosion-resistant or high-strength parts. |
| Magnesium oxide / magnesia | `local_derived`, mare/olivine-favored | Refractories, Sorel-cement concepts, ceramic additions. |
| Basaltic glass / glass-ceramic | `local_derived`, mare or glass-deposit favored | Insulation, wear surfaces, cast basalt, glass fiber, nonmetal structural parts. |

### Site-Sensitive Materials

Use these when the machine design explicitly assumes the matching site:

| Material family | Main source | Design implication |
|---|---|---|
| Water ice | Polar permanently shadowed craters | Useful but operationally hard; avoid as a casual consumable. |
| Hydrogen | Polar water or solar-wind volatiles | Valuable reductant; design for recycle. |
| Carbon / CO / CO2 / CH4 | Polar volatiles, carbonaceous impact material, trace regolith carbon | Use sparingly; prefer recycle and low-carbon processes. |
| Nitrogen / ammonia | Polar volatiles or solar-wind implanted nitrogen | Scarce; avoid open-loop use. |
| Sulfur / H2S / troilite | Troilite in regolith/meteorites or polar volatiles | Useful for chemistry; do not assume bulk availability. |
| KREEP-derived K/P/REE/Th/U | KREEP terranes | Advanced, localized, chemically complex. |
| Pyroclastic or impact glass | Volcanic glass deposits, agglutinates, impact melt glass | Useful glass feedstock, but source/site should be explicit if it matters. |

### Scarce or High-Risk Materials

Avoid making these baseline requirements for early machines:

| Material family | Risk |
|---|---|
| Copper | Low lunar abundance; wiring-heavy designs should be marked import-heavy unless a local route closes. |
| Zinc | Low abundance; treat as import or long-term trace extraction. |
| Sodium and halogens | Present in limited/localized minerals; process salts should be recycled tightly. |
| Potassium and phosphorus | KREEP/apatite-derived; useful but localized and chemically involved. |
| Chromium and manganese | Present as minor elements; extraction is difficult and they should not drive baseline alloys. |
| Nickel, cobalt, tungsten, tantalum, niobium, selenium, platinum-group traces | Mainly trace, KREEP/granite, or meteoritic/impact-site sources; use for critical low-mass functions only. |
| Rare earth elements | KREEP-derived and advanced; avoid rare-earth magnets in baseline designs. |
| Lithium, boron, zirconium | Very low or localized; avoid Li alloys, borosilicate assumptions, and zirconia/yttria dependence unless explicitly imported or researched. |
| Mercury | Polar volatile/LCROSS detection context; treat as contaminant or niche trace material, not a design feedstock. |
| Helium-3 and noble gases | Very low concentration; not relevant to near-term machine material selection except niche uses. |
| Polymers, elastomers, specialty lubricants | Depend on scarce C/H/N/S chemistry; minimize and mark imports explicitly. |
| Semiconductor-grade silicon and dopants | Industrial silicon is plausible; electronics-grade material is not a baseline assumption. |

### Magnetic, Electronic, and Specialty Materials

The source inventory flags several useful machine materials that are possible in
principle but risky as baseline choices:

| Material family | Availability judgment | Design implication |
|---|---|---|
| Ferrites / magnetite | Moderate if based on iron oxides; Ni/Zn/Co ferrites inherit Ni/Zn/Co scarcity. | Prefer simple iron-oxide ferrites for low-performance magnetic parts; mark high-performance ferrites as advanced. |
| Alnico / permalloy / Kovar / fernico | Limited by Ni/Co and sometimes Cu/Mo/Mn additions. | Use only where function justifies the alloy; document imported or meteoritic trace requirements. |
| Refractory metal parts | W/Ta/Nb are trace/localized. | Keep as low-mass critical parts; avoid using them as ordinary electrodes or heaters unless closure is explicit. |
| Quartz / fused silica | SiO2 route is plausible; high-purity quartz crystals are more advanced. | Fused silica is a good design material; precision quartz sensors/crystals need separate closure. |
| Zirconia and yttria-stabilized ceramics | Zr/Y sources are weak/localized. | Treat zirconia sensors/ceramics as specialty items unless the recipe is intentionally modeled. |

## Machine BOM Checklist

Before adding a new machine design:

1. Search for an existing machine, tool, part, or material with equivalent
   function and compatible material class.
2. Prefer designs based on iron/steel-like stock, aluminum, alumina, silica,
   glass, ceramics, and regolith-derived structures.
3. Keep polymers, copper, rare earth magnets, specialty chemicals, sealed
   bearings, refractory metals, specialty magnetic alloys, and precision
   electronics explicit in the BOM if they are needed.
4. Add a short material rationale to the machine or BOM `notes`.
5. Run closure on the candidate machine:

```bash
python -m src.cli closure --machine <machine_id>
```

6. Compare the critical BOM materials using the availability labels above.

Suggested BOM note:

```yaml
notes: |
  Material rationale:
  - Baseline structure uses lunar-derivable metal and ceramic materials.
  - Copper, polymers, precision electronics, and specialty lubricants are kept
    explicit rather than hidden inside generic assemblies.
  - Specialty magnetic alloys, refractory metals, and rare trace elements are
    treated as advanced or imported unless closure proves a local route.
  - Site-sensitive volatile use must be justified by the scenario.
```

## Source Summary

This guide summarizes notes from converted ISRU, lunar industry, and Ellery
papers. Key source themes:

- Lunar regolith is the main bulk feedstock.
- Highland regolith/anorthite favors aluminum, alumina, calcium/lime, silica,
  glass, ceramics, and oxygen.
- Mare regolith/ilmenite favors iron, titanium/titania, oxygen, and basaltic
  glass or glass-ceramic materials.
- Polar permanently shadowed craters are the most important water/volatile
  source, but are operationally difficult.
- KREEP and meteoritic materials provide important specialty elements, but are
  localized and should not dominate early machine BOMs.
- Pyroclastic/impact glass can be useful, but should not replace generic
  regolith or basalt feedstocks unless a site-specific design requires it.
- Several attractive high-performance materials (Kovar, Alnico, permalloy,
  ferrites, refractory metals, quartz sensors, zirconia ceramics) need explicit
  closure because their minor or trace constituents can dominate feasibility.
