# Code Generator Architecture

This document explains how the code generator works, including the data sources it uses and how they combine to produce type-safe Python dataclasses for CloudFormation resources.

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

The generated code enables type-safe CloudFormation template definitions:

```python
from cloudformation_dataclasses.aws.dynamodb import (
    Table,
    KeySchema,
    AttributeDefinition,
    KeyType,      # Enum class
    AttributeType,  # Alias for ScalarAttributeType
    HASH,         # Direct alias: KeyType.HASH
    S,            # Direct alias: ScalarAttributeType.S
)

# All of these are valid:
KeySchema(attribute_name="pk", key_type=KeyType.HASH)  # Enum class
KeySchema(attribute_name="pk", key_type=HASH)          # Module alias
KeySchema(attribute_name="pk", key_type="HASH")        # String (backward compatible)

# IDE autocomplete works with enum classes
KeySchema(attribute_name="pk", key_type=KeyType.  # ← Shows HASH, RANGE
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

**Last Updated**: 2025-12-17
