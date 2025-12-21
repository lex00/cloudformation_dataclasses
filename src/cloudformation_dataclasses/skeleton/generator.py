"""Skeleton generator - copies template files with variable substitution."""

from __future__ import annotations

import re
from importlib import resources
from pathlib import Path
from typing import NamedTuple


class SkeletonInfo(NamedTuple):
    """Information about an available skeleton."""

    name: str
    description: str


# Map skeleton names to their descriptions
SKELETON_DESCRIPTIONS: dict[str, str] = {
    "s3_bucket": "S3 bucket with encryption, versioning, and bucket policy",
}


def list_skeletons() -> list[SkeletonInfo]:
    """List all available skeleton templates.

    Returns:
        List of SkeletonInfo with name and description.
    """
    skeletons_pkg = resources.files("cloudformation_dataclasses.skeleton.templates")

    available = []
    for item in skeletons_pkg.iterdir():
        if item.is_dir() and not item.name.startswith("_"):
            description = SKELETON_DESCRIPTIONS.get(item.name, "No description")
            available.append(SkeletonInfo(name=item.name, description=description))

    return sorted(available, key=lambda s: s.name)


def _to_pascal_case(name: str) -> str:
    """Convert snake_case or kebab-case to PascalCase.

    Examples:
        my_project -> MyProject
        my-project -> MyProject
    """
    # Replace hyphens with underscores, then capitalize each word
    words = name.replace("-", "_").split("_")
    return "".join(word.capitalize() for word in words)


def _substitute_variables(content: str, variables: dict[str, str]) -> str:
    """Substitute {{variable}} placeholders in content.

    Args:
        content: Template content with {{variable}} placeholders.
        variables: Map of variable names to values.

    Returns:
        Content with placeholders replaced.
    """

    def replace(match: re.Match[str]) -> str:
        var_name = match.group(1)
        if var_name in variables:
            return variables[var_name]
        # Leave unrecognized variables as-is
        return match.group(0)

    return re.sub(r"\{\{(\w+)\}\}", replace, content)


def generate_skeleton(
    skeleton_name: str,
    output_dir: Path,
    *,
    project_name: str = "my_project",
    component: str = "MyComponent",
    stage: str = "dev",
    region: str = "us-east-1",
) -> list[Path]:
    """Generate a project skeleton from a template.

    Args:
        skeleton_name: Name of the skeleton (e.g., "s3_bucket").
        output_dir: Directory to write generated files to.
        project_name: Project name for naming pattern (default: "my_project").
        component: Component name (default: "MyComponent").
        stage: Deployment stage (default: "dev").
        region: AWS region (default: "us-east-1").

    Returns:
        List of created file paths.

    Raises:
        ValueError: If skeleton_name is not found.
    """
    # Normalize skeleton name (allow hyphens or underscores)
    skeleton_name = skeleton_name.replace("-", "_")

    # Get skeleton package
    try:
        skeleton_pkg = resources.files(
            f"cloudformation_dataclasses.skeleton.templates.{skeleton_name}"
        )
    except ModuleNotFoundError:
        available = [s.name for s in list_skeletons()]
        raise ValueError(
            f"Unknown skeleton: {skeleton_name!r}. "
            f"Available: {', '.join(available) or 'none'}"
        ) from None

    # Build variable substitution map
    variables = {
        "project_name": project_name,
        "ProjectName": _to_pascal_case(project_name),
        "component": component,
        "stage": stage,
        "region": region,
    }

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    created_files: list[Path] = []

    # Process each template file (skip package infrastructure files)
    for item in skeleton_pkg.iterdir():
        # Skip Python package infrastructure (not templates)
        if item.name in ("__init__.py", "__pycache__"):
            continue
        if item.is_dir():
            continue

        # Read template content
        content = item.read_text()

        # Determine output filename (strip .template suffix if present)
        output_name = item.name
        if output_name.endswith(".template"):
            output_name = output_name[: -len(".template")]

        # Substitute variables
        content = _substitute_variables(content, variables)

        # Write output file
        output_path = output_dir / output_name
        output_path.write_text(content)
        created_files.append(output_path)

    return created_files
