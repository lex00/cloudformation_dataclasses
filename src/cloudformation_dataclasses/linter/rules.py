"""Lint rules for cloudformation_dataclasses code.

This module defines the lint rules that detect patterns in user code that can
be improved. Each rule:

- Detects a specific anti-pattern (e.g., string literals instead of constants)
- Provides a clear message explaining the issue
- Suggests a better alternative with the exact replacement
- Specifies the imports needed for the fix

Rules:
    CFD001: Use condition operator constants instead of string literals
    CFD002: Use parameter type constants instead of string literals
    CFD003: Use pseudo-parameter constants instead of Ref() with strings
    CFD004: Use enum constants instead of string literals
    CFD005: Use PropertyType classes instead of dict literals
    CFD006: Use intrinsic function classes instead of raw dicts
    CFD007: Remove unnecessary .to_dict() calls on intrinsic functions
    CFD008: Use 'from .. import *' instead of explicit parent imports in stack files
    CFD009: Use wrapper classes instead of inline PropertyType constructors
    CFD010: Use ref(ParameterClass) instead of Ref("ParameterName")
    CFD011: Add missing required stack imports (from .. import *, from . import *)

Example:
    >>> from cloudformation_dataclasses.linter.rules import get_all_rules, LintContext
    >>> import ast
    >>> source = 'type = "String"'
    >>> context = LintContext(source=source, tree=ast.parse(source))
    >>> for rule in get_all_rules():
    ...     issues = rule.check(context)
    ...     for issue in issues:
    ...         print(f"{issue.rule_id}: {issue.message}")
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
from cloudformation_dataclasses.core.ast_helpers import is_cloudformation_dataclass


@dataclass
class LintIssue:
    """A detected lint issue with fix information.

    Represents a single issue found by a lint rule, including all information
    needed to display the issue and optionally auto-fix it.

    Attributes:
        rule_id: The rule identifier (e.g., "CFD001").
        message: Human-readable description of the issue.
        line: Line number where the issue was found (1-indexed).
        column: Column number where the issue was found (0-indexed).
        original: The original code that should be replaced (empty for insertions).
        suggestion: The suggested replacement code (or line to insert).
        fix_imports: List of import statements needed for the fix.
        insert_after_line: If set, insert suggestion as new line after this line number.
            Line 0 means insert at the very beginning (after module docstring if present).
    """

    rule_id: str
    message: str
    line: int
    column: int
    original: str
    suggestion: str
    fix_imports: list[str]
    insert_after_line: Optional[int] = None


@dataclass
class LintContext:
    """Context for linting, including source code and AST.

    Provides all the information a lint rule needs to analyze code.

    Attributes:
        source: The original source code as a string.
        tree: The parsed AST of the source code.
        filename: The filename for error messages (default: "<unknown>").
    """

    source: str
    tree: ast.AST
    filename: str = "<unknown>"


class LintRule(ABC):
    """Abstract base class for lint rules.

    Each lint rule must define a rule_id, description, and implement
    the check() method to detect issues.

    Attributes:
        rule_id: Unique identifier for the rule (e.g., "CFD001").
        description: Human-readable description of what the rule checks.
    """

    rule_id: str
    description: str

    @abstractmethod
    def check(self, context: LintContext) -> list[LintIssue]:
        """Check code for issues matching this rule.

        Args:
            context: The lint context containing source and AST.

        Returns:
            List of LintIssue objects for each detected issue.
        """
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


class DictShouldBeIntrinsic(LintRule):
    """Detect raw intrinsic function dicts that should use typed helpers.

    CloudFormation intrinsic functions like Ref, Sub, Select, Join, etc.
    should be expressed using the typed helpers from cloudformation_dataclasses.intrinsics
    rather than raw dict literals.

    Detects: {"Ref": "VpcId"}, {"Fn::Sub": "..."}, {"Fn::Select": [...]}
    Suggests: Ref("VpcId"), Sub("..."), Select(...)
    """

    rule_id = "CFD006"
    description = "Use intrinsic function classes instead of raw dicts"

    # Map CloudFormation intrinsic keys to Python function names and their module
    INTRINSIC_MAP: dict[str, tuple[str, str]] = {
        "Ref": ("Ref", "cloudformation_dataclasses.intrinsics"),
        "Fn::Sub": ("Sub", "cloudformation_dataclasses.intrinsics"),
        "Fn::Select": ("Select", "cloudformation_dataclasses.intrinsics"),
        "Fn::Join": ("Join", "cloudformation_dataclasses.intrinsics"),
        "Fn::GetAZs": ("GetAZs", "cloudformation_dataclasses.intrinsics"),
        "Fn::GetAtt": ("GetAtt", "cloudformation_dataclasses.intrinsics"),
        "Fn::If": ("If", "cloudformation_dataclasses.intrinsics"),
        "Fn::Equals": ("Equals", "cloudformation_dataclasses.intrinsics"),
        "Fn::And": ("And", "cloudformation_dataclasses.intrinsics"),
        "Fn::Or": ("Or", "cloudformation_dataclasses.intrinsics"),
        "Fn::Not": ("Not", "cloudformation_dataclasses.intrinsics"),
        "Fn::Base64": ("Base64", "cloudformation_dataclasses.intrinsics"),
        "Fn::Split": ("Split", "cloudformation_dataclasses.intrinsics"),
        "Fn::ImportValue": ("ImportValue", "cloudformation_dataclasses.intrinsics"),
        "Fn::FindInMap": ("FindInMap", "cloudformation_dataclasses.intrinsics"),
        "Fn::Cidr": ("Cidr", "cloudformation_dataclasses.intrinsics"),
    }

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            # Look for single-key dict literals that match intrinsic patterns
            if isinstance(node, ast.Dict) and len(node.keys) == 1:
                key = node.keys[0]
                if isinstance(key, ast.Constant) and isinstance(key.value, str):
                    key_str = key.value
                    if key_str in self.INTRINSIC_MAP:
                        func_name, module = self.INTRINSIC_MAP[key_str]
                        import_stmt = f"from {module} import {func_name}"

                        issues.append(
                            LintIssue(
                                rule_id=self.rule_id,
                                message=f"Use {func_name}() instead of {{'{key_str}': ...}}",
                                line=key.lineno,
                                column=key.col_offset,
                                original=f'{{"{key_str}": ...}}',
                                suggestion=f"{func_name}(...)",
                                fix_imports=[import_stmt],
                            )
                        )

        return issues


class UnnecessaryToDict(LintRule):
    """Detect unnecessary .to_dict() calls on intrinsic function results.

    When using intrinsic functions like ref(), get_att(), Join(), etc.,
    calling .to_dict() is unnecessary because these functions return objects
    that serialize correctly when used directly.

    Detects: ref(MyResource).to_dict(), get_att(MyResource, "Arn").to_dict()
    Suggests: ref(MyResource), get_att(MyResource, "Arn")
    """

    rule_id = "CFD007"
    description = "Remove unnecessary .to_dict() calls on intrinsic functions"

    # Functions that return serializable intrinsic objects
    INTRINSIC_FUNCTIONS = {"ref", "get_att", "Ref", "GetAtt", "Sub", "Join", "Select", "If"}

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            # Look for method calls: something.to_dict()
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute) and node.func.attr == "to_dict":
                    # Check if the object is a call to an intrinsic function
                    obj = node.func.value
                    if isinstance(obj, ast.Call):
                        func = obj.func
                        func_name = None
                        if isinstance(func, ast.Name):
                            func_name = func.id
                        elif isinstance(func, ast.Attribute):
                            func_name = func.attr

                        if func_name in self.INTRINSIC_FUNCTIONS:
                            issues.append(
                                LintIssue(
                                    rule_id=self.rule_id,
                                    message=f"Remove .to_dict() - {func_name}() returns a serializable object",
                                    line=node.lineno,
                                    column=node.col_offset,
                                    original=f"{func_name}(...).to_dict()",
                                    suggestion=f"{func_name}(...)",
                                    fix_imports=[],
                                )
                            )

        return issues


class InlinePropertyTypeConstructor(LintRule):
    """Detect inline PropertyType constructors that should be wrapper classes.

    In cloudformation_dataclasses, nested PropertyTypes should be defined as
    separate wrapper classes with @cloudformation_dataclass, not as inline
    constructor calls.

    Detects:
        security_group_ingress = [security_group.Ingress(...)]
        default_actions = [listener.Action(...)]
        alias_target = record_set.AliasTarget(...)

    Suggests:
        @cloudformation_dataclass
        class MyIngress:
            resource: ec2.security_group.Ingress
            ...

        security_group_ingress = [MyIngress]
    """

    rule_id = "CFD009"
    description = "Use wrapper classes instead of inline PropertyType constructors"

    # Known PropertyType module.Class patterns that indicate inline constructors
    # Format: (module_pattern, class_name) -> description
    KNOWN_PROPERTY_TYPES: dict[tuple[str, str], str] = {
        # EC2 Security Group
        ("security_group", "Ingress"): "security group ingress rule",
        ("security_group", "Egress"): "security group egress rule",
        # ELB Listener
        ("listener", "Action"): "listener action",
        ("listener", "Certificate"): "listener certificate",
        ("listener", "RedirectConfig"): "redirect config",
        ("listener", "ForwardConfig"): "forward config",
        ("listener", "AuthenticateOidcConfig"): "OIDC auth config",
        ("listener", "AuthenticateCognitoConfig"): "Cognito auth config",
        # Route53 RecordSet
        ("record_set", "AliasTarget"): "alias target",
        ("record_set", "GeoLocation"): "geo location",
        # ECS Task Definition
        ("task_definition", "ContainerDefinition"): "container definition",
        ("task_definition", "PortMapping"): "port mapping",
        ("task_definition", "LogConfiguration"): "log configuration",
        ("task_definition", "Environment"): "environment variable",
        ("task_definition", "MountPoint"): "mount point",
        ("task_definition", "VolumeFrom"): "volume from",
        ("task_definition", "Secret"): "secret",
        # ECS Service
        ("service", "LoadBalancer"): "load balancer config",
        ("service", "NetworkConfiguration"): "network configuration",
        ("service", "AwsVpcConfiguration"): "VPC configuration",
        # IAM
        ("role", "Policy"): "inline policy",
        # Lambda
        ("function", "Code"): "function code",
        ("function", "VpcConfig"): "VPC config",
        ("function", "Environment"): "environment",
        # CloudWatch
        ("alarm", "Dimension"): "metric dimension",
        ("alarm", "MetricDataQuery"): "metric data query",
        # ACM Certificate
        ("certificate", "DomainValidationOption"): "domain validation option",
        # RDS
        ("db_instance", "DBInstanceRole"): "DB instance role",
    }

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            # Check for direct Call nodes that match PropertyType patterns
            if isinstance(node, ast.Call):
                issue = self._check_call(node)
                if issue:
                    issues.append(issue)

        return issues

    def _check_call(self, node: ast.Call) -> Optional[LintIssue]:
        """Check if a Call node is an inline PropertyType constructor."""
        # Look for patterns like: module.ClassName(...)
        # E.g., security_group.Ingress(...), listener.Action(...)
        func = node.func
        if not isinstance(func, ast.Attribute):
            return None

        class_name = func.attr
        # Get the module part (e.g., security_group, listener)
        if isinstance(func.value, ast.Name):
            module_name = func.value.id
        elif isinstance(func.value, ast.Attribute):
            # Could be nested like ec2.security_group.Ingress
            module_name = func.value.attr
        else:
            return None

        # Check if this matches a known PropertyType pattern
        key = (module_name, class_name)
        if key in self.KNOWN_PROPERTY_TYPES:
            description = self.KNOWN_PROPERTY_TYPES[key]
            return LintIssue(
                rule_id=self.rule_id,
                message=f"Define {description} as a separate @cloudformation_dataclass wrapper",
                line=node.lineno,
                column=node.col_offset,
                original=f"{module_name}.{class_name}(...)",
                suggestion=f"@cloudformation_dataclass class My{class_name}: resource: ...{class_name}",
                fix_imports=[],
            )

        return None


class ExplicitParentImport(LintRule):
    """Detect explicit imports from parent package in stack resource files.

    Stack resource files should only use `from .. import *` for consistency.
    The parent package's __init__.py should re-export everything needed.

    Detects: from .. import (foo, bar, baz)
    Suggests: from .. import *
    """

    rule_id = "CFD008"
    description = "Use 'from .. import *' instead of explicit imports from parent"

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        # Only check files in a stack/ directory
        filename = str(context.filename)
        if "/stack/" not in filename:
            return issues

        # Skip __init__.py files
        if filename.endswith("__init__.py"):
            return issues

        for node in ast.walk(context.tree):
            if isinstance(node, ast.ImportFrom):
                # Check for `from .. import something` (not `from .. import *`)
                if node.module is None and node.level == 2:
                    # This is `from .. import X` or `from .. import (X, Y, Z)`
                    # Check if it's a star import
                    is_star = any(alias.name == "*" for alias in node.names)
                    if not is_star:
                        names = ", ".join(alias.name for alias in node.names)
                        issues.append(
                            LintIssue(
                                rule_id=self.rule_id,
                                message="Use 'from .. import *' instead of explicit imports",
                                line=node.lineno,
                                column=node.col_offset,
                                original=f"from .. import {names}",
                                suggestion="from .. import *",
                                fix_imports=[],
                            )
                        )

        return issues


class RefShouldBeParameterClass(LintRule):
    """Detect Ref() calls with parameter names that should use ref(ParameterClass).

    When referencing CloudFormation parameters, use ref(ParameterClass) to reference
    the Parameter wrapper class defined in params.py, rather than Ref("ParamName").

    This provides better type safety and allows IDEs to track references.

    Detects:
        vpc_id = Ref("VpcId")
        certificate_arn = Ref("CertificateArn")

    Suggests:
        vpc_id = ref(VpcIdParam)  # where VpcIdParam is defined in params.py
        certificate_arn = ref(CertificateArnParam)

    Note: This rule only flags Ref() calls with PascalCase parameter names
    (not pseudo-parameters like "AWS::Region" which are handled by CFD003).
    """

    rule_id = "CFD010"
    description = "Use ref(ParameterClass) instead of Ref() with parameter name strings"

    # Common parameter name patterns (PascalCase identifiers, not AWS:: prefixed)
    PARAM_NAME_PATTERN = re.compile(r'^[A-Z][a-zA-Z0-9]*$')

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        # Only check files in a stack/ directory (resource files that should use params)
        filename = str(context.filename)
        if "/stack/" not in filename:
            return issues

        # Skip params.py itself
        if filename.endswith("params.py"):
            return issues

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
                        param_name = arg.value

                        # Skip pseudo-parameters (handled by CFD003)
                        if param_name.startswith("AWS::"):
                            continue

                        # Check if it looks like a parameter name (PascalCase)
                        if self.PARAM_NAME_PATTERN.match(param_name):
                            # Suggest the conventional Param suffix
                            suggested_class = f"{param_name}Param"
                            issues.append(
                                LintIssue(
                                    rule_id=self.rule_id,
                                    message=f"Use ref({suggested_class}) instead of Ref('{param_name}')",
                                    line=node.lineno,
                                    column=node.col_offset,
                                    original=f'Ref("{param_name}")',
                                    suggestion=f"ref({suggested_class})",
                                    fix_imports=[],
                                )
                            )

        return issues


class MissingStackImport(LintRule):
    """Detect missing required import lines in stack files.

    Stack files need specific import patterns:
    - params.py: from .. import *, from . import *
    - outputs.py: from .. import * (resource import varies by module name)
    - resource files: from .. import *, from . import *

    This rule checks for missing star imports and suggests adding them.

    Detects missing:
        from .. import *  # noqa: F403, F401
        from . import *
    """

    rule_id = "CFD011"
    description = "Missing required stack import"

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        # Only check files in a stack/ directory
        filename = str(context.filename)
        if "/stack/" not in filename:
            return issues

        # Skip __init__.py files
        if filename.endswith("__init__.py"):
            return issues

        # Determine file type
        basename = filename.split("/")[-1]

        # Find existing star imports
        has_parent_star = False  # from .. import *
        has_sibling_star = False  # from . import *, from params import *, from {module} import *
        last_import_line = 0
        first_import_line = 0

        for node in context.tree.body:
            if isinstance(node, ast.ImportFrom):
                is_star = any(alias.name == "*" for alias in node.names)
                if is_star:
                    if node.level == 2 and node.module is None:
                        # from .. import *
                        has_parent_star = True
                    elif node.level == 1:
                        # from . import * or from .something import *
                        has_sibling_star = True
                    elif node.level == 0 and node.module:
                        # from params import * or from alb import * (bare module names)
                        has_sibling_star = True
                if first_import_line == 0:
                    first_import_line = node.lineno
                last_import_line = max(last_import_line, node.end_lineno or node.lineno)
            elif isinstance(node, ast.Import):
                if first_import_line == 0:
                    first_import_line = node.lineno
                last_import_line = max(last_import_line, node.end_lineno or node.lineno)

        # Find where to insert (after docstring if present)
        insert_at_top = 0
        if context.tree.body and isinstance(context.tree.body[0], ast.Expr):
            first_stmt = context.tree.body[0]
            if isinstance(first_stmt.value, ast.Constant) and isinstance(
                first_stmt.value.value, str
            ):
                # Module has a docstring
                insert_at_top = first_stmt.end_lineno or first_stmt.lineno

        # All stack files need from .. import *
        if not has_parent_star:
            issues.append(
                LintIssue(
                    rule_id=self.rule_id,
                    message="Missing 'from .. import *'",
                    line=insert_at_top + 1,
                    column=0,
                    original="",
                    suggestion="from .. import *  # noqa: F403, F401",
                    fix_imports=[],
                    insert_after_line=insert_at_top,
                )
            )

        # Only params.py needs a second import (from . import * for sibling params)
        # Resource files and outputs.py get everything through from .. import *
        if basename == "params.py" and not has_sibling_star:
            insert_line = last_import_line if last_import_line > 0 else insert_at_top
            if not has_parent_star:
                # We're adding from .. import * too, so second import goes after that
                insert_line = insert_at_top + 1 if insert_at_top > 0 else 1

            issues.append(
                LintIssue(
                    rule_id=self.rule_id,
                    message="Missing 'from . import *'",
                    line=insert_line + 1,
                    column=0,
                    original="",
                    suggestion="from . import *  # noqa: F403, F401",
                    fix_imports=[],
                    insert_after_line=insert_line,
                )
            )

        return issues


class FileShouldBeSplit(LintRule):
    """Detect resource files with many resources that should be split.

    When a resource file has 12+ resources AND would split into multiple
    category files, it's beneficial to split into category-based files
    (network.py, security.py, compute.py, etc.) for better organization.

    This rule only triggers if the split would actually produce multiple files.
    """

    rule_id = "CFD012"
    description = "File has many resources and should be split"
    threshold = 12  # Minimum resources to trigger warning

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        # Count @cloudformation_dataclass decorated classes
        resource_count = 0
        for node in ast.walk(context.tree):
            if isinstance(node, ast.ClassDef) and is_cloudformation_dataclass(node):
                resource_count += 1

        if resource_count >= self.threshold:
            # Check if split would produce multiple files
            from cloudformation_dataclasses.linter.split import split_resource_file

            split_files = split_resource_file(context.source)
            if len(split_files) > 1:
                issues.append(
                    LintIssue(
                        rule_id=self.rule_id,
                        message=f"File has {resource_count} resources across {len(split_files)} categories. Run: cfn-dataclasses split {context.filename}",
                        line=1,
                        column=0,
                        original="",
                        suggestion="",
                        fix_imports=[],
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
    DictShouldBeIntrinsic,
    UnnecessaryToDict,
    InlinePropertyTypeConstructor,
    ExplicitParentImport,
    RefShouldBeParameterClass,
    FileShouldBeSplit,
]


def get_all_rules() -> list[LintRule]:
    """Get instances of all available lint rules.

    Returns:
        List of instantiated LintRule objects, one for each rule.
    """
    return [rule_cls() for rule_cls in ALL_RULES]
