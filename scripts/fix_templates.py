#!/usr/bin/env python3
"""Apply known fixes to CloudFormation templates in-place.

This script fixes known issues in third-party CloudFormation templates
before importing them. Run this before the import to ensure templates
can be parsed correctly.
"""

import re
from collections import defaultdict
from pathlib import Path


def rename_duplicate_templates(source_dir: Path) -> int:
    """Rename templates with duplicate base names to avoid collisions.

    When multiple templates have the same filename (e.g., example.yaml in
    different directories), they would all generate packages with the same
    name, causing file collisions. This function renames them with numeric
    suffixes (example_1.yaml, example_2.yaml, etc.).

    Returns:
        Count of files renamed.
    """
    # Find all yaml files and group by basename
    templates_by_name: dict[str, list[Path]] = defaultdict(list)
    for template_path in source_dir.rglob("*.yaml"):
        templates_by_name[template_path.name].append(template_path)

    renamed_count = 0
    for name, paths in templates_by_name.items():
        if len(paths) > 1:
            # Multiple templates with same name - rename them
            stem = Path(name).stem
            suffix = Path(name).suffix
            for i, path in enumerate(sorted(paths), start=1):
                new_name = f"{stem}_{i}{suffix}"
                new_path = path.parent / new_name
                path.rename(new_path)
                print(f"  Renamed: {path.name} -> {new_name}")
                renamed_count += 1

    return renamed_count


def fix_efs_with_automount(content: str) -> str:
    """Fix JSON array syntax in YAML literal block.

    The template incorrectly uses JSON array syntax inside a YAML literal block:
        UserData: !Base64
          Fn::Sub: |-
            "#!/bin/bash -x\\n",
            "export LC_CTYPE=en_US.UTF-8\\n",

    This converts it to proper YAML multi-line string:
        UserData: !Base64
          Fn::Sub: |-
            #!/bin/bash -x
            export LC_CTYPE=en_US.UTF-8
    """
    return re.sub(r'^(\s*)"(.*)\\n",?$', r'\1\2', content, flags=re.MULTILINE)


# Map of template filename -> fix function
FIXES = {
    "efs_with_automount_to_ec2.yaml": fix_efs_with_automount,
}


def apply_fixes(source_dir: Path) -> int:
    """Apply all known fixes to templates in source_dir.

    Returns:
        Count of fixes applied.
    """
    fixed_count = 0

    # First, rename duplicate templates to avoid package name collisions
    fixed_count += rename_duplicate_templates(source_dir)

    # Then apply content fixes
    for template_path in source_dir.rglob("*.yaml"):
        fix_func = FIXES.get(template_path.name)
        if fix_func:
            content = template_path.read_text()
            fixed = fix_func(content)
            if fixed != content:
                template_path.write_text(fixed)
                print(f"  Fixed: {template_path.name}")
                fixed_count += 1
    return fixed_count


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <source_dir>", file=sys.stderr)
        sys.exit(1)

    source_dir = Path(sys.argv[1])
    if not source_dir.is_dir():
        print(f"Error: {source_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    count = apply_fixes(source_dir)
    if count > 0:
        print(f"Applied {count} fix(es)")
    else:
        print("No fixes needed")
