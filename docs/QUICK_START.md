# Quick Start

Get started with `cloudformation_dataclasses` in 5 minutes.

## Installation

```bash
pip install cloudformation_dataclasses
```

## Create a New Project

Use the skeleton generator to create a new project with best practices:

```bash
cfn-dataclasses-init default -o my_project/
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
    region = "us-east-1"             # AWS region
    tags = [EnvironmentTag, ...]     # Base tags for all resources
```

Resources using this context automatically get:
- **Consistent naming**: Based on the naming pattern (e.g., `myproject-MyComponent-DataBucket-dev-us-east-1`)
- **Base tags**: Applied to all resources

See the [Context Guide](CONTEXT.md) for full documentation on naming patterns, tag management, and multi-environment deployments.

### 2. Add Resources

Create a new file for each resource. For example, `my_project/bucket.py`:

```python
from . import *
from cloudformation_dataclasses.aws.s3 import Bucket

@cloudformation_dataclass
class DataBucket:
    resource: Bucket
    # Context is applied at template level - no need to set it here
```

Then build the template in `my_project/main.py`:

```python
from .context import ctx

def build_template() -> Template:
    return Template.from_registry(
        description="My Infrastructure",
        context=ctx,  # Applies naming + tags to all resources
    )
```

The context automatically:
- Sets physical names (e.g., `bucket_name`) based on the naming pattern
- Merges context tags with any resource-specific tags

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
cfn-dataclasses-init default -o my_project/ \
    --project-name analytics \
    --component storage \
    --stage prod \
    --region us-west-2
```

List available skeletons:

```bash
cfn-dataclasses-init --list
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
- **Import existing templates**: Use `cfn-dataclasses-import` to convert CloudFormation YAML

## See Also

- [Context Guide](CONTEXT.md) - Full documentation on naming patterns, tags, and multi-environment deployments
- [Template Importer](IMPORTER.md) - Convert existing CloudFormation templates
- [with_context example](../examples/with_context/s3_bucket/) - Complete working example with context
