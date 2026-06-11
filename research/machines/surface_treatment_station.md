# Machine identity

- Queue item: `machine_reality_surface_treatment_station`
- KB item: `surface_treatment_station`
- KB name: Surface treatment station
- KB file: `kb/items/machines/surface_treatment_station.yaml`
- Current KB kind: `machine`
- Current mass: 300 kg
- Current BOM: `bom_surface_treatment_station_v0`
- Current recipe: `recipe_surface_treatment_station_base_v0`

# KB usage and needed function

`surface_treatment_station` is used by `surface_treatment_basic_v0` and `surface_treatment_anodizing_v0`. The KB notes describe chemical surface treatments such as etching, passivation, and coating preparation.

The BOM includes a chemical bath tank set, agitation system, bath ventilation, circulation pump, basic control panel, welded support frame, and fasteners. That matches a wet-chemistry metal-finishing station: tanks for cleaners/acids/electrolytes/rinses, fixtures or racks for parts, pumping/agitation, ventilation or fume extraction, and basic controls.

# Reality classification

Real practical machine.

The item should be interpreted as a compact wet-process surface-treatment station or line, not as one universal finishing machine. It is realistic for cleaning, etching, pickling, passivation, anodizing, and coating-prep operations. It should remain distinct from `coating_station` for paint/powder/epoxy spray or dip coatings and from `spin_coating_station_v0` for photoresist or thin-film spin coating.

# Evidence links

- HPI Processes sells wet process lines for cleaning, electroplating, anodizing, passivation, electro-polishing, etching, and related metal finishing processes, including manual or automated process benches: https://www.hpipro.com/productdetail/wet-process-line/
- Best Technology describes a titanium anodizing equipment line with 10 polypropylene tanks, manual anodizing capacity, and a rectifier for the anodizing tank: https://www.besttechnologyinc.com/surface-finishing/titanium-anodizing-equipment-line/
- Technic describes titanium anodizing equipment/process steps including alkaline cleaning, rinsing, optional fluoride cleaning, and the anodization bath: https://www.technic.com/equipment/anodizing-equipment/titanium-anodizing-equipment
- Palm Technology describes etching and passivation as chemical surface treatments used to clean, texture, prepare, or protect metal surfaces: https://www.palmequipment.com/index.cfm?FuseAction=Info_EtchPass
- Best Technology describes stainless steel passivation as a common nitric-acid or citric-acid chemical finishing process for corrosion resistance: https://www.besttechnologyinc.com/passivation-systems/what-is-passivation/
- Finishing and Coating describes type III aluminum anodizing as involving cleaning, etching, deoxidizing/desmutting, anodizing, and rinsing tanks: https://finishingandcoating.com/index.php/anodizingcat/278-the-most-important-anodizing-tank
- EPA anodizing pollution-control guidance recommends air pollution controls, secondary containment, and wastewater pretreatment for anodizing facilities: https://www.pfonline.com/articles/pollution-control-for-anodizing
- P2 InfoHouse notes that rinsing follows cleaning, plating, and stripping operations, stops chemical reactions, and prevents cross-contamination of subsequent plating tanks: https://p2infohouse.org/ref/03/02454/rinsing.htm

# Commercial alternatives

Commercial alternatives include:

- Manual wet process bench with polypropylene or stainless tanks.
- Multi-tank anodizing line with rectifier, rinse tanks, and part racks.
- Pickling/passivation tank line for stainless steel.
- Electroplating or electropolishing line with rectifiers and chemistry controls.
- Spray washer or aqueous parts-cleaning line for degreasing and pretreatment.
- Coating booth or dip-coating station for paint, powder, epoxy, or ceramic coatings; this is adjacent but not the same machine.

# Build or open-source references

A simple local station is plausible if the KB already has tanks, chemically compatible plumbing, ventilation, pumps, and basic controls. Useful subassemblies include:

- acid/alkali-compatible tanks and drain containment,
- rinse tanks or flowing rinse plumbing,
- part baskets, racks, hooks, or fixtures,
- agitation, circulation, heating, and temperature sensing where needed,
- local exhaust ventilation and corrosion-resistant ducting,
- rectifier and electrical contacts for anodizing, plating, or electropolishing,
- pH/chemistry measurement and wastewater handling.

The current BOM is plausible for generic cleaning, etching, passivation, and prep. For anodizing specifically, the KB should include or require a DC rectifier, electrodes/bus bars, and process-specific chemistry. For pickling/passivation, waste treatment and fume control are not optional realism details.

# Related machine research

Related local reports:

- `chemical_bath_station.md`
- `controlled_atmosphere_chamber.md`
- `drying_oven.md`
- `heat_treatment_furnace_v0.md`
- `surface_grinder.md`
- `pcb_fab_equipment.md`
- `pcb_development_station.md`

Related KB items include `coating_station`, `coating_station_v0`, `spin_coating_station_v0`, `pcb_tinning_plating_bath`, `chemical_bath_station`, `chemical_bath_agitation_system`, `coating_booth_enclosure`, `coating_spray_gun_and_pump`, and `coating_drying_oven`.

# Recommendation for KB realism

Keep `surface_treatment_station` as a real generic wet-chemical surface-treatment machine.

Recommended refinements:

- Define its scope as wet chemical cleaning, etching, pickling, passivation, anodizing, and coating preparation.
- Avoid using it for paint, epoxy, powder coating, spray coating, drying/curing, or photoresist spin coating; those should use `coating_station` or `spin_coating_station_v0`.
- Split out process-specific requirements when they matter: rectifier/electrodes for anodizing or plating, heat/cooling for temperature-sensitive baths, wastewater treatment for acid/metal-bearing effluent, and ventilation/containment for fuming chemistries.
- Keep the 300 kg mass as plausible for a compact manual multi-tank station, but model larger automated lines separately if throughput grows.

# Confidence and open questions

Confidence: high that the item is real; high that the BOM is directionally plausible for a compact wet-process station; medium that current process scoping is clean because `surface_treatment_basic_v0` currently mentions simple protective coatings as well as wet chemical prep.

Open questions:

- Should `surface_treatment_anodizing_v0` require an explicit rectifier component or a distinct `anodizing_line` variant?
- Should acid waste neutralization and wastewater treatment be separate machines/resources in the KB?
- Should `surface_treatment_basic_v0` remove "simple protective coatings" and leave coating application to `coating_station`?
