# Feature Comparison Matrix

A comprehensive feature comparison between cloudformation_dataclasses, AWS CDK (Python), and Troposphere.

## Quick Summary

| Category | cloudformation_dataclasses | AWS CDK | Troposphere |
|----------|---------------------------|---------|-------------|
| **Paradigm** | Declarative | Imperative | Imperative |
| **Runtime** | Python only | Python + Node.js | Python |
| **Dependencies** | None (stdlib) | 500MB+ | cfn-flip |
| **Learning curve** | Low | High | Medium |

---

## Syntax & Design

| Feature | cloudformation_dataclasses | AWS CDK | Troposphere |
|---------|:--------------------------:|:-------:|:-----------:|
| **Declarative syntax** | ✅ | ❌ | ❌ |
| Infrastructure defined as data, not code | ✅ | ❌ | ❌ |
| No constructor calls needed | ✅ | ❌ | ❌ |
| No execution order dependencies | ✅ | ❌ | ❌ |
| Flat nested property structure | ✅ | ❌ | ❌ |
| Class-based resource references | ✅ | ✅ | ❌ (strings) |
| Type-safe refs (catch typos in IDE) | ✅ | ⚠️ | ❌ |
| Auto-generated logical IDs | ✅ | ✅ | ❌ |
| Readable logical IDs (no hashes) | ✅ | ❌ | ✅ |

### Why Declarative Matters

```python
# cloudformation_dataclasses: Infrastructure as DATA
@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name = "data"
    versioning = MyVersioning  # Just a reference

# CDK/Troposphere: Infrastructure as CODE
bucket = Bucket(self, "MyBucket", bucket_name="data")
bucket.add_versioning(...)  # Execute methods
template.add_resource(bucket)  # Don't forget this!
```

---

## File Organization & Imports

| Feature | cloudformation_dataclasses | AWS CDK | Troposphere |
|---------|:--------------------------:|:-------:|:-----------:|
| **Single import pattern** | ✅ | ❌ | ❌ |
| Cross-file refs without imports | ✅ | ❌ | ❌ |
| Move resources without import changes | ✅ | ❌ | ❌ |
| No circular import issues | ✅ | ❌ | ❌ |
| Service-based file organization | ✅ | ⚠️ | ❌ |
| Auto-discovery of resources | ✅ | ❌ | ❌ |

### Why Simplified Imports Matter

```python
# cloudformation_dataclasses: ONE import, reference anything
# stack/compute.py
from .. import *

@cloudformation_dataclass
class MyFunction:
    resource: Function
    bucket = ref(DataBucket)  # DataBucket is in storage.py - no import needed!

# CDK: Explicit imports + constructor wiring
from .storage import StorageConstruct
class ComputeConstruct(Construct):
    def __init__(self, scope, id, storage: StorageConstruct):  # Must wire
        ...
```

**Move `DataBucket` from `storage.py` to `main.py`?**
- cloudformation_dataclasses: Zero changes
- CDK/Troposphere: Update imports in every file that references it

---

## Resource Management

| Feature | cloudformation_dataclasses | AWS CDK | Troposphere |
|---------|:--------------------------:|:-------:|:-----------:|
| **Automatic resource registration** | ✅ | ✅ | ❌ |
| No `add_resource()` calls needed | ✅ | ✅ | ❌ |
| No silent missing resources | ✅ | ✅ | ❌ |
| Template.from_registry() | ✅ | ❌ | ❌ |
| Context-based resource naming | ✅ | ⚠️ | ❌ |
| Blue/green deployment naming | ✅ | ❌ | ❌ |
| Automatic tag inheritance | ✅ | ⚠️ | ❌ |

### Why Auto-Registration Matters

```python
# cloudformation_dataclasses: Define it, it's registered
@cloudformation_dataclass
class MyBucket:
    resource: Bucket

template = Template.from_registry()  # Collects all resources

# Troposphere: Must remember to register
bucket = Bucket("MyBucket", ...)
template.add_resource(bucket)  # Forget this = silent bug
```

---

## Runtime & Dependencies

| Feature | cloudformation_dataclasses | AWS CDK | Troposphere |
|---------|:--------------------------:|:-------:|:-----------:|
| **Pure Python (no other runtime)** | ✅ | ❌ | ✅ |
| No Node.js required | ✅ | ❌ | ✅ |
| No transitive dependencies | ✅ | ❌ | ❌ |
| Small install size (~15MB) | ✅ | ❌ | ⚠️ |
| Fast pip install | ✅ | ❌ | ✅ |
| Python-only Docker images | ✅ | ❌ | ✅ |
| Simple CI/CD setup | ✅ | ❌ | ✅ |

### Install Size Comparison

| Library | Size | Node.js Required |
|---------|------|------------------|
| cloudformation_dataclasses | ~15 MB | No |
| Troposphere | ~50 MB | No |
| AWS CDK | ~500 MB+ | Yes (18+) |

---

## CloudFormation Output

| Feature | cloudformation_dataclasses | AWS CDK | Troposphere |
|---------|:--------------------------:|:-------:|:-----------:|
| **Clean, minimal output** | ✅ | ❌ | ✅ |
| No CDK metadata in templates | ✅ | ❌ | ✅ |
| No bootstrap parameters | ✅ | ❌ | ✅ |
| Readable logical IDs | ✅ | ❌ | ✅ |
| 1:1 CloudFormation mapping | ✅ | ❌ | ✅ |
| GitOps-friendly templates | ✅ | ❌ | ✅ |
| Predictable resource names | ✅ | ❌ | ✅ |

### Output Comparison

**cloudformation_dataclasses:**
```json
{
  "Resources": {
    "MyBucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": { "BucketName": "data" }
    }
  }
}
```

**AWS CDK:**
```json
{
  "Resources": {
    "MyBucketF68F3FF0": {
      "Type": "AWS::S3::Bucket",
      "Properties": { "BucketName": "data" },
      "Metadata": { "aws:cdk:path": "Stack/MyBucket/Resource" }
    }
  },
  "Parameters": { "BootstrapVersion": { ... } },
  "Rules": { "CheckBootstrapVersion": { ... } }
}
```

---

## Type Safety & IDE Support

| Feature | cloudformation_dataclasses | AWS CDK | Troposphere |
|---------|:--------------------------:|:-------:|:-----------:|
| **Type hints on resource classes** | ✅ | ⚠️ | ✅ |
| IDE autocomplete for properties | ✅ | ⚠️ | ✅ |
| **Type-safe cross-resource refs** | ✅ | ✅ | ❌ |
| Go-to-definition for refs | ✅ | ⚠️ | ❌ |
| Catch ref typos at edit time | ✅ | ⚠️ | ❌ |
| mypy/pyright support | ✅ | ⚠️ | ✅ |
| No jsii wrapper limitations | ✅ | ❌ | ✅ |
| Refactor-safe references | ✅ | ⚠️ | ❌ |

### The Key Difference: Cross-Resource References

Troposphere has good IDE support for resource classes and properties. The limitation is **string-based references** between resources:

```python
# cloudformation_dataclasses: Class reference - IDE validates
role = get_att(MyRol, "Arn")  # ❌ IDE error: "MyRol" undefined
role = get_att(MyRole, "Arn")  # ✅ IDE knows MyRole exists

# Troposphere: String reference - no IDE validation
Role=GetAtt("MyRol", "Arn")  # ⚠️ No error - typo caught at deploy time
Role=GetAtt("MyRole", "Arn")  # Works, but IDE can't verify "MyRole" exists
```

Rename `MyRole` to `ExecutionRole`?
- cloudformation_dataclasses: IDE shows all references, refactor updates them
- Troposphere: Must manually find/replace all `"MyRole"` strings

---

## Template Import

| Feature | cloudformation_dataclasses | AWS CDK | Troposphere |
|---------|:--------------------------:|:-------:|:-----------:|
| **Import existing templates** | ✅ | ⚠️ | ❌ |
| YAML/JSON to Python conversion | ✅ | ❌ | ❌ |
| Batch import (directories) | ✅ | ❌ | ❌ |
| Auto-detect implicit refs | ✅ | ❌ | ❌ |
| Generate typed wrapper classes | ✅ | ❌ | ❌ |
| Preserve template structure | ✅ | ❌ | ❌ |

### Import Command

```bash
# Import a single template
cfn-dataclasses-import template.yaml -o my_stack/

# Batch import a directory of templates
cfn-dataclasses-import templates/ -o output/

# CDK has CfnInclude but it's runtime, not code generation
# Troposphere has no import capability
```

---

## AI/LLM Friendliness

| Feature | cloudformation_dataclasses | AWS CDK | Troposphere |
|---------|:--------------------------:|:-------:|:-----------:|
| **Declarative = easier to generate** | ✅ | ❌ | ❌ |
| Simple class structure | ✅ | ❌ | ⚠️ |
| No method call sequences | ✅ | ❌ | ❌ |
| Predictable patterns | ✅ | ⚠️ | ⚠️ |
| Single import line per file | ✅ | ❌ | ❌ |
| No wiring/registration logic | ✅ | ❌ | ❌ |
| Service-based file splitting | ✅ | ⚠️ | ❌ |

### Why AI Agents Prefer Declarative

AI assistants generate more reliable code with declarative syntax because:
- **No state**: Each class is self-contained
- **No order**: Resources can be defined in any order
- **No wiring**: References are just class names
- **Predictable**: Same pattern for every resource type

---

## Deployment Context

| Feature | cloudformation_dataclasses | AWS CDK | Troposphere |
|---------|:--------------------------:|:-------:|:-----------:|
| **Built-in DeploymentContext** | ✅ | ⚠️ | ❌ |
| Auto-generate resource names | ✅ | ⚠️ | ❌ |
| Environment-based naming | ✅ | ⚠️ | ❌ |
| Blue/green deployment groups | ✅ | ❌ | ❌ |
| Region in resource names | ✅ | ⚠️ | ❌ |
| Project/component hierarchy | ✅ | ⚠️ | ❌ |
| Automatic tag propagation | ✅ | ⚠️ | ❌ |

### DeploymentContext Example

```python
@cloudformation_dataclass
class MyContext:
    context: DeploymentContext
    project_name = "myapp"
    component = "api"
    stage = "prod"
    deployment_group = "blue"
    region = "us-east-1"

@cloudformation_dataclass
class DataBucket:
    resource: Bucket
    context = ctx
    # Auto-names to: myapp-api-DataBucket-prod-blue-us-east-1
    # Auto-tags with project, component, stage, etc.
```

---

## What CDK Does Better

To be fair, CDK excels in areas cloudformation_dataclasses doesn't cover:

| Feature | cloudformation_dataclasses | AWS CDK |
|---------|:--------------------------:|:-------:|
| L2/L3 high-level constructs | ❌ | ✅ |
| Asset bundling (Lambda zips) | ❌ | ✅ |
| Docker image building | ❌ | ✅ |
| Integrated deployment | ❌ | ✅ |
| Cross-stack references | ❌ | ✅ |
| Drift detection | ❌ | ✅ |

**Use CDK when you need:**
- High-level abstractions that generate multiple resources
- Built-in asset bundling for Lambda/Docker
- `cdk deploy` integration

**Use cloudformation_dataclasses when you need:**
- Pure Python, no Node.js
- Declarative, AI-friendly syntax
- Clean CloudFormation output
- Flexible file organization
- GitOps workflows

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Full support |
| ⚠️ | Partial/limited support |
| ❌ | Not supported |

---

## See Also

- [CDK Comparison](./CDK.md) - Detailed comparison with AWS CDK
- [Troposphere Comparison](./TROPOSPHERE.md) - Detailed comparison with Troposphere
- [Quick Start](../QUICK_START.md) - Get started with cloudformation_dataclasses
- [Importer Guide](../IMPORTER.md) - Import existing CloudFormation templates
