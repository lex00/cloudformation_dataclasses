"""Tests for rds_mysql_with_read_replica example."""

import pytest

from rds_mysql_with_read_replica.main import build_template


class TestRdsMysqlWithReadReplica:
    """Test rds_mysql_with_read_replica example."""

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
        assert len(output["Resources"]) == 4
