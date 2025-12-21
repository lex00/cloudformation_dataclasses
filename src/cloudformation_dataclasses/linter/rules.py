"""Lint rules for cloudformation_dataclasses code.

Each rule detects a specific pattern that can be improved and provides
suggestions for better alternatives.
"""

import ast
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from cloudformation_dataclasses.constants import (
    CONDITION_OPERATOR_MAP,
    PARAMETER_TYPE_MAP,
    PSEUDO_PARAMETER_MAP,
)


@dataclass
class LintIssue:
    """A detected lint issue."""

    rule_id: str
    message: str
    line: int
    column: int
    original: str
    suggestion: str
    # For auto-fixing
    fix_imports: list[str]  # Imports to add (e.g., ["from cloudformation_dataclasses.core.constants import BOOL"])


@dataclass
class LintContext:
    """Context for linting, including source code and AST."""

    source: str
    tree: ast.AST
    filename: str = "<unknown>"


class LintRule(ABC):
    """Base class for lint rules."""

    rule_id: str
    description: str

    @abstractmethod
    def check(self, context: LintContext) -> list[LintIssue]:
        """Check code for issues matching this rule."""
        pass


class StringShouldBeConditionOperator(LintRule):
    """Detect IAM condition operators as string literals.

    Detects: {"Bool": {...}, "StringEquals": {...}}
    Suggests: {BOOL: {...}, STRING_EQUALS: {...}}
    """

    rule_id = "CFD001"
    description = "Use condition operator constants instead of string literals"

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            # Look for dict literals with string keys
            if isinstance(node, ast.Dict):
                for key in node.keys:
                    if isinstance(key, ast.Constant) and isinstance(key.value, str):
                        operator_str = key.value
                        if operator_str in CONDITION_OPERATOR_MAP:
                            constant_name = CONDITION_OPERATOR_MAP[operator_str]
                            # Determine the import needed
                            if "." in constant_name:
                                # ConditionOperator.X - need full import
                                import_stmt = "from cloudformation_dataclasses.core.constants import ConditionOperator"
                            else:
                                # Short alias like BOOL, STRING_EQUALS
                                import_stmt = f"from cloudformation_dataclasses.core.constants import {constant_name}"

                            issues.append(
                                LintIssue(
                                    rule_id=self.rule_id,
                                    message=f"Use {constant_name} instead of '{operator_str}'",
                                    line=key.lineno,
                                    column=key.col_offset,
                                    original=f'"{operator_str}"',
                                    suggestion=constant_name,
                                    fix_imports=[import_stmt],
                                )
                            )

        return issues


class StringShouldBeParameterType(LintRule):
    """Detect parameter types as string literals.

    Detects: type = "String", type = "Number"
    Suggests: type = STRING, type = NUMBER
    """

    rule_id = "CFD002"
    description = "Use parameter type constants instead of string literals"

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            # Look for assignments to 'type' attribute
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "type":
                        if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                            type_str = node.value.value
                            if type_str in PARAMETER_TYPE_MAP:
                                constant_name = PARAMETER_TYPE_MAP[type_str]
                                if "." in constant_name:
                                    import_stmt = (
                                        "from cloudformation_dataclasses.core.constants import ParameterType"
                                    )
                                else:
                                    import_stmt = (
                                        f"from cloudformation_dataclasses.core.constants import {constant_name}"
                                    )

                                issues.append(
                                    LintIssue(
                                        rule_id=self.rule_id,
                                        message=f"Use {constant_name} instead of '{type_str}'",
                                        line=node.value.lineno,
                                        column=node.value.col_offset,
                                        original=f'"{type_str}"',
                                        suggestion=constant_name,
                                        fix_imports=[import_stmt],
                                    )
                                )

            # Also check keyword arguments in function/class calls
            if isinstance(node, ast.Call):
                for keyword in node.keywords:
                    if keyword.arg == "type":
                        if isinstance(keyword.value, ast.Constant) and isinstance(keyword.value.value, str):
                            type_str = keyword.value.value
                            if type_str in PARAMETER_TYPE_MAP:
                                constant_name = PARAMETER_TYPE_MAP[type_str]
                                if "." in constant_name:
                                    import_stmt = (
                                        "from cloudformation_dataclasses.core.constants import ParameterType"
                                    )
                                else:
                                    import_stmt = (
                                        f"from cloudformation_dataclasses.core.constants import {constant_name}"
                                    )

                                issues.append(
                                    LintIssue(
                                        rule_id=self.rule_id,
                                        message=f"Use {constant_name} instead of '{type_str}'",
                                        line=keyword.value.lineno,
                                        column=keyword.value.col_offset,
                                        original=f'"{type_str}"',
                                        suggestion=constant_name,
                                        fix_imports=[import_stmt],
                                    )
                                )

        return issues


class RefShouldBePseudoParameter(LintRule):
    """Detect Ref() calls with pseudo-parameters that should use constants.

    Detects: Ref("AWS::Region"), Ref("AWS::StackName")
    Suggests: AWS_REGION, AWS_STACK_NAME
    """

    rule_id = "CFD003"
    description = "Use pseudo-parameter constants instead of Ref() with string literals"

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            if isinstance(node, ast.Call):
                # Check if it's a Ref() call
                func = node.func
                is_ref = False
                if isinstance(func, ast.Name) and func.id == "Ref":
                    is_ref = True
                elif isinstance(func, ast.Attribute) and func.attr == "Ref":
                    is_ref = True

                if is_ref and node.args:
                    arg = node.args[0]
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        pseudo_param = arg.value
                        if pseudo_param in PSEUDO_PARAMETER_MAP:
                            constant_name = PSEUDO_PARAMETER_MAP[pseudo_param]
                            import_stmt = (
                                f"from cloudformation_dataclasses.intrinsics import {constant_name}"
                            )

                            issues.append(
                                LintIssue(
                                    rule_id=self.rule_id,
                                    message=f"Use {constant_name} instead of Ref('{pseudo_param}')",
                                    line=node.lineno,
                                    column=node.col_offset,
                                    original=f'Ref("{pseudo_param}")',
                                    suggestion=constant_name,
                                    fix_imports=[import_stmt],
                                )
                            )

        return issues


class StringShouldBeEnum(LintRule):
    """Detect string literals that should be enum constants.

    This rule works by pattern matching known enum values in assignments,
    keyword arguments, and dict key-value pairs.

    Detects:
    - sse_algorithm = "AES256"
    - {'SSEAlgorithm': 'AES256'}
    - {'Status': 'Enabled'}

    Suggests:
    - sse_algorithm = ServerSideEncryption.AES256
    - {'SSEAlgorithm': ServerSideEncryption.AES256}
    - {'Status': BucketVersioningStatus.ENABLED}

    Note: This rule uses static analysis with known patterns.
    The linter core can do deeper runtime analysis when the classes are available.
    """

    rule_id = "CFD004"
    description = "Use enum constants instead of string literals"

    # Known enum patterns: field_name -> (enum_class, module, {value: constant_name})
    # Keys can be snake_case (Python) or PascalCase (CloudFormation)
    KNOWN_ENUMS: dict[str, tuple[str, str, dict[str, str]]] = {
        # S3 enums - snake_case keys
        "sse_algorithm": (
            "ServerSideEncryption",
            "cloudformation_dataclasses.aws.s3",
            {"AES256": "AES256", "aws:kms": "AWS_KMS", "aws:kms:dsse": "AWS_KMS_DSSE"},
        ),
        "status": (
            "BucketVersioningStatus",
            "cloudformation_dataclasses.aws.s3",
            {"Enabled": "ENABLED", "Suspended": "SUSPENDED"},
        ),
        # DynamoDB enums
        "key_type": (
            "KeyType",
            "cloudformation_dataclasses.aws.dynamodb",
            {"HASH": "HASH", "RANGE": "RANGE"},
        ),
        "attribute_type": (
            "AttributeType",
            "cloudformation_dataclasses.aws.dynamodb",
            {"S": "S", "N": "N", "B": "B"},
        ),
        "billing_mode": (
            "BillingMode",
            "cloudformation_dataclasses.aws.dynamodb",
            {"PROVISIONED": "PROVISIONED", "PAY_PER_REQUEST": "PAY_PER_REQUEST"},
        ),
        "projection_type": (
            "ProjectionType",
            "cloudformation_dataclasses.aws.dynamodb",
            {"ALL": "ALL", "KEYS_ONLY": "KEYS_ONLY", "INCLUDE": "INCLUDE"},
        ),
        "stream_view_type": (
            "StreamViewType",
            "cloudformation_dataclasses.aws.dynamodb",
            {
                "KEYS_ONLY": "KEYS_ONLY",
                "NEW_IMAGE": "NEW_IMAGE",
                "OLD_IMAGE": "OLD_IMAGE",
                "NEW_AND_OLD_IMAGES": "NEW_AND_OLD_IMAGES",
            },
        ),
        # Lambda enums
        "runtime": (
            "Runtime",
            "cloudformation_dataclasses.aws.lambda_",
            {
                "python3.8": "PYTHON3_8",
                "python3.9": "PYTHON3_9",
                "python3.10": "PYTHON3_10",
                "python3.11": "PYTHON3_11",
                "python3.12": "PYTHON3_12",
                "nodejs18.x": "NODEJS18_X",
                "nodejs20.x": "NODEJS20_X",
            },
        ),
        # EC2 / VPC enums
        "ip_protocol": (
            "IpProtocol",
            "cloudformation_dataclasses.core.constants",
            {"tcp": "TCP", "udp": "UDP", "icmp": "ICMP", "icmpv6": "ICMPV6", "-1": "ALL"},
        ),
    }

    # CloudFormation PascalCase keys -> (enum_class, module, {value: constant_name})
    # These are used inside dict literals with CloudFormation property names
    KNOWN_DICT_KEYS: dict[str, tuple[str, str, dict[str, str]]] = {
        # S3 properties
        "SSEAlgorithm": (
            "ServerSideEncryption",
            "cloudformation_dataclasses.aws.s3",
            {"AES256": "AES256", "aws:kms": "AWS_KMS", "aws:kms:dsse": "AWS_KMS_DSSE"},
        ),
        "Status": (
            "BucketVersioningStatus",
            "cloudformation_dataclasses.aws.s3",
            {"Enabled": "ENABLED", "Suspended": "SUSPENDED"},
        ),
        # DynamoDB properties
        "KeyType": (
            "KeyType",
            "cloudformation_dataclasses.aws.dynamodb",
            {"HASH": "HASH", "RANGE": "RANGE"},
        ),
        "AttributeType": (
            "AttributeType",
            "cloudformation_dataclasses.aws.dynamodb",
            {"S": "S", "N": "N", "B": "B"},
        ),
        "BillingMode": (
            "BillingMode",
            "cloudformation_dataclasses.aws.dynamodb",
            {"PROVISIONED": "PROVISIONED", "PAY_PER_REQUEST": "PAY_PER_REQUEST"},
        ),
        "ProjectionType": (
            "ProjectionType",
            "cloudformation_dataclasses.aws.dynamodb",
            {"ALL": "ALL", "KEYS_ONLY": "KEYS_ONLY", "INCLUDE": "INCLUDE"},
        ),
        "StreamViewType": (
            "StreamViewType",
            "cloudformation_dataclasses.aws.dynamodb",
            {
                "KEYS_ONLY": "KEYS_ONLY",
                "NEW_IMAGE": "NEW_IMAGE",
                "OLD_IMAGE": "OLD_IMAGE",
                "NEW_AND_OLD_IMAGES": "NEW_AND_OLD_IMAGES",
            },
        ),
        # Lambda properties
        "Runtime": (
            "Runtime",
            "cloudformation_dataclasses.aws.lambda_",
            {
                "python3.8": "PYTHON3_8",
                "python3.9": "PYTHON3_9",
                "python3.10": "PYTHON3_10",
                "python3.11": "PYTHON3_11",
                "python3.12": "PYTHON3_12",
                "nodejs18.x": "NODEJS18_X",
                "nodejs20.x": "NODEJS20_X",
            },
        ),
        # EC2 / VPC properties
        "IpProtocol": (
            "IpProtocol",
            "cloudformation_dataclasses.core.constants",
            {"tcp": "TCP", "udp": "UDP", "icmp": "ICMP", "icmpv6": "ICMPV6", "-1": "ALL"},
        ),
    }

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            # Check assignments: field_name = "value"
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        field_name = target.id
                        if field_name in self.KNOWN_ENUMS:
                            if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                                value = node.value.value
                                enum_class, module, value_map = self.KNOWN_ENUMS[field_name]
                                if value in value_map:
                                    const_name = value_map[value]
                                    suggestion = f"{enum_class}.{const_name}"
                                    import_stmt = f"from {module} import {enum_class}"

                                    issues.append(
                                        LintIssue(
                                            rule_id=self.rule_id,
                                            message=f"Use {suggestion} instead of '{value}'",
                                            line=node.value.lineno,
                                            column=node.value.col_offset,
                                            original=f'"{value}"',
                                            suggestion=suggestion,
                                            fix_imports=[import_stmt],
                                        )
                                    )

            # Check keyword arguments in function/class calls
            if isinstance(node, ast.Call):
                for keyword in node.keywords:
                    if keyword.arg and keyword.arg in self.KNOWN_ENUMS:
                        if isinstance(keyword.value, ast.Constant) and isinstance(keyword.value.value, str):
                            value = keyword.value.value
                            enum_class, module, value_map = self.KNOWN_ENUMS[keyword.arg]
                            if value in value_map:
                                const_name = value_map[value]
                                suggestion = f"{enum_class}.{const_name}"
                                import_stmt = f"from {module} import {enum_class}"

                                issues.append(
                                    LintIssue(
                                        rule_id=self.rule_id,
                                        message=f"Use {suggestion} instead of '{value}'",
                                        line=keyword.value.lineno,
                                        column=keyword.value.col_offset,
                                        original=f'"{value}"',
                                        suggestion=suggestion,
                                        fix_imports=[import_stmt],
                                    )
                                )

            # Check dict literals: {'SSEAlgorithm': 'AES256'}
            if isinstance(node, ast.Dict):
                for key, val in zip(node.keys, node.values):
                    if isinstance(key, ast.Constant) and isinstance(key.value, str):
                        key_str = key.value
                        if key_str in self.KNOWN_DICT_KEYS:
                            if isinstance(val, ast.Constant) and isinstance(val.value, str):
                                value = val.value
                                enum_class, module, value_map = self.KNOWN_DICT_KEYS[key_str]
                                if value in value_map:
                                    const_name = value_map[value]
                                    suggestion = f"{enum_class}.{const_name}"
                                    import_stmt = f"from {module} import {enum_class}"

                                    issues.append(
                                        LintIssue(
                                            rule_id=self.rule_id,
                                            message=f"Use {suggestion} instead of '{value}'",
                                            line=val.lineno,
                                            column=val.col_offset,
                                            original=f'"{value}"',
                                            suggestion=suggestion,
                                            fix_imports=[import_stmt],
                                        )
                                    )

        return issues


class DictShouldBePropertyType(LintRule):
    """Detect dict literals that should be PropertyType instances.

    This is a pattern-matching rule that looks for dict literals that
    look like CloudFormation resource properties.

    Detects: {"ServerSideEncryptionConfiguration": [...]}
    Suggests: BucketEncryption(...)

    Note: Full detection requires runtime type introspection.
    This static rule catches obvious patterns.
    """

    rule_id = "CFD005"
    description = "Use PropertyType classes instead of dict literals"

    # Known PropertyType patterns: dict key -> (PropertyType class, module, field mappings)
    KNOWN_PROPERTY_TYPES: dict[str, tuple[str, str]] = {
        # S3
        "ServerSideEncryptionConfiguration": ("BucketEncryption", "cloudformation_dataclasses.aws.s3"),
        "ServerSideEncryptionByDefault": (
            "ServerSideEncryptionByDefault",
            "cloudformation_dataclasses.aws.s3",
        ),
        "ServerSideEncryptionRule": ("ServerSideEncryptionRule", "cloudformation_dataclasses.aws.s3"),
        "VersioningConfiguration": ("VersioningConfiguration", "cloudformation_dataclasses.aws.s3"),
        "BucketEncryption": ("BucketEncryption", "cloudformation_dataclasses.aws.s3"),
        # DynamoDB
        "AttributeDefinitions": ("AttributeDefinition", "cloudformation_dataclasses.aws.dynamodb"),
        "KeySchema": ("KeySchema", "cloudformation_dataclasses.aws.dynamodb"),
        "ProvisionedThroughput": ("ProvisionedThroughput", "cloudformation_dataclasses.aws.dynamodb"),
        "GlobalSecondaryIndex": ("GlobalSecondaryIndex", "cloudformation_dataclasses.aws.dynamodb"),
        "LocalSecondaryIndex": ("LocalSecondaryIndex", "cloudformation_dataclasses.aws.dynamodb"),
        "StreamSpecification": ("StreamSpecification", "cloudformation_dataclasses.aws.dynamodb"),
        # Lambda
        "Code": ("Code", "cloudformation_dataclasses.aws.lambda_"),
        "VpcConfig": ("VpcConfig", "cloudformation_dataclasses.aws.lambda_"),
        "Environment": ("Environment", "cloudformation_dataclasses.aws.lambda_"),
        # EC2
        "SecurityGroupIngress": ("Ingress", "cloudformation_dataclasses.aws.ec2"),
        "SecurityGroupEgress": ("Egress", "cloudformation_dataclasses.aws.ec2"),
    }

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            if isinstance(node, ast.Dict):
                for key in node.keys:
                    if isinstance(key, ast.Constant) and isinstance(key.value, str):
                        key_str = key.value
                        if key_str in self.KNOWN_PROPERTY_TYPES:
                            class_name, module = self.KNOWN_PROPERTY_TYPES[key_str]
                            import_stmt = f"from {module} import {class_name}"

                            issues.append(
                                LintIssue(
                                    rule_id=self.rule_id,
                                    message=f"Consider using {class_name}() instead of dict with '{key_str}' key",
                                    line=key.lineno,
                                    column=key.col_offset,
                                    original=f'{{"{key_str}": ...}}',
                                    suggestion=f"{class_name}(...)",
                                    fix_imports=[import_stmt],
                                )
                            )

        return issues


# All available rules
ALL_RULES: list[type[LintRule]] = [
    StringShouldBeConditionOperator,
    StringShouldBeParameterType,
    RefShouldBePseudoParameter,
    StringShouldBeEnum,
    DictShouldBePropertyType,
]


def get_all_rules() -> list[LintRule]:
    """Get instances of all available lint rules."""
    return [rule_cls() for rule_cls in ALL_RULES]
