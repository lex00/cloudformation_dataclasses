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

```bash
cfn-dataclasses init -o my_project/
```

This creates:

```
my_project/
├── my_project/
│   ├── __init__.py    # Centralized imports
│   ├── __main__.py    # For `python -m my_project`
│   ├── main.py        # Template builder
│   └── stack/         # Your resources
│       ├── __init__.py
│       └── main.py
├── tests/
└── pyproject.toml
```

## Add Your First Resource

Create `my_project/stack/storage.py`:

```python
from .. import *

@cloudformation_dataclass
class DataBucket:
    resource: s3.Bucket
    bucket_name = "my-data-bucket"
```

That's it. Resources auto-register when defined. The `from .. import *` pattern provides everything you need: `cloudformation_dataclass`, `ref`, `get_att`, and AWS modules like `s3`, `ec2`, `lambda_` (all imported in the parent `__init__.py`).

### Generate CloudFormation

```bash
uv run python -m my_project
```

Outputs CloudFormation JSON to stdout.

### Deploy

```bash
uv run python -m my_project > template.json
aws cloudformation deploy --template-file template.json --stack-name my-project
```

---

## Multi-File Organization

Split resources across files - they all register automatically:

```
my_project/stack/
├── __init__.py      # Auto-discovery via setup_resources()
├── storage.py       # S3, EFS
├── compute.py       # Lambda, EC2
├── network.py       # VPC, Subnets
└── database.py      # DynamoDB, RDS
```

Each file just imports from the parent package:

```python
# stack/compute.py
from .. import *

@cloudformation_dataclass
class MyFunction:
    resource: lambda_.Function
    function_name = "my-handler"
    runtime = Runtime.PYTHON3_12
    role: GetAtt[ExecutionRole] = get_att(ARN)  # Reference resource in another file
```

**Key benefit:** Resources auto-register when defined. Move resources between files freely - auto-discovery handles everything.

---

## Cross-File References

Reference resources defined in other files using type annotations:

```python
# stack/storage.py
from .. import *

@cloudformation_dataclass
class DataBucket:
    resource: s3.Bucket
    bucket_name = "data"

# stack/compute.py
from .. import *

@cloudformation_dataclass
class ProcessorFunction:
    resource: lambda_.Function
    environment = {"BUCKET": ref(DataBucket)}  # Reference works across files
```

For forward references (when the target isn't imported yet), use type annotations:

```python
bucket: Ref[DataBucket] = ref()  # Type annotation resolves at runtime
```

---

## Template Building

`Template.from_registry()` collects all registered resources automatically:

```python
# main.py
from my_project.stack import *  # Triggers auto-discovery

template = Template.from_registry(
    description="My Application Stack",
    parameters=[EnvironmentParam],
    outputs=[BucketArnOutput],
)
print(template.to_json())
```

---

## Next Steps

- See [examples/](../examples/) for real-world templates
- Use `cfn-dataclasses import` to convert existing CloudFormation templates
- Use `cfn-dataclasses lint --fix` to auto-fix style issues

## See Also

- [Adoption Guide](ADOPTION.md) - Migration strategies and team onboarding
- [CLI Reference](CLI.md) - Full command documentation
- [Internals](INTERNALS.md) - How auto-registration works
