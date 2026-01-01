"""
Tests for auto_fixer.py

Tests automatic fixing of validation issues.
"""
import pytest
import yaml
from pathlib import Path
from tempfile import TemporaryDirectory

from src.kb_core.auto_fixer import AutoFixer, FixResult, batch_fix_issues
from src.kb_core.validators import ValidationIssue, ValidationLevel


@pytest.fixture
def temp_kb():
    """Create temporary KB directory structure."""
    with TemporaryDirectory() as tmpdir:
        kb_root = Path(tmpdir) / "kb"
        kb_root.mkdir()

        # Create subdirectories
        (kb_root / "processes").mkdir()
        (kb_root / "recipes").mkdir()
        (kb_root / "items" / "materials").mkdir(parents=True)
        (kb_root / "items" / "parts").mkdir(parents=True)
        (kb_root / "items" / "machines").mkdir(parents=True)

        yield kb_root


@pytest.fixture
def fixer(temp_kb):
    """Create AutoFixer instance with temp KB."""
    return AutoFixer(kb_root=temp_kb, dry_run=False)


@pytest.fixture
def dry_run_fixer(temp_kb):
    """Create AutoFixer instance in dry-run mode."""
    return AutoFixer(kb_root=temp_kb, dry_run=True)


class TestProcessTypeRequired:
    """Test auto-fixing missing process_type."""

    def test_infer_continuous_from_linear_rate(self, fixer, temp_kb):
        """Should infer process_type: continuous from linear_rate time_model."""
        # Create test file
        process_file = temp_kb / "processes" / "test_process.yaml"
        data = {
            "id": "test_process",
            "time_model": {"type": "linear_rate", "rate": 100.0, "rate_unit": "kg/hr"},
        }
        with process_file.open('w') as f:
            yaml.safe_dump(data, f)

        # Create validation issue
        issue = ValidationIssue(
            level=ValidationLevel.ERROR,
            category="schema",
            rule="process_type_required",
            entity_type="process",
            entity_id="test_process",
            message="Missing process_type"
        )

        # Apply fix
        result = fixer.fix_issue(issue, process_file)

        # Verify
        assert result.success
        assert "continuous" in result.message
        assert "process_type: continuous" in result.changes_made

        # Check file was updated
        with process_file.open('r') as f:
            updated_data = yaml.safe_load(f)
        assert updated_data['process_type'] == 'continuous'

    def test_infer_batch_from_batch_time_model(self, fixer, temp_kb):
        """Should infer process_type: batch from batch time_model."""
        process_file = temp_kb / "processes" / "test_batch.yaml"
        data = {
            "id": "test_batch",
            "time_model": {"type": "batch", "hr_per_batch": 2.0},
        }
        with process_file.open('w') as f:
            yaml.safe_dump(data, f)

        issue = ValidationIssue(
            level=ValidationLevel.ERROR,
            category="schema",
            rule="process_type_required",
            entity_type="process",
            entity_id="test_batch",
            message="Missing process_type"
        )

        result = fixer.fix_issue(issue, process_file)

        assert result.success
        assert "batch" in result.message

        with process_file.open('r') as f:
            updated_data = yaml.safe_load(f)
        assert updated_data['process_type'] == 'batch'

    def test_cannot_infer_without_time_model(self, fixer, temp_kb):
        """Should fail if no time_model present."""
        process_file = temp_kb / "processes" / "no_time_model.yaml"
        data = {"id": "no_time_model"}
        with process_file.open('w') as f:
            yaml.safe_dump(data, f)

        issue = ValidationIssue(
            level=ValidationLevel.ERROR,
            category="schema",
            rule="process_type_required",
            entity_type="process",
            entity_id="no_time_model",
            message="Missing process_type"
        )

        result = fixer.fix_issue(issue, process_file)

        assert not result.success
        assert "no time_model" in result.message.lower()


class TestDeprecatedField:
    """Test auto-fixing deprecated field usage."""

    def test_migrate_rate_kg_per_hr(self, fixer, temp_kb):
        """Should migrate rate_kg_per_hr to rate + rate_unit."""
        process_file = temp_kb / "processes" / "old_process.yaml"
        data = {
            "id": "old_process",
            "process_type": "continuous",
            "time_model": {"type": "linear_rate", "rate_kg_per_hr": 50.0},
        }
        with process_file.open('w') as f:
            yaml.safe_dump(data, f)

        issue = ValidationIssue(
            level=ValidationLevel.ERROR,
            category="schema",
            rule="deprecated_field",
            entity_type="process",
            entity_id="old_process",
            message="Deprecated field 'rate_kg_per_hr'",
            field_path="time_model.rate_kg_per_hr"
        )

        result = fixer.fix_issue(issue, process_file)

        assert result.success
        assert "rate_kg_per_hr" in result.message

        with process_file.open('r') as f:
            updated_data = yaml.safe_load(f)
        assert 'rate_kg_per_hr' not in updated_data['time_model']
        assert updated_data['time_model']['rate'] == 50.0
        assert updated_data['time_model']['rate_unit'] == 'kg/hr'


class TestSetupHrInContinuous:
    """Test removing setup_hr from continuous processes."""

    def test_remove_setup_hr_from_continuous(self, fixer, temp_kb):
        """Should remove setup_hr from continuous process."""
        process_file = temp_kb / "processes" / "continuous_with_setup.yaml"
        data = {
            "id": "continuous_with_setup",
            "process_type": "continuous",
            "time_model": {
                "type": "linear_rate",
                "rate": 100.0,
                "rate_unit": "kg/hr",
                "setup_hr": 0.5
            },
        }
        with process_file.open('w') as f:
            yaml.safe_dump(data, f)

        issue = ValidationIssue(
            level=ValidationLevel.ERROR,
            category="semantic",
            rule="setup_hr_in_continuous",
            entity_type="process",
            entity_id="continuous_with_setup",
            message="Continuous process cannot have setup_hr"
        )

        result = fixer.fix_issue(issue, process_file)

        assert result.success
        assert "Removed setup_hr" in result.message

        with process_file.open('r') as f:
            updated_data = yaml.safe_load(f)
        assert 'setup_hr' not in updated_data['time_model']


class TestTargetItemIdRequired:
    """Test inferring target_item_id from filename."""

    def test_infer_from_recipe_prefix(self, fixer, temp_kb):
        """Should infer target_item_id from 'recipe_<item>_v0.yaml' pattern."""
        recipe_file = temp_kb / "recipes" / "recipe_motor_v0.yaml"
        data = {
            "id": "recipe_motor_v0",
            "steps": [{"process_id": "assemble"}]
        }
        with recipe_file.open('w') as f:
            yaml.safe_dump(data, f)

        issue = ValidationIssue(
            level=ValidationLevel.ERROR,
            category="schema",
            rule="target_item_id_required",
            entity_type="recipe",
            entity_id="recipe_motor_v0",
            message="Missing target_item_id"
        )

        result = fixer.fix_issue(issue, recipe_file)

        assert result.success
        assert "motor" in result.message

        with recipe_file.open('r') as f:
            updated_data = yaml.safe_load(f)
        assert updated_data['target_item_id'] == 'motor'

    def test_infer_with_underscores(self, fixer, temp_kb):
        """Should handle multi-word item names like steel_ingot."""
        recipe_file = temp_kb / "recipes" / "recipe_steel_ingot_v1.yaml"
        data = {
            "id": "recipe_steel_ingot_v1",
            "steps": [{"process_id": "smelt"}]
        }
        with recipe_file.open('w') as f:
            yaml.safe_dump(data, f)

        issue = ValidationIssue(
            level=ValidationLevel.ERROR,
            category="schema",
            rule="target_item_id_required",
            entity_type="recipe",
            entity_id="recipe_steel_ingot_v1",
            message="Missing target_item_id"
        )

        result = fixer.fix_issue(issue, recipe_file)

        assert result.success

        with recipe_file.open('r') as f:
            updated_data = yaml.safe_load(f)
        assert updated_data['target_item_id'] == 'steel_ingot'


class TestDryRun:
    """Test dry-run mode doesn't write changes."""

    def test_dry_run_no_write(self, dry_run_fixer, temp_kb):
        """Dry-run should not write changes to disk."""
        process_file = temp_kb / "processes" / "test_dry_run.yaml"
        original_data = {
            "id": "test_dry_run",
            "time_model": {"type": "batch", "hr_per_batch": 1.0},
        }
        with process_file.open('w') as f:
            yaml.safe_dump(original_data, f)

        issue = ValidationIssue(
            level=ValidationLevel.ERROR,
            category="schema",
            rule="process_type_required",
            entity_type="process",
            entity_id="test_dry_run",
            message="Missing process_type"
        )

        result = dry_run_fixer.fix_issue(issue, process_file)

        assert result.success
        assert "dry-run" in result.message

        # File should be unchanged
        with process_file.open('r') as f:
            current_data = yaml.safe_load(f)
        assert 'process_type' not in current_data


class TestUnfixableRules:
    """Test rules that cannot be auto-fixed."""

    def test_scaling_basis_not_found_unfixable(self, fixer, temp_kb):
        """Should not auto-fix scaling_basis_not_found (requires domain knowledge)."""
        process_file = temp_kb / "processes" / "missing_scaling.yaml"
        data = {
            "id": "missing_scaling",
            "process_type": "continuous",
            "time_model": {
                "type": "linear_rate",
                "rate": 100.0,
                "rate_unit": "kg/hr",
                "scaling_basis": "nonexistent_item"
            },
        }
        with process_file.open('w') as f:
            yaml.safe_dump(data, f)

        issue = ValidationIssue(
            level=ValidationLevel.ERROR,
            category="semantic",
            rule="scaling_basis_not_found",
            entity_type="process",
            entity_id="missing_scaling",
            message="scaling_basis 'nonexistent_item' not found"
        )

        result = fixer.fix_issue(issue, process_file)

        assert not result.success
        assert "manual intervention" in result.message


class TestBatchFix:
    """Test batch fixing multiple issues."""

    def test_batch_fix_multiple_issues(self, temp_kb):
        """Should fix multiple issues in batch."""
        # Create multiple files with issues
        process1 = temp_kb / "processes" / "process1.yaml"
        with process1.open('w') as f:
            yaml.safe_dump({
                "id": "process1",
                "time_model": {"type": "linear_rate", "rate": 50.0, "rate_unit": "kg/hr"}
            }, f)

        process2 = temp_kb / "processes" / "process2.yaml"
        with process2.open('w') as f:
            yaml.safe_dump({
                "id": "process2",
                "time_model": {"type": "batch", "hr_per_batch": 1.0}
            }, f)

        issues = [
            ValidationIssue(
                level=ValidationLevel.ERROR,
                category="schema",
                rule="process_type_required",
                entity_type="process",
                entity_id="process1",
                message="Missing process_type"
            ),
            ValidationIssue(
                level=ValidationLevel.ERROR,
                category="schema",
                rule="process_type_required",
                entity_type="process",
                entity_id="process2",
                message="Missing process_type"
            ),
        ]

        successful, failed = batch_fix_issues(issues, temp_kb, dry_run=False)

        assert len(successful) == 2
        assert len(failed) == 0

        # Verify both files were updated
        with process1.open('r') as f:
            data1 = yaml.safe_load(f)
        assert data1['process_type'] == 'continuous'

        with process2.open('r') as f:
            data2 = yaml.safe_load(f)
        assert data2['process_type'] == 'batch'

    def test_batch_fix_with_max_fixes(self, temp_kb):
        """Should respect max_fixes parameter."""
        process1 = temp_kb / "processes" / "p1.yaml"
        with process1.open('w') as f:
            yaml.safe_dump({"id": "p1", "time_model": {"type": "batch", "hr_per_batch": 1.0}}, f)

        process2 = temp_kb / "processes" / "p2.yaml"
        with process2.open('w') as f:
            yaml.safe_dump({"id": "p2", "time_model": {"type": "batch", "hr_per_batch": 1.0}}, f)

        issues = [
            ValidationIssue(
                level=ValidationLevel.ERROR,
                category="schema",
                rule="process_type_required",
                entity_type="process",
                entity_id="p1",
                message="Missing process_type"
            ),
            ValidationIssue(
                level=ValidationLevel.ERROR,
                category="schema",
                rule="process_type_required",
                entity_type="process",
                entity_id="p2",
                message="Missing process_type"
            ),
        ]

        successful, failed = batch_fix_issues(issues, temp_kb, dry_run=False, max_fixes=1)

        # Should only fix first issue
        assert len(successful) == 1
        assert successful[0].changes_made == ["process_type: batch"]


class TestFileNotFound:
    """Test handling of missing files."""

    def test_file_not_found(self, fixer):
        """Should fail gracefully if file doesn't exist."""
        issue = ValidationIssue(
            level=ValidationLevel.ERROR,
            category="schema",
            rule="process_type_required",
            entity_type="process",
            entity_id="nonexistent",
            message="Missing process_type"
        )

        result = fixer.fix_issue(issue)

        assert not result.success
        assert "not found" in result.message.lower()


class TestGetSummary:
    """Test summary reporting."""

    def test_summary_counts_fixes(self, fixer, temp_kb):
        """Summary should track fixes applied and skipped."""
        # Create fixable issue
        process_file = temp_kb / "processes" / "fixable.yaml"
        with process_file.open('w') as f:
            yaml.safe_dump({
                "id": "fixable",
                "time_model": {"type": "batch", "hr_per_batch": 1.0}
            }, f)

        fixable_issue = ValidationIssue(
            level=ValidationLevel.ERROR,
            category="schema",
            rule="process_type_required",
            entity_type="process",
            entity_id="fixable",
            message="Missing process_type"
        )

        # Create unfixable issue
        unfixable_issue = ValidationIssue(
            level=ValidationLevel.ERROR,
            category="semantic",
            rule="scaling_basis_not_found",
            entity_type="process",
            entity_id="fixable",
            message="scaling_basis not found"
        )

        fixer.fix_issue(fixable_issue, process_file)
        fixer.fix_issue(unfixable_issue, process_file)

        summary = fixer.get_summary()
        assert "1 fixes applied" in summary
        assert "1 skipped" in summary
