"""
Basic tests for S3 bucket example.

These tests demonstrate how to use cloudformation_dataclasses and verify that
the example generates valid CloudFormation templates.
"""

from cloudformation_dataclasses.core import Template

# Import the example dataclasses
from ..bucket import MyData
from ..bucket_policy import MyDataPolicy


def test_example_generates_valid_template():
    """Verify the example generates a valid CloudFormation template."""
    # Create resources
    bucket = MyData()
    policy = MyDataPolicy()

    # Add to template
    template = Template(description="S3 bucket with encryption policy")
    template.add_resource(bucket)
    template.add_resource(policy)

    # Validate
    errors = template.validate()
    assert errors == [], f"Template validation failed: {errors}"


def test_bucket_has_expected_configuration():
    """Verify the bucket has expected encryption and versioning."""
    bucket = MyData()

    # Get CloudFormation representation
    cf_dict = bucket.resource.to_dict()

    # Check encryption is configured
    assert "BucketEncryption" in cf_dict["Properties"]
    encryption = cf_dict["Properties"]["BucketEncryption"]
    assert encryption["ServerSideEncryptionConfiguration"][0][
        "ServerSideEncryptionByDefault"
    ]["SSEAlgorithm"] == "AES256"

    # Check versioning is enabled
    assert "VersioningConfiguration" in cf_dict["Properties"]
    assert cf_dict["Properties"]["VersioningConfiguration"]["Status"] == "Enabled"


def test_bucket_has_merged_tags():
    """Verify tags from context and resource are merged."""
    bucket = MyData()

    # Check all tags are present
    all_tags = bucket.resource.all_tags
    tag_dict = {tag.key: tag.value for tag in all_tags}

    # Context tags
    assert tag_dict["Environment"] == "Production"
    assert tag_dict["Project"] == "MyApplication"
    assert tag_dict["ManagedBy"] == "cloudformation-dataclasses"

    # Resource-specific tag
    assert tag_dict["DataClassification"] == "sensitive"


def test_policy_references_bucket():
    """Verify the bucket policy correctly references the bucket."""
    bucket = MyData()
    policy = MyDataPolicy()

    # Get CloudFormation representation
    cf_dict = policy.resource.to_dict()

    # Check bucket reference
    assert cf_dict["Properties"]["Bucket"] == {"Ref": "MyData"}


def test_context_driven_naming():
    """Verify automatic resource naming from deployment context."""
    bucket = MyData()

    # Check generated name follows pattern
    expected_name = "analytics-DataPlatform-MyData-prod-001-blue-us-east-1"
    assert bucket.resource.resource_name == expected_name

    # Logical ID should be the class name
    assert bucket.resource.logical_id == "MyData"
