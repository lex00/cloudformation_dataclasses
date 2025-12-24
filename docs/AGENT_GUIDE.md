# AI Agent Guide for cloudformation_dataclasses

This document is for AI coding assistants. Read it when helping users with `cloudformation_dataclasses`.

## When to Use This Guide

Use this guide when users want to:
- **Create a new project** → [Workflow: New Project](#workflow-new-project)
- **Import an existing CloudFormation template** → [Workflow: Import Template](#workflow-import-template)
- **Analyze or refactor existing code** → [Workflow: Refactor Code](#workflow-refactor-code)

---

## Workflow: New Project

When users want to create new CloudFormation resources from scratch.

### Step 1: Determine Requirements

Ask:
- What AWS resources do they need? (S3, Lambda, EC2, etc.)
- What's the project name and environment? (dev, staging, prod)

### Step 2: Generate Skeleton

Run the project generator:

```bash
cfn-dataclasses-init default -o <project_name>/
```

List available skeletons:
```bash
cfn-dataclasses-init --list
```

**Generated project structure:**
```
my_project/
├── pyproject.toml           # Package config (uv/pip)
├── my_project/
│   ├── __init__.py          # Centralized imports from library
│   ├── main.py              # build_template() entry point
│   └── resources/
│       ├── __init__.py      # Auto-discovery: imports all resource files
│       └── bucket.py        # One file per resource
└── tests/
    └── test_my_project.py
```

**How auto-discovery works:**

`resources/__init__.py` imports all resource modules:
```python
from my_project.resources.bucket import *
```

When `main.py` imports from `resources`, all `@cloudformation_dataclass` decorators run, registering each resource in the global registry. Then `Template.from_registry()` collects them all.

**Key pattern:** Import triggers registration. No explicit resource list needed.

### Step 3: Add Resources

For each new resource:

1. **Create a new file** in `resources/` (e.g., `resources/lambda_function.py`)
2. **Add the import** to `resources/__init__.py`
3. **Define wrapper class** with `@cloudformation_dataclass`

```python
# resources/lambda_function.py
from __future__ import annotations
from my_project import *  # Gets all imports from __init__.py

@cloudformation_dataclass
class MyFunction:
    resource: Function
    function_name: str = "my-handler"
    runtime = Runtime.PYTHON3_12
    handler: str = "index.handler"
    role: GetAtt[ExecutionRole] = get_att("Arn")  # Reference another resource
```

Then add to `resources/__init__.py`:
```python
from my_project.resources.lambda_function import *
```

**Key pattern:** Each resource file imports `from my_project import *` to get all library imports.

### Step 4: Add Tags

Define reusable tags as wrapper classes:

```python
@cloudformation_dataclass
class EnvironmentTag:
    resource: Tag
    key = "Environment"
    value = "prod"

@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name = "my-bucket"
    tags = [EnvironmentTag, Tag(key="Team", value="Data")]
```

### Step 5: Build and Validate

```python
from cloudformation_dataclasses.core import Template

# Instantiate resources (triggers auto-registration)
bucket = MyBucket()
policy = MyBucketPolicy()

# Build template from registry
template = Template.from_registry(description="My infrastructure")

# Validate
errors = template.validate()
if errors:
    print("Errors:", errors)
else:
    print(template.to_json())
```

---

## Workflow: Import Template

When users have existing CloudFormation YAML/JSON templates.

### Step 1: Get Template Location

Ask for the template file path or have them paste the content.

### Step 2: Run Importer

```bash
# Generate as package (recommended for larger templates)
cfn-dataclasses-import template.yaml -o my_stack/

# Generate as single file
cfn-dataclasses-import template.yaml -o my_stack.py

# Preview output
cfn-dataclasses-import template.yaml | less
```

### For Multiple Templates (Batch Mode)

```bash
cfn-dataclasses-import /path/to/templates/ -o examples/3rd_party/source/
```

Batch mode automatically:
- Recursively finds all templates
- Creates separate package for each
- Detects attribution from source README/LICENSE
- Logs output to `import.log`

See [IMPORTER.md](IMPORTER.md) for details on batch importing.

### Step 3: Review Generated Code

Check for improvements:
1. **Replace string literals** with type-safe enums
2. **Verify resource references** use `ref()` and `get_att()`

### Step 4: Run Linter

The linter detects common issues:

```python
from cloudformation_dataclasses.linter import lint_code, fix_code

# Check for issues
issues = lint_code(code)
for issue in issues:
    print(f"{issue.line}: {issue.message}")

# Auto-fix
fixed_code = fix_code(code)
```

Common fixes:
- `"AES256"` → `ServerSideEncryption.AES256`
- `"Enabled"` → `BucketVersioningStatus.ENABLED`
- `{"StringEquals": ...}` → `{STRING_EQUALS: ...}`

---

## Workflow: Refactor Code

When users have existing `cloudformation_dataclasses` code to improve.

### Step 1: Check for String Literals

Replace strings with type-safe constants:

| String | Constant |
|--------|----------|
| `"AES256"` | `ServerSideEncryption.AES256` |
| `"aws:kms"` | `ServerSideEncryption.AWS_KMS` |
| `"Enabled"` | `BucketVersioningStatus.ENABLED` |
| `"Suspended"` | `BucketVersioningStatus.SUSPENDED` |
| `"StringEquals"` | `STRING_EQUALS` |
| `"Bool"` | `BOOL` |

### Step 2: Use ref() for Dependencies

```python
# Before
bucket = ref("MyBucket")  # String reference

# After
bucket = ref(MyBucket)  # Class reference (type-safe)
```

### Step 3: Validate

```python
template = Template.from_registry()
errors = template.validate()
assert errors == [], f"Validation errors: {errors}"
```

---

## Pattern Reference

### Required Patterns

1. **Always use wrapper classes** - Never instantiate resources directly:
   ```python
   @cloudformation_dataclass
   class MyBucket:
       resource: Bucket
       bucket_name = "my-bucket"
   ```

2. **Use type-safe constants** - Never use string literals for enums

3. **Use ref() for references** - Not string logical IDs

### Import Quick Reference

| Need | Import From | Examples |
|------|-------------|----------|
| Decorator & helpers | `core` | `cloudformation_dataclass`, `ref`, `get_att` |
| Tag class | `core` | `Tag` |
| Condition operators | `core` | `STRING_EQUALS`, `IP_ADDRESS`, `BOOL` |
| Policy classes | `core` | `PolicyStatement`, `DenyStatement`, `PolicyDocument` |
| Template | `core` | `Template`, `Parameter`, `Output` |
| Intrinsic functions | `intrinsics` | `Sub`, `Ref`, `GetAtt`, `Join`, `If` |
| Pseudo-parameters | `intrinsics` | `AWS_REGION`, `AWS_ACCOUNT_ID`, `AWS_PARTITION` |
| Service resources | `aws.<service>` | `Bucket`, `Instance`, `Function` |
| Service enums | `aws.<service>` | `BucketVersioningStatus`, `ServerSideEncryption` |

### Common Enums

**S3:**
```python
from cloudformation_dataclasses.aws.s3 import (
    ServerSideEncryption,      # .AES256, .AWS_KMS
    BucketVersioningStatus,    # .ENABLED, .SUSPENDED
    BucketCannedACL,           # .PRIVATE, .PUBLIC_READ
)
```

**IAM Conditions:**
```python
from cloudformation_dataclasses.core import (
    STRING_EQUALS, STRING_NOT_EQUALS, STRING_LIKE,
    IP_ADDRESS, ARN_LIKE, ARN_EQUALS, BOOL,
)
```

**Lambda:**
```python
from cloudformation_dataclasses.aws.lambda_ import (
    Runtime,        # .PYTHON3_12, .NODEJS20_X
    Architecture,   # .X86_64, .ARM64
)
```

---

## Test Scenario

Use this test to verify the workflow works correctly.

### Test Prompt

Give this to the agent:

```
Create an S3 bucket with AES256 encryption and versioning enabled.
Add tags for Environment=dev and Project=test-project.

Generate the template and validate it.
```

### Expected Actions

1. Create project with `cfn-dataclasses-init default -o test_bucket/` or write code directly
2. Configure bucket with:
   - `ServerSideEncryption.AES256` (NOT string `"AES256"`)
   - `BucketVersioningStatus.ENABLED` (NOT string `"Enabled"`)
3. Add tags using Tag wrappers or Tag class
4. Build template with `Template.from_registry()`
5. Validate with `template.validate()` - should return `[]`

### Validation Code

```python
# Build and validate
template = Template.from_registry(description="Test S3 bucket")
errors = template.validate()
assert errors == [], f"Validation errors: {errors}"

# Verify JSON serialization
import json
json_output = json.dumps(template.to_dict(), indent=2)
assert "AWS::S3::Bucket" in json_output
print("✓ All validations passed")
```

### Validation Checklist

- [ ] No string literals for enums
- [ ] `template.validate()` returns empty list
- [ ] Template serializes to valid JSON

---

## See Also

- [QUICK_START.md](QUICK_START.md) - Project generator reference
- [IMPORTER.md](IMPORTER.md) - cfn-dataclasses-import command usage
- [LINTER.md](LINTER.md) - Linter rules and auto-fix
