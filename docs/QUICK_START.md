# Quick Start

Get started with `cloudformation_dataclasses` in 5 minutes.

## Installation

```bash
pip install cloudformation_dataclasses
```

## Create a New Project

Use the skeleton generator to create a new project with best practices:

```bash
cfn-init default -o my_project/
```

This creates a complete project structure:

```
my_project/
├── __init__.py        # Package exports
├── context.py         # Deployment context (naming, tags, environment)
├── main.py            # Template builder and entry point
├── pyproject.toml     # Package config with dependencies
├── py.typed           # PEP 561 typed package marker
├── mypy.ini           # mypy type checking config
├── CLAUDE.md          # Claude Code project guidance
├── .vscode/           # VSCode settings
│   └── settings.json
└── README.md          # Project documentation
```

## Customize Your Project

### 1. Configure the Deployment Context

Edit `my_project/context.py` to set your environment:

```python
@cloudformation_dataclass
class MyProjectContext:
    context: DeploymentContext
    project_name = "my_project"      # Top-level project name
    component = "MyComponent"        # Logical grouping
    stage = "dev"                    # dev, staging, prod
    deployment_name = "001"          # Deployment identifier
    deployment_group = "blue"        # For blue/green deployments
    region = "us-east-1"             # AWS region
    tags = [EnvironmentTag, ...]     # Base tags for all resources
```

Resources using this context automatically get:
- **Consistent naming**: Based on the naming pattern
- **Base tags**: Applied to all resources

### 2. Add Resources

Create a new file for each resource. For example, `my_project/bucket.py`:

```python
from . import *
from .context import ctx
from cloudformation_dataclasses.aws.s3 import Bucket

@cloudformation_dataclass
class DataBucket:
    resource: Bucket
    context = ctx
    bucket_name = "my-data-bucket"
```

Then import it in `my_project/main.py`:

```python
from .bucket import DataBucket

def build_template() -> Template:
    bucket = DataBucket()  # Creates and registers the resource
    return Template.from_registry()
```

### 3. Generate CloudFormation

```bash
python -m my_project.main
```

This outputs the CloudFormation JSON template to stdout.

### 4. Deploy

```bash
# Generate template file
python -m my_project.main > template.json

# Deploy with AWS CLI
aws cloudformation deploy \
    --template-file template.json \
    --stack-name my-project-dev
```

## CLI Options

Customize the skeleton with CLI flags:

```bash
cfn-init default -o my_project/ \
    --project-name analytics \
    --component storage \
    --stage prod \
    --region us-west-2
```

List available skeletons:

```bash
cfn-init --list
```

## DeploymentContext Reference

The `DeploymentContext` provides automatic resource naming and shared tags.

### Fields

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

### Default Naming Pattern

```
{project_name}-{component}-{resource_name}-{stage}-{deployment_name}-{deployment_group}-{region}
```

**Example**: `analytics-storage-DataBucket-prod-001-blue-us-west-2`

Empty fields are automatically removed from the generated name (no double dashes).

### Custom Naming Pattern

Override the default pattern in your context:

```python
@cloudformation_dataclass
class MyContext:
    context: DeploymentContext
    project_name = "myapp"
    component = "api"
    stage = "prod"
    region = "us-east-1"

    # Shorter pattern without deployment_name/group
    naming_pattern = "{project_name}-{component}-{resource_name}-{stage}"
```

This produces: `myapp-api-DataBucket-prod`

### Overriding Context Fields

Any field can be overridden when instantiating the context:

```python
# Define defaults in the class
@cloudformation_dataclass
class MyContext:
    context: DeploymentContext
    project_name = "myapp"
    component = "api"
    stage = "dev"
    region = "us-east-1"

# Override at instantiation
ctx_prod = MyContext(stage="prod", region="us-west-2")
ctx_staging = MyContext(stage="staging")
```

### Blue/Green Deployments

Use `deployment_group` for zero-downtime deployments:

```python
# Create two contexts with different deployment groups
ctx_blue = MyContext(deployment_group="blue")
ctx_green = MyContext(deployment_group="green")

# Resources get different names based on deployment group
# myapp-api-DataBucket-prod-001-blue-us-east-1
# myapp-api-DataBucket-prod-001-green-us-east-1
```

## Key Concepts

### Wrapper Classes

Configuration is defined using wrapper classes:

```python
@cloudformation_dataclass
class MyBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [MyServerSideEncryptionRule]
```

Benefits:
- **Reusable**: Use the same config across multiple resources
- **Type-safe**: IDE autocomplete and validation
- **Declarative**: Clear, readable configuration

### Auto-Registration

Resources are automatically collected when you call `Template.from_registry()`:

```python
bucket = DataBucket()   # Registered
role = MyIAMRole()      # Registered

template = Template.from_registry()  # Collects all registered resources
```

## Next Steps

- **Add more resources**: Create new files for Lambda, IAM, etc.
- **Customize naming**: Override `naming_pattern` in your context
- **Add tags**: Define organization-specific tags in `context.py`
- **Import existing templates**: Use `cfn-import` to convert CloudFormation YAML

## See Also

- [Template Importer](IMPORTER.md)
