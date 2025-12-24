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
cfn-dataclasses-import template.yaml -o my_stack.py

# Or if working from source with uv
uv run cfn-dataclasses-import template.yaml -o my_stack.py

# Read from stdin, write to stdout
cat template.yaml | cfn-dataclasses-import -

# JSON templates work too
cfn-dataclasses-import template.json -o my_stack.py
```

## CLI Reference

```
cfn-dataclasses-import [OPTIONS] INPUT

Arguments:
  INPUT                      Template file or directory (batch mode)

Options:
  -o, --output PATH          Output path: directory for package, .py file for single file
                             Default: stdout (single file)
  --no-main                  Omit if __name__ == '__main__' block (single-file only)
  --skip-checks              Skip validation, linting, and test generation
  --version                  Show version and exit
  --help                     Show this message and exit
```

### Output Mode Detection

The importer automatically determines whether to generate a package or single file based on the `-o` path:

| Output Path | Generated Format |
|-------------|------------------|
| `-o my_stack/` | Package (directory with multiple files) |
| `-o output.py` | Single file |
| No `-o` (stdout) | Single file |
| `-o -` (explicit stdout) | Single file |

### Examples

```bash
# Generate as package (default when -o is a directory)
cfn-dataclasses-import vpc.yaml -o infrastructure/vpc/

# Generate as single file (when -o ends with .py)
cfn-dataclasses-import vpc.yaml -o vpc.py

# Omit the main block for library modules
cfn-dataclasses-import vpc.yaml --no-main -o vpc.py

# Pipe for quick preview
cfn-dataclasses-import template.yaml | less
```

### Batch Mode

Import multiple templates from a directory:

```bash
cfn-dataclasses-import /path/to/templates/ -o examples/3rd_party/source_name/
```

**Example output:**
```
Found 5 template(s) in /path/to/templates
Importing vpc.yaml... ✓
Importing lambda.yaml... ✗
Importing s3.yaml... ✓
Importing dynamodb.yaml... ✓
Importing api.yaml... ✓

Summary: 4/5 succeeded
Failed:
  - lambda.yaml: Error parsing template

Log: examples/3rd_party/source_name/import.log
```

**Batch mode automatically:**
- Recursively finds all `.yaml`, `.yml`, and `.json` templates
- Creates separate package for each template
- Detects attribution from source README/LICENSE
- Logs output to `import.log`
- Continues on error (each template is independent)

**Folder structure (nested package):**
```
examples/3rd_party/source_name/
├── import.log           # Batch log file
├── vpc/                 # From vpc.yaml (project root)
│   ├── pyproject.toml   # Portable package config
│   ├── README.md        # Auto-generated with attribution
│   ├── .gitignore       # Python gitignore
│   ├── py.typed
│   ├── mypy.ini
│   ├── CLAUDE.md
│   ├── .vscode/
│   │   └── settings.json
│   ├── original/        # Source template preserved
│   │   └── vpc.yaml
│   ├── tests/           # Auto-generated tests
│   │   ├── __init__.py
│   │   └── test_vpc.py
│   └── vpc/             # Actual Python package
│       ├── __init__.py
│       ├── __main__.py  # For `python -m vpc`
│       ├── config.py
│       ├── main.py
│       └── resources/
│           ├── __init__.py
│           └── *.py
├── s3/                  # From s3.yaml
│   └── ...
└── dynamodb/            # From dynamodb.yaml
    └── ...
```

Each generated package is **portable** - you can copy it into another project and use it directly with `uv run python -m vpc` or `uv run pytest tests/`.

**Attribution detection:**

The importer walks up the directory tree (up to 5 levels) to find attribution info. This handles importing from subdirectories of a repo.

| Source | Extracted Info | Priority |
|--------|---------------|----------|
| `.git/config` | Remote origin URL (GitHub/GitLab) | **Highest** |
| `README.md` | GitHub/GitLab URL (fallback), project name (first heading) | Lower |
| `LICENSE`, `LICENSE.txt`, `LICENSE.md` | License type (MIT, Apache-2.0, GPL, BSD) | - |

Git remote origin takes priority over URLs found in README, ensuring the correct repository is attributed even when the README links to other projects.

Each generated package gets a README with:
- Source attribution and license info
- uv installation requirement with link
- Usage instructions (portable package, run tests, generate template)
- Resource table listing all CloudFormation resources

**Skip checks for debugging:**
```bash
cfn-dataclasses-import /path/to/templates/ -o output/ --skip-checks
```

Skips validation, linting, and test generation.

### Package Output

When the output path is a directory, the importer generates a portable Python package with a nested structure. Each resource gets its own file for better readability and AI-friendly context management.

```bash
cfn-dataclasses-import template.yaml -o my_stack/
```

This generates a **nested package structure**:
```
my_stack/                    # Project root
├── pyproject.toml           # Package config with uv/pip support
├── README.md                # Usage instructions + resource table
├── .gitignore               # Python gitignore
├── original/                # Source template preserved
│   └── template.yaml
├── tests/                   # Auto-generated tests
│   ├── __init__.py
│   └── test_my_stack.py
└── my_stack/                # Actual Python package
    ├── __init__.py          # Centralized imports
    ├── __main__.py          # For `python -m my_stack`
    ├── main.py              # build_template() entry point
    └── stack/               # Parameters, outputs, and resources
        ├── __init__.py      # Re-exports params + resources (via setup_resources)
        ├── params.py        # Parameters, Mappings, Conditions
        ├── outputs.py       # Output definitions (if any)
        ├── main.py          # Resources (SCCs + uncategorized)
        ├── compute.py       # EC2, Lambda, ECS resources (if any)
        ├── network.py       # VPC, Subnet, SecurityGroup resources (if any)
        ├── storage.py       # S3, EFS resources (if any)
        └── database.py      # RDS, DynamoDB resources (if any)
```

Resources are organized by AWS service category for large templates (10+ resources). Smaller templates put all resources in `stack/main.py`.

### File Organization Logic

For templates with 10+ resources, the importer groups resources by AWS service category:

| Category File | AWS Services |
|--------------|--------------|
| `compute.py` | EC2 (instances), Lambda, ECS, EKS, Batch, AutoScaling, ElasticBeanstalk, Lightsail |
| `network.py` | EC2 (VPC, Subnet, SecurityGroup, etc.), ELB, Route53, CloudFront, API Gateway |
| `storage.py` | S3, EFS, FSx, Backup |
| `database.py` | RDS, DynamoDB, ElastiCache, Neptune, DocumentDB, Redshift |
| `security.py` | IAM, Cognito, SecretsManager, KMS, WAF, ACM, SSM |
| `messaging.py` | SNS, SQS, EventBridge, StepFunctions, AppSync |
| `monitoring.py` | CloudWatch, Logs, CloudTrail, X-Ray |
| `cicd.py` | CodeBuild, CodePipeline, CodeCommit, CodeDeploy |
| `infra.py` | CloudFormation, Config, ServiceCatalog |
| `main.py` | Uncategorized services + resources with circular dependencies |

**Circular Dependencies (SCCs)**

When resources have circular references (A → B → C → A), they form a *Strongly Connected Component* (SCC). The importer detects these cycles and places all resources in an SCC together in `main.py` to avoid Python import errors.

For example, if a Lambda function references an S3 bucket, and the bucket's notification configuration references the Lambda:
```yaml
# Circular: Lambda → Bucket → Lambda
MyFunction:
  Type: AWS::Lambda::Function
  Properties:
    Environment:
      Variables:
        BUCKET: !Ref MyBucket

MyBucket:
  Type: AWS::S3::Bucket
  Properties:
    NotificationConfiguration:
      LambdaConfigurations:
        - Function: !GetAtt MyFunction.Arn
```

Both resources go to `main.py` even though Lambda is normally in `compute.py` and S3 in `storage.py`.

**Run the generated package:**
```bash
cd my_stack/
uv run python -m my_stack     # Generate CloudFormation JSON
uv run pytest tests/ -v       # Run tests (pytest auto-installed)
```

**`__init__.py`** - Centralizes all imports:
```python
"""My Stack - generated by cfn-dataclasses-import."""
from cloudformation_dataclasses.core import (
    cloudformation_dataclass, ref, get_att, Template, Parameter, ...
)
from cloudformation_dataclasses.aws.s3 import Bucket, BucketEncryption, ...
from cloudformation_dataclasses.intrinsics import Sub, AWS_ACCOUNT_ID, ...

__all__ = [...]
```

**`stack/params.py`** - Parameters and configuration:
```python
"""Parameters, Mappings, and Conditions."""
from .. import *  # noqa: F403

@cloudformation_dataclass
class AppName:
    resource: Parameter
    type = STRING
    description = "Application name"
```

**`stack/main.py`** (or `stack/storage.py` for large templates) - Resources with PropertyType wrappers:
```python
"""Stack resources."""
from .. import *  # noqa: F403

@cloudformation_dataclass
class MyBucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256

@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name = Sub("${AppName}-data")
    bucket_encryption = MyBucketServerSideEncryptionByDefault
    logging_configuration = LoggingConfiguration(
        destination_bucket_name=ref(MyLogBucket)
    )
```

**`stack/__init__.py`** - Re-exports params and uses dynamic resource loading:
```python
"""Stack - parameters, outputs, and resources."""
from .params import *  # noqa: F403, F401

# Import resources with topological ordering
from cloudformation_dataclasses.core.resource_loader import setup_resources
setup_resources(__file__, __name__, globals())

# Import outputs after resources (outputs reference resource classes)
try:
    from .outputs import *  # noqa: F403, F401
except ImportError:
    pass
```

**`stack/outputs.py`** - Output definitions (generated only if template has outputs):
```python
"""Template outputs."""
from .. import *  # noqa: F403

@cloudformation_dataclass
class BucketArnOutput:
    resource: Output
    value = get_att(MyBucket, ARN)  # ARN constant for type safety
```

**`main.py`** - Template builder and entry point:
```python
"""Template builder."""
from . import *  # noqa: F403, F401

def build_template() -> Template:
    return Template.from_registry(
        description="...",
        parameters=[AppName],
        outputs=[BucketArnOutput],
    )

def main() -> None:
    import json
    print(json.dumps(build_template().to_dict(), indent=2))

if __name__ == "__main__":
    main()
```

**Benefits:**
- **Service-based organization** - Resources grouped by AWS service category (compute, network, storage, etc.)
- **AI-friendly** - Agents can work on one category at a time within context limits
- **Clear ownership** - Easy to find where a resource is defined
- **Natural grouping** - PropertyType wrappers stay with their parent resource
- **Dynamic loading** - `setup_resources()` handles topological ordering automatically
- Cleaner imports with `from . import *`
- Logical separation of params, resources, outputs, and main

## Output Style

The importer generates declarative wrapper classes using `@cloudformation_dataclass`. Every resource, parameter, output, and PropertyType becomes a separate class with explicit type declarations.

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

**Best for:** Team collaboration, reusable components, large templates, maintainability, maximum type safety.

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

Logical IDs are preserved as class names:

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
# Output
bucket_name = ref(BucketParam)
bucket_arn = get_att(MyBucket, ARN)  # ARN constant for type safety
```

### Smart Pattern Detection

The importer automatically detects and improves common CloudFormation patterns:

**Implicit Refs**: When a `!Sub` pattern matches a resource's name, it's replaced with `ref()`:
```yaml
# Input - Author used !Sub instead of !Ref
BucketName: !Sub ${AppName}-${AWS::Region}  # On S3 bucket
Bucket: !Sub ${AppName}-${AWS::Region}       # On bucket policy (same pattern!)
```
```python
# Output - Importer detects the relationship
bucket_name = Sub('${AppName}-${AWS::Region}')  # Original stays
bucket = ref(ObjectStorageBucket)               # Replaced with ref()
```

**ARN Detection**: When a `!Sub` builds an ARN, it's replaced with `get_att()`:
```yaml
# Input - Manual ARN construction
Resource:
  - !Sub arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}
  - !Sub arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}/*
```
```python
# Output - Uses get_att() and Join() for cleaner code
resource_arn = [
    get_att(ObjectStorageBucket, ARN),
    Join('', [get_att(ObjectStorageBucket, ARN), '/*']),
]
```

These optimizations happen automatically and create proper CloudFormation dependency relationships.

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
├── cli.py           # Command-line interface
└── codegen/         # Python code generation (package with 8 modules)
    ├── __init__.py  # Public API: generate_code(), generate_package()
    ├── context.py   # CodegenContext, PackageContext, pattern maps
    ├── values.py    # Value serialization, intrinsic_to_python
    ├── classes.py   # Class generation (params, resources, outputs)
    ├── blocks.py    # Block mode PropertyType wrapper generation
    ├── imports.py   # Import statement generation
    ├── topology.py  # SCC detection, topological sort
    ├── package.py   # Package/file generation
    └── helpers.py   # SERVICE_CATEGORIES, utilities
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

**codegen/** - Code Generator Package

The code generator is organized into focused modules:

| Module | Purpose |
|--------|---------|
| `context.py` | CodegenContext and PackageContext classes, pattern maps for implicit ref/get_att detection |
| `values.py` | Value serialization (`value_to_python`, `intrinsic_to_python`) |
| `classes.py` | Class generation for parameters, resources, outputs, mappings, conditions |
| `blocks.py` | Block mode PropertyType wrapper and policy document generation |
| `imports.py` | Import statement generation |
| `topology.py` | Strongly connected component detection, topological sort for resource ordering |
| `package.py` | Package/file generation, init file generation |
| `helpers.py` | SERVICE_CATEGORIES for file organization, utility functions |

Public API (from `codegen/__init__.py`):
- `generate_code(template, include_main=True)` - Single-file generation
- `generate_package(template, package_name)` - Package generation (multiple files)

Features:
- Automatically detects implicit refs and ARN patterns
- Uses `ARN` constant for `get_att()` calls (type-safe, IDE-friendly)
- Uses `Join()` for ARN wildcards instead of verbose `Sub()` patterns
- Groups resources by AWS service category (compute, network, storage, etc.)

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
uv run pytest tests/importer/test_codegen.py::TestBlockModeWithTags -v
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

**TestGenerateSimpleBucket** - Code generation
- Docstring generation
- Import statements
- Resource class generation
- Template class generation

**TestBlockModeWithTags** - Tag handling
- Wrapper classes for all PropertyTypes
- Correct class references

**TestBlockModeWithPolicies** - Policy document handling
- Wrapper classes for policy structures
- Proper dependency tracking

## Lessons Learned

### Forward References in Generated Code

The importer automatically generates annotation-based forward references for cross-resource dependencies:

```python
from __future__ import annotations

@cloudformation_dataclass
class ContentBucketLoggingConfiguration:
    resource: LoggingConfiguration
    destination_bucket_name: Ref[ContentLogBucket] = ref()  # Annotation-based ref

@cloudformation_dataclass
class MyLambdaFunction:
    resource: Function
    role = get_att(LambdaIAMRole, "Arn")
```

### DependsOn Class References

Resources in `depends_on` use class references instead of strings:

```python
from .lambda_invoke_permission import LambdaInvokePermission

@cloudformation_dataclass
class S3BucketNotification:
    resource: Bucket
    depends_on = [LambdaInvokePermission]  # Class reference
```

### Parameter-Only Sub Patterns

When a `!Sub` expression references only parameters (not resources), the importer preserves `Sub()` instead of converting to `get_att()`.

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
from cloudformation_dataclasses.importer.codegen import generate_code, generate_package

# Parse a template file
template = parse_template(Path("template.yaml"))

# Or parse a string
yaml_content = """
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
"""
template = parse_template(yaml_content, source_name="inline.yaml")

# Generate single file
code = generate_code(template, include_main=True)
print(code)

# Generate package (multiple files with nested structure)
package_name = "my_stack"
files = generate_package(template, package_name=package_name)
for filename, content in files.items():
    print(f"=== {filename} ===")
    print(content)

# Write package to disk
output_dir = Path("my_stack")
output_dir.mkdir(exist_ok=True)
for filename, content in files.items():
    file_path = output_dir / filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content)

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
