"""Shared constant mappings and runtime registries for code generation and linting.

This module provides mappings between CloudFormation string values and their
Python constant equivalents, plus utilities for looking up resource and property types.

**Mapping Dictionaries:**
- `CONDITION_OPERATOR_MAP`: "StringEquals" -> `STRING_EQUALS`
- `PARAMETER_TYPE_MAP`: "String" -> `STRING`
- `PSEUDO_PARAMETER_MAP`: "AWS::Region" -> `AWS_REGION`

**Registry Functions:**
- `resolve_resource_type`: Find the Python class for a CF resource type
- `get_all_resource_types`: List all available resource types
- `find_property_type_for_cf_keys`: Match property types by their fields

Example:
    >>> from cloudformation_dataclasses.constants import PSEUDO_PARAMETER_MAP
    >>> PSEUDO_PARAMETER_MAP["AWS::Region"]
    'AWS_REGION'
    >>>
    >>> from cloudformation_dataclasses.constants import resolve_resource_type
    >>> resolve_resource_type("AWS::S3::Bucket")
    ('cloudformation_dataclasses.aws.s3', 'Bucket')
"""

from cloudformation_dataclasses.constants.maps import (
    CONDITION_OPERATOR_MAP,
    CONDITION_OPERATOR_REVERSE_MAP,
    PARAMETER_TYPE_MAP,
    PARAMETER_TYPE_REVERSE_MAP,
    PSEUDO_PARAMETER_MAP,
    PSEUDO_PARAMETER_REVERSE_MAP,
)

from cloudformation_dataclasses.constants.registry import (
    CLASS_NAME_PATTERN,
    CLASS_WITH_PARENT_PATTERN,
    find_property_type_for_cf_keys,
    get_all_property_types,
    get_all_resource_types,
    get_class_modules,
    get_property_type_info,
    is_ambiguous_class_name,
    resolve_resource_type,
)

__all__ = [
    # Maps
    "CONDITION_OPERATOR_MAP",
    "CONDITION_OPERATOR_REVERSE_MAP",
    "PARAMETER_TYPE_MAP",
    "PARAMETER_TYPE_REVERSE_MAP",
    "PSEUDO_PARAMETER_MAP",
    "PSEUDO_PARAMETER_REVERSE_MAP",
    # Registry patterns
    "CLASS_NAME_PATTERN",
    "CLASS_WITH_PARENT_PATTERN",
    # Registry functions
    "find_property_type_for_cf_keys",
    "get_all_property_types",
    "get_all_resource_types",
    "get_class_modules",
    "get_property_type_info",
    "is_ambiguous_class_name",
    "resolve_resource_type",
]
