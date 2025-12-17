# Proposal: Rich Metadata for Seed File Requirements

## Problem

Current seed files only support flat string lists with inline comments:

```yaml
requires_ids:
  - iron_powder_or_sheet                    # Fe from ilmenite reduction
  - nickel_compound_active_material          # Ni(OH)2 precursor
```

Workers receiving work queue items have minimal context about:
- What the item actually is
- Which paper/section it came from
- How critical it is to implement
- What design documents to reference
- Dependencies and complexity

## Proposed Solution

Support **rich requirement objects** alongside simple string IDs for backward compatibility:

```yaml
requires_ids:
  # Simple format (backward compatible)
  - simple_item_id

  # Rich format (new)
  - id: fresnel_lens_large_scale_v0
    description: "Large Fresnel lens for solar concentration"
    source_paper: "ellery-2022-metalysis"
    source_section: "Section 4.2, p.15-17"
    priority: essential  # essential | important | optimization
    category: solar_thermal
    estimated_complexity: high  # low | medium | high
    depends_on:
      - solar_tracking_mechanism_v0
      - glass_casting_process_v0
    design_doc: "design/solar_thermionics_report.md"
    notes: "Energy efficiency: 97% thermal / 3% electrical split"
```

## Schema Definition

### RequirementMetadata Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | Item identifier (same as current string format) |
| `description` | string | No | Human-readable description of the item |
| `source_paper` | string | No | Paper filename(s) where technology identified |
| `source_section` | string | No | Section/page numbers in paper |
| `priority` | enum | No | `essential` \| `important` \| `optimization` |
| `category` | string | No | Technology category (e.g., `solar_thermal`, `electronics`) |
| `estimated_complexity` | enum | No | `low` \| `medium` \| `high` |
| `depends_on` | list[string] | No | IDs of prerequisite items |
| `design_doc` | string | No | Path to design document with specs |
| `notes` | string | No | Additional context, parameters, constraints |

## Implementation Changes

### 1. Update `kbtool/models.py`

Add a new model for rich requirements:

```python
class SeedRequirement(_BaseModel):
    """Rich requirement metadata for seed files."""
    id: str  # The item ID
    description: Optional[str] = None
    source_paper: Optional[str] = None
    source_section: Optional[str] = None
    priority: Optional[str] = None  # essential, important, optimization
    category: Optional[str] = None
    estimated_complexity: Optional[str] = None  # low, medium, high
    depends_on: List[str] = Field(default_factory=list)
    design_doc: Optional[str] = None
    notes: Optional[str] = None
```

### 2. Update `kbtool/indexer.py`

Modify `_collect_refs` to handle both string and object formats:

```python
def _collect_refs(kind: str, data: dict) -> Tuple[Set[str], List[dict], List[dict]]:
    # ... existing code ...

    if kind in ("process", "seed"):
        # ... existing inputs/outputs handling ...

        # Enhanced requires_ids handling
        for req in data.get("requires_ids", []) or []:
            if isinstance(req, str):
                # Simple string format (backward compatible)
                refs.add(str(req))
            elif isinstance(req, dict):
                # Rich object format (new)
                item_id = req.get("id")
                if item_id:
                    refs.add(str(item_id))
                    # Store metadata for work queue enrichment
                    # (implementation details TBD)
```

### 3. Update Work Queue Format

Enrich work queue items with metadata from seed requirements:

```json
{
  "id": "fresnel_lens_large_scale_v0",
  "issue": "referenced_only",
  "context": {
    "seed_files": ["paper_reviews_dec2024_comprehensive_v0"],
    "metadata": {
      "description": "Large Fresnel lens for solar concentration",
      "source_paper": "ellery-2022-metalysis",
      "source_section": "Section 4.2, p.15-17",
      "priority": "essential",
      "category": "solar_thermal",
      "estimated_complexity": "high",
      "depends_on": ["solar_tracking_mechanism_v0", "glass_casting_process_v0"],
      "design_doc": "design/solar_thermionics_report.md",
      "notes": "Energy efficiency: 97% thermal / 3% electrical split"
    }
  }
}
```

### 4. Queue Tool Display Enhancement

Update `kbtool/queue_tool.py` to display rich metadata when showing work items:

```
════════════════════════════════════════════════════════════════════════════
LEASED: fresnel_lens_large_scale_v0
════════════════════════════════════════════════════════════════════════════
Issue: referenced_only
Priority: essential
Category: solar_thermal
Complexity: high

Description:
  Large Fresnel lens for solar concentration

Source:
  Paper: ellery-2022-metalysis
  Section: Section 4.2, p.15-17
  Design doc: design/solar_thermionics_report.md

Dependencies:
  - solar_tracking_mechanism_v0
  - glass_casting_process_v0

Notes:
  Energy efficiency: 97% thermal / 3% electrical split
════════════════════════════════════════════════════════════════════════════
```

## Benefits

1. **Better Context**: Workers immediately understand what they're implementing
2. **Traceability**: Direct links to source papers and design docs
3. **Prioritization**: Clear indication of essential vs. nice-to-have items
4. **Dependency Awareness**: Workers know what must exist first
5. **Complexity Estimation**: Helps with task planning and allocation
6. **Backward Compatible**: Existing seed files with simple strings still work

## Migration Path

1. **Phase 1**: Implement code changes with backward compatibility
2. **Phase 2**: Enhance one seed file (e.g., thermionic system) as proof of concept
3. **Phase 3**: Gradually enrich existing seed files with metadata
4. **Phase 4**: Create new seed files using rich format by default

## Example: Enhanced Seed File

```yaml
id: paper_reviews_dec2024_comprehensive_v0
kind: seed
name: "Comprehensive Missing Technologies from 23 Paper Reviews"

requires_ids:
  # Solar Thermal Systems
  - id: fresnel_lens_large_scale_v0
    description: "Large Fresnel lens for solar concentration, C~10,000, 2700°C"
    source_paper: "ellery-2022-metalysis"
    source_section: "Section 4.2, Table 3"
    priority: essential
    category: solar_thermal
    estimated_complexity: high
    depends_on:
      - glass_casting_process_v0
      - precision_grinding_system_v0
    design_doc: "design/solar_thermionics_report.md"
    notes: "Critical for both power generation and high-temp processing. Concentration ratio determines max achievable temperature."

  - id: parabolic_mirror_dish_v0
    description: "Parabolic mirror dish, 90% reflectivity, 1600°C focus"
    source_paper: "ellery-2022-metalysis"
    source_section: "Section 4.2, Figure 5"
    priority: important
    category: solar_thermal
    estimated_complexity: medium
    depends_on:
      - nickel_sheet_rolling_v0
      - mirror_polishing_v0
    design_doc: "design/solar_thermionics_report.md"
    notes: "Alternative to Fresnel lens. Lower concentration but simpler manufacturing."

  # FFC Process
  - id: ffc_reactor_enhanced_v0
    description: "Enhanced FFC reactor with molten CaCl₂ at 900°C"
    source_paper: "ellery-2022-metalysis, Sustainable-ISRU"
    source_section: "ellery-2022, Section 3; Sustainable-ISRU, Section 5.2"
    priority: essential
    category: metal_extraction
    estimated_complexity: high
    depends_on:
      - molten_salt_containment_v0
      - graphite_anode_assembly_v0
      - temperature_control_system_v0
    design_doc: "design/ffc_metalysis_system.md"
    notes: "Core technology for lunar metal extraction. 97% thermal / 3% electrical energy split optimizes for solar thermal."

  # Vacuum Tube Electronics
  - id: tungsten_cathode_oxide_coated_v0
    description: "Tungsten cathode with oxide coating (BaO/SrO/CaO)"
    source_paper: "photolithoautotroph, ISRU-neural-computing"
    source_section: "photolithoautotroph, Section 7.3; ISRU-neural, Section 4.1"
    priority: essential
    category: electronics
    estimated_complexity: medium
    depends_on:
      - tungsten_wire_drawing_v0
      - cathode_oxide_coating_process_v0
    design_doc: "design/vacuum_tube_electronics.md"
    notes: "Foundation for all vacuum tube electronics. Demonstrated in 2017 baseline."

  # Continue for all ~300 items...
```

## Open Questions

1. Should we validate priority/complexity enum values, or keep them freeform?
2. Should `depends_on` be enforced by indexer (i.e., create dependency edges)?
3. Should we support multiple source papers as a list, or keep as comma-separated string?
4. Should design_doc paths be validated to ensure they exist?
5. Should we add a `demonstrated` boolean flag for technologies with proven hardware?

## Next Steps

1. Review proposal with user
2. Implement code changes in `kbtool/`
3. Create enhanced version of one existing seed file as example
4. Update comprehensive seed file with rich metadata
5. Document worker workflow with enhanced queue items
