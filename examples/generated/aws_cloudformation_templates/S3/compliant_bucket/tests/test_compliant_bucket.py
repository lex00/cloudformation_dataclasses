"""Tests for compliant_bucket S3 example."""

import json

from ..main import build_template
from ..resources import (
    ObjectStorageBucket,
    ObjectStorageLogBucket,
    ObjectStorageReplicaBucket,
)


def test_template_structure():
    """Verify template has correct structure."""
    template = build_template()
    result = template.to_dict()

    assert result["AWSTemplateFormatVersion"] == "2010-09-09"
    assert "Description" in result
    assert "Parameters" in result
    assert "Resources" in result


def test_template_parameters():
    """Verify all parameters are present with correct types."""
    template = build_template()
    result = template.to_dict()
    params = result["Parameters"]

    assert "AppName" in params
    assert params["AppName"]["Type"] == "String"
    assert "Description" in params["AppName"]


def test_template_resources():
    """Verify all 8 resources are present."""
    template = build_template()
    result = template.to_dict()
    resources = result["Resources"]

    # 3 buckets
    assert "ObjectStorageBucket" in resources
    assert "ObjectStorageLogBucket" in resources
    assert "ObjectStorageReplicaBucket" in resources

    # 3 bucket policies
    assert "ObjectStorageBucketPolicyPolicy" in resources
    assert "ObjectStorageLogBucketPolicyPolicy" in resources
    assert "ObjectStorageReplicaBucketPolicyPolicy" in resources

    # IAM resources
    assert "ObjectStorageReplicationRole" in resources
    assert "ObjectStorageReplicationPolicy" in resources


def test_bucket_types():
    """Verify bucket resource types."""
    template = build_template()
    result = template.to_dict()
    resources = result["Resources"]

    assert resources["ObjectStorageBucket"]["Type"] == "AWS::S3::Bucket"
    assert resources["ObjectStorageLogBucket"]["Type"] == "AWS::S3::Bucket"
    assert resources["ObjectStorageReplicaBucket"]["Type"] == "AWS::S3::Bucket"


def test_bucket_policy_types():
    """Verify bucket policy resource types."""
    template = build_template()
    result = template.to_dict()
    resources = result["Resources"]

    assert resources["ObjectStorageBucketPolicyPolicy"]["Type"] == "AWS::S3::BucketPolicy"
    assert resources["ObjectStorageLogBucketPolicyPolicy"]["Type"] == "AWS::S3::BucketPolicy"
    assert resources["ObjectStorageReplicaBucketPolicyPolicy"]["Type"] == "AWS::S3::BucketPolicy"


def test_bucket_encryption():
    """Verify all buckets have AES256 encryption."""
    template = build_template()
    result = template.to_dict()
    resources = result["Resources"]

    for bucket_name in ["ObjectStorageBucket", "ObjectStorageLogBucket", "ObjectStorageReplicaBucket"]:
        bucket = resources[bucket_name]["Properties"]
        assert "BucketEncryption" in bucket
        encryption = bucket["BucketEncryption"]
        assert "ServerSideEncryptionConfiguration" in encryption
        rules = encryption["ServerSideEncryptionConfiguration"]
        assert len(rules) >= 1
        sse_default = rules[0]["ServerSideEncryptionByDefault"]
        assert sse_default["SSEAlgorithm"] == "AES256"


def test_bucket_versioning():
    """Verify all buckets have versioning enabled."""
    template = build_template()
    result = template.to_dict()
    resources = result["Resources"]

    for bucket_name in ["ObjectStorageBucket", "ObjectStorageLogBucket", "ObjectStorageReplicaBucket"]:
        bucket = resources[bucket_name]["Properties"]
        assert "VersioningConfiguration" in bucket
        assert bucket["VersioningConfiguration"]["Status"] == "Enabled"


def test_bucket_public_access_blocked():
    """Verify all buckets block public access."""
    template = build_template()
    result = template.to_dict()
    resources = result["Resources"]

    for bucket_name in ["ObjectStorageBucket", "ObjectStorageLogBucket", "ObjectStorageReplicaBucket"]:
        bucket = resources[bucket_name]["Properties"]
        assert "PublicAccessBlockConfiguration" in bucket
        public_access = bucket["PublicAccessBlockConfiguration"]
        assert public_access["BlockPublicAcls"] is True
        assert public_access["BlockPublicPolicy"] is True
        assert public_access["IgnorePublicAcls"] is True
        assert public_access["RestrictPublicBuckets"] is True


def test_log_bucket_has_object_lock():
    """Verify log bucket has object lock enabled."""
    template = build_template()
    result = template.to_dict()
    log_bucket = result["Resources"]["ObjectStorageLogBucket"]["Properties"]

    assert log_bucket["ObjectLockEnabled"] is True
    assert "ObjectLockConfiguration" in log_bucket


def test_main_bucket_has_replication():
    """Verify main bucket has replication configured."""
    template = build_template()
    result = template.to_dict()
    main_bucket = result["Resources"]["ObjectStorageBucket"]["Properties"]

    assert "ReplicationConfiguration" in main_bucket
    replication = main_bucket["ReplicationConfiguration"]
    assert "Role" in replication
    assert "Rules" in replication
    assert len(replication["Rules"]) >= 1


def test_main_bucket_has_logging():
    """Verify main bucket has logging configured."""
    template = build_template()
    result = template.to_dict()
    main_bucket = result["Resources"]["ObjectStorageBucket"]["Properties"]

    assert "LoggingConfiguration" in main_bucket
    logging = main_bucket["LoggingConfiguration"]
    assert "DestinationBucketName" in logging


def test_bucket_policies_deny_non_https():
    """Verify all bucket policies deny non-HTTPS requests."""
    template = build_template()
    result = template.to_dict()
    resources = result["Resources"]

    for policy_name in [
        "ObjectStorageBucketPolicyPolicy",
        "ObjectStorageLogBucketPolicyPolicy",
        "ObjectStorageReplicaBucketPolicyPolicy",
    ]:
        policy = resources[policy_name]["Properties"]
        policy_doc = policy["PolicyDocument"]
        statements = policy_doc["Statement"]

        # Find the deny statement
        deny_stmts = [s for s in statements if s["Effect"] == "Deny"]
        assert len(deny_stmts) >= 1

        deny_stmt = deny_stmts[0]
        assert deny_stmt["Action"] == "s3:*"
        assert "Condition" in deny_stmt
        assert "Bool" in deny_stmt["Condition"]
        assert deny_stmt["Condition"]["Bool"]["aws:SecureTransport"] is False


def test_iam_role_exists():
    """Verify IAM role for replication exists."""
    template = build_template()
    result = template.to_dict()
    resources = result["Resources"]

    assert "ObjectStorageReplicationRole" in resources
    # Note: Type may be CloudFormationResource since IAM isn't in generated types


def test_template_json_serialization():
    """Verify template can be serialized to JSON."""
    template = build_template()
    json_str = template.to_json()

    # Should be valid JSON
    parsed = json.loads(json_str)
    assert "Resources" in parsed
    assert len(parsed["Resources"]) == 8


def test_template_validation():
    """Verify template passes basic validation."""
    template = build_template()
    errors = template.validate()
    assert errors == []
