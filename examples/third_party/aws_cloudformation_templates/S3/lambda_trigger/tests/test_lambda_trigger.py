"""Tests for Lambda Trigger example."""

import pytest

from ..main import build_template


class TestLambdaTrigger:
    """Test lambda_trigger example."""

    @pytest.fixture
    def template(self):
        """Build template."""
        return build_template()

    def test_validates(self, template):
        """Template should pass validation."""
        errors = template.validate()
        assert errors == [], f"Validation errors: {errors}"

    def test_template_structure(self, template):
        """Verify template has expected structure."""
        output = template.to_dict()
        assert "AWSTemplateFormatVersion" in output
        assert "Resources" in output
        assert "Parameters" in output

    def test_template_resources(self, template):
        """Verify all expected resources are present."""
        resources = template.to_dict()["Resources"]
        expected = [
            "LambdaIAMRole",
            "S3TriggerLambdaFunction",
            "LambdaInvokePermission",
            "S3BucketNotification",
        ]
        for res_id in expected:
            assert res_id in resources

    def test_bucket_depends_on_permission(self, template):
        """Verify S3 bucket has DependsOn for Lambda permission."""
        resources = template.to_dict()["Resources"]
        bucket = resources["S3BucketNotification"]
        assert "DependsOn" in bucket
        assert "LambdaInvokePermission" in bucket["DependsOn"]

    def test_lambda_permission_source_arn(self, template):
        """Verify Lambda permission uses Sub for SourceArn (not GetAtt)."""
        resources = template.to_dict()["Resources"]
        permission = resources["LambdaInvokePermission"]
        source_arn = permission["Properties"]["SourceArn"]
        # Should be Fn::Sub, not Fn::GetAtt
        assert "Fn::Sub" in source_arn
        assert "Fn::GetAtt" not in str(source_arn)
