"""
Tests for core base classes.

Tests Tag, PolicyStatement, PolicyDocument, DeploymentContext, and CloudFormationResource.
"""

import pytest
from dataclasses import dataclass

from cloudformation_dataclasses.core.base import (
    CloudFormationResource,
    DeploymentContext,
    DenyStatement,
    PolicyDocument,
    PolicyStatement,
    Tag,
)
from cloudformation_dataclasses.intrinsics.functions import Ref


class TestTag:
    """Tests for Tag class."""

    def test_tag_creation(self):
        """Test creating a tag."""
        tag = Tag(key="Environment", value="Production")
        assert tag.key == "Environment"
        assert tag.value == "Production"

    def test_tag_to_dict(self):
        """Test tag serialization to dict."""
        tag = Tag(key="Project", value="MyApp")
        assert tag.to_dict() == {"Key": "Project", "Value": "MyApp"}

    def test_tag_multiple(self):
        """Test creating multiple tags."""
        tags = [
            Tag(key="Environment", value="Production"),
            Tag(key="Project", value="MyApp"),
            Tag(key="ManagedBy", value="CloudFormation")
        ]
        assert len(tags) == 3
        assert all(isinstance(t, Tag) for t in tags)


class TestPolicyStatement:
    """Tests for PolicyStatement class."""

    def test_policy_statement_allow(self):
        """Test creating an Allow policy statement."""
        stmt = PolicyStatement(
            sid="AllowS3Read",
            effect="Allow",
            principal="*",
            action="s3:GetObject",
            resource_arn="arn:aws:s3:::my-bucket/*"
        )
        result = stmt.to_dict()
        assert result["Effect"] == "Allow"
        assert result["Sid"] == "AllowS3Read"
        assert result["Principal"] == "*"
        assert result["Action"] == "s3:GetObject"
        assert result["Resource"] == "arn:aws:s3:::my-bucket/*"

    def test_policy_statement_deny(self):
        """Test creating a Deny policy statement."""
        stmt = PolicyStatement(
            effect="Deny",
            action="s3:PutObject",
            resource_arn="*"
        )
        result = stmt.to_dict()
        assert result["Effect"] == "Deny"
        assert result["Action"] == "s3:PutObject"
        assert result["Resource"] == "*"

    def test_policy_statement_with_condition(self):
        """Test policy statement with condition."""
        stmt = PolicyStatement(
            effect="Deny",
            action="s3:PutObject",
            resource_arn="arn:aws:s3:::my-bucket/*",
            condition={"StringNotEquals": {"s3:x-amz-server-side-encryption": "AES256"}}
        )
        result = stmt.to_dict()
        assert result["Condition"] == {
            "StringNotEquals": {"s3:x-amz-server-side-encryption": "AES256"}
        }

    def test_policy_statement_minimal(self):
        """Test policy statement with minimal fields."""
        stmt = PolicyStatement(effect="Allow")
        result = stmt.to_dict()
        assert result == {"Effect": "Allow"}
        assert "Sid" not in result
        assert "Principal" not in result

    def test_policy_statement_with_intrinsic(self):
        """Test policy statement with intrinsic function."""
        stmt = PolicyStatement(
            effect="Allow",
            action="s3:GetObject",
            resource_arn={"Fn::Sub": "arn:aws:s3:::${BucketName}/*"}
        )
        result = stmt.to_dict()
        assert result["Resource"] == {"Fn::Sub": "arn:aws:s3:::${BucketName}/*"}


class TestDenyStatement:
    """Tests for DenyStatement class."""

    def test_deny_statement_default_effect(self):
        """Test DenyStatement has Deny as default effect."""
        stmt = DenyStatement(action="s3:DeleteObject", resource_arn="*")
        result = stmt.to_dict()
        assert result["Effect"] == "Deny"

    def test_deny_statement_full(self):
        """Test DenyStatement with all fields."""
        stmt = DenyStatement(
            sid="DenyDelete",
            principal="*",
            action="s3:DeleteObject",
            resource_arn="arn:aws:s3:::my-bucket/*"
        )
        result = stmt.to_dict()
        assert result["Effect"] == "Deny"
        assert result["Sid"] == "DenyDelete"


class TestPolicyDocument:
    """Tests for PolicyDocument class."""

    def test_policy_document_empty(self):
        """Test creating an empty policy document."""
        doc = PolicyDocument()
        result = doc.to_dict()
        assert result["Version"] == "2012-10-17"
        assert result["Statement"] == []

    def test_policy_document_with_statements(self):
        """Test policy document with statements."""
        stmt1 = PolicyStatement(effect="Allow", action="s3:GetObject", resource_arn="*")
        stmt2 = PolicyStatement(effect="Deny", action="s3:DeleteObject", resource_arn="*")
        doc = PolicyDocument(statement=[stmt1, stmt2])
        result = doc.to_dict()
        assert len(result["Statement"]) == 2
        assert result["Statement"][0]["Effect"] == "Allow"
        assert result["Statement"][1]["Effect"] == "Deny"

    def test_policy_document_custom_version(self):
        """Test policy document with custom version."""
        doc = PolicyDocument(version="2008-10-17")
        result = doc.to_dict()
        assert result["Version"] == "2008-10-17"

    def test_policy_document_with_dict_statement(self):
        """Test policy document with dict statement."""
        doc = PolicyDocument(statement=[
            {"Effect": "Allow", "Action": "s3:*", "Resource": "*"}
        ])
        result = doc.to_dict()
        assert result["Statement"][0] == {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        }


class TestDeploymentContext:
    """Tests for DeploymentContext class."""

    @dataclass
    class TestContext(DeploymentContext):
        """Test deployment context."""
        pass

    def test_deployment_context_resource_naming(self):
        """Test resource name generation from context."""
        ctx = self.TestContext(
            component="DataPlatform",
            stage="prod",
            deployment_name="001",
            deployment_group="blue",
            region="us-east-1"
        )
        name = ctx.resource_name("MyData")
        assert name == "DataPlatform-MyData-prod-001-blue-us-east-1"

    def test_deployment_context_custom_pattern(self):
        """Test custom naming pattern."""
        ctx = self.TestContext(
            component="API",
            stage="dev",
            naming_pattern="{component}-{resource_name}-{stage}"
        )
        name = ctx.resource_name("Gateway")
        assert name == "API-Gateway-dev"

    def test_deployment_context_simple_pattern(self):
        """Test simple naming pattern."""
        ctx = self.TestContext(
            component="MyApp",
            naming_pattern="{component}-{resource_name}"
        )
        name = ctx.resource_name("Database")
        assert name == "MyApp-Database"

    def test_deployment_context_partial_params(self):
        """Test naming with partial parameters."""
        ctx = self.TestContext(
            component="Service",
            stage="staging"
        )
        name = ctx.resource_name("Queue")
        # Should omit empty parts
        assert name == "Service-Queue-staging"

    def test_deployment_context_override_pattern(self):
        """Test overriding pattern per resource."""
        ctx = self.TestContext(
            component="Platform",
            stage="prod",
            naming_pattern="{component}-{resource_name}-{stage}"
        )
        # Override pattern for specific resource
        name = ctx.resource_name("Special", pattern="{resource_name}-only")
        assert name == "Special-only"

    def test_deployment_context_tags(self):
        """Test context tags."""
        ctx = self.TestContext(
            component="MyApp",
            tags=[
                Tag(key="Environment", value="Production"),
                Tag(key="ManagedBy", value="CloudFormation")
            ]
        )
        assert len(ctx.tags) == 2
        assert ctx.tags[0].key == "Environment"

    def test_deployment_context_blue_green(self):
        """Test blue/green deployment naming."""
        ctx_blue = self.TestContext(
            component="API",
            stage="prod",
            deployment_name="001",
            deployment_group="blue",
            region="us-east-1"
        )
        ctx_green = self.TestContext(
            component="API",
            stage="prod",
            deployment_name="001",
            deployment_group="green",
            region="us-east-1"
        )

        name_blue = ctx_blue.resource_name("Service")
        name_green = ctx_green.resource_name("Service")

        assert "blue" in name_blue
        assert "green" in name_green
        assert name_blue != name_green


class TestCloudFormationResource:
    """Tests for CloudFormationResource base class."""

    @dataclass
    class TestResource(CloudFormationResource):
        """Test resource class."""
        resource_type = "AWS::Test::Resource"
        test_property: str = "default"

        def _get_properties(self):
            return {"TestProperty": self.test_property}

    def test_resource_creation(self):
        """Test creating a resource."""
        resource = self.TestResource(test_property="value")
        assert resource.test_property == "value"

    def test_resource_logical_id(self):
        """Test resource logical ID."""
        resource = self.TestResource(logical_id="MyTestResource")
        assert resource.logical_id == "MyTestResource"
        assert resource.effective_logical_id == "MyTestResource"

    def test_resource_name_without_context(self):
        """Test resource name without context."""
        resource = self.TestResource(logical_id="MyResource")
        assert resource.resource_name == "MyResource"

    def test_resource_name_with_context(self):
        """Test resource name with deployment context."""
        @dataclass
        class TestContext(DeploymentContext):
            pass

        ctx = TestContext(
            component="MyApp",
            stage="prod",
            deployment_name="001",
            deployment_group="blue",
            region="us-east-1"
        )
        resource = self.TestResource(context=ctx, logical_id="Database")
        assert resource.resource_name == "MyApp-Database-prod-001-blue-us-east-1"

    def test_resource_tags_without_context(self):
        """Test resource tags without context."""
        resource = self.TestResource(
            tags=[Tag(key="Name", value="MyResource")]
        )
        assert len(resource.all_tags) == 1
        assert resource.all_tags[0].key == "Name"

    def test_resource_tags_with_context(self):
        """Test tag merging with context."""
        @dataclass
        class TestContext(DeploymentContext):
            pass

        ctx = TestContext(
            tags=[
                Tag(key="Environment", value="Production"),
                Tag(key="Project", value="MyProject")
            ]
        )
        resource = self.TestResource(
            context=ctx,
            tags=[Tag(key="Name", value="MyResource")]
        )
        all_tags = resource.all_tags
        assert len(all_tags) == 3
        assert all_tags[0].key == "Environment"
        assert all_tags[1].key == "Project"
        assert all_tags[2].key == "Name"

    def test_resource_to_dict(self):
        """Test resource serialization."""
        resource = self.TestResource(
            logical_id="MyResource",
            test_property="custom_value"
        )
        result = resource.to_dict()
        assert result["Type"] == "AWS::Test::Resource"
        assert result["Properties"]["TestProperty"] == "custom_value"

    def test_resource_with_depends_on(self):
        """Test resource with DependsOn."""
        resource = self.TestResource(
            depends_on=["OtherResource", "AnotherResource"]
        )
        result = resource.to_dict()
        assert result["DependsOn"] == ["OtherResource", "AnotherResource"]

    def test_resource_with_condition(self):
        """Test resource with Condition."""
        resource = self.TestResource(condition="IsProduction")
        result = resource.to_dict()
        assert result["Condition"] == "IsProduction"

    def test_resource_with_deletion_policy(self):
        """Test resource with DeletionPolicy."""
        resource = self.TestResource(deletion_policy="Retain")
        result = resource.to_dict()
        assert result["DeletionPolicy"] == "Retain"

    def test_resource_with_metadata(self):
        """Test resource with Metadata."""
        resource = self.TestResource(
            metadata={"Key": "Value", "Nested": {"Inner": "Data"}}
        )
        result = resource.to_dict()
        assert result["Metadata"]["Key"] == "Value"
        assert result["Metadata"]["Nested"]["Inner"] == "Data"

    def test_resource_ref(self):
        """Test creating Ref to resource."""
        resource = self.TestResource(logical_id="MyResource")
        ref = resource.ref()
        assert isinstance(ref, Ref)
        assert ref.to_dict() == {"Ref": "MyResource"}

    def test_resource_get_att(self):
        """Test creating GetAtt for resource."""
        resource = self.TestResource(logical_id="MyResource")
        get_att = resource.get_att("Arn")
        assert get_att.to_dict() == {"Fn::GetAtt": ["MyResource", "Arn"]}

    def test_resource_naming_pattern_override(self):
        """Test per-resource naming pattern override."""
        @dataclass
        class TestContext(DeploymentContext):
            pass

        ctx = TestContext(
            component="MyApp",
            stage="prod",
            naming_pattern="{component}-{resource_name}-{stage}"
        )
        resource = self.TestResource(
            context=ctx,
            logical_id="Special",
            naming_pattern="{resource_name}-custom"
        )
        assert resource.resource_name == "Special-custom"

    def test_resource_effective_logical_id_fallback(self):
        """Test effective_logical_id falls back to resource_name."""
        resource = self.TestResource()
        # Without logical_id, should use class name
        assert resource.effective_logical_id == "TestResource"

    def test_resource_with_update_replace_policy(self):
        """Test resource with UpdateReplacePolicy."""
        resource = self.TestResource(update_replace_policy="Snapshot")
        result = resource.to_dict()
        assert result["UpdateReplacePolicy"] == "Snapshot"
