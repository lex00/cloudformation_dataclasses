"""Shared constant mappings for code generation and linting.

These maps are used by both the importer (for code generation) and the linter
(for detecting and fixing common issues).
"""

# =============================================================================
# Condition Operator Mappings
# =============================================================================

# Map IAM condition operator strings to their Python constant names
CONDITION_OPERATOR_MAP: dict[str, str] = {
    # String conditions
    "StringEquals": "STRING_EQUALS",
    "StringNotEquals": "STRING_NOT_EQUALS",
    "StringEqualsIgnoreCase": "ConditionOperator.STRING_EQUALS_IGNORE_CASE",
    "StringNotEqualsIgnoreCase": "ConditionOperator.STRING_NOT_EQUALS_IGNORE_CASE",
    "StringLike": "STRING_LIKE",
    "StringNotLike": "STRING_NOT_LIKE",
    # Numeric conditions
    "NumericEquals": "ConditionOperator.NUMERIC_EQUALS",
    "NumericNotEquals": "ConditionOperator.NUMERIC_NOT_EQUALS",
    "NumericLessThan": "ConditionOperator.NUMERIC_LESS_THAN",
    "NumericLessThanEquals": "ConditionOperator.NUMERIC_LESS_THAN_EQUALS",
    "NumericGreaterThan": "ConditionOperator.NUMERIC_GREATER_THAN",
    "NumericGreaterThanEquals": "ConditionOperator.NUMERIC_GREATER_THAN_EQUALS",
    # Date conditions
    "DateEquals": "ConditionOperator.DATE_EQUALS",
    "DateNotEquals": "ConditionOperator.DATE_NOT_EQUALS",
    "DateLessThan": "ConditionOperator.DATE_LESS_THAN",
    "DateLessThanEquals": "ConditionOperator.DATE_LESS_THAN_EQUALS",
    "DateGreaterThan": "ConditionOperator.DATE_GREATER_THAN",
    "DateGreaterThanEquals": "ConditionOperator.DATE_GREATER_THAN_EQUALS",
    # Boolean
    "Bool": "BOOL",
    # Binary
    "BinaryEquals": "ConditionOperator.BINARY_EQUALS",
    # IP Address
    "IpAddress": "IP_ADDRESS",
    "NotIpAddress": "ConditionOperator.NOT_IP_ADDRESS",
    # ARN conditions
    "ArnEquals": "ARN_EQUALS",
    "ArnNotEquals": "ConditionOperator.ARN_NOT_EQUALS",
    "ArnLike": "ARN_LIKE",
    "ArnNotLike": "ConditionOperator.ARN_NOT_LIKE",
    # Null check
    "Null": "ConditionOperator.NULL",
    # IfExists variants
    "StringEqualsIfExists": "ConditionOperator.STRING_EQUALS_IF_EXISTS",
    "StringNotEqualsIfExists": "ConditionOperator.STRING_NOT_EQUALS_IF_EXISTS",
    "StringLikeIfExists": "ConditionOperator.STRING_LIKE_IF_EXISTS",
    "StringNotLikeIfExists": "ConditionOperator.STRING_NOT_LIKE_IF_EXISTS",
    "NumericEqualsIfExists": "ConditionOperator.NUMERIC_EQUALS_IF_EXISTS",
    "BoolIfExists": "ConditionOperator.BOOL_IF_EXISTS",
    "IpAddressIfExists": "ConditionOperator.IP_ADDRESS_IF_EXISTS",
    "ArnEqualsIfExists": "ConditionOperator.ARN_EQUALS_IF_EXISTS",
    "ArnLikeIfExists": "ConditionOperator.ARN_LIKE_IF_EXISTS",
    # ForAllValues and ForAnyValue set operators
    "ForAllValues:StringEquals": "ConditionOperator.FOR_ALL_VALUES_STRING_EQUALS",
    "ForAllValues:StringLike": "ConditionOperator.FOR_ALL_VALUES_STRING_LIKE",
    "ForAnyValue:StringEquals": "ConditionOperator.FOR_ANY_VALUE_STRING_EQUALS",
    "ForAnyValue:StringLike": "ConditionOperator.FOR_ANY_VALUE_STRING_LIKE",
    "ForAllValues:ArnLike": "ConditionOperator.FOR_ALL_VALUES_ARN_LIKE",
    "ForAnyValue:ArnLike": "ConditionOperator.FOR_ANY_VALUE_ARN_LIKE",
}

# Reverse map: constant name -> string value (for linting)
CONDITION_OPERATOR_REVERSE_MAP: dict[str, str] = {v: k for k, v in CONDITION_OPERATOR_MAP.items()}


# =============================================================================
# Pseudo-Parameter Mappings
# =============================================================================

# Map AWS pseudo-parameter strings to their Python constant names
PSEUDO_PARAMETER_MAP: dict[str, str] = {
    "AWS::AccountId": "AWS_ACCOUNT_ID",
    "AWS::NotificationARNs": "AWS_NOTIFICATION_ARNS",
    "AWS::NoValue": "AWS_NO_VALUE",
    "AWS::Partition": "AWS_PARTITION",
    "AWS::Region": "AWS_REGION",
    "AWS::StackId": "AWS_STACK_ID",
    "AWS::StackName": "AWS_STACK_NAME",
    "AWS::URLSuffix": "AWS_URL_SUFFIX",
}

# Reverse map: constant name -> pseudo-parameter string
PSEUDO_PARAMETER_REVERSE_MAP: dict[str, str] = {v: k for k, v in PSEUDO_PARAMETER_MAP.items()}


# =============================================================================
# Parameter Type Mappings
# =============================================================================

# Map CloudFormation parameter type strings to their Python constant names
PARAMETER_TYPE_MAP: dict[str, str] = {
    # Basic types
    "String": "STRING",
    "Number": "NUMBER",
    "List<Number>": "ParameterType.LIST_NUMBER",
    "CommaDelimitedList": "ParameterType.COMMA_DELIMITED_LIST",
    # EC2 types
    "AWS::EC2::AvailabilityZone::Name": "ParameterType.AWS_EC2_AVAILABILITY_ZONE_NAME",
    "AWS::EC2::Image::Id": "ParameterType.AWS_EC2_IMAGE_ID",
    "AWS::EC2::Instance::Id": "ParameterType.AWS_EC2_INSTANCE_ID",
    "AWS::EC2::KeyPair::KeyName": "ParameterType.AWS_EC2_KEY_PAIR_KEY_NAME",
    "AWS::EC2::SecurityGroup::GroupName": "ParameterType.AWS_EC2_SECURITY_GROUP_GROUP_NAME",
    "AWS::EC2::SecurityGroup::Id": "ParameterType.AWS_EC2_SECURITY_GROUP_ID",
    "AWS::EC2::Subnet::Id": "ParameterType.AWS_EC2_SUBNET_ID",
    "AWS::EC2::Volume::Id": "ParameterType.AWS_EC2_VOLUME_ID",
    "AWS::EC2::VPC::Id": "ParameterType.AWS_EC2_VPC_ID",
    # Route53
    "AWS::Route53::HostedZone::Id": "ParameterType.AWS_ROUTE53_HOSTED_ZONE_ID",
    # List types
    "List<AWS::EC2::AvailabilityZone::Name>": "ParameterType.LIST_AWS_EC2_AVAILABILITY_ZONE_NAME",
    "List<AWS::EC2::Image::Id>": "ParameterType.LIST_AWS_EC2_IMAGE_ID",
    "List<AWS::EC2::Instance::Id>": "ParameterType.LIST_AWS_EC2_INSTANCE_ID",
    "List<AWS::EC2::SecurityGroup::GroupName>": (
        "ParameterType.LIST_AWS_EC2_SECURITY_GROUP_GROUP_NAME"
    ),
    "List<AWS::EC2::SecurityGroup::Id>": "ParameterType.LIST_AWS_EC2_SECURITY_GROUP_ID",
    "List<AWS::EC2::Subnet::Id>": "ParameterType.LIST_AWS_EC2_SUBNET_ID",
    "List<AWS::EC2::Volume::Id>": "ParameterType.LIST_AWS_EC2_VOLUME_ID",
    "List<AWS::EC2::VPC::Id>": "ParameterType.LIST_AWS_EC2_VPC_ID",
    "List<AWS::Route53::HostedZone::Id>": "ParameterType.LIST_AWS_ROUTE53_HOSTED_ZONE_ID",
    # SSM types
    "AWS::SSM::Parameter::Name": "ParameterType.AWS_SSM_PARAMETER_NAME",
    "AWS::SSM::Parameter::Value<String>": "ParameterType.AWS_SSM_PARAMETER_VALUE_STRING",
    "AWS::SSM::Parameter::Value<List<String>>": (
        "ParameterType.AWS_SSM_PARAMETER_VALUE_LIST_STRING"
    ),
    "AWS::SSM::Parameter::Value<CommaDelimitedList>": (
        "ParameterType.AWS_SSM_PARAMETER_VALUE_COMMA_DELIMITED_LIST"
    ),
}

# Reverse map: constant name -> parameter type string
PARAMETER_TYPE_REVERSE_MAP: dict[str, str] = {v: k for k, v in PARAMETER_TYPE_MAP.items()}


# =============================================================================
# Resource Type Registry
# =============================================================================

import importlib
import os
import re
from pathlib import Path
from typing import Any, Optional

# Cache for resource type mappings
_RESOURCE_TYPE_MAP: dict[str, tuple[str, str]] = {}
_RESOURCE_TYPE_MAP_BUILT = False


def _build_resource_type_map() -> None:
    """Build mapping from CloudFormation types to Python classes by scanning aws modules."""
    global _RESOURCE_TYPE_MAP, _RESOURCE_TYPE_MAP_BUILT
    if _RESOURCE_TYPE_MAP_BUILT:
        return

    _RESOURCE_TYPE_MAP_BUILT = True

    # Find the aws directory
    try:
        import cloudformation_dataclasses.aws as aws_pkg
        aws_dir = Path(aws_pkg.__file__).parent
    except (ImportError, AttributeError):
        return

    # Pattern to find resource_type class variable assignments
    resource_type_pattern = re.compile(
        r'resource_type:\s*ClassVar\[str\]\s*=\s*["\']([^"\']+)["\']'
    )
    class_name_pattern = re.compile(r'^class\s+(\w+)\s*\(')

    # Scan all .py files in the aws directory
    for py_file in aws_dir.glob("*.py"):
        if py_file.name.startswith("_"):
            continue

        module_name = py_file.stem  # e.g., "iam", "s3", "ec2"

        try:
            content = py_file.read_text()
        except Exception:
            continue

        # Find all class definitions and their resource_type
        current_class = None
        for line in content.split("\n"):
            class_match = class_name_pattern.match(line)
            if class_match:
                current_class = class_match.group(1)
                continue

            if current_class:
                type_match = resource_type_pattern.search(line)
                if type_match:
                    resource_type = type_match.group(1)
                    _RESOURCE_TYPE_MAP[resource_type] = (module_name, current_class)


def resolve_resource_type(resource_type: str) -> Optional[tuple[str, str]]:
    """
    Resolve a CloudFormation resource type to Python module and class.

    Args:
        resource_type: CloudFormation resource type (e.g., "AWS::S3::Bucket")

    Returns:
        Tuple of (module_name, class_name) or None if unknown.
        module_name is relative to cloudformation_dataclasses.aws
    """
    _build_resource_type_map()
    return _RESOURCE_TYPE_MAP.get(resource_type)


def get_all_resource_types() -> dict[str, tuple[str, str]]:
    """Get all known resource types and their Python mappings."""
    _build_resource_type_map()
    return _RESOURCE_TYPE_MAP.copy()


# =============================================================================
# PropertyType Registry
# =============================================================================

# Stores information about PropertyType classes for code generation
# Structure: {
#   (module_name, class_name): {
#       "cf_to_python": {"CFPropertyName": "python_field_name"},
#       "python_to_cf": {"python_field_name": "CFPropertyName"},
#       "field_types": {"python_field_name": "type_annotation_string"},
#   }
# }
_PROPERTY_TYPE_MAP: dict[tuple[str, str], dict[str, Any]] = {}
_PROPERTY_TYPE_MAP_BUILT = False

# Reverse lookup: CloudFormation property name -> list of (module, class) that use it
# Used for quick lookups when we see a CF property name in a dict
_CF_PROPERTY_TO_CLASSES: dict[str, list[tuple[str, str]]] = {}


def _build_property_type_map() -> None:
    """Build mapping of PropertyType classes and their field information."""
    global _PROPERTY_TYPE_MAP, _PROPERTY_TYPE_MAP_BUILT, _CF_PROPERTY_TO_CLASSES
    if _PROPERTY_TYPE_MAP_BUILT:
        return

    _PROPERTY_TYPE_MAP_BUILT = True

    # Find the aws directory
    try:
        import cloudformation_dataclasses.aws as aws_pkg
        aws_dir = Path(aws_pkg.__file__).parent
    except (ImportError, AttributeError):
        return

    # Patterns for parsing
    class_pattern = re.compile(r'^class\s+(\w+)\s*\(\s*(\w+)\s*\)')
    property_mappings_pattern = re.compile(
        r'_property_mappings:\s*ClassVar\[dict\[str,\s*str\]\]\s*=\s*\{([^}]+)\}'
    )
    field_pattern = re.compile(r'^\s+(\w+):\s*(.+?)\s*(?:=|$)')
    mapping_entry_pattern = re.compile(r'"(\w+)":\s*"(\w+)"')

    # Scan all .py files in the aws directory
    for py_file in aws_dir.glob("*.py"):
        if py_file.name.startswith("_"):
            continue

        module_name = py_file.stem

        try:
            content = py_file.read_text()
        except Exception:
            continue

        # Parse the file to find PropertyType classes
        current_class: Optional[str] = None
        current_parent: Optional[str] = None
        current_mappings: dict[str, str] = {}
        current_fields: dict[str, str] = {}
        in_class = False

        lines = content.split("\n")
        for i, line in enumerate(lines):
            # Check for class definition
            class_match = class_pattern.match(line)
            if class_match:
                # Save previous class if it was a PropertyType
                if current_class and current_parent == "PropertyType" and current_mappings:
                    key = (module_name, current_class)
                    cf_to_python = {v: k for k, v in current_mappings.items()}
                    _PROPERTY_TYPE_MAP[key] = {
                        "cf_to_python": cf_to_python,
                        "python_to_cf": current_mappings.copy(),
                        "field_types": current_fields.copy(),
                    }
                    # Add to reverse lookup
                    for cf_name in cf_to_python:
                        if cf_name not in _CF_PROPERTY_TO_CLASSES:
                            _CF_PROPERTY_TO_CLASSES[cf_name] = []
                        _CF_PROPERTY_TO_CLASSES[cf_name].append(key)

                current_class = class_match.group(1)
                current_parent = class_match.group(2)
                current_mappings = {}
                current_fields = {}
                in_class = True
                continue

            if not in_class or not current_class:
                continue

            # Check for _property_mappings
            if "_property_mappings" in line:
                # Try to find the full mapping (may span multiple lines)
                mapping_text = line
                j = i
                while "}" not in mapping_text and j < len(lines) - 1:
                    j += 1
                    mapping_text += lines[j]
                # Extract all mappings
                for match in mapping_entry_pattern.finditer(mapping_text):
                    python_name, cf_name = match.groups()
                    current_mappings[python_name] = cf_name
                continue

            # Check for field type annotations
            field_match = field_pattern.match(line)
            if field_match:
                field_name, type_annotation = field_match.groups()
                if not field_name.startswith("_"):
                    current_fields[field_name] = type_annotation

        # Don't forget the last class
        if current_class and current_parent == "PropertyType" and current_mappings:
            key = (module_name, current_class)
            cf_to_python = {v: k for k, v in current_mappings.items()}
            _PROPERTY_TYPE_MAP[key] = {
                "cf_to_python": cf_to_python,
                "python_to_cf": current_mappings.copy(),
                "field_types": current_fields.copy(),
            }
            for cf_name in cf_to_python:
                if cf_name not in _CF_PROPERTY_TO_CLASSES:
                    _CF_PROPERTY_TO_CLASSES[cf_name] = []
                _CF_PROPERTY_TO_CLASSES[cf_name].append(key)


def get_property_type_info(
    module: str, class_name: str
) -> Optional[dict[str, Any]]:
    """
    Get information about a PropertyType class.

    Args:
        module: Module name (e.g., "s3")
        class_name: Class name (e.g., "BucketEncryption")

    Returns:
        Dict with cf_to_python, python_to_cf, and field_types mappings,
        or None if not found.
    """
    _build_property_type_map()
    return _PROPERTY_TYPE_MAP.get((module, class_name))


def find_property_type_for_cf_keys(
    cf_keys: set[str], module_hint: Optional[str] = None
) -> Optional[tuple[str, str]]:
    """
    Find a PropertyType class that matches a set of CloudFormation property keys.

    Args:
        cf_keys: Set of CloudFormation property names from a dict
        module_hint: Optional module name to prefer (e.g., "s3").
                     If provided, ONLY matches from that module are considered.

    Returns:
        Tuple of (module_name, class_name) or None if no match.
    """
    _build_property_type_map()

    # Find candidates that have at least one matching key
    candidates: dict[tuple[str, str], int] = {}
    for key in cf_keys:
        if key in _CF_PROPERTY_TO_CLASSES:
            for class_key in _CF_PROPERTY_TO_CLASSES[key]:
                # If we have a module hint, skip classes from other modules
                if module_hint and class_key[0] != module_hint:
                    continue
                candidates[class_key] = candidates.get(class_key, 0) + 1

    if not candidates:
        return None

    # Score candidates: prefer classes where ALL provided keys are valid
    best_matches: list[tuple[tuple[str, str], float, int]] = []
    for class_key, match_count in candidates.items():
        info = _PROPERTY_TYPE_MAP[class_key]
        total_keys = len(info["cf_to_python"])
        expected_keys = set(info["cf_to_python"].keys())

        # Check if all provided keys are in the expected set
        all_match = cf_keys.issubset(expected_keys)
        if not all_match:
            # Penalize partial matches heavily
            continue

        # Score: ratio of matched keys to total keys (higher is better, more specific)
        specificity = match_count / total_keys if total_keys > 0 else 0
        best_matches.append((class_key, specificity, total_keys))

    if not best_matches:
        return None

    # Sort by specificity desc (prefer more specific matches)
    best_matches.sort(key=lambda x: (-x[1], x[2]))

    return best_matches[0][0] if best_matches else None


def get_all_property_types() -> dict[tuple[str, str], dict[str, Any]]:
    """Get all known PropertyType classes and their information."""
    _build_property_type_map()
    return _PROPERTY_TYPE_MAP.copy()
