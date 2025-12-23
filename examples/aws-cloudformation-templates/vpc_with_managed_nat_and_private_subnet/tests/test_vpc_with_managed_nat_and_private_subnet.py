"""Tests for vpc_with_managed_nat_and_private_subnet example."""

import pytest

from vpc_with_managed_nat_and_private_subnet.main import build_template


class TestVpcWithManagedNatAndPrivateSubnet:
    """Test vpc_with_managed_nat_and_private_subnet example."""

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
        assert len(output["Resources"]) == 26
