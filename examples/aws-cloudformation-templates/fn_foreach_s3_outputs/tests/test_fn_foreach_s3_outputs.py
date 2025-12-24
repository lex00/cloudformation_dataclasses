"""Tests for fn_foreach_s3_outputs example."""

import pytest

from fn_foreach_s3_outputs.main import build_template


class TestFnForeachS3Outputs:
    """Test fn_foreach_s3_outputs example."""

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
        assert len(output["Resources"]) == 0
