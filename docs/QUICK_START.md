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
│   ├── __init__.py    # Centralized imports + setup_resources()
│   ├── __init__.pyi   # Type stubs
│   ├── __main__.py    # For `python -m my_project`
│   └── main.py        # Your resources
└── pyproject.toml
```

## Add Your First Resource

Create `my_project/storage.py`:

```python
from . import *

@cloudformation_dataclass
class DataBucket:
    resource: s3.Bucket
    bucket_name = "my-data-bucket"
```

That's it. Resources auto-register when defined. The `from . import *` pattern provides everything you need: `cloudformation_dataclass`, `ref`, `get_att`, and AWS modules like `s3`, `ec2`, `lambda_` (all imported in `__init__.py`).

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
my_project/
├── __init__.py      # Auto-discovery via setup_resources()
├── storage.py       # S3, EFS
├── compute.py       # Lambda, EC2
├── network.py       # VPC, Subnets
└── database.py      # DynamoDB, RDS
```

Each file just imports from the package:

```python
# compute.py
from . import *

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
# storage.py
from . import *

@cloudformation_dataclass
class DataBucket:
    resource: s3.Bucket
    bucket_name = "data"

# compute.py
from . import *

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
# __main__.py
from cloudformation_dataclasses import run_package_cli

# Auto-builds template from all registered resources
run_package_cli(__name__, description="My Application Stack")

# Or with custom logic:
def build_template() -> Template:
    template = Template.from_registry(
        description="My Application Stack",
        parameters=[EnvironmentParam],
        outputs=[BucketArnOutput],
    )
    return template

run_package_cli(__name__, build_fn=build_template)
```

---

## Linting and IDE Support

The CLI includes tools to keep your code clean and your IDE happy.

### Linting

Check for common issues and auto-fix them:

```bash
# Check for issues
cfn-dataclasses lint my_project/

# Auto-fix issues
cfn-dataclasses lint my_project/ --fix

# Watch mode (auto-fix enabled by default)
cfn-dataclasses lint my_project/ --watch
```

The linter detects patterns like raw dict intrinsics (`{"Ref": "..."}`) and suggests type-safe alternatives (`Ref("...")`). See [CLI Reference](CLI.md#lint) for all lint rules.

### Type Stubs

The `from . import *` pattern requires `.pyi` stub files for IDE autocomplete. These are generated automatically by:

- `cfn-dataclasses init` and `cfn-dataclasses import`
- `cfn-dataclasses lint --fix`
- `setup_resources()` at runtime (if missing)

To manually regenerate stubs:

```bash
cfn-dataclasses stubs my_project/

# Or watch mode
cfn-dataclasses stubs my_project/ --watch
```

See [IDE Support](IDE_SUPPORT.md) for Pylance/mypy configuration.

---

## Next Steps

- See [examples/](../examples/) for real-world templates
- Use `cfn-dataclasses import` to convert existing CloudFormation templates

## See Also

- [Adoption Guide](ADOPTION.md) - Migration strategies and team onboarding
- [CLI Reference](CLI.md) - Full command documentation
- [IDE Support](IDE_SUPPORT.md) - Pylance, mypy, type checking setup
- [Internals](INTERNALS.md) - How auto-registration works
