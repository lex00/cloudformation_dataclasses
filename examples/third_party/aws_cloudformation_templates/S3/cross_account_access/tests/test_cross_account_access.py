"""Tests for cross_account_access example."""

import pytest

from ..main import build_template


class TestCrossAccountAccess:
    """Test cross_account_access example."""

    @pytest.fixture
    def template(self):
        """Build template."""
        return build_template()

    def test_validates(self, template):
        """Template should pass validation."""
        errors = template.validate()
        assert errors == [], f"Validation errors: {errors}"

    def test_template_structure(self, template):
        """Verify basic template structure."""
        output = template.to_dict()
        assert "AWSTemplateFormatVersion" in output
        assert "Resources" in output
        assert "Parameters" in output
        assert "Outputs" in output

    def test_template_resources(self, template):
        """Verify all expected resources are present."""
        output = template.to_dict()
        resources = output["Resources"]

        expected_resources = [
            "Bucket",
            "BucketPolicy",
        ]

        for resource_id in expected_resources:
            assert resource_id in resources, f"Missing resource: {resource_id}"

    def test_template_parameters(self, template):
        """Verify parameters exist."""
        output = template.to_dict()
        parameters = output["Parameters"]

        assert "BucketName" in parameters
        assert parameters["BucketName"]["Type"] == "String"

        assert "PublisherAccountID" in parameters
        assert parameters["PublisherAccountID"]["Type"] == "String"

    def test_template_outputs(self, template):
        """Verify outputs exist."""
        output = template.to_dict()
        outputs = output["Outputs"]

        assert "BucketOutput" in outputs
        assert "BucketPolicyOutput" in outputs

    def test_bucket_encryption_enabled(self, template):
        """Verify bucket has encryption configured."""
        output = template.to_dict()
        resources = output["Resources"]

        bucket = resources["Bucket"]
        assert bucket["Type"] == "AWS::S3::Bucket"
        props = bucket["Properties"]
        assert "BucketEncryption" in props

    def test_bucket_versioning_enabled(self, template):
        """Verify bucket has versioning enabled."""
        output = template.to_dict()
        resources = output["Resources"]

        bucket = resources["Bucket"]
        props = bucket["Properties"]
        assert "VersioningConfiguration" in props
        assert props["VersioningConfiguration"]["Status"] == "Enabled"

    def test_public_access_blocked(self, template):
        """Verify bucket has public access blocked."""
        output = template.to_dict()
        resources = output["Resources"]

        bucket = resources["Bucket"]
        props = bucket["Properties"]
        assert "PublicAccessBlockConfiguration" in props
        pac = props["PublicAccessBlockConfiguration"]
        assert pac.get("BlockPublicAcls") is True
        assert pac.get("BlockPublicPolicy") is True
        assert pac.get("IgnorePublicAcls") is True
        assert pac.get("RestrictPublicBuckets") is True

    def test_bucket_policy_has_cross_account_statements(self, template):
        """Verify bucket policy has cross-account access statements."""
        output = template.to_dict()
        resources = output["Resources"]

        policy = resources["BucketPolicy"]
        assert policy["Type"] == "AWS::S3::BucketPolicy"
        policy_doc = policy["Properties"]["PolicyDocument"]

        # Should have 3 statements: 2 Allow (cross-account) + 1 Deny (secure transport)
        statements = policy_doc["Statement"]
        assert len(statements) == 3

        # Check for Allow statements with cross-account principal
        allow_statements = [s for s in statements if s["Effect"] == "Allow"]
        assert len(allow_statements) == 2

        # Check for Deny statement with SecureTransport condition
        deny_statements = [s for s in statements if s["Effect"] == "Deny"]
        assert len(deny_statements) == 1
        deny_stmt = deny_statements[0]
        assert "Condition" in deny_stmt
        assert "Bool" in deny_stmt["Condition"]
