"""
CloudFormation dataclass pattern support for block syntax.

This module provides the mechanisms that enable the declarative block syntax
where resources are defined as CloudFormation dataclasses:

    @cloudformation_dataclass
    class MyBucket:
        resource: Bucket
        bucket_name: str = "my-bucket"

    my_bucket = MyBucket()  # No parameters needed!

The CloudFormation dataclass pattern allows all configuration to live in field
declarations rather than at instantiation time.
"""

from __future__ import annotations

from dataclasses import MISSING, Field, dataclass, field, fields, is_dataclass
from typing import Any, ClassVar, Type, get_type_hints

from cloudformation_dataclasses.core.base import CloudFormationResource, Tag


def ref(wrapper_class: Type[Any] | str) -> DeferredRef:
    """
    Create a DeferredRef for use in wrapper dataclass field declarations.

    This is a helper function that enables the block syntax pattern:
        @dataclass
        class MySubnet:
            resource: Subnet
            vpc_id: Any = ref(MyVPC)  # or ref("MyVPC")

    Args:
        wrapper_class: The wrapper class or class name to reference

    Returns:
        A DeferredRef that will be resolved during resource creation

    Example:
        >>> from cloudformation_dataclasses.core.wrapper import ref
        >>>
        >>> @dataclass
        >>> class MyVPC:
        >>>     resource: VPC
        >>>     cidr_block: str = "10.0.0.0/16"
        >>>
        >>> @dataclass
        >>> class MySubnet:
        >>>     resource: Subnet
        >>>     cidr_block: str = "10.0.1.0/24"
        >>>     vpc_id: Any = ref(MyVPC)  # Cross-resource reference
    """
    if isinstance(wrapper_class, str):
        logical_id = wrapper_class
    else:
        logical_id = wrapper_class.__name__

    return DeferredRef(logical_id=logical_id)


def get_att(wrapper_class: Type[Any] | str, attribute: str) -> DeferredGetAtt:
    """
    Create a DeferredGetAtt for use in wrapper dataclass field declarations.

    This enables the block syntax pattern:
        @dataclass
        class MyOutput:
            resource: Output
            value: Any = get_att(MyInstance, "PublicIp")

    Args:
        wrapper_class: The wrapper class or class name to reference
        attribute: The CloudFormation attribute name

    Returns:
        A DeferredGetAtt that will be resolved during resource creation
    """
    if isinstance(wrapper_class, str):
        logical_id = wrapper_class
    else:
        logical_id = wrapper_class.__name__

    return DeferredGetAtt(logical_id=logical_id, attribute_name=attribute)


@dataclass
class DeferredRef:
    """
    A deferred Ref that will be resolved when the wrapper is instantiated.

    This enables the pattern:
        @dataclass
        class MySubnet:
            resource: Subnet
            vpc_id: Any = field(default_factory=lambda: DeferredRef("MyVPC"))

    The DeferredRef is resolved to an actual Ref during wrapper instantiation.
    """

    logical_id: str

    def to_dict(self) -> dict[str, str]:
        """Serialize to CloudFormation JSON format."""
        return {"Ref": self.logical_id}


@dataclass
class DeferredGetAtt:
    """
    A deferred GetAtt that will be resolved when the wrapper is instantiated.

    This enables the pattern:
        @dataclass
        class MySubnet:
            resource: Subnet
            availability_zone: Any = field(default_factory=lambda: DeferredGetAtt("MyInstance", "AvailabilityZone"))
    """

    logical_id: str
    attribute_name: str

    def to_dict(self) -> dict[str, list[str]]:
        """Serialize to CloudFormation JSON format."""
        return {"Fn::GetAtt": [self.logical_id, self.attribute_name]}


def is_wrapper_dataclass(cls: Type[Any]) -> bool:
    """
    Check if a class is a wrapper dataclass (has a 'resource' or 'context' field).

    A wrapper dataclass wraps either:
    - CloudFormation resources/Tags via 'resource:' field
    - DeploymentContext via 'context:' field

    Args:
        cls: The class to check

    Returns:
        True if the class has a 'resource' or 'context' field annotation

    Examples:
        >>> @dataclass
        >>> class MyBucket:
        >>>     resource: Bucket
        >>>     bucket_name: str = "my-bucket"
        >>>
        >>> is_wrapper_dataclass(MyBucket)
        True

        >>> @dataclass
        >>> class MyDeploymentContext:
        >>>     context: DeploymentContext
        >>>     environment: str = "Prod"
        >>>
        >>> is_wrapper_dataclass(MyDeploymentContext)
        True
    """
    if not is_dataclass(cls):
        return False

    try:
        type_hints = get_type_hints(cls)
        return "resource" in type_hints or "context" in type_hints
    except Exception:
        return False


def cloudformation_dataclass(maybe_cls: Type[Any] | None = None):
    """
    Decorator that enables the CloudFormation dataclass pattern.

    This decorator automatically applies @dataclass, so you only need @cloudformation_dataclass.
    It modifies the class so that the 'resource' or 'context' field has a default value.

    Usage:
        >>> from cloudformation_dataclasses.core import cloudformation_dataclass
        >>> from cloudformation_dataclasses.aws.s3 import Bucket
        >>>
        >>> @cloudformation_dataclass
        >>> class MyBucket:
        >>>     resource: Bucket
        >>>     bucket_name: str = "my-bucket"
        >>>
        >>> bucket = MyBucket()  # Works! No 'resource' parameter needed

    Args:
        maybe_cls: The class to wrap (used when decorator is called without parens)

    Returns:
        The decorator function or the modified class
    """

    def decorator(cls: Type[Any]) -> Type[Any]:
        """Apply CloudFormation dataclass modifications to the class."""
        from dataclasses import dataclass as make_dataclass, field as dc_field

        # Detect and handle all defaults (both mutable and immutable)
        # Mutable defaults (lists, dicts) -> field(default_factory=...)
        # Immutable defaults (str, int, bool) -> add annotation so they become dataclass fields
        for attr_name in list(vars(cls).keys()):
            if attr_name.startswith("_"):
                continue

            attr_value = getattr(cls, attr_name, MISSING)
            if attr_value is MISSING:
                continue

            # Add type annotation if missing
            if not hasattr(cls, "__annotations__"):
                cls.__annotations__ = {}
            if attr_name not in cls.__annotations__:
                # Infer type from value
                if isinstance(attr_value, list):
                    cls.__annotations__[attr_name] = list
                elif isinstance(attr_value, dict):
                    cls.__annotations__[attr_name] = dict
                else:
                    cls.__annotations__[attr_name] = type(attr_value)

            # Check if this is a mutable default (list, dict, or class instance)
            if isinstance(attr_value, (list, dict)) or (
                hasattr(attr_value, "__class__") and
                not isinstance(attr_value, (str, int, float, bool, type(None)))
            ):
                # Convert to field(default_factory=...) to avoid mutable default error
                # Use a function to create proper closure for each value
                def make_factory(value):
                    return lambda: value

                setattr(cls, attr_name, dc_field(default_factory=make_factory(attr_value)))

        # Add a default to the 'resource' or 'context' field annotation
        # We do this by adding __annotations__ modification
        wrapper_field = None
        if hasattr(cls, "__annotations__"):
            if "resource" in cls.__annotations__:
                wrapper_field = "resource"
                if not hasattr(cls, "resource") or getattr(cls, "resource") is MISSING:
                    setattr(cls, "resource", None)
            elif "context" in cls.__annotations__:
                wrapper_field = "context"
                if not hasattr(cls, "context") or getattr(cls, "context") is MISSING:
                    setattr(cls, "context", None)

        # Handle fields whose type is a wrapper dataclass (like context: ProdDeploymentContext)
        # We need to give these fields defaults too
        if hasattr(cls, "__annotations__"):
            type_hints = get_type_hints(cls)
            for field_name, field_type in type_hints.items():
                if field_name in ("resource", "context"):
                    continue
                # Check if the type is a wrapper dataclass
                if isinstance(field_type, type) and is_wrapper_dataclass(field_type):
                    # Add None as default if no default exists
                    if not hasattr(cls, field_name):
                        setattr(cls, field_name, None)

        # Store original __post_init__ if it exists
        original_post_init = getattr(cls, "__post_init__", None)

        def __post_init__(self):
            """Auto-create wrapped resource/context during initialization."""
            # Determine which field to check
            if wrapper_field == "resource" and getattr(self, "resource", None) is None:
                self.resource = create_wrapped_resource(self)
            elif wrapper_field == "context" and getattr(self, "context", None) is None:
                self.context = create_wrapped_resource(self)

            # Call original __post_init__ if it existed
            if original_post_init is not None:
                original_post_init(self)

        # Add the __post_init__ method
        cls.__post_init__ = __post_init__

        # Apply @dataclass decorator
        cls = make_dataclass(cls)

        return cls

    # Handle both @cloudformation_dataclass and @cloudformation_dataclass() syntax
    if maybe_cls is None:
        # Called with parens: @cloudformation_dataclass()
        return decorator
    else:
        # Called without parens: @cloudformation_dataclass
        return decorator(maybe_cls)


def get_wrapped_resource_type(cls: Type[Any]) -> Type[Any] | None:
    """
    Get the wrapped type (CloudFormation resource, Tag, or DeploymentContext).

    Args:
        cls: A wrapper dataclass class

    Returns:
        The wrapped class (e.g., Bucket, VPC, Tag, DeploymentContext), or None if not a wrapper

    Examples:
        >>> @dataclass
        >>> class MyBucket:
        >>>     resource: Bucket
        >>>
        >>> get_wrapped_resource_type(MyBucket)
        <class 'Bucket'>

        >>> @dataclass
        >>> class MyDeploymentContext:
        >>>     context: DeploymentContext
        >>>
        >>> get_wrapped_resource_type(MyDeploymentContext)
        <class 'DeploymentContext'>
    """
    if not is_wrapper_dataclass(cls):
        return None

    try:
        type_hints = get_type_hints(cls)
        # Check for both 'resource' and 'context' fields
        if "resource" in type_hints:
            return type_hints["resource"]
        elif "context" in type_hints:
            return type_hints["context"]
        return None
    except Exception:
        return None


def create_wrapped_resource(wrapper_instance: Any) -> Any:
    """
    Create the underlying wrapped object from a wrapper instance.

    This function extracts all fields from the wrapper (except 'resource' or 'context')
    and uses them to instantiate the underlying wrapped object.

    Args:
        wrapper_instance: An instance of a wrapper dataclass

    Returns:
        An instance of the underlying wrapped object (CloudFormationResource, Tag, or DeploymentContext)

    Examples:
        >>> @dataclass
        >>> class MyBucket:
        >>>     resource: Bucket
        >>>     bucket_name: str = "my-bucket"
        >>>
        >>> wrapper = MyBucket()
        >>> bucket = create_wrapped_resource(wrapper)
        >>> isinstance(bucket, Bucket)
        True

        >>> @dataclass
        >>> class MyDeploymentContext:
        >>>     context: DeploymentContext
        >>>     environment: str = "Prod"
        >>>
        >>> wrapper = MyDeploymentContext()
        >>> ctx = create_wrapped_resource(wrapper)
        >>> isinstance(ctx, DeploymentContext)
        True
    """
    wrapper_class = type(wrapper_instance)
    wrapped_type = get_wrapped_resource_type(wrapper_class)

    if wrapped_type is None:
        raise TypeError(f"{wrapper_class.__name__} is not a wrapper dataclass")

    # Determine which field is the wrapper field
    wrapper_field_name = "resource" if "resource" in get_type_hints(wrapper_class) else "context"

    # Extract all fields except the wrapper field ('resource' or 'context')
    kwargs: dict[str, Any] = {}
    for field in fields(wrapper_instance):
        if field.name == wrapper_field_name:
            continue

        value = getattr(wrapper_instance, field.name)

        # Skip None values if the field has a default
        if value is None and field.default is not MISSING:
            continue
        if value is None and field.default_factory is not MISSING:  # type: ignore
            continue

        # Handle nested wrappers, deferred refs, and other values
        if isinstance(value, DeferredRef):
            # Convert DeferredRef to actual Ref
            # Keep as DeferredRef - it has to_dict() method for serialization
            kwargs[field.name] = value
        elif isinstance(value, DeferredGetAtt):
            # Convert DeferredGetAtt to actual GetAtt
            # Keep as DeferredGetAtt - it has to_dict() method for serialization
            kwargs[field.name] = value
        elif isinstance(value, type) and is_wrapper_dataclass(value):
            # Value is a wrapper CLASS - instantiate it first, then unwrap
            nested_wrapper = value()
            kwargs[field.name] = create_wrapped_resource(nested_wrapper)
        elif isinstance(value, list):
            # Handle list of wrappers/deferred refs/tags
            resolved_list = []
            for item in value:
                if isinstance(item, DeferredRef):
                    resolved_list.append(item)  # Keep as DeferredRef
                elif isinstance(item, DeferredGetAtt):
                    resolved_list.append(item)  # Keep as DeferredGetAtt
                elif isinstance(item, type) and is_wrapper_dataclass(item):
                    # Item is a wrapper CLASS - instantiate it first, then unwrap
                    nested_wrapper = item()
                    resolved_list.append(create_wrapped_resource(nested_wrapper))
                elif is_wrapper_dataclass(type(item)):
                    # Item is a wrapper INSTANCE - unwrap it
                    resolved_list.append(create_wrapped_resource(item))
                elif isinstance(item, dict) and field.name == "tags":
                    # Convert dict tags to Tag objects
                    from cloudformation_dataclasses.core.base import Tag
                    if "Key" in item and "Value" in item:
                        resolved_list.append(Tag(key=item["Key"], value=item["Value"]))
                    elif "key" in item and "value" in item:
                        resolved_list.append(Tag(key=item["key"], value=item["value"]))
                    else:
                        resolved_list.append(item)
                else:
                    resolved_list.append(item)
            kwargs[field.name] = resolved_list
        elif is_wrapper_dataclass(type(value)):
            # Handle single wrapper
            kwargs[field.name] = create_wrapped_resource(value)
        else:
            kwargs[field.name] = value

    # Instantiate the underlying wrapped object
    wrapped_instance = wrapped_type(**kwargs)

    # Set the logical_id to the wrapper class name for automatic name inference
    # This enables the pattern where class name becomes the CloudFormation logical ID
    # Example: class MyBucket -> logical ID "MyBucket" in template
    if isinstance(wrapped_instance, CloudFormationResource):
        # Always set logical_id to wrapper class name (not resource class name)
        # This is critical for the block syntax vision
        wrapped_instance.logical_id = wrapper_class.__name__

    return wrapped_instance
