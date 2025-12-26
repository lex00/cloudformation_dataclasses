# Comparison

A comparison of CloudFormation authoring approaches for teams evaluating their IaC tooling options.

## Who This Comparison Is For

Teams heavily invested in AWS who are at a crossroads with their infrastructure tooling. Common pain points:

- **Terraform**: State management overhead, team coordination around state locks, drift handling
- **CDK**: Node.js dependency, verbose generated templates, abstraction complexity
- **Raw CloudFormation**: Hostile authoring experience, no type safety, error-prone references
- **Corporate/opaque tooling**: Internal platforms that hide too much, vendor lock-in, "magic" that breaks

If you're happy with your current tooling, you probably don't need this library.

---

## Quick Summary

| Category | cloudformation_dataclasses | AWS CDK | Terraform |
|----------|---------------------------|---------|-----------|
| **Paradigm** | Declarative (Python) | Imperative (Python + Node.js) | Declarative (HCL) |
| **State management** | None (CloudFormation handles it) | Via CDK toolkit | Required (remote backend) |
| **Runtime** | Python only | Python + Node.js | Go binary |
| **Dependencies** | pyyaml only | 500MB+ | Terraform CLI + providers |
| **Learning curve** | Low | High | Medium |
| **Multi-cloud** | AWS only | AWS (primarily) | Multi-cloud |

---

## Syntax & Authoring

| Feature | cloudformation_dataclasses | AWS CDK | Terraform |
|---------|:--------------------------:|:-------:|:---------:|
| **Declarative syntax** | ✅ | ❌ | ✅ |
| Infrastructure defined as data | ✅ | ❌ | ✅ |
| No constructor/method calls | ✅ | ❌ | ✅ |
| No execution order dependencies | ✅ | ❌ | ✅ |
| Type-safe resource references | ✅ | ✅ | ❌ (strings) |
| IDE autocomplete | ✅ | ⚠️ | ⚠️ |
| Catch ref typos at edit time | ✅ | ⚠️ | ❌ |

### Syntax Comparison

```python
# cloudformation_dataclasses: Infrastructure as DATA
@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name = "data"
    versioning = MyVersioning  # Just a reference
```

```python
# CDK: Imperative construct tree
bucket = s3.Bucket(self, "MyBucket", bucket_name="data")
bucket.add_lifecycle_rule(...)  # Mutate after creation
```

```hcl
# Terraform: Declarative HCL
resource "aws_s3_bucket" "my_bucket" {
  bucket = "data"
}
```

Both cloudformation_dataclasses and Terraform are declarative. The difference: cloudformation_dataclasses uses Python with type hints; Terraform uses HCL with state management.

---

## State Management

| Aspect | cloudformation_dataclasses | AWS CDK | Terraform |
|--------|:--------------------------:|:-------:|:---------:|
| **State file required** | ❌ | ❌ | ✅ |
| State locking concerns | N/A | N/A | Yes |
| Remote backend setup | N/A | N/A | Required for teams |
| Drift detection | Via CloudFormation | Via CDK | Via `terraform plan` |
| State contains secrets | N/A | N/A | Yes (plaintext) |

### The State Management Trade-off

Terraform's state file provides powerful features (resource tracking, drift detection, dependency graph). It also introduces operational overhead:

- **State locking**: Teams must coordinate who can run `terraform apply`
- **Remote backend**: S3 + DynamoDB (or similar) required for team use
- **Secrets exposure**: State files contain sensitive values in plaintext
- **State drift**: Discrepancies between state and reality require manual resolution

cloudformation_dataclasses delegates state entirely to CloudFormation. You author templates; CloudFormation tracks what's deployed. This is simpler but means you're tied to CloudFormation's capabilities.

---

## Runtime & Dependencies

| Feature | cloudformation_dataclasses | AWS CDK | Terraform |
|---------|:--------------------------:|:-------:|:---------:|
| **Pure Python** | ✅ | ❌ | N/A |
| No Node.js required | ✅ | ❌ | ✅ |
| No transitive dependencies | ✅ | ❌ | ✅ |
| Small install size | ✅ (~15MB) | ❌ (~500MB+) | ⚠️ (~100MB+) |
| Python-only Docker images | ✅ | ❌ | N/A |

---

## CloudFormation Output

| Feature | cloudformation_dataclasses | AWS CDK |
|---------|:--------------------------:|:-------:|
| **Clean, minimal output** | ✅ | ❌ |
| No metadata in templates | ✅ | ❌ |
| Readable logical IDs | ✅ | ❌ (hashed) |
| 1:1 CloudFormation mapping | ✅ | ❌ |
| GitOps-friendly templates | ✅ | ⚠️ |

*Terraform generates its own plan format, not CloudFormation templates.*

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

## File Organization

| Feature | cloudformation_dataclasses | AWS CDK | Terraform |
|---------|:--------------------------:|:-------:|:---------:|
| **Single import pattern** | ✅ | ❌ | N/A |
| Cross-file refs without imports | ✅ | ❌ | ✅ |
| Move resources without cascading changes | ✅ | ❌ | ✅ |
| No circular import issues | ✅ | ❌ | ✅ |
| Auto-discovery of resources | ✅ | ❌ | ✅ |

### Why This Matters

```python
# cloudformation_dataclasses: ONE import, reference anything
from . import *

@cloudformation_dataclass
class MyFunction:
    resource: Function
    bucket = ref(DataBucket)  # DataBucket is in another file - no import needed
```

Move `DataBucket` between files → **zero import changes**.

CDK requires explicit imports and constructor wiring. Moving a resource means updating imports throughout the codebase.

---

## Template Import

| Feature | cloudformation_dataclasses | AWS CDK | Terraform |
|---------|:--------------------------:|:-------:|:---------:|
| **Import existing CloudFormation** | ✅ | ⚠️ | ⚠️ |
| YAML/JSON to Python conversion | ✅ | ❌ | ❌ |
| Batch import (directories) | ✅ | ❌ | ❌ |
| Generate typed wrapper classes | ✅ | ❌ | ❌ |

```bash
# Import a single template
cfn-dataclasses import template.yaml -o my_stack/

# Batch import a directory
cfn-dataclasses import templates/ -o output/
```

---

## AI/Agent Friendliness

| Feature | cloudformation_dataclasses | AWS CDK | Terraform |
|---------|:--------------------------:|:-------:|:---------:|
| **Declarative = easier to generate** | ✅ | ❌ | ✅ |
| Simple class structure | ✅ | ❌ | ⚠️ |
| Type hints constrain output | ✅ | ⚠️ | ❌ |
| Predictable patterns | ✅ | ⚠️ | ✅ |
| No wiring/registration logic | ✅ | ❌ | ✅ |

AI assistants generate more reliable code with:
- **Declarative syntax**: No execution order to manage
- **Type hints**: Constraints that reduce the search space
- **Simple patterns**: Same structure for every resource

A Python dataclass with 5 typed fields is a better prompt than a 50-line YAML example.

---

## What Others Do Better

### CDK Strengths

| Feature | cloudformation_dataclasses | AWS CDK |
|---------|:--------------------------:|:-------:|
| L2/L3 high-level constructs | ❌ | ✅ |
| Asset bundling (Lambda zips) | ❌ | ✅ |
| Docker image building | ❌ | ✅ |
| Integrated deployment | ❌ | ✅ |
| Cross-stack references | ❌ | ✅ |

**Use CDK when you need**: High-level abstractions, asset bundling, or `cdk deploy` integration.

### Terraform Strengths

| Feature | cloudformation_dataclasses | Terraform |
|---------|:--------------------------:|:---------:|
| Multi-cloud support | ❌ | ✅ |
| Provider ecosystem | AWS only | Extensive |
| `terraform plan` preview | ❌ | ✅ |
| Import existing resources | ❌ | ✅ |

**Use Terraform when you need**: Multi-cloud infrastructure or non-AWS resources.

---

## Code Examples

### S3 Bucket with Encryption

**cloudformation_dataclasses:**
```python
@cloudformation_dataclass
class MyEncryption:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256

@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name = "my-app-data"
    bucket_encryption = MyEncryption
```

**AWS CDK:**
```python
bucket = s3.Bucket(
    self, "MyBucket",
    bucket_name="my-app-data",
    encryption=s3.BucketEncryption.S3_MANAGED,
)
```

CDK is more concise here—the L2 construct handles encryption configuration.

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
    function_name = "my-handler"
    runtime = Runtime.PYTHON3_12
    handler = "index.handler"
    role = get_att(MyRole, "Arn")
```

**AWS CDK:**
```python
# CDK creates the role automatically
fn = lambda_.Function(
    self, "MyFunction",
    function_name="my-handler",
    runtime=lambda_.Runtime.PYTHON_3_12,
    handler="index.handler",
    code=lambda_.Code.from_asset("lambda"),  # Plus bundling
)
```

CDK is more concise and handles asset bundling. cloudformation_dataclasses is more explicit about what's created.

---

## When to Use cloudformation_dataclasses

- **AWS-only** infrastructure with no multi-cloud requirements
- Teams who want **no state management overhead**
- **Pure Python** environment (no Node.js)
- **Clean, readable** CloudFormation output
- **AI-assisted** infrastructure authoring
- **GitOps workflows** where templates are the source of truth

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Full support |
| ⚠️ | Partial/limited support |
| ❌ | Not supported |
| N/A | Not applicable |

---

## Notes

**Troposphere**: Another Python library for CloudFormation. Uses imperative syntax with string-based references. If you're considering Troposphere, cloudformation_dataclasses offers similar capabilities with type-safe references and declarative syntax.

---

## See Also

- [Quick Start](QUICK_START.md) - Get started with cloudformation_dataclasses
- [CLI Reference](CLI.md) - Import existing CloudFormation templates
