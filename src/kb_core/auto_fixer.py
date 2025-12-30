"""
Auto-Fixer for Validation Issues

Implements automatic fixes for common validation errors that can be
safely resolved without domain knowledge.

Fixable rules:
- process_type_required: Infer from time_model type
- deprecated_field: Migrate old fields to new schema
- setup_hr_in_continuous: Remove setup_hr from continuous processes
- target_item_id_required: Infer from recipe filename

Rules requiring manual intervention are logged but not auto-fixed.
"""
from __future__ import annotations

import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass

from .validators import ValidationIssue, ValidationLevel


@dataclass
class FixResult:
    """Result of applying an auto-fix."""
    success: bool
    message: str
    changes_made: List[str]


class AutoFixer:
    """
    Automatically fix common validation issues in KB files.

    Usage:
        fixer = AutoFixer(kb_root=Path("kb"))
        result = fixer.fix_issue(validation_issue)
        if result.success:
            print(f"Fixed: {result.message}")
    """

    def __init__(self, kb_root: Path, dry_run: bool = False):
        """
        Initialize auto-fixer.

        Args:
            kb_root: Path to KB root directory
            dry_run: If True, don't write changes to disk
        """
        self.kb_root = kb_root
        self.dry_run = dry_run
        self.fixes_applied = 0
        self.fixes_skipped = 0

    def fix_issue(self, issue: ValidationIssue, file_path: Optional[Path] = None) -> FixResult:
        """
        Attempt to auto-fix a validation issue.

        Args:
            issue: ValidationIssue to fix
            file_path: Optional explicit file path (if not in issue context)

        Returns:
            FixResult with success status and details
        """
        # Get file path
        if file_path is None:
            file_path = self._get_file_path(issue)

        if file_path is None or not file_path.exists():
            return FixResult(
                success=False,
                message=f"File not found for {issue.entity_type} '{issue.entity_id}'",
                changes_made=[]
            )

        # Dispatch to appropriate fix method
        fix_method = self._get_fix_method(issue.rule)

        if fix_method is None:
            self.fixes_skipped += 1
            return FixResult(
                success=False,
                message=f"Rule '{issue.rule}' requires manual intervention",
                changes_made=[]
            )

        # Load YAML file
        try:
            with file_path.open('r', encoding='utf-8') as f:
                data = yaml.safe_load(f)

            if not isinstance(data, dict):
                return FixResult(
                    success=False,
                    message=f"Invalid YAML structure in {file_path}",
                    changes_made=[]
                )
        except Exception as e:
            return FixResult(
                success=False,
                message=f"Failed to load {file_path}: {e}",
                changes_made=[]
            )

        # Apply fix
        result = fix_method(data, issue, file_path)

        # Write back if successful and not dry_run
        if result.success and not self.dry_run:
            try:
                self._write_yaml(file_path, data)
                self.fixes_applied += 1
            except Exception as e:
                return FixResult(
                    success=False,
                    message=f"Failed to write {file_path}: {e}",
                    changes_made=result.changes_made
                )

        if result.success and self.dry_run:
            result.message += " (dry-run, not written)"

        return result

    def _get_fix_method(self, rule: str):
        """Get the appropriate fix method for a validation rule."""
        fix_methods = {
            'process_type_required': self._fix_process_type_required,
            'deprecated_field': self._fix_deprecated_field,
            'setup_hr_in_continuous': self._fix_setup_hr_in_continuous,
            'target_item_id_required': self._fix_target_item_id_required,
        }
        return fix_methods.get(rule)

    def _get_file_path(self, issue: ValidationIssue) -> Optional[Path]:
        """Determine file path from validation issue."""
        # Try to get from entries (if available)
        # For now, infer from entity_type and entity_id
        entity_type = issue.entity_type
        entity_id = issue.entity_id

        if entity_type == 'process':
            return self.kb_root / 'processes' / f'{entity_id}.yaml'
        elif entity_type == 'recipe':
            return self.kb_root / 'recipes' / f'{entity_id}.yaml'
        elif entity_type in ('material', 'part', 'machine'):
            # Try multiple locations
            for subdir in ['materials', 'parts', 'machines']:
                path = self.kb_root / 'items' / subdir / f'{entity_id}.yaml'
                if path.exists():
                    return path
            # Try imports
            for path in (self.kb_root / 'imports').rglob(f'{entity_id}.yaml'):
                return path

        return None

    # =========================================================================
    # Fix Methods
    # =========================================================================

    def _fix_process_type_required(
        self,
        data: dict,
        issue: ValidationIssue,
        file_path: Path
    ) -> FixResult:
        """
        Fix: Missing process_type
        Strategy: Infer from time_model type
        - linear_rate -> continuous
        - batch -> batch
        """
        time_model = data.get('time_model')

        if not time_model or not isinstance(time_model, dict):
            return FixResult(
                success=False,
                message="Cannot infer process_type: no time_model found",
                changes_made=[]
            )

        time_model_type = time_model.get('type')

        if time_model_type == 'linear_rate':
            data['process_type'] = 'continuous'
            inferred_type = 'continuous'
        elif time_model_type == 'batch':
            data['process_type'] = 'batch'
            inferred_type = 'batch'
        else:
            return FixResult(
                success=False,
                message=f"Cannot infer process_type from time_model.type '{time_model_type}'",
                changes_made=[]
            )

        return FixResult(
            success=True,
            message=f"Added process_type: {inferred_type} (inferred from time_model)",
            changes_made=[f"process_type: {inferred_type}"]
        )

    def _fix_deprecated_field(
        self,
        data: dict,
        issue: ValidationIssue,
        file_path: Path
    ) -> FixResult:
        """
        Fix: Deprecated field usage
        Strategy: Migrate to new schema

        Common migrations:
        - rate_kg_per_hr -> rate + rate_unit: "kg/hr"
        - setup_time_hr -> setup_hr (time_model)
        """
        changes = []

        # Handle rate_kg_per_hr -> rate + rate_unit
        time_model = data.get('time_model')
        if time_model and isinstance(time_model, dict):
            if 'rate_kg_per_hr' in time_model:
                rate_value = time_model.pop('rate_kg_per_hr')
                time_model['rate'] = rate_value
                time_model['rate_unit'] = 'kg/hr'
                changes.append(f"Migrated rate_kg_per_hr -> rate + rate_unit")

        # Handle other deprecated fields as needed
        # (Add more migration patterns here as they're discovered)

        if not changes:
            return FixResult(
                success=False,
                message="No deprecated field migration implemented for this case",
                changes_made=[]
            )

        return FixResult(
            success=True,
            message=f"Migrated deprecated field(s): {', '.join(changes)}",
            changes_made=changes
        )

    def _fix_setup_hr_in_continuous(
        self,
        data: dict,
        issue: ValidationIssue,
        file_path: Path
    ) -> FixResult:
        """
        Fix: setup_hr in continuous process
        Strategy: Remove setup_hr (only valid for batch)
        """
        time_model = data.get('time_model')

        if not time_model or not isinstance(time_model, dict):
            return FixResult(
                success=False,
                message="No time_model found",
                changes_made=[]
            )

        if 'setup_hr' not in time_model:
            return FixResult(
                success=False,
                message="No setup_hr field found to remove",
                changes_made=[]
            )

        setup_hr_value = time_model.pop('setup_hr')

        return FixResult(
            success=True,
            message=f"Removed setup_hr ({setup_hr_value}) from continuous process",
            changes_made=[f"Removed setup_hr: {setup_hr_value}"]
        )

    def _fix_target_item_id_required(
        self,
        data: dict,
        issue: ValidationIssue,
        file_path: Path
    ) -> FixResult:
        """
        Fix: Missing target_item_id in recipe
        Strategy: Infer from recipe filename

        Common patterns:
        - recipe_motor_v0.yaml -> motor
        - recipe_steel_ingot_v1.yaml -> steel_ingot
        """
        # Try to infer from filename
        filename = file_path.stem  # e.g., "recipe_motor_v0"

        # Remove "recipe_" prefix if present
        if filename.startswith('recipe_'):
            target_id = filename[7:]  # Remove "recipe_"
        else:
            target_id = filename

        # Remove version suffix if present (e.g., "_v0", "_v1")
        import re
        target_id = re.sub(r'_v\d+$', '', target_id)

        if not target_id or target_id == filename:
            return FixResult(
                success=False,
                message=f"Cannot infer target_item_id from filename '{filename}'",
                changes_made=[]
            )

        data['target_item_id'] = target_id

        return FixResult(
            success=True,
            message=f"Added target_item_id: {target_id} (inferred from filename)",
            changes_made=[f"target_item_id: {target_id}"]
        )

    # =========================================================================
    # Helper Methods
    # =========================================================================

    def _write_yaml(self, file_path: Path, data: dict) -> None:
        """
        Write YAML data to file with proper formatting.

        Preserves comments and formatting as much as possible.
        """
        with file_path.open('w', encoding='utf-8') as f:
            yaml.safe_dump(
                data,
                f,
                default_flow_style=False,
                sort_keys=False,
                allow_unicode=True,
                width=120
            )

    def get_summary(self) -> str:
        """Get summary of fixes applied."""
        return f"Auto-fix summary: {self.fixes_applied} fixes applied, {self.fixes_skipped} skipped"


def batch_fix_issues(
    issues: List[ValidationIssue],
    kb_root: Path,
    dry_run: bool = False,
    max_fixes: Optional[int] = None
) -> Tuple[List[FixResult], List[FixResult]]:
    """
    Batch fix multiple validation issues.

    Args:
        issues: List of ValidationIssue objects to fix
        kb_root: Path to KB root directory
        dry_run: If True, don't write changes to disk
        max_fixes: Optional maximum number of fixes to apply

    Returns:
        Tuple of (successful_fixes, failed_fixes)
    """
    fixer = AutoFixer(kb_root, dry_run=dry_run)

    successful = []
    failed = []

    for i, issue in enumerate(issues):
        if max_fixes and i >= max_fixes:
            break

        result = fixer.fix_issue(issue)

        if result.success:
            successful.append(result)
        else:
            failed.append(result)

    return successful, failed
