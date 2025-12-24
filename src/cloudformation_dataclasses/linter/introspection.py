"""Type introspection utilities for linting cloudformation_dataclasses code.

This module provides utilities to analyze type hints and extract enum classes,
PropertyType classes, and other type information needed for linting.

Key functions:
- get_enum_for_field(): Find enum class for a typed field
- get_enum_values(): Get constant names and values from enum-like classes
- find_enum_constant_for_value(): Reverse lookup from value to constant name
- get_property_type_for_field(): Find PropertyType class for a typed field
- is_property_type(): Check if a class is a PropertyType subclass
- get_module_for_class(): Extract AWS module name from class module path

These utilities support the linter's ability to suggest enum constants and
PropertyType wrappers instead of raw string values.
"""

from typing import Any, Optional, Union, get_args, get_origin, get_type_hints

from cloudformation_dataclasses.core.base import PropertyType


def get_enum_for_field(cls: type, field_name: str) -> Optional[type]:
    """Get the enum class valid for a field, if any.

    Examines the type hint for the field and extracts any enum class from a Union type.
    For example, Union[str, ServerSideEncryption, Ref] would return ServerSideEncryption.

    Args:
        cls: The class to inspect (e.g., ServerSideEncryptionByDefault)
        field_name: The field name to check (e.g., "sse_algorithm")

    Returns:
        The enum class if found, None otherwise
    """
    try:
        hints = get_type_hints(cls)
    except Exception:
        return None

    if field_name not in hints:
        return None

    type_hint = hints[field_name]
    return _extract_enum_from_type(type_hint, cls)


def _extract_enum_from_type(type_hint: Any, context_cls: type) -> Optional[type]:
    """Extract an enum class from a type hint.

    Args:
        type_hint: The type hint to analyze
        context_cls: The class containing this type hint (for module context)

    Returns:
        The enum class if found, None otherwise
    """
    origin = get_origin(type_hint)

    # Handle Optional[X] which is Union[X, None]
    if origin is Union:
        args = get_args(type_hint)
        for arg in args:
            enum_cls = _is_enum_class(arg, context_cls)
            if enum_cls is not None:
                return enum_cls

    # Direct type (not Union)
    enum_cls = _is_enum_class(type_hint, context_cls)
    if enum_cls is not None:
        return enum_cls

    return None


def _is_enum_class(cls: Any, context_cls: type) -> Optional[type]:
    """Check if a type is an enum-like class (simple class with string constants).

    Our "enum" classes are simple Python classes with class attributes that are strings.
    They are NOT Python Enum subclasses, and NOT PropertyType subclasses.

    Args:
        cls: The type to check
        context_cls: The class for module context

    Returns:
        The class if it's an enum class, None otherwise
    """
    # Skip None, str, and other built-in types
    if cls is None or cls is type(None) or cls is str:
        return None

    # Must be a class
    if not isinstance(cls, type):
        return None

    # Skip PropertyType subclasses
    try:
        if issubclass(cls, PropertyType):
            return None
    except TypeError:
        pass

    # Skip intrinsic function classes (Ref, GetAtt, Sub, etc.)
    module = getattr(cls, "__module__", "")
    if "intrinsics" in module:
        return None

    # Should be in an aws.* module (same as context or nearby)
    if not module.startswith("cloudformation_dataclasses.aws."):
        return None

    # Check if it has string class attributes (enum pattern)
    string_attrs = get_enum_values(cls)
    if not string_attrs:
        return None

    return cls


def get_enum_values(enum_class: type) -> dict[str, str]:
    """Get all string constant values from an enum-like class.

    Args:
        enum_class: The enum class to inspect

    Returns:
        Dict mapping attribute names to their string values
        Example: {"AES256": "AES256", "AWS_KMS": "aws:kms"}
    """
    values = {}
    for attr in dir(enum_class):
        if attr.startswith("_"):
            continue
        try:
            val = getattr(enum_class, attr)
            if isinstance(val, str):
                values[attr] = val
        except Exception:
            pass
    return values


def find_enum_constant_for_value(enum_class: type, value: str) -> Optional[str]:
    """Find the enum constant name that matches a given string value.

    Args:
        enum_class: The enum class to search
        value: The string value to find

    Returns:
        The constant name if found, None otherwise
        Example: find_enum_constant_for_value(ServerSideEncryption, "AES256") -> "AES256"
    """
    values = get_enum_values(enum_class)
    for const_name, const_value in values.items():
        if const_value == value:
            return const_name
    return None


def get_property_type_for_field(cls: type, field_name: str) -> Optional[type]:
    """Get the PropertyType class expected for a field.

    Args:
        cls: The class to inspect (e.g., Bucket)
        field_name: The field name to check (e.g., "bucket_encryption")

    Returns:
        The PropertyType subclass if found, None otherwise
    """
    try:
        hints = get_type_hints(cls)
    except Exception:
        return None

    if field_name not in hints:
        return None

    type_hint = hints[field_name]
    return _extract_property_type_from_type(type_hint)


def _extract_property_type_from_type(type_hint: Any) -> Optional[type]:
    """Extract a PropertyType class from a type hint.

    Args:
        type_hint: The type hint to analyze

    Returns:
        The PropertyType subclass if found, None otherwise
    """
    origin = get_origin(type_hint)

    # Handle Optional[X] which is Union[X, None]
    if origin is Union:
        args = get_args(type_hint)
        for arg in args:
            if _is_property_type_class(arg):
                return arg

    # Handle list[X]
    if origin is list:
        args = get_args(type_hint)
        if args and _is_property_type_class(args[0]):
            return args[0]

    # Direct type
    if _is_property_type_class(type_hint):
        return type_hint

    return None


def _is_property_type_class(cls: Any) -> bool:
    """Check if a type is a PropertyType subclass."""
    if not isinstance(cls, type):
        return False
    try:
        return issubclass(cls, PropertyType) and cls is not PropertyType
    except TypeError:
        return False


def is_property_type(cls: type) -> bool:
    """Check if a class is a PropertyType subclass.

    Args:
        cls: The class to check

    Returns:
        True if it's a PropertyType subclass, False otherwise
    """
    return _is_property_type_class(cls)


def get_module_for_class(cls: type) -> Optional[str]:
    """Get the module name for a class.

    Args:
        cls: The class to check

    Returns:
        The short module name (e.g., "s3" for cloudformation_dataclasses.aws.s3)
    """
    module = getattr(cls, "__module__", "")
    if module.startswith("cloudformation_dataclasses.aws."):
        return module.split(".")[-1]
    return None
