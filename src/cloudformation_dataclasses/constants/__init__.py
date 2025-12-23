"""Shared constant mappings and runtime registries for code generation and linting.

This module re-exports from:
- maps.py: Immutable mapping dictionaries for operators, parameters, and types
- registry.py: Runtime functions for AWS module scanning and class lookup
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
