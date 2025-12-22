"""Tests for ec2_instance_with_ephemeral_drives example."""

import pytest

from ec2_instance_with_ephemeral_drives.main import build_template


class TestEc2InstanceWithEphemeralDrives:
    """Test ec2_instance_with_ephemeral_drives example."""

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
