"""
AST helper utilities for CloudFormation dataclasses.

This module provides functions for analyzing and manipulating Python AST nodes,
shared between the importer and linter systems.
"""

import ast
from typing import Optional


def is_cloudformation_dataclass(node: ast.ClassDef) -> bool:
    """Check if a class has the @cloudformation_dataclass decorator.

    Args:
        node: An AST ClassDef node.

    Returns:
        True if the class has the @cloudformation_dataclass decorator.

    Example:
        >>> import ast
        >>> source = '''
        ... @cloudformation_dataclass
        ... class MyBucket:
        ...     resource: s3.Bucket
        ... '''
        >>> tree = ast.parse(source)
        >>> cls = tree.body[0]
        >>> is_cloudformation_dataclass(cls)
        True
    """
    for decorator in node.decorator_list:
        # Simple decorator: @cloudformation_dataclass
        if isinstance(decorator, ast.Name) and decorator.id == "cloudformation_dataclass":
            return True
        # Decorator with args: @cloudformation_dataclass(...)
        elif isinstance(decorator, ast.Call):
            func = decorator.func
            if isinstance(func, ast.Name) and func.id == "cloudformation_dataclass":
                return True
    return False


def find_decorator(node: ast.ClassDef, name: str) -> Optional[ast.expr]:
    """Find a decorator by name on a class.

    Args:
        node: An AST ClassDef node.
        name: The decorator name to find.

    Returns:
        The decorator AST node if found, None otherwise.
    """
    for decorator in node.decorator_list:
        if isinstance(decorator, ast.Name) and decorator.id == name:
            return decorator
        elif isinstance(decorator, ast.Call):
            func = decorator.func
            if isinstance(func, ast.Name) and func.id == name:
                return decorator
    return None


def find_last_import_line(tree: ast.Module) -> int:
    """Find the line number after the last import statement.

    Args:
        tree: An AST Module node.

    Returns:
        The line number where new imports should be inserted (after existing imports).
        Returns 1 if no imports found.
    """
    last_import_line = 0

    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            last_import_line = node.end_lineno or node.lineno
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
            # Skip docstrings at module level
            if last_import_line == 0:
                continue
        elif last_import_line > 0:
            # Found non-import after imports, stop
            break

    return last_import_line if last_import_line > 0 else 1


def parse_existing_imports(tree: ast.Module) -> dict[str, set[str]]:
    """Parse existing imports from an AST tree.

    Args:
        tree: An AST Module node.

    Returns:
        A dict mapping module names to sets of imported names.
        For `from x import y, z` returns {'x': {'y', 'z'}}.
        For `import x` returns {'x': {'x'}}.

    Example:
        >>> import ast
        >>> source = '''
        ... from os import path, getcwd
        ... import sys
        ... '''
        >>> tree = ast.parse(source)
        >>> imports = parse_existing_imports(tree)
        >>> imports['os']
        {'path', 'getcwd'}
    """
    imports: dict[str, set[str]] = {}

    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and node.module:
            if node.module not in imports:
                imports[node.module] = set()
            for alias in node.names:
                imports[node.module].add(alias.name)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                module_name = alias.name
                if module_name not in imports:
                    imports[module_name] = set()
                imports[module_name].add(alias.asname or alias.name)

    return imports


def extract_resource_annotation(node: ast.ClassDef) -> Optional[tuple[str, str]]:
    """Extract the resource type annotation from a cloudformation_dataclass.

    Looks for `resource: module.ClassName` pattern.

    Args:
        node: An AST ClassDef node.

    Returns:
        A tuple of (module, class_name) if found, None otherwise.
        For `resource: s3.Bucket` returns ('s3', 'Bucket').

    Example:
        >>> import ast
        >>> source = '''
        ... @cloudformation_dataclass
        ... class MyBucket:
        ...     resource: s3.Bucket
        ... '''
        >>> tree = ast.parse(source)
        >>> cls = tree.body[0]
        >>> extract_resource_annotation(cls)
        ('s3', 'Bucket')
    """
    for stmt in node.body:
        if isinstance(stmt, ast.AnnAssign):
            if isinstance(stmt.target, ast.Name) and stmt.target.id == "resource":
                return _parse_resource_annotation(stmt.annotation)
    return None


def _parse_resource_annotation(annotation: ast.expr) -> Optional[tuple[str, str]]:
    """Parse a resource type annotation.

    Handles patterns like:
    - s3.Bucket -> ('s3', 'Bucket')
    - s3.bucket.Bucket -> ('s3.bucket', 'Bucket')
    """
    if isinstance(annotation, ast.Attribute):
        class_name = annotation.attr

        # Simple case: s3.Bucket
        if isinstance(annotation.value, ast.Name):
            module = annotation.value.id
            return (module, class_name)

        # Nested case: s3.bucket.Bucket
        elif isinstance(annotation.value, ast.Attribute):
            parts = []
            current = annotation.value
            while isinstance(current, ast.Attribute):
                parts.append(current.attr)
                current = current.value
            if isinstance(current, ast.Name):
                parts.append(current.id)
                parts.reverse()
                module = ".".join(parts)
                return (module, class_name)

    return None


def get_string_value(node: ast.expr) -> Optional[str]:
    """Get the string value from an AST node if it's a string constant.

    Args:
        node: An AST expression node.

    Returns:
        The string value if the node is a string constant, None otherwise.
    """
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def is_call_to(node: ast.expr, name: str) -> bool:
    """Check if an AST node is a call to a specific function.

    Args:
        node: An AST expression node.
        name: The function name to check for.

    Returns:
        True if the node is a call to the specified function.

    Example:
        >>> import ast
        >>> source = "ref(MyBucket)"
        >>> tree = ast.parse(source, mode='eval')
        >>> is_call_to(tree.body, 'ref')
        True
    """
    if not isinstance(node, ast.Call):
        return False

    func = node.func
    if isinstance(func, ast.Name):
        return func.id == name
    elif isinstance(func, ast.Attribute):
        return func.attr == name

    return False
