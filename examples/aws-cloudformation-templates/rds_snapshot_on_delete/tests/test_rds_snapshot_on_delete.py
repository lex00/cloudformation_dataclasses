"""Tests for rds_snapshot_on_delete example."""

import pytest

from rds_snapshot_on_delete.main import build_template


class TestRdsSnapshotOnDelete:
    """Test rds_snapshot_on_delete example."""

    @pytest.fixture
    def template(self):
        """Build template."""
        return build_template()

    def test_validates(self, template):
        """Template should pass validation."""
        errors = template.validate()
        assert errors == [], f"Validation errors: {errors}"

    def test_resource_count(self, template):
        """Verify expected number of resources."""
        output = template.to_dict()
        assert len(output["Resources"]) == 1
