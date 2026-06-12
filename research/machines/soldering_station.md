# Soldering Station

## Machine identity

- KB ID: `soldering_station`
- KB name: Soldering station
- KB file: `kb/items/machines/soldering_station.yaml`
- Current KB type: `machine`
- Current KB mass: 8 kg
- Current KB description: temperature-controlled soldering station for electronics assembly and wiring termination.

## KB usage and needed function

The KB uses `soldering_station` in manual electronics and wiring processes:

- `electronics_assembly_v0`
- `wiring_and_electronics_integration_v0`
- `crimping_and_soldering_basic_v0`
- `sensor_integration_v0`
- `position_sensor_set_assembly_v0`

It also appears in `bom_circuit_board_tools_v0`. The needed function is controlled hand soldering, tinning, connector/wire termination, PCB touch-up, sensor wiring, and small electronics assembly.

## Reality classification

Classification: real practical bench tool/station.

Temperature-controlled soldering stations are standard electronics assembly and repair equipment. They are not large production machines, but they are real reusable bench stations with a base controller, heating handpiece, tip, holder/stand, sensor feedback, and usually ESD-safe construction for electronics work.

The 8 kg KB mass is plausible for a station plus stand, cables, tips, accessories, enclosure, and some tooling, though many compact commercial stations are closer to 1-3 kg. If the KB item includes accessories and a rugged bench setup, 8 kg is acceptable.

## Evidence links

- Weller, "Soldering Stations": commercial product families include soldering, rework, hot-air, and desoldering stations, with ESD-safe and IPC-compliant options. Source: https://www.weller-tools.com/us/en/industrial-soldering/products/soldering-stations
- Weller WE 1010NA: digital 120 V soldering station described for a range of soldering jobs with improved controls and safety features. Source: https://www.weller-tools.com/we1010na/
- Hakko FX-888DX: commercial digital soldering station with ceramic heating element/sensor and multiple compatible handpieces. Source: https://hakkousa.com/fx-888dx.html
- SparkFun/Hakko FX888D listing: describes adjustable temperature control, 50-480 C range, ceramic heating element, rapid thermal recovery, and compact design. Source: https://sparkfuneducation.com/products/hakko-soldering-station.html
- Weller rework equipment page: distinguishes rework, hot-air, desoldering, and soldering procedures for electronic assemblies. Source: https://www.weller-tools.com/us/en/industrial-soldering/rework

## Commercial alternatives

- Hakko FX-888D/FX-888DX class temperature-controlled soldering stations.
- Weller WE/WT/WX line soldering stations.
- JBC cartridge-based stations for high-performance hand soldering.
- Hot-air/rework stations when SMT rework, BGA/QFP rework, or desoldering is required.
- Portable open-firmware irons such as Pinecil for low-mass field work, though they are not a full station.

## Build or open-source references

DIY temperature-controlled soldering stations are common and plausible because the core system is a heating element, temperature sensor, handpiece, power supply, controller, display/control interface, and stand.

Examples:

- Instructables, "DIY Digital Soldering Station": https://www.instructables.com/DIY-Digital-Soldering-Station/
- PCB Smoke, "DIY Digital Soldering Station": https://pcbsmoke.wordpress.com/2015/07/12/diy-digital-soldering-station/
- AxxSolder open-source JBC cartridge controller project: https://github.com/AxxAxx/AxxSolder

Local manufacture is realistic if resistive heating elements, ceramic insulation, temperature sensors, control electronics, safe power supply design, and tips are available. Soldering tips and ESD/safety quality may still be imported in early models.

## Related machine research

Related KB items:

- `pcb_fab_equipment`
- `circuit_board_tools`
- `reflow_soldering_process_v0`
- `soldering_process_wave_v0`
- `solder_paste_application_v0`
- `hand_tools_electrical`
- `power_supply_bench`

Hand soldering should remain distinct from reflow ovens, wave soldering, and automated pick-and-place equipment. A soldering station can support prototypes, repair, wiring, and low-volume assembly, while reflow/wave tools handle production PCB assembly.

## Recommendation for KB realism

Keep as a real reusable bench station.

Recommended future clarification: "Temperature-controlled hand soldering station for wiring, through-hole work, PCB touch-up, and low-volume electronics assembly." Do not treat it as a full PCB production line. For SMT boards, pair it with solder paste/reflow equipment or keep those processes separate.

This is a good example where labor bot plus tool is appropriate operationally: the soldering station provides controlled heat, and `labor_bot_general_v0` or a specialized electronics worker provides manipulation, inspection, and process judgment.

## Confidence and open questions

Confidence: high that the item is real and appropriate.

Open questions:

- Should the KB mass be reduced if the item represents only a compact station, or kept at 8 kg to include accessories and a rugged bench setup?
- Should hot-air rework/desoldering be included in this item or represented separately?
- Should soldering tips, flux, solder wire/paste, and fume extraction be explicit consumables/equipment?
