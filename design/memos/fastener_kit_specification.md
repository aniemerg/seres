# Fastener Kit Specification

## Purpose
Define the detailed contents of standardized fastener kits used throughout the KB. These kits provide assorted hardware for mechanical assemblies.

## Design Principles
1. **Metric Standard** - Use ISO metric threads (M3, M4, M5, M6, M8, M10, M12)
2. **Common Lengths** - Stock 3-4 lengths per size to cover 80% of use cases
3. **Steel Construction** - Standard carbon steel, can be upgraded to stainless for corrosion resistance
4. **Balanced Mix** - Include bolts, nuts, washers in ratios matching typical assembly needs
5. **Mass-Based Kits** - Total kit mass is the controlled parameter

## Fastener Kit Small (1.5 kg)
**Target Applications**: Electronics, instrumentation, light mechanical assemblies
**Size Range**: M3 to M8

### Contents Breakdown:

#### M3 Fasteners (~300g, 20%)
- Socket head cap screws M3x8: 50 pcs (~75g)
- Socket head cap screws M3x12: 50 pcs (~85g)
- Hex nuts M3: 120 pcs (~60g)
- Flat washers M3: 120 pcs (~50g)
- Lock washers M3: 60 pcs (~30g)

#### M4 Fasteners (~375g, 25%)
- Socket head cap screws M4x10: 40 pcs (~85g)
- Socket head cap screws M4x16: 40 pcs (~100g)
- Hex nuts M4: 100 pcs (~90g)
- Flat washers M4: 100 pcs (~60g)
- Lock washers M4: 50 pcs (~40g)

#### M5 Fasteners (~375g, 25%)
- Hex bolts M5x12: 30 pcs (~90g)
- Hex bolts M5x20: 30 pcs (~120g)
- Hex nuts M5: 80 pcs (~90g)
- Flat washers M5: 80 pcs (~50g)
- Lock washers M5: 40 pcs (~25g)

#### M6 Fasteners (~300g, 20%)
- Hex bolts M6x16: 20 pcs (~90g)
- Hex bolts M6x25: 20 pcs (~120g)
- Hex nuts M6: 50 pcs (~60g)
- Flat washers M6: 50 pcs (~25g)
- Lock washers M6: 20 pcs (~5g)

#### M8 Fasteners (~150g, 10%)
- Hex bolts M8x20: 10 pcs (~70g)
- Hex bolts M8x30: 8 pcs (~65g)
- Hex nuts M8: 20 pcs (~10g)
- Flat washers M8: 20 pcs (~5g)

**Total Mass**: ~1500g (1.5 kg)
**Total Pieces**: ~1,218 fasteners

---

## Fastener Kit Medium (1.0 kg)
**Target Applications**: General machinery, structural assemblies, equipment frames
**Size Range**: M6 to M12

### Contents Breakdown:

#### M6 Fasteners (~200g, 20%)
- Hex bolts M6x20: 20 pcs (~100g)
- Hex nuts M6: 50 pcs (~60g)
- Flat washers M6: 50 pcs (~25g)
- Lock washers M6: 25 pcs (~15g)

#### M8 Fasteners (~300g, 30%)
- Hex bolts M8x25: 15 pcs (~105g)
- Hex bolts M8x40: 12 pcs (~115g)
- Hex nuts M8: 40 pcs (~50g)
- Flat washers M8: 40 pcs (~20g)
- Lock washers M8: 20 pcs (~10g)

#### M10 Fasteners (~300g, 30%)
- Hex bolts M10x30: 10 pcs (~115g)
- Hex bolts M10x50: 8 pcs (~115g)
- Hex nuts M10: 30 pcs (~45g)
- Flat washers M10: 30 pcs (~20g)
- Lock washers M10: 15 pcs (~5g)

#### M12 Fasteners (~200g, 20%)
- Hex bolts M12x40: 6 pcs (~105g)
- Hex bolts M12x60: 5 pcs (~100g)
- Hex nuts M12: 15 pcs (~25g)
- Flat washers M12: 15 pcs (~10g)

**Total Mass**: ~1000g (1.0 kg)
**Total Pieces**: ~366 fasteners

---

## Fastener Kit Large (2.0 kg)
**Target Applications**: Heavy machinery, large structural assemblies, pressure vessels
**Size Range**: M10 to M20

### Contents Breakdown:

#### M10 Fasteners (~400g, 20%)
- Hex bolts M10x40: 12 pcs (~140g)
- Hex bolts M10x60: 10 pcs (~145g)
- Hex nuts M10: 40 pcs (~60g)
- Flat washers M10: 40 pcs (~30g)
- Lock washers M10: 20 pcs (~25g)

#### M12 Fasteners (~600g, 30%)
- Hex bolts M12x50: 10 pcs (~175g)
- Hex bolts M12x80: 8 pcs (~180g)
- Hex nuts M12: 30 pcs (~90g)
- Flat washers M12: 30 pcs (~90g)
- Lock washers M12: 20 pcs (~65g)

#### M16 Fasteners (~600g, 30%)
- Hex bolts M16x60: 6 pcs (~180g)
- Hex bolts M16x100: 5 pcs (~190g)
- Hex nuts M16: 15 pcs (~120g)
- Flat washers M16: 15 pcs (~60g)
- Lock washers M16: 10 pcs (~50g)

#### M20 Fasteners (~400g, 20%)
- Hex bolts M20x80: 3 pcs (~180g)
- Hex bolts M20x120: 3 pcs (~210g)
- Hex nuts M20: 8 pcs (~10g)
- Flat washers M20: 8 pcs (~0g)

**Total Mass**: ~2000g (2.0 kg)
**Total Pieces**: ~253 fasteners

---

## Individual Fastener Components

To produce these kits, we need item definitions for:

### Bolts/Screws (by size and length)
- hex_bolt_{size}x{length} (e.g., hex_bolt_m6x20)
- socket_cap_screw_{size}x{length} (e.g., socket_cap_screw_m4x10)

### Nuts (by size)
- hex_nut_{size} (e.g., hex_nut_m6)

### Washers (by size and type)
- flat_washer_{size} (e.g., flat_washer_m6)
- lock_washer_{size} (e.g., lock_washer_m6)

## Production Processes Required

1. **Cold heading** - Form bolt heads and nut blanks
2. **Thread rolling** - Create threads (stronger than cutting)
3. **Stamping/punching** - Create washers from sheet stock
4. **Heat treatment** - Optional hardening for high-strength applications
5. **Sorting and kitting** - Assemble mixed kits from individual components

## Material Requirements

- **Steel wire/rod stock** - For bolts and nuts (cold heading)
- **Steel sheet stock** - For washers (punching)
- **Total steel per kit**:
  - Small: 1.5 kg input → 1.5 kg output (minimal scrap)
  - Medium: 1.0 kg input → 1.0 kg output
  - Large: 2.0 kg input → 2.0 kg output

## Quality Standards

- **Thread tolerance**: ISO 6g for bolts, 6H for nuts (normal tolerance)
- **Surface finish**: Mill finish acceptable, can upgrade to zinc plating
- **Strength class**: Grade 4.8 minimum (400 MPa tensile, 8% ductility)
- **Hardness**: HRB 70-95 typical for carbon steel fasteners

## Notes

- This specification uses simplified item IDs. Full implementation may use shortened naming.
- Quantities are approximate and can be adjusted based on manufacturing constraints.
- Lock washers can be substituted with additional flat washers if spring wire unavailable.
- Thread rolling is preferred over thread cutting for superior strength and surface finish.
