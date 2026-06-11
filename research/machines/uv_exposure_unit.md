# UV Exposure Unit Machine Reality Research

## Machine identity

- KB machine id: `uv_exposure_unit`
- KB name: UV exposure unit
- KB file: `kb/items/machines/uv_exposure_unit.yaml`
- Current KB mass: 100 kg
- Current BOM: `bom_uv_exposure_unit`
- Current recipe: `recipe_uv_exposure_unit_v0`

## KB usage and needed function

The unit is required by `photolithography_process_simple_v0` alongside `pcb_fab_equipment` and `pcb_development_station`. It is also a component of `pcb_fab_equipment`.

The needed function is controlled ultraviolet exposure of photoresist-coated substrates through a mask. For PCB work this means adequate UV wavelength, uniform intensity, exposure timing, mask contact or vacuum frame, alignment, and UV shielding.

## Reality classification

Real practical machine.

UV exposure units are standard equipment for PCB photolithography, solder mask exposure, screen printing, and photoresist work. The KB item is realistic. The 100 kg mass is plausible for a rugged or semi-industrial exposure station, but heavy for a small desktop PCB exposure box. The current BOM of only frame plus lamp module is a simplified placeholder.

## Evidence links

- Golden Eagle/Etch Machinery describes PCB UV LED exposure machines for dry film, wet film, inner/outer layer, and solder-mask exposure, including vacuum systems and CCD alignment on production units: <https://www.etchmachinery.com/exposure-machine.html>
- Golden Eagle describes single-face UV exposure machines as photolithography systems using UV light to transfer circuit patterns onto photosensitive PCB substrates: <https://www.etchmachinery.com/LED-exposure-machine.html>
- Fastlink Electronics explains PCB exposure as the step where UV light exposes photoresist on a PCB substrate to transfer the circuit pattern: <https://www.fastlink-electronics.com/exposure-in-pcb-production/>
- Make-It.ca documents a DIY UV LED exposure box for exposing sensitized PC boards and UV-sensitive adhesives: <https://www.make-it.ca/uv-led-pc-board-exposure-build/>

## Commercial alternatives

- Desktop UV exposure box for hobby/prototype PCBs.
- Vacuum-frame UV exposure unit for better mask contact.
- Double-sided UV exposure machine for two-sided boards.
- CCD-aligned industrial LED exposure machine for multilayer PCB or solder mask work.
- Screen-printing exposure unit if the process is screen/stencil rather than PCB photoresist.

## Build or open-source references

DIY UV exposure boxes are straightforward: UV LEDs or tubes, enclosure, timer/controller, glass or acrylic mask-contact surface, power supply, cooling, and UV shielding. The build becomes harder when exposure uniformity, double-sided alignment, vacuum contact, and repeatable calibration are needed.

The KB recipe is credible as a simple assembly from frame and lamp module, but production PCB work should include timer/control electronics, mask registration, shielding, and potentially vacuum hold-down.

## Related machine research

Related local reports:

- `research/machines/pcb_development_station.md`
- `research/machines/pcb_fab_equipment.md`
- `research/machines/pcb_etching_tank.md`

These support keeping the UV exposure unit as one submodule in a larger PCB photolithography workflow.

## Recommendation for KB realism

Keep the item as real PCB/photoresist equipment.

Recommended options:

- Keep separate from `pcb_development_station`; exposure and development are different process steps.
- Keep as a component of `pcb_fab_equipment` where full PCB fabrication is abstracted.
- Add or document mask/contact frame, timer, UV shielding, and alignment features if precision matters.
- Consider lowering mass for a desktop/prototype unit or keeping 100 kg only for an enclosed semi-industrial station.
- Do not use this item to imply full semiconductor lithography capability; simple PCB photolithography is a much lower bar.

## Confidence and open questions

Confidence: high that the item is real and appropriate for simple PCB photoresist work; medium on the 100 kg mass and missing alignment/vacuum/timer details.

Open questions:

- Is the target PCB workflow single-sided, double-sided, or multilayer?
- Should the exposure unit include a vacuum frame and registration pins?
- What UV wavelength and photoresist type does the KB assume?
