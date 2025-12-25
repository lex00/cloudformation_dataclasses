"""Split resource files into category-based files.

This module provides functionality to analyze a Python resource file
and split it into multiple files based on AWS service categories.
"""

import ast
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from cloudformation_dataclasses.core.file_organization import (
    ResourceInfo,
    get_category,
    organize_resources,
)


@dataclass
class ClassDefinition:
    """A class definition extracted from source."""

    name: str
    start_line: int  # 1-indexed
    end_line: int  # 1-indexed
    source: str  # The source code for this class
    decorator_line: Optional[int] = None  # Line of @cloudformation_dataclass if present


def parse_resource_file(source: str) -> tuple[dict[str, ResourceInfo], dict[str, ClassDefinition]]:
    """Parse a Python source file to extract resource information.

    Args:
        source: Python source code

    Returns:
        Tuple of (resources dict, class definitions dict)
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return {}, {}

    lines = source.splitlines()
    resources: dict[str, ResourceInfo] = {}
    class_defs: dict[str, ClassDefinition] = {}

    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef):
            continue

        # Check if decorated with @cloudformation_dataclass
        is_dataclass = False
        decorator_line = None
        for decorator in node.decorator_list:
            if isinstance(decorator, ast.Name) and decorator.id == "cloudformation_dataclass":
                is_dataclass = True
                decorator_line = decorator.lineno
            elif isinstance(decorator, ast.Call):
                func = decorator.func
                if isinstance(func, ast.Name) and func.id == "cloudformation_dataclass":
                    is_dataclass = True
                    decorator_line = decorator.lineno

        if not is_dataclass:
            continue

        # Extract resource type from `resource: ec2.SecurityGroup` annotation
        service = None
        type_name = None
        for stmt in node.body:
            if isinstance(stmt, ast.AnnAssign):
                if isinstance(stmt.target, ast.Name) and stmt.target.id == "resource":
                    service, type_name = _parse_resource_annotation(stmt.annotation)
                    break

        if not service or not type_name:
            continue

        # Find dependencies (ref() and get_att() calls)
        dependencies = _find_dependencies(node)

        # Get source lines
        start_line = decorator_line or node.lineno
        end_line = node.end_lineno or node.lineno

        # Extract source code for this class (including decorator and any preceding comments)
        class_source = "\n".join(lines[start_line - 1 : end_line])

        resources[node.name] = ResourceInfo(
            class_name=node.name,
            service=service,
            type_name=type_name,
            source_lines=(start_line, end_line),
            dependencies=dependencies,
        )

        class_defs[node.name] = ClassDefinition(
            name=node.name,
            start_line=start_line,
            end_line=end_line,
            source=class_source,
            decorator_line=decorator_line,
        )

    return resources, class_defs


def _parse_resource_annotation(annotation: ast.expr) -> tuple[Optional[str], Optional[str]]:
    """Parse resource type annotation like `ec2.SecurityGroup`.

    Returns:
        Tuple of (service, type_name) or (None, None) if not parseable
    """
    if isinstance(annotation, ast.Attribute):
        # e.g., ec2.SecurityGroup or elasticloadbalancingv2.LoadBalancer
        type_name = annotation.attr

        # Get the service module
        if isinstance(annotation.value, ast.Name):
            module = annotation.value.id
            service = _module_to_service(module)
            return service, type_name
        elif isinstance(annotation.value, ast.Attribute):
            # e.g., route53.record_set.AliasTarget - it's a PropertyType, not a Resource
            # For PropertyTypes, use the parent module
            if isinstance(annotation.value.value, ast.Name):
                module = annotation.value.value.id
                service = _module_to_service(module)
                return service, type_name

    return None, None


def _module_to_service(module: str) -> str:
    """Convert Python module name to AWS service name.

    Maps common module names to their CloudFormation service names.
    """
    module_map = {
        "ec2": "EC2",
        "s3": "S3",
        "iam": "IAM",
        "lambda_": "Lambda",
        "rds": "RDS",
        "dynamodb": "DynamoDB",
        "ecs": "ECS",
        "eks": "EKS",
        "elasticloadbalancingv2": "ElasticLoadBalancingV2",
        "route53": "Route53",
        "cloudfront": "CloudFront",
        "apigateway": "APIGateway",
        "sns": "SNS",
        "sqs": "SQS",
        "cloudwatch": "CloudWatch",
        "logs": "Logs",
        "kms": "KMS",
        "secretsmanager": "SecretsManager",
        "cognito": "Cognito",
        "certificatemanager": "CertificateManager",
        "acm": "CertificateManager",
        "ssm": "SSM",
        "codebuild": "CodeBuild",
        "codepipeline": "CodePipeline",
        "events": "Events",
        "stepfunctions": "StepFunctions",
        "efs": "EFS",
        "elasticache": "ElastiCache",
        "autoscaling": "AutoScaling",
        "wafv2": "WAFv2",
    }
    return module_map.get(module.lower(), module.upper())


def _find_dependencies(node: ast.ClassDef) -> set[str]:
    """Find class names referenced via ref() or get_att() in a class body."""
    dependencies: set[str] = set()

    for child in ast.walk(node):
        if isinstance(child, ast.Call):
            func = child.func
            func_name = None
            if isinstance(func, ast.Name):
                func_name = func.id
            elif isinstance(func, ast.Attribute):
                func_name = func.attr

            if func_name in ("ref", "get_att") and child.args:
                arg = child.args[0]
                if isinstance(arg, ast.Name):
                    dependencies.add(arg.id)

    return dependencies


def split_resource_file(
    source: str,
    *,
    min_resources_to_split: int = 3,
) -> dict[str, str]:
    """Split a resource file into category-based files.

    Args:
        source: Python source code
        min_resources_to_split: Minimum resources before splitting (default 3)

    Returns:
        Dict of filename -> source code
    """
    resources, class_defs = parse_resource_file(source)

    if not resources:
        return {"main": source}

    # Organize into categories
    categories = organize_resources(resources, min_resources_to_split=min_resources_to_split)

    # If everything is in main, no split needed
    if len(categories) == 1 and "main" in categories:
        return {"main": source}

    # Extract header (imports and module docstring)
    header = _extract_header(source)

    # Build output files
    result: dict[str, str] = {}
    for category, class_names in categories.items():
        # Sort by original source order
        sorted_names = sorted(
            class_names,
            key=lambda n: class_defs[n].start_line if n in class_defs else 0,
        )

        # Build file content
        parts = [header, ""]
        for class_name in sorted_names:
            if class_name in class_defs:
                parts.append("")
                parts.append(class_defs[class_name].source)

        content = "\n".join(parts).strip() + "\n"
        result[category] = content

    return result


def _extract_header(source: str) -> str:
    """Extract the header portion of a file (docstring + imports)."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return ""

    lines = source.splitlines()

    # Find the last import line
    last_import_line = 0
    first_class_line = len(lines) + 1

    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            last_import_line = max(last_import_line, node.end_lineno or node.lineno)
        elif isinstance(node, ast.ClassDef):
            # Check for decorator
            if node.decorator_list:
                first_class_line = min(first_class_line, node.decorator_list[0].lineno)
            else:
                first_class_line = min(first_class_line, node.lineno)
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
            # Module docstring
            last_import_line = max(last_import_line, node.end_lineno or node.lineno)

    # Header is everything up to and including the last import
    # But stop before the first class
    end_line = min(last_import_line, first_class_line - 1)
    if end_line > 0:
        return "\n".join(lines[:end_line])
    return ""


def print_split_preview(source: str, filename: str = "<source>") -> None:
    """Print a preview of how a file would be split."""
    resources, class_defs = parse_resource_file(source)

    if not resources:
        print(f"{filename}: No @cloudformation_dataclass resources found")
        return

    categories = organize_resources(resources, min_resources_to_split=3)

    print(f"\n{filename}: {len(resources)} resources")
    print("=" * 60)

    for category, class_names in sorted(categories.items()):
        print(f"\n{category}.py ({len(class_names)} resources):")
        for name in class_names:
            if name in resources:
                info = resources[name]
                print(f"  - {name} ({info.service}::{info.type_name})")


def write_split_files(
    source_path: Path,
    output_dir: Optional[Path] = None,
    *,
    dry_run: bool = False,
) -> dict[str, Path]:
    """Split a resource file and write the results.

    Args:
        source_path: Path to the source file
        output_dir: Directory to write files (default: same as source)
        dry_run: If True, don't write files, just return what would be written

    Returns:
        Dict of category -> output path
    """
    source = source_path.read_text()
    split_files = split_resource_file(source)

    if output_dir is None:
        output_dir = source_path.parent

    result: dict[str, Path] = {}
    for category, content in split_files.items():
        out_path = output_dir / f"{category}.py"
        result[category] = out_path

        if not dry_run:
            out_path.write_text(content)

    return result
