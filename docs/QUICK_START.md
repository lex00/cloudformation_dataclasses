# Quick Start

Get started with `cloudformation_dataclasses` in 5 minutes.

## Installation

```bash
# Using uv (recommended)
uv add cloudformation_dataclasses

# Or using pip
pip install cloudformation_dataclasses
```

## Create a New Project

Use the `init` subcommand to create a new project:

```bash
uv run cfn-dataclasses init -o my_project/
```

This creates a complete project structure:

```
my_project/
├── my_project/        # Python package
│   ├── __init__.py    # Common imports (Template, cloudformation_dataclass, ref, get_att)
│   ├── main.py        # Template builder and entry point
│   ├── __main__.py    # Allows `python -m my_project`
│   └── stack/         # Parameters and resources
├── tests/             # Test suite
├── pyproject.toml     # Package config with dependencies
├── py.typed           # PEP 561 typed package marker
├── mypy.ini           # mypy type checking config
├── CLAUDE.md          # Claude Code project guidance
├── .vscode/           # VSCode settings
└── README.md          # Project documentation
```

## Add Your First Resource

### 1. Edit `my_project/__init__.py`

Uncomment the AWS module imports you need:

```python
# In my_project/__init__.py
from cloudformation_dataclasses.aws import s3  # Uncomment and add modules
```

### 2. Create a Resource File

Create `my_project/stack/storage.py`:

```python
from .. import *  # noqa: F403

@cloudformation_dataclass
class DataBucket:
    resource: s3.Bucket
    bucket_name = "my-data-bucket"
```

### 3. Generate CloudFormation

```bash
uv run python -m my_project
```

This outputs the CloudFormation JSON template to stdout.

### 4. Deploy

```bash
# Generate template file
uv run python -m my_project > template.json

# Deploy with AWS CLI
aws cloudformation deploy \
    --template-file template.json \
    --stack-name my-project-dev
```

## CLI Options

Customize the project name:

```bash
uv run cfn-dataclasses init -o my_project/ --project-name analytics
```

## Adding Tags

Define reusable tags as wrapper classes:

```python
from .. import *  # noqa: F403

@cloudformation_dataclass
class EnvironmentTag:
    resource: Tag
    key = "Environment"
    value = "prod"

@cloudformation_dataclass
class DataBucket:
    resource: s3.Bucket
    bucket_name = "my-data-bucket"
    tags = [EnvironmentTag, Tag(key="Team", value="Data")]
```

## Cross-Resource References

Use `ref()` and `get_att()` for type-safe references between resources:

```python
from .. import *  # noqa: F403

@cloudformation_dataclass
class MyBucket:
    resource: s3.Bucket

@cloudformation_dataclass
class MyBucketPolicy:
    resource: s3.BucketPolicy
    bucket = ref(MyBucket)  # Type-safe reference
```

## Next Steps

- **Add more resources**: Create new files in `stack/` for Lambda, IAM, DynamoDB, etc.
- **Import existing templates**: Use `cfn-dataclasses import` to convert CloudFormation YAML
- **Lint your code**: Use `cfn-dataclasses lint` to check for style issues

## See Also

- [Template Importer](IMPORTER.md) - Convert existing CloudFormation templates
- [Registry](REGISTRY.md) - Multi-file organization and resource discovery
