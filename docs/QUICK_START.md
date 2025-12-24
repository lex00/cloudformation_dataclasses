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

### 1. Add Resources

Create a new file for each resource. For example, `my_project/bucket.py`:

```python
from . import *
from cloudformation_dataclasses.aws.s3 import Bucket

@cloudformation_dataclass
class DataBucket:
    resource: Bucket
    bucket_name = "my-data-bucket"
```

### 2. Add Tags

Define reusable tags as wrapper classes:

```python
@cloudformation_dataclass
class EnvironmentTag:
    resource: Tag
    key = "Environment"
    value = "prod"

@cloudformation_dataclass
class DataBucket:
    resource: Bucket
    bucket_name = "my-data-bucket"
    tags = [EnvironmentTag, Tag(key="Team", value="Data")]
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
- **Import existing templates**: Use `cfn-dataclasses-import` to convert CloudFormation YAML

## See Also

- [Template Importer](IMPORTER.md) - Convert existing CloudFormation templates
- [Registry](REGISTRY.md) - Multi-file organization and resource discovery
