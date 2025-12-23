"""Tests for vpc_ec2_instance_with_multiple_static_ipaddresses example."""

import pytest

from vpc_ec2_instance_with_multiple_static_ipaddresses.main import build_template


class TestVpcEc2InstanceWithMultipleStaticIpaddresses:
    """Test vpc_ec2_instance_with_multiple_static_ipaddresses example."""

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
        assert len(output["Resources"]) == 5
