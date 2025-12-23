"""Tests for event_consume_from_list example."""

import pytest

from event_consume_from_list.main import build_template


class TestEventConsumeFromList:
    """Test event_consume_from_list example."""

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
