# Linter for cloudformation_dataclasses

The linter detects common mistakes in Python code that uses cloudformation_dataclasses and automatically fixes them to use type-safe constants, enums, and PropertyType classes.

## Why Use the Linter?

When writing CloudFormation templates with cloudformation_dataclasses, it's easy to accidentally use string literals instead of the library's type-safe constants. For example:

```python
# Common mistake - string literal
sse_algorithm = "AES256"

# Better - type-safe enum constant
sse_algorithm = ServerSideEncryption.AES256
```

The linter catches these patterns and can automatically fix them, ensuring your code:
- Uses type-safe constants with IDE autocompletion
- Catches typos at "compile time" rather than CloudFormation deploy time
- Is consistent with library best practices

## Lint Rules

The linter includes 5 rules:

| Rule ID | Name | Detects | Suggests |
|---------|------|---------|----------|
| CFD001 | StringShouldBeConditionOperator | `{"Bool": {...}}` | `{BOOL: {...}}` |
| CFD002 | StringShouldBeParameterType | `type = "String"` | `type = STRING` |
| CFD003 | RefShouldBePseudoParameter | `Ref("AWS::Region")` | `AWS_REGION` |
| CFD004 | StringShouldBeEnum | `sse_algorithm = "AES256"` | `ServerSideEncryption.AES256` |
| CFD005 | DictShouldBePropertyType | `{"ServerSideEncryptionConfiguration": ...}` | `BucketEncryption(...)` |

## Integration with cfn-dataclasses-import

The linter is integrated with the `cfn-dataclasses-import` command and runs automatically by default:

```bash
# Lint is enabled by default
cfn-dataclasses-import template.yaml -o output.py

# Explicitly enable (same as default)
cfn-dataclasses-import template.yaml --lint -o output.py

# Disable linting to see raw generated code
cfn-dataclasses-import template.yaml --no-lint -o output.py
```

## Programmatic Usage

### Linting Code

```python
from cloudformation_dataclasses.linter import lint_code, lint_file

# Lint a code string
issues = lint_code('''
from cloudformation_dataclasses.aws.s3 import Bucket
sse_algorithm = "AES256"
condition = {"Bool": {"key": "value"}}
''')

for issue in issues:
    print(f"{issue.line}:{issue.column} [{issue.rule_id}] {issue.message}")
    print(f"  Replace: {issue.original}")
    print(f"  With:    {issue.suggestion}")

# Lint a file
issues = lint_file("my_template.py")
```

### Fixing Code

```python
from cloudformation_dataclasses.linter import fix_code, fix_file

# Fix a code string
code = '''
sse_algorithm = "AES256"
condition = {"Bool": {"key": "value"}}
'''
fixed = fix_code(code)
print(fixed)
# Output includes:
# - Replaced "AES256" with ServerSideEncryption.AES256
# - Replaced "Bool" with BOOL
# - Added required imports

# Fix a file (returns fixed content)
fixed = fix_file("my_template.py")

# Fix a file in place
fix_file("my_template.py", write=True)
```

### Using with generate_code

The linter is integrated with `generate_code()`:

```python
from cloudformation_dataclasses.importer import parse_template, generate_code

template = parse_template("template.yaml")

# Lint is enabled by default
code = generate_code(template, mode="block")

# Disable linting
code = generate_code(template, mode="block", lint=False)
```

## Available Constants

### Condition Operators (IAM Policies)

Import from `cloudformation_dataclasses.core.constants`:

| Constant | Value |
|----------|-------|
| `BOOL` | `"Bool"` |
| `STRING_EQUALS` | `"StringEquals"` |
| `STRING_NOT_EQUALS` | `"StringNotEquals"` |
| `STRING_LIKE` | `"StringLike"` |
| `STRING_NOT_LIKE` | `"StringNotLike"` |
| `IP_ADDRESS` | `"IpAddress"` |
| `ARN_EQUALS` | `"ArnEquals"` |
| `ARN_LIKE` | `"ArnLike"` |

For less common operators, use `ConditionOperator.OPERATOR_NAME`.

### Parameter Types

Import from `cloudformation_dataclasses.core.constants`:

| Constant | Value |
|----------|-------|
| `STRING` | `"String"` |
| `NUMBER` | `"Number"` |

For AWS-specific types, use `ParameterType.AWS_EC2_VPC_ID`, etc.

### IP Protocols (Security Groups)

Import from `cloudformation_dataclasses.core.constants`:

| Constant | Value |
|----------|-------|
| `IpProtocol.TCP` | `"tcp"` |
| `IpProtocol.UDP` | `"udp"` |
| `IpProtocol.ICMP` | `"icmp"` |
| `IpProtocol.ICMPV6` | `"icmpv6"` |
| `IpProtocol.ALL` | `"-1"` |

### Pseudo-Parameters

Import from `cloudformation_dataclasses.intrinsics`:

| Constant | Equivalent |
|----------|------------|
| `AWS_REGION` | `Ref("AWS::Region")` |
| `AWS_STACK_NAME` | `Ref("AWS::StackName")` |
| `AWS_ACCOUNT_ID` | `Ref("AWS::AccountId")` |
| `AWS_PARTITION` | `Ref("AWS::Partition")` |
| `AWS_STACK_ID` | `Ref("AWS::StackId")` |
| `AWS_URL_SUFFIX` | `Ref("AWS::URLSuffix")` |
| `AWS_NO_VALUE` | `Ref("AWS::NoValue")` |
| `AWS_NOTIFICATION_ARNS` | `Ref("AWS::NotificationARNs")` |

### Service Enums

Each AWS service module includes enum classes for constrained string values:

```python
# S3
from cloudformation_dataclasses.aws.s3 import (
    ServerSideEncryption,  # AES256, AWS_KMS, AWS_KMS_DSSE
    BucketVersioningStatus,  # ENABLED, SUSPENDED
)

# DynamoDB
from cloudformation_dataclasses.aws.dynamodb import (
    KeyType,  # HASH, RANGE
    AttributeType,  # S, N, B
    BillingMode,  # PROVISIONED, PAY_PER_REQUEST
    ProjectionType,  # ALL, KEYS_ONLY, INCLUDE
)

# Lambda
from cloudformation_dataclasses.aws.lambda_ import (
    Runtime,  # PYTHON3_12, NODEJS20_X, etc.
)
```

## LintIssue Structure

Each issue returned by `lint_code()` has:

```python
@dataclass
class LintIssue:
    rule_id: str       # e.g., "CFD001"
    message: str       # Human-readable description
    line: int          # Line number (1-indexed)
    column: int        # Column number (0-indexed)
    original: str      # Original code pattern
    suggestion: str    # Suggested replacement
    fix_imports: list[str]  # Imports needed for the fix
```

## Custom Rules

You can run specific rules:

```python
from cloudformation_dataclasses.linter import (
    lint_code,
    StringShouldBeEnum,
    StringShouldBeConditionOperator,
)

# Only check for enum issues
issues = lint_code(code, rules=[StringShouldBeEnum()])

# Check enum and condition operator issues
issues = lint_code(code, rules=[
    StringShouldBeEnum(),
    StringShouldBeConditionOperator(),
])
```

## Best Practices

1. **Always run with linting enabled** when using `cfn-dataclasses-import` - it's on by default
2. **Review generated code** after import to understand the structure
3. **Use IDE autocompletion** with enum and constant classes to discover valid values
4. **Prefer type-safe constants** over string literals for:
   - Parameter types (`STRING`, `NUMBER`, `ParameterType.*`)
   - Condition operators (`BOOL`, `STRING_EQUALS`, etc.)
   - Pseudo-parameters (`AWS_REGION`, `AWS_STACK_NAME`, etc.)
   - Service-specific enums (`ServerSideEncryption.AES256`, etc.)

## See Also

- [Forward References](./FORWARD_REFERENCES.md) - Cross-module resource references with `Ref[T]` and `GetAtt[T]` (not handled by linter)
- [Agent Guide](./AGENT_GUIDE.md) - Workflows for AI assistants
- [IMPORTER.md](IMPORTER.md) - Full importer documentation
- [README.md](../README.md) - Library overview
