# Stamping Press Basic Machine Reality Research

## Machine identity

- KB machine id: `stamping_press_basic`
- KB name: Stamping press (basic)
- KB file: `kb/items/machines/stamping_press_basic.yaml`
- Current KB mass: 1000 kg
- Current BOM: `bom_stamping_press_basic_v0`
- Current recipe: `recipe_machine_stamping_press_basic_import_v0`

## KB usage and needed function

The machine is used by:

- `lamination_stamping_v0`, converting `electrical_steel_sheet` into `stator_rotor_lamination_set` at 20 kg/hr.
- `iron_core_lamination_basic_v0`, making small laminated iron core pieces from thin steel sheet.

The required function is repetitive die-based blanking/punching/forming of thin steel sheet. For motor or transformer laminations, the important capabilities are press tonnage, die alignment, repeatable stroke control, and usually feeding/stacking support. This is distinct from a press brake, plate rolling mill, or generic hydraulic shop press.

## Reality classification

Real practical machine, but the KB name is broad and the current "basic" model should be treated as a low-end hydraulic/mechanical stamping press plus die/tooling, not as a complete high-speed lamination line.

The 1000 kg mass is plausible for a small C-frame hydraulic or mechanical press body, but may be low for a press capable of production motor lamination stamping. Commercial lamination systems commonly use higher-tonnage presses and automation. A generic `stamping_press_basic` can remain useful for early or low-throughput punching, but the KB should not imply it is equivalent to an automated electric-motor lamination line.

## Evidence links

- AIDA-America describes mechanical stamping presses used for metal stamping in gap-frame and straight-side forms, with gap-frame press capacities starting in the tens of tons rather than "desktop" scale: <https://www.aida-america.com/mechanical-stamping-presses/>
- ANDRITZ describes electric motor lamination press lines as complete systems with feeder, press, stacker, and scrap conveyor; the example line is in the thousands of kN class. This supports keeping lamination production as a specialized stamping application, not just a manual tool: <https://www.andritz.com/products-en/metals/stamping/electric-motor-sheeting>
- Thomson Lamination reports custom motor, rotor, and stator lamination stamping using high-speed presses up to 250 tons: <https://www.tlclam.net/capabilities/precision-motor-lamination-stamping/>
- Revolution Machine Tools describes C-frame hydraulic presses as metalworking machines for stamping, punching, and forming sheet metal, supporting the KB's low-end hydraulic C-frame concept: <https://www.rmtus.com/c-frame-hydraulic-presses>

## Commercial alternatives

- Gap-frame/C-frame mechanical stamping press: best fit for repetitive blanking and punching of sheet metal with dies.
- Hydraulic C-frame press: plausible lower-speed option for simple punching/forming and prototyping.
- Complete motor lamination press line: press plus decoiler/feeder/stacker/scrap handling for high-throughput laminations.
- Outsourced lamination stamping service: realistic early supply-chain alternative for precision motor cores.

## Build or open-source references

No credible open-source design for a production lamination stamping press was found during this pass. A fabricated hydraulic C-frame press can be built from heavy steel frame members, cylinder, pump, valves, guides, platens, and controls, which matches the current KB recipe. However, die design, guarding, ram guidance, frame deflection, and overload protection are safety-critical and should not be modeled as a simple manual tool build.

For a self-reproduction model, the current build recipe is useful as a coarse fabrication path for a low-speed press, while precision lamination dies and press controls should remain separate capability assumptions if the model needs realistic motor production.

## Related machine research

Related local reports:

- `research/machines/steel_forming_press.md`
- `research/machines/hydraulic_press.md`
- `research/machines/press_brake.md`
- `research/machines/metal_forming_basic_v0.md`

Those reports support keeping separate machine concepts for generic pressing, straight-line bending, rolling, and high-volume die stamping.

## Recommendation for KB realism

Keep the machine concept, but clarify it.

Recommended options:

- Rename to `c_frame_stamping_press_basic` or `hydraulic_stamping_press_basic` if this is intended to represent the current welded-frame hydraulic build recipe.
- Keep `stamping_press_basic` only as a generic imported capability if the KB intentionally abstracts away drive type and tonnage.
- Add or model tooling separately when laminations matter: `lamination_stamping_die_set`, sheet feeder, and possibly stacking/scrap handling.
- Do not merge it into `hydraulic_press`; stamping needs die alignment and repeatable stroke behavior that a generic press does not capture.
- If the process is meant to represent production motor-core laminations, consider a future specialized machine such as `motor_lamination_press_line` rather than increasing the scope of this item.

## Confidence and open questions

Confidence: high that stamping presses are real and appropriate for sheet-metal punching/lamination work; medium that the current 1000 kg hydraulic C-frame model is adequate for the specific KB lamination rates.

Open questions:

- What lamination size and electrical steel thickness does the KB intend for `stator_rotor_lamination_set`?
- Should lamination dies be imported, fabricated locally, or represented as consumable tooling?
- Should `lamination_stamping_v0` require a feeder/stacker for the modeled 20 kg/hr throughput, or is labor loading acceptable at this abstraction layer?
