# cloudformation_dataclasses

**Python dataclasses for AWS CloudFormation template synthesis**

A pure Python library that uses dataclasses as a declarative interface for AWS CloudFormation template generation. Zero runtime dependencies, fully type-safe, IDE-friendly.

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- 🎯 **Declarative Block Syntax** - Infrastructure as typed dataclass fields
- 🔒 **Type-Safe** - Full Python type hints with mypy/pyright support
- 🚀 **Zero Runtime Dependencies** - Core package has no dependencies
- 🤖 **Auto-Generated** - All AWS resources generated from official CloudFormation specs
- 💡 **IDE-Friendly** - Full autocomplete and type checking in VS Code, PyCharm, etc.
- 📦 **Pure Python** - No Node.js required (unlike AWS CDK)
- 🔄 **Always Current** - Easy regeneration from latest AWS specs

## Installation

### From PyPI (when published)

```bash
# Core package (zero runtime dependencies)
pip install cloudformation_dataclasses

# With YAML support
pip install cloudformation_dataclasses[yaml]

# Development dependencies
pip install cloudformation_dataclasses[dev]
```

### From Source

```bash
# Clone repository
git clone https://github.com/lex00/cloudformation_dataclasses.git
cd cloudformation_dataclasses

# Install with uv (recommended)
uv sync

# Or with pip
pip install -e .
```

### Check Installed Version

```python
from cloudformation_dataclasses import __version__, print_version_info

print(__version__)  # Package version: 0.1.0
print_version_info()  # Detailed version information
```

**Current Release: v0.2.0**
- Package: `0.2.0`
- CloudFormation Spec: `227.0.0`
- Generator: `1.0.0`
- Available Resources: All 262 AWS services (1,502 resource types)

## Quick Start

### Simple Example

```python
@cloudformation_dataclass
class MyAppBucket:
    resource: Bucket

bucket = MyAppBucket()
template = Template(description="S3 bucket for application data")
template.add_resource(bucket)

print(template.to_json())
```

### Complete Example

See [examples/s3_bucket/](examples/s3_bucket/) for a complete modular example with deployment context, encryption, and bucket policies.

```python
# context.py - Deployment context with environment defaults and shared tags
@cloudformation_dataclass
class ProdDeploymentContext:
    context: DeploymentContext
    component: str = "DataPlatform"
    stage: str = "prod"
    deployment_name: str = "001"
    deployment_group: str = "blue"  # For blue/green deployments
    region: str = "us-east-1"
    tags = [
        {"Key": "Environment", "Value": "Production"},
        {"Key": "Project", "Value": "MyApplication"},
        {"Key": "ManagedBy", "Value": "cloudformation-dataclasses"},
    ]

ctx = ProdDeploymentContext()

# bucket.py - Nested encryption configuration using wrapper dataclasses
@cloudformation_dataclass
class MyServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = "AES256"

@cloudformation_dataclass
class MyServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = MyServerSideEncryptionByDefault

@cloudformation_dataclass
class MyBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [MyServerSideEncryptionRule]

# S3 bucket with context, tags, encryption, and versioning
@cloudformation_dataclass
class MyData:
    resource: Bucket
    context = ctx
    tags = [{"Key": "DataClassification", "Value": "sensitive"}]
    bucket_encryption = MyBucketEncryption
    versioning_configuration = {"Status": "Enabled"}

# bucket_policy.py - Bucket policy requiring encrypted uploads
@cloudformation_dataclass
class DenyUnencryptedUploadsStatement:
    resource: DenyStatement
    sid = "DenyUnencryptedObjectUploads"
    principal = "*"
    action = "s3:PutObject"
    resource_arn = {"Fn::Sub": "arn:aws:s3:::${MyData}/*"}
    condition = {"StringNotEquals": {"s3:x-amz-server-side-encryption": "AES256"}}

@cloudformation_dataclass
class EncryptionRequiredPolicyDocument:
    resource: PolicyDocument
    statement = [DenyUnencryptedUploadsStatement]

@cloudformation_dataclass
class MyDataPolicy:
    resource: BucketPolicy
    context = ctx
    bucket = ref(MyData)
    policy_document = EncryptionRequiredPolicyDocument

# main.py - Create and export template
bucket = MyData()
policy = MyDataPolicy()

template = Template(description="S3 bucket with encryption-required policy")
template.add_resource(bucket)
template.add_resource(policy)

print(template.to_json())
```

**Run the example:**
```bash
uv run python -m examples.s3_bucket.main
```

**Key Features:**
- 🎯 **Declarative** - All configuration in dataclass field declarations
- 🏷️ **Smart naming** - Configurable resource naming patterns with deployment context
- 🔗 **Cross-references** - `ref()` for resource dependencies
- 🏗️ **Nested config** - Wrapper classes or inline dicts
- 🏭 **Deployment context** - Shared environment defaults and configurable naming patterns
- 📋 **Tag merging** - Context tags + resource-specific tags
- 🔐 **IAM policies** - Type-safe policy documents and statements
- ⚡ **Zero boilerplate** - Instantiate with `MyData()` - no parameters needed

### Resource Naming

The library automatically generates resource names from class names and deployment context:

```python
# Context defines the naming pattern
@cloudformation_dataclass
class ProdDeploymentContext:
    context: DeploymentContext
    component: str = "DataPlatform"          # Application/service component
    stage: str = "prod"                       # Environment stage (dev, staging, prod)
    deployment_name: str = "001"              # Deployment identifier
    deployment_group: str = "blue"            # For blue/green deployments
    region: str = "us-east-1"                 # AWS region
    # Default pattern: {component}-{resource_name}-{stage}-{deployment_name}-{deployment_group}-{region}

ctx = ProdDeploymentContext()

# Class name becomes resource_name in the pattern
@cloudformation_dataclass
class MyData:
    resource: Bucket
    context = ctx

bucket = MyData()
# Resource name: DataPlatform-MyData-prod-001-blue-us-east-1
# Logical ID: MyData
```

**Context Parameters**:
- `component`: Application or service component name
- `stage`: Deployment stage/environment (dev, staging, prod)
- `deployment_name`: Unique deployment identifier
- `deployment_group`: For blue/green deployments - enables zero-downtime deployments
- `region`: AWS region

**Blue/Green Deployments**:
```python
# Blue deployment (current production)
ctx_blue = ProdDeploymentContext(deployment_group="blue")
# Green deployment (new version)
ctx_green = ProdDeploymentContext(deployment_group="green")

# Creates separate resource sets for zero-downtime deployments:
# DataPlatform-MyData-prod-001-blue-us-east-1
# DataPlatform-MyData-prod-001-green-us-east-1
```

**Pattern can be customized per context or overridden per resource:**

```python
# Custom context pattern
@cloudformation_dataclass
class SimpleContext:
    context: DeploymentContext
    component: str = "MyApp"
    naming_pattern: str = "{component}-{resource_name}"

# Per-resource pattern override
@cloudformation_dataclass
class MySpecial:
    resource: Bucket
    context = ctx
    naming_pattern = "{resource_name}-{stage}"  # Override context pattern
```

## Project Status

🚧 **Alpha** - Under active development

### Completed

- ✅ **Declarative block syntax** - `@cloudformation_dataclass` decorator with automatic field handling
- ✅ **Core base classes** - CloudFormationResource, Tag, DeploymentContext, PolicyDocument, PolicyStatement
- ✅ **Deployment context** - Environment defaults, automatic resource naming, tag merging
- ✅ **Cross-resource references** - `ref()` and `get_att()` helpers with DeferredRef/DeferredGetAtt
- ✅ **IAM policy support** - PolicyDocument and PolicyStatement base classes
- ✅ **Complete intrinsic functions** - Ref, GetAtt, Sub, Join, If, Select, Split, etc.
- ✅ **Template system** - Template, Parameter, Output, Condition, Mapping with validation
- ✅ **Code generator** - Auto-generate from CloudFormation specs with full serialization
- ✅ **All AWS services** - Complete generation of all 262 AWS services (1,502 resource types)
- ✅ **Comprehensive test suite** - 128 tests covering framework, intrinsics, wrapper pattern, and S3 integration
- ✅ **Inline dict support** - Tags and simple properties work with inline dicts
- ✅ **Nested configuration** - Mix wrapper classes and inline dicts as needed

### In Progress

- 🚧 **Extended examples** - EC2, Lambda, DynamoDB, API Gateway, etc.
- 🚧 **API documentation** - Auto-generated docs from docstrings
- 🚧 **Best practices guide** - Patterns and recommendations for common use cases

## Code Generation

### CloudFormation Spec Version

**Pinned Spec Version:** 227.0.0 (December 2024)
**Generator Version:** 1.0.0

All generated code is based on these exact versions for reproducible builds:
- **CloudFormation Spec**: AWS's resource specification version
- **Generator**: Our code generator version (independent of AWS spec)

```bash
# Check current spec version
uv run python -m cloudformation_dataclasses.codegen.spec_parser version

# Download CloudFormation spec (validates version matches pinned)
uv run python -m cloudformation_dataclasses.codegen.spec_parser download

# List all available AWS services
uv run python -m cloudformation_dataclasses.codegen.spec_parser list-services
```

**Spec Contents:** 262 AWS services, 1,502 resource types, 8,117 property types

### Generating Services

Generate Python classes from CloudFormation specifications:

```bash
# Generate specific service
uv run python -m cloudformation_dataclasses.codegen.generator --service S3
uv run python -m cloudformation_dataclasses.codegen.generator --service EC2
```

### Version Management

**Two independent versions:**

1. **CloudFormation Spec Version** (`CLOUDFORMATION_SPEC_VERSION`)
   - AWS's specification version (e.g., `227.0.0`)
   - Updated when AWS releases new resources or changes existing ones
   - Triggers regeneration of all services

2. **Generator Version** (`GENERATOR_VERSION`)
   - Our code generator's version (e.g., `1.0.0`)
   - Updated when fixing generator bugs or adding generator features
   - Independent of AWS spec updates
   - Uses semantic versioning: MAJOR.MINOR.PATCH

**Updating CloudFormation Spec (AWS releases new version):**
```bash
# 1. Update both versions in src/cloudformation_dataclasses/codegen/config.py
#    CLOUDFORMATION_SPEC_VERSION = "228.0.0"  # New AWS version
#    GENERATOR_VERSION = "1.1.0"              # Bump minor for spec upgrade

# 2. Download new spec
uv run python -m cloudformation_dataclasses.codegen.spec_parser download

# 3. Regenerate services
uv run python -m cloudformation_dataclasses.codegen.generator --service S3

# 4. Run tests
uv run pytest tests/ -v

# 5. Commit
git commit -m "Update to CloudFormation spec v228.0.0 (generator v1.1.0)"
```

**Patching Generator (fixing bugs, no spec change):**
```bash
# 1. Fix generator code
vim src/cloudformation_dataclasses/codegen/generator.py

# 2. Update only generator version in config.py
#    CLOUDFORMATION_SPEC_VERSION = "227.0.0"  # Unchanged
#    GENERATOR_VERSION = "1.0.1"              # Patch bump for bug fix

# 3. Regenerate affected service
uv run python -m cloudformation_dataclasses.codegen.generator --service S3

# 4. Run tests
uv run pytest tests/ -v

# 5. Commit
git commit -m "Fix S3 property serialization (generator v1.0.1, spec v227.0.0)"
```

## Development

### Setup

```bash
git clone https://github.com/lex00/cloudformation_dataclasses.git
cd cloudformation_dataclasses

# Install with uv (recommended)
uv sync --all-extras

# Or with pip
pip install -e ".[dev]"
```

### Common Tasks

```bash
# Run tests
pytest tests/ -v

# Type check
mypy src/cloudformation_dataclasses/

# Format code
black src/ tests/

# Regenerate S3 resources
python -m cloudformation_dataclasses.codegen.generator --service S3
```

## Architecture

### Design Principles

1. **Generated, Not Hand-Written** - All AWS resources auto-generated from CloudFormation specs
2. **Type Safety Throughout** - Full Python type annotations with mypy/pyright support
3. **Zero Runtime Dependencies** - Core package requires nothing (pyyaml optional)
4. **Pythonic Ergonomics** - snake_case properties mapping to CloudFormation PascalCase
5. **Explicit Over Implicit** - Clear behavior, no magic

### Two-Layer Validation

1. **Static Type Checking** (development time) - mypy/pyright catch type errors
2. **CloudFormation Validation** (deployment time) - AWS validates templates

No Pydantic or runtime validation needed - minimal dependencies, CloudFormation as source of truth.

## Project Structure

```
cloudformation_dataclasses/
├── src/cloudformation_dataclasses/
│   ├── core/              # Base classes
│   ├── intrinsics/        # Intrinsic functions
│   ├── codegen/           # Code generation
│   └── aws/               # Generated resources
├── tests/                 # Framework validation tests
├── examples/              # Usage examples with focused tests
├── planning.md            # Design document
├── CLAUDE.md              # Development guide
└── README.md              # This file
```

### Testing Structure

- **tests/** - Framework validation tests that verify core functionality (resource creation, serialization, template generation, tag merging, context-driven naming, etc.)
- **examples/*/tests/** - User-focused tests that demonstrate typical usage patterns and verify examples work correctly

## Documentation

- **User Guide**: [README.md](README.md) - This file (getting started, examples, usage)
- **Developer Guide**: [DEVELOPERS.md](DEVELOPERS.md) - Building, testing, and publishing
- **Changelog**: [CHANGELOG.md](CHANGELOG.md) - Version history and release notes
- **Planning Document**: [planning.md](planning.md) - Complete architecture and design
- **Project Checklist**: [CHECKLIST.md](CHECKLIST.md) - Implementation progress
- **CloudFormation Spec**: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html

## License

MIT License - see [LICENSE](LICENSE)

## Acknowledgments

Built with Python 3.13, uv, and AWS CloudFormation Resource Specifications.

Generated with [Claude Code](https://claude.ai/code)
