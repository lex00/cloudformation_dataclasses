"""Tests for common_resources_stackset example."""

import pytest

from common_resources_stackset.main import build_template


class TestCommonResourcesStackset:
    """Test common_resources_stackset example."""

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
