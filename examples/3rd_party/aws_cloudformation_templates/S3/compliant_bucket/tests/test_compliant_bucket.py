"""Test all 2 versions of compliant_bucket produce identical CloudFormation output."""

import pytest

from ..block.main import build_template as build_block
from ..mixed.main import build_template as build_mixed


class TestAllVersions:
    """Test all 2 versions produce identical CloudFormation output."""

    @pytest.fixture
    def block_template(self):
        """Load block version."""
        return build_block()

    @pytest.fixture
    def mixed_template(self):
        """Load mixed version."""
        return build_mixed()

    def test_all_versions_produce_same_output(
        self,
        block_template,
        mixed_template,
    ):
        """Both versions should produce identical CloudFormation."""
        block = block_template.to_dict()
        mixed = mixed_template.to_dict()

        assert block == mixed, "block != mixed"

    def test_block_validates(self, block_template):
        """block version should pass validation."""
        errors = block_template.validate()
        assert errors == [], f"Validation errors: {errors}"

    def test_mixed_validates(self, mixed_template):
        """mixed version should pass validation."""
        errors = mixed_template.validate()
        assert errors == [], f"Validation errors: {errors}"

    def test_template_structure(self, block_template):
        """Verify basic template structure."""
        template = block_template.to_dict()
        assert "AWSTemplateFormatVersion" in template
        assert "Resources" in template
        assert "Parameters" in template

    def test_template_resources(self, block_template):
        """Verify all expected resources are present."""
        template = block_template.to_dict()
        resources = template["Resources"]

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

    def test_template_parameters(self, block_template):
        """Verify AppName parameter exists."""
        template = block_template.to_dict()
        parameters = template["Parameters"]

        assert "AppName" in parameters
        assert parameters["AppName"]["Type"] == "String"

    def test_bucket_encryption_enabled(self, block_template):
        """Verify all buckets have encryption configured."""
        template = block_template.to_dict()
        resources = template["Resources"]

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

    def test_public_access_blocked(self, block_template):
        """Verify all buckets have public access blocked."""
        template = block_template.to_dict()
        resources = template["Resources"]

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
