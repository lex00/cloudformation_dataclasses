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
cfn-init s3-bucket -o <project_name>/
```

Available skeletons (check with `cfn-init --list`):
- `s3-bucket` - S3 bucket with encryption, versioning, and bucket policy

Customize with flags:
```bash
cfn-init s3-bucket -o my_project/ \
    --project-name analytics \
    --component storage \
    --stage prod \
    --region us-west-2
```

### Step 3: Customize DeploymentContext

Edit `context.py` to set naming and tags:

```python
@cloudformation_dataclass
class MyProjectContext:
    context: DeploymentContext
    project_name = "my-project"      # Top-level project name
    component = "api"                 # Logical grouping
    stage = "dev"                     # dev, staging, prod
    deployment_name = "001"           # Deployment identifier
    deployment_group = "blue"         # For blue/green deployments
    region = "us-east-1"              # AWS region
    tags = [EnvironmentTag, ProjectTag, ManagedByTag]

# Override at instantiation for different environments:
ctx = MyProjectContext()                    # Use defaults
ctx_prod = MyProjectContext(stage="prod")   # Override stage
```

### Step 4: Add Resources

For each resource, create a wrapper class:

```python
@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    context = ctx  # Use deployment context for naming
    bucket_encryption = MyBucketEncryption
    versioning_configuration = MyVersioningConfiguration
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
cfn-import template.yaml -o my_stack/

# Generate as single file
cfn-import template.yaml -o my_stack.py

# Preview output
cfn-import template.yaml | less
```

### Step 3: Review Generated Code

Check for improvements:
1. **Add DeploymentContext** if not present
2. **Replace string literals** with type-safe enums
3. **Verify resource references** use `ref()` and `get_att()`

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

### Step 2: Add DeploymentContext

If resources don't use context, add one:

```python
# Before
@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name = "my-app-bucket-prod"  # Hardcoded name

# After
@cloudformation_dataclass
class MyContext:
    context: DeploymentContext
    project_name = "my-app"
    stage = "prod"

ctx = MyContext()

@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    context = ctx  # Auto-generates: my-app-MyBucket-prod
```

### Step 3: Use ref() for Dependencies

```python
# Before
bucket = ref("MyBucket")  # String reference

# After
bucket = ref(MyBucket)  # Class reference (type-safe)
```

### Step 4: Validate

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
       context = ctx
   ```

2. **Use DeploymentContext** - For consistent naming and tags

3. **Use type-safe constants** - Never use string literals for enums

4. **Use ref() for references** - Not string logical IDs

### Import Quick Reference

| Need | Import From | Examples |
|------|-------------|----------|
| Decorator & helpers | `core` | `cloudformation_dataclass`, `ref`, `get_att` |
| Deployment context | `core` | `DeploymentContext`, `Tag` |
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
Use a DeploymentContext with:
- project_name: "test-project"
- component: "storage"
- stage: "dev"
- region: "us-east-1"

Generate the template and validate it.
```

### Expected Actions

1. Create project with `cfn-init s3-bucket -o test_bucket/` or write code directly
2. Set DeploymentContext with provided values
3. Configure bucket with:
   - `ServerSideEncryption.AES256` (NOT string `"AES256"`)
   - `BucketVersioningStatus.ENABLED` (NOT string `"Enabled"`)
4. Build template with `Template.from_registry()`
5. Validate with `template.validate()` - should return `[]`

### Validation Code

```python
# Build and validate
template = Template.from_registry(description="Test S3 bucket")
errors = template.validate()
assert errors == [], f"Validation errors: {errors}"

# Check resource naming includes context
bucket = DataBucket()
assert "test-project-storage" in bucket.resource.resource_name

# Verify JSON serialization
import json
json_output = json.dumps(template.to_dict(), indent=2)
assert "AWS::S3::Bucket" in json_output
print("✓ All validations passed")
```

### Validation Checklist

- [ ] No string literals for enums
- [ ] DeploymentContext used with all fields
- [ ] Resource name follows pattern: `test-project-storage-DataBucket-dev-...`
- [ ] `template.validate()` returns empty list
- [ ] Template serializes to valid JSON

---

## See Also

- [QUICK_START.md](QUICK_START.md) - Project generator and DeploymentContext reference
- [IMPORTER.md](IMPORTER.md) - cfn-import command usage
- [LINTER.md](LINTER.md) - Linter rules and auto-fix
