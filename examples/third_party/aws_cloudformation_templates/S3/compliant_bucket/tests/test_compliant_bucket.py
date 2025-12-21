"""Tests for compliant_bucket example."""

import pytest

from ..main import build_template


class TestCompliantBucket:
    """Test compliant_bucket example."""

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

    def test_template_resources(self, template):
        """Verify all expected resources are present."""
        output = template.to_dict()
        resources = output["Resources"]

        expected_resources = [
            "ObjectStorageBucket",
            "ObjectStorageLogBucket",
            "ObjectStorageReplicaBucket",
            "ObjectStorageBucketPolicyPolicy",
            "ObjectStorageLogBucketPolicyPolicy",
            "ObjectStorageReplicaBucketPolicyPolicy",
            "ObjectStorageReplicationRole",
            "ObjectStorageReplicationPolicy",
        ]

        for resource_id in expected_resources:
            assert resource_id in resources, f"Missing resource: {resource_id}"

    def test_template_parameters(self, template):
        """Verify AppName parameter exists."""
        output = template.to_dict()
        parameters = output["Parameters"]

        assert "AppName" in parameters
        assert parameters["AppName"]["Type"] == "String"

    def test_bucket_encryption_enabled(self, template):
        """Verify all buckets have encryption configured."""
        output = template.to_dict()
        resources = output["Resources"]

        bucket_resources = [
            "ObjectStorageBucket",
            "ObjectStorageLogBucket",
            "ObjectStorageReplicaBucket",
        ]

        for bucket_id in bucket_resources:
            bucket = resources[bucket_id]
            assert bucket["Type"] == "AWS::S3::Bucket"
            props = bucket["Properties"]
            assert "BucketEncryption" in props, f"{bucket_id} missing encryption"

    def test_public_access_blocked(self, template):
        """Verify all buckets have public access blocked."""
        output = template.to_dict()
        resources = output["Resources"]

        bucket_resources = [
            "ObjectStorageBucket",
            "ObjectStorageLogBucket",
            "ObjectStorageReplicaBucket",
        ]

        for bucket_id in bucket_resources:
            props = resources[bucket_id]["Properties"]
            if "PublicAccessBlockConfiguration" in props:
                pac = props["PublicAccessBlockConfiguration"]
                assert pac.get("BlockPublicAcls") is True
                assert pac.get("BlockPublicPolicy") is True
                assert pac.get("IgnorePublicAcls") is True
                assert pac.get("RestrictPublicBuckets") is True
