# cf-dataclasses: Python Dataclasses for AWS CloudFormation

## Executive Summary

A design/architecture document for `cloudformation_dataclasses`, a pure Python library that uses **dataclasses as a superior declarative interface** for AWS CloudFormation template synthesis. The library focuses solely on **generating CloudFormation JSON/YAML** from Python dataclasses - deployment is handled by external tools.

### Why Dataclasses for Infrastructure?

**Dataclasses provide declarative infrastructure where all wiring happens inside field declarations:**

The key insight: **Each resource is a wrapper dataclass with all properties and relationships as typed fields**.

```python
# All configuration and wiring inside dataclass declarations
@dataclass
class MyVPC:
    resource: VPC
    cidr_block: str = "10.0.0.0/16"
    enable_dns_hostnames: bool = True

@dataclass
class MySubnet:
    resource: Subnet
    cidr_block: str = "10.0.1.0/24"
    vpc_id: MyVPC.ref()
    availability_zone: str = "us-east-1a"

# Simple instantiation - no wiring code needed
my_vpc = MyVPC()
my_subnet = MySubnet()
```

**The differentiator: Pure declarative syntax**
- **All wiring in field declarations** - No imperative instantiation code
- **Type-safe references** - `Ref` objects for CloudFormation references
- **Scannable structure** - See all properties and relationships at a glance
- **Block-style syntax** - Resources as typed field declarations

**Why this approach is superior:**

1. **Declarative Wiring** - All relationships as field declarations, not imperative code
2. **Wrapper Pattern** - Each resource wrapped in a dataclass with `resource:` field
3. **Type Safety** - Full Python type checking for properties and references
4. **No External Wiring** - Instantiation is just `MyVPC()`, no configuration at call site
5. **Scannable** - See all properties and relationships in one place

### Core Value Proposition

1. **Dataclass-First Design** - Infrastructure definitions that read like documentation
2. **Type Safety Throughout** - Catch configuration errors before deployment via Python's type system
3. **Pure Python** - Zero Node.js dependencies (unlike AWS CDK)
4. **Declarative Readability** - Code that clearly expresses infrastructure intent
5. **Modern Python** - Leverages latest Python (3.13+) with dataclasses, type hints, pattern matching

---

## 1. Architecture Overview

### Design Principles

1. **Generated, Not Hand-Written** - All resource classes generated from official AWS CloudFormation Resource Specifications
2. **Type Safety Throughout** - Explicit Python type annotations, typed intrinsic functions
3. **Pythonic Ergonomics** - Use Python idioms, snake_case properties (map to PascalCase internally)
4. **Composability** - Resources as building blocks, support higher-level constructs
5. **Explicit Over Implicit** - Clear behavior, no magic

### Architecture Layers

```
User Code (Application Layer)
    ↓
High-Level Constructs (Optional)
    ↓
Core Resource Layer (Generated from AWS specs)
    ↓
Intrinsic Functions Layer
    ↓
Template Serialization Layer
    ↓
Deployment Layer (Optional boto3 integration)
```

---

## 2. Core Technical Design

### 2.1 Base Resource Class

Every CloudFormation resource inherits from:

```python
@dataclass
class Tag:
    """CloudFormation resource tag."""
    key: str
    value: str

@dataclass
class CloudFormationResource(ABC):
    resource_type: ClassVar[str]
    logical_id: Optional[str] = None
    depends_on = []
    condition: Optional[str] = None
    deletion_policy: Optional[str] = None
    tags = []
    context: Optional["DeploymentContext"] = None

    @property
    def resource_name(self) -> str:
        """Auto-generate resource name from context + class name"""
        if self.context:
            return self.context.resource_name(self.__class__.__name__)
        return self.__class__.__name__

    @property
    def all_tags(self) -> List["Tag"]:
        """Merge context tags with resource-specific tags"""
        if self.context:
            return self.context.tags + self.tags
        return self.tags

    def to_dict(self) -> Dict[str, Any]: ...
    def ref(self) -> "Ref": ...
    def get_att(self, attribute: str) -> "GetAtt": ...

@dataclass
class DeploymentContext(ABC):
    """Base class for deployment context - supports inferred naming like resources."""
    context_type: ClassVar[str]
    component: Optional[str] = None
    environment: Optional[str] = None
    naming_suffix: Optional[str] = None
    naming_group: Optional[str] = None
    region: Optional[str] = None
    account_id: Optional[str] = None
    project_name: Optional[str] = None
    tags = []

    def resource_name(self, resource_class_name: str) -> str:
        """Generate AWS resource name: Component-ResourceName-Environment-Suffix+Group"""
        parts = [self.component, resource_class_name, self.environment]
        if self.naming_suffix and self.naming_group:
            parts.append(f"{self.naming_suffix}{self.naming_group}")
        elif self.naming_suffix:
            parts.append(self.naming_suffix)
        return "-".join(filter(None, parts))
```

### 2.2 Generated Resource Example

```python
@dataclass
class Instance(CloudFormationResource):
    """AWS::EC2::Instance resource."""

    resource_type: ClassVar[str] = "AWS::EC2::Instance"

    # Properties (snake_case, maps to PascalCase)
    image_id: Optional[Union[str, Ref, GetAtt]] = None
    instance_type: Optional[Union[str, Ref]] = None
    subnet_id: Optional[Union[str, Ref, GetAtt]] = None
    security_group_ids: Optional[List[Union[str, Ref]]] = None
    tags: Optional[List["Tag"]] = None

    # Typed attribute accessors
    @property
    def attr_public_ip(self) -> GetAtt:
        return self.get_att("PublicIp")
```

### 2.3 Intrinsic Functions

Type-safe intrinsic functions as dataclasses:

```python
@dataclass
class Ref:
    logical_id: str
    def to_dict(self) -> Dict[str, Any]:
        return {"Ref": self.logical_id}

@dataclass
class GetAtt:
    logical_id: str
    attribute_name: str
    def to_dict(self) -> Dict[str, Any]:
        return {"Fn::GetAtt": [self.logical_id, self.attribute_name]}

@dataclass
class Sub:
    template_string: str
    variables: Optional[Dict[str, Union[str, Ref, GetAtt]]] = None
    def to_dict(self) -> Dict[str, Any]: ...
```

### 2.4 Type System

**CloudFormation → Python Mappings:**
- `String` → `str`
- `Integer/Long` → `int`
- `Double` → `float`
- `Boolean` → `bool`
- `Json` → `Dict[str, Any]`
- Lists → `List[T]`
- Property types → nested dataclasses

**Union types for flexibility:**
```python
# String property accepts literal or intrinsic functions
instance_type: Optional[Union[str, Ref]] = None
```

### 2.5 Validation Strategy

**Two-layer validation (no additional libraries required):**

1. **Static Type Checking** - mypy/pyright catch type errors before runtime
2. **CloudFormation Validation** - AWS validates template during deployment

Pure Python dataclasses with type annotations provide static analysis. No runtime validation libraries (like Pydantic) needed - keeps dependencies minimal and lets CloudFormation be the source of truth.

---

## 3. API Design Examples

### Context Layer: Deployment Environment Defaults

**Define your deployment context as a dataclass:**

```python
from dataclasses import dataclass
from cloudformation_dataclasses.core import Tag, DeploymentContext

@dataclass
class EnvironmentTag:
    resource: Tag
    key: str = "Environment"
    value: str = "production"

@dataclass
class ProjectTag:
    resource: Tag
    key: str = "Project"
    value: str = "myapp"

@dataclass
class ManagedByTag:
    resource: Tag
    key: str = "ManagedBy"
    value: str = "cloudformation_dataclasses"

@dataclass
class MyDeploymentContext:
    """Wrapper for deployment context - name: 'MyDeploymentContext'"""

    context: DeploymentContext
    component: str = "MyComponent"
    environment: str = "Prod"
    naming_suffix: str = "100"
    naming_group: str = "A"
    region: str = "us-east-1"
    account_id: str = "123456789012"
    project_name: str = "myapp"
    tags = [EnvironmentTag, ProjectTag, ManagedByTag]

# Block-style instantiation with defaults - name inferred from class
ctx = MyDeploymentContext()

# Example resource naming:
# ctx.resource_name("MyBucket") -> "MyComponent-MyBucket-Prod-100A"
```

### Example 1: Single S3 Bucket (Block Style)

**Wrapper dataclass with resource field - name inferred from class:**

```python
from dataclasses import dataclass
from cloudformation_dataclasses.aws.s3 import Bucket
from cloudformation_dataclasses.core import Tag

@dataclass
class ServerSideEncryptionByDefault:
    sse_algorithm: str = "AES256"

@dataclass
class ServerSideEncryptionRule:
    server_side_encryption_by_default: ServerSideEncryptionByDefault

@dataclass
class BucketEncryption:
    server_side_encryption_configuration: list[ServerSideEncryptionRule]

@dataclass
class VersioningConfiguration:
    status: str = "Enabled"

@dataclass
class DataClassificationTag:
    """Custom tag for this specific bucket"""

    resource: Tag
    key: str = "DataClassification"
    value: str = "sensitive"

@dataclass
class MyDataBucket:
    """Bucket name inferred from class name: 'MyDataBucket'"""

    resource: Bucket
    versioning_configuration: VersioningConfiguration
    bucket_encryption: BucketEncryption
    tags = [DataClassificationTag]  # Custom tags - context tags auto-merged
    context = ctx  # Provides naming + base tags

# Instantiate - resource_name automatically becomes "MyComponent-MyDataBucket-Prod-100A"
my_bucket = MyDataBucket()
print(my_bucket.resource_name)  # "MyComponent-MyDataBucket-Prod-100A"
print(my_bucket.all_tags)  # [EnvironmentTag, ProjectTag, ManagedByTag, DataClassificationTag]

# Generate CloudFormation template
template = my_bucket.to_cloudformation()
print(template.to_json())  # or template.to_yaml()
```

### Example 2: VPC with Subnet (Block Style, Manual Wiring)

**VPC and Subnet as wrapper dataclasses - names from class names:**

```python
from dataclasses import dataclass
from cloudformation_dataclasses.aws.ec2 import VPC, Subnet

@dataclass
class MyVPC:
    """Wrapper for VPC - resource name: 'MyVPC'"""

    resource: VPC
    cidr_block: str = "10.0.0.0/16"
    enable_dns_hostnames: bool = True
    enable_dns_support: bool = True

@dataclass
class MySubnet:
    """Wrapper for Subnet - resource name: 'MySubnet'"""

    resource: Subnet
    cidr_block: str = "10.0.1.0/24"
    vpc_id: MyVPC.ref()
    availability_zone: str = f"{ctx.region}a"
    map_public_ip_on_launch: bool = True

# Instantiate
my_vpc = MyVPC()
my_subnet = MySubnet()

# Generate CloudFormation
template = Template()
template.add_resource(my_vpc)
template.add_resource(my_subnet)
print(template.to_json())
```

### Example 3: EC2 Web Server (Block Style, Declarative Wiring)

**Web server with VPC, Subnet, SecurityGroup, and Instance - all wiring in dataclass fields:**

```python
from dataclasses import dataclass, field
from cloudformation_dataclasses.aws.ec2 import VPC, Subnet, Instance, SecurityGroup, SecurityGroupIngress
from cloudformation_dataclasses.core import Template

@dataclass
class HttpIngress:
    """HTTP ingress rule"""

    resource: SecurityGroupIngress
    ip_protocol: str = "tcp"
    from_port: int = 80
    to_port: int = 80
    cidr_ip: str = "0.0.0.0/0"

@dataclass
class MyVPC:
    """Wrapper for VPC - resource name: 'MyVPC'"""

    resource: VPC
    cidr_block: str = "10.0.0.0/16"
    enable_dns_hostnames: bool = True
    enable_dns_support: bool = True

@dataclass
class MySubnet:
    """Wrapper for Subnet - resource name: 'MySubnet'"""

    resource: Subnet
    cidr_block: str = "10.0.1.0/24"
    vpc_id: MyVPC.ref()
    availability_zone: str = f"{ctx.region}a"
    map_public_ip_on_launch: bool = True

@dataclass
class MySecurityGroup:
    """Wrapper for SecurityGroup - resource name: 'MySecurityGroup'"""

    resource: SecurityGroup
    group_description: str = "Allow HTTP traffic"
    vpc_id: MyVPC.ref()
    security_group_ingress = [HttpIngress]

@dataclass
class MyWebServer:
    """Wrapper for Instance - resource name: 'MyWebServer'"""

    resource: Instance
    instance_type: str = "t3.micro"
    image_id: str = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2
    subnet_id: MySubnet.ref()
    security_group_ids = [MySecurityGroup]  # List reference by class name
    tags = ctx.tags

# Instantiate - no wiring needed, it's all in the dataclasses
http_ingress = HttpIngress()
my_vpc = MyVPC()
my_subnet = MySubnet()
my_sg = MySecurityGroup()
my_instance = MyWebServer()

# Generate CloudFormation
template = Template()
template.add_resource(my_vpc)
template.add_resource(my_subnet)
template.add_resource(my_sg)
template.add_resource(my_instance)
print(template.to_json())
```


---

## 4. Critical Files to Create

### Project Structure

```
cloudformation_dataclasses/             # Repository folder
├── pyproject.toml                      # Package metadata (name: cloudformation_dataclasses)
├── README.md
├── LICENSE
└── src/
    └── cloudformation_dataclasses/     # Python module
        ├── __init__.py
        ├── core/
        │   ├── __init__.py
        │   ├── base.py                 # CloudFormationResource, Tag, DeploymentContext
        │   └── template.py             # Template, Parameter, Output, Condition
        ├── intrinsics/
        │   ├── __init__.py
        │   └── functions.py            # Ref, GetAtt, Sub, Join, If, etc.
        ├── codegen/
        │   ├── __init__.py
        │   ├── spec_parser.py          # AWS spec downloader and parser
        │   └── generator.py            # Dataclass code generator
        └── aws/                        # Generated AWS resource modules
            ├── __init__.py
            ├── s3.py                   # Generated S3 resources
            ├── ec2.py                  # Generated EC2 resources
            └── ...                     # Other AWS services
```

### Key Files

1. **[src/cloudformation_dataclasses/core/base.py](cloudformation_dataclasses/src/cloudformation_dataclasses/core/base.py)**
   - `CloudFormationResource` base class
   - `Tag` class
   - `DeploymentContext` base class
   - Common resource functionality (ref(), get_att(), to_dict())
   - Auto-naming support (resource_name property)
   - Auto-merging tags (all_tags property)

2. **[src/cloudformation_dataclasses/intrinsics/functions.py](cloudformation_dataclasses/src/cloudformation_dataclasses/intrinsics/functions.py)**
   - Ref, GetAtt, Sub, Join, If, etc.
   - Type-safe intrinsic function classes
   - Serialization to CloudFormation JSON/YAML

3. **[src/cloudformation_dataclasses/core/template.py](cloudformation_dataclasses/src/cloudformation_dataclasses/core/template.py)**
   - Template class
   - Parameter, Output, Condition classes
   - Serialization to JSON/YAML
   - Template validation

4. **[src/cloudformation_dataclasses/codegen/spec_parser.py](cloudformation_dataclasses/src/cloudformation_dataclasses/codegen/spec_parser.py)**
   - Download CloudFormation specs from AWS
   - Parse ResourceTypes and PropertyTypes
   - Extract resource metadata
   - Handle spec updates

5. **[src/cloudformation_dataclasses/codegen/generator.py](cloudformation_dataclasses/src/cloudformation_dataclasses/codegen/generator.py)**
   - Generate dataclass definitions from specs
   - Type mapping (CloudFormation → Python)
   - Create typed attribute properties
   - Format generated code with Black
   - Generate per-service modules (s3.py, ec2.py, etc.)

6. **Project Setup (uv-managed)**
   - **Package name**: `cloudformation_dataclasses` (on PyPI)
   - **Repository folder**: `cloudformation_dataclasses/`
   - **Python module**: `cloudformation_dataclasses` (in `src/` directory)
   - **Module import**: `from cloudformation_dataclasses import ...`
   - **Initialize**: `uv init cloudformation_dataclasses` with src-layout
   - **pyproject.toml**: Generated and managed by uv
     ```toml
     [project]
     name = "cloudformation_dataclasses"
     version = "0.1.0"
     description = "Python dataclasses for AWS CloudFormation template synthesis"
     requires-python = ">=3.13"
     dependencies = []  # Zero runtime dependencies!

     [project.optional-dependencies]
     yaml = ["pyyaml>=6.0"]
     dev = ["mypy", "pytest", "ruff", "black", "requests"]
     ```
   - **Runtime dependencies**: NONE - zero dependencies!
   - **Optional dependencies**:
     - `pyyaml` - YAML serialization via `pip install cloudformation_dataclasses[yaml]`
   - **Development dependencies** (NOT shipped with package):
     - `black` - Code formatting for generated files (build-time only)
     - `mypy` - Static type checking
     - `pytest` - Testing framework
     - `ruff` - Fast Python linter
     - `requests` - Download CloudFormation specs (codegen only)

---

## 5. Code Generation Deep Dive

### 5.1 CloudFormation Spec Structure

The AWS CloudFormation Resource Specification is a JSON file with this structure:

```json
{
  "PropertyTypes": {
    "AWS::S3::Bucket.VersioningConfiguration": {
      "Documentation": "...",
      "Properties": {
        "Status": {
          "Documentation": "...",
          "PrimitiveType": "String",
          "Required": true
        }
      }
    }
  },
  "ResourceTypes": {
    "AWS::S3::Bucket": {
      "Documentation": "...",
      "Properties": {
        "BucketName": {
          "Documentation": "...",
          "PrimitiveType": "String",
          "Required": false
        },
        "VersioningConfiguration": {
          "Documentation": "...",
          "Type": "VersioningConfiguration",
          "Required": false
        },
        "Tags": {
          "Documentation": "...",
          "Type": "List",
          "ItemType": "Tag",
          "Required": false
        }
      },
      "Attributes": {
        "Arn": {
          "PrimitiveType": "String"
        },
        "DomainName": {
          "PrimitiveType": "String"
        }
      }
    }
  }
}
```

### 5.2 Type Mapping Strategy

**CloudFormation Type → Python Type Mapping:**

| CloudFormation Type | Python Type | Notes |
|---------------------|-------------|-------|
| `String` | `str` | Literal string values |
| `Integer` | `int` | Whole numbers |
| `Long` | `int` | Python int handles arbitrary precision |
| `Double` | `float` | Floating point numbers |
| `Boolean` | `bool` | True/False values |
| `Json` | `Dict[str, Any]` | Arbitrary JSON objects |
| `Timestamp` | `str` | ISO 8601 timestamp strings |
| `List` (primitive) | `List[T]` | Where T is the mapped primitive type |
| `List` (complex) | `List[PropertyClass]` | Nested property type dataclass |
| `Map` | `Dict[str, T]` | Key-value mappings |
| PropertyType reference | Nested dataclass | e.g., `VersioningConfiguration` |

**Union Types for Intrinsic Function Support:**

Every property type is wrapped in a Union to support CloudFormation intrinsic functions:

```python
# String property
property_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

# Integer property
count: Optional[Union[int, Ref]] = None

# Boolean property
enabled: Optional[Union[bool, Ref, If]] = None

# List property
items: Optional[Union[List[str], Ref]] = None
```

### 5.3 Property Name Conversion

**PascalCase → snake_case Rules:**

```python
def to_snake_case(name: str) -> str:
    """
    Convert PascalCase to snake_case.

    Examples:
        BucketName -> bucket_name
        VPCId -> vpc_id
        S3Key -> s3_key
        IPv6CidrBlock -> ipv6_cidr_block
    """
    # Insert underscore before uppercase letters (except at start)
    result = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    # Insert underscore before uppercase in acronyms
    result = re.sub('([a-z0-9])([A-Z])', r'\1_\2', result)
    return result.lower()
```

**Reserved Python Keywords:**

If a property name conflicts with Python keywords, append underscore:

```python
# CloudFormation property "Type" conflicts with Python
type_: Optional[str] = None  # Maps to CloudFormation "Type"
```

### 5.4 Code Generation Algorithm

**Step-by-step generation process:**

```python
def generate_resource_class(resource_name: str, resource_spec: dict) -> str:
    """
    Generate a dataclass for a CloudFormation resource.

    Args:
        resource_name: e.g., "AWS::S3::Bucket"
        resource_spec: The resource specification from the JSON

    Returns:
        Generated Python dataclass code as string
    """

    # 1. Extract service and class name
    # "AWS::S3::Bucket" -> service="s3", class_name="Bucket"
    parts = resource_name.split("::")
    service = parts[1].lower()
    class_name = parts[2]

    # 2. Generate nested property type dataclasses first
    property_classes = []
    for prop_name, prop_spec in resource_spec.get("Properties", {}).items():
        if "Type" in prop_spec and not is_primitive_type(prop_spec["Type"]):
            # Generate nested dataclass for complex property type
            property_classes.append(
                generate_property_class(prop_spec["Type"], spec)
            )

    # 3. Generate main resource class
    class_code = f'@dataclass\n'
    class_code += f'class {class_name}(CloudFormationResource):\n'

    # Add docstring from AWS documentation
    if "Documentation" in resource_spec:
        class_code += f'    """{resource_spec["Documentation"]}"""\n\n'

    # Add resource_type class variable
    class_code += f'    resource_type: ClassVar[str] = "{resource_name}"\n\n'

    # 4. Generate property fields
    for prop_name, prop_spec in resource_spec.get("Properties", {}).items():
        snake_name = to_snake_case(prop_name)
        python_type = map_type(prop_spec)
        required = prop_spec.get("Required", False)

        # Add property docstring
        if "Documentation" in prop_spec:
            class_code += f'    # {prop_spec["Documentation"]}\n'

        # Generate field with type annotation
        if required:
            class_code += f'    {snake_name}: {python_type}\n'
        else:
            class_code += f'    {snake_name}: Optional[{python_type}] = None\n'

    # 5. Generate typed attribute accessor properties
    for attr_name, attr_spec in resource_spec.get("Attributes", {}).items():
        snake_name = to_snake_case(attr_name)
        class_code += f'\n    @property\n'
        class_code += f'    def attr_{snake_name}(self) -> GetAtt:\n'
        class_code += f'        """Get the {attr_name} attribute."""\n'
        class_code += f'        return self.get_att("{attr_name}")\n'

    return "\n\n".join(property_classes) + "\n\n" + class_code
```

### 5.5 Generated Code Examples

**Example 1: Simple Resource (S3 Bucket)**

From CloudFormation spec:
```json
{
  "AWS::S3::Bucket": {
    "Properties": {
      "BucketName": {
        "PrimitiveType": "String",
        "Required": false
      },
      "VersioningConfiguration": {
        "Type": "VersioningConfiguration",
        "Required": false
      }
    },
    "Attributes": {
      "Arn": {"PrimitiveType": "String"},
      "DomainName": {"PrimitiveType": "String"}
    }
  }
}
```

Generated Python:
```python
@dataclass
class VersioningConfiguration:
    """Versioning configuration for S3 bucket."""
    status: Optional[Union[str, Ref]] = None


@dataclass
class Bucket(CloudFormationResource):
    """AWS::S3::Bucket - Amazon S3 bucket resource."""

    resource_type: ClassVar[str] = "AWS::S3::Bucket"

    # The name of the bucket
    bucket_name: Optional[Union[str, Ref, Sub]] = None

    # Versioning configuration for this bucket
    versioning_configuration: Optional[VersioningConfiguration] = None

    @property
    def attr_arn(self) -> GetAtt:
        """Get the Arn attribute."""
        return self.get_att("Arn")

    @property
    def attr_domain_name(self) -> GetAtt:
        """Get the DomainName attribute."""
        return self.get_att("DomainName")
```

**Example 2: Complex Resource (EC2 Instance)**

Generated code includes:
- Multiple nested property type dataclasses
- Required and optional fields
- List properties
- Typed attribute accessors

```python
@dataclass
class BlockDeviceMapping:
    """Block device mapping for EC2 instance."""
    device_name: Union[str, Ref]
    ebs: Optional["EbsBlockDevice"] = None
    virtual_name: Optional[Union[str, Ref]] = None


@dataclass
class EbsBlockDevice:
    """EBS block device configuration."""
    volume_size: Optional[Union[int, Ref]] = None
    volume_type: Optional[Union[str, Ref]] = None
    encrypted: Optional[Union[bool, Ref, If]] = None


@dataclass
class Instance(CloudFormationResource):
    """AWS::EC2::Instance - EC2 virtual server."""

    resource_type: ClassVar[str] = "AWS::EC2::Instance"

    # Amazon Machine Image ID (required)
    image_id: Union[str, Ref, GetAtt]

    # Instance type (e.g., t3.micro)
    instance_type: Union[str, Ref]

    # Block device mappings
    block_device_mappings: Optional[List[BlockDeviceMapping]] = None

    # Subnet ID for the instance
    subnet_id: Optional[Union[str, Ref, GetAtt]] = None

    # Security group IDs
    security_group_ids: Optional[List[Union[str, Ref]]] = None

    @property
    def attr_availability_zone(self) -> GetAtt:
        """Get the AvailabilityZone attribute."""
        return self.get_att("AvailabilityZone")

    @property
    def attr_private_dns_name(self) -> GetAtt:
        """Get the PrivateDnsName attribute."""
        return self.get_att("PrivateDnsName")

    @property
    def attr_public_ip(self) -> GetAtt:
        """Get the PublicIp attribute."""
        return self.get_att("PublicIp")
```

### 5.6 Handling Edge Cases

**1. Recursive Property Types:**

Some AWS resources have circular references. Handle with forward references:

```python
@dataclass
class Rule:
    """Security group rule that may reference other security groups."""
    source_security_group_id: Optional[Union[str, Ref, "SecurityGroup"]] = None
```

**2. Polymorphic Properties:**

Some properties accept multiple distinct types:

```python
# CloudFormation allows string or object for some properties
code: Optional[Union[str, Code]] = None
```

**3. List of Primitives vs List of Objects:**

```python
# List of strings
availability_zones: Optional[Union[List[str], Ref]] = None

# List of complex objects
rules: Optional[List[SecurityGroupRule]] = None
```

**4. Properties Named After Python Builtins:**

```python
# "Type" conflicts with builtin
type_: Optional[Union[str, Ref]] = None

# Mapping in serialization preserves CloudFormation name
def to_dict(self) -> dict:
    result = {}
    if self.type_ is not None:
        result["Type"] = serialize(self.type_)
    return result
```

### 5.7 Validation Strategy

**Two-layer validation approach:**

The library uses a **defense-in-depth** validation strategy with two complementary layers:

#### Layer 1: Static Type Checking (Development Time)

Python's type system + mypy/pyright catches errors before code runs:

```python
from cloudformation_dataclasses.aws.s3 import Bucket
from cloudformation_dataclasses.aws.ec2 import Instance, VPC, Subnet

# ✅ Type checker catches type mismatches
@dataclass
class MyBucket:
    resource: Bucket
    bucket_name: int = 123  # ❌ Type error: Expected str, got int

# ✅ Type checker ensures required fields
@dataclass
class MyInstance:
    resource: Instance
    # ❌ Missing required fields: image_id, instance_type

# ✅ Type checker validates cross-resource references
@dataclass
class MyVPC:
    resource: VPC
    cidr_block: str = "10.0.0.0/16"

@dataclass
class MySubnet:
    resource: Subnet
    cidr_block: str = "10.0.1.0/24"
    vpc_id: MyBucket.ref()  # ❌ Type error: Expected VPC ref, got Bucket ref
```

**What static typing catches:**
- Wrong primitive types (str vs int vs bool)
- Missing required properties in wrapper dataclasses
- Invalid property names (typos caught via autocomplete)
- Type-incompatible cross-resource references
- List vs scalar mismatches

**What static typing doesn't catch:**
- Invalid string values (e.g., invalid instance type "t99.invalid")
- Cross-resource constraint violations
- Region-specific limitations
- Property value ranges and patterns
- Complex business rules

#### Layer 2: CloudFormation Validation (Deployment Time)

AWS CloudFormation validates the complete template:

```python
# This passes Python type checking but fails CloudFormation validation
@dataclass
class MyVPC:
    resource: VPC
    cidr_block: str = "10.0.0.0/16"

@dataclass
class MyInstance:
    resource: Instance
    image_id: str = "ami-12345"
    instance_type: str = "t99.invalid"  # Invalid instance type - CloudFormation rejects
    vpc_id: MyVPC.ref()

# Instantiate
my_vpc = MyVPC()
my_instance = MyInstance()

# Generate template
template = Template()
template.add_resource(my_vpc)
template.add_resource(my_instance)

# When deployed, CloudFormation returns detailed error:
# "Value (t99.invalid) for parameter instanceType is invalid.
#  Valid values: t3.micro, t3.small, ..."
```

**Validation happens during:**
1. **Template validation** - `aws cloudformation validate-template`
2. **Stack creation/update** - CloudFormation validates before applying changes
3. **Change sets** - Preview changes with validation before execution

**Why this approach?**

1. **Single Source of Truth**: CloudFormation spec is the ultimate authority
2. **No Duplication**: Avoid reimplementing AWS's validation logic in Python
3. **Always Current**: AWS updates validation rules server-side
4. **Fast Feedback Loop**: Type checking gives instant feedback, CloudFormation catches the rest
5. **Minimal Dependencies**: No Pydantic, no validation frameworks needed

#### Optional: Template Validation Helper

For users who want pre-deployment validation:

```python
from cloudformation_dataclasses.validation import validate_template

# Define resources using block syntax
@dataclass
class MyBucket:
    resource: Bucket
    bucket_name: str = "my-bucket"

@dataclass
class MyVPC:
    resource: VPC
    cidr_block: str = "10.0.0.0/16"

# Instantiate
my_bucket = MyBucket()
my_vpc = MyVPC()

# Build template
template = Template()
template.add_resource(my_bucket)
template.add_resource(my_vpc)

# Optional: Validate via AWS API before deployment
try:
    validate_template(template.to_json())
    print("✅ Template is valid")
except ValidationError as e:
    print(f"❌ Template validation failed: {e}")
```

This calls AWS's `validate-template` API but is **optional** - users can skip it and let CloudFormation validate during deployment.

#### Validation Testing Strategy

Generated code includes tests that verify:

1. **Spec compliance**: Generated types match CloudFormation spec
2. **Serialization correctness**: Dataclasses serialize to valid CloudFormation JSON
3. **Required fields**: Mypy catches missing required properties
4. **Type safety**: Invalid types rejected at static analysis time

```python
# tests/test_generated_s3.py

# Test wrapper definitions (block syntax)
@dataclass
class TestBucket:
    resource: Bucket
    bucket_name: str = "my-test-bucket"

@dataclass
class TestVPC:
    resource: VPC
    cidr_block: str = "10.0.0.0/16"

@dataclass
class TestSubnet:
    resource: Subnet
    cidr_block: str = "10.0.1.0/24"
    vpc_id: TestVPC.ref()  # Reference to VPC


def test_bucket_serialization():
    """Verify bucket wrapper serializes to valid CloudFormation JSON"""
    bucket = TestBucket()
    result = bucket.to_dict()

    assert result == {
        "Type": "AWS::S3::Bucket",
        "Properties": {
            "BucketName": "my-test-bucket"
        }
    }


def test_intrinsic_functions():
    """Verify intrinsic functions serialize correctly"""
    vpc = TestVPC()
    subnet = TestSubnet()

    result = subnet.to_dict()
    assert result["Properties"]["VpcId"] == {"Ref": "TestVPC"}


def test_mypy_catches_type_errors():
    """This file intentionally has type errors for mypy to catch"""
    # Run: mypy tests/test_type_errors.py --strict
    # Expected: mypy reports errors

    @dataclass
    class InvalidBucket:
        resource: Bucket
        bucket_name: int = 123  # ❌ Type error: int is not str
```

### 5.8 Module Organization

**Service-based module structure:**

Each AWS service gets its own module file in `src/cloudformation_dataclasses/aws/`:

- `s3.py` - All S3 resources (Bucket, BucketPolicy, AccessPoint, etc.)
- `ec2.py` - All EC2 resources (Instance, VPC, Subnet, SecurityGroup, etc.)
- `lambda_.py` - Lambda resources (underscore to avoid Python keyword)
- `rds.py` - RDS resources (DBInstance, DBCluster, etc.)
- `iam.py` - IAM resources (Role, Policy, User, Group, etc.)

**Module header template:**

```python
"""
AWS CloudFormation S3 Resources

Auto-generated from AWS CloudFormation Resource Specification.
Specification version: {spec_version}
Generated on: {generation_timestamp}

DO NOT EDIT - This file is automatically generated.
To regenerate: python -m cloudformation_dataclasses.codegen.generator
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List, Optional, Union

from cloudformation_dataclasses.core.base import CloudFormationResource
from cloudformation_dataclasses.intrinsics.functions import Ref, GetAtt, Sub, Join, If


# All S3 resource and property type dataclasses follow...
```

---

## 6. Package Build and Distribution Strategy

### 6.1 Pre-Generation Approach

**All AWS resource classes are pre-generated and committed to the repository.**

**Rationale:**
- **Reliability**: Users get tested, stable generated code
- **No runtime dependencies**: No need for code generation at install time
- **IDE support**: Immediate autocomplete and type checking
- **Transparency**: Users can browse generated code on GitHub
- **Faster installs**: No generation step during pip install

**Trade-offs:**
- Larger repository size (~50-100MB of generated Python code)
- Updates require regeneration and new package release
- Git history includes generated file changes

### 6.2 Build Process

**Pre-publish build steps:**

```bash
# 1. Download latest CloudFormation spec
python -m cloudformation_dataclasses.codegen.spec_parser download

# 2. Generate all AWS resource modules
python -m cloudformation_dataclasses.codegen.generator --all

# 3. Format generated code
uv run black src/cloudformation_dataclasses/aws/

# 4. Type check
uv run mypy src/cloudformation_dataclasses/

# 5. Run tests
uv run pytest tests/

# 6. Build package
uv build

# 7. Publish to PyPI
uv publish
```

**Build script: `scripts/build.sh`**

```bash
#!/bin/bash
set -e

echo "Building cloudformation_dataclasses package..."

# Download latest CloudFormation spec
echo "Downloading CloudFormation spec..."
python -m cloudformation_dataclasses.codegen.spec_parser download

# Generate all resource modules
echo "Generating resource classes..."
python -m cloudformation_dataclasses.codegen.generator --all

# Format with Black
echo "Formatting generated code..."
uv run black src/cloudformation_dataclasses/aws/

# Lint with Ruff
echo "Linting..."
uv run ruff check src/

# Type check with mypy
echo "Type checking..."
uv run mypy src/cloudformation_dataclasses/

# Run tests
echo "Running tests..."
uv run pytest tests/ -v

# Build package
echo "Building package..."
uv build

echo "Build complete! Package ready in dist/"
```

### 6.3 Package Structure

**Published package contents:**

```
cloudformation_dataclasses/
├── src/
│   └── cloudformation_dataclasses/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── base.py
│       │   └── template.py
│       ├── intrinsics/
│       │   ├── __init__.py
│       │   └── functions.py
│       ├── codegen/                    # Code generation tools
│       │   ├── __init__.py
│       │   ├── spec_parser.py
│       │   └── generator.py
│       └── aws/                        # GENERATED - Committed to git
│           ├── __init__.py             # Exports all resources
│           ├── s3.py                   # ~5,000 lines
│           ├── ec2.py                  # ~15,000 lines
│           ├── lambda_.py              # ~2,000 lines
│           ├── rds.py                  # ~8,000 lines
│           ├── iam.py                  # ~4,000 lines
│           ├── dynamodb.py
│           ├── cloudfront.py
│           ├── route53.py
│           └── ...                     # ~300+ service modules
├── tests/
├── scripts/
│   ├── build.sh
│   └── regenerate.sh
├── pyproject.toml
├── README.md
└── LICENSE
```

**Estimated package size:**
- Generated code: ~80MB uncompressed, ~8MB compressed
- Total package: ~10MB wheel file
- PyPI download: ~10MB

### 6.4 Version Strategy

**Semantic Versioning with Spec Tracking:**

```
Package Version: X.Y.Z
  X = Major version (breaking API changes)
  Y = Minor version (new AWS resources/properties, non-breaking)
  Z = Patch version (bug fixes, documentation)
```

**Examples:**
- `0.1.0` - Initial release
- `0.2.0` - New AWS resources added (e.g., new EC2 instance types)
- `0.2.1` - Bug fix in code generation
- `1.0.0` - Stable API, production ready

**Track CloudFormation spec version in metadata:**

```python
# src/cloudformation_dataclasses/__init__.py
__version__ = "0.1.0"
__spec_version__ = "116.0.0"  # AWS CloudFormation spec version
__spec_date__ = "2024-01-15"
```

### 6.5 Update Cadence

**Release strategy:**

1. **Monthly releases** - Check for CloudFormation spec updates monthly
2. **On-demand releases** - For critical new AWS resources/features
3. **Automated detection** - CI/CD checks for spec updates daily

**GitHub Actions workflow for spec monitoring:**

```yaml
# .github/workflows/check-spec-updates.yml
name: Check CloudFormation Spec Updates

on:
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight UTC
  workflow_dispatch:

jobs:
  check-updates:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'

      - name: Install dependencies
        run: |
          pip install uv
          uv sync

      - name: Check for spec updates
        run: |
          python -m cloudformation_dataclasses.codegen.spec_parser check-updates

      - name: Create issue if updates available
        if: steps.check.outputs.updated == 'true'
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: 'New CloudFormation Spec Available',
              body: 'AWS has released a new CloudFormation spec. Consider regenerating resources and releasing a new version.'
            })
```

### 6.6 CI/CD Pipeline

**Complete CI/CD for releases:**

```yaml
# .github/workflows/release.yml
name: Release Package

on:
  push:
    tags:
      - 'v*'

jobs:
  build-and-publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'

      - name: Install uv
        run: pip install uv

      - name: Install dependencies
        run: uv sync --all-extras

      - name: Download CloudFormation spec
        run: python -m cloudformation_dataclasses.codegen.spec_parser download

      - name: Generate resource classes
        run: python -m cloudformation_dataclasses.codegen.generator --all

      - name: Format code
        run: uv run black src/cloudformation_dataclasses/aws/

      - name: Type check
        run: uv run mypy src/cloudformation_dataclasses/

      - name: Run tests
        run: uv run pytest tests/ -v --cov

      - name: Build package
        run: uv build

      - name: Publish to PyPI
        env:
          UV_PUBLISH_TOKEN: ${{ secrets.PYPI_TOKEN }}
        run: uv publish

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v1
        with:
          files: dist/*
          generate_release_notes: true
```

### 6.7 Development Workflow

**For contributors and maintainers:**

```bash
# Clone repository
git clone https://github.com/yourusername/cloudformation_dataclasses.git
cd cloudformation_dataclasses

# Install development dependencies
uv sync --all-extras

# Regenerate ALL resource classes from latest spec
./scripts/regenerate.sh

# Regenerate specific service
python -m cloudformation_dataclasses.codegen.generator --service s3

# Run tests
uv run pytest tests/ -v

# Type check
uv run mypy src/

# Format code
uv run black src/ tests/

# Lint
uv run ruff check src/ tests/
```

**Regeneration script: `scripts/regenerate.sh`**

```bash
#!/bin/bash
# Regenerate all AWS resource classes from CloudFormation spec

set -e

echo "Regenerating CloudFormation resource classes..."

# Download latest spec
echo "Downloading latest CloudFormation spec..."
python -m cloudformation_dataclasses.codegen.spec_parser download

# Clean existing generated files
echo "Cleaning existing generated files..."
rm -rf src/cloudformation_dataclasses/aws/*.py
touch src/cloudformation_dataclasses/aws/__init__.py

# Generate all resources
echo "Generating resource classes (this may take a few minutes)..."
python -m cloudformation_dataclasses.codegen.generator --all

# Format
echo "Formatting generated code..."
uv run black src/cloudformation_dataclasses/aws/

echo "Regeneration complete!"
echo "Generated files are in src/cloudformation_dataclasses/aws/"
echo "Don't forget to run tests: uv run pytest tests/"
```

### 6.8 pyproject.toml Configuration

**Complete pyproject.toml:**

```toml
[project]
name = "cloudformation_dataclasses"
version = "0.1.0"
description = "Python dataclasses for AWS CloudFormation template synthesis"
authors = [
    {name = "Your Name", email = "you@example.com"}
]
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.13"
keywords = ["aws", "cloudformation", "infrastructure", "iac", "dataclasses"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.13",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: System :: Systems Administration",
]

dependencies = []  # Zero runtime dependencies!

[project.optional-dependencies]
yaml = [
    "pyyaml>=6.0",  # For YAML template serialization
]
dev = [
    # Development/build-time only - NOT shipped with the package
    "mypy>=1.8",
    "pytest>=7.4",
    "pytest-cov>=4.1",
    "ruff>=0.1",
    "black>=23.12",
    "requests>=2.31",  # For downloading CloudFormation specs during codegen
]

[project.urls]
Homepage = "https://github.com/yourusername/cloudformation_dataclasses"
Documentation = "https://cloudformation-dataclasses.readthedocs.io"
Repository = "https://github.com/yourusername/cloudformation_dataclasses"
Issues = "https://github.com/yourusername/cloudformation_dataclasses/issues"

# uv automatically handles build system - no [build-system] section needed
# uv will use hatchling by default for src-layout projects

[tool.uv]
dev-dependencies = [
    "mypy>=1.8",
    "pytest>=7.4",
    "pytest-cov>=4.1",
    "ruff>=0.1",
    "black>=23.12",
]

[tool.black]
line-length = 100
target-version = ['py313']
include = '\.pyi?$'

[tool.ruff]
line-length = 100
target-version = "py313"

[tool.mypy]
python_version = "3.13"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --cov=cloudformation_dataclasses --cov-report=term-missing"

[tool.coverage.run]
source = ["src/cloudformation_dataclasses"]
omit = [
    "*/tests/*",
    "*/codegen/*",  # Exclude code generation tools from coverage
]
```

### 6.9 Generated File Management

**Git strategy for generated files:**

```gitignore
# .gitignore - DO NOT ignore generated files
# Generated files are committed to ensure reliability

# Ignore Python artifacts
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Ignore test artifacts
.pytest_cache/
.coverage
htmlcov/

# Ignore IDE files
.vscode/
.idea/
*.swp
*.swo

# Ignore spec download cache (regenerated on build)
.cloudformation_spec_cache/
```

**Generated file header:**

Every generated file includes a header warning not to edit manually:

```python
"""
AWS CloudFormation EC2 Resources

⚠️  AUTO-GENERATED FILE - DO NOT EDIT MANUALLY ⚠️

This file is automatically generated from the AWS CloudFormation Resource Specification.

Specification Version: 116.0.0
Generated: 2024-01-15T10:30:00Z
Generator: cloudformation_dataclasses.codegen.generator v0.1.0

To regenerate this file:
    python -m cloudformation_dataclasses.codegen.generator --service ec2

Or regenerate all services:
    ./scripts/regenerate.sh
"""
```

---

## 7. Conclusion

`cloudformation_dataclasses` fills a critical gap in the Python CloudFormation ecosystem by **making dataclasses the interface for declarative infrastructure**.

### The Core Innovation: Wrapper Dataclasses with Declarative Wiring

The primary value is **all infrastructure wiring happens inside dataclass field declarations**:

1. **No Imperative Code** - Wiring is field declarations, not instantiation parameters
2. **Wrapper Pattern** - Each resource wrapped with `resource:` field indicating CloudFormation type
3. **References as Fields** - `vpc_id: MyVPC.ref()` declared in dataclass, not at call site
4. **Scannable Infrastructure** - All properties and relationships visible in one dataclass definition
5. **Type-Safe by Default** - Python type system validates all properties and references

### Technical Benefits

- **Modern Python (3.13+)** - Latest language features for best developer experience
- **Pure Python** - No Node.js dependency overhead
- **Auto-Generated** - Stay current with AWS via automated spec updates
- **IDE-Native** - Full autocomplete, type checking, refactoring support

The architecture leverages automated code generation to stay current with AWS while providing a **dataclass-first interface that makes infrastructure code as readable as it is type-safe**. Infrastructure-as-code should be easy to understand, maintain, and evolve—dataclasses deliver this naturally.

---

## References

- AWS CloudFormation Resource Specification: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html
- Specification JSON: https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json
