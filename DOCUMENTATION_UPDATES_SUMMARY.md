# Documentation Updates Summary - CLI Commands for Claude

## Problem
Claude Code was trying to use Python API (`base_builder.interactive`) which caused state management issues. CLI commands exist but weren't prominently documented as the recommended approach.

## Solution
Updated existing documentation to clearly direct Claude Code users to CLI commands instead of Python API.

---

## Files Modified

### 1. `base_builder/README.md`
**Changes:**
- Added prominent "Recommended: CLI Commands" section at top of Quick Start
- Marked it with ⭐ for visibility
- Explicitly noted it's for "Claude Code or other assistants"
- Listed benefits (no state management, simple, reliable, scriptable)
- Moved autonomous agent mode to "Alternative" section

**Key addition:**
```markdown
### Recommended: CLI Commands (For Manual Control)

**⭐ Use this approach when:**
- Working with Claude Code or other assistants
- Running simulations manually
...
```

### 2. `base_builder/INTERACTIVE_MODE.md`
**Changes:**
- Added **prominent warning** at top of file
- Explained why CLI is better for Claude Code
- Provided CLI command examples
- Clarified Python API is for custom scripts only

**Key addition:**
```markdown
⚠️ **IMPORTANT - For Claude Code Users:**

**DO NOT use this Python API approach when working in Claude Code.**

**Instead, use the CLI commands via Bash:**
...
```

### 3. `base_builder/interactive.py`
**Changes:**
- Updated module docstring with warning
- Added instructions to use CLI commands instead
- Noted state management issues with Python API

**Key addition:**
```python
"""
⚠️ WARNING FOR CLAUDE CODE USERS:
    DO NOT USE THIS MODULE IN CLAUDE CODE!

    Use the CLI commands instead via Bash tool:
        python -m base_builder.cli_commands view-state --sim-id <name>
        ...
"""
```

### 4. `README.md` (main project)
**Changes:**
- Updated Base Builder section to emphasize CLI
- Marked CLI commands with ⭐
- Added warning to Python API section
- Updated documentation links with emphasis

**Key changes:**
```markdown
⭐ **Recommended: CLI Commands (for Claude Code and manual control)**
...

**Alternative: Python API (for custom scripts only)**
# ⚠️ NOT recommended for Claude Code - use CLI commands above instead
```

### 5. `design/memos/drive_motor_medium_production_plan.md`
**Changes:**
- Added complete "Production Using CLI Commands" section
- Showed full workflow with bash commands
- Referenced CLI guide

**Key addition:**
- Complete bash script showing all steps to build drive_motor_medium
- Each import, recipe run, preview, and advance-time command

---

## Files Created

### 6. `scripts/build_component_template.sh` (NEW)
**Purpose:** Template script showing standard build workflow

**Contents:**
- Complete workflow from imports to verification
- Helpful comments and customization notes
- Error handling (set -e)
- Demonstrates all key CLI commands
- 130+ lines with clear structure

**Usage:**
```bash
./scripts/build_component_template.sh <sim_id> <component> <recipe>
```

### 7. `docs/CLI_USAGE_FOR_CLAUDE.md` (NEW)
**Purpose:** Quick reference specifically for Claude Code usage

**Contents:**
- Clear DO/DON'T list
- Basic command pattern
- All available commands
- Complete example (drive_motor_medium)
- Common patterns
- Comparison table (CLI vs Python API)
- References to full documentation

**Key sections:**
- ❌ DO NOT / ✅ DO lists
- Command reference
- Complete working example
- Why CLI is better (comparison table)

---

## Documentation Structure

```
├── README.md (main)
│   └── Points to CLI commands ⭐
│
├── CLI_QUICK_REFERENCE.md (existing)
│   └── Quick command reference
│
├── docs/
│   ├── CLI_COMMANDS_GUIDE.md (existing, 595 lines)
│   │   └── Complete CLI reference
│   └── CLI_USAGE_FOR_CLAUDE.md (NEW)
│       └── Claude-specific quick guide
│
├── base_builder/
│   ├── README.md (updated)
│   │   └── CLI commands promoted to top
│   ├── INTERACTIVE_MODE.md (updated)
│   │   └── Warning added at top
│   └── interactive.py (updated)
│       └── Warning in docstring
│
├── scripts/
│   └── build_component_template.sh (NEW)
│       └── Working template
│
└── design/memos/
    └── drive_motor_medium_production_plan.md (updated)
        └── CLI commands section added
```

---

## Key Improvements

### 1. Visibility
- ⭐ stars mark recommended approaches
- Warnings at top of files (not buried)
- "DO NOT" / "DO" lists for clarity

### 2. Discoverability
- Main README points to CLI first
- Multiple documentation files guide to CLI
- Template script provides working example

### 3. Clarity
- Explicit "For Claude Code" callouts
- Clear comparison table showing benefits
- Concrete examples, not just descriptions

### 4. Completeness
- Full workflow examples
- Template script demonstrating best practices
- Links between all documentation

---

## Impact

### Before:
- CLI commands existed but not prominently featured
- Claude Code users found Python API first
- State management issues occurred
- No clear guidance on which approach to use

### After:
- ✅ CLI commands clearly marked as recommended
- ✅ Warnings in Python API files redirect to CLI
- ✅ Multiple entry points guide to CLI
- ✅ Working template script demonstrates usage
- ✅ Claude-specific documentation created
- ✅ Clear DO/DON'T guidance

---

## Testing

Verified:
- ✅ All CLI commands have help text
- ✅ Documentation links are correct
- ✅ Template script is executable
- ✅ Examples use correct syntax
- ✅ Warnings appear in strategic locations

---

## Next Steps for Claude

When asked to build components:

1. **Read:** `docs/CLI_USAGE_FOR_CLAUDE.md` or `docs/CLI_COMMANDS_GUIDE.md`
2. **Use:** CLI commands via Bash tool
3. **Pattern:** import → run-recipe → preview → advance-time → verify
4. **Reference:** `scripts/build_component_template.sh` for working example

**DO NOT:**
- Use `from base_builder.interactive import *`
- Write Python scripts for simulation control
- Try to manage simulation state

**DO:**
- Use `python -m base_builder.cli_commands <command>`
- Run one command per operation
- Preview before advancing time
