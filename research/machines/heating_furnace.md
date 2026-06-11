# Heating furnace

## Machine identity

- KB ID: `heating_furnace`
- KB file: `kb/items/machines/heating_furnace.yaml`
- KB name: Heating furnace (general purpose)
- KB mass: 512 kg per unit
- Current KB role: general-purpose 600-1200 C furnace for preheating, hot rolling preparation, getter activation, carbon anode processing, and material heat treatment.

## KB usage and needed function

Local usage shows this item overlaps with the furnace family:

- It is listed in the minimal/self-reproducing machine set.
- It is used by hot rolling and steel/nickel forming processes, carbon anode forming, anorthite/lime/soda process steps, and related heating operations.
- Its notes specify electric resistance or solar-thermal heating, insulated chamber, heating elements, and temperature control.
- `docs/dedupe_decisions.md` already keeps `furnace_basic` as a general-purpose 200-1200 C furnace and `furnace_high_temp` as a 1600-3000 C specialized furnace.
- A separate `heating_furnace_module` exists for fiber drawing/getter activation contexts.

The needed function is controlled preheating and moderate-temperature heat treatment. This is real, but the distinction from `furnace_basic` is not obvious from current notes.

## Reality classification

Classification: real practical machine, possible KB duplicate/variant.

Industrial heat-treatment and preheating furnaces are standard equipment. The KB item is realistic as a furnace. It may be redundant with `furnace_basic` unless it is intentionally a larger or more controlled preheating furnace for rolling/forming lines.

## Evidence links

- Fives describes heat treatment furnaces up to 1200 C for strip coils, wire rod coils, cast iron tubes, graphite electrodes, chamber furnaces, and preheaters/dryers: https://www.fivesgroup.com/steel/reheating/heat-treatment
- Kanthal describes electric roller hearth furnaces used for annealing, slab reheating, stress relieving, hardening, normalizing, tempering, and preheating blanks for hot forming: https://www.kanthal.com/en/industries/steel/continuous-furnaces/electric-heating-benefits-over-gas/
- LAC lists metal heat treatment furnaces including preheating, annealing, hardening, and tempering furnaces, with chamber furnaces around 700-1250 C: https://www.lac.cz/en/furnaces-and-dryers/industrial-furnaces-and-dryers/heat-treatment-of-metals
- DirectIndustry lists resistance/muffle furnaces with 1100-1200 C maximum temperature ranges and ceramic fiber insulation/control features: https://www.directindustry.com/industrial-manufacturer/heat-treatment-oven-150799-_2.html
- U.S. DOE process heating sourcebook describes electric resistance heating as a long-used method for heating and melting metals/nonmetals with high controllability: https://www.energy.gov/sites/prod/files/2016/04/f30/Improving%20Process%20Heating%20System%20Performance%20A%20Sourcebook%20for%20Industry%20Third%20Edition_0.pdf

## Commercial alternatives

Commercial alternatives include:

- Electric resistance chamber furnaces.
- Muffle furnaces for lab/small batch work.
- Roller hearth furnaces for continuous preheating/heat treatment.
- Bell, bogie hearth, rotary hearth, and conveyor furnaces.
- Solar-thermal preheaters if process integration supports it.
- `furnace_basic` in the KB for general heating/melting/heat treatment.

For the KB, this item only needs to remain separate if preheating/hot-forming workflow capacity differs from `furnace_basic`.

## Build or open-source references

Small heat-treatment furnaces can be built from refractory brick or ceramic fiber insulation, Kanthal/NiCr/FeCrAl heating elements, a thermocouple, PID controller, relay/SSR, metal shell, and safety cutoff. DIY heat-treat oven and tube furnace builds demonstrate the basic construction pattern, but industrial reliability requires electrical safety, insulation design, overtemperature protection, and atmosphere/fume handling.

## Related machine research

Related local reports:

- `research/machines/furnace_high_temp.md`
- `research/machines/casting_furnace_v0.md`
- `research/machines/drying_oven.md`

Related KB items:

- `furnace_basic`
- `furnace_high_temp`
- `heating_furnace_module`
- `annealing_oven_small`
- `drying_oven`
- `casting_furnace_v0` (deprecated)
- `sintering_furnace_v0` (deprecated)

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep as real equipment, but review for consolidation with `furnace_basic`.

Recommended cleanup when KB edits are allowed:

- If `heating_furnace` only means general 600-1200 C heating, consolidate references into `furnace_basic`.
- If it is specifically a preheat furnace for rolling/forming or getter activation, rename to "preheating furnace" and document that distinct duty.
- Keep it separate from `furnace_high_temp`; this item's 600-1200 C range does not cover carbothermal/sintering/MRE-class temperatures.
- Keep it separate from `drying_oven`; this item is hotter and for heat treatment/preheating, not moisture removal.
- Clarify whether the 512 kg mass includes power conditioning and material handling.

## Confidence and open questions

Confidence: high that the equipment is real; medium-low that it should remain distinct from `furnace_basic`.

Open questions:

- Is this intended as a dedicated preheater for rolling lines?
- What chamber size/load mass is assumed?
- Does the self-reproducing set need both `furnace_basic` and `heating_furnace`, or is this a duplicate created before furnace dedupe?
