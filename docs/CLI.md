# CLI Reference

The `cfn-dataclasses` command provides three subcommands for working with CloudFormation templates.

## Quick Reference

| Command | Description |
|---------|-------------|
| `cfn-dataclasses init -o <path>` | Create new project skeleton |
| `cfn-dataclasses import <template> -o <path>` | Convert YAML/JSON template to Python |
| `cfn-dataclasses lint <path> [--fix]` | Check and auto-fix code style |

```bash
cfn-dataclasses --version  # Show version
cfn-dataclasses --help     # Show help
```

---

## init

Create a new project skeleton with all the scaffolding you need.

```bash
cfn-dataclasses init -o my_stack/
cfn-dataclasses init -o my_stack/ --project-name analytics
```

### Options

| Option | Description |
|--------|-------------|
| `-o, --output PATH` | Output directory (required) |
| `--project-name NAME` | Project name (defaults to directory name) |

### Generated Structure

```
my_stack/
├── pyproject.toml           # Package config with uv/pip support
├── my_stack/
│   ├── __init__.py          # Centralized imports + setup_resources()
│   ├── __init__.pyi         # Type stubs
│   ├── __main__.py          # For `python -m my_stack` (uses run_package_cli())
│   └── main.py              # Your resources go here
```

See [Quick Start](QUICK_START.md) for a walkthrough of adding your first resource.

---

## import

Convert existing CloudFormation YAML/JSON templates to Python code.

```bash
# Single file to package (recommended)
cfn-dataclasses import template.yaml -o my_stack/

# Single file to single Python file
cfn-dataclasses import template.yaml -o my_stack.py

# Preview output
cfn-dataclasses import template.yaml | less

# Batch import directory
cfn-dataclasses import /path/to/templates/ -o output/
```

### Options

| Option | Description |
|--------|-------------|
| `-o, --output PATH` | Output path: directory for package, `.py` for single file |
| `--project-name NAME` | Project name (defaults to output directory name) |
| `--no-main` | Omit `if __name__ == '__main__'` block (single-file only) |
| `--skip-checks` | Skip validation, linting, and test generation |

### Output Mode Detection

| Output Path | Generated Format |
|-------------|------------------|
| `-o my_stack/` | Package (directory with multiple files) |
| `-o output.py` | Single file |
| No `-o` (stdout) | Single file |

### Package Output

When outputting to a directory, resources are organized by AWS service category in a flat structure:

```
my_stack/
├── pyproject.toml
├── original/template.yaml     # Source preserved
├── my_stack/
│   ├── __init__.py            # Centralized imports + setup_resources()
│   ├── __init__.pyi           # Type stubs
│   ├── __main__.py            # Uses run_package_cli()
│   ├── params.py              # Parameters, Mappings, Conditions
│   ├── outputs.py             # Output definitions
│   ├── compute.py             # Lambda, EC2, ECS
│   ├── network.py             # VPC, Subnets, Security Groups
│   ├── storage.py             # S3, EFS
│   ├── database.py            # RDS, DynamoDB
│   └── main.py                # Uncategorized resources
```

**Key pattern: Single import.** Resource files use `from . import *` to get everything they need.

### Batch Mode

Import multiple templates from a directory:

```bash
cfn-dataclasses import /path/to/templates/ -o examples/output/
```

Batch mode automatically:
- Recursively finds all `.yaml`, `.yml`, and `.json` templates
- Creates separate package for each template
- Detects attribution from source README/LICENSE
- Logs output to `import.log`
- Continues on error

### Intrinsic Functions

All CloudFormation intrinsic functions are supported:

| Function | YAML Tag | Long Form |
|----------|----------|-----------|
| Ref | `!Ref` | `Fn::Ref` |
| GetAtt | `!GetAtt` | `Fn::GetAtt` |
| Sub | `!Sub` | `Fn::Sub` |
| Join | `!Join` | `Fn::Join` |
| If | `!If` | `Fn::If` |
| Equals | `!Equals` | `Fn::Equals` |
| And/Or/Not | `!And` | `Fn::And` |
| FindInMap | `!FindInMap` | `Fn::FindInMap` |
| Select | `!Select` | `Fn::Select` |
| Split | `!Split` | `Fn::Split` |
| Base64 | `!Base64` | `Fn::Base64` |
| Cidr | `!Cidr` | `Fn::Cidr` |
| GetAZs | `!GetAZs` | `Fn::GetAZs` |
| ImportValue | `!ImportValue` | `Fn::ImportValue` |

---

## lint

Detect common mistakes and auto-fix them to use type-safe constants.

```bash
# Check a file or directory
cfn-dataclasses lint my_stack/

# Auto-fix issues in place
cfn-dataclasses lint my_stack/ --fix
```

### Options

| Option | Description |
|--------|-------------|
| `--fix` | Auto-fix issues in place |

### Lint Rules

| Rule | Detects | Suggests |
|------|---------|----------|
| CFD001 | `{"Bool": {...}}` | `{BOOL: {...}}` |
| CFD002 | `type = "String"` | `type = STRING` |
| CFD003 | `Ref("AWS::Region")` | `AWS_REGION` |
| CFD004 | `sse_algorithm = "AES256"` | `ServerSideEncryption.AES256` |
| CFD005 | `{"ServerSideEncryptionConfiguration": ...}` | `BucketEncryption(...)` |

### Output Examples

**No issues:**
```
$ cfn-dataclasses lint my_project/
✓ No issues found
```

**With issues:**
```
$ cfn-dataclasses lint my_project/
my_project/stack/storage.py:15:20: CFD004 Use ServerSideEncryption.AES256 instead of "AES256"

Found 1 issue in 1 file
```

**With --fix:**
```
$ cfn-dataclasses lint my_project/ --fix
Fixed my_project/stack/storage.py (1 issue)

Fixed 1 issue in 1 file
```

### Integration with import

The linter runs automatically when using `cfn-dataclasses import`. Use `--skip-checks` to disable.

---

## Available Constants

### Condition Operators (IAM Policies)

```python
from cloudformation_dataclasses.core.constants import (
    BOOL, STRING_EQUALS, STRING_NOT_EQUALS, STRING_LIKE,
    IP_ADDRESS, ARN_EQUALS, ARN_LIKE,
)
```

### Parameter Types

```python
from cloudformation_dataclasses.core.constants import STRING, NUMBER
```

### Pseudo-Parameters

```python
from cloudformation_dataclasses.intrinsics import (
    AWS_REGION, AWS_STACK_NAME, AWS_ACCOUNT_ID,
    AWS_PARTITION, AWS_STACK_ID, AWS_URL_SUFFIX,
)
```

### Service Enums

Each AWS service module includes enum classes. Available via the single import pattern:

```python
# S3
ServerSideEncryption.AES256, ServerSideEncryption.AWS_KMS
BucketVersioningStatus.ENABLED, BucketVersioningStatus.SUSPENDED

# DynamoDB
KeyType.HASH, KeyType.RANGE
AttributeType.S, AttributeType.N, AttributeType.B
BillingMode.PROVISIONED, BillingMode.PAY_PER_REQUEST

# Lambda
Runtime.PYTHON3_12, Runtime.NODEJS20_X
Architecture.X86_64, Architecture.ARM64
```

---

## Programmatic Usage

### Import API

```python
from pathlib import Path
from cloudformation_dataclasses.importer.parser import parse_template
from cloudformation_dataclasses.importer.codegen import generate_code, generate_package

# Parse a template
template = parse_template(Path("template.yaml"))

# Generate single file
code = generate_code(template, include_main=True)

# Generate package (multiple files)
files = generate_package(template, package_name="my_stack")
for filename, content in files.items():
    print(f"=== {filename} ===")
```

### Lint API

```python
from cloudformation_dataclasses.linter import lint_code, fix_code

# Check for issues
issues = lint_code(code)
for issue in issues:
    print(f"{issue.line}: {issue.message}")

# Auto-fix
fixed_code = fix_code(code)
```

---

## See Also

- [Quick Start](QUICK_START.md) - Create your first project
- [Registry](REGISTRY.md) - Multi-file organization
- [Examples](../examples/) - Real-world templates
