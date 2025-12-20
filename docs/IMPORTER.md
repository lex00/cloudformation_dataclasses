# CloudFormation Template Importer

Convert existing CloudFormation YAML/JSON templates to Python code using `cloudformation_dataclasses`.

## Installation

```bash
# Install with importer support
pip install cloudformation-dataclasses[importer]

# Or with uv
uv pip install cloudformation-dataclasses[importer]
```

## Quick Start

```bash
# Convert a template to Python (after pip install)
cfn-import template.yaml -o my_stack.py

# Or if working from source with uv
uv run cfn-import template.yaml -o my_stack.py

# Read from stdin, write to stdout
cat template.yaml | cfn-import -

# JSON templates work too
cfn-import template.json -o my_stack.py
```

## CLI Reference

```
cfn-import [OPTIONS] INPUT

Arguments:
  INPUT                      Template file path, or "-" for stdin

Options:
  -o, --output PATH          Output file path (default: stdout)
  -m, --mode MODE            Output mode: block, brief, mixed (default: block)
  --no-main                  Omit if __name__ == '__main__' block
  --lint                     Run linter on generated code (default: enabled)
  --no-lint                  Disable linter (output raw generated code)
  --version                  Show version and exit
  --help                     Show this message and exit
```

### Linter Integration

By default, the importer runs the linter on generated code to replace string literals with type-safe constants. For example:

- `"Bool"` → `BOOL` (condition operators)
- `"String"` → `STRING` (parameter types)
- `Ref("AWS::Region")` → `AWS_REGION` (pseudo-parameters)
- `"AES256"` → `ServerSideEncryption.AES256` (service enums)

To disable linting and see the raw generated code:

```bash
cfn-import template.yaml --no-lint -o output.py
```

See [LINTER.md](./LINTER.md) for more details on the linter.

### Examples

```bash
# Generate block mode (default, recommended)
cfn-import vpc.yaml -o infrastructure/vpc.py

# Generate brief mode (imperative style)
cfn-import vpc.yaml --mode brief -o vpc.py

# Generate mixed mode
cfn-import vpc.yaml --mode mixed -o vpc.py

# Omit the main block for library modules
cfn-import vpc.yaml --no-main -o vpc.py

# Pipe for quick preview
cfn-import template.yaml | less
```

## Output Modes

The importer supports three output styles. **Block mode is recommended** as it provides the most readable, maintainable code.

### Block Mode (Default)

Generates declarative wrapper classes using `@cloudformation_dataclass`. Every resource, parameter, and output becomes a separate class.

```bash
cfn-import template.yaml --mode block -o output.py
```

**Input:**
```yaml
Parameters:
  BucketNameParam:
    Type: String
    Default: my-default-bucket

Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Ref BucketNameParam

Outputs:
  BucketArn:
    Value: !GetAtt MyBucket.Arn
```

**Output:**
```python
@cloudformation_dataclass
class BucketNameParam:
    resource: Parameter
    type = 'String'
    default = 'my-default-bucket'


@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name = ref(BucketNameParam)


@cloudformation_dataclass
class BucketArnOutput:
    resource: Output
    value = get_att(MyBucket, "Arn")


@cloudformation_dataclass
class MyTemplate:
    resource: Template
    parameters = [BucketNameParam]
    resources = [MyBucket]
    outputs = [BucketArnOutput]


def build_template() -> Template:
    return MyTemplate().resource


if __name__ == "__main__":
    import json
    print(json.dumps(build_template().to_dict(), indent=2))
```

**Best for:** Team collaboration, reusable components, large templates, maintainability.

### Brief Mode

Generates imperative code with direct object instantiation. No wrapper classes.

```bash
cfn-import template.yaml --mode brief -o output.py
```

**Output:**
```python
bucket_name_param = Parameter(
    logical_id='BucketNameParam',
    type='String',
    default='my-default-bucket',
)

my_bucket = Bucket(
    logical_id='MyBucket',
    bucket_name=ref(bucket_name_param),
)

bucket_arn_output = Output(
    logical_id='BucketArn',
    value=get_att(my_bucket, "Arn"),
)

template = Template(
    parameters=[bucket_name_param],
    resources=[my_bucket],
    outputs=[bucket_arn_output],
)


if __name__ == "__main__":
    import json
    print(json.dumps(template.to_dict(), indent=2))
```

**Best for:** Quick conversions, small templates, prototyping, scripting.

### Mixed Mode

Combines block and brief approaches. Uses wrapper classes for resources, but intelligently inlines certain constructs:

- **Tags**: Inlined if used once, wrapper class if reused (2+ times)
- **Policy Documents**: Uses `PolicyDocument` and `PolicyStatement` classes
- **Resources/Parameters/Outputs**: Always wrapper classes

```bash
cfn-import template.yaml --mode mixed -o output.py
```

**Input (with tags and policy):**
```yaml
Resources:
  ProdBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: prod-bucket
      Tags:
        - Key: Environment
          Value: Production
        - Key: Team
          Value: Platform

  StagingBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: staging-bucket
      Tags:
        - Key: Environment
          Value: Staging
        - Key: Team
          Value: Platform  # Same as ProdBucket - will be extracted

  BucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref ProdBucket
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal: "*"
            Action: s3:GetObject
            Resource: !Sub "${ProdBucket.Arn}/*"
```

**Output:**
```python
# Reused tag extracted to wrapper class
@cloudformation_dataclass
class TeamPlatformTag:
    resource: Tag
    key = 'Team'
    value = 'Platform'


@cloudformation_dataclass
class ProdBucket:
    resource: Bucket
    bucket_name = 'prod-bucket'
    tags = [
        Tag(key='Environment', value='Production'),  # Unique - inlined
        TeamPlatformTag,                              # Reused - reference
    ]


@cloudformation_dataclass
class StagingBucket:
    resource: Bucket
    bucket_name = 'staging-bucket'
    tags = [
        Tag(key='Environment', value='Staging'),     # Unique - inlined
        TeamPlatformTag,                              # Reused - reference
    ]


@cloudformation_dataclass
class BucketPolicy:
    resource: BucketPolicy
    bucket = ref(ProdBucket)
    policy_document = PolicyDocument(statement=[
        PolicyStatement(
            principal='*',
            action='s3:GetObject',
            resource_arn=Sub('${ProdBucket.Arn}/*'),
        ),
    ])
```

**Best for:** Balanced readability with inline convenience for simple constructs.

## Mode Comparison

| Feature | Block | Brief | Mixed |
|---------|-------|-------|-------|
| Resources | Wrapper class | Variable | Wrapper class |
| Parameters | Wrapper class | Variable | Wrapper class |
| Outputs | Wrapper class | Variable | Wrapper class |
| Tags (unique) | Raw dict | Raw dict | `Tag()` inline |
| Tags (reused) | Raw dict | Raw dict | Wrapper class |
| Policy documents | Raw dict | Raw dict | `PolicyDocument()` |
| Policy statements | Raw dict | Raw dict | `PolicyStatement()` |
| Template | Wrapper class | Variable | Wrapper class |
| `build_template()` | Yes | No | Yes |
| Decorator | `@cloudformation_dataclass` | None | `@cloudformation_dataclass` |

### When to Use Each Mode

**Block Mode** (default, recommended)
- Large, complex templates
- Team projects with multiple contributors
- When you need maximum reusability
- When you want consistent, predictable output

**Brief Mode**
- Quick one-off conversions
- Small templates (< 10 resources)
- Scripts and automation
- When you prefer imperative style

**Mixed Mode**
- Medium-sized templates
- When you have repeated tags across resources
- When you want typed policy documents
- Balance between readability and verbosity

## Supported Features

### Intrinsic Functions

The importer handles all CloudFormation intrinsic functions:

| Function | YAML Tag | Long Form |
|----------|----------|-----------|
| Ref | `!Ref` | `Fn::Ref` |
| GetAtt | `!GetAtt` | `Fn::GetAtt` |
| Sub | `!Sub` | `Fn::Sub` |
| Join | `!Join` | `Fn::Join` |
| Select | `!Select` | `Fn::Select` |
| If | `!If` | `Fn::If` |
| Equals | `!Equals` | `Fn::Equals` |
| And | `!And` | `Fn::And` |
| Or | `!Or` | `Fn::Or` |
| Not | `!Not` | `Fn::Not` |
| Condition | `!Condition` | `Fn::Condition` |
| FindInMap | `!FindInMap` | `Fn::FindInMap` |
| GetAZs | `!GetAZs` | `Fn::GetAZs` |
| Base64 | `!Base64` | `Fn::Base64` |
| Cidr | `!Cidr` | `Fn::Cidr` |
| ImportValue | `!ImportValue` | `Fn::ImportValue` |
| Split | `!Split` | `Fn::Split` |
| Transform | `!Transform` | `Fn::Transform` |

### Template Sections

| Section | Supported |
|---------|-----------|
| Parameters | Yes |
| Resources | Yes |
| Outputs | Yes |
| Conditions | Yes |
| Mappings | Yes |
| Description | Yes |

## Code Generation Details

### Naming Conventions

CloudFormation PascalCase names are converted to Python snake_case:

| CloudFormation | Python |
|----------------|--------|
| `BucketName` | `bucket_name` |
| `VPCId` | `vpc_id` |
| `IPv6CidrBlock` | `i_pv6_cidr_block` |

Logical IDs are preserved as class names in block mode:

| Logical ID | Class Name |
|------------|------------|
| `MyBucket` | `class MyBucket:` |
| `VPCStack` | `class VPCStack:` |

### Reference Handling

References are converted to `ref()` and `get_att()` calls:

```yaml
# Input
BucketName: !Ref BucketParam
BucketArn: !GetAtt MyBucket.Arn
```

```python
# Output (block mode)
bucket_name = ref(BucketParam)
bucket_arn = get_att(MyBucket, "Arn")
```

### Resource Ordering

Resources are topologically sorted so dependencies are defined before dependents:

```yaml
Resources:
  BucketPolicy:           # References MyBucket
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref MyBucket
  MyBucket:               # Defined second in YAML
    Type: AWS::S3::Bucket
```

```python
# Output: MyBucket comes first
@cloudformation_dataclass
class MyBucket:
    resource: Bucket

@cloudformation_dataclass
class BucketPolicy:
    resource: BucketPolicy
    bucket = ref(MyBucket)
```

## Project Structure

The importer is located in `src/cloudformation_dataclasses/importer/`:

```
importer/
├── __init__.py      # Package exports
├── ir.py            # Intermediate representation dataclasses
├── parser.py        # YAML/JSON parsing with intrinsic support
├── codegen.py       # Python code generation
└── cli.py           # Command-line interface
```

### Module Overview

**ir.py** - Intermediate Representation

Defines dataclasses for the parsed template structure:
- `IRTemplate` - Complete parsed template
- `IRResource` - Parsed resource with properties
- `IRParameter` - Parsed parameter
- `IROutput` - Parsed output
- `IRCondition` - Parsed condition
- `IRMapping` - Parsed mapping
- `IRIntrinsic` - Parsed intrinsic function
- `IntrinsicType` - Enum of all intrinsic types

**parser.py** - Template Parser

- `parse_template(source, source_name=None)` - Main entry point
- Handles YAML with custom constructors for `!Ref`, `!GetAtt`, etc.
- Handles JSON with `Fn::` prefix detection
- Builds reference graph for dependency ordering

**codegen.py** - Code Generator

- `generate_code(template, mode="block", include_main=True, lint=True)` - Main entry point
- Supports block, brief, and mixed output modes
- Handles imports, class generation, and formatting
- When `lint=True` (default), runs the linter to replace string literals with type-safe constants

**cli.py** - Command Line Interface

- Argument parsing with argparse
- File/stdin input handling
- File/stdout output handling

## Tests

Tests are located in `tests/importer/`:

```
tests/importer/
├── __init__.py
├── test_parser.py       # Parser unit tests
├── test_codegen.py      # Code generator tests
└── templates/           # Test fixtures
    ├── simple_bucket.yaml
    ├── simple_bucket.json
    ├── bucket_with_ref.yaml
    ├── intrinsics.yaml
    ├── bucket_with_tags.yaml
    └── bucket_with_policy.yaml
```

### Running Tests

```bash
# Run all importer tests
uv run pytest tests/importer/ -v

# Run with coverage
uv run pytest tests/importer/ --cov=cloudformation_dataclasses.importer

# Run specific test class
uv run pytest tests/importer/test_codegen.py::TestBriefMode -v
```

### Test Fixtures

**simple_bucket.yaml** - Basic S3 bucket with output
```yaml
Description: Simple S3 bucket
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: my-test-bucket
Outputs:
  BucketName:
    Description: Name of the bucket
    Value: !Ref MyBucket
```

**bucket_with_ref.yaml** - Parameter references and GetAtt
```yaml
Parameters:
  BucketNameParam:
    Type: String
    Default: my-default-bucket
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Ref BucketNameParam
Outputs:
  BucketArn:
    Value: !GetAtt MyBucket.Arn
```

**intrinsics.yaml** - Various intrinsic functions
```yaml
Conditions:
  IsProd: !Equals [!Ref Environment, prod]
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub "${AWS::StackName}-bucket"
  MyQueue:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: !Join ["-", [!Ref AWS::StackName, queue]]
      VisibilityTimeout: !If [IsProd, 300, 30]
```

### Test Categories

**TestToSnakeCase** - Property name conversion
- `BucketName` → `bucket_name`
- `VPCId` → `vpc_id`

**TestParseSimpleBucket** - Basic parsing
- Description extraction
- Resource type parsing
- Property extraction

**TestParseBucketWithRef** - Reference handling
- Parameter parsing
- `!Ref` intrinsic detection
- `!GetAtt` intrinsic detection

**TestParseIntrinsics** - Intrinsic functions
- Condition parsing
- `!Sub`, `!Join`, `!If` handling
- Reference graph building

**TestGenerateSimpleBucket** - Block mode generation
- Docstring generation
- Import statements
- Resource class generation
- Template class generation

**TestBriefMode** - Brief mode generation
- Variable assignments
- No decorator usage
- Direct Template construction

**TestMixedMode** - Mixed mode generation
- Wrapper classes for resources
- Build function generation

**TestMixedModeWithTags** - Tag reuse detection
- Reused tags generate wrapper classes
- Unique tags inlined as `Tag()`
- Correct class references

**TestMixedModeWithPolicies** - Policy document handling
- `PolicyDocument` class usage
- `PolicyStatement` class usage
- Proper field mapping (sid, effect, resource_arn, etc.)

## Limitations

### Not Yet Supported

| Feature | Status |
|---------|--------|
| Live import from AWS | Planned |
| Nested stack flattening | Planned |
| `AWS::CloudFormation::CustomResource` | Emitted as comment |
| `Custom::*` resource types | Emitted as comment |
| SAM resources (`AWS::Serverless::*`) | Not supported |
| CloudFormation Macros | Not supported |

### Known Edge Cases

1. **Snake case collisions**: `MyVPC` and `MyVpc` both become `my_vpc`
2. **Complex GetAtt**: `!GetAtt Foo.Bar.Baz` follows CloudFormation rules (first `.` splits logical ID from attribute)
3. **Circular references**: Warned but not prevented

## Programmatic Usage

You can use the importer as a library:

```python
from pathlib import Path
from cloudformation_dataclasses.importer.parser import parse_template
from cloudformation_dataclasses.importer.codegen import generate_code

# Parse a template file
template = parse_template(Path("template.yaml"))

# Or parse a string
yaml_content = """
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
"""
template = parse_template(yaml_content, source_name="inline.yaml")

# Generate code (linter enabled by default)
code = generate_code(template, mode="block", include_main=True)
print(code)

# Disable linter to see raw generated code
code = generate_code(template, mode="block", lint=False)

# Access the IR directly
for name, resource in template.resources.items():
    print(f"{name}: {resource.resource_type}")
```

## Contributing

When adding new features to the importer:

1. Add test fixtures in `tests/importer/templates/`
2. Add parser tests in `tests/importer/test_parser.py`
3. Add codegen tests in `tests/importer/test_codegen.py`
4. Ensure all generated code compiles: `compile(code, "<test>", "exec")`
5. Run the full test suite: `uv run pytest tests/importer/ -v`
