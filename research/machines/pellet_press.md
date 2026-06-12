# Pellet Press

## Machine identity

- KB ID: `pellet_press`
- KB name: Pellet press
- KB file: `kb/items/machines/pellet_press.yaml`
- Current KB type: `machine`
- Current KB mass: 22 kg
- Current KB note: stub machine; current BOM only includes basic steel frame/plates and warns that a functional press needs hydraulic/pneumatic mechanism, motor/actuator, controls, die/mold set, and feed hopper.

## KB usage and needed function

The KB uses `pellet_press` for:

- `regolith_pellet_pressing_process_v0`
- `powder_pressing_process_v0`
- `powder_metallurgy_pressing_v0`
- Catalyst preparation references in `sabatier_reaction_complete_v0`, `methanol_synthesis_from_syngas_v0`, `reverse_water_gas_shift_v0`, `bosch_reaction_v0`, `ostwald_process_nitric_acid_v0`, `ostwald_stage1_ammonia_oxidation_v0`, `carbon_monoxide_oxidation_v0`, `claus_process_sulfur_recovery_v0`, and `syngas_generation_steam_reforming_v0`.

The needed function is compacting loose powder into pellets, briquettes, tablets, or green compacts using a die and press force. Uses include catalyst pellets, lab analysis pellets, regolith cathode pellets, ceramic/metal powder compacts, and possibly feedstock preparation.

## Reality classification

Classification: real practical machine/tooling system, but current KB implementation is incomplete.

Laboratory pellet presses and powder compaction presses are real. They usually consist of a hydraulic, pneumatic, screw, or electric press plus hardened die sets. Production pelletizers can be much larger and may use roller/die mechanisms, extrusion, or high-throughput compaction.

The KB's 22 kg mass is plausible for a small manual frame or die fixture, but not a complete automatic pellet press if hydraulics, actuator, controls, and dies are included. A functional lab-scale press is often in the tens to hundreds of kg depending on force rating; production systems are larger.

## Evidence links

- Specac describes laboratory hydraulic presses and pellet dies used to press solid and semi-solid pellets for IR, XRF, dielectric spectroscopy, dissolution testing, and related methods. Source: https://specac.com/product-category/sample-preparation-equipment/
- MSE Supplies sells a lab-scale 20-ton electric hydraulic pellet press for powders used in FTIR/XRF, battery electrode materials, metallurgy, ceramics, and catalysis. Source: https://www.msesupplies.com/products/mse-pro-lab-scale-20-ton-electric-hydraulic-pellet-press
- ZYLAB describes a 30-ton automatic powder pellet press for high-pressure shaping of ceramics and metal powders, with programmable pressurizing, hold, and release. Source: https://www.zylabsolution.com/products/30-ton-automatic-powder-pellet-press/
- PelletPressDieSets.com sells precision-machined die sets for making powder pellets, including circular and square dies, custom dies, hydraulic lab presses, and accessories. Source: https://www.pelletpressdiesets.com/
- Kintek describes laboratory hydraulic presses as used to transform loose catalyst powders into mechanically stable pellets suitable for reactor use. Source: https://kinteksolution.com/faqs/why-is-a-laboratory-hydraulic-press-typically-used-to-pelletize-catalyst-powder-before-it-is-loaded-into-a-reaction-tube
- University of Washington lists a Carver hydraulic laboratory press used for making KBr pellets for FTIR analysis. Source: https://chem.washington.edu/instruments/kbr-pellet-press

## Commercial alternatives

- Manual hydraulic lab press plus pellet die.
- Electric hydraulic pellet press.
- Pneumatic pellet press for small analytical pellets.
- Powder compaction press for metal/ceramic green bodies.
- Tablet press for small pharmaceutical/catalyst-style tablets.
- Roller-die pellet mill for biomass or bulk feed pellets.
- Briquetting press for larger agglomerates.

## Build or open-source references

A simple pellet press can be locally built from:

- H-frame or C-frame press body.
- Bottle jack, hydraulic cylinder, screw actuator, or pneumatic cylinder.
- Hardened die set with sleeve, punch, and ejector.
- Load or pressure measurement.
- Optional hopper/fill mechanism for repetitive production.
- Ejection/demolding tools and safety guarding.

The hard part is not the frame alone. For repeatable pellets, die material, finish, alignment, pressure control, powder preparation, binder content, dwell time, and ejection matter. Catalyst and regolith pellets may also need downstream drying, calcination, sintering, or screening.

## Related machine research

Related reports already present:

- `molding_press_basic.md`
- `hydraulic_press.md`
- `powder_mixer.md`
- `dies.md`
- `sintering_furnace_v0.md`

`pellet_press` overlaps with `molding_press_basic`, but it can remain distinct as a smaller powder-pellet/tablet press with dedicated dies. It should not be confused with a production biomass pellet mill unless that specific feedstock and mechanism are required.

## Recommendation for KB realism

Keep as a real item, but revise mass/BOM and scope.

Recommended future wording: "laboratory/pilot powder pellet press with die set." Add explicit components: press frame, hydraulic or screw actuator, die set(s), load/pressure measurement, ejector, optional hopper, and controls if automatic.

If the KB uses it for catalyst pellets and regolith cathode pellets, a lab/pilot powder pellet press is appropriate. If it is meant for high-throughput bulk pelletizing, split a larger `pellet_mill` or `briquetting_press`.

Do not rely on the current 22 kg frame-only BOM as a complete functional machine.

## Confidence and open questions

Confidence: high that pellet presses are real; high that the KB BOM is incomplete; medium on whether one press covers all catalyst, regolith, and powder metallurgy uses.

Open questions:

- What pellet diameter, pressure, and throughput are needed?
- Are dies separate tooling items per pellet shape/material?
- Does regolith pellet pressing require binder addition or sintering after pressing?
- Should catalyst pelletization be a tablet/pellet press or an extrusion/spheronization process?
