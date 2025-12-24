"""
Core base classes for CloudFormation resources.

This module provides the foundational classes that all CloudFormation resources inherit from:
- CloudFormationResource: Abstract base class for all AWS resources
- PropertyType: Base class for CloudFormation property types (nested structures)
- Tag: CloudFormation resource tag
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, ClassVar, Optional, Union

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

        # With intrinsic function
        tag = Tag(key="Name", value=Ref("MyResource"))

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
    value: Any  # Can be str or intrinsic function

    def to_dict(self) -> dict[str, Any]:
        """Serialize tag to CloudFormation JSON format."""
        value = self.value.to_dict() if hasattr(self.value, "to_dict") else self.value
        return {"Key": self.key, "Value": value}


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

    def _serialize_value(self, value: Any) -> Any:
        """Recursively serialize a value for CloudFormation JSON.

        Args:
            value: Any value that may need serialization.

        Returns:
            The serialized value suitable for CloudFormation JSON.
        """
        # Handle objects with to_dict() method (intrinsic functions, etc.)
        if hasattr(value, "to_dict"):
            return value.to_dict()

        # Handle lists recursively
        if isinstance(value, list):
            return [self._serialize_value(item) for item in value]

        # Handle dicts recursively
        if isinstance(value, dict):
            return {key: self._serialize_value(val) for key, val in value.items()}

        # Return primitive values as-is
        return value

    def to_dict(self) -> dict[str, Any]:
        """Serialize statement to IAM policy format.

        Returns:
            IAM policy statement as a dict.
        """
        stmt: dict[str, Any] = {"Effect": self.effect}

        if self.sid:
            stmt["Sid"] = self.sid
        if self.principal is not None:
            stmt["Principal"] = self._serialize_value(self.principal)
        if self.action is not None:
            stmt["Action"] = self._serialize_value(self.action)
        if self.resource_arn is not None:
            stmt["Resource"] = self._serialize_value(self.resource_arn)
        if self.condition is not None:
            stmt["Condition"] = self._serialize_value(self.condition)

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
            "Statement": [s.to_dict() if hasattr(s, "to_dict") else s for s in self.statement],
        }


@dataclass
class PropertyType:
    """
    Base class for CloudFormation property types (nested structures).

    Generated property type classes inherit from this to get data-driven serialization.
    Each subclass defines _property_mappings to map field names to CF property names.
    """

    _property_mappings: ClassVar[dict[str, str]] = {}

    def _serialize_value(self, value: Any) -> Any:
        """Recursively serialize a value for CloudFormation JSON.

        Args:
            value: Any value that may need serialization.

        Returns:
            The serialized value suitable for CloudFormation JSON.
        """
        if hasattr(value, "to_dict"):
            return value.to_dict()
        if isinstance(value, list):
            return [self._serialize_value(item) for item in value]
        if isinstance(value, dict):
            return {key: self._serialize_value(val) for key, val in value.items()}
        return value

    def to_dict(self) -> dict[str, Any]:
        """Serialize to CloudFormation format using _property_mappings.

        Returns:
            Dict of CloudFormation property names to serialized values.
        """
        props: dict[str, Any] = {}
        for field_name, cf_name in self.__class__._property_mappings.items():
            value = getattr(self, field_name, None)
            if value is not None:
                props[cf_name] = self._serialize_value(value)
        return props


@dataclass
class CloudFormationResource(ABC):
    """
    Abstract base class for all CloudFormation resources.

    All generated AWS resource classes inherit from this base class, which provides:
    - Logical ID management
    - CloudFormation property serialization
    - Intrinsic function support (Ref, GetAtt)
    - Dependency tracking
    - Conditional resource creation
    - Deletion policy support

    Generated resource classes override:
    - resource_type: ClassVar[str] - The AWS CloudFormation resource type
    - _property_mappings: ClassVar[dict[str, str]] - Maps field names to CF property names
    - Property fields with appropriate types and defaults
    """

    resource_type: ClassVar[str]
    _property_mappings: ClassVar[dict[str, str]] = {}

    logical_id: Optional[str] = None
    depends_on: list[Union[str, type]] = field(default_factory=list)
    condition: Optional[str] = None
    deletion_policy: Optional[str] = None
    update_replace_policy: Optional[str] = None
    metadata: Optional[dict[str, Any]] = None
    tags: list[Tag] = field(default_factory=list)

    @property
    def resource_name(self) -> str:
        """
        Get the resource name.

        Uses logical_id if set (which contains the wrapper class name),
        otherwise falls back to the resource class name.

        Returns:
            The resource name
        """
        return self.logical_id if self.logical_id else self.__class__.__name__

    @property
    def all_tags(self) -> list[Tag]:
        """
        Get all tags for this resource.

        Returns:
            List of tags
        """
        return self.tags if self.tags is not None else []

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
            # Resolve class references to their logical IDs (class names)
            resolved_deps = []
            for dep in self.depends_on:
                if isinstance(dep, type):
                    resolved_deps.append(dep.__name__)
                else:
                    resolved_deps.append(dep)
            result["DependsOn"] = resolved_deps
        if self.condition:
            result["Condition"] = self.condition
        if self.deletion_policy:
            result["DeletionPolicy"] = self.deletion_policy
        if self.update_replace_policy:
            result["UpdateReplacePolicy"] = self.update_replace_policy
        if self.metadata:
            result["Metadata"] = self.metadata

        return result

    def _serialize_value(self, value: Any) -> Any:
        """Recursively serialize a value for CloudFormation JSON.

        Args:
            value: Any value that may need serialization.

        Returns:
            The serialized value suitable for CloudFormation JSON.
        """
        if hasattr(value, "to_dict"):
            return value.to_dict()
        if isinstance(value, list):
            return [self._serialize_value(item) for item in value]
        if isinstance(value, dict):
            return {key: self._serialize_value(val) for key, val in value.items()}
        return value

    def _get_properties(self) -> dict[str, Any]:
        """
        Get the Properties section of the CloudFormation resource.

        Uses _property_mappings to serialize fields to CloudFormation format.
        Handles intrinsic functions, nested property types, and lists automatically.

        Returns:
            Dictionary of CloudFormation properties
        """
        props: dict[str, Any] = {}
        mappings = self.__class__._property_mappings

        for field_name, cf_name in mappings.items():
            # Special case: tags field uses all_tags
            if field_name == "tags":
                value = self.all_tags
            else:
                value = getattr(self, field_name, None)

            if value is not None:
                props[cf_name] = self._serialize_value(value)

        return props

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
