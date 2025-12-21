"""Tests for ubuntu20_04_cfn_hup example."""

import pytest

from ubuntu20_04_cfn_hup.main import build_template


class TestUbuntu2004CfnHup:
    """Test ubuntu20_04_cfn_hup example."""

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
        assert len(output["Resources"]) == 2
