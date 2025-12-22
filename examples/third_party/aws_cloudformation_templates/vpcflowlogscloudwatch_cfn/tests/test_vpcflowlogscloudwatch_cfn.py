"""Tests for vpcflowlogscloudwatch_cfn example."""

import pytest

from vpcflowlogscloudwatch_cfn.main import build_template


class TestVpcflowlogscloudwatchCfn:
    """Test vpcflowlogscloudwatch_cfn example."""

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
        assert len(output["Resources"]) == 3
