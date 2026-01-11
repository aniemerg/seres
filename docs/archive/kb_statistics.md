# Knowledge Base Statistics Summary

**Update 2026-01-11:** Archived as stale plan/memo; superseded by current src-based workflow.

Generated: 2025-12-16

## Overall Status

- **Total Entries in Index:** 2,556
- **Total Work Queue Items:** 730 pending
- **Completion Rate:** 77.7% (2,556 / 3,286 total needed)

## Item Counts by Type

| Type | Count | Percentage |
|------|-------|------------|
| Recipes | 775 | 30.3% |
| Parts | 500 | 19.6% |
| Processes | 212 | 8.3% |
| Machines | 168 | 6.6% |
| BOMs | 122 | 4.8% |
| Materials | 116 | 4.5% |
| Resources | 10 | 0.4% |
| Seeds | 4 | 0.2% |
| **Total Items** | **784** | **30.7%** |

## Machine Statistics

- **Total Machines:** 168
- **Machines with BOM:** 159 (94.6%)
- **Machines with Capabilities:** 167 (99.4%)
- **Total Capability Assignments:** 239
- **Unique Capabilities:** 201

## Recipe & BOM Coverage

### Recipe Coverage
- **Total Recipes:** 775
- **Items Needing Recipes:** 783
- **Items WITH Recipes:** 722 (92.2%)
- **Items WITHOUT Recipes:** 61 (7.8%)

### BOM Coverage
- **Total BOMs:** 122
- **Machines Needing BOMs:** 168
- **Machines WITH BOM Files:** 118 (70.2%)
- **Machines WITHOUT BOM Files:** 50 (29.8%)

## Manufacturing Complexity

- **Average Components per BOM:** 7.2
- **Total Component References:** 884
- **Average Steps per Recipe:** 3.2
- **Total Recipe Steps:** 2,379

## Process Layer Distribution

| Layer | Process Count |
|-------|---------------|
| layer_0 | 3 |
| layer_1 | 2 |
| layer_2 | 5 |
| layer_3 | 14 |
| layer_4 | 38 |
| layer_5 | 53 |
| layer_6 | 87 |
| layer_7 | 61 |
| layer_8 | 13 |
| **Total** | **212** |

## Material Class Distribution (Top 10)

| Material Class | Count |
|----------------|-------|
| Steel | 421 |
| Electronic | 70 |
| Composite | 68 |
| Ceramic | 29 |
| Glass | 13 |
| Organic | 12 |
| Copper | 11 |
| Aluminum | 10 |
| Metal | 8 |
| Mineral | 5 |

## Most Complex Machines (by component count)

1. MRE reactor v0 - 12 components
2. Cartesian 3D printer v0 - 11 components
3. High-temperature furnace v0 - 11 components
4. Reduction furnace v0 - 11 components
5. Milling machine (general) v0 - 10 components
6. Heat treatment furnace - 10 components
7. Cylindrical grinding machine v0 - 10 components
8. Magnetic core memory threading machine v0 - 10 components
9. Small loader - 10 components
10. FFC controlled DC power supply v0 - 10 components

## Most Referenced Items (in BOMs)

1. fastener_kit_medium - 73 BOMs
2. control_compute_module_imported - 34 BOMs
3. sensor_suite_general - 33 BOMs
4. control_panel_basic - 29 BOMs
5. power_conditioning_module - 26 BOMs
6. fastener_kit_small - 22 BOMs
7. support_frame_welded - 12 BOMs
8. power_output_terminals - 12 BOMs
9. drive_motor_medium - 11 BOMs
10. bearing_set_heavy - 9 BOMs

## Mass Distribution by Type

| Type | Total Mass (kg) | Average Mass (kg) |
|------|-----------------|-------------------|
| Machines | 77,530.0 | 461.5 |
| Parts | 27,944.4 | 55.9 |
| Materials | 64.0 | 0.6 |

## Seed File Analysis

| Seed File | Requirements |
|-----------|--------------|
| paper_reviews_dec2024_comprehensive_v0 | 343 |
| thermionic_system_roadmap_v0 | 61 |
| battery_system_nife_v0 | 48 |
| papers_gap_seed_v0 | 39 |
| **Total** | **491** |

## Progress This Session

- **Items Completed:** 75
- **Index Growth:** +221 entries (+9.5%)
- **Starting Index:** 2,335 entries
- **Final Index:** 2,556 entries
- **Files Created:** ~225 (items + recipes + BOMs + resources)

## Key Insights

1. **Strong Recipe Coverage:** 92.2% of items have manufacturing recipes defined
2. **Good BOM Coverage:** 94.6% of machines have BOMs, though only 70.2% have separate BOM files
3. **Layered Manufacturing:** Processes span 9 layers (layer_0 through layer_8), with most concentrated in layers 5-7
4. **Material Focus:** Steel dominates (421 items), followed by electronic and composite materials
5. **Modular Design:** Average of 7.2 components per machine suggests relatively modular construction
6. **Process Efficiency:** Average of 3.2 steps per recipe indicates streamlined manufacturing routes
7. **Work Remaining:** 730 pending items in work queue (22.3% of total system)

## Areas for Improvement

1. **BOM File Coverage:** 50 machines (29.8%) still need separate BOM files
2. **Recipe Gaps:** 61 items (7.8%) lack manufacturing recipes
3. **Resource Types:** Only 10 resource types defined - may need expansion
4. **Work Queue:** 730 items pending (mix of referenced_only, no_recipe, import_stub, etc.)
