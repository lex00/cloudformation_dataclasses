# cloudformation_dataclasses vs AWS CDK (Python)

This document compares cloudformation_dataclasses with [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) for Python, focusing specifically on **CloudFormation template synthesis** (not deployment or other CDK features).

## Overview

Both libraries generate CloudFormation templates from Python code, but CDK is a full infrastructure-as-code framework while cloudformation_dataclasses focuses purely on template synthesis.

| Aspect | cloudformation_dataclasses | AWS CDK (Python) |
|--------|---------------------------|------------------|
| **Paradigm** | Declarative (wrapper dataclasses) | Imperative (construct tree) |
| **Runtime** | Pure Python (stdlib only) | Node.js required |
| **Dependencies** | Zero | aws-cdk-lib + constructs + Node.js |
| **Output** | CloudFormation JSON/YAML | CloudFormation + CDK metadata |
| **Scope** | Template synthesis only | Full lifecycle (synth, deploy, destroy) |

## Key Advantages

### 1. Truly Declarative Syntax

cloudformation_dataclasses uses a **declarative** pattern where infrastructure is defined as data, not code. Each resource is a simple class with fields - no constructors, no method calls, no execution order to worry about:

```python
@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name = "data"
    versioning_configuration = MyVersioning  # Just reference another class
    tags = [EnvironmentTag, ProjectTag]      # List of tag classes
```

CDK uses an **imperative** pattern where you execute code to build a construct tree. Order matters, state is mutable, and you're programming rather than configuring:

```python
class MyStack(Stack):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Imperative: execute code in order to build tree
        bucket = s3.Bucket(self, "MyBucket", bucket_name="data")
        bucket.add_lifecycle_rule(...)  # Mutate after creation

        if some_condition:
            bucket.grant_read(some_role)  # Conditional logic embedded in code
```

**Why declarative matters:**
- **Easier to read**: Infrastructure is data, not behavior
- **Easier to generate**: AI assistants can produce declarative configs more reliably
- **Easier to diff**: Changes are visible as field differences, not code flow changes
- **No hidden state**: What you see is what you get

### 2. Pure Python, No Node.js Required

cloudformation_dataclasses is **pure Python** - no Node.js, no JavaScript runtime, no cross-language bindings:

```bash
# Generated package structure
my_stack/
├── __init__.py      # All library imports centralized
├── main.py          # build_template() entry point
└── stack/
    ├── storage.py   # S3 resources
    ├── compute.py   # Lambda resources
    └── ...

# Just Python - no Node.js needed
pip install cloudformation_dataclasses
python -m my_stack > template.json
```

CDK requires **Node.js installed system-wide** in addition to Python:

```bash
# CDK synthesis requires Node.js runtime
$ cdk synth
# Internally runs: node /path/to/cdk/cli.js synth

# CI/CD pipelines need both Python AND Node.js
# Docker images need both runtimes
# Local development needs both installed
```

| Library | Runtime Requirements | Install Size |
|---------|---------------------|--------------|
| cloudformation_dataclasses | Python 3.10+ only | ~15 MB |
| AWS CDK | Python + Node.js 18+ | ~500 MB+ |

**Why pure Python matters:**
- **Simpler CI/CD**: No Node.js setup in pipelines
- **Smaller containers**: Python-only Docker images
- **Faster installs**: No npm/node_modules
- **Fewer breakages**: No Node.js version conflicts
- **Native Python**: No jsii translation layer

### 3. Simplified Imports & Flexible File Organization

cloudformation_dataclasses uses a **single import pattern** that provides everything you need. Resources can reference each other across files without explicit imports:

```python
# stack/storage.py
from .. import *  # Gets ALL library imports AND resource classes

@cloudformation_dataclass
class DataBucket:
    resource: Bucket
    bucket_name = "data"

# stack/compute.py
from .. import *  # Same simple import

@cloudformation_dataclass
class MyFunction:
    resource: Function
    # Reference DataBucket from storage.py - no import needed!
    environment = {"BUCKET": ref(DataBucket)}

# stack/security.py
from .. import *

@cloudformation_dataclass
class BucketPolicy:
    resource: BucketPolicy
    # Reference both - still no imports!
    bucket = ref(DataBucket)
```

**Move a resource between files? Zero import changes required.**

CDK requires **explicit imports and constructor wiring** between modules:

```python
# constructs/storage.py
from aws_cdk import aws_s3 as s3
from constructs import Construct

class StorageConstruct(Construct):
    def __init__(self, scope, id):
        super().__init__(scope, id)
        self.bucket = s3.Bucket(self, "DataBucket")

# constructs/compute.py
from aws_cdk import aws_lambda as lambda_
from constructs import Construct
from .storage import StorageConstruct  # Must import explicitly

class ComputeConstruct(Construct):
    def __init__(self, scope, id, storage: StorageConstruct):  # Must accept as param
        super().__init__(scope, id)
        fn = lambda_.Function(
            self, "MyFunction",
            environment={"BUCKET": storage.bucket.bucket_name}  # Must wire through
        )

# app.py - Must wire everything together
storage = StorageConstruct(stack, "Storage")
compute = ComputeConstruct(stack, "Compute", storage=storage)  # Must pass explicitly
```

**Move a resource in CDK? Update imports, constructor signatures, and wiring throughout.**

**Why simplified imports matter:**
- **Refactor freely**: Move resources between files without cascading changes
- **AI-friendly**: Agents can work on one file at a time
- **Less boilerplate**: One import line per file
- **No circular import headaches**: The registry handles resolution

### 4. Clean, Readable Output

cloudformation_dataclasses produces **minimal CloudFormation** - just your resources:

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyBucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": { "BucketName": "data" }
    }
  }
}
```

CDK adds **metadata, parameters, and hashed logical IDs**:

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyBucketF68F3FF0": {
      "Type": "AWS::S3::Bucket",
      "Properties": { "BucketName": "data" },
      "Metadata": {
        "aws:cdk:path": "MyStack/MyBucket/Resource"
      }
    }
  },
  "Rules": { "CheckBootstrapVersion": { ... } },
  "Parameters": { "BootstrapVersion": { ... } }
}
```

| Library | Logical ID |
|---------|-----------|
| cloudformation_dataclasses | Class name (`MyBucket`) |
| CDK | Construct ID + hash (`MyBucketF68F3FF0`) |

**Why clean output matters:**
- **Readable templates**: Logical IDs match your code
- **Easy debugging**: Find resources in AWS console by class name
- **Version control friendly**: Smaller diffs, clearer changes
- **GitOps ready**: Templates are the source of truth, not CDK state

### 5. Type-Safe Resource References

cloudformation_dataclasses uses **class references** that your IDE understands:

```python
@cloudformation_dataclass
class MyRole:
    resource: Role
    assume_role_policy_document = LambdaAssumeRolePolicy

@cloudformation_dataclass
class MyFunction:
    resource: Function
    role = get_att(MyRole, "Arn")  # IDE knows MyRole exists, autocompletes
```

CDK references work at runtime but **jsii wrappers limit IDE support**:

```python
# CDK's Python bindings are auto-generated from TypeScript
# Type hints exist but IDE support is inconsistent
fn = lambda_.Function(
    self, "MyFunction",
    role=role,  # Works, but autocomplete varies by IDE
)
```

## Code Comparison

### Creating an S3 Bucket with Encryption

**cloudformation_dataclasses:**
```python
from cloudformation_dataclasses import cloudformation_dataclass, Template
from cloudformation_dataclasses.aws.s3 import (
    Bucket, ServerSideEncryptionByDefault, ServerSideEncryption
)

@cloudformation_dataclass
class MyEncryption:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256

@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name: str = "my-app-data"
    bucket_encryption = MyEncryption

template = Template.from_registry(description="My Stack")
print(template.to_json())
```

**AWS CDK:**
```python
from aws_cdk import App, Stack
from aws_cdk import aws_s3 as s3
from constructs import Construct

class MyStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(
            self, "MyBucket",
            bucket_name="my-app-data",
            encryption=s3.BucketEncryption.S3_MANAGED,
        )

app = App()
MyStack(app, "MyStack")
app.synth()  # Requires Node.js runtime
```

### Lambda with IAM Role

**cloudformation_dataclasses:**
```python
@cloudformation_dataclass
class MyRole:
    resource: Role
    assume_role_policy_document = LambdaAssumeRolePolicy
    managed_policy_arns = [
        "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
    ]

@cloudformation_dataclass
class MyFunction:
    resource: Function
    function_name: str = "my-handler"
    runtime = Runtime.PYTHON3_12
    handler: str = "index.handler"
    role = get_att(MyRole, "Arn")
    code = MyCode
```

**AWS CDK:**
```python
from aws_cdk import aws_lambda as lambda_

class MyStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # CDK creates the role automatically with correct permissions
        fn = lambda_.Function(
            self, "MyFunction",
            function_name="my-handler",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="index.handler",
            code=lambda_.Code.from_asset("lambda"),
        )
```

## Feature Comparison

| Feature | cloudformation_dataclasses | AWS CDK |
|---------|---------------------------|---------|
| Template synthesis | Yes | Yes |
| Deploy/destroy | No (use AWS CLI/SAM) | Yes (`cdk deploy`) |
| Asset bundling | No | Yes (Lambda zips, Docker) |
| Cross-stack refs | Manual | Automatic |
| Drift detection | No | Yes (via metadata) |
| L2/L3 constructs | No (1:1 mapping) | Yes (high-level abstractions) |
| Type checking | Full Python type hints | Partial (jsii limitations) |
| IDE support | Native Python | Limited (jsii wrappers) |
| File reorganization | Trivial (no import changes) | Requires import/signature updates |
| Runtime requirements | Python only | Python + Node.js |
| Output readability | Clean, minimal | Verbose with metadata |

## When to Use Each

### Use cloudformation_dataclasses when:

- You want **pure Python** without Node.js dependency
- You prefer **declarative** configuration over imperative code
- You want **1:1 CloudFormation mapping** with full control
- You're generating templates for **CI/CD pipelines** or **GitOps**
- You want **clean, readable** CloudFormation output
- You want to **reorganize resources** between files without updating imports
- You're working with **AI assistants** (declarative syntax is easier to generate)

### Use AWS CDK when:

- You want **high-level abstractions** (L2/L3 constructs)
- You need **asset bundling** (Lambda code, Docker images)
- You want **integrated deployment** (`cdk deploy`)
- You prefer **imperative** programming with conditionals and loops
- You're already using **CDK in TypeScript/Java** and want consistency
- You need **cross-stack references** managed automatically

## Migration

### From CDK to cloudformation_dataclasses

1. **Synthesize the CDK template**:
   ```bash
   cdk synth > template.yaml
   ```

2. **Import into cloudformation_dataclasses**:
   ```bash
   cfn-dataclasses import template.yaml -o my_stack/
   ```

3. **Clean up**: Remove CDK metadata, simplify logical IDs

4. **Remove Node.js dependency**: The generated Python package needs only Python

### From cloudformation_dataclasses to CDK

1. **Generate CloudFormation**: `python -m my_stack > template.json`
2. Use `CfnInclude` to import into CDK (not recommended - loses CDK benefits)
3. Or manually port to CDK constructs

## See Also

- [AWS CDK Python Reference](https://docs.aws.amazon.com/cdk/api/v2/python/)
- [CDK vs CloudFormation](https://docs.aws.amazon.com/cdk/v2/guide/cfn_layer.html)
- [cloudformation_dataclasses Quick Start](../QUICK_START.md)
- [Troposphere Comparison](./TROPOSPHERE.md)
