"""Tests for elb_access_logs_and_connection_draining example."""

import pytest

from elb_access_logs_and_connection_draining.main import build_template


class TestElbAccessLogsAndConnectionDraining:
    """Test elb_access_logs_and_connection_draining example."""

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
        assert len(output["Resources"]) == 6
