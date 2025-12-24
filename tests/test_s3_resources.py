"""
Framework validation tests for S3 resources.

Tests the core functionality of CloudFormation dataclasses with S3 resources:
- Resource creation and serialization
- Template generation and validation
- Tag handling
- Cross-resource references
"""

import json

import pytest

from cloudformation_dataclasses.aws.s3 import Bucket, BucketPolicy
from cloudformation_dataclasses.core import (
    Template,
    Tag,
    cloudformation_dataclass,
    ref,
)


def test_bucket_creation():
    """Test that bucket can be created with wrapper pattern."""

    @cloudformation_dataclass
    class SimpleBucket:
        resource: Bucket

    bucket = SimpleBucket()

    assert bucket.resource is not None
    assert isinstance(bucket.resource, Bucket)


def test_bucket_has_cloudformation_methods():
    """Test that bucket resource has CloudFormation methods."""

    @cloudformation_dataclass
    class SimpleBucket:
        resource: Bucket

    bucket = SimpleBucket()

    assert hasattr(bucket.resource, "ref")
    assert hasattr(bucket.resource, "get_att")
    assert hasattr(bucket.resource, "to_dict")
    assert hasattr(bucket.resource, "_get_properties")


def test_bucket_ref():
    """Test that Ref intrinsic function works."""

    @cloudformation_dataclass
    class SimpleBucket:
        resource: Bucket

    bucket = SimpleBucket()
    ref_func = bucket.resource.ref()

    assert ref_func.to_dict() == {"Ref": "SimpleBucket"}


def test_template_generation():
    """Test that bucket generates valid CloudFormation template."""

    @cloudformation_dataclass
    class SimpleBucket:
        resource: Bucket

    bucket = SimpleBucket()

    template = Template(description="Test S3 bucket template")
    template.add_resource(bucket)

    # Validate template structure
    errors = template.validate()
    assert errors == [], f"Template validation failed: {errors}"

    # Check template dict structure
    template_dict = template.to_dict()
    assert "AWSTemplateFormatVersion" in template_dict
    assert template_dict["AWSTemplateFormatVersion"] == "2010-09-09"
    assert "Description" in template_dict
    assert template_dict["Description"] == "Test S3 bucket template"
    assert "Resources" in template_dict
    assert "SimpleBucket" in template_dict["Resources"]


def test_template_json_serialization():
    """Test that template serializes to valid JSON."""

    @cloudformation_dataclass
    class SimpleBucket:
        resource: Bucket

    bucket = SimpleBucket()

    template = Template()
    template.add_resource(bucket)

    json_str = template.to_json()

    # Verify it's valid JSON
    parsed = json.loads(json_str)
    assert parsed["Resources"]["SimpleBucket"]["Type"] == "AWS::S3::Bucket"


def test_template_yaml_serialization():
    """Test that template serializes to YAML (if pyyaml available)."""
    pytest.importorskip("yaml")

    @cloudformation_dataclass
    class SimpleBucket:
        resource: Bucket

    bucket = SimpleBucket()

    template = Template()
    template.add_resource(bucket)

    yaml_str = template.to_yaml()

    # Basic check that it's YAML format
    assert "AWSTemplateFormatVersion:" in yaml_str
    assert "Resources:" in yaml_str
    assert "SimpleBucket:" in yaml_str
    assert "AWS::S3::Bucket" in yaml_str


def test_bucket_properties_serialization():
    """Test that bucket properties serialize correctly."""

    @cloudformation_dataclass
    class VersionedBucket:
        resource: Bucket
        versioning_configuration = {"Status": "Enabled"}

    bucket = VersionedBucket()

    cf_dict = bucket.resource.to_dict()

    assert cf_dict["Type"] == "AWS::S3::Bucket"
    assert "Properties" in cf_dict
    assert cf_dict["Properties"]["VersioningConfiguration"]["Status"] == "Enabled"


def test_multiple_buckets_in_template():
    """Test template with multiple bucket resources."""

    @cloudformation_dataclass
    class FirstBucket:
        resource: Bucket

    @cloudformation_dataclass
    class SecondBucket:
        resource: Bucket

    bucket1 = FirstBucket()
    bucket2 = SecondBucket()

    template = Template()
    template.add_resource(bucket1)
    template.add_resource(bucket2)

    errors = template.validate()
    assert errors == []

    template_dict = template.to_dict()
    assert len(template_dict["Resources"]) == 2
    assert "FirstBucket" in template_dict["Resources"]
    assert "SecondBucket" in template_dict["Resources"]


def test_resource_tags():
    """Test that resource tags are handled correctly."""

    @cloudformation_dataclass
    class TaggedBucket:
        resource: Bucket
        tags = [
            {"Key": "Environment", "Value": "Test"},
            {"Key": "ManagedBy", "Value": "pytest"},
        ]

    bucket = TaggedBucket()

    # Verify tags are converted to Tag instances
    assert len(bucket.resource.tags) == 2
    assert bucket.resource.tags[0].key == "Environment"
    assert bucket.resource.tags[0].value == "Test"
    assert bucket.resource.tags[1].key == "ManagedBy"
    assert bucket.resource.tags[1].value == "pytest"

    # Verify all_tags returns the tags
    assert len(bucket.resource.all_tags) == 2


def test_tags_in_cloudformation_template():
    """Test that tags appear in the CloudFormation template."""

    @cloudformation_dataclass
    class TaggedBucket:
        resource: Bucket
        tags = [
            {"Key": "Environment", "Value": "Test"},
            {"Key": "ManagedBy", "Value": "pytest"},
        ]

    bucket = TaggedBucket()
    template = Template(description="Test bucket with tags")
    template.add_resource(bucket)

    template_dict = template.to_dict()
    tags = template_dict["Resources"]["TaggedBucket"]["Properties"]["Tags"]

    # Verify tags are in the CloudFormation template
    assert len(tags) == 2

    # Convert to dict for easier assertion
    tag_dict = {tag["Key"]: tag["Value"] for tag in tags}

    assert tag_dict["Environment"] == "Test"
    assert tag_dict["ManagedBy"] == "pytest"


def test_tag_wrapper_classes():
    """Test that Tag wrapper classes work correctly."""

    @cloudformation_dataclass
    class EnvironmentTag:
        resource: Tag
        key = "Environment"
        value = "Production"

    @cloudformation_dataclass
    class ProjectTag:
        resource: Tag
        key = "Project"
        value = "Analytics"

    @cloudformation_dataclass
    class TaggedBucket:
        resource: Bucket
        tags = [EnvironmentTag, ProjectTag]

    bucket = TaggedBucket()

    # Verify tags are created from wrapper classes
    assert len(bucket.resource.tags) == 2
    tag_keys = {tag.key for tag in bucket.resource.tags}
    assert tag_keys == {"Environment", "Project"}


def test_cross_resource_references():
    """Test that cross-resource references work with ref()."""

    @cloudformation_dataclass
    class RefBucket:
        resource: Bucket

    @cloudformation_dataclass
    class RefBucketPolicy:
        resource: BucketPolicy
        bucket = ref(RefBucket)
        policy_document = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Deny",
                    "Principal": "*",
                    "Action": "s3:*",
                    "Resource": "*",
                }
            ],
        }

    bucket = RefBucket()
    policy = RefBucketPolicy()

    template = Template()
    template.add_resource(bucket)
    template.add_resource(policy)

    errors = template.validate()
    assert errors == []

    template_dict = template.to_dict()

    # Verify bucket reference in policy
    assert template_dict["Resources"]["RefBucketPolicy"]["Properties"]["Bucket"] == {
        "Ref": "RefBucket"
    }
