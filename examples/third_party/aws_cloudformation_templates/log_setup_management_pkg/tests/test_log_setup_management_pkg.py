"""Tests for log_setup_management_pkg example."""

import pytest

from log_setup_management_pkg.main import build_template


class TestLogSetupManagementPkg:
    """Test log_setup_management_pkg example."""

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
        assert len(output["Resources"]) == 10
