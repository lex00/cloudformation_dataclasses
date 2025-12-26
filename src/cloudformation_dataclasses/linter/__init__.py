"""Linter for cloudformation_dataclasses code.

This module provides linting and auto-fixing capabilities for Python code
that uses cloudformation_dataclasses. It detects common mistakes like:

- Using string literals instead of enum constants
- Using string literals instead of condition operator constants
- Using string literals instead of parameter type constants
- Using Ref("AWS::Region") instead of AWS_REGION
- Using dict literals instead of PropertyType classes

Example usage:

    from cloudformation_dataclasses.linter import lint_code, fix_code

    # Check code for issues
    issues = lint_code('''
        from cloudformation_dataclasses.aws.s3 import Bucket
        sse_algorithm = "AES256"
    ''')
    for issue in issues:
        print(f"{issue.line}:{issue.column}: {issue.message}")

    # Auto-fix code
    fixed = fix_code('''
        from cloudformation_dataclasses.aws.s3 import Bucket
        sse_algorithm = "AES256"
    ''')
    print(fixed)

The linter is also integrated with the importer:

    from cloudformation_dataclasses.importer import generate_code

    code = generate_code(template, mode="block", lint=True)  # Default: lint=True

And can be used with build_template at runtime (optional warnings):

    template = build_template(warn_on_lint_issues=True)
"""

import ast
import re
from typing import Optional

from cloudformation_dataclasses.core.ast_helpers import find_last_import_line
from cloudformation_dataclasses.linter.rules import (
    ALL_RULES,
    DictShouldBePropertyType,
    LintContext,
    LintIssue,
    LintRule,
    RefShouldBePseudoParameter,
    StringShouldBeConditionOperator,
    StringShouldBeEnum,
    StringShouldBeParameterType,
    get_all_rules,
)

__all__ = [
    # Core functions
    "lint_code",
    "lint_file",
    "fix_code",
    "fix_file",
    # Data classes
    "LintIssue",
    "LintContext",
    # Rules
    "LintRule",
    "StringShouldBeConditionOperator",
    "StringShouldBeParameterType",
    "RefShouldBePseudoParameter",
    "StringShouldBeEnum",
    "DictShouldBePropertyType",
    "ALL_RULES",
    "get_all_rules",
]


def lint_code(
    source: str,
    *,
    filename: str = "<string>",
    rules: Optional[list[LintRule]] = None,
) -> list[LintIssue]:
    """Lint Python source code for cloudformation_dataclasses issues.

    Args:
        source: The Python source code to lint
        filename: Optional filename for error messages
        rules: Optional list of rules to apply. Defaults to all rules.

    Returns:
        List of LintIssue objects describing detected issues
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        # Can't lint code that doesn't parse
        return []

    context = LintContext(source=source, tree=tree, filename=filename)

    if rules is None:
        rules = get_all_rules()

    issues: list[LintIssue] = []
    for rule in rules:
        issues.extend(rule.check(context))

    # Sort by line number, then column
    issues.sort(key=lambda i: (i.line, i.column))
    return issues


def lint_file(
    filepath: str,
    *,
    rules: Optional[list[LintRule]] = None,
) -> list[LintIssue]:
    """Lint a Python file for cloudformation_dataclasses issues.

    Args:
        filepath: Path to the Python file to lint
        rules: Optional list of rules to apply. Defaults to all rules.

    Returns:
        List of LintIssue objects describing detected issues
    """
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()
    return lint_code(source, filename=filepath, rules=rules)


def fix_code(
    source: str,
    *,
    filename: str = "<string>",
    rules: Optional[list[LintRule]] = None,
    add_imports: bool = True,
) -> str:
    """Fix lint issues in Python source code.

    This function applies auto-fixes for detected lint issues.

    Args:
        source: The Python source code to fix
        filename: Optional filename for context (used by some rules)
        rules: Optional list of rules to apply. Defaults to all rules.
        add_imports: Whether to add required imports. Defaults to True.

    Returns:
        The fixed source code
    """
    issues = lint_code(source, filename=filename, rules=rules)
    if not issues:
        return source

    # Separate insertions from replacements
    insertions = [i for i in issues if i.insert_after_line is not None]
    replacements = [i for i in issues if i.insert_after_line is None]

    # Collect all fix imports
    all_imports: set[str] = set()
    if add_imports:
        for issue in issues:
            all_imports.update(issue.fix_imports)

    # Separate multi-line and single-line replacements
    multiline_replacements = [i for i in replacements if "\n" in i.original]
    singleline_replacements = [i for i in replacements if "\n" not in i.original]

    # Apply multi-line replacements first (on the full source)
    # Sort by line number descending to preserve positions
    fixed_source = source
    for issue in sorted(multiline_replacements, key=lambda i: i.line, reverse=True):
        # Try to find and replace the original string
        original_patterns = [
            issue.original,
            issue.original.replace('"', "'"),
        ]
        for pattern in original_patterns:
            if pattern in fixed_source:
                fixed_source = fixed_source.replace(pattern, issue.suggestion, 1)
                break

    # Apply single-line replacements
    issues_by_line: dict[int, list[LintIssue]] = {}
    for issue in singleline_replacements:
        if issue.line not in issues_by_line:
            issues_by_line[issue.line] = []
        issues_by_line[issue.line].append(issue)

    lines = fixed_source.splitlines(keepends=True)

    # Apply replacements line by line (in reverse order to preserve positions)
    for line_num in sorted(issues_by_line.keys(), reverse=True):
        line_issues = issues_by_line[line_num]
        # Sort by column in reverse order
        line_issues.sort(key=lambda i: i.column, reverse=True)

        if line_num <= len(lines):
            line = lines[line_num - 1]
            for issue in line_issues:
                # Try to find and replace the original string
                # Handle both single and double quotes
                original_patterns = [
                    issue.original,
                    issue.original.replace('"', "'"),
                ]
                for pattern in original_patterns:
                    if pattern in line:
                        line = line.replace(pattern, issue.suggestion, 1)
                        break
            lines[line_num - 1] = line

    # Apply insertions (in reverse line order to preserve positions)
    # Sort by insert_after_line descending
    for issue in sorted(insertions, key=lambda i: i.insert_after_line or 0, reverse=True):
        insert_pos = issue.insert_after_line or 0
        # Ensure the suggestion ends with a newline
        suggestion = issue.suggestion
        if not suggestion.endswith("\n"):
            suggestion += "\n"
        # Insert after the specified line (insert_pos is 0-indexed conceptually)
        # Line 0 means insert at the very beginning
        # Line N means insert after line N
        lines.insert(insert_pos, suggestion)

    fixed_source = "".join(lines)

    # Add imports if needed
    if add_imports and all_imports:
        fixed_source = _add_imports(fixed_source, all_imports)

    return fixed_source


def fix_file(
    filepath: str,
    *,
    rules: Optional[list[LintRule]] = None,
    add_imports: bool = True,
    write: bool = False,
) -> str:
    """Fix lint issues in a Python file.

    Args:
        filepath: Path to the Python file to fix
        rules: Optional list of rules to apply. Defaults to all rules.
        add_imports: Whether to add required imports. Defaults to True.
        write: Whether to write the fixed code back to the file.
            Defaults to False (returns fixed code without writing).

    Returns:
        The fixed source code
    """
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()

    fixed = fix_code(source, rules=rules, add_imports=add_imports)

    if write and fixed != source:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(fixed)

    return fixed


def _add_imports(source: str, imports: set[str]) -> str:
    """Add import statements to source code.

    Tries to add imports in a sensible location:
    1. After existing cloudformation_dataclasses imports
    2. After other imports
    3. At the beginning of the file

    Args:
        source: The source code
        imports: Set of import statements to add

    Returns:
        Source code with imports added
    """
    if not imports:
        return source

    # Parse to find existing imports
    try:
        tree = ast.parse(source)
    except SyntaxError:
        # Fall back to adding at the top
        import_block = "\n".join(sorted(imports))
        return import_block + "\n\n" + source

    # Find the line of the last module-level import statement
    last_import_line = find_last_import_line(tree)

    # Filter out imports that already exist (module-level only)
    existing_imports = set()
    for node in tree.body:
        if isinstance(node, ast.ImportFrom):
            if node.module:
                for alias in node.names:
                    existing_imports.add(f"from {node.module} import {alias.name}")

    new_imports = imports - existing_imports
    if not new_imports:
        return source

    # Group imports by module for cleaner output
    import_by_module: dict[str, list[str]] = {}
    for imp in new_imports:
        match = re.match(r"from ([\w.]+) import (.+)", imp)
        if match:
            module, name = match.groups()
            if module not in import_by_module:
                import_by_module[module] = []
            import_by_module[module].append(name)

    # Build import lines
    import_lines = []
    for module in sorted(import_by_module.keys()):
        names = sorted(import_by_module[module])
        import_lines.append(f"from {module} import {', '.join(names)}")

    import_block = "\n".join(import_lines)

    # Insert after last import
    lines = source.splitlines(keepends=True)
    if last_import_line > 0:
        # Insert after the last import line
        insert_pos = last_import_line
        # Add a newline before if needed
        if insert_pos < len(lines) and lines[insert_pos - 1].strip():
            import_block = "\n" + import_block
        lines.insert(insert_pos, import_block + "\n")
    else:
        # No existing imports, add at the beginning
        # But skip any docstrings or comments at the start
        insert_pos = 0
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped and not stripped.startswith("#") and not stripped.startswith('"""') and not stripped.startswith("'''"):
                insert_pos = i
                break
        lines.insert(insert_pos, import_block + "\n\n")

    return "".join(lines)
