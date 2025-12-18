"""Tests for cross_account_access S3 example."""

import json

from ..cross_account_access import (
    build_template,
    ctx,
    SharedBucket,
    SharedBucketPolicy,
)


def test_template_structure():
    """Verify template has correct structure."""
    template = build_template()
    result = template.to_dict()

    assert result["AWSTemplateFormatVersion"] == "2010-09-09"
    assert "Description" in result
    assert "Parameters" in result
    assert "Resources" in result
    assert "Outputs" in result


def test_template_parameters():
    """Verify all parameters are present with correct types."""
    template = build_template()
    result = template.to_dict()
    params = result["Parameters"]

    # Both parameters present
    assert "BucketName" in params
    assert "PublisherAccountID" in params

    # Verify types
    assert params["BucketName"]["Type"] == "String"
    assert params["PublisherAccountID"]["Type"] == "String"

    # Verify descriptions
    assert "Description" in params["BucketName"]
    assert "Description" in params["PublisherAccountID"]


def test_template_resources():
    """Verify S3 bucket and policy resources."""
    template = build_template()
    result = template.to_dict()
    resources = result["Resources"]

    # Both resources present
    assert "SharedBucket" in resources
    assert "SharedBucketPolicy" in resources

    # Verify types
    assert resources["SharedBucket"]["Type"] == "AWS::S3::Bucket"
    assert resources["SharedBucketPolicy"]["Type"] == "AWS::S3::BucketPolicy"


def test_bucket_encryption():
    """Verify bucket has AES256 encryption configured."""
    template = build_template()
    result = template.to_dict()
    bucket = result["Resources"]["SharedBucket"]["Properties"]

    # Has encryption configuration
    assert "BucketEncryption" in bucket
    encryption = bucket["BucketEncryption"]

    # Has server-side encryption config
    assert "ServerSideEncryptionConfiguration" in encryption
    rules = encryption["ServerSideEncryptionConfiguration"]
    assert len(rules) == 1

    # AES256 algorithm
    sse_default = rules[0]["ServerSideEncryptionByDefault"]
    assert sse_default["SSEAlgorithm"] == "AES256"


def test_bucket_versioning():
    """Verify bucket has versioning enabled."""
    template = build_template()
    result = template.to_dict()
    bucket = result["Resources"]["SharedBucket"]["Properties"]

    assert "VersioningConfiguration" in bucket
    assert bucket["VersioningConfiguration"]["Status"] == "Enabled"


def test_bucket_public_access_block():
    """Verify bucket blocks all public access."""
    template = build_template()
    result = template.to_dict()
    bucket = result["Resources"]["SharedBucket"]["Properties"]

    assert "PublicAccessBlockConfiguration" in bucket
    public_access = bucket["PublicAccessBlockConfiguration"]

    assert public_access["BlockPublicAcls"] is True
    assert public_access["BlockPublicPolicy"] is True
    assert public_access["IgnorePublicAcls"] is True
    assert public_access["RestrictPublicBuckets"] is True


def test_bucket_name_from_parameter():
    """Verify bucket name references the BucketName parameter."""
    template = build_template()
    result = template.to_dict()
    bucket = result["Resources"]["SharedBucket"]["Properties"]

    assert bucket["BucketName"] == {"Ref": "BucketName"}


def test_bucket_policy_references_bucket():
    """Verify bucket policy references the SharedBucket resource."""
    template = build_template()
    result = template.to_dict()
    policy = result["Resources"]["SharedBucketPolicy"]["Properties"]

    assert policy["Bucket"] == {"Ref": "SharedBucket"}


def test_bucket_policy_statements():
    """Verify bucket policy has correct IAM statements."""
    template = build_template()
    result = template.to_dict()
    policy_doc = result["Resources"]["SharedBucketPolicy"]["Properties"]["PolicyDocument"]

    assert policy_doc["Version"] == "2012-10-17"
    assert len(policy_doc["Statement"]) == 3

    # Find statements by Sid
    statements = {s["Sid"]: s for s in policy_doc["Statement"]}

    # Cross-account ListBucket
    assert "CrossAccListBucket" in statements
    list_stmt = statements["CrossAccListBucket"]
    assert list_stmt["Effect"] == "Allow"
    assert list_stmt["Action"] == "s3:ListBucket"

    # Cross-account GetObject
    assert "CrossAccGetObject" in statements
    get_stmt = statements["CrossAccGetObject"]
    assert get_stmt["Effect"] == "Allow"
    assert get_stmt["Action"] == "s3:GetObject"

    # Deny non-HTTPS
    assert "DenyNonHttps" in statements
    deny_stmt = statements["DenyNonHttps"]
    assert deny_stmt["Effect"] == "Deny"
    assert deny_stmt["Action"] == "s3:*"
    assert "Condition" in deny_stmt
    assert deny_stmt["Condition"]["Bool"]["aws:SecureTransport"] == "false"


def test_bucket_policy_uses_sub_with_partition():
    """Verify bucket policy ARNs use Sub with AWS::Partition."""
    template = build_template()
    result = template.to_dict()
    policy_doc = result["Resources"]["SharedBucketPolicy"]["Properties"]["PolicyDocument"]

    # Find the ListBucket statement
    list_stmt = next(s for s in policy_doc["Statement"] if s["Sid"] == "CrossAccListBucket")

    # Resource should be a Sub intrinsic (already serialized to dict)
    resource = list_stmt["Resource"]
    assert "Fn::Sub" in resource
    # Sub should include AWS::Partition
    sub_value = resource["Fn::Sub"]
    assert isinstance(sub_value, list)
    assert sub_value[0] == "arn:${AWS::Partition}:s3:::${Bucket}"
    # Variables should include Bucket ref
    assert "Bucket" in sub_value[1]
    assert sub_value[1]["Bucket"] == {"Ref": "BucketName"}


def test_template_outputs():
    """Verify outputs reference the resources."""
    template = build_template()
    result = template.to_dict()
    outputs = result["Outputs"]

    assert "BucketOutput" in outputs
    assert outputs["BucketOutput"]["Value"] == {"Ref": "SharedBucket"}
    assert "Description" in outputs["BucketOutput"]

    assert "BucketPolicyOutput" in outputs
    assert outputs["BucketPolicyOutput"]["Value"] == {"Ref": "SharedBucketPolicy"}


def test_template_json_serialization():
    """Verify template can be serialized to JSON."""
    template = build_template()
    json_str = template.to_json()

    # Should be valid JSON
    parsed = json.loads(json_str)
    assert "Resources" in parsed
    assert "SharedBucket" in parsed["Resources"]
    assert "SharedBucketPolicy" in parsed["Resources"]


def test_template_validation():
    """Verify template passes basic validation."""
    template = build_template()
    errors = template.validate()
    assert errors == []


def test_deployment_context():
    """Verify deployment context is configured correctly."""
    assert ctx.project_name == "dataplatform"
    assert ctx.component == "storage"
    assert ctx.stage == "prod"
    assert ctx.region == "us-east-1"


def test_resource_naming():
    """Verify resource naming uses deployment context pattern."""
    bucket = SharedBucket()
    # Resource name should follow pattern: {project_name}-{component}-{resource_name}-{stage}
    expected_name = "dataplatform-storage-SharedBucket-prod"
    assert bucket.resource.resource_name == expected_name

    # Logical ID should be the class name
    assert bucket.resource.logical_id == "SharedBucket"


def test_resource_tags():
    """Verify tags are applied from deployment context."""
    bucket = SharedBucket()
    all_tags = bucket.resource.all_tags

    # Should have context tags
    tag_dict = {tag.key: tag.value for tag in all_tags}
    assert tag_dict["Environment"] == "Production"
    assert tag_dict["ManagedBy"] == "cloudformation-dataclasses"
