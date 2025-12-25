# Adoption Guide

Practical guidance for teams adopting cloudformation_dataclasses alongside existing infrastructure.

---

## Migration Strategies

### Side-by-Side Adoption

You don't need to migrate everything at once. cloudformation_dataclasses generates standard CloudFormation templates that deploy with the same CLI you already use.

**Coexistence patterns:**

| Existing Tool | Integration Approach |
|---------------|---------------------|
| Raw CloudFormation | Import existing templates with `cfn-dataclasses import`, or keep them as-is and gradually add new stacks in Python |
| CDK | Both generate CloudFormation. Deploy CDK stacks and dataclass stacks independently |
| Terraform | Separate state domains. Terraform manages its resources; CloudFormation manages yours |

### Incremental Migration Path

**Week 1: Proof of concept**
- Pick a small, isolated stack (dev environment, internal tool)
- Import it: `cfn-dataclasses import template.yaml -o my_stack/`
- Verify the generated Python produces identical CloudFormation output
- Deploy to a test environment

**Week 2-4: Build confidence**
- Convert 2-3 more stacks
- Establish team patterns (file organization, naming conventions)
- Set up CI/CD for the new Python stacks

**Ongoing: New stacks in Python**
- All new infrastructure uses cloudformation_dataclasses
- Migrate legacy stacks opportunistically (when you're touching them anyway)

### Import Workflow

```bash
# Single template
cfn-dataclasses import template.yaml -o my_stack/

# Directory of templates
cfn-dataclasses import templates/ -o output/

# Verify output matches
diff <(python -m my_stack) template.json
```

The importer preserves:
- Resource logical IDs
- Parameter names and defaults
- Output definitions
- Conditions and mappings

### What NOT to Migrate

Some stacks are better left alone:
- **Stable production stacks** that never change
- **Stacks managed by other teams** (coordinate first)
- **CDK stacks with heavy L2/L3 usage** (the abstractions don't translate)

Migration should reduce maintenance burden, not create it.

---

## Escape Hatches

When you hit an edge case the library doesn't handle cleanly.

### Raw CloudFormation Passthrough

For properties not yet typed, pass raw dictionaries:

```python
@cloudformation_dataclass
class MyResource:
    resource: SomeResource
    # Typed properties
    name = "my-resource"
    # Raw passthrough for untyped/new properties
    some_new_property = {"Key": "Value", "Nested": {"Deep": True}}
```

The serializer passes dictionaries through unchanged.

### Untyped Resources

If a resource type isn't in the library yet (new AWS service, custom resource):

```python
from cloudformation_dataclasses.core import CloudFormationResource

@dataclass
class MyCustomResource(CloudFormationResource):
    """Custom resource not yet in the library."""

    class Meta:
        resource_type = "AWS::NewService::Resource"

    property_one: str
    property_two: int = 42
```

This gives you type safety for your properties while using a resource type the library doesn't know about.

### Inline CloudFormation JSON

For complex intrinsic function combinations:

```python
@cloudformation_dataclass
class MyResource:
    resource: Function
    environment = {
        "COMPLEX_VALUE": {
            "Fn::Join": ["-", [
                {"Ref": "AWS::StackName"},
                {"Fn::Select": [0, {"Fn::Split": [",", {"Ref": "SomeParam"}]}]}
            ]]
        }
    }
```

Raw CloudFormation intrinsics pass through. Use this sparingly—if you're doing this often, something's wrong.

### When to Use Escape Hatches

| Situation | Approach |
|-----------|----------|
| New AWS resource type | Custom resource class |
| New property on existing resource | Raw dict passthrough |
| Complex Fn::If/Fn::Join nesting | Inline CloudFormation JSON |
| One-off weird requirement | Whatever works, with a comment |

### When to File an Issue

If you're using escape hatches for:
- Common resource types
- Standard properties
- Patterns other teams would need

...file an issue. The library should handle it.

---

## Team Onboarding

A playbook for getting your team productive in the first week.

### Day 1: Environment Setup

```bash
# Clone your stack repo
git clone <repo>
cd <repo>

# Install dependencies
uv sync

# Verify it works
uv run python -m my_stack > /dev/null && echo "OK"
```

**What to check:**
- Python 3.10+ installed
- uv or pip available
- AWS credentials configured (for deployment)

### Day 1-2: Read the Code

Start with `__init__.py`:
```python
# This imports everything you need
from cloudformation_dataclasses.core import (
    cloudformation_dataclass,
    ref,
    get_att,
    ...
)
from cloudformation_dataclasses.aws import s3, ec2, lambda_
```

Then read one resource file:
```python
from . import *

@cloudformation_dataclass
class DataBucket:
    resource: s3.Bucket
    bucket_name = "my-data"
```

That's the pattern. Every resource file looks like this.

### Day 2-3: Make a Small Change

Find something low-risk:
- Add a tag to an existing resource
- Change a parameter default
- Add a new output

```python
# Before
@cloudformation_dataclass
class MyBucket:
    resource: s3.Bucket
    bucket_name = "data"

# After
@cloudformation_dataclass
class MyBucket:
    resource: s3.Bucket
    bucket_name = "data"
    tags = [Tag(key="Environment", value="dev")]
```

Run it, diff the output, deploy to dev.

### Day 3-4: Add a New Resource

Create a new file in the package directory:

```python
# monitoring.py
from . import *

@cloudformation_dataclass
class AlertTopic:
    resource: sns.Topic
    topic_name = "alerts"
```

Resources auto-register. No imports to update elsewhere.

### Day 5: Review the Patterns

By now you've seen:
- `from . import *` at the top of every file
- `@cloudformation_dataclass` decorator
- `resource: <type>` to specify the CloudFormation type
- `ref()` and `get_att()` for references
- Class attributes for properties

That's 90% of what you need.

### Common Gotchas

| Problem | Solution |
|---------|----------|
| "NameError: s3 is not defined" | Check `__init__.py` imports the AWS module |
| "Circular import" | Shouldn't happen—use `from . import *` pattern |
| "Resource not in template" | File not in package directory, or missing decorator |
| "Wrong property name" | Use IDE autocomplete, or check the AWS docs |

### Team Conventions to Establish

Decide these early:
- **File organization**: By service (network.py, compute.py) or by feature?
- **Naming**: PascalCase for classes, snake_case for files?
- **Parameter patterns**: Centralized params.py or per-feature?

Document in your repo's README.

### Resources

- [Quick Start](QUICK_START.md) - 5-minute intro
- [CLI Reference](CLI.md) - Import and lint commands
- [Internals](INTERNALS.md) - How auto-registration works

---

## See Also

- [Philosophy](PHILOSOPHY.md) - Why this approach
- [Comparison](COMPARISON.md) - vs CDK, Terraform, raw CloudFormation
