"""
Tests for indexer validation (Issue #13).

Tests that the indexer correctly validates items for missing mass fields.
"""
import pytest

from src.indexer.indexer import _collect_nulls


class TestMassValidation:
    """Tests for mass field validation in indexer."""

    def test_collect_nulls_material_with_mass(self):
        """Materials with mass should not be flagged."""
        data = {
            "id": "test_material",
            "kind": "material",
            "mass": 50.0,
            "unit": "kg"
        }

        nulls = _collect_nulls("material", data)

        assert len(nulls) == 0, "Material with mass should not be flagged"

    def test_collect_nulls_material_without_mass(self):
        """Materials without mass should be flagged."""
        data = {
            "id": "test_material_no_mass",
            "kind": "material",
            "unit": "kg"
        }

        nulls = _collect_nulls("material", data)

        assert len(nulls) == 1, "Material without mass should be flagged"
        assert nulls[0]["field"] == "mass"

    def test_collect_nulls_software_without_mass(self):
        """Software materials should not require mass."""
        data = {
            "id": "test_software",
            "kind": "material",
            "material_class": "software",
            "unit": "unit"
        }

        nulls = _collect_nulls("material", data)

        assert len(nulls) == 0, "Software items should not require mass"

    def test_collect_nulls_abstract_without_mass(self):
        """Abstract materials should not require mass."""
        data = {
            "id": "test_abstract",
            "kind": "material",
            "material_class": "abstract",
            "unit": "unit"
        }

        nulls = _collect_nulls("material", data)

        assert len(nulls) == 0, "Abstract items should not require mass"

    def test_collect_nulls_information_without_mass(self):
        """Information materials should not require mass."""
        data = {
            "id": "test_information",
            "kind": "material",
            "material_class": "information",
            "unit": "unit"
        }

        nulls = _collect_nulls("material", data)

        assert len(nulls) == 0, "Information items should not require mass"

    def test_collect_nulls_part_without_mass(self):
        """Parts without mass should be flagged."""
        data = {
            "id": "test_part_no_mass",
            "kind": "part",
            "unit": "unit"
        }

        nulls = _collect_nulls("part", data)

        assert len(nulls) == 1, "Part without mass should be flagged"
        assert nulls[0]["field"] == "mass"

    def test_collect_nulls_machine_without_mass(self):
        """Machines without mass should be flagged."""
        data = {
            "id": "test_machine_no_mass",
            "kind": "machine",
            "unit": "unit"
        }

        nulls = _collect_nulls("machine", data)

        assert len(nulls) == 1, "Machine without mass should be flagged"
        assert nulls[0]["field"] == "mass"

    def test_collect_nulls_part_with_mass(self):
        """Parts with mass should not be flagged."""
        data = {
            "id": "test_part",
            "kind": "part",
            "mass": 10.0,
            "unit": "unit"
        }

        nulls = _collect_nulls("part", data)

        assert len(nulls) == 0, "Part with mass should not be flagged"

    def test_collect_nulls_machine_with_mass(self):
        """Machines with mass should not be flagged."""
        data = {
            "id": "test_machine",
            "kind": "machine",
            "mass": 100.0,
            "unit": "unit"
        }

        nulls = _collect_nulls("machine", data)

        assert len(nulls) == 0, "Machine with mass should not be flagged"
