# Deployment Context

The `DeploymentContext` provides automatic resource naming and tag management across your CloudFormation templates.

## Overview

Context solves two common problems in infrastructure-as-code:

1. **Consistent naming**: Resources need predictable names that include environment, region, and other deployment metadata
2. **Tag management**: Base tags (environment, project, cost center) need to be applied to all resources

Instead of manually setting names and tags on every resource, define them once in a context and apply at template level.

## Quick Example

```python
from cloudformation_dataclasses.core import (
    cloudformation_dataclass,
    DeploymentContext,
    Tag,
    Template,
)
from cloudformation_dataclasses.aws.s3 import Bucket

# Define base tags
@cloudformation_dataclass
class EnvironmentTag:
    resource: Tag
    key = "Environment"
    value = "Production"

# Define deployment context
@cloudformation_dataclass
class ProdContext:
    context: DeploymentContext
    project_name = "myapp"
    component = "storage"
    stage = "prod"
    region = "us-east-1"
    tags = [EnvironmentTag]

ctx = ProdContext()

# Define resources without explicit names
@cloudformation_dataclass
class DataBucket:
    resource: Bucket
    # bucket_name is auto-populated from context

# Build template with context
template = Template.from_registry(
    description="My Infrastructure",
    context=ctx,  # Injects context into all resources
)
```

The bucket automatically gets:
- **Name**: `myapp-storage-DataBucket-prod-us-east-1`
- **Tags**: `[{Key: "Environment", Value: "Production"}]`

## Template-Level Context

Context is applied at the template level via `Template.from_registry()`:

```python
template = Template.from_registry(
    description="My Application Stack",
    context=ctx,  # Applied to all resources
)
```

This automatically:
- Injects the context into all resources that don't already have one
- Sets physical names (e.g., `bucket_name`, `function_name`) using the naming pattern
- Merges context tags with resource-specific tags

Resources define configuration, not deployment metadata:

```python
@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    # No bucket_name - auto-populated from context
    # No context assignment - injected by template

@cloudformation_dataclass
class MyFunction:
    resource: Function
    runtime = "python3.12"
    handler = "index.handler"
    # No function_name - auto-populated from context
```

## DeploymentContext Fields

| Field | Description | Used in Naming |
|-------|-------------|----------------|
| `project_name` | Top-level project/organization name | Yes |
| `component` | Logical grouping within your project | Yes |
| `stage` | Deployment stage (dev, staging, prod) | Yes |
| `deployment_name` | Deployment identifier (e.g., "001", "v2") | Yes |
| `deployment_group` | Blue/green deployment group | Yes |
| `region` | AWS region | Yes |
| `naming_pattern` | Custom naming pattern (optional) | N/A |
| `tags` | Base tags applied to all resources | N/A |

## Naming Pattern

### Default Pattern

```
{project_name}-{component}-{resource_name}-{stage}-{deployment_name}-{deployment_group}-{region}
```

**Example**: `analytics-storage-DataBucket-prod-001-blue-us-west-2`

Empty fields are automatically removed (no double dashes).

### Custom Pattern

Override the default pattern:

```python
@cloudformation_dataclass
class MyContext:
    context: DeploymentContext
    project_name = "myapp"
    component = "api"
    stage = "prod"
    region = "us-east-1"

    # Shorter pattern
    naming_pattern = "{project_name}-{component}-{resource_name}-{stage}"
```

This produces: `myapp-api-DataBucket-prod`

### Auto-Named Resources

The following resource types support automatic naming:

| Resource Type | Name Field |
|--------------|------------|
| `AWS::S3::Bucket` | `bucket_name` |
| `AWS::Lambda::Function` | `function_name` |
| `AWS::DynamoDB::Table` | `table_name` |
| `AWS::SQS::Queue` | `queue_name` |
| `AWS::SNS::Topic` | `topic_name` |
| `AWS::EC2::SecurityGroup` | `group_name` |
| `AWS::IAM::Role` | `role_name` |
| `AWS::StepFunctions::StateMachine` | `state_machine_name` |
| ... | (994 resources support auto-naming) |

Resources without a name field (like EC2 instances, VPCs) use CloudFormation-generated IDs but can still receive tags.

## Tag Management

### Context Tags

Define base tags that apply to all resources:

```python
@cloudformation_dataclass
class EnvironmentTag:
    resource: Tag
    key = "Environment"
    value = "Production"

@cloudformation_dataclass
class CostCenterTag:
    resource: Tag
    key = "CostCenter"
    value = "Engineering"

@cloudformation_dataclass
class ProdContext:
    context: DeploymentContext
    project_name = "myapp"
    stage = "prod"
    tags = [EnvironmentTag, CostCenterTag]
```

### Tag Merging

Resource-specific tags merge with context tags:

```python
@cloudformation_dataclass
class DataClassificationTag:
    resource: Tag
    key = "DataClassification"
    value = "Sensitive"

@cloudformation_dataclass
class DataBucket:
    resource: Bucket
    tags = [DataClassificationTag]  # Resource-specific tag
```

When rendered, the bucket has all tags:
```json
{
  "Tags": [
    {"Key": "Environment", "Value": "Production"},
    {"Key": "CostCenter", "Value": "Engineering"},
    {"Key": "DataClassification", "Value": "Sensitive"}
  ]
}
```

### Tag Priority

If both context and resource define the same tag key, the resource-specific tag wins.

## Multiple Environments

### Override at Instantiation

```python
@cloudformation_dataclass
class AppContext:
    context: DeploymentContext
    project_name = "myapp"
    component = "api"
    stage = "dev"  # Default
    region = "us-east-1"

# Create different environments
ctx_dev = AppContext()
ctx_staging = AppContext(stage="staging")
ctx_prod = AppContext(stage="prod", region="us-west-2")
```

### Blue/Green Deployments

Use `deployment_group` for zero-downtime deployments:

```python
ctx_blue = AppContext(deployment_group="blue")
ctx_green = AppContext(deployment_group="green")

# Resources get different names:
# myapp-api-DataBucket-prod-001-blue-us-east-1
# myapp-api-DataBucket-prod-001-green-us-east-1
```

### Environment-Specific Tags

```python
@cloudformation_dataclass
class DevEnvironmentTag:
    resource: Tag
    key = "Environment"
    value = "Development"

@cloudformation_dataclass
class ProdEnvironmentTag:
    resource: Tag
    key = "Environment"
    value = "Production"

@cloudformation_dataclass
class DevContext:
    context: DeploymentContext
    stage = "dev"
    tags = [DevEnvironmentTag]

@cloudformation_dataclass
class ProdContext:
    context: DeploymentContext
    stage = "prod"
    tags = [ProdEnvironmentTag]
```

## Per-Resource Context Override

While template-level context is recommended, you can override for specific resources:

```python
@cloudformation_dataclass
class SpecialBucket:
    resource: Bucket
    context = special_ctx  # Uses different context
```

Resources with an explicit context are not overwritten by `Template.from_registry(context=...)`.

## Project Structure

A typical project using context:

```
my_project/
├── __init__.py
├── context.py          # DeploymentContext definition
├── main.py             # Template.from_registry(context=ctx)
└── resources/
    ├── __init__.py
    ├── bucket.py       # S3 buckets
    ├── tables.py       # DynamoDB tables
    └── functions.py    # Lambda functions
```

### context.py

```python
from cloudformation_dataclasses.core import (
    cloudformation_dataclass,
    DeploymentContext,
    Tag,
)

@cloudformation_dataclass
class EnvironmentTag:
    resource: Tag
    key = "Environment"
    value = "Production"

@cloudformation_dataclass
class ProjectTag:
    resource: Tag
    key = "Project"
    value = "MyApplication"

@cloudformation_dataclass
class ProdContext:
    context: DeploymentContext
    project_name = "analytics"
    component = "DataPlatform"
    stage = "prod"
    deployment_name = "001"
    deployment_group = "blue"
    region = "us-east-1"
    tags = [EnvironmentTag, ProjectTag]

ctx = ProdContext()
```

### main.py

```python
from .context import ctx
from cloudformation_dataclasses.core import Template

# Import resources to trigger registration
from . import resources  # noqa: F401

def build_template() -> Template:
    return Template.from_registry(
        description="My Infrastructure",
        context=ctx,
    )

if __name__ == "__main__":
    import json
    print(json.dumps(build_template().to_dict(), indent=2))
```

### resources/bucket.py

```python
from cloudformation_dataclasses.core import cloudformation_dataclass
from cloudformation_dataclasses.aws.s3 import Bucket

@cloudformation_dataclass
class DataBucket:
    resource: Bucket
    # Auto-named: analytics-DataPlatform-DataBucket-prod-001-blue-us-east-1
```

## Complete Example

See the [with_context/s3_bucket](../examples/with_context/s3_bucket/) example for a complete working project demonstrating:

- Context definition with tags
- Multiple resources using template-level context
- Resource-specific tags merged with context tags
- Template generation

Run the example:

```bash
cd examples/with_context/s3_bucket
python -m s3_bucket.main
```

## See Also

- [Quick Start](QUICK_START.md) - Getting started guide
- [Registry](REGISTRY.md) - Auto-registration and `Template.from_registry()`
