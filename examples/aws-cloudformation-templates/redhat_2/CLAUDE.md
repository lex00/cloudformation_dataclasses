# Redhat2

CloudFormation infrastructure using cloudformation_dataclasses.

## Key Patterns

1. **Wrapper classes** with `@cloudformation_dataclass` decorator
2. **Type-safe enums** - use enum values, not strings
3. **ref() for references** - `ref(MyResource)` or `Ref("ParamName")`
4. **Intrinsic functions** - use typed helpers, not raw dicts

## Anti-Patterns to Avoid

NEVER use raw CloudFormation dict patterns:

```python
# ❌ WRONG
vpc_id = {"Ref": "VpcId"}
az = {"Fn::Select": [0, {"Fn::GetAZs": ""}]}
assume_role_policy_document = {"Version": "2012-10-17", "Statement": [...]}

# ✅ CORRECT
from cloudformation_dataclasses.intrinsics import Ref, Select, GetAZs
vpc_id = Ref("VpcId")
az = Select(0, GetAZs())
# Use separate PolicyDocument/PolicyStatement wrapper classes
```

## Intrinsic Functions

```python
from cloudformation_dataclasses.intrinsics import (
    Ref, Sub, Join, Select, GetAZs,
    AWS_REGION, AWS_ACCOUNT_ID, AWS_STACK_NAME,
)
```

## Commands

```bash
# Generate template
python -m redhat_2

# Type check
mypy redhat_2/

# Lint
cfn-dataclasses lint redhat_2/
```

## Validation

```python
template = Template.from_registry()
errors = template.validate()
assert errors == []
```

## Adding Resources

1. Create wrapper class in package directory
2. Use `@cloudformation_dataclass` decorator
3. All nested PropertyTypes should be separate wrapper classes
4. Resources auto-register via `setup_resources()` in `__init__.py`
