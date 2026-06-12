# Machine identity

- Queue item: `machine_reality_ball_mill_v0`
- KB item: `ball_mill_v0`
- KB name: Ball mill v0
- KB file: `kb/items/machines/ball_mill_v0.yaml`
- Current KB kind: `machine`
- Current mass: 927.5 kg
- Current capabilities: `ball_mill`, `powder_milling`
- Current BOM: `bom_ball_mill_v0`
- Current recipe: `recipe_ball_mill_v0`

# KB usage and needed function

`ball_mill_v0` is used by powder and grinding processes including `ball_milling_v0`, `regolith_crushing_grinding_v0`, `crushing_and_grinding_v0`, `grinding_and_milling_v0`, `powder_milling_process_v0`, `sizing_grinding_basic_v0`, `graphite_powder_production_v0`, `ceramic_powder_synthesis_v0`, `metal_powdering_process_v0`, `iron_powder_synthesis_v0`, and ferrite/regolith/olivine grinding tasks.

The needed function is bulk comminution and mixing: a rotating lined shell tumbles grinding media with feed material to reduce particle size and homogenize powders. The KB BOM includes a mill shell, abrasion-resistant liners, trunnion supports, heavy bearings, motor, gearbox, welded frame, and fasteners, which matches an industrial rotary ball mill.

# Reality classification

Real practical machine.

`ball_mill_v0` should remain distinct from a rock crusher, CNC mill, surface grinder, powder mixer, and grinding wheels. It is downstream of crushing and upstream of screening/classification or powder processing. It can also mix powders, but if no size reduction is required, `powder_mixer` is the more realistic machine.

# Evidence links

- 911Metallurgist sells small ball mills with motor, gears, steel liners, and optional grinding media; it describes light- and heavy-duty mills for wet or dry pulverizing/grinding: https://www.911metallurgist.com/blog/ball-mill/
- JXSC describes ball milling as a grinding method using manganese, iron, steel, or ceramic balls to reduce ore and other materials to controlled fine sizes in mineral processing: https://www.jxscmachine.com/rock-crusher/ball-mill/
- JXSC's grinding mill parts list includes shell/head linings, trunnion liners, gears and pinions, main bearings, trunnions, grinding media, and trommel screens, matching the KB's shell/liner/trunnion/bearing/drive model: https://www.jxscmachine.com/spare-parts/grinding-mill-parts/
- University of Alaska Fairbanks AMIT 135 training describes ball mills supported on steel tires or trunnions, driven by girth gears and pinions, with the charge cascading during rotation: https://millops.community.uaf.edu/amit-135/amit-135-lesson-7/
- Digitalfire describes conventional ball mills in pottery and ceramic plants as reducing particles to fine micrometer sizes for glaze suspension, melt homogeneity, and body plasticity: https://digitalfire.com/glossary/ball%2Bmilling
- RETSCH describes planetary ball mills for pulverizing soft, hard, brittle, and fibrous materials in dry or wet mode; this supports the lab-scale alternative, though it is a different high-energy design from the KB's medium rotary mill: https://www.retsch.com/products/milling/planetary-ball-mills/

# Commercial alternatives

Commercial alternatives include:

- Batch rotary ball mill for ceramic, mineral, or powder processing.
- Continuous ball mill with feed/discharge handling and classifier.
- Rod mill for coarser grinding with less fines.
- Attritor/stirred media mill for finer or faster wet grinding.
- Planetary ball mill for laboratory-scale high-energy milling.
- Vibratory mill for small high-energy batches.
- Hammer mill or impact mill for brittle feed where contamination and particle shape constraints are looser.

# Build or open-source references

A medium rotary ball mill is locally buildable if the system can fabricate heavy rotating structures and wear parts. Critical requirements include:

- balanced cylindrical shell or drum,
- replaceable wear liners,
- trunnions or roller support,
- heavy bearings and seals,
- motor, gearbox, coupling, and guard,
- grinding media charge,
- dust containment or wet milling containment,
- feed/discharge system and downstream screen/classifier,
- maintenance access for liners, media, and bearings.

The KB BOM is directionally good. It should add `grinding_media_steel` or `grinding_media_alumina_v0` as tooling/consumable inventory, because a ball mill without media cannot mill. For abrasive regolith and ceramics, liner wear and media contamination are important realism details.

# Related machine research

Related local reports:

- `rock_crusher_basic.md`
- `vibrating_screen_v0.md`
- `powder_mixer.md`
- `grinding_wheels.md`
- `surface_grinder.md`
- `milling_machine_general_v0.md`
- `cnc_mill.md`

Related KB items include `grinding_media_steel`, `grinding_media_alumina_v0`, `powder_mixer`, `screening_equipment_v0`, `vibrating_screen_v0`, `rock_crusher_basic`, and `dust_collection_system`.

# Recommendation for KB realism

Keep `ball_mill_v0` as a real medium-scale powder milling machine.

Recommended refinements:

- Define it as a rotary ball mill for wet/dry bulk comminution and powder homogenization.
- Add grinding media as an explicit required consumable/tooling item for ball-milling processes or the ball mill BOM.
- Keep it downstream of crushing; feed rocks generally need crushing before ball milling.
- Keep it distinct from `powder_mixer` when particle-size reduction is needed, and use `powder_mixer` for blending-only steps.
- Keep it distinct from CNC milling and surface grinding; those are precision shape-generation/finishing machines, not bulk powder mills.
- Consider adding dust collection, wet milling slurry handling, screening/classification, liner wear, and media contamination details for regolith and ceramic workflows.

# Confidence and open questions

Confidence: high that the item is real; high that the mass/BOM are plausible for a medium rotary mill; medium on whether all current powdering processes should use a ball mill versus crusher, hammer mill, attritor, or mixer.

Open questions:

- What feed size and product particle-size distribution does the KB assume?
- Should the KB distinguish batch ball mills from continuous mills?
- Should reactive metal powders require inert atmosphere or wet milling to manage fire/explosion risk?
