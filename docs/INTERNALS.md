# Internals

This document covers the internal architecture of cloudformation_dataclasses for contributors and maintainers.

**Contents:**
- [Resource Registry](#resource-registry) - How auto-registration and discovery work
- [AWS Resource Generator](#aws-resource-generator) - How AWS resource classes are generated from CloudFormation specs
- [Template Importer](#template-importer) - How CloudFormation templates are converted to Python
- [Shared Utilities](#shared-utilities) - Common infrastructure between linter and importer

---

# Resource Registry

The resource registry enables automatic registration and discovery of CloudFormation resources, eliminating manual resource listing.

## How It Works

When you decorate a class with `@cloudformation_dataclass`, it automatically registers with a global registry:

```python
@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name = "data"
    # Automatically registered as "AWS::S3::Bucket"
```

The decorator checks if the wrapped class has a `resource_type` attribute (indicating it's a CloudFormation resource, not a PropertyType) and registers accordingly.

## Auto-Discovery

The `setup_resources()` function in the package's `__init__.py` handles auto-discovery:

```python
from cloudformation_dataclasses.core.resource_loader import setup_resources
setup_resources(__file__, __name__, globals())
```

This function:
1. Finds all `.py` files in the package directory
2. Imports each module, triggering `@cloudformation_dataclass` decorators
3. Exports all public names for the single import pattern

## What Registers

| Type | Registers | Example |
|------|-----------|---------|
| Resources | ✅ | `Bucket`, `Function`, `Table` |
| PropertyTypes | ❌ | `BucketEncryption`, `KeySchema` |
| PolicyDocument | ❌ | IAM policy components |
| Tag | ❌ | Resource attributes |

PropertyTypes are nested configuration - they're part of resources, not standalone CloudFormation resources.

## Registry API

```python
from cloudformation_dataclasses.core import registry

# Get all registered resources
all_resources = registry.get_all()

# Query by CloudFormation type (class or string)
tables = registry.get_by_type(Table)
tables = registry.get_by_type("AWS::DynamoDB::Table")

# Get by class name
my_table = registry.get_by_name("UsersTable")

# Clear for test isolation
registry.clear()

# Check membership
"MyBucket" in registry  # True/False
len(registry)           # Count
```

## Template.from_registry()

Builds templates from all registered resources:

```python
template = Template.from_registry(
    description="My Stack",
    parameters=[EnvironmentParam],
    outputs=[BucketArnOutput],
    scope_package="my_project.stack",  # Optional: limit scope
)
```

## Disabling Registration

For helper resources you don't want in the template:

```python
@cloudformation_dataclass(register=False)
class HelperBucket:
    resource: Bucket
    # Won't appear in Template.from_registry()
```

## Test Isolation

Use `registry.clear()` in test fixtures:

```python
@pytest.fixture(autouse=True)
def clear_registry():
    registry.clear()
    yield
    registry.clear()
```

---

# AWS Resource Generator

This section explains how the code generator works, including the data sources it uses and how they combine to produce type-safe Python dataclasses for CloudFormation resources.

## Overview

The generator produces Python modules for each AWS service by combining two data sources:

1. **CloudFormation Resource Specification** - Defines resource types, properties, and structure
2. **Botocore Service Models** - Provides enum values and property-to-enum mappings

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           Code Generator                                 │
│                                                                          │
│  ┌──────────────────────┐         ┌──────────────────────┐              │
│  │  CloudFormation Spec │         │   Botocore Models    │              │
│  │                      │         │                      │              │
│  │  • Resource types    │         │  • Enum values       │              │
│  │  • Property types    │         │  • Shape definitions │              │
│  │  • Property specs    │         │  • Property→Enum     │              │
│  │  • Required fields   │         │    mappings          │              │
│  └──────────┬───────────┘         └──────────┬───────────┘              │
│             │                                │                          │
│             └───────────────┬────────────────┘                          │
│                             ▼                                           │
│                    ┌────────────────┐                                   │
│                    │   generator.py │                                   │
│                    └────────┬───────┘                                   │
│                             │                                           │
│                             ▼                                           │
│              ┌──────────────────────────┐                               │
│              │  Generated Python Module │                               │
│              │                          │                               │
│              │  • Dataclass definitions │                               │
│              │  • Type annotations      │                               │
│              │  • Enum classes          │                               │
│              │  • Module-level aliases  │                               │
│              └──────────────────────────┘                               │
└─────────────────────────────────────────────────────────────────────────┘
```

## Data Sources

### 1. CloudFormation Resource Specification

**Source**: `specs/CloudFormationResourceSpecification.json`
**URL**: `https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json`
**Parser**: `spec_parser.py`

The CloudFormation spec is a JSON file published by AWS that defines all CloudFormation resource types. It provides:

#### Resource Types
Each resource type (e.g., `AWS::DynamoDB::Table`) includes:
- **Properties**: What properties the resource accepts
- **Attributes**: What values can be retrieved with `!GetAtt`
- **Documentation**: Links to AWS documentation

```json
{
  "ResourceTypes": {
    "AWS::DynamoDB::Table": {
      "Properties": {
        "TableName": {
          "PrimitiveType": "String",
          "Required": false,
          "UpdateType": "Immutable"
        },
        "KeySchema": {
          "Type": "List",
          "ItemType": "KeySchema",
          "Required": true
        }
      },
      "Attributes": {
        "Arn": { "PrimitiveType": "String" },
        "StreamArn": { "PrimitiveType": "String" }
      }
    }
  }
}
```

#### Property Types
Complex nested structures are defined as PropertyTypes:

```json
{
  "PropertyTypes": {
    "AWS::DynamoDB::Table.KeySchema": {
      "Properties": {
        "AttributeName": {
          "PrimitiveType": "String",
          "Required": true
        },
        "KeyType": {
          "PrimitiveType": "String",
          "Required": true
        }
      }
    }
  }
}
```

#### Type Information
The spec defines several type categories:

| Spec Field | Python Mapping | Example |
|------------|----------------|---------|
| `PrimitiveType: String` | `str` | `"my-bucket"` |
| `PrimitiveType: Integer` | `int` | `5` |
| `PrimitiveType: Boolean` | `bool` | `True` |
| `PrimitiveType: Json` | `dict[str, Any]` | `{"key": "value"}` |
| `Type: List` | `list[ItemType]` | `[item1, item2]` |
| `Type: Map` | `dict[str, ItemType]` | `{"k": item}` |
| `Type: PropertyTypeName` | `PropertyTypeName` | Nested dataclass |

### 2. Botocore Service Models

**Source**: Installed `botocore` package
**Parser**: `botocore_enums.py`

Botocore is the low-level foundation of the AWS SDK (boto3). Its service models contain valuable information not available in the CloudFormation spec:

#### Enum Values
Botocore defines valid values for string enumerations:

```json
{
  "shapes": {
    "KeyType": {
      "type": "string",
      "enum": ["HASH", "RANGE"]
    },
    "ProjectionType": {
      "type": "string",
      "enum": ["ALL", "KEYS_ONLY", "INCLUDE"]
    }
  }
}
```

#### Shape Definitions (Structures)
Botocore defines which struct members reference which enum types:

```json
{
  "shapes": {
    "KeySchemaElement": {
      "type": "structure",
      "members": {
        "AttributeName": { "shape": "KeySchemaAttributeName" },
        "KeyType": { "shape": "KeyType" }
      }
    }
  }
}
```

This tells us that `KeySchemaElement.KeyType` accepts values from the `KeyType` enum.

## Service Name Mapping

CloudFormation and botocore use different naming conventions:

| CloudFormation | Botocore |
|----------------|----------|
| `DynamoDB` | `dynamodb` |
| `ApiGateway` | `apigateway` |
| `CertificateManager` | `acm` |
| `ElasticLoadBalancingV2` | `elbv2` |
| `MSK` | `kafka` |

The `CF_TO_BOTOCORE_SERVICE` dictionary in `botocore_enums.py` maps between these conventions.

## Structure Name Mapping

Some structures have different names between CloudFormation and botocore:

| CloudFormation | Botocore |
|----------------|----------|
| `KeySchema` | `KeySchemaElement` |

The `CF_TO_BOTOCORE_STRUCT` dictionary handles these cases.

## Generation Process

### Step 1: Parse CloudFormation Spec

`spec_parser.py` loads and parses the CloudFormation spec:

```python
spec = get_spec()  # Returns CloudFormationSpec

# Access resources for a service
for resource_type, resource_spec in spec.resources_by_service("DynamoDB").items():
    print(resource_spec.class_name)  # "Table", "GlobalTable"
    print(resource_spec.properties)   # Dict of PropertySpec objects

# Access property types for a service
for prop_type, prop_spec in spec.property_types_by_service("DynamoDB").items():
    print(prop_spec.name)  # "KeySchema", "AttributeDefinition"
```

### Step 2: Extract Botocore Enums

`botocore_enums.py` extracts enum information:

```python
# Get all enums for a service
enums = get_service_enums("DynamoDB")
# Returns: {"KeyType": ["HASH", "RANGE"], "ProjectionType": ["ALL", ...], ...}

# Get property-to-enum mappings
mappings = get_property_enum_mappings("DynamoDB")
# Returns: {("KeySchemaElement", "KeyType"): "KeyType",
#           ("AttributeDefinition", "AttributeType"): "ScalarAttributeType", ...}
```

### Step 3: Generate Python Code

`generator.py` combines both sources to generate Python modules:

```python
def generate_service_module(service_name: str) -> str:
    spec = get_spec()

    # Get CloudFormation resources and property types
    resources = spec.resources_by_service(service_name)
    property_types = spec.property_types_by_service(service_name)

    # Get botocore enum information
    enum_classes, enum_aliases = generate_service_enums(service_name)
    enum_mappings = get_property_enum_mappings(service_name)

    # Generate property type classes
    for prop_type, prop_spec in property_types.items():
        generate_property_type_class(prop_spec, enum_mappings)

    # Generate resource classes
    for resource_type, resource_spec in resources.items():
        generate_resource_class(resource_spec, enum_mappings)
```

### Step 4: Map Property Types with Enum Support

When generating type annotations, the generator checks if a property maps to an enum:

```python
def map_property_type(prop, resource_type, prop_name, struct_name, enum_mappings):
    if prop.primitive_type == "String" and enum_mappings:
        # Look up enum type for this property
        enum_type = enum_mappings.get((struct_name, prop_name))

        # Handle CF→botocore struct name differences
        if not enum_type:
            botocore_struct = CF_TO_BOTOCORE_STRUCT.get(struct_name)
            if botocore_struct:
                enum_type = enum_mappings.get((botocore_struct, prop_name))

        if enum_type:
            # Apply class alias (e.g., ScalarAttributeType → AttributeType)
            display_type = CLASS_ALIASES.get(enum_type, enum_type)
            return f"Union[str, {display_type}, Ref, GetAtt, Sub]"

    # Default string type without enum
    return f"Union[str, Ref, GetAtt, Sub]"
```

## Generated Output

For each service, the generator produces a Python module with:

### 1. Header with Version Info
```python
"""
AWS CloudFormation DynamoDB Resources

⚠️  AUTO-GENERATED FILE - DO NOT EDIT MANUALLY ⚠️

Version Information:
  CloudFormation Spec: 2025.12.11
  Generator Version: 1.0.0
  Combined: spec-2025.12.11_gen-1.0.0
  Generated: 2025-12-17 10:30:00
"""
```

### 2. Enum Classes (from Botocore)
```python
class KeyType:
    """KeyType enum values."""

    HASH = "HASH"
    RANGE = "RANGE"


class ProjectionType:
    """ProjectionType enum values."""

    ALL = "ALL"
    INCLUDE = "INCLUDE"
    KEYS_ONLY = "KEYS_ONLY"
```

### 3. Property Type Dataclasses (from CF Spec + Botocore)
```python
@dataclass
class KeySchema:
    """AWS::DynamoDB::Table.KeySchema property type."""

    attribute_name: Union[str, Ref, GetAtt, Sub]
    key_type: Union[str, KeyType, Ref, GetAtt, Sub]  # ← Enum type included!

    def to_dict(self) -> dict[str, Any]:
        ...
```

### 4. Resource Dataclasses (from CF Spec)
```python
@dataclass
class Table(CloudFormationResource):
    """AWS::DynamoDB::Table resource."""

    RESOURCE_TYPE = "AWS::DynamoDB::Table"

    key_schema: list[KeySchema]
    attribute_definitions: list[AttributeDefinition]
    table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    ...
```

### 5. Module-Level Aliases
```python
# Class aliases for convenience
AttributeType = ScalarAttributeType

# Value aliases for direct import
HASH = KeyType.HASH
RANGE = KeyType.RANGE
S = ScalarAttributeType.S
N = ScalarAttributeType.N
B = ScalarAttributeType.B
```

## Usage Example

The generated code enables type-safe CloudFormation template definitions. In your project, these imports are centralized in `__init__.py` and available via the single import pattern:

```python
# In your __init__.py, imports are centralized:
from cloudformation_dataclasses.aws.dynamodb import (
    Table, KeySchema, AttributeDefinition,
    KeyType, AttributeType, HASH, S,
)

# In resource files, use the single import:
from . import *  # Gets Table, KeySchema, KeyType, etc.

# All of these are valid:
KeySchema(attribute_name="pk", key_type=KeyType.HASH)  # Enum class
KeySchema(attribute_name="pk", key_type=HASH)          # Module alias
KeySchema(attribute_name="pk", key_type="HASH")        # String (backward compatible)

# IDE autocomplete works with enum classes
KeySchema(attribute_name="pk", key_type=KeyType.  # ← Shows HASH, RANGE
```

## Type Annotations and Forward References

The generator produces Union types that enable cross-resource references:

```python
# Generated type annotation
table_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
key_type: Union[str, KeyType, Ref, GetAtt, Sub]  # Includes enum
```

These Union types allow wrapper classes to use:
- Literal values (`"my-table"`)
- Enum constants (`KeyType.HASH`)
- CloudFormation intrinsics (`Ref`, `GetAtt`, `Sub`)

When users write wrapper classes that reference other resources, they use the `ref()` and `get_att()` helpers with annotation-based forward references:

```python
from __future__ import annotations

@cloudformation_dataclass
class MyBucketPolicy:
    resource: BucketPolicy
    bucket = ref(MyBucket)  # Direct class reference
```

## Files

| File | Purpose |
|------|---------|
| `codegen/config.py` | Version configuration |
| `codegen/spec_parser.py` | CloudFormation spec parser |
| `codegen/botocore_enums.py` | Botocore enum extraction |
| `codegen/generator.py` | Code generator |
| `specs/CloudFormationResourceSpecification.json` | Committed CF spec |
| `aws/*.py` | Generated service modules |

## Regenerating Services

```bash
# Regenerate a single service
./scripts/regenerate.sh DynamoDB

# Regenerate all services
./scripts/regenerate.sh --all

# Manual generation
uv run python -m cloudformation_dataclasses.codegen.generator --service DynamoDB
```

---

# Template Importer

The importer converts CloudFormation YAML/JSON templates to Python code. This section covers its internal architecture.

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

## Module Overview

### ir.py - Intermediate Representation

Defines dataclasses for the parsed template structure:
- `IRTemplate` - Complete parsed template
- `IRResource` - Parsed resource with properties
- `IRParameter` - Parsed parameter
- `IROutput` - Parsed output
- `IRCondition` - Parsed condition
- `IRMapping` - Parsed mapping
- `IRIntrinsic` - Parsed intrinsic function
- `IntrinsicType` - Enum of all intrinsic types

### parser.py - Template Parser

- `parse_template(source, source_name=None)` - Main entry point
- Handles YAML with custom constructors for `!Ref`, `!GetAtt`, etc.
- Handles JSON with `Fn::` prefix detection
- Builds reference graph for dependency ordering

### codegen/ - Code Generator Package

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

### cli.py - Command Line Interface

- Argument parsing with argparse
- File/stdin input handling
- File/stdout output handling

## Circular Dependency Handling (SCCs)

When resources have circular references (A → B → C → A), they form a *Strongly Connected Component* (SCC). The `topology.py` module detects these cycles using Tarjan's algorithm and places all resources in an SCC together in `main.py` to avoid Python import errors.

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

### SCC Relevance: Python Imports vs CloudFormation

**Important**: SCCs are used for **Python code organization**, not CloudFormation correctness.

- **Python requirement**: Resources with circular dependencies must be in the same file to avoid import errors
- **CloudFormation behavior**: Resource order in templates is irrelevant - AWS builds its own dependency graph from `Ref`, `GetAtt`, and `DependsOn`
- **What SCCs solve**: Preventing Python circular import errors when generating multi-file packages
- **What SCCs don't affect**: CloudFormation template validity or deployment behavior

The SCC detection in `topology.py` ensures generated Python code is importable, not that CloudFormation templates are valid. CloudFormation itself is completely order-independent.

For more details, see `DRAFT_SCC_RELEVANCE.md`.

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

## Limitations

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
3. **Circular references**: Detected and handled via SCC grouping

---

# Shared Utilities

The linter and importer share common infrastructure through modules in `core/`. This avoids code duplication and ensures consistent behavior.

## Shared Modules

### core/naming.py

Name conversion utilities used by both systems:

```python
from cloudformation_dataclasses.core.naming import (
    to_snake_case,        # PascalCase → snake_case (BucketName → bucket_name)
    to_pascal_case,       # snake_case → PascalCase (bucket_name → BucketName)
    sanitize_python_name, # Handle Python keywords (class → class_)
    sanitize_class_name,  # Handle numeric prefixes (123Resource → _123Resource)
)
```

**Used by:**
- `importer/parser.py` - Converting CloudFormation property names
- `codegen/generator.py` - Generating Python class names
- `linter/split.py` - File organization utilities

### core/ast_helpers.py

Python AST analysis utilities:

```python
from cloudformation_dataclasses.core.ast_helpers import (
    is_cloudformation_dataclass,  # Check for @cloudformation_dataclass decorator
    find_decorator,               # Find decorator by name on a class
    find_last_import_line,        # Find where to insert new imports
    parse_existing_imports,       # Extract import info from AST
    extract_resource_annotation,  # Get resource type from class (s3.Bucket)
)
```

**Used by:**
- `linter/split.py` - Analyzing resource files for splitting
- `linter/__init__.py` - Import management for auto-fixes
- `linter/rules.py` - Detecting `@cloudformation_dataclass` decorated classes

## Relationship Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        core/                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐   │
│  │  naming.py   │    │ ast_helpers  │    │ constants/   │   │
│  │              │    │              │    │              │   │
│  │ to_snake_case│    │ is_cf_dc()   │    │ KNOWN_ENUMS  │   │
│  │ to_pascal    │    │ find_import  │    │ PropertyType │   │
│  │ sanitize_*   │    │ extract_*    │    │ mappings     │   │
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘   │
│         │                   │                   │           │
└─────────┼───────────────────┼───────────────────┼───────────┘
          │                   │                   │
    ┌─────┴─────┐       ┌─────┴─────┐       ┌─────┴─────┐
    │           │       │           │       │           │
┌───▼───┐   ┌───▼───┐   │       ┌───▼───┐   │       ┌───▼───┐
│parser │   │codegen│   │       │split  │   │       │rules  │
│       │   │       │   │       │       │   │       │       │
└───────┘   └───────┘   │       └───────┘   │       └───────┘
  importer/             │         linter/   │
                        │                   │
                        └───────────────────┘
```

## Design Rationale

1. **Single source of truth**: Name conversion logic is defined once
2. **No circular imports**: Core utilities don't depend on importer or linter
3. **Testable**: Shared utilities can be tested independently
4. **Backward compatible**: `importer/parser.py` re-exports naming functions for existing code

For detailed analysis of unification opportunities, see `docs/DRAFT_LINTER_IMPORTER_UNIFICATION.md`.

---

**Last Updated**: 2025-12-25
