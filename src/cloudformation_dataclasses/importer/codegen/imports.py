"""Import statement generation."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .context import CodegenContext


def generate_imports(ctx: "CodegenContext") -> str:
    """Generate import statements."""
    lines = []

    # Group imports by package
    core_imports = ctx.imports.get("cloudformation_dataclasses.core", set())
    if core_imports:
        sorted_imports = sorted(core_imports)
        if len(sorted_imports) <= 3:
            lines.append(f"from cloudformation_dataclasses.core import {', '.join(sorted_imports)}")
        else:
            lines.append("from cloudformation_dataclasses.core import (")
            for name in sorted_imports:
                lines.append(f"    {name},")
            lines.append(")")

    # AWS module imports
    aws_modules = sorted(
        (mod, names)
        for mod, names in ctx.imports.items()
        if mod.startswith("cloudformation_dataclasses.aws.")
    )
    for module, names in aws_modules:
        sorted_names = sorted(names)
        if len(sorted_names) <= 3:
            lines.append(f"from {module} import {', '.join(sorted_names)}")
        else:
            lines.append(f"from {module} import (")
            for name in sorted_names:
                lines.append(f"    {name},")
            lines.append(")")

    # Intrinsic imports
    if ctx.intrinsic_imports:
        sorted_intrinsics = sorted(ctx.intrinsic_imports)
        if len(sorted_intrinsics) <= 3:
            lines.append(
                f"from cloudformation_dataclasses.intrinsics import {', '.join(sorted_intrinsics)}"
            )
        else:
            lines.append("from cloudformation_dataclasses.intrinsics import (")
            for name in sorted_intrinsics:
                lines.append(f"    {name},")
            lines.append(")")

    return "\n".join(lines)
