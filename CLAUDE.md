# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Agent Workflows

**Key Tools:**
- `cfn-dataclasses init -o <dir>/` - Create new project skeleton
- `cfn-dataclasses import <template> -o <output>` - Import CloudFormation YAML/JSON
- `cfn-dataclasses lint <path> [--fix]` - Lint and auto-fix code style issues

**Always validate after generating code:**
```python
template = Template.from_registry()
errors = template.validate()
assert errors == []
```

---

## Project Overview

`cloudformation_dataclasses` is a Python library that uses **dataclasses as a declarative interface** for AWS CloudFormation template synthesis. The library focuses solely on **generating CloudFormation JSON/YAML** from Python dataclasses.

**Core Innovation**: Wrapper dataclasses with declarative wiring where all infrastructure relationships are defined as typed field declarations, not imperative code.

## Architecture Principles

### The Wrapper Dataclass Pattern

Every CloudFormation resource is wrapped in a user-defined dataclass with a `resource:` field:

```python
@cloudformation_dataclass
class MyVPC:
    resource: VPC
    cidr_block: str = "10.0.0.0/16"
    enable_dns_hostnames: bool = True

@cloudformation_dataclass
class MySubnet:
    resource: Subnet
    cidr_block: str = "10.0.1.0/24"
    vpc_id = ref(MyVPC)  # Cross-resource reference via ref() helper
```

**Key point**: ALL wiring happens inside dataclass field declarations, not at instantiation.

### Code Generation Strategy

All AWS resource classes are **pre-generated from CloudFormation specs** and **committed to git**. This is NOT runtime generation.

**Rationale**:
- Minimal runtime dependencies (just pyyaml)
- IDE autocomplete works immediately
- Users can browse generated code on GitHub
- No generation step during pip install
- Tested, stable generated code

### Type System

- **CloudFormation → Python mappings**: String→str, Integer→int, Boolean→bool, etc.
- **Union types for intrinsics**: Every property accepts literal values OR CloudFormation functions (Ref, GetAtt, Sub, etc.)
- **PascalCase → snake_case**: CloudFormation properties like `BucketName` become `bucket_name`

### Cross-Resource References

Use `ref()` and `get_att()` with direct class references:

```python
@cloudformation_dataclass
class BucketPolicy:
    resource: s3.BucketPolicy
    bucket = ref(MyBucket)  # Direct class reference
    policy_document = BucketPolicyPolicyDocument
```

Auto-discovery via `setup_resources()` ensures all classes are available at runtime regardless of which file they're defined in.

**Qualified resource types for name collisions:**

When a wrapper class has the same name as the AWS resource class (e.g., `class Bucket` wrapping `s3.Bucket`), use the module-qualified type to avoid self-reference:

```python
@cloudformation_dataclass
class Bucket:
    resource: s3.Bucket  # NOT resource: Bucket (would be self-referential)
    bucket_name = ref(BucketName)
```

The codegen automatically detects these collisions and generates qualified names.

### Validation Strategy (Two-Layer)

1. **Static Type Checking** (mypy/pyright) - Catches type errors at development time
2. **CloudFormation Validation** - AWS validates during deployment/template validation

**No Pydantic or runtime validation libraries** - keeps dependencies minimal, lets CloudFormation be the source of truth.

## Project Structure

```
src/cloudformation_dataclasses/
├── core/                # Base classes
│   ├── base.py         # CloudFormationResource, Tag, DeploymentContext
│   └── template.py     # Template, Parameter, Output, Condition
├── intrinsics/         # Type-safe CloudFormation functions
│   └── functions.py    # Ref, GetAtt, Sub, Join, If, etc.
├── codegen/            # Code generation tools (build-time only)
│   ├── spec_parser.py  # Download and parse AWS CloudFormation specs
│   └── generator.py    # Generate dataclass code from specs
└── aws/                # GENERATED - All AWS resources (committed to git)
    ├── s3.py          # ~5,000 lines
    ├── ec2.py         # ~15,000 lines
    ├── lambda_.py     # ~2,000 lines
    └── ...            # ~300+ service modules
```

## Development Commands

### Setup

```bash
# Clone and install development dependencies
uv sync --all-extras
```

### Code Generation

```bash
# Regenerate ALL AWS resource classes from latest CloudFormation spec
./scripts/regenerate.sh

# Or manually:
python -m cloudformation_dataclasses.codegen.spec_parser download
python -m cloudformation_dataclasses.codegen.generator --all
uv run black src/cloudformation_dataclasses/aws/

# Regenerate specific service only
python -m cloudformation_dataclasses.codegen.generator --service s3
```

### Testing

```bash
# Run all tests
uv run pytest tests/ -v

# Run with coverage
uv run pytest tests/ -v --cov

# Run specific test file
uv run pytest tests/test_s3.py -v

# Run specific test
uv run pytest tests/test_s3.py::test_bucket_serialization -v
```

### Type Checking

```bash
# Type check entire codebase
uv run mypy src/cloudformation_dataclasses/

# Type check specific module
uv run mypy src/cloudformation_dataclasses/core/
```

### Linting and Formatting

```bash
# Format code
uv run black src/ tests/

# Lint
uv run ruff check src/ tests/
```

### Building

```bash
# Full build pipeline (download spec, generate, format, test, build)
./scripts/build.sh

# Build package only
uv build
```

## Critical Implementation Rules

### 1. Block/Wrapper Syntax (Not Imperative)

**ALWAYS use wrapper dataclasses** - never use imperative instantiation:

```python
# ✅ CORRECT - Block syntax with wrapper
@dataclass
class MyBucket:
    resource: Bucket
    bucket_name: str = "my-bucket"
    versioning_configuration: VersioningConfiguration

my_bucket = MyBucket()

# ❌ WRONG - Imperative syntax
bucket = Bucket(bucket_name="my-bucket", versioning_configuration=...)
```

### 2. Resource Naming

CloudFormation resource names do NOT include service prefixes:
- Class name: `Instance` (not `EC2Instance`)
- Namespacing via module: `from cloudformation_dataclasses.aws.ec2 import Instance`

### 3. Generated Code Management

- Generated files in `src/cloudformation_dataclasses/aws/*.py` are **committed to git**
- Every generated file includes a header: `⚠️ AUTO-GENERATED FILE - DO NOT EDIT MANUALLY`
- Never manually edit generated files - regenerate instead
- Format generated code with Black before committing

### 4. Dependencies

**Runtime dependencies**:
- `pyyaml` - Required for YAML template parsing and serialization
- Optional: `watchdog` for `cfn-dataclasses stubs --watch` via `pip install cloudformation_dataclasses[stubs]`

**Development dependencies** (NOT shipped):
- `black` - Format generated code (build-time only)
- `mypy` - Static type checking
- `pytest` - Testing
- `ruff` - Linting
- `requests` - Download CloudFormation specs (codegen only)

### 5. Python Version

Requires Python 3.10+ for union syntax (`X | Y`) and built-in generics.

## Code Generation Algorithm

When modifying the code generator (`codegen/generator.py`):

1. **Parse CloudFormation spec** - JSON structure with ResourceTypes and PropertyTypes
2. **Generate nested property classes first** - Complex property types become dataclasses
3. **Map CloudFormation types to Python types** - String→str, Integer→int, Boolean→bool, Json→Dict[str, Any], etc.
4. **Convert PascalCase to snake_case** - With special handling for acronyms (VPCId → vpc_id)
5. **Handle Python keywords** - Append underscore if needed (type → type_)
6. **Create Union types** - Allow literals OR intrinsic functions for each property
7. **Generate typed attribute accessors** - @property methods for GetAtt attributes
8. **Add docstrings** - From CloudFormation documentation
9. **Format with Black** - Ensure consistent code style

## Package Build and Distribution

### Build System

- Uses **uv** as package manager and build system
- No explicit `[build-system]` in pyproject.toml - uv handles it automatically
- Src-layout: `src/cloudformation_dataclasses/` for proper isolation

### Pre-Generation Workflow

1. Download latest CloudFormation spec from AWS
2. Generate all resource classes (~300 services)
3. Format with Black
4. Type check with mypy
5. Run tests
6. Build wheel
7. Publish to PyPI

### Version Strategy

Semantic versioning with CloudFormation spec tracking:
- `X.Y.Z` - Major.Minor.Patch for package version
- CloudFormation spec date in YYYY.MM.DD format (from AWS Last-Modified header)
- Spec file committed to `specs/` directory for reproducibility
- Check for updates: `uv run python -m cloudformation_dataclasses.codegen.spec_parser check`
- Update spec: `uv run python -m cloudformation_dataclasses.codegen.spec_parser update`

## Understanding the Codebase

### Key Concepts

1. **CloudFormationResource** - Base class for all AWS resources, provides:
   - `resource_type: ClassVar[str]` - AWS resource type (e.g., "AWS::S3::Bucket")
   - `to_dict()` - Serialize to CloudFormation JSON
   - `ref()` - Create Ref intrinsic function
   - `get_att()` - Create GetAtt intrinsic function
   - Auto-naming via `resource_name` property
   - Tag merging via `all_tags` property

2. **DeploymentContext** - Provides environment defaults:
   - Project name, component, environment, region, account_id
   - Auto-generates resource names (e.g., "MyProject-MyComponent-MyBucket-prod-001-blue-us-east-1")
   - Merges tags across context and resources

3. **Intrinsic Functions** - Type-safe CloudFormation functions:
   - `Ref` - Reference to logical ID
   - `GetAtt` - Get resource attribute
   - `Sub` - String substitution
   - `Join`, `If`, `Select`, etc.

4. **Template** - Container for CloudFormation template:
   - Add resources, parameters, outputs, conditions
   - Serialize to JSON/YAML
   - Optional validation via AWS API

### Reading Generated Code

Generated files follow this pattern:

```python
# Header with generation metadata
"""AWS CloudFormation EC2 Resources
⚠️ AUTO-GENERATED FILE - DO NOT EDIT MANUALLY
CloudFormation Spec: 2025.12.11
Generator Version: 1.0.0
Generated: 2024-12-15T13:18:57Z
"""

# Nested property type dataclasses first
@dataclass
class PropertyTypeClass:
    field: Optional[Union[str, Ref]] = None

# Main resource class
@dataclass
class ResourceClass(CloudFormationResource):
    resource_type: ClassVar[str] = "AWS::Service::Resource"

    # Properties (snake_case)
    property_name: Optional[Union[str, Ref, GetAtt]] = None

    # Typed attribute accessors
    @property
    def attr_name(self) -> GetAtt:
        return self.get_att("AttributeName")
```

## Testing Strategy

### Test Structure

- `tests/test_generated_*.py` - Test generated AWS resource classes
- Use wrapper dataclass pattern in test fixtures
- Verify serialization to CloudFormation JSON
- Test intrinsic function serialization
- Include mypy type error tests (files that should fail type checking)

### Example Test Pattern

```python
# Define wrapper dataclasses at module level
@dataclass
class TestBucket:
    resource: Bucket
    bucket_name: str = "test-bucket"

def test_serialization():
    bucket = TestBucket()
    result = bucket.to_dict()
    assert result["Type"] == "AWS::S3::Bucket"
    assert result["Properties"]["BucketName"] == "test-bucket"
```

## Important References

- AWS CloudFormation Resource Specification: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html
- Specification JSON: https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json

## Anti-Patterns to Avoid

When generating code for this library, NEVER use raw CloudFormation dict patterns.

### 1. Raw Intrinsic Function Dicts
```python
# ❌ WRONG - raw dict
vpc_id = {"Ref": "VpcId"}
availability_zone = {"Fn::Select": [0, {"Fn::GetAZs": ""}]}
password = {"Fn::Sub": "${Secret}"}
joined = {"Fn::Join": [",", [...]]}

# ✅ CORRECT - typed helpers
from cloudformation_dataclasses.intrinsics import Ref, Sub, Select, GetAZs, Join
vpc_id = Ref("VpcId")
availability_zone = Select(0, GetAZs())
password = Sub("${Secret}")
joined = Join(",", [...])
```

### 2. Pseudo-Parameter References
```python
# ❌ WRONG
region = {"Ref": "AWS::Region"}
account_id = {"Ref": "AWS::AccountId"}

# ✅ CORRECT
from cloudformation_dataclasses.intrinsics import AWS_REGION, AWS_ACCOUNT_ID
region = AWS_REGION
account_id = AWS_ACCOUNT_ID
```

### 3. Inline PropertyType Constructors
```python
# ❌ WRONG - inline constructor in list
security_group_ingress = [
    ec2.security_group.Ingress(ip_protocol=IpProtocol.TCP, from_port=443)
]

# ✅ CORRECT - separate wrapper class
@cloudformation_dataclass
class MySecurityGroupIngress:
    resource: ec2.security_group.Ingress
    ip_protocol = IpProtocol.TCP
    from_port = 443

@cloudformation_dataclass
class MySecurityGroup:
    resource: ec2.SecurityGroup
    security_group_ingress = [MySecurityGroupIngress]
```

### 4. Inline IAM Policies
```python
# ❌ WRONG - inline dict
assume_role_policy_document = {
    "Version": "2012-10-17",
    "Statement": [{"Effect": "Allow", ...}]
}

# ✅ CORRECT - wrapper classes
@cloudformation_dataclass
class MyAssumeRoleStatement:
    resource: PolicyStatement
    principal = {"Service": "lambda.amazonaws.com"}
    action = "sts:AssumeRole"

@cloudformation_dataclass
class MyAssumeRolePolicy:
    resource: PolicyDocument
    statement = [MyAssumeRoleStatement]

@cloudformation_dataclass
class MyRole:
    resource: iam.Role
    assume_role_policy_document = MyAssumeRolePolicy
```

### Available Intrinsic Functions

Import from `cloudformation_dataclasses.intrinsics`:
- `Ref("ParameterName")` - Reference parameters
- `ref(ResourceClass)` - Reference resources (lowercase)
- `get_att(ResourceClass, "Attribute")` - Get resource attributes
- `Sub("string with ${variable}")` - String substitution
- `Join(",", [items])` - Join list to string
- `Select(index, list)` - Select item from list
- `GetAZs(region="")` - Get availability zones
- `AWS_REGION`, `AWS_ACCOUNT_ID`, `AWS_STACK_NAME` - Pseudo-parameters
