"""
Framework validation tests for S3 resources.

Tests the core functionality of CloudFormation dataclasses with S3 resources:
- Resource creation and serialization
- Template generation and validation
- Tag merging
- Context-driven naming
- Cross-resource references
"""

import json

import pytest

from cloudformation_dataclasses.aws.s3 import Bucket, BucketPolicy
from cloudformation_dataclasses.core import (
    Template,
    DeploymentContext,
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


def test_deployment_context_tags():
    """Test that deployment context tags are merged with resource-specific tags."""

    @cloudformation_dataclass
    class ProdContext:
        context: DeploymentContext
        tags = [
            {"Key": "Environment", "Value": "Test"},
            {"Key": "ManagedBy", "Value": "pytest"},
        ]

    ctx = ProdContext()

    @cloudformation_dataclass
    class TaggedBucket:
        resource: Bucket
        context = ctx
        tags = [{"Key": "DataClassification", "Value": "test-data"}]

    bucket = TaggedBucket()

    # Verify context has 2 base tags
    assert len(ctx.tags) == 2
    context_tag_keys = {tag["Key"] for tag in ctx.tags}
    assert context_tag_keys == {"Environment", "ManagedBy"}

    # Verify bucket has 1 resource-specific tag
    assert len(bucket.resource.tags) == 1
    assert bucket.resource.tags[0].key == "DataClassification"
    assert bucket.resource.tags[0].value == "test-data"

    # Verify all_tags merges both (2 from context + 1 resource-specific = 3 total)
    assert len(bucket.resource.all_tags) == 3
    all_tag_keys = {tag.key for tag in bucket.resource.all_tags}
    assert all_tag_keys == {"Environment", "ManagedBy", "DataClassification"}


def test_context_tags_in_cloudformation_template():
    """Test that context base tags appear in the CloudFormation template."""

    @cloudformation_dataclass
    class ProdContext:
        context: DeploymentContext
        tags = [
            {"Key": "Environment", "Value": "Test"},
            {"Key": "ManagedBy", "Value": "pytest"},
        ]

    ctx = ProdContext()

    @cloudformation_dataclass
    class TaggedBucket:
        resource: Bucket
        context = ctx
        tags = [{"Key": "DataClassification", "Value": "test-data"}]

    bucket = TaggedBucket()
    template = Template(description="Test bucket with context tags")
    template.add_resource(bucket)

    template_dict = template.to_dict()
    tags = template_dict["Resources"]["TaggedBucket"]["Properties"]["Tags"]

    # Verify all 3 tags are in the CloudFormation template
    assert len(tags) == 3

    # Convert to dict for easier assertion
    tag_dict = {tag["Key"]: tag["Value"] for tag in tags}

    # Verify context tags (2 base tags)
    assert tag_dict["Environment"] == "Test"
    assert tag_dict["ManagedBy"] == "pytest"

    # Verify resource-specific tag
    assert tag_dict["DataClassification"] == "test-data"


def test_context_driven_naming():
    """Test that deployment context provides automatic resource naming."""

    @cloudformation_dataclass
    class ProdContext:
        context: DeploymentContext
        project_name = "acme"
        component = "TestApp"
        stage = "test"
        deployment_name = "001"
        deployment_group = "blue"
        region = "us-east-1"

    ctx = ProdContext()

    @cloudformation_dataclass
    class MyTestBucket:
        resource: Bucket
        context = ctx

    bucket = MyTestBucket()

    # Verify context naming pattern
    # Class name: MyTestBucket
    # Pattern: {project_name}-{component}-{resource_name}-{stage}-{deployment_name}-{deployment_group}-{region}
    assert (
        bucket.resource.resource_name
        == "acme-TestApp-MyTestBucket-test-001-blue-us-east-1"
    )

    # Verify logical ID comes from wrapper class name
    assert bucket.resource.logical_id == "MyTestBucket"

    # Verify context values
    assert ctx.project_name == "acme"
    assert ctx.component == "TestApp"
    assert ctx.stage == "test"
    assert ctx.deployment_name == "001"
    assert ctx.deployment_group == "blue"
    assert ctx.region == "us-east-1"


def test_custom_naming_pattern():
    """Test that naming pattern can be customized."""

    @cloudformation_dataclass
    class SimpleContext:
        context: DeploymentContext
        component = "MyApp"
        naming_pattern = "{component}-{resource_name}"

    ctx = SimpleContext()

    @cloudformation_dataclass
    class NamedBucket:
        resource: Bucket
        context = ctx

    bucket = NamedBucket()

    # Verify custom pattern is used
    assert bucket.resource.resource_name == "MyApp-NamedBucket"


def test_resource_specific_naming_pattern():
    """Test that naming pattern can be overridden per resource."""

    @cloudformation_dataclass
    class ProdContext:
        context: DeploymentContext
        component = "TestApp"
        stage = "test"

    ctx = ProdContext()

    @cloudformation_dataclass
    class CustomNamedBucket:
        resource: Bucket
        context = ctx
        naming_pattern = "{resource_name}-{stage}"

    bucket = CustomNamedBucket()

    # Verify resource-specific pattern overrides context pattern
    assert bucket.resource.resource_name == "CustomNamedBucket-test"


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
