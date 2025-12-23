"""Tests for cfn_endpoint_creationpolicy_no_igw example."""

import pytest

from cfn_endpoint_creationpolicy_no_igw.main import build_template


class TestCfnEndpointCreationpolicyNoIgw:
    """Test cfn_endpoint_creationpolicy_no_igw example."""

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
        assert len(output["Resources"]) == 11
