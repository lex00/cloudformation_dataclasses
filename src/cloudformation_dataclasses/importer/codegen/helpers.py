"""Helper utilities and constants for code generation.

This module provides utility functions and mappings used throughout
the code generation process:

- Class name sanitization and validation
- Service category mapping for file organization
- Tag class name generation
- PropertyType resolution and type hint parsing
- Enum value lookup

Constants:
- SERVICE_CATEGORIES: Map AWS services to category files
- KNOWN_ENUMS: Map enum classes to their value-to-constant mappings
"""

import re
from typing import Any, Optional

from cloudformation_dataclasses.constants import (
    find_property_type_for_cf_keys,
    get_property_type_info,
)
from cloudformation_dataclasses.importer.ir import IRResource


# =============================================================================
# Service Category Mapping for Resource File Organization
# =============================================================================

# Map AWS service names to category files for large templates (10+ resources)
SERVICE_CATEGORIES: dict[str, str] = {
    # Compute
    "EC2": "compute",
    "Lambda": "compute",
    "ECS": "compute",
    "EKS": "compute",
    "Batch": "compute",
    "AutoScaling": "compute",
    "ElasticBeanstalk": "compute",
    "Lightsail": "compute",
    # Storage
    "S3": "storage",
    "EFS": "storage",
    "FSx": "storage",
    "Backup": "storage",
    # Database
    "RDS": "database",
    "DynamoDB": "database",
    "ElastiCache": "database",
    "Neptune": "database",
    "DocumentDB": "database",
    "Redshift": "database",
    "MemoryDB": "database",
    # Networking
    "ElasticLoadBalancing": "network",
    "ElasticLoadBalancingV2": "network",
    "Route53": "network",
    "CloudFront": "network",
    "APIGateway": "network",
    "ApiGatewayV2": "network",
    "GlobalAccelerator": "network",
    # Security/IAM
    "IAM": "security",
    "Cognito": "security",
    "SecretsManager": "security",
    "KMS": "security",
    "WAF": "security",
    "WAFv2": "security",
    "ACM": "security",
    "SSM": "security",
    # Messaging/Integration
    "SNS": "messaging",
    "SQS": "messaging",
    "EventBridge": "messaging",
    "Events": "messaging",
    "StepFunctions": "messaging",
    "AppSync": "messaging",
    # Monitoring/Logging
    "CloudWatch": "monitoring",
    "Logs": "monitoring",
    "CloudTrail": "monitoring",
    "XRay": "monitoring",
    # CI/CD
    "CodeBuild": "cicd",
    "CodePipeline": "cicd",
    "CodeCommit": "cicd",
    "CodeDeploy": "cicd",
    # Infrastructure
    "CloudFormation": "infra",
    "Config": "infra",
    "ServiceCatalog": "infra",
}

# EC2 resource types that should go to network.py instead of compute.py
EC2_NETWORK_TYPES: set[str] = {
    "VPC",
    "Subnet",
    "InternetGateway",
    "NatGateway",
    "RouteTable",
    "Route",
    "SecurityGroup",
    "NetworkAcl",
    "VPCEndpoint",
    "EIP",
    "VPCGatewayAttachment",
    "SubnetRouteTableAssociation",
    "NetworkInterface",
    "VPNGateway",
    "VPNConnection",
    "CustomerGateway",
    "TransitGateway",
    "TransitGatewayAttachment",
}


def get_resource_category(resource: IRResource) -> str:
    """Get the category file for a resource based on its AWS service.

    Returns 'main' for uncategorized services, or a category name like
    'compute', 'storage', 'network', etc.
    """
    service = resource.service

    # Special case: EC2 VPC-related resources go to network
    if service == "EC2" and resource.type_name in EC2_NETWORK_TYPES:
        return "network"

    return SERVICE_CATEGORIES.get(service, "main")


# =============================================================================
# Name Sanitization
# =============================================================================


# Import from shared module
from cloudformation_dataclasses.core.naming import sanitize_class_name


# =============================================================================
# PropertyType Resolution
# =============================================================================


def resolve_property_type(
    expected_class: Optional[str],
    expected_module: Optional[str],
    cf_keys: Optional[set[str]] = None,
    module_hint: Optional[str] = None,
) -> Optional[tuple[str, str, dict[str, Any]]]:
    """
    Resolve a PropertyType by expected class/module or by CF property keys.

    First tries to match using expected_class and expected_module.
    If that fails, falls back to searching by CF property keys.

    Args:
        expected_class: Expected class name from type hint
        expected_module: Expected module name from type hint
        cf_keys: Set of CloudFormation property names in the dict
        module_hint: Module hint for key-based lookup (e.g., "ec2")

    Returns:
        Tuple of (module_name, class_name, property_type_info) or None if not found.
    """
    # Try expected class first
    if expected_class and expected_module:
        info = get_property_type_info(expected_module, expected_class)
        if info:
            return (expected_module, expected_class, info)

    # Fall back to key-based lookup
    if cf_keys:
        match = find_property_type_for_cf_keys(cf_keys, module_hint=module_hint)
        if match:
            pt_module, pt_class = match
            info = get_property_type_info(pt_module, pt_class)
            if info:
                return (pt_module, pt_class, info)

    return None


# =============================================================================
# Known Enum Mappings
# =============================================================================

# Known enum mappings: (module, enum_class) -> {string_value: constant_name}
# Used during code generation to convert string literals to enum references
KNOWN_ENUMS: dict[tuple[str, str], dict[str, str]] = {
    # S3 enums
    ("s3", "ServerSideEncryption"): {
        "AES256": "AES256",
        "aws:kms": "AWS_KMS",
        "aws:kms:dsse": "AWS_KMS_DSSE",
    },
    ("s3", "BucketVersioningStatus"): {
        "Enabled": "ENABLED",
        "Suspended": "SUSPENDED",
    },
    ("s3", "ObjectLockEnabled"): {
        "Enabled": "ENABLED",
    },
    ("s3", "ObjectLockMode"): {
        "COMPLIANCE": "COMPLIANCE",
        "GOVERNANCE": "GOVERNANCE",
    },
    ("s3", "ObjectLockRetentionMode"): {
        "COMPLIANCE": "COMPLIANCE",
        "GOVERNANCE": "GOVERNANCE",
    },
    ("s3", "ReplicationRuleStatus"): {
        "Enabled": "ENABLED",
        "Disabled": "DISABLED",
    },
    # DynamoDB enums
    ("dynamodb", "KeyType"): {
        "HASH": "HASH",
        "RANGE": "RANGE",
    },
    ("dynamodb", "AttributeType"): {
        "S": "S",
        "N": "N",
        "B": "B",
    },
    ("dynamodb", "BillingMode"): {
        "PROVISIONED": "PROVISIONED",
        "PAY_PER_REQUEST": "PAY_PER_REQUEST",
    },
    ("dynamodb", "ProjectionType"): {
        "ALL": "ALL",
        "KEYS_ONLY": "KEYS_ONLY",
        "INCLUDE": "INCLUDE",
    },
    ("dynamodb", "StreamViewType"): {
        "KEYS_ONLY": "KEYS_ONLY",
        "NEW_IMAGE": "NEW_IMAGE",
        "OLD_IMAGE": "OLD_IMAGE",
        "NEW_AND_OLD_IMAGES": "NEW_AND_OLD_IMAGES",
    },
    # Lambda enums
    ("lambda_", "Runtime"): {
        "python3.8": "PYTHON3_8",
        "python3.9": "PYTHON3_9",
        "python3.10": "PYTHON3_10",
        "python3.11": "PYTHON3_11",
        "python3.12": "PYTHON3_12",
        "python3.13": "PYTHON3_13",
        "nodejs18.x": "NODEJS18_X",
        "nodejs20.x": "NODEJS20_X",
        "nodejs22.x": "NODEJS22_X",
    },
}


# Known type wrapper names to skip when extracting class names
_SKIP_TYPE_NAMES = frozenset({
    "Optional", "Union", "Any", "Ref", "GetAtt", "Sub", "ClassVar",
    "List", "Dict", "Set", "Tuple", "Callable", "Sequence", "Mapping",
    "list", "dict", "set", "tuple", "bool", "str", "int", "float",
})


def extract_class_from_type_hint(type_hint: Optional[str]) -> Optional[str]:
    """
    Extract a PropertyType class name from a type annotation string.

    Args:
        type_hint: Type annotation like "Optional[BucketEncryption]" or
                   "Optional[list[ServerSideEncryptionRule]]"

    Returns:
        Class name (e.g., "BucketEncryption") or None if no class found.
    """
    if not type_hint:
        return None

    # Find all PascalCase identifiers in the type hint
    for match in re.finditer(r"\b([A-Z][a-zA-Z0-9]*)\b", type_hint):
        class_name = match.group(1)
        if class_name not in _SKIP_TYPE_NAMES:
            return class_name

    return None


def extract_enum_from_type_hint(type_hint: str) -> Optional[tuple[str, str]]:
    """
    Extract enum class name from a type annotation string.

    Args:
        type_hint: Type annotation like "Optional[Union[str, ServerSideEncryption, Ref, ...]]"

    Returns:
        Tuple of (module, enum_class) if found, None otherwise.
    """
    # Look for known enum class names in the type hint
    for (module, enum_class), _ in KNOWN_ENUMS.items():
        if enum_class in type_hint:
            return (module, enum_class)
    return None


# =============================================================================
# Tag Utilities
# =============================================================================


def tag_class_name(key: str, value: str) -> str:
    """Generate a class name for a tag."""
    from cloudformation_dataclasses.core.naming import to_pascal_case

    return f"{to_pascal_case(key)}{to_pascal_case(value)}Tag"


def tag_signature(tag: dict[str, Any]) -> str:
    """Get the signature for a tag (Key:Value)."""
    return f"{tag.get('Key', '')}:{tag.get('Value', '')}"


# =============================================================================
# Logical ID Utilities
# =============================================================================


def logical_id_to_filename(logical_id: str) -> str:
    """Convert LogicalId to snake_case filename (without .py extension)."""
    from cloudformation_dataclasses.core.naming import to_snake_case

    return to_snake_case(logical_id)
