# Plan: Import Workflow Automation

This document outlines planned improvements to automate the `cfn-import` workflow.

## Current Pain Points

1. **Manual post-import steps** - After running `cfn-import`, users must manually verify, type-check, and lint the generated code
2. **No batch import** - Importing multiple templates requires manual repetition of the same commands
3. **No built-in validation** - Generated code issues aren't caught until runtime
4. **Manual test generation** - Every example needs the same boilerplate tests written by hand

## Proposed Improvements

### 1. `--validate` Flag (Priority: High)

Add a `--validate` flag to `cfn-import` that automatically verifies generated code works.

**Usage:**
```bash
cfn-import template.yaml -o my_project/ --validate
# Generated: my_project/__init__.py
# Generated: my_project/resources/*.py
# ...
# Validating... ✓ Template builds successfully (12 resources)
```

**Behavior:**
- Import the generated module
- Call `build_template()`
- Run `template.validate()` if available
- Report success/failure with resource count

**Files to modify:**
- `src/cloudformation_dataclasses/importer/cli.py`

**Implementation:**
```python
if args.validate:
    import importlib.util
    import sys

    # Add output directory to path
    sys.path.insert(0, str(output_dir.parent))

    # Import the generated module
    spec = importlib.util.spec_from_file_location(
        output_dir.name,
        output_dir / "__init__.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Import main and call build_template
    main_spec = importlib.util.spec_from_file_location(
        f"{output_dir.name}.main",
        output_dir / "main.py"
    )
    main_module = importlib.util.module_from_spec(main_spec)
    main_spec.loader.exec_module(main_module)

    template = main_module.build_template()
    print(f"✓ Template builds successfully ({len(template.resources)} resources)")
```

### 2. `--with-tests` Flag (Priority: Medium)

Auto-generate a `tests/` directory with basic validation tests.

**Usage:**
```bash
cfn-import template.yaml -o my_project/ --with-tests
```

**Generated files:**
- `tests/__init__.py`
- `tests/conftest.py` - Registry isolation fixture
- `tests/test_template.py` - Basic validation tests

**Files to modify:**
- `src/cloudformation_dataclasses/importer/cli.py`
- `src/cloudformation_dataclasses/importer/codegen.py`

**New templates to add:**
- `src/cloudformation_dataclasses/package_templates/tests/__init__.py.template`
- `src/cloudformation_dataclasses/package_templates/tests/conftest.py.template`
- `src/cloudformation_dataclasses/package_templates/tests/test_template.py.template`

**Test template content:**
```python
"""Tests for {{project_name}} CloudFormation template."""

import pytest
from {{project_name}}.main import build_template


class TestTemplateStructure:
    """Test basic template structure."""

    def test_template_builds(self):
        """Template builds without errors."""
        template = build_template()
        assert template is not None

    def test_resources_present(self):
        """Template has expected resources."""
        template = build_template()
        assert len(template.resources) == {{resource_count}}

    def test_template_has_description(self):
        """Template has a description."""
        template = build_template()
        assert template.description


class TestTemplateValidation:
    """Test template validation."""

    def test_validation_passes(self):
        """Template passes validation."""
        template = build_template()
        errors = template.validate()
        assert errors == []

    def test_to_dict_succeeds(self):
        """Template can be serialized to dict."""
        template = build_template()
        result = template.to_dict()
        assert "Resources" in result
        assert len(result["Resources"]) == {{resource_count}}
```

### 3. Batch Import Script (Priority: Medium)

Create `scripts/batch-import.sh` for importing multiple templates at once.

**Usage:**
```bash
./scripts/batch-import.sh /path/to/templates examples/output/
# Importing template1.yaml... ✓
# Importing template2.yaml... ✓
# Summary: 2/2 succeeded
```

**Script outline:**
```bash
#!/bin/bash
set -e

SOURCE_DIR="$1"
OUTPUT_DIR="$2"

if [ -z "$SOURCE_DIR" ] || [ -z "$OUTPUT_DIR" ]; then
    echo "Usage: $0 <source_dir> <output_dir>"
    exit 1
fi

SUCCESS=0
FAILED=0

for template in $(find "$SOURCE_DIR" -maxdepth 1 -name "*.yaml" -o -name "*.json"); do
    name=$(basename "$template" | sed 's/\.[^.]*$//' | tr '-' '_' | tr '[:upper:]' '[:lower:]')
    echo -n "Importing $template... "

    if uv run cfn-import "$template" -o "$OUTPUT_DIR/$name/" --validate 2>/dev/null; then
        echo "✓"
        ((SUCCESS++))
    else
        echo "✗"
        ((FAILED++))
    fi
done

echo ""
echo "Summary: $SUCCESS succeeded, $FAILED failed"
```

### 4. Test Script Enhancement (Priority: Low)

Add `--validate-examples` flag to `scripts/test.sh`.

**Usage:**
```bash
./scripts/test.sh --validate-examples
```

**Behavior:**
- Discover all examples in `examples/` directory
- For each example, import and run `build_template()`
- Report success/failure summary

**Files to modify:**
- `scripts/test.sh`

## Implementation Order

| Priority | Feature | Effort | Impact |
|----------|---------|--------|--------|
| 1 | `--validate` flag | Low | High - Catches errors immediately |
| 2 | `--with-tests` flag | Medium | Medium - Reduces boilerplate |
| 3 | `batch-import.sh` | Low | Medium - Useful for collections |
| 4 | `test.sh --validate-examples` | Low | Low - CI integration |

## Future Considerations

- **`--lint` flag** - Run ruff on generated code
- **`--type-check` flag** - Run mypy on generated code
- **`--format` flag** - Run black on generated code
- **Watch mode** - Re-import when source template changes
- **Diff mode** - Show changes when re-importing
