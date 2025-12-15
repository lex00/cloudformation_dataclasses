"""
Core base classes for CloudFormation resources.

This module provides the foundational classes that all CloudFormation resources inherit from:
- CloudFormationResource: Abstract base class for all AWS resources
- Tag: CloudFormation resource tag
- DeploymentContext: Environment configuration and naming context
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, ClassVar, Optional

if TYPE_CHECKING:
    from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref


@dataclass
class Tag:
    """
    CloudFormation resource tag.

    Can be used directly or as a wrapper dataclass base.

    Usage:
        # Direct usage (simple)
        tag = Tag(key="Environment", value="Production")

        # Wrapper usage (declarative)
        @dataclass
        @wrapper
        class EnvironmentTag:
            resource: Tag
            key: str = "Environment"
            value: str = "Production"

        tag = EnvironmentTag()
    """

    key: str
    value: str

    def to_dict(self) -> dict[str, str]:
        """Serialize tag to CloudFormation JSON format."""
        return {"Key": self.key, "Value": self.value}


@dataclass
class PolicyStatement:
    """
    IAM Policy Statement.

    Can be used directly or as a wrapper dataclass base for policy statements.

    Note: Uses 'resource_arn' instead of 'resource' to avoid naming conflicts
    with the wrapper pattern's 'resource:' field.
    """

    sid: Optional[str] = None
    effect: str = "Allow"
    principal: Any = None
    action: Any = None
    resource_arn: Any = None
    condition: Optional[dict[str, Any]] = None

    def to_dict(self) -> dict[str, Any]:
        """Serialize statement to IAM policy format."""
        stmt: dict[str, Any] = {"Effect": self.effect}

        if self.sid:
            stmt["Sid"] = self.sid
        if self.principal is not None:
            stmt["Principal"] = self.principal
        if self.action is not None:
            stmt["Action"] = self.action
        if self.resource_arn is not None:
            stmt["Resource"] = self.resource_arn
        if self.condition is not None:
            stmt["Condition"] = self.condition

        return stmt


@dataclass
class DenyStatement(PolicyStatement):
    """
    IAM Deny Policy Statement.

    Subclass of PolicyStatement with effect pre-set to "Deny".
    """

    effect: str = "Deny"


@dataclass
class PolicyDocument:
    """
    IAM Policy Document.

    Can be used directly or as a wrapper dataclass base for policy documents.
    """

    version: str = "2012-10-17"
    statement: list[Any] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Serialize policy document to IAM format."""
        return {
            "Version": self.version,
            "Statement": [
                s.to_dict() if hasattr(s, "to_dict") else s
                for s in self.statement
            ]
        }


@dataclass
class DeploymentContext(ABC):
    """
    Base class for deployment context - provides environment defaults and resource naming.

    The context supports automatic resource naming with a configurable pattern.
    Default pattern: {component}-{resource_name}-{stage}-{deployment_name}-{deployment_group}-{region}

    Parameters:
        component: Application or service component name (e.g., "DataPlatform", "APIGateway")
        stage: Deployment stage/environment (e.g., "dev", "staging", "prod")
        deployment_name: Unique deployment identifier (e.g., "001", "v2")
        deployment_group: For blue/green deployments - enables zero-downtime deployments (e.g., "blue", "green")
        region: AWS region for deployment (e.g., "us-east-1")
        naming_pattern: Custom naming pattern (default includes all parameters)

    Example (block syntax):
        @dataclass
        class MyDeploymentContext:
            context: DeploymentContext
            component: str = "DataPlatform"
            stage: str = "prod"
            deployment_name: str = "001"
            deployment_group: str = "blue"
            region: str = "us-east-1"

        ctx = MyDeploymentContext()
        # resource_name("MyData") -> "DataPlatform-MyData-prod-001-blue-us-east-1"

    Blue/Green deployments:
        ctx_blue = MyDeploymentContext(deployment_group="blue")
        ctx_green = MyDeploymentContext(deployment_group="green")
        # Creates separate resource sets for zero-downtime deployments

    The naming pattern can be customized per context or overridden per resource.
    """

    context_type: ClassVar[str]

    component: Optional[str] = None
    stage: Optional[str] = None
    deployment_name: Optional[str] = None
    deployment_group: Optional[str] = None
    region: Optional[str] = None
    account_id: Optional[str] = None
    project_name: Optional[str] = None
    naming_pattern: str = "{component}-{resource_name}-{stage}-{deployment_name}-{deployment_group}-{region}"
    tags: list[Tag] = field(default_factory=list)

    def resource_name(
        self,
        resource_class_name: str,
        pattern: Optional[str] = None
    ) -> str:
        """
        Generate AWS resource name from context and class name.

        Args:
            resource_class_name: The class name of the resource wrapper
            pattern: Optional custom naming pattern (overrides context pattern)

        Returns:
            Generated resource name string

        Example:
            >>> ctx.resource_name("MyData")
            "DataPlatform-MyData-prod-001-A-us-east-1"
            >>> ctx.resource_name("MyData", "{component}-{resource_name}")
            "DataPlatform-MyData"
        """
        naming_pattern = pattern or self.naming_pattern

        # Build context dict for formatting
        context_vars = {
            "component": self.component or "",
            "resource_name": resource_class_name,
            "stage": self.stage or "",
            "deployment_name": self.deployment_name or "",
            "deployment_group": self.deployment_group or "",
            "region": self.region or "",
        }

        # Format pattern and clean up empty parts
        formatted = naming_pattern.format(**context_vars)
        # Remove empty segments (multiple dashes, leading/trailing dashes)
        parts = [p for p in formatted.split("-") if p]
        return "-".join(parts)


@dataclass
class CloudFormationResource(ABC):
    """
    Abstract base class for all CloudFormation resources.

    All generated AWS resource classes inherit from this base class, which provides:
    - Logical ID management
    - Resource naming via context
    - Tag merging (context tags + resource-specific tags)
    - CloudFormation property serialization
    - Intrinsic function support (Ref, GetAtt)
    - Dependency tracking
    - Conditional resource creation
    - Deletion policy support

    Generated resource classes override:
    - resource_type: ClassVar[str] - The AWS CloudFormation resource type
    - Property fields with appropriate types and defaults
    """

    resource_type: ClassVar[str]

    logical_id: Optional[str] = None
    depends_on: list[str] = field(default_factory=list)
    condition: Optional[str] = None
    deletion_policy: Optional[str] = None
    update_replace_policy: Optional[str] = None
    metadata: Optional[dict[str, Any]] = None
    tags: list[Tag] = field(default_factory=list)
    context: Optional[DeploymentContext] = None
    naming_pattern: Optional[str] = None  # Override context naming pattern

    @property
    def resource_name(self) -> str:
        """
        Auto-generate resource name from context + class name.

        If context is provided, uses context.resource_name() with optional
        resource-specific naming_pattern override.

        Uses logical_id if set (which contains the wrapper class name),
        otherwise falls back to the resource class name.

        Returns:
            The generated or default resource name

        Example:
            # With context
            >>> bucket = MyData(context=ctx)
            >>> bucket.resource_name
            "DataPlatform-MyData-prod-001-A-us-east-1"

            # With custom pattern override
            >>> bucket = MyData(
            ...     context=ctx,
            ...     naming_pattern="{component}-{resource_name}"
            ... )
            >>> bucket.resource_name
            "DataPlatform-MyData"
        """
        if self.context:
            # Use logical_id if set (contains wrapper class name like "MyData")
            # Otherwise use resource class name (like "Bucket")
            class_name = self.logical_id if self.logical_id else self.__class__.__name__
            return self.context.resource_name(
                class_name,
                pattern=self.naming_pattern
            )
        return self.logical_id if self.logical_id else self.__class__.__name__

    @property
    def all_tags(self) -> list[Tag]:
        """
        Merge context tags with resource-specific tags.

        Context tags are applied first, then resource-specific tags.
        This allows resource tags to override context tags if needed.

        Returns:
            Combined list of tags from context and resource
        """
        resource_tags = self.tags if self.tags is not None else []
        if self.context:
            return self.context.tags + resource_tags
        return resource_tags

    @property
    def effective_logical_id(self) -> str:
        """
        Get the logical ID to use in CloudFormation template.

        Uses explicit logical_id if set, otherwise uses resource_name.

        Returns:
            The logical ID for this resource
        """
        return self.logical_id if self.logical_id else self.resource_name

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize resource to CloudFormation JSON format.

        This method must be implemented by generated resource classes to convert
        Python dataclass fields to CloudFormation property format.

        Returns:
            CloudFormation resource representation as dict

        Example output:
            {
                "Type": "AWS::S3::Bucket",
                "Properties": {
                    "BucketName": "my-bucket",
                    "VersioningConfiguration": {
                        "Status": "Enabled"
                    }
                }
            }
        """
        result: dict[str, Any] = {"Type": self.resource_type}

        # Add Properties section (implemented by subclasses)
        properties = self._get_properties()
        if properties:
            result["Properties"] = properties

        # Add optional CloudFormation resource attributes
        if self.depends_on:
            result["DependsOn"] = self.depends_on
        if self.condition:
            result["Condition"] = self.condition
        if self.deletion_policy:
            result["DeletionPolicy"] = self.deletion_policy
        if self.update_replace_policy:
            result["UpdateReplacePolicy"] = self.update_replace_policy
        if self.metadata:
            result["Metadata"] = self.metadata

        return result

    @abstractmethod
    def _get_properties(self) -> dict[str, Any]:
        """
        Get the Properties section of the CloudFormation resource.

        This is implemented by generated resource classes to serialize
        their specific properties.

        Returns:
            Dictionary of CloudFormation properties
        """
        ...

    def ref(self) -> Ref:
        """
        Create a Ref intrinsic function referencing this resource.

        Returns:
            Ref intrinsic function pointing to this resource's logical ID

        Example:
            >>> my_vpc = MyVPC()
            >>> subnet = MySubnet(vpc_id=my_vpc.ref())
        """
        from cloudformation_dataclasses.intrinsics.functions import Ref

        return Ref(logical_id=self.effective_logical_id)

    def get_att(self, attribute: str) -> GetAtt:
        """
        Create a GetAtt intrinsic function for a resource attribute.

        Args:
            attribute: The CloudFormation attribute name (PascalCase)

        Returns:
            GetAtt intrinsic function

        Example:
            >>> instance = MyInstance()
            >>> public_ip = instance.get_att("PublicIp")
        """
        from cloudformation_dataclasses.intrinsics.functions import GetAtt

        return GetAtt(logical_id=self.effective_logical_id, attribute_name=attribute)
