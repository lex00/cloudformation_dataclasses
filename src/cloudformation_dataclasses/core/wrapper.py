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

from dataclasses import MISSING, dataclass, fields, is_dataclass
from typing import Any, Generic, Type, TypeVar, get_type_hints

from cloudformation_dataclasses.core.base import CloudFormationResource

# Type variable for generic Ref/GetAtt type markers
T = TypeVar("T")


class Ref(Generic[T]):
    """
    Type marker for resource references using annotations.

    Used in type annotations to enable forward references with IDE support:

        @cloudformation_dataclass
        class BucketPolicy:
            resource: BucketPolicy
            bucket: Ref[Bucket] = ref()  # IDE sees Ref[Bucket], resolves at runtime

    With `from __future__ import annotations`, the annotation becomes a string
    and is evaluated later, avoiding import-time NameError for forward references.
    """

    pass


class GetAtt(Generic[T]):
    """
    Type marker for GetAtt references using annotations.

    Used in type annotations to enable forward references with IDE support:

        @cloudformation_dataclass
        class BucketArnOutput:
            resource: Output
            value: GetAtt[Bucket] = get_att("Arn")

    With `from __future__ import annotations`, the annotation becomes a string
    and is evaluated later, avoiding import-time NameError for forward references.
    """

    pass


def ref(wrapper_class: Type[Any] | str | None = None) -> DeferredRef:
    """
    Create a DeferredRef for use in wrapper dataclass field declarations.

    This function supports three usage patterns:

    1. Class reference (when class is available at definition time):
        bucket_name = ref(BucketName)  # Parameter refs work this way

    2. String reference (always works, but no IDE support):
        bucket = ref("Bucket")

    3. Annotation-based reference (recommended for cross-resource refs):
        bucket: Ref[Bucket] = ref()  # IDE support via type annotation

    The annotation-based pattern uses PEP 563 (`from __future__ import annotations`)
    to defer evaluation of the type annotation, avoiding NameError for forward refs.
    The actual class name is extracted from the annotation at resource creation time.

    Args:
        wrapper_class: The wrapper class, class name, or None (annotation-based)

    Returns:
        A DeferredRef that will be resolved during resource creation

    Example:
        >>> from cloudformation_dataclasses.core.wrapper import ref, Ref
        >>>
        >>> @cloudformation_dataclass
        >>> class MyVPC:
        >>>     resource: VPC
        >>>     cidr_block: str = "10.0.0.0/16"
        >>>
        >>> @cloudformation_dataclass
        >>> class MySubnet:
        >>>     resource: Subnet
        >>>     cidr_block: str = "10.0.1.0/24"
        >>>     vpc_id: Ref[MyVPC] = ref()  # Annotation-based cross-resource reference
    """
    if wrapper_class is None:
        # Annotation-based - logical_id will be extracted from type hint later
        return DeferredRef(logical_id=None)
    elif isinstance(wrapper_class, str):
        return DeferredRef(logical_id=wrapper_class)
    else:
        return DeferredRef(logical_id=wrapper_class.__name__)


def get_att(
    wrapper_class_or_attribute: Type[Any] | str, attribute: str | None = None
) -> DeferredGetAtt:
    """
    Create a DeferredGetAtt for use in wrapper dataclass field declarations.

    This function supports three usage patterns:

    1. Class reference (when class is available at definition time):
        value = get_att(MyInstance, "PublicIp")

    2. String reference (always works, but no IDE support):
        value = get_att("MyInstance", "PublicIp")

    3. Annotation-based reference (recommended for cross-resource refs):
        value: GetAtt[MyInstance] = get_att("PublicIp")  # IDE support via annotation

    Args:
        wrapper_class_or_attribute: The wrapper class, class name, or attribute name
            (if using annotation-based pattern)
        attribute: The CloudFormation attribute name (None for annotation-based)

    Returns:
        A DeferredGetAtt that will be resolved during resource creation
    """
    if attribute is None:
        # Annotation-based - first arg is the attribute name
        # logical_id will be extracted from type hint later
        return DeferredGetAtt(logical_id=None, attribute_name=str(wrapper_class_or_attribute))
    elif isinstance(wrapper_class_or_attribute, str):
        return DeferredGetAtt(logical_id=wrapper_class_or_attribute, attribute_name=attribute)
    else:
        return DeferredGetAtt(
            logical_id=wrapper_class_or_attribute.__name__, attribute_name=attribute
        )


@dataclass
class DeferredRef:
    """
    A deferred Ref that will be resolved when the wrapper is instantiated.

    The logical_id can be:
    - A string (class name or logical ID)
    - None (for annotation-based refs, resolved later from type hint)

    Example patterns:
        vpc_id = ref(MyVPC)           # logical_id = "MyVPC"
        vpc_id = ref("MyVPC")         # logical_id = "MyVPC"
        vpc_id: Ref[MyVPC] = ref()    # logical_id = None, resolved from annotation
    """

    logical_id: str | None = None

    def to_dict(self) -> dict[str, str]:
        """Serialize to CloudFormation JSON format."""
        if self.logical_id is None:
            raise ValueError(
                "DeferredRef.logical_id must be set before serialization. "
                "For annotation-based refs (bucket: Ref[Bucket] = ref()), "
                "the logical_id is resolved during resource creation."
            )
        return {"Ref": self.logical_id}


@dataclass
class DeferredGetAtt:
    """
    A deferred GetAtt that will be resolved when the wrapper is instantiated.

    The logical_id can be:
    - A string (class name or logical ID)
    - None (for annotation-based refs, resolved later from type hint)

    Example patterns:
        arn = get_att(MyBucket, "Arn")           # logical_id = "MyBucket"
        arn = get_att("MyBucket", "Arn")         # logical_id = "MyBucket"
        arn: GetAtt[MyBucket] = get_att("Arn")   # logical_id = None, resolved from annotation
    """

    logical_id: str | None = None
    attribute_name: str = ""

    def to_dict(self) -> dict[str, list[str]]:
        """Serialize to CloudFormation JSON format."""
        if self.logical_id is None:
            raise ValueError(
                "DeferredGetAtt.logical_id must be set before serialization. "
                "For annotation-based refs (arn: GetAtt[Bucket] = get_att('Arn')), "
                "the logical_id is resolved during resource creation."
            )
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
        # If get_type_hints fails (e.g., forward references can't be resolved),
        # fall back to checking raw annotations
        annotations = getattr(cls, "__annotations__", {})
        return "resource" in annotations or "context" in annotations


def cloudformation_dataclass(maybe_cls: Type[Any] | None = None, *, register: bool = True):
    """
    Decorator that enables the CloudFormation dataclass pattern.

    This decorator automatically applies @dataclass, so you only need @cloudformation_dataclass.
    It modifies the class so that the 'resource' or 'context' field has a default value.

    Resources are automatically registered with the global registry, enabling:
    - Multi-file template organization
    - Type-based queries (e.g., get all DynamoDB tables)
    - Automatic template building via Template.from_registry()

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
        register: If True (default), auto-register with global registry.
                  Only top-level CloudFormation resources are registered
                  (not PropertyTypes like BucketEncryption).

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
                hasattr(attr_value, "__class__")
                and not isinstance(attr_value, (str, int, float, bool, type(None)))
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
            try:
                type_hints = get_type_hints(cls)
                for field_name, field_type in type_hints.items():
                    if field_name in ("resource", "context"):
                        continue
                    # Check if the type is a wrapper dataclass
                    if isinstance(field_type, type) and is_wrapper_dataclass(field_type):
                        # Add None as default if no default exists
                        if not hasattr(cls, field_name):
                            setattr(cls, field_name, None)
            except Exception:
                # If we can't resolve type hints (e.g., forward references),
                # skip this optimization. It's not critical.
                pass

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

        # Auto-register if requested
        # Only register top-level CloudFormation resources (not PropertyTypes)
        if register:
            from cloudformation_dataclasses.core.registry import registry

            # Get the wrapped resource type
            wrapped_type = get_wrapped_resource_type(cls)
            if wrapped_type is not None:
                # Only register if the wrapped type has a resource_type attribute
                # This filters out PropertyTypes, PolicyDocument, etc.
                cf_type = getattr(wrapped_type, "resource_type", None)
                if cf_type:
                    registry.register(cls, cf_type)

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
        # Get the raw annotation (might be a string with PEP 563)
        annotations = getattr(cls, "__annotations__", {})

        # Determine which field to look up
        field_name = "resource" if "resource" in annotations else "context" if "context" in annotations else None
        if field_name is None:
            return None

        annotation = annotations[field_name]

        # If it's already a type, return it directly
        if isinstance(annotation, type):
            # Check for self-reference (wrapper class same name as resource class)
            if annotation is cls:
                return _find_aws_resource_class(annotation.__name__)
            return annotation

        # If it's a string (PEP 563), resolve it carefully
        if isinstance(annotation, str):
            import sys
            module = sys.modules.get(cls.__module__)
            if module:
                globalns = vars(module)

                # Handle dotted names like "s3.BucketPolicy"
                if "." in annotation:
                    try:
                        # Try to eval the dotted name in the module's globals
                        resolved = eval(annotation, globalns)
                        if isinstance(resolved, type):
                            return resolved
                    except Exception:
                        pass

                # Check if it's a simple name in globals
                if annotation in globalns:
                    resolved = globalns[annotation]
                    # Check for self-reference (e.g., class BucketPolicy with resource: BucketPolicy)
                    if resolved is cls:
                        # The annotation resolved to the wrapper class itself
                        # This means a local class shadows an imported AWS class
                        # Try to find the actual AWS resource class
                        return _find_aws_resource_class(annotation)
                    return resolved

                # Fall back to get_type_hints
                try:
                    type_hints = get_type_hints(cls, globalns=globalns)
                    resolved = type_hints.get(field_name)
                    if resolved is cls:
                        return _find_aws_resource_class(annotation)
                    return resolved
                except Exception:
                    pass

        return None
    except Exception:
        return None


def _find_aws_resource_class(class_name: str) -> Type[Any] | None:
    """Find an AWS resource class by name from cloudformation_dataclasses.aws modules."""
    try:
        # Search AWS modules for the class
        import cloudformation_dataclasses.aws as aws_pkg
        import pkgutil
        for finder, name, ispkg in pkgutil.iter_modules(aws_pkg.__path__):
            try:
                module = __import__(f"cloudformation_dataclasses.aws.{name}", fromlist=[class_name])
                if hasattr(module, class_name):
                    candidate = getattr(module, class_name)
                    # Make sure it's an actual CloudFormation resource class
                    # (has resource_type attribute)
                    if hasattr(candidate, "resource_type"):
                        return candidate
            except Exception:
                continue
    except Exception:
        pass
    return None


def _get_annotation_hints(wrapper_class: Type[Any]) -> dict[str, Any]:
    """
    Get type hints for a wrapper class, including registry classes for forward ref resolution.

    This enables annotation-based refs like `bucket: Ref[Bucket] = ref()` to be resolved
    even when Bucket is defined in a different module and uses auto-discovery.
    """
    import sys

    try:
        # Get the module globals for the wrapper class
        module = sys.modules.get(wrapper_class.__module__, None)
        globalns = vars(module) if module else {}

        # Include registry classes for forward reference resolution
        try:
            from cloudformation_dataclasses.core.registry import registry

            localns = {cls.__name__: cls for cls in registry.get_all()}
        except Exception:
            localns = {}

        return get_type_hints(wrapper_class, globalns=globalns, localns=localns)
    except Exception:
        # If we can't resolve hints, return empty dict
        # The ref will fail later with a clear error message
        return {}


def _resolve_ref_from_annotation(
    field_name: str, hints: dict[str, Any], expected_origin: type
) -> str | None:
    """
    Extract the target class name from a type annotation like Ref[Bucket] or GetAtt[Bucket].

    Args:
        field_name: The name of the field to look up
        hints: Type hints dict from get_type_hints()
        expected_origin: Either Ref or GetAtt class

    Returns:
        The logical ID (class name) or None if not resolvable
    """
    hint = hints.get(field_name)
    if hint is None:
        return None

    # Check if this is a generic like Ref[Bucket] or GetAtt[Bucket]
    origin = getattr(hint, "__origin__", None)
    if origin is not expected_origin:
        return None

    args = getattr(hint, "__args__", ())
    if not args:
        return None

    target = args[0]
    if isinstance(target, type):
        return target.__name__
    elif isinstance(target, str):
        return target
    else:
        return str(target)


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
    # Use raw annotations to avoid get_type_hints failure with forward references
    annotations = getattr(wrapper_class, "__annotations__", {})
    wrapper_field_name = "resource" if "resource" in annotations else "context"

    # Get type hints for resolving annotation-based refs
    # We need to include registry classes for forward reference resolution
    annotation_hints = _get_annotation_hints(wrapper_class)

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
            # Resolve annotation-based refs (logical_id is None)
            if value.logical_id is None:
                value.logical_id = _resolve_ref_from_annotation(
                    field.name, annotation_hints, Ref
                )
            kwargs[field.name] = value
        elif isinstance(value, DeferredGetAtt):
            # Resolve annotation-based refs (logical_id is None)
            if value.logical_id is None:
                value.logical_id = _resolve_ref_from_annotation(
                    field.name, annotation_hints, GetAtt
                )
            kwargs[field.name] = value
        elif isinstance(value, type) and is_wrapper_dataclass(value):
            # Value is a wrapper CLASS - instantiate it first, then unwrap
            nested_wrapper = value()
            kwargs[field.name] = create_wrapped_resource(nested_wrapper)
        elif isinstance(value, list):
            # Handle list of wrappers/deferred refs/tags
            # Special handling for Template dict fields - convert to dict with names
            from cloudformation_dataclasses.core.template import (
                Condition,
                Mapping,
                Output,
                Parameter,
                Template,
            )

            is_template_dict_field = (
                wrapped_type is Template
                and field.name in ("parameters", "outputs", "conditions", "mappings")
            )

            if is_template_dict_field:
                # Convert list to dict, using wrapper class names as keys
                result_dict: dict[str, Any] = {}
                for item in value:
                    if isinstance(item, type) and is_wrapper_dataclass(item):
                        # Item is a wrapper CLASS - instantiate and unwrap
                        name = item.__name__
                        nested_wrapper = item()
                        result_dict[name] = create_wrapped_resource(nested_wrapper)
                    elif is_wrapper_dataclass(type(item)):
                        # Item is a wrapper INSTANCE - get name from class and unwrap
                        name = type(item).__name__
                        result_dict[name] = create_wrapped_resource(item)
                    elif isinstance(item, (Parameter, Output, Condition, Mapping)):
                        # Already a concrete object - skip (can't infer name)
                        continue
                    else:
                        # Unknown type - skip
                        continue
                kwargs[field.name] = result_dict
            elif field.name == "depends_on":
                # depends_on: keep class references as-is, they'll be resolved in to_dict()
                kwargs[field.name] = value
            else:
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
