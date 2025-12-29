# Claude Base 001 - Complete Simulation Replay Guide

Generated: 2025-12-28 18:51:15
Total Events: 386
Duration: ~585.7 hours

This guide provides a complete step-by-step replay of the simulation.
Each event is documented with enough detail to manually reproduce the simulation.

================================================================================

## Executive Summary

- **52 imports** (929.2 kg total)
- **20 recipes** executed
- **58 processes** run
- **6 machines built**: labor_bot_general_v0, drill_press_v0, chemical_reactor_heated_v0,
  press_brake_v0, forge_or_induction_heater_v0, rolling_mill_v0
- **49 unique items** in final inventory
- **33 supply chains** established
- **Deepest supply chain**: 18 steps (tailings)

## Event Type Distribution

- **state_snapshot**: 167 events
- **process_complete**: 77 events
- **process_start**: 58 events
- **import**: 52 events
- **recipe_start**: 20 events
- **build**: 7 events
- **sim_start**: 3 events
- **preview**: 2 events

================================================================================

## Complete Event-by-Event Replay

Follow these events in order to manually replay the simulation:


### [1/386] SIM_START
**Timestamp**: `2025-12-20T18:05:37.121454Z`

**Action**: Initialize simulation
- Simulation ID: `claude_base_001`
- Start time: `2025-12-20T18:05:37.121454Z`

**Manual Replay**: Start a new simulation session.

### [2/386] IMPORT
**Timestamp**: `2025-12-20T18:05:37.121856Z`

**Action**: Import item from external supply
- Item: `labor_bot_general_v0`
- Quantity: `1.0 count`

**Manual Replay**: Add `1.0 count` of `labor_bot_general_v0` to inventory.

### [3/386] PROCESS_START
**Timestamp**: `2025-12-20T18:05:37.122170Z`

**Action**: Start process
- Process: `regolith_mining_simple_v0`
- Scale: `1.0x`

**Manual Replay**: Run process `regolith_mining_simple_v0` at scale 1.0x.

### [4/386] PREVIEW
**Timestamp**: `2025-12-20T18:05:37.122444Z`

**Action**: Preview operation

**Manual Replay**: This was a simulation preview, no action needed.

### [5/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-20T18:05:37.122457Z`

**Action**: Process completed
- Process: `regolith_mining_simple_v0`
- Outputs produced:
  - `regolith_lunar_mare`: 100.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [6/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-20T18:05:37.122494Z`

**Action**: State checkpoint
- Total inventory items: `2`
- Current inventory:
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [7/386] SIM_START
**Timestamp**: `2025-12-20T19:48:33.137154Z`

**Action**: Initialize simulation
- Simulation ID: `claude_base_001`
- Start time: `2025-12-20T19:48:33.137154Z`

**Manual Replay**: Start a new simulation session.

### [8/386] PROCESS_START
**Timestamp**: `2025-12-20T19:48:33.137596Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `1.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 1.0x.

### [9/386] SIM_START
**Timestamp**: `2025-12-20T19:48:45.477860Z`

**Action**: Initialize simulation
- Simulation ID: `claude_base_001`
- Start time: `2025-12-20T19:48:45.477860Z`

**Manual Replay**: Start a new simulation session.

### [10/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-20T19:48:45.478239Z`

**Action**: State checkpoint
- Total inventory items: `2`
- Current inventory:
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [11/386] PROCESS_START
**Timestamp**: `2025-12-21T02:37:34.595065Z`

**Action**: Start process
- Process: `regolith_mining_simple_v0`
- Scale: `1.0x`

**Manual Replay**: Run process `regolith_mining_simple_v0` at scale 1.0x.

### [12/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T02:37:34.595323Z`

**Action**: State checkpoint
- Total inventory items: `2`
- Current inventory:
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [13/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T02:37:34.595543Z`

**Action**: Process completed
- Process: `regolith_mining_simple_v0`
- Outputs produced:
  - `regolith_lunar_mare`: 100.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [14/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T02:37:34.595549Z`

**Action**: State checkpoint
- Total inventory items: `2`
- Current inventory:
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [15/386] PROCESS_START
**Timestamp**: `2025-12-21T02:37:34.595836Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `10.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 10.0x.

### [16/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T02:37:34.595839Z`

**Action**: State checkpoint
- Total inventory items: `2`
- Current inventory:
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [17/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T02:37:34.595897Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 6.0 kg
  - `tailings`: 4.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [18/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T02:37:34.595902Z`

**Action**: State checkpoint
- Total inventory items: `4`
- Current inventory:
  - `iron_ore_or_ilmenite`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [19/386] PROCESS_START
**Timestamp**: `2025-12-21T02:41:38.582226Z`

**Action**: Start process
- Process: `iron_pure_production_from_ilmenite_v0`
- Scale: `6.0x`

**Manual Replay**: Run process `iron_pure_production_from_ilmenite_v0` at scale 6.0x.

### [20/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T02:41:38.582563Z`

**Action**: State checkpoint
- Total inventory items: `3`
- Current inventory:
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [21/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T02:41:38.582780Z`

**Action**: Process completed
- Process: `iron_pure_production_from_ilmenite_v0`
- Outputs produced:
  - `iron_metal_pure`: 6.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [22/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T02:41:38.582787Z`

**Action**: State checkpoint
- Total inventory items: `4`
- Current inventory:
  - `iron_metal_pure`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [23/386] PROCESS_START
**Timestamp**: `2025-12-21T02:47:38.668053Z`

**Action**: Start process
- Process: `iron_powder_from_pure_iron_v0`
- Scale: `6.0x`

**Manual Replay**: Run process `iron_powder_from_pure_iron_v0` at scale 6.0x.

### [24/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T02:47:38.668396Z`

**Action**: State checkpoint
- Total inventory items: `3`
- Current inventory:
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [25/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T02:47:38.668630Z`

**Action**: Process completed
- Process: `iron_powder_from_pure_iron_v0`
- Outputs produced:
  - `iron_powder_or_sheet`: 6.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [26/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T02:47:38.668639Z`

**Action**: State checkpoint
- Total inventory items: `4`
- Current inventory:
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [27/386] IMPORT
**Timestamp**: `2025-12-21T02:48:27.036135Z`

**Action**: Import item from external supply
- Item: `heating_element_electric`
- Quantity: `12.0 kg`
- Mass: `12.0 kg`

**Manual Replay**: Add `12.0 kg` of `heating_element_electric` to inventory.

### [28/386] IMPORT
**Timestamp**: `2025-12-21T02:48:27.036605Z`

**Action**: Import item from external supply
- Item: `fastener_kit_medium`
- Quantity: `3.0 kg`
- Mass: `3.0 kg`

**Manual Replay**: Add `3.0 kg` of `fastener_kit_medium` to inventory.

### [29/386] IMPORT
**Timestamp**: `2025-12-21T02:48:54.386845Z`

**Action**: Import item from external supply
- Item: `drill_press_v0`
- Quantity: `1.0 count`

**Manual Replay**: Add `1.0 count` of `drill_press_v0` to inventory.

### [30/386] IMPORT
**Timestamp**: `2025-12-21T02:48:54.387334Z`

**Action**: Import item from external supply
- Item: `forge_or_induction_heater`
- Quantity: `1.0 count`

**Manual Replay**: Add `1.0 count` of `forge_or_induction_heater` to inventory.

### [31/386] PROCESS_START
**Timestamp**: `2025-12-21T03:00:28.461440Z`

**Action**: Start process
- Process: `regolith_mining_simple_v0`
- Scale: `1.0x`

**Manual Replay**: Run process `regolith_mining_simple_v0` at scale 1.0x.

### [32/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:00:28.461666Z`

**Action**: State checkpoint
- Total inventory items: `4`
- Current inventory:
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [33/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:00:28.462236Z`

**Action**: Process completed
- Process: `regolith_mining_simple_v0`
- Outputs produced:
  - `regolith_lunar_mare`: 100.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [34/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:00:28.462244Z`

**Action**: State checkpoint
- Total inventory items: `4`
- Current inventory:
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [35/386] PROCESS_START
**Timestamp**: `2025-12-21T03:00:28.462337Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `20.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 20.0x.

### [36/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:00:28.462340Z`

**Action**: State checkpoint
- Total inventory items: `4`
- Current inventory:
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [37/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:00:28.462403Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 12.0 kg
  - `tailings`: 8.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [38/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:00:28.462408Z`

**Action**: State checkpoint
- Total inventory items: `5`
- Current inventory:
  - `iron_ore_or_ilmenite`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [39/386] PROCESS_START
**Timestamp**: `2025-12-21T03:00:28.462486Z`

**Action**: Start process
- Process: `iron_pure_production_from_ilmenite_v0`
- Scale: `12.0x`

**Manual Replay**: Run process `iron_pure_production_from_ilmenite_v0` at scale 12.0x.

### [40/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:00:28.462489Z`

**Action**: State checkpoint
- Total inventory items: `4`
- Current inventory:
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [41/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:00:28.462543Z`

**Action**: Process completed
- Process: `iron_pure_production_from_ilmenite_v0`
- Outputs produced:
  - `iron_metal_pure`: 12.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [42/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:00:28.462548Z`

**Action**: State checkpoint
- Total inventory items: `5`
- Current inventory:
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [43/386] PROCESS_START
**Timestamp**: `2025-12-21T03:00:28.462623Z`

**Action**: Start process
- Process: `base_metal_parts_from_raw_metal_v0`
- Scale: `3.0x`

**Manual Replay**: Run process `base_metal_parts_from_raw_metal_v0` at scale 3.0x.

### [44/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:00:28.462626Z`

**Action**: State checkpoint
- Total inventory items: `5`
- Current inventory:
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [45/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:00:28.462706Z`

**Action**: Process completed
- Process: `base_metal_parts_from_raw_metal_v0`
- Outputs produced:
  - `base_metal_parts`: 3.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [46/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:00:28.462710Z`

**Action**: State checkpoint
- Total inventory items: `6`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [47/386] PROCESS_START
**Timestamp**: `2025-12-21T03:08:07.750083Z`

**Action**: Start process
- Process: `regolith_mining_simple_v0`
- Scale: `1.0x`

**Manual Replay**: Run process `regolith_mining_simple_v0` at scale 1.0x.

### [48/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:08:07.750420Z`

**Action**: State checkpoint
- Total inventory items: `6`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [49/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:08:07.750643Z`

**Action**: Process completed
- Process: `regolith_mining_simple_v0`
- Outputs produced:
  - `regolith_lunar_mare`: 100.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [50/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:08:07.750649Z`

**Action**: State checkpoint
- Total inventory items: `6`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [51/386] PROCESS_START
**Timestamp**: `2025-12-21T03:08:07.751018Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `30.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 30.0x.

### [52/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:08:07.751021Z`

**Action**: State checkpoint
- Total inventory items: `6`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [53/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:08:07.751101Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 18.0 kg
  - `tailings`: 12.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [54/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:08:07.751105Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_ore_or_ilmenite`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [55/386] PROCESS_START
**Timestamp**: `2025-12-21T03:08:07.751212Z`

**Action**: Start process
- Process: `iron_pure_production_from_ilmenite_v0`
- Scale: `18.0x`

**Manual Replay**: Run process `iron_pure_production_from_ilmenite_v0` at scale 18.0x.

### [56/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:08:07.751214Z`

**Action**: State checkpoint
- Total inventory items: `6`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [57/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:08:07.751263Z`

**Action**: Process completed
- Process: `iron_pure_production_from_ilmenite_v0`
- Outputs produced:
  - `iron_metal_pure`: 18.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [58/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:08:07.751266Z`

**Action**: State checkpoint
- Total inventory items: `6`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [59/386] PROCESS_START
**Timestamp**: `2025-12-21T03:08:07.751325Z`

**Action**: Start process
- Process: `base_metal_parts_from_raw_metal_v0`
- Scale: `7.0x`

**Manual Replay**: Run process `base_metal_parts_from_raw_metal_v0` at scale 7.0x.

### [60/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:08:07.751327Z`

**Action**: State checkpoint
- Total inventory items: `5`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [61/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:08:07.751377Z`

**Action**: Process completed
- Process: `base_metal_parts_from_raw_metal_v0`
- Outputs produced:
  - `base_metal_parts`: 7.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [62/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:08:07.751380Z`

**Action**: State checkpoint
- Total inventory items: `5`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [63/386] PROCESS_START
**Timestamp**: `2025-12-21T03:10:14.105665Z`

**Action**: Start process
- Process: `metal_parts_fabrication_v0`
- Scale: `3.0x`

**Manual Replay**: Run process `metal_parts_fabrication_v0` at scale 3.0x.

### [64/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:10:14.105958Z`

**Action**: State checkpoint
- Total inventory items: `5`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [65/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:10:14.106231Z`

**Action**: Process completed
- Process: `metal_parts_fabrication_v0`
- Outputs produced:
  - `cast_metal_parts`: 3.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [66/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:10:14.106237Z`

**Action**: State checkpoint
- Total inventory items: `6`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [67/386] PROCESS_START
**Timestamp**: `2025-12-21T03:10:14.106526Z`

**Action**: Start process
- Process: `regolith_mining_simple_v0`
- Scale: `1.0x`

**Manual Replay**: Run process `regolith_mining_simple_v0` at scale 1.0x.

### [68/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:10:14.106530Z`

**Action**: State checkpoint
- Total inventory items: `6`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [69/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:10:14.106602Z`

**Action**: Process completed
- Process: `regolith_mining_simple_v0`
- Outputs produced:
  - `regolith_lunar_mare`: 100.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [70/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:10:14.106607Z`

**Action**: State checkpoint
- Total inventory items: `6`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [71/386] PROCESS_START
**Timestamp**: `2025-12-21T03:10:14.106681Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `15.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 15.0x.

### [72/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:10:14.106683Z`

**Action**: State checkpoint
- Total inventory items: `6`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [73/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:10:14.106737Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 9.0 kg
  - `tailings`: 6.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [74/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:10:14.106741Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_ore_or_ilmenite`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [75/386] PROCESS_START
**Timestamp**: `2025-12-21T03:10:14.106828Z`

**Action**: Start process
- Process: `iron_pure_production_from_ilmenite_v0`
- Scale: `9.0x`

**Manual Replay**: Run process `iron_pure_production_from_ilmenite_v0` at scale 9.0x.

### [76/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:10:14.106830Z`

**Action**: State checkpoint
- Total inventory items: `6`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [77/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:10:14.106879Z`

**Action**: Process completed
- Process: `iron_pure_production_from_ilmenite_v0`
- Outputs produced:
  - `iron_metal_pure`: 9.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [78/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:10:14.106882Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [79/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:10:14.106937Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [80/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:10:14.106983Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [81/386] BUILD
**Timestamp**: `2025-12-21T03:45:12.487637Z`

**Action**: Build item
- Item: `None`
- Quantity: `1`

**Manual Replay**: Construct 1x `None` using available materials.

### [82/386] PROCESS_START
**Timestamp**: `2025-12-21T03:54:46.082323Z`

**Action**: Start process
- Process: `regolith_mining_simple_v0`
- Scale: `2.0x`

**Manual Replay**: Run process `regolith_mining_simple_v0` at scale 2.0x.

### [83/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:54:46.082506Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [84/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:54:46.082717Z`

**Action**: Process completed
- Process: `regolith_mining_simple_v0`
- Outputs produced:
  - `regolith_lunar_mare`: 200.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [85/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:54:46.082724Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [86/386] PROCESS_START
**Timestamp**: `2025-12-21T03:54:46.082886Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `3.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 3.0x.

### [87/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:54:46.082889Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [88/386] PROCESS_START
**Timestamp**: `2025-12-21T03:54:46.082973Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `3.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 3.0x.

### [89/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:54:46.082977Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [90/386] PROCESS_START
**Timestamp**: `2025-12-21T03:54:46.083063Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `3.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 3.0x.

### [91/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:54:46.083066Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [92/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:54:46.083170Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 1.7999999999999998 kg
  - `tailings`: 1.2000000000000002 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [93/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:54:46.083177Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 1.7999999999999998 kg
  - `tailings`: 1.2000000000000002 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [94/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:54:46.083182Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 1.7999999999999998 kg
  - `tailings`: 1.2000000000000002 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [95/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:54:46.083186Z`

**Action**: State checkpoint
- Total inventory items: `8`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_ore_or_ilmenite`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [96/386] PROCESS_START
**Timestamp**: `2025-12-21T03:56:05.977346Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `30.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 30.0x.

### [97/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:05.977554Z`

**Action**: State checkpoint
- Total inventory items: `8`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_ore_or_ilmenite`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [98/386] PROCESS_START
**Timestamp**: `2025-12-21T03:56:05.977749Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `30.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 30.0x.

### [99/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:05.977753Z`

**Action**: State checkpoint
- Total inventory items: `8`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_ore_or_ilmenite`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [100/386] PROCESS_START
**Timestamp**: `2025-12-21T03:56:05.977874Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `30.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 30.0x.

### [101/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:05.977876Z`

**Action**: State checkpoint
- Total inventory items: `8`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_ore_or_ilmenite`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [102/386] PROCESS_START
**Timestamp**: `2025-12-21T03:56:05.977954Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `30.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 30.0x.

### [103/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:05.977957Z`

**Action**: State checkpoint
- Total inventory items: `8`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_ore_or_ilmenite`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [104/386] PROCESS_START
**Timestamp**: `2025-12-21T03:56:05.978068Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `30.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 30.0x.

### [105/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:05.978070Z`

**Action**: State checkpoint
- Total inventory items: `8`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_ore_or_ilmenite`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [106/386] PROCESS_START
**Timestamp**: `2025-12-21T03:56:05.978149Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `30.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 30.0x.

### [107/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:05.978151Z`

**Action**: State checkpoint
- Total inventory items: `8`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_ore_or_ilmenite`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [108/386] PROCESS_START
**Timestamp**: `2025-12-21T03:56:05.978257Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `30.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 30.0x.

### [109/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:05.978259Z`

**Action**: State checkpoint
- Total inventory items: `8`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_ore_or_ilmenite`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [110/386] PROCESS_START
**Timestamp**: `2025-12-21T03:56:05.978463Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `30.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 30.0x.

### [111/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:05.978468Z`

**Action**: State checkpoint
- Total inventory items: `8`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_ore_or_ilmenite`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [112/386] PROCESS_START
**Timestamp**: `2025-12-21T03:56:05.978617Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `30.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 30.0x.

### [113/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:05.978620Z`

**Action**: State checkpoint
- Total inventory items: `8`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_ore_or_ilmenite`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [114/386] PROCESS_START
**Timestamp**: `2025-12-21T03:56:05.978742Z`

**Action**: Start process
- Process: `ilmenite_extraction_from_regolith_v0`
- Scale: `30.0x`

**Manual Replay**: Run process `ilmenite_extraction_from_regolith_v0` at scale 30.0x.

### [115/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:05.978744Z`

**Action**: State checkpoint
- Total inventory items: `8`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_ore_or_ilmenite`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [116/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:56:05.978862Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 18.0 kg
  - `tailings`: 12.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [117/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:56:05.978868Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 18.0 kg
  - `tailings`: 12.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [118/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:56:05.978874Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 18.0 kg
  - `tailings`: 12.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [119/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:56:05.978878Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 18.0 kg
  - `tailings`: 12.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [120/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:56:05.978881Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 18.0 kg
  - `tailings`: 12.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [121/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:56:05.978884Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 18.0 kg
  - `tailings`: 12.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [122/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:56:05.978887Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 18.0 kg
  - `tailings`: 12.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [123/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:56:05.978889Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 18.0 kg
  - `tailings`: 12.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [124/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:56:05.978892Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 18.0 kg
  - `tailings`: 12.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [125/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:56:05.978895Z`

**Action**: Process completed
- Process: `ilmenite_extraction_from_regolith_v0`
- Outputs produced:
  - `iron_ore_or_ilmenite`: 18.0 kg
  - `tailings`: 12.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [126/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:05.978899Z`

**Action**: State checkpoint
- Total inventory items: `8`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_ore_or_ilmenite`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [127/386] PROCESS_START
**Timestamp**: `2025-12-21T03:56:05.979093Z`

**Action**: Start process
- Process: `iron_pure_production_from_ilmenite_v0`
- Scale: `185.4x`

**Manual Replay**: Run process `iron_pure_production_from_ilmenite_v0` at scale 185.4x.

### [128/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:05.979095Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [129/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:56:05.979163Z`

**Action**: Process completed
- Process: `iron_pure_production_from_ilmenite_v0`
- Outputs produced:
  - `iron_metal_pure`: 185.4 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [130/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:05.979167Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [131/386] PROCESS_START
**Timestamp**: `2025-12-21T03:56:39.637387Z`

**Action**: Start process
- Process: `base_metal_parts_from_raw_metal_v0`
- Scale: `15.0x`

**Manual Replay**: Run process `base_metal_parts_from_raw_metal_v0` at scale 15.0x.

### [132/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:39.637685Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [133/386] PROCESS_START
**Timestamp**: `2025-12-21T03:56:39.637938Z`

**Action**: Start process
- Process: `base_metal_parts_from_raw_metal_v0`
- Scale: `15.0x`

**Manual Replay**: Run process `base_metal_parts_from_raw_metal_v0` at scale 15.0x.

### [134/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:39.637942Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [135/386] PROCESS_START
**Timestamp**: `2025-12-21T03:56:39.638022Z`

**Action**: Start process
- Process: `base_metal_parts_from_raw_metal_v0`
- Scale: `15.0x`

**Manual Replay**: Run process `base_metal_parts_from_raw_metal_v0` at scale 15.0x.

### [136/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:39.638025Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [137/386] PROCESS_START
**Timestamp**: `2025-12-21T03:56:39.638099Z`

**Action**: Start process
- Process: `base_metal_parts_from_raw_metal_v0`
- Scale: `15.0x`

**Manual Replay**: Run process `base_metal_parts_from_raw_metal_v0` at scale 15.0x.

### [138/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:39.638102Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [139/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:56:39.638272Z`

**Action**: Process completed
- Process: `base_metal_parts_from_raw_metal_v0`
- Outputs produced:
  - `base_metal_parts`: 15.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [140/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:56:39.638278Z`

**Action**: Process completed
- Process: `base_metal_parts_from_raw_metal_v0`
- Outputs produced:
  - `base_metal_parts`: 15.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [141/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:56:39.638281Z`

**Action**: Process completed
- Process: `base_metal_parts_from_raw_metal_v0`
- Outputs produced:
  - `base_metal_parts`: 15.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [142/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T03:56:39.638284Z`

**Action**: Process completed
- Process: `base_metal_parts_from_raw_metal_v0`
- Outputs produced:
  - `base_metal_parts`: 15.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [143/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:56:39.638289Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [144/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T03:59:15.656166Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [145/386] IMPORT
**Timestamp**: `2025-12-21T05:21:52.581955Z`

**Action**: Import item from external supply
- Item: `chemical_reactor_heated_v0`
- Quantity: `1.0 count`

**Manual Replay**: Add `1.0 count` of `chemical_reactor_heated_v0` to inventory.

### [146/386] IMPORT
**Timestamp**: `2025-12-21T05:22:25.754520Z`

**Action**: Import item from external supply
- Item: `rolling_mill_v0`
- Quantity: `1.0 count`

**Manual Replay**: Add `1.0 count` of `rolling_mill_v0` to inventory.

### [147/386] IMPORT
**Timestamp**: `2025-12-21T05:22:32.971152Z`

**Action**: Import item from external supply
- Item: `lathe_engine_v0`
- Quantity: `1.0 count`

**Manual Replay**: Add `1.0 count` of `lathe_engine_v0` to inventory.

### [148/386] IMPORT
**Timestamp**: `2025-12-21T05:22:32.971621Z`

**Action**: Import item from external supply
- Item: `press_brake_v0`
- Quantity: `1.0 count`

**Manual Replay**: Add `1.0 count` of `press_brake_v0` to inventory.

### [149/386] PROCESS_START
**Timestamp**: `2025-12-21T05:22:48.094644Z`

**Action**: Start process
- Process: `regolith_mining_highlands_v0`
- Scale: `1.0x`

**Manual Replay**: Run process `regolith_mining_highlands_v0` at scale 1.0x.

### [150/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:22:48.094953Z`

**Action**: State checkpoint
- Total inventory items: `7`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [151/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T05:23:05.633168Z`

**Action**: Process completed
- Process: `regolith_mining_highlands_v0`
- Outputs produced:
  - `regolith_lunar_highlands`: 100.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [152/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:23:05.633449Z`

**Action**: State checkpoint
- Total inventory items: `8`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [153/386] IMPORT
**Timestamp**: `2025-12-21T05:24:56.920475Z`

**Action**: Import item from external supply
- Item: `carbon_anode`
- Quantity: `2.0 kg`
- Mass: `2.0 kg`

**Manual Replay**: Add `2.0 kg` of `carbon_anode` to inventory.

### [154/386] IMPORT
**Timestamp**: `2025-12-21T05:24:56.920975Z`

**Action**: Import item from external supply
- Item: `cryolite_flux`
- Quantity: `0.5 kg`
- Mass: `0.5 kg`

**Manual Replay**: Add `0.5 kg` of `cryolite_flux` to inventory.

### [155/386] IMPORT
**Timestamp**: `2025-12-21T05:25:04.420494Z`

**Action**: Import item from external supply
- Item: `hydrochloric_acid`
- Quantity: `10.0 kg`
- Mass: `10.0 kg`

**Manual Replay**: Add `10.0 kg` of `hydrochloric_acid` to inventory.

### [156/386] IMPORT
**Timestamp**: `2025-12-21T05:27:47.581968Z`

**Action**: Import item from external supply
- Item: `carbon_anode`
- Quantity: `2.0 kg`
- Mass: `2.0 kg`

**Manual Replay**: Add `2.0 kg` of `carbon_anode` to inventory.

### [157/386] IMPORT
**Timestamp**: `2025-12-21T05:27:47.582384Z`

**Action**: Import item from external supply
- Item: `cryolite_flux`
- Quantity: `0.5 kg`
- Mass: `0.5 kg`

**Manual Replay**: Add `0.5 kg` of `cryolite_flux` to inventory.

### [158/386] IMPORT
**Timestamp**: `2025-12-21T05:27:47.582713Z`

**Action**: Import item from external supply
- Item: `hydrochloric_acid`
- Quantity: `10.0 kg`
- Mass: `10.0 kg`

**Manual Replay**: Add `10.0 kg` of `hydrochloric_acid` to inventory.

### [159/386] PREVIEW
**Timestamp**: `2025-12-21T05:28:12.658945Z`

**Action**: Preview operation

**Manual Replay**: This was a simulation preview, no action needed.

### [160/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:28:12.659239Z`

**Action**: State checkpoint
- Total inventory items: `8`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [161/386] IMPORT
**Timestamp**: `2025-12-21T05:33:22.518405Z`

**Action**: Import item from external supply
- Item: `carbon_anode`
- Quantity: `2.0 kg`
- Mass: `2.0 kg`

**Manual Replay**: Add `2.0 kg` of `carbon_anode` to inventory.

### [162/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:38:21.916372Z`

**Action**: State checkpoint
- Total inventory items: `8`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [163/386] IMPORT
**Timestamp**: `2025-12-21T05:43:47.426504Z`

**Action**: Import item from external supply
- Item: `hydrochloric_acid`
- Quantity: `10.0 kg`
- Mass: `10.0 kg`

**Manual Replay**: Add `10.0 kg` of `hydrochloric_acid` to inventory.

### [164/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:43:47.426706Z`

**Action**: State checkpoint
- Total inventory items: `9`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `hydrochloric_acid`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [165/386] PROCESS_START
**Timestamp**: `2025-12-21T05:43:54.837038Z`

**Action**: Start process
- Process: `alumina_extraction_from_highlands_v0`
- Scale: `1.0x`

**Manual Replay**: Run process `alumina_extraction_from_highlands_v0` at scale 1.0x.

### [166/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:43:54.837242Z`

**Action**: State checkpoint
- Total inventory items: `8`
- Current inventory:
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [167/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T05:44:07.939664Z`

**Action**: Process completed
- Process: `alumina_extraction_from_highlands_v0`
- Outputs produced:
  - `alumina_powder`: 12.0 kg
  - `processed_tailings_v0`: 98.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [168/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:44:07.939897Z`

**Action**: State checkpoint
- Total inventory items: `10`
- Current inventory:
  - `alumina_powder`: ? kg
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [169/386] PROCESS_START
**Timestamp**: `2025-12-21T05:49:20.258334Z`

**Action**: Start process
- Process: `regolith_mining_carbonaceous_v0`
- Scale: `1.0x`

**Manual Replay**: Run process `regolith_mining_carbonaceous_v0` at scale 1.0x.

### [170/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:49:20.258678Z`

**Action**: State checkpoint
- Total inventory items: `10`
- Current inventory:
  - `alumina_powder`: ? kg
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [171/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T05:49:28.049862Z`

**Action**: Process completed
- Process: `regolith_mining_carbonaceous_v0`
- Outputs produced:
  - `regolith_carbonaceous`: 50.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [172/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:49:28.050085Z`

**Action**: State checkpoint
- Total inventory items: `11`
- Current inventory:
  - `alumina_powder`: ? kg
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [173/386] PROCESS_START
**Timestamp**: `2025-12-21T05:49:37.842709Z`

**Action**: Start process
- Process: `carbon_extraction_from_carbonaceous_v0`
- Scale: `3.0x`

**Manual Replay**: Run process `carbon_extraction_from_carbonaceous_v0` at scale 3.0x.

### [174/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:49:37.843028Z`

**Action**: State checkpoint
- Total inventory items: `11`
- Current inventory:
  - `alumina_powder`: ? kg
  - `base_metal_parts`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [175/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T05:49:48.469434Z`

**Action**: Process completed
- Process: `carbon_extraction_from_carbonaceous_v0`
- Outputs produced:
  - `carbon_reductant`: 0.8999999999999999 kg
  - `tailings`: 29.099999999999998 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [176/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:49:48.469800Z`

**Action**: State checkpoint
- Total inventory items: `12`
- Current inventory:
  - `alumina_powder`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [177/386] PROCESS_START
**Timestamp**: `2025-12-21T05:50:16.406891Z`

**Action**: Start process
- Process: `silicon_extraction_from_regolith_carbothermic_v0`
- Scale: `0.75x`

**Manual Replay**: Run process `silicon_extraction_from_regolith_carbothermic_v0` at scale 0.75x.

### [178/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:50:16.407167Z`

**Action**: State checkpoint
- Total inventory items: `12`
- Current inventory:
  - `alumina_powder`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [179/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T05:50:26.815103Z`

**Action**: Process completed
- Process: `silicon_extraction_from_regolith_carbothermic_v0`
- Outputs produced:
  - `silicon_metal_v0`: 0.75 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [180/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:50:26.815368Z`

**Action**: State checkpoint
- Total inventory items: `13`
- Current inventory:
  - `alumina_powder`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - `silicon_metal_v0`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [181/386] IMPORT
**Timestamp**: `2025-12-21T05:51:15.419887Z`

**Action**: Import item from external supply
- Item: `carbon_anode`
- Quantity: `3.0 kg`
- Mass: `3.0 kg`

**Manual Replay**: Add `3.0 kg` of `carbon_anode` to inventory.

### [182/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:51:15.420139Z`

**Action**: State checkpoint
- Total inventory items: `14`
- Current inventory:
  - `alumina_powder`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - `silicon_metal_v0`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [183/386] IMPORT
**Timestamp**: `2025-12-21T05:51:31.127951Z`

**Action**: Import item from external supply
- Item: `cryolite_flux`
- Quantity: `1.0 kg`
- Mass: `1.0 kg`

**Manual Replay**: Add `1.0 kg` of `cryolite_flux` to inventory.

### [184/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:51:31.128291Z`

**Action**: State checkpoint
- Total inventory items: `15`
- Current inventory:
  - `alumina_powder`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - `silicon_metal_v0`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [185/386] PROCESS_START
**Timestamp**: `2025-12-21T05:51:33.506042Z`

**Action**: Start process
- Process: `aluminum_smelting_hall_heroult_v0`
- Scale: `5.0x`

**Manual Replay**: Run process `aluminum_smelting_hall_heroult_v0` at scale 5.0x.

### [186/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:51:33.506366Z`

**Action**: State checkpoint
- Total inventory items: `15`
- Current inventory:
  - `alumina_powder`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - `silicon_metal_v0`: ? kg
  - `tailings`: ? kg

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [187/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T05:51:44.013250Z`

**Action**: Process completed
- Process: `aluminum_smelting_hall_heroult_v0`
- Outputs produced:
  - `aluminum_alloy_ingot`: 5.0 kg
  - `co2_gas`: 7.5 kg
  - `cryolite_flux`: 0.675 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [188/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:51:44.013581Z`

**Action**: State checkpoint
- Total inventory items: `17`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - ... and 2 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [189/386] PROCESS_START
**Timestamp**: `2025-12-21T05:52:17.923282Z`

**Action**: Start process
- Process: `electrical_steel_production_v0`
- Scale: `5.0x`

**Manual Replay**: Run process `electrical_steel_production_v0` at scale 5.0x.

### [190/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:52:17.923568Z`

**Action**: State checkpoint
- Total inventory items: `17`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - ... and 2 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [191/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T05:52:27.561064Z`

**Action**: Process completed
- Process: `electrical_steel_production_v0`
- Outputs produced:
  - `electrical_steel_sheet`: 5.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [192/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:52:27.561308Z`

**Action**: State checkpoint
- Total inventory items: `18`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `cryolite_flux`: ? kg
  - `electrical_steel_sheet`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - `regolith_lunar_highlands`: ? kg
  - ... and 3 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [193/386] PROCESS_START
**Timestamp**: `2025-12-21T05:57:31.189798Z`

**Action**: Start process
- Process: `lamination_stamping_v0`
- Scale: `5.0x`

**Manual Replay**: Run process `lamination_stamping_v0` at scale 5.0x.

### [194/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:57:31.190081Z`

**Action**: State checkpoint
- Total inventory items: `17`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - ... and 2 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [195/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T05:57:39.425470Z`

**Action**: Process completed
- Process: `lamination_stamping_v0`
- Outputs produced:
  - `stator_rotor_lamination_set`: 4.75 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [196/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:57:39.425710Z`

**Action**: State checkpoint
- Total inventory items: `18`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - `regolith_lunar_highlands`: ? kg
  - `regolith_lunar_mare`: ? kg
  - ... and 3 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [197/386] IMPORT
**Timestamp**: `2025-12-21T05:58:18.939685Z`

**Action**: Import item from external supply
- Item: `aluminum_wire`
- Quantity: `2.5 kg`
- Mass: `2.5 kg`

**Manual Replay**: Add `2.5 kg` of `aluminum_wire` to inventory.

### [198/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:58:18.940021Z`

**Action**: State checkpoint
- Total inventory items: `19`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - `regolith_lunar_highlands`: ? kg
  - ... and 4 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [199/386] IMPORT
**Timestamp**: `2025-12-21T05:58:21.316049Z`

**Action**: Import item from external supply
- Item: `coil_insulation_material`
- Quantity: `0.1 kg`
- Mass: `0.1 kg`

**Manual Replay**: Add `0.1 kg` of `coil_insulation_material` to inventory.

### [200/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:58:21.316416Z`

**Action**: State checkpoint
- Total inventory items: `20`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - ... and 5 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [201/386] PROCESS_START
**Timestamp**: `2025-12-21T05:59:15.716762Z`

**Action**: Start process
- Process: `wire_drawing_aluminum_v0`
- Scale: `2.5x`

**Manual Replay**: Run process `wire_drawing_aluminum_v0` at scale 2.5x.

### [202/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:59:15.717077Z`

**Action**: State checkpoint
- Total inventory items: `20`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - ... and 5 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [203/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T05:59:24.477687Z`

**Action**: Process completed
- Process: `wire_drawing_aluminum_v0`
- Outputs produced:
  - `aluminum_wire`: 2.375 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [204/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T05:59:24.478044Z`

**Action**: State checkpoint
- Total inventory items: `20`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - ... and 5 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [205/386] IMPORT
**Timestamp**: `2025-12-21T06:00:19.583115Z`

**Action**: Import item from external supply
- Item: `coil_insulation_material`
- Quantity: `0.1 kg`
- Mass: `0.1 kg`

**Manual Replay**: Add `0.1 kg` of `coil_insulation_material` to inventory.

### [206/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T06:00:19.583361Z`

**Action**: State checkpoint
- Total inventory items: `20`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - ... and 5 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [207/386] PROCESS_START
**Timestamp**: `2025-12-21T06:00:29.007241Z`

**Action**: Start process
- Process: `coil_winding_basic_v0`
- Scale: `1.0x`

**Manual Replay**: Run process `coil_winding_basic_v0` at scale 1.0x.

### [208/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T06:00:29.007509Z`

**Action**: State checkpoint
- Total inventory items: `20`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - ... and 5 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [209/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T06:00:36.169652Z`

**Action**: Process completed
- Process: `coil_winding_basic_v0`
- Outputs produced:
  - `motor_coil_wound`: 2.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [210/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T06:00:36.169906Z`

**Action**: State checkpoint
- Total inventory items: `21`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_coil_wound`: ? kg
  - `processed_tailings_v0`: ? kg
  - ... and 6 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [211/386] RECIPE_START
**Timestamp**: `2025-12-21T06:07:41.182519Z`

**Action**: Start recipe
- Recipe: `recipe_motor_shaft_steel_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_motor_shaft_steel_v0` to produce 1x `None`.

### [212/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T06:07:41.183124Z`

**Action**: State checkpoint
- Total inventory items: `21`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_coil_wound`: ? kg
  - `processed_tailings_v0`: ? kg
  - ... and 6 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [213/386] RECIPE_START
**Timestamp**: `2025-12-21T06:07:47.724535Z`

**Action**: Start recipe
- Recipe: `recipe_motor_housing_steel_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_motor_housing_steel_v0` to produce 1x `None`.

### [214/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T06:07:47.724835Z`

**Action**: State checkpoint
- Total inventory items: `21`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_coil_wound`: ? kg
  - `processed_tailings_v0`: ? kg
  - ... and 6 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [215/386] IMPORT
**Timestamp**: `2025-12-21T06:07:56.228853Z`

**Action**: Import item from external supply
- Item: `bearing_set_small`
- Quantity: `0.5 kg`
- Mass: `0.5 kg`

**Manual Replay**: Add `0.5 kg` of `bearing_set_small` to inventory.

### [216/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T06:07:56.229155Z`

**Action**: State checkpoint
- Total inventory items: `22`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_small`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_coil_wound`: ? kg
  - ... and 7 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [217/386] PROCESS_START
**Timestamp**: `2025-12-21T06:08:32.644971Z`

**Action**: Start process
- Process: `electrical_steel_production_v0`
- Scale: `0.5x`

**Manual Replay**: Run process `electrical_steel_production_v0` at scale 0.5x.

### [218/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T06:08:32.645204Z`

**Action**: State checkpoint
- Total inventory items: `22`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_small`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_coil_wound`: ? kg
  - ... and 7 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [219/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T06:08:35.061195Z`

**Action**: Process completed
- Process: `recipe:recipe_motor_shaft_steel_v0`

**Manual Replay**: Add outputs to inventory as listed above.

### [220/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T06:08:35.061454Z`

**Action**: Process completed
- Process: `recipe:recipe_motor_housing_steel_v0`

**Manual Replay**: Add outputs to inventory as listed above.

### [221/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T06:08:35.061459Z`

**Action**: Process completed
- Process: `electrical_steel_production_v0`
- Outputs produced:
  - `electrical_steel_sheet`: 0.5 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [222/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T06:08:35.061470Z`

**Action**: State checkpoint
- Total inventory items: `23`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_small`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `electrical_steel_sheet`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - ... and 8 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [223/386] PROCESS_START
**Timestamp**: `2025-12-21T06:08:43.550680Z`

**Action**: Start process
- Process: `lamination_stamping_v0`
- Scale: `0.5x`

**Manual Replay**: Run process `lamination_stamping_v0` at scale 0.5x.

### [224/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T06:08:43.550868Z`

**Action**: State checkpoint
- Total inventory items: `22`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_small`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_coil_wound`: ? kg
  - ... and 7 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [225/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T06:08:46.084496Z`

**Action**: Process completed
- Process: `lamination_stamping_v0`
- Outputs produced:
  - `stator_rotor_lamination_set`: 0.475 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [226/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T06:08:46.084854Z`

**Action**: State checkpoint
- Total inventory items: `22`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_small`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_coil_wound`: ? kg
  - ... and 7 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [227/386] PROCESS_START
**Timestamp**: `2025-12-21T06:08:54.277664Z`

**Action**: Start process
- Process: `motor_final_assembly_v0`
- Scale: `1.0x`

**Manual Replay**: Run process `motor_final_assembly_v0` at scale 1.0x.

### [228/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T06:08:54.277956Z`

**Action**: State checkpoint
- Total inventory items: `20`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `processed_tailings_v0`: ? kg
  - `regolith_carbonaceous`: ? kg
  - ... and 5 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [229/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T06:11:26.549659Z`

**Action**: Process completed
- Process: `motor_final_assembly_v0`
- Outputs produced:
  - `motor_electric_small`: 1.0 unit

**Manual Replay**: Add outputs to inventory as listed above.

### [230/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T06:11:26.549954Z`

**Action**: State checkpoint
- Total inventory items: `21`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_electric_small`: ? unit
  - `processed_tailings_v0`: ? kg
  - ... and 6 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [231/386] IMPORT
**Timestamp**: `2025-12-21T14:33:23.737101Z`

**Action**: Import item from external supply
- Item: `plate_rolling_mill`
- Quantity: `1.0 count`

**Manual Replay**: Add `1.0 count` of `plate_rolling_mill` to inventory.

### [232/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T14:33:23.737403Z`

**Action**: State checkpoint
- Total inventory items: `22`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_electric_small`: ? unit
  - `plate_rolling_mill`: ? count
  - ... and 7 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [233/386] IMPORT
**Timestamp**: `2025-12-21T14:33:26.411442Z`

**Action**: Import item from external supply
- Item: `heat_treatment_furnace`
- Quantity: `1.0 count`

**Manual Replay**: Add `1.0 count` of `heat_treatment_furnace` to inventory.

### [234/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T14:33:26.411741Z`

**Action**: State checkpoint
- Total inventory items: `23`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_electric_small`: ? unit
  - ... and 8 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [235/386] PROCESS_START
**Timestamp**: `2025-12-21T14:34:50.934518Z`

**Action**: Start process
- Process: `steel_refining_basic_v0`
- Scale: `2.0x`

**Manual Replay**: Run process `steel_refining_basic_v0` at scale 2.0x.

### [236/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T14:34:50.934783Z`

**Action**: State checkpoint
- Total inventory items: `23`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_electric_small`: ? unit
  - ... and 8 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [237/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T14:34:57.660203Z`

**Action**: Process completed
- Process: `steel_refining_basic_v0`
- Outputs produced:
  - `steel_billet_or_slab`: 2.0 kg
  - `slag`: 0.1 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [238/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T14:34:57.660471Z`

**Action**: State checkpoint
- Total inventory items: `25`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_electric_small`: ? unit
  - ... and 10 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [239/386] PROCESS_START
**Timestamp**: `2025-12-21T14:35:25.299599Z`

**Action**: Start process
- Process: `steel_stock_hot_rolling_v0`
- Scale: `1.5x`

**Manual Replay**: Run process `steel_stock_hot_rolling_v0` at scale 1.5x.

### [240/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T14:35:25.299836Z`

**Action**: State checkpoint
- Total inventory items: `25`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_electric_small`: ? unit
  - ... and 10 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [241/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T14:35:32.096065Z`

**Action**: Process completed
- Process: `steel_stock_hot_rolling_v0`
- Outputs produced:
  - `steel_stock`: 1.5 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [242/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T14:35:32.096294Z`

**Action**: State checkpoint
- Total inventory items: `26`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_electric_small`: ? unit
  - ... and 11 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [243/386] RECIPE_START
**Timestamp**: `2025-12-21T14:35:52.528420Z`

**Action**: Start recipe
- Recipe: `recipe_fastener_kit_small_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_fastener_kit_small_v0` to produce 1x `None`.

### [244/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T14:35:52.528672Z`

**Action**: State checkpoint
- Total inventory items: `26`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_electric_small`: ? unit
  - ... and 11 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [245/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T14:36:11.291293Z`

**Action**: Process completed
- Process: `recipe:recipe_fastener_kit_small_v0`

**Manual Replay**: Add outputs to inventory as listed above.

### [246/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T14:36:11.291571Z`

**Action**: State checkpoint
- Total inventory items: `26`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_electric_small`: ? unit
  - ... and 11 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [247/386] PROCESS_START
**Timestamp**: `2025-12-21T14:39:33.196545Z`

**Action**: Start process
- Process: `fastener_kit_medium_production_v0`
- Scale: `1.0x`

**Manual Replay**: Run process `fastener_kit_medium_production_v0` at scale 1.0x.

### [248/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T14:39:33.196789Z`

**Action**: State checkpoint
- Total inventory items: `26`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - `motor_electric_small`: ? unit
  - ... and 11 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [249/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T14:39:41.071518Z`

**Action**: Process completed
- Process: `fastener_kit_medium_production_v0`
- Outputs produced:
  - `fastener_kit_medium`: 1.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [250/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T14:39:41.071862Z`

**Action**: State checkpoint
- Total inventory items: `27`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - ... and 12 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [251/386] PROCESS_START
**Timestamp**: `2025-12-21T15:23:35.477255Z`

**Action**: Start process
- Process: `steel_refining_basic_v0`
- Scale: `2.5x`

**Manual Replay**: Run process `steel_refining_basic_v0` at scale 2.5x.

### [252/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T15:23:35.477517Z`

**Action**: State checkpoint
- Total inventory items: `27`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - ... and 12 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [253/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T15:23:42.718592Z`

**Action**: Process completed
- Process: `steel_refining_basic_v0`
- Outputs produced:
  - `steel_billet_or_slab`: 2.5 kg
  - `slag`: 0.125 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [254/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T15:23:42.718851Z`

**Action**: State checkpoint
- Total inventory items: `27`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - ... and 12 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [255/386] PROCESS_START
**Timestamp**: `2025-12-21T15:23:56.985742Z`

**Action**: Start process
- Process: `steel_stock_hot_rolling_v0`
- Scale: `3.0x`

**Manual Replay**: Run process `steel_stock_hot_rolling_v0` at scale 3.0x.

### [256/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T15:23:56.986091Z`

**Action**: State checkpoint
- Total inventory items: `26`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - ... and 11 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [257/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T15:24:05.184261Z`

**Action**: Process completed
- Process: `steel_stock_hot_rolling_v0`
- Outputs produced:
  - `steel_stock`: 3.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [258/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T15:24:05.184569Z`

**Action**: State checkpoint
- Total inventory items: `26`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - ... and 11 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [259/386] PROCESS_START
**Timestamp**: `2025-12-21T15:24:28.739770Z`

**Action**: Start process
- Process: `steel_refining_basic_v0`
- Scale: `1.2x`

**Manual Replay**: Run process `steel_refining_basic_v0` at scale 1.2x.

### [260/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T15:24:28.740080Z`

**Action**: State checkpoint
- Total inventory items: `26`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - ... and 11 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [261/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T15:24:38.386762Z`

**Action**: Process completed
- Process: `steel_refining_basic_v0`
- Outputs produced:
  - `steel_billet_or_slab`: 1.2 kg
  - `slag`: 0.06 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [262/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T15:24:38.387056Z`

**Action**: State checkpoint
- Total inventory items: `27`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - ... and 12 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [263/386] PROCESS_START
**Timestamp**: `2025-12-21T15:24:41.427462Z`

**Action**: Start process
- Process: `steel_stock_hot_rolling_v0`
- Scale: `1.2x`

**Manual Replay**: Run process `steel_stock_hot_rolling_v0` at scale 1.2x.

### [264/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T15:24:41.427827Z`

**Action**: State checkpoint
- Total inventory items: `26`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - ... and 11 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [265/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T15:24:44.497012Z`

**Action**: Process completed
- Process: `steel_stock_hot_rolling_v0`
- Outputs produced:
  - `steel_stock`: 1.2 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [266/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T15:24:44.497242Z`

**Action**: State checkpoint
- Total inventory items: `26`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - ... and 11 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [267/386] PROCESS_START
**Timestamp**: `2025-12-21T15:24:56.597032Z`

**Action**: Start process
- Process: `bearing_set_heavy_production_v0`
- Scale: `1.0x`

**Manual Replay**: Run process `bearing_set_heavy_production_v0` at scale 1.0x.

### [268/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T15:24:56.597309Z`

**Action**: State checkpoint
- Total inventory items: `26`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - `labor_bot_general_v0`: ? count
  - ... and 11 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [269/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T15:25:05.019884Z`

**Action**: Process completed
- Process: `bearing_set_heavy_production_v0`
- Outputs produced:
  - `bearing_set_heavy`: 4.0 kg

**Manual Replay**: Add outputs to inventory as listed above.

### [270/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T15:25:05.020102Z`

**Action**: State checkpoint
- Total inventory items: `27`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 12 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [271/386] RECIPE_START
**Timestamp**: `2025-12-21T21:23:24.297292Z`

**Action**: Start recipe
- Recipe: `recipe_motor_assembly_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_motor_assembly_v0` to produce 1x `None`.

### [272/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:23:24.297604Z`

**Action**: State checkpoint
- Total inventory items: `27`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 12 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [273/386] RECIPE_START
**Timestamp**: `2025-12-21T21:23:31.180321Z`

**Action**: Start recipe
- Recipe: `recipe_shaft_and_bearing_set_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_shaft_and_bearing_set_v0` to produce 1x `None`.

### [274/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:23:31.180586Z`

**Action**: State checkpoint
- Total inventory items: `27`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 12 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [275/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:23:57.117938Z`

**Action**: Process completed
- Process: `recipe:recipe_motor_assembly_v0`

**Manual Replay**: Add outputs to inventory as listed above.

### [276/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:23:57.118210Z`

**Action**: Process completed
- Process: `recipe:recipe_shaft_and_bearing_set_v0`

**Manual Replay**: Add outputs to inventory as listed above.

### [277/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:23:57.118218Z`

**Action**: State checkpoint
- Total inventory items: `27`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 12 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [278/386] RECIPE_START
**Timestamp**: `2025-12-21T21:25:56.209648Z`

**Action**: Start recipe
- Recipe: `recipe_motor_assembly_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_motor_assembly_v0` to produce 1x `None`.

### [279/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:25:56.209889Z`

**Action**: State checkpoint
- Total inventory items: `27`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 12 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [280/386] RECIPE_START
**Timestamp**: `2025-12-21T21:25:58.726445Z`

**Action**: Start recipe
- Recipe: `recipe_shaft_and_bearing_set_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_shaft_and_bearing_set_v0` to produce 1x `None`.

### [281/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:25:58.726748Z`

**Action**: State checkpoint
- Total inventory items: `27`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 12 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [282/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:26:01.280933Z`

**Action**: Process completed
- Process: `recipe:recipe_motor_assembly_v0`
- Outputs produced:
  - `motor_assembly`: 1.0 count

**Manual Replay**: Add outputs to inventory as listed above.

### [283/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:26:01.281337Z`

**Action**: Process completed
- Process: `recipe:recipe_shaft_and_bearing_set_v0`
- Outputs produced:
  - `shaft_and_bearing_set`: 1.0 count

**Manual Replay**: Add outputs to inventory as listed above.

### [284/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:26:01.281345Z`

**Action**: State checkpoint
- Total inventory items: `29`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `fastener_kit_medium`: ? kg
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 14 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [285/386] BUILD
**Timestamp**: `2025-12-21T21:26:58.027239Z`

**Action**: Build item
- Item: `None`
- Quantity: `1`

**Manual Replay**: Construct 1x `None` using available materials.

### [286/386] RECIPE_START
**Timestamp**: `2025-12-21T21:27:25.664486Z`

**Action**: Start recipe
- Recipe: `recipe_machine_column_cast_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_machine_column_cast_v0` to produce 1x `None`.

### [287/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:27:25.664824Z`

**Action**: State checkpoint
- Total inventory items: `27`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 12 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [288/386] RECIPE_START
**Timestamp**: `2025-12-21T21:27:28.185657Z`

**Action**: Start recipe
- Recipe: `recipe_spindle_head_basic_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_spindle_head_basic_v0` to produce 1x `None`.

### [289/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:27:28.185895Z`

**Action**: State checkpoint
- Total inventory items: `27`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 12 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [290/386] IMPORT
**Timestamp**: `2025-12-21T21:31:29.813489Z`

**Action**: Import item from external supply
- Item: `metal_alloy_bulk`
- Quantity: `200.0 kg`
- Mass: `200.0 kg`

**Manual Replay**: Add `200.0 kg` of `metal_alloy_bulk` to inventory.

### [291/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:31:29.813793Z`

**Action**: State checkpoint
- Total inventory items: `28`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 13 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [292/386] RECIPE_START
**Timestamp**: `2025-12-21T21:31:41.048124Z`

**Action**: Start recipe
- Recipe: `recipe_table_top_t_slot_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_table_top_t_slot_v0` to produce 1x `None`.

### [293/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:31:41.048443Z`

**Action**: State checkpoint
- Total inventory items: `28`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 13 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [294/386] RECIPE_START
**Timestamp**: `2025-12-21T21:31:43.532946Z`

**Action**: Start recipe
- Recipe: `recipe_depth_stop_mechanism_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_depth_stop_mechanism_v0` to produce 1x `None`.

### [295/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:31:43.533262Z`

**Action**: State checkpoint
- Total inventory items: `28`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 13 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [296/386] RECIPE_START
**Timestamp**: `2025-12-21T21:31:46.037965Z`

**Action**: Start recipe
- Recipe: `recipe_belt_and_pulley_set_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_belt_and_pulley_set_v0` to produce 1x `None`.

### [297/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:31:46.038215Z`

**Action**: State checkpoint
- Total inventory items: `28`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 13 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [298/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:32:04.769214Z`

**Action**: Process completed
- Process: `recipe:recipe_machine_column_cast_v0`

**Manual Replay**: Add outputs to inventory as listed above.

### [299/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:32:04.769471Z`

**Action**: Process completed
- Process: `recipe:recipe_spindle_head_basic_v0`

**Manual Replay**: Add outputs to inventory as listed above.

### [300/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:32:04.769475Z`

**Action**: Process completed
- Process: `recipe:recipe_table_top_t_slot_v0`

**Manual Replay**: Add outputs to inventory as listed above.

### [301/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:32:04.769477Z`

**Action**: Process completed
- Process: `recipe:recipe_depth_stop_mechanism_v0`

**Manual Replay**: Add outputs to inventory as listed above.

### [302/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:32:04.769479Z`

**Action**: Process completed
- Process: `recipe:recipe_belt_and_pulley_set_v0`

**Manual Replay**: Add outputs to inventory as listed above.

### [303/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:32:04.769497Z`

**Action**: State checkpoint
- Total inventory items: `28`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 13 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [304/386] RECIPE_START
**Timestamp**: `2025-12-21T21:33:35.652442Z`

**Action**: Start recipe
- Recipe: `recipe_machine_column_cast_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_machine_column_cast_v0` to produce 1x `None`.

### [305/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:33:35.652678Z`

**Action**: State checkpoint
- Total inventory items: `28`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 13 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [306/386] RECIPE_START
**Timestamp**: `2025-12-21T21:33:38.197661Z`

**Action**: Start recipe
- Recipe: `recipe_spindle_head_basic_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_spindle_head_basic_v0` to produce 1x `None`.

### [307/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:33:38.198024Z`

**Action**: State checkpoint
- Total inventory items: `28`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 13 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [308/386] RECIPE_START
**Timestamp**: `2025-12-21T21:33:40.659656Z`

**Action**: Start recipe
- Recipe: `recipe_table_top_t_slot_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_table_top_t_slot_v0` to produce 1x `None`.

### [309/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:33:40.659980Z`

**Action**: State checkpoint
- Total inventory items: `28`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 13 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [310/386] RECIPE_START
**Timestamp**: `2025-12-21T21:33:43.166459Z`

**Action**: Start recipe
- Recipe: `recipe_depth_stop_mechanism_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_depth_stop_mechanism_v0` to produce 1x `None`.

### [311/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:33:43.166710Z`

**Action**: State checkpoint
- Total inventory items: `28`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 13 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [312/386] RECIPE_START
**Timestamp**: `2025-12-21T21:33:45.672949Z`

**Action**: Start recipe
- Recipe: `recipe_belt_and_pulley_set_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_belt_and_pulley_set_v0` to produce 1x `None`.

### [313/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:33:45.673191Z`

**Action**: State checkpoint
- Total inventory items: `28`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - `iron_powder_or_sheet`: ? kg
  - ... and 13 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [314/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:33:48.171380Z`

**Action**: Process completed
- Process: `recipe:recipe_machine_column_cast_v0`
- Outputs produced:
  - `machine_column_cast`: 1.0 unit

**Manual Replay**: Add outputs to inventory as listed above.

### [315/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:33:48.171744Z`

**Action**: Process completed
- Process: `recipe:recipe_spindle_head_basic_v0`
- Outputs produced:
  - `spindle_head_basic`: 1.0 unit

**Manual Replay**: Add outputs to inventory as listed above.

### [316/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:33:48.171748Z`

**Action**: Process completed
- Process: `recipe:recipe_table_top_t_slot_v0`
- Outputs produced:
  - `table_top_t_slot`: 1.0 unit

**Manual Replay**: Add outputs to inventory as listed above.

### [317/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:33:48.171752Z`

**Action**: Process completed
- Process: `recipe:recipe_depth_stop_mechanism_v0`
- Outputs produced:
  - `depth_stop_mechanism`: 1.0 unit

**Manual Replay**: Add outputs to inventory as listed above.

### [318/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:33:48.171756Z`

**Action**: Process completed
- Process: `recipe:recipe_belt_and_pulley_set_v0`
- Outputs produced:
  - `belt_and_pulley_set`: 1.0 unit

**Manual Replay**: Add outputs to inventory as listed above.

### [319/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:33:48.171764Z`

**Action**: State checkpoint
- Total inventory items: `33`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `belt_and_pulley_set`: ? unit
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `depth_stop_mechanism`: ? unit
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - ... and 18 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [320/386] BUILD
**Timestamp**: `2025-12-21T21:33:55.548477Z`

**Action**: Build item
- Item: `None`
- Quantity: `1`

**Manual Replay**: Construct 1x `None` using available materials.

### [321/386] RECIPE_START
**Timestamp**: `2025-12-21T21:35:31.663450Z`

**Action**: Start recipe
- Recipe: `recipe_motor_assembly_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_motor_assembly_v0` to produce 1x `None`.

### [322/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:35:31.663766Z`

**Action**: State checkpoint
- Total inventory items: `28`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - ... and 13 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [323/386] RECIPE_START
**Timestamp**: `2025-12-21T21:35:46.841069Z`

**Action**: Start recipe
- Recipe: `recipe_power_electronics_module_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_power_electronics_module_v0` to produce 1x `None`.

### [324/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:35:46.841351Z`

**Action**: State checkpoint
- Total inventory items: `28`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - `iron_metal_pure`: ? kg
  - ... and 13 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [325/386] IMPORT
**Timestamp**: `2025-12-21T21:36:15.747405Z`

**Action**: Import item from external supply
- Item: `chemical_reactor_heated_body`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `chemical_reactor_heated_body` to inventory.

### [326/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:36:15.747809Z`

**Action**: State checkpoint
- Total inventory items: `29`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_body`: ? unit
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - ... and 14 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [327/386] IMPORT
**Timestamp**: `2025-12-21T21:36:18.289595Z`

**Action**: Import item from external supply
- Item: `reactor_shell_steel_v0`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `reactor_shell_steel_v0` to inventory.

### [328/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:36:18.289865Z`

**Action**: State checkpoint
- Total inventory items: `30`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_body`: ? unit
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - ... and 15 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [329/386] IMPORT
**Timestamp**: `2025-12-21T21:36:20.820409Z`

**Action**: Import item from external supply
- Item: `pressure_vessel_steel`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `pressure_vessel_steel` to inventory.

### [330/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:36:20.820745Z`

**Action**: State checkpoint
- Total inventory items: `31`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_body`: ? unit
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - ... and 16 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [331/386] IMPORT
**Timestamp**: `2025-12-21T21:36:23.320417Z`

**Action**: Import item from external supply
- Item: `heating_element_set_basic`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `heating_element_set_basic` to inventory.

### [332/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:36:23.320649Z`

**Action**: State checkpoint
- Total inventory items: `32`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_body`: ? unit
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - ... and 17 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [333/386] BUILD
**Timestamp**: `2025-12-21T21:36:25.890237Z`

**Action**: Build item
- Item: `None`
- Quantity: `1`

**Manual Replay**: Construct 1x `None` using available materials.

### [334/386] IMPORT
**Timestamp**: `2025-12-21T21:37:31.647320Z`

**Action**: Import item from external supply
- Item: `steel_drum`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `steel_drum` to inventory.

### [335/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:37:31.647561Z`

**Action**: State checkpoint
- Total inventory items: `30`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - `heat_treatment_furnace`: ? count
  - ... and 15 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [336/386] IMPORT
**Timestamp**: `2025-12-21T21:37:34.224361Z`

**Action**: Import item from external supply
- Item: `bearing_set`
- Quantity: `2.0 unit`

**Manual Replay**: Add `2.0 unit` of `bearing_set` to inventory.

### [337/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:37:34.224687Z`

**Action**: State checkpoint
- Total inventory items: `31`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - ... and 16 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [338/386] IMPORT
**Timestamp**: `2025-12-21T21:37:36.795530Z`

**Action**: Import item from external supply
- Item: `grinding_media_steel`
- Quantity: `50.0 kg`
- Mass: `50.0 kg`

**Manual Replay**: Add `50.0 kg` of `grinding_media_steel` to inventory.

### [339/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:37:36.795745Z`

**Action**: State checkpoint
- Total inventory items: `32`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - ... and 17 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [340/386] RECIPE_START
**Timestamp**: `2025-12-21T21:37:39.314840Z`

**Action**: Start recipe
- Recipe: `recipe_motor_assembly_v0`
- Target: `None` (qty: 1)
- Estimated duration: `1.0 hours`

**Manual Replay**: Begin recipe `recipe_motor_assembly_v0` to produce 1x `None`.

### [341/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:37:39.315108Z`

**Action**: State checkpoint
- Total inventory items: `32`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - ... and 17 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [342/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:37:41.854093Z`

**Action**: Process completed
- Process: `recipe:recipe_motor_assembly_v0`
- Outputs produced:
  - `motor_assembly`: 1.0 count

**Manual Replay**: Add outputs to inventory as listed above.

### [343/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:37:41.854333Z`

**Action**: Process completed
- Process: `recipe:recipe_power_electronics_module_v0`

**Manual Replay**: Add outputs to inventory as listed above.

### [344/386] PROCESS_COMPLETE
**Timestamp**: `2025-12-21T21:37:41.854338Z`

**Action**: Process completed
- Process: `recipe:recipe_motor_assembly_v0`
- Outputs produced:
  - `motor_assembly`: 1.0 count

**Manual Replay**: Add outputs to inventory as listed above.

### [345/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:37:41.854348Z`

**Action**: State checkpoint
- Total inventory items: `33`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - ... and 18 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [346/386] BUILD
**Timestamp**: `2025-12-21T21:38:01.231238Z`

**Action**: Build item
- Item: `None`
- Quantity: `1`

**Manual Replay**: Construct 1x `None` using available materials.

### [347/386] IMPORT
**Timestamp**: `2025-12-21T21:38:44.789069Z`

**Action**: Import item from external supply
- Item: `machined_steel_part_precision`
- Quantity: `120.0 kg`
- Mass: `120.0 kg`

**Manual Replay**: Add `120.0 kg` of `machined_steel_part_precision` to inventory.

### [348/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:38:44.789326Z`

**Action**: State checkpoint
- Total inventory items: `34`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - ... and 19 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [349/386] IMPORT
**Timestamp**: `2025-12-21T21:38:47.375924Z`

**Action**: Import item from external supply
- Item: `structural_steel_frame`
- Quantity: `500.0 kg`
- Mass: `500.0 kg`

**Manual Replay**: Add `500.0 kg` of `structural_steel_frame` to inventory.

### [350/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:38:47.376242Z`

**Action**: State checkpoint
- Total inventory items: `35`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - ... and 20 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [351/386] IMPORT
**Timestamp**: `2025-12-21T21:38:49.993807Z`

**Action**: Import item from external supply
- Item: `hydraulic_system_medium`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `hydraulic_system_medium` to inventory.

### [352/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:38:49.994036Z`

**Action**: State checkpoint
- Total inventory items: `36`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - ... and 21 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [353/386] IMPORT
**Timestamp**: `2025-12-21T21:38:52.534158Z`

**Action**: Import item from external supply
- Item: `power_electronics_module`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `power_electronics_module` to inventory.

### [354/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:38:52.534568Z`

**Action**: State checkpoint
- Total inventory items: `37`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - ... and 22 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [355/386] IMPORT
**Timestamp**: `2025-12-21T21:38:55.099857Z`

**Action**: Import item from external supply
- Item: `control_panel_assembly_v0`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `control_panel_assembly_v0` to inventory.

### [356/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:38:55.100114Z`

**Action**: State checkpoint
- Total inventory items: `38`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `control_panel_assembly_v0`: ? unit
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - ... and 23 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [357/386] IMPORT
**Timestamp**: `2025-12-21T21:39:05.542267Z`

**Action**: Import item from external supply
- Item: `fastener_kit_medium`
- Quantity: `1.0 kit`

**Manual Replay**: Add `1.0 kit` of `fastener_kit_medium` to inventory.

### [358/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:39:05.542567Z`

**Action**: State checkpoint
- Total inventory items: `39`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `control_panel_assembly_v0`: ? unit
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - ... and 24 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [359/386] BUILD
**Timestamp**: `2025-12-21T21:39:08.131281Z`

**Action**: Build item
- Item: `None`
- Quantity: `1`

**Manual Replay**: Construct 1x `None` using available materials.

### [360/386] IMPORT
**Timestamp**: `2025-12-21T21:41:32.136919Z`

**Action**: Import item from external supply
- Item: `lathe_bed_simple`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `lathe_bed_simple` to inventory.

### [361/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:41:32.137157Z`

**Action**: State checkpoint
- Total inventory items: `37`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - ... and 22 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [362/386] IMPORT
**Timestamp**: `2025-12-21T21:41:34.694394Z`

**Action**: Import item from external supply
- Item: `lathe_headstock_simple`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `lathe_headstock_simple` to inventory.

### [363/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:41:34.694656Z`

**Action**: State checkpoint
- Total inventory items: `38`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - ... and 23 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [364/386] IMPORT
**Timestamp**: `2025-12-21T21:41:37.265653Z`

**Action**: Import item from external supply
- Item: `lathe_spindle_and_bearings`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `lathe_spindle_and_bearings` to inventory.

### [365/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:41:37.265963Z`

**Action**: State checkpoint
- Total inventory items: `39`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - ... and 24 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [366/386] IMPORT
**Timestamp**: `2025-12-21T21:41:39.912719Z`

**Action**: Import item from external supply
- Item: `tailstock_assembly`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `tailstock_assembly` to inventory.

### [367/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:41:39.912972Z`

**Action**: State checkpoint
- Total inventory items: `40`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - ... and 25 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [368/386] IMPORT
**Timestamp**: `2025-12-21T21:41:42.469503Z`

**Action**: Import item from external supply
- Item: `lathe_carriage_simple`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `lathe_carriage_simple` to inventory.

### [369/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:41:42.469734Z`

**Action**: State checkpoint
- Total inventory items: `41`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - ... and 26 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [370/386] IMPORT
**Timestamp**: `2025-12-21T21:41:45.031198Z`

**Action**: Import item from external supply
- Item: `lathe_leadscrew_simple`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `lathe_leadscrew_simple` to inventory.

### [371/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:41:45.031555Z`

**Action**: State checkpoint
- Total inventory items: `42`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - ... and 27 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [372/386] IMPORT
**Timestamp**: `2025-12-21T21:41:47.576304Z`

**Action**: Import item from external supply
- Item: `lathe_tool_post_basic`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `lathe_tool_post_basic` to inventory.

### [373/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:41:47.576613Z`

**Action**: State checkpoint
- Total inventory items: `43`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - ... and 28 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [374/386] IMPORT
**Timestamp**: `2025-12-21T21:41:50.145056Z`

**Action**: Import item from external supply
- Item: `gearbox_reducer_small`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `gearbox_reducer_small` to inventory.

### [375/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:41:50.145381Z`

**Action**: State checkpoint
- Total inventory items: `44`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - `forge_or_induction_heater_v0`: ? count
  - ... and 29 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [376/386] IMPORT
**Timestamp**: `2025-12-21T21:41:52.771530Z`

**Action**: Import item from external supply
- Item: `control_panel_basic`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `control_panel_basic` to inventory.

### [377/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:41:52.771765Z`

**Action**: State checkpoint
- Total inventory items: `45`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `control_panel_basic`: ? unit
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - ... and 30 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [378/386] IMPORT
**Timestamp**: `2025-12-21T21:41:55.337975Z`

**Action**: Import item from external supply
- Item: `turning_tools_general`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `turning_tools_general` to inventory.

### [379/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:41:55.338267Z`

**Action**: State checkpoint
- Total inventory items: `46`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `control_panel_basic`: ? unit
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - ... and 31 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [380/386] IMPORT
**Timestamp**: `2025-12-21T21:41:57.869905Z`

**Action**: Import item from external supply
- Item: `safety_guard_steel_mesh`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `safety_guard_steel_mesh` to inventory.

### [381/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:41:57.870145Z`

**Action**: State checkpoint
- Total inventory items: `47`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `control_panel_basic`: ? unit
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - ... and 32 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [382/386] IMPORT
**Timestamp**: `2025-12-21T21:42:10.915607Z`

**Action**: Import item from external supply
- Item: `motor_electric_small`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `motor_electric_small` to inventory.

### [383/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:42:10.915912Z`

**Action**: State checkpoint
- Total inventory items: `48`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `control_panel_basic`: ? unit
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - ... and 33 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [384/386] IMPORT
**Timestamp**: `2025-12-21T21:42:21.617884Z`

**Action**: Import item from external supply
- Item: `fastener_kit_medium`
- Quantity: `1.0 unit`

**Manual Replay**: Add `1.0 unit` of `fastener_kit_medium` to inventory.

### [385/386] STATE_SNAPSHOT
**Timestamp**: `2025-12-21T21:42:21.618179Z`

**Action**: State checkpoint
- Total inventory items: `49`
- Sample inventory (first 15 items):
  - `alumina_powder`: ? kg
  - `aluminum_alloy_ingot`: ? kg
  - `aluminum_wire`: ? kg
  - `base_metal_parts`: ? kg
  - `bearing_set`: ? unit
  - `bearing_set_heavy`: ? kg
  - `carbon_anode`: ? kg
  - `carbon_reductant`: ? kg
  - `cast_metal_parts`: ? kg
  - `chemical_reactor_heated_v0`: ? count
  - `co2_gas`: ? kg
  - `coil_insulation_material`: ? kg
  - `control_panel_basic`: ? unit
  - `cryolite_flux`: ? kg
  - `drill_press_v0`: ? count
  - ... and 34 more items

**Manual Replay**: Checkpoint - verify inventory matches the state above.

### [386/386] BUILD
**Timestamp**: `2025-12-21T21:42:37.510661Z`

**Action**: Build item
- Item: `None`
- Quantity: `1`

**Manual Replay**: Construct 1x `None` using available materials.

================================================================================

## Final Inventory State

**Total items**: 49

| Item ID | Quantity | Unit |
|---------|----------|------|
| `alumina_powder` | ? | kg |
| `aluminum_alloy_ingot` | ? | kg |
| `aluminum_wire` | ? | kg |
| `base_metal_parts` | ? | kg |
| `bearing_set` | ? | unit |
| `bearing_set_heavy` | ? | kg |
| `carbon_anode` | ? | kg |
| `carbon_reductant` | ? | kg |
| `cast_metal_parts` | ? | kg |
| `chemical_reactor_heated_v0` | ? | count |
| `co2_gas` | ? | kg |
| `coil_insulation_material` | ? | kg |
| `control_panel_basic` | ? | unit |
| `cryolite_flux` | ? | kg |
| `drill_press_v0` | ? | count |
| `fastener_kit_medium` | ? | unit |
| `forge_or_induction_heater_v0` | ? | count |
| `gearbox_reducer_small` | ? | unit |
| `grinding_media_steel` | ? | kg |
| `heat_treatment_furnace` | ? | count |
| `iron_metal_pure` | ? | kg |
| `iron_powder_or_sheet` | ? | kg |
| `labor_bot_general_v0` | ? | count |
| `lathe_bed_simple` | ? | unit |
| `lathe_carriage_simple` | ? | unit |
| `lathe_headstock_simple` | ? | unit |
| `lathe_leadscrew_simple` | ? | unit |
| `lathe_spindle_and_bearings` | ? | unit |
| `lathe_tool_post_basic` | ? | unit |
| `machined_steel_part_precision` | ? | kg |
| `metal_alloy_bulk` | ? | kg |
| `motor_assembly` | ? | count |
| `motor_electric_small` | ? | unit |
| `plate_rolling_mill` | ? | count |
| `press_brake_v0` | ? | count |
| `processed_tailings_v0` | ? | kg |
| `regolith_carbonaceous` | ? | kg |
| `regolith_lunar_highlands` | ? | kg |
| `regolith_lunar_mare` | ? | kg |
| `rolling_mill_v0` | ? | count |
| `safety_guard_steel_mesh` | ? | unit |
| `silicon_metal_v0` | ? | kg |
| `slag` | ? | kg |
| `stator_rotor_lamination_set` | ? | kg |
| `steel_stock` | ? | kg |
| `structural_steel_frame` | ? | kg |
| `tailings` | ? | kg |
| `tailstock_assembly` | ? | unit |
| `turning_tools_general` | ? | unit |

================================================================================

## Key Supply Chains Established

These show which processes produce which items:

- `alumina_powder` ← `alumina_extraction_from_highlands_v0`
- `aluminum_alloy_ingot` ← `aluminum_smelting_hall_heroult_v0`
- `aluminum_wire` ← `wire_drawing_aluminum_v0`
- `base_metal_parts` ← `base_metal_parts_from_raw_metal_v0`
- `bearing_set_heavy` ← `bearing_set_heavy_production_v0`
- `belt_and_pulley_set` ← `recipe:recipe_belt_and_pulley_set_v0`
- `carbon_reductant` ← `carbon_extraction_from_carbonaceous_v0`
- `cast_metal_parts` ← `metal_parts_fabrication_v0`
- `co2_gas` ← `aluminum_smelting_hall_heroult_v0`
- `cryolite_flux` ← `aluminum_smelting_hall_heroult_v0`
- `depth_stop_mechanism` ← `recipe:recipe_depth_stop_mechanism_v0`
- `electrical_steel_sheet` ← `electrical_steel_production_v0`
- `fastener_kit_medium` ← `fastener_kit_medium_production_v0`
- `iron_metal_pure` ← `iron_pure_production_from_ilmenite_v0`
- `iron_ore_or_ilmenite` ← `ilmenite_extraction_from_regolith_v0`
- `iron_powder_or_sheet` ← `iron_powder_from_pure_iron_v0`
- `machine_column_cast` ← `recipe:recipe_machine_column_cast_v0`
- `motor_assembly` ← `recipe:recipe_motor_assembly_v0`
- `motor_coil_wound` ← `coil_winding_basic_v0`
- `motor_electric_small` ← `motor_final_assembly_v0`

================================================================================

## End of Replay Guide

You now have a complete step-by-step guide to manually replay the claude_base_001 simulation.
