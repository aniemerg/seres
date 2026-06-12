# PCB fabrication equipment

## Machine identity

- KB ID: `pcb_fab_equipment`
- KB name: PCB fabrication equipment
- KB file: `kb/items/machines/pcb_fab_equipment.yaml`
- KB kind: `machine`
- Current KB mass: 435.3 kg
- Current KB structure: UV exposure equipment, chemical development/etch tanks, PCB drilling station, tinning/plating bath, and supporting process equipment for single- or double-sided boards.

## KB usage and needed function

The KB uses `pcb_fab_equipment` as a capacity provider for:

- `kb/processes/pcb_fabrication_v0.yaml`
- `kb/processes/photolithography_process_simple_v0.yaml`
- `kb/processes/solar_cell_fabrication_v0.yaml`

It supports recipes for bare PCBs, assembled boards, control boards, sensors, and embedded/control electronics. The local notes describe a subtractive PCB flow: UV exposure of photoresist, development, etching, drilling, and surface finishing.

## Reality classification

Classification: real practical equipment bundle or station.

`pcb_fab_equipment` is not one machine in the narrow sense. It is a bundled PCB prototyping/fabrication line: exposure, development, etching, drilling/routing, and finishing equipment. That is a realistic way to model a small lab or seed-factory PCB capability while avoiding premature proliferation of separate tool IDs.

The current mass of 435.3 kg is plausible for a small in-house PCB lab with multiple wet-process and drilling machines. It is far below a full industrial multilayer PCB factory, but the KB notes already constrain the scope to simple single/double-sided boards with coarse 0.2-0.5 mm traces.

## Evidence links

- LPKF sells benchtop PCB prototyping systems and circuit board plotters for milling, drilling, and contour milling PCBs. Sources: https://www.lpkfusa.com/pcb and https://www.lpkfusa.com/products-technologies/pcb-prototyping-equipment/pcb-milling-machines
- Bungard Elektronik lists PCB lab machines including PCB drilling machines, dry film laminators, spray etching/developing machines, and laboratory etching systems. Source: https://www.bungard.de/en/machines
- PCBWay's process overview shows that PCB manufacturing includes inner/outer layer imaging, etching, drilling, plating, soldermask, surface finish, and electrical test. Source: https://www.pcbway.com/pcb-service.html
- DIY and lab-scale PCB processes commonly use an exposure mask, UV exposure, development, etching, and drilling/cutting. Source: https://justaddelectrons.com/blogi/diy-home-pcb-exposure-and-etching-process/

## Commercial alternatives

Commercial alternatives include:

- LPKF ProtoMat-style benchtop PCB milling/drilling machine.
- Bungard-style PCB lab equipment set: laminator, exposure unit, spray etcher/developer, drill, and plating/tinning equipment.
- Small chemical etching bench with UV exposure box and manual drill press for simple boards.
- Full industrial PCB manufacturing line for multilayer boards, plated through holes, soldermask, inspection, and electrical testing.

For the KB's current needs, a PCB lab/prototyping station is more realistic than assuming semiconductor-grade electronics manufacturing. It can plausibly produce simple control PCBs but not advanced ICs.

## Build or open-source references

Low-end PCB fabrication can be assembled from simple equipment:

- DIY UV/photoresist flows use printed masks, UV exposure, developer, etchant, and drilling/cutting tools.
- Instructables and hobby workflows show minimal PCB labs built from a laminator, printer, UV lamp, trays/tanks, etchant, and small drill: https://www.instructables.com/DIY-PCB-lab-for-under-3500/
- Open-source CNC routers or converted desktop mills can do PCB isolation milling and drilling, but process quality and repeatability vary.

These are adequate references for simple boards. They do not validate the KB's ability to make fine-pitch multilayer boards, plated vias at industrial yield, soldermask, or high-reliability aerospace electronics.

## Related machine research

Related KB entries include:

- `pcb_fab_station`
- `pcb_development_station`
- `pcb_drilling_station`
- `pcb_etching_tank_set`
- `pcb_tinning_plating_bath`
- `uv_exposure_unit`
- `soldering_station`
- `test_bench_electrical`
- `control_compute_module_imported`

There is overlap between `pcb_fab_equipment` and `pcb_fab_station`. Future cleanup should decide whether one is deprecated or whether `pcb_fab_equipment` is the complete station while the others are components.

## Recommendation for KB realism

Keep as a station/tool bundle for now, but clarify scope.

Recommended note: "Aggregated small PCB prototyping/fabrication station for simple single- and double-sided boards; includes exposure, develop/etch, drilling, and surface finish equipment. Does not represent advanced multilayer industrial PCB fabrication."

Potential future split:

- `uv_exposure_unit`
- `pcb_development_station`
- `pcb_etching_tank_set`
- `pcb_drilling_station`
- `pcb_tinning_plating_bath`
- `pcb_inspection_test_station`

The split should only happen if separate capacity, mass, or consumables matter. Conservative mode supports keeping the current aggregate while the KB is coarse.

## Confidence and open questions

Confidence: high that this is real as a practical equipment bundle; medium on the current mass because component scope is not fully explicit.

Open questions:

- Does the KB require plated through holes, soldermask, silkscreen, and electrical testing, or only etched bare boards?
- Is `pcb_fab_station` a duplicate of `pcb_fab_equipment`?
- Are etchants, developers, photoresist, copper-clad laminate, drill bits, and rinse/waste treatment modeled as consumables?
- Should solar-cell photolithography share this equipment, or does it need a distinct clean process station?
