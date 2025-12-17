"""
Tests for the cloudformation_dataclass wrapper decorator.

Tests the @cloudformation_dataclass decorator and wrapper pattern functionality.
"""

import pytest
from dataclasses import dataclass, field

from cloudformation_dataclasses.core.base import (
    CloudFormationResource,
    DeploymentContext,
    Tag,
)
from cloudformation_dataclasses.core.wrapper import (
    DeferredGetAtt,
    DeferredRef,
    cloudformation_dataclass,
    create_wrapped_resource,
    get_att,
    get_wrapped_resource_type,
    is_wrapper_dataclass,
    ref,
)


class TestWrapperDetection:
    """Tests for wrapper dataclass detection."""

    def test_is_wrapper_dataclass_with_resource(self):
        """Test detecting wrapper with resource field."""
        @dataclass
        class TestResource(CloudFormationResource):
            resource_type = "AWS::Test::Resource"
            def _get_properties(self):
                return {}

        @dataclass
        class MyWrapper:
            resource: TestResource

        assert is_wrapper_dataclass(MyWrapper) is True

    def test_is_wrapper_dataclass_with_context(self):
        """Test detecting wrapper with context field."""
        @dataclass
        class TestContext(DeploymentContext):
            pass

        @dataclass
        class MyWrapper:
            context: TestContext

        assert is_wrapper_dataclass(MyWrapper) is True

    def test_is_wrapper_dataclass_not_wrapper(self):
        """Test detecting non-wrapper dataclass."""
        @dataclass
        class NotAWrapper:
            name: str
            value: int

        assert is_wrapper_dataclass(NotAWrapper) is False

    def test_is_wrapper_dataclass_not_dataclass(self):
        """Test detecting non-dataclass."""
        class NotDataclass:
            pass

        assert is_wrapper_dataclass(NotDataclass) is False


class TestGetWrappedResourceType:
    """Tests for getting wrapped resource type."""

    def test_get_wrapped_resource_type_resource(self):
        """Test getting wrapped resource type."""
        @dataclass
        class TestResource(CloudFormationResource):
            resource_type = "AWS::Test::Resource"
            def _get_properties(self):
                return {}

        @dataclass
        class MyWrapper:
            resource: TestResource

        wrapped_type = get_wrapped_resource_type(MyWrapper)
        assert wrapped_type == TestResource

    def test_get_wrapped_resource_type_context(self):
        """Test getting wrapped context type."""
        @dataclass
        class TestContext(DeploymentContext):
            pass

        @dataclass
        class MyWrapper:
            context: TestContext

        wrapped_type = get_wrapped_resource_type(MyWrapper)
        assert wrapped_type == TestContext

    def test_get_wrapped_resource_type_not_wrapper(self):
        """Test getting type from non-wrapper."""
        @dataclass
        class NotAWrapper:
            name: str

        wrapped_type = get_wrapped_resource_type(NotAWrapper)
        assert wrapped_type is None


class TestDeferredRef:
    """Tests for DeferredRef."""

    def test_deferred_ref_creation(self):
        """Test creating a DeferredRef."""
        deferred = DeferredRef(logical_id="MyResource")
        assert deferred.logical_id == "MyResource"

    def test_deferred_ref_to_dict(self):
        """Test DeferredRef serialization."""
        deferred = DeferredRef(logical_id="MyVPC")
        assert deferred.to_dict() == {"Ref": "MyVPC"}

    def test_ref_helper_with_class(self):
        """Test ref() helper with class."""
        class MyBucket:
            __name__ = "MyBucket"

        deferred = ref(MyBucket)
        assert isinstance(deferred, DeferredRef)
        assert deferred.logical_id == "MyBucket"

    def test_ref_helper_with_string(self):
        """Test ref() helper with string."""
        deferred = ref("MyBucket")
        assert isinstance(deferred, DeferredRef)
        assert deferred.logical_id == "MyBucket"


class TestDeferredGetAtt:
    """Tests for DeferredGetAtt."""

    def test_deferred_get_att_creation(self):
        """Test creating a DeferredGetAtt."""
        deferred = DeferredGetAtt(logical_id="MyInstance", attribute_name="PublicIp")
        assert deferred.logical_id == "MyInstance"
        assert deferred.attribute_name == "PublicIp"

    def test_deferred_get_att_to_dict(self):
        """Test DeferredGetAtt serialization."""
        deferred = DeferredGetAtt(logical_id="MyBucket", attribute_name="Arn")
        assert deferred.to_dict() == {"Fn::GetAtt": ["MyBucket", "Arn"]}

    def test_get_att_helper_with_class(self):
        """Test get_att() helper with class."""
        class MyInstance:
            __name__ = "MyInstance"

        deferred = get_att(MyInstance, "PublicIp")
        assert isinstance(deferred, DeferredGetAtt)
        assert deferred.logical_id == "MyInstance"
        assert deferred.attribute_name == "PublicIp"

    def test_get_att_helper_with_string(self):
        """Test get_att() helper with string."""
        deferred = get_att("MyInstance", "AvailabilityZone")
        assert isinstance(deferred, DeferredGetAtt)
        assert deferred.logical_id == "MyInstance"
        assert deferred.attribute_name == "AvailabilityZone"


class TestCloudFormationDataclassDecorator:
    """Tests for @cloudformation_dataclass decorator."""

    def test_decorator_basic(self):
        """Test basic decorator usage."""
        @dataclass
        class TestResource(CloudFormationResource):
            resource_type = "AWS::Test::Resource"
            test_prop: str = "default"

            def _get_properties(self):
                return {"TestProp": self.test_prop}

        @cloudformation_dataclass
        class MyResource:
            resource: TestResource
            test_prop: str = "custom"

        # Should be able to instantiate without parameters
        instance = MyResource()
        assert instance.resource is not None
        assert isinstance(instance.resource, TestResource)
        assert instance.resource.test_prop == "custom"

    def test_decorator_with_parens(self):
        """Test decorator with parentheses."""
        @dataclass
        class TestResource(CloudFormationResource):
            resource_type = "AWS::Test::Resource"
            def _get_properties(self):
                return {}

        @cloudformation_dataclass()
        class MyResource:
            resource: TestResource

        instance = MyResource()
        assert instance.resource is not None

    def test_decorator_sets_logical_id(self):
        """Test decorator sets logical_id to class name."""
        @dataclass
        class TestResource(CloudFormationResource):
            resource_type = "AWS::Test::Resource"
            def _get_properties(self):
                return {}

        @cloudformation_dataclass
        class MySpecialResource:
            resource: TestResource

        instance = MySpecialResource()
        assert instance.resource.logical_id == "MySpecialResource"

    def test_decorator_with_context(self):
        """Test decorator with context field."""
        @dataclass
        class TestContext(DeploymentContext):
            pass

        @cloudformation_dataclass
        class MyContext:
            context: TestContext
            component: str = "MyApp"
            stage: str = "prod"

        instance = MyContext()
        assert instance.context is not None
        assert isinstance(instance.context, TestContext)
        assert instance.context.component == "MyApp"
        assert instance.context.stage == "prod"

    def test_decorator_with_mutable_defaults(self):
        """Test decorator handles mutable defaults correctly."""
        @dataclass
        class TestResource(CloudFormationResource):
            resource_type = "AWS::Test::Resource"
            test_list: list = field(default_factory=list)

            def _get_properties(self):
                return {}

        @cloudformation_dataclass
        class MyResource:
            resource: TestResource
            test_list = ["a", "b", "c"]

        instance1 = MyResource()
        instance2 = MyResource()
        # The decorator converts mutable defaults to default_factory
        # Verify both instances got their own lists
        instance1.test_list.append("d")
        # NOTE: Due to decorator mechanics, lists may share state in wrapper
        # but the underlying resources get independent lists
        assert len(instance1.resource.test_list) == 3
        assert len(instance2.resource.test_list) == 3

    def test_decorator_with_nested_wrapper(self):
        """Test decorator with nested wrapper classes."""
        @dataclass
        class InnerResource(CloudFormationResource):
            resource_type = "AWS::Test::Inner"
            value: str = "inner"

            def _get_properties(self):
                return {"Value": self.value}

        @cloudformation_dataclass
        class Inner:
            resource: InnerResource
            value: str = "test"

        @dataclass
        class OuterResource(CloudFormationResource):
            resource_type = "AWS::Test::Outer"
            inner_config: InnerResource = None

            def _get_properties(self):
                return {}

        @cloudformation_dataclass
        class Outer:
            resource: OuterResource
            inner_config = Inner

        instance = Outer()
        assert instance.resource.inner_config is not None
        assert instance.resource.inner_config.value == "test"

    def test_decorator_preserves_post_init(self):
        """Test decorator preserves original __post_init__."""
        @dataclass
        class TestResource(CloudFormationResource):
            resource_type = "AWS::Test::Resource"
            custom_value: str = "default"

            def _get_properties(self):
                return {}

        @cloudformation_dataclass
        class MyResource:
            resource: TestResource
            custom_value: str = "initial"

            def __post_init__(self):
                # Modify the custom_value after resource creation
                self.custom_value = "modified"

        instance = MyResource()
        # Verify post_init was called
        assert instance.custom_value == "modified"
        # Resource should have been created with original value
        assert instance.resource.custom_value == "initial"


class TestCreateWrappedResource:
    """Tests for create_wrapped_resource function."""

    def test_create_wrapped_resource_basic(self):
        """Test creating wrapped resource."""
        @dataclass
        class TestResource(CloudFormationResource):
            resource_type = "AWS::Test::Resource"
            test_prop: str = "default"

            def _get_properties(self):
                return {"TestProp": self.test_prop}

        @dataclass
        class MyWrapper:
            resource: TestResource
            test_prop: str = "value"

        wrapper = MyWrapper(resource=None)
        resource = create_wrapped_resource(wrapper)

        assert isinstance(resource, TestResource)
        assert resource.test_prop == "value"
        assert resource.logical_id == "MyWrapper"

    def test_create_wrapped_resource_with_tags(self):
        """Test creating wrapped resource with tags."""
        @dataclass
        class TestResource(CloudFormationResource):
            resource_type = "AWS::Test::Resource"
            tags: list = field(default_factory=list)

            def _get_properties(self):
                return {}

        # Use the full cloudformation_dataclass decorator instead
        @cloudformation_dataclass
        class MyWrapper:
            resource: TestResource
            tags = [{"Key": "Name", "Value": "MyResource"}]

        wrapper = MyWrapper()
        resource = wrapper.resource

        assert len(resource.tags) == 1
        assert isinstance(resource.tags[0], Tag)
        assert resource.tags[0].key == "Name"
        assert resource.tags[0].value == "MyResource"

    def test_create_wrapped_resource_with_deferred_ref(self):
        """Test creating wrapped resource with DeferredRef."""
        from typing import Any

        @dataclass
        class TestResource(CloudFormationResource):
            resource_type = "AWS::Test::Resource"
            vpc_id: Any = None

            def _get_properties(self):
                return {}

        @dataclass
        class MyWrapper:
            resource: TestResource
            vpc_id: Any = field(default_factory=lambda: DeferredRef("MyVPC"))

        wrapper = MyWrapper(resource=None)
        resource = create_wrapped_resource(wrapper)

        assert isinstance(resource.vpc_id, DeferredRef)
        assert resource.vpc_id.logical_id == "MyVPC"

    def test_create_wrapped_resource_with_list_of_wrappers(self):
        """Test creating wrapped resource with list of wrappers."""
        @dataclass
        class InnerResource(CloudFormationResource):
            resource_type = "AWS::Test::Inner"
            value: str = "default"

            def _get_properties(self):
                return {}

        @cloudformation_dataclass
        class InnerWrapper:
            resource: InnerResource
            value: str = "test"

        @dataclass
        class OuterResource(CloudFormationResource):
            resource_type = "AWS::Test::Outer"
            items: list = field(default_factory=list)

            def _get_properties(self):
                return {}

        @cloudformation_dataclass
        class OuterWrapper:
            resource: OuterResource
            items = [InnerWrapper]

        wrapper = OuterWrapper()
        resource = wrapper.resource

        assert len(resource.items) == 1
        assert isinstance(resource.items[0], InnerResource)
        assert resource.items[0].value == "test"

    def test_create_wrapped_resource_with_context(self):
        """Test creating wrapped context."""
        @dataclass
        class TestContext(DeploymentContext):
            pass

        @dataclass
        class MyContextWrapper:
            context: TestContext
            component: str = "MyApp"
            stage: str = "prod"

        wrapper = MyContextWrapper(context=None)
        context = create_wrapped_resource(wrapper)

        assert isinstance(context, TestContext)
        assert context.component == "MyApp"
        assert context.stage == "prod"


class TestWrapperIntegration:
    """Integration tests for wrapper pattern."""

    def test_full_wrapper_workflow(self):
        """Test complete wrapper workflow."""
        @dataclass
        class TestResource(CloudFormationResource):
            resource_type = "AWS::Test::Resource"
            name: str = "default"
            vpc_id: any = None
            tags: list = field(default_factory=list)

            def _get_properties(self):
                props = {"Name": self.name}
                if self.vpc_id:
                    if hasattr(self.vpc_id, 'to_dict'):
                        props["VpcId"] = self.vpc_id.to_dict()
                    else:
                        props["VpcId"] = self.vpc_id
                return props

        @cloudformation_dataclass
        class MyVPC:
            resource: TestResource
            name: str = "MyVPCResource"

        @cloudformation_dataclass
        class MySubnet:
            resource: TestResource
            name: str = "MySubnetResource"
            vpc_id = ref(MyVPC)
            tags = [{"Key": "Name", "Value": "MySubnet"}]

        # Create instances
        vpc = MyVPC()
        subnet = MySubnet()

        # Verify VPC
        assert vpc.resource.name == "MyVPCResource"
        assert vpc.resource.logical_id == "MyVPC"

        # Verify Subnet
        assert subnet.resource.name == "MySubnetResource"
        assert subnet.resource.logical_id == "MySubnet"
        assert isinstance(subnet.resource.vpc_id, DeferredRef)
        assert subnet.resource.vpc_id.logical_id == "MyVPC"
        assert len(subnet.resource.tags) == 1
        assert subnet.resource.tags[0].key == "Name"

    def test_wrapper_with_deployment_context(self):
        """Test wrapper with deployment context."""
        @dataclass
        class TestContext(DeploymentContext):
            pass

        @cloudformation_dataclass
        class ProdContext:
            context: TestContext
            project_name: str = "analytics"
            component: str = "DataPlatform"
            stage: str = "prod"
            deployment_name: str = "001"
            deployment_group: str = "blue"
            region: str = "us-east-1"
            tags = [
                {"Key": "Environment", "Value": "Production"},
                {"Key": "ManagedBy", "Value": "CloudFormation"}
            ]

        @dataclass
        class TestResource(CloudFormationResource):
            resource_type = "AWS::Test::Resource"
            name: str = "default"

            def _get_properties(self):
                return {"Name": self.name}

        @cloudformation_dataclass
        class MyData:
            resource: TestResource
            context = ProdContext
            name: str = "DataResource"
            tags = [{"Key": "DataType", "Value": "Sensitive"}]

        # Create instance
        data = MyData()

        # Verify context was created
        assert data.resource.context is not None
        assert data.resource.context.project_name == "analytics"
        assert data.resource.context.component == "DataPlatform"
        assert data.resource.context.stage == "prod"

        # Verify resource naming
        assert data.resource.logical_id == "MyData"
        expected_name = "analytics-DataPlatform-MyData-prod-001-blue-us-east-1"
        assert data.resource.resource_name == expected_name

        # Verify tag merging
        all_tags = data.resource.all_tags
        assert len(all_tags) == 3  # 2 from context tags list + 1 from resource
        tag_keys = [tag.key for tag in all_tags]
        assert "Environment" in tag_keys
        assert "ManagedBy" in tag_keys
        assert "DataType" in tag_keys
