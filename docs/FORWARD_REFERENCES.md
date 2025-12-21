# Forward References

This guide explains how to reference resources across modules in `cloudformation_dataclasses`, including the annotation-based forward reference pattern that enables IDE support for cross-module dependencies.

## Overview

When building CloudFormation templates with multiple resources, you often need to reference one resource from another. For example, a bucket policy needs to reference its bucket, or a Lambda function needs its IAM role's ARN.

**The challenge**: In Python, if you write `ref(Bucket)` but the `Bucket` class isn't defined or imported yet, you get a `NameError`. This commonly happens with:
- Cross-module references (resources in different files)
- Auto-discovery patterns (resources registered dynamically)
- Circular dependencies between resources

**The solution**: Use annotation-based forward references with PEP 563.

## The Three Reference Patterns

### Pattern 1: Direct Class Reference

```python
from .my_vpc import MyVPC

@cloudformation_dataclass
class MySubnet:
    resource: Subnet
    vpc_id = ref(MyVPC)  # Direct reference to imported class
```

**When to use**:
- The target class is in the same file
- The target class is already imported
- Referencing parameters (defined in `config.py` and imported before resources)

**IDE support**: Full autocomplete and go-to-definition.

### Pattern 2: String Reference

```python
@cloudformation_dataclass
class MyBucketPolicy:
    resource: BucketPolicy
    bucket = ref("MyBucket")  # String logical ID
```

**When to use**:
- Simple cases where you don't need IDE navigation
- Quick prototypes
- When the target's class name matches its logical ID

**IDE support**: None - no autocomplete or navigation.

### Pattern 3: Annotation-Based Reference (Recommended for Cross-Module)

```python
from __future__ import annotations

@cloudformation_dataclass
class MyBucketPolicy:
    resource: BucketPolicy
    bucket: Ref[MyBucket] = ref()  # Type annotation + empty ref()
```

**When to use**:
- Cross-module references
- Auto-discovery patterns (resources in `resources/__init__.py`)
- Any time you want IDE support but can't import the class directly

**IDE support**: Full autocomplete and go-to-definition via the type annotation.

## Type Markers

The library provides two generic type markers for annotation-based references:

### `Ref[T]` - Resource References

Creates a CloudFormation `{"Ref": "LogicalId"}` intrinsic function.

```python
from __future__ import annotations
from cloudformation_dataclasses.core import Ref, ref

@cloudformation_dataclass
class MyBucketPolicy:
    resource: BucketPolicy
    bucket: Ref[MyBucket] = ref()  # → {"Ref": "MyBucket"}
```

### `GetAtt[T]` - Attribute References

Creates a CloudFormation `{"Fn::GetAtt": ["LogicalId", "Attribute"]}` intrinsic function.

```python
from __future__ import annotations
from cloudformation_dataclasses.core import GetAtt, get_att

@cloudformation_dataclass
class MyLambdaFunction:
    resource: Function
    role: GetAtt[MyLambdaRole] = get_att("Arn")  # → {"Fn::GetAtt": ["MyLambdaRole", "Arn"]}
```

## Decision Tree: Which Pattern to Use?

```
Is the target class already imported/defined?
├── YES → Use Pattern 1: ref(TargetClass)
└── NO
    ├── Do you need IDE support (autocomplete, go-to-definition)?
    │   ├── YES → Use Pattern 3: target: Ref[TargetClass] = ref()
    │   └── NO  → Use Pattern 2: ref("TargetClass")
```

**Quick reference table**:

| Scenario | Pattern | Example |
|----------|---------|---------|
| Same-file reference | Direct | `vpc_id = ref(MyVPC)` |
| Parameter reference | Direct | `bucket_name = ref(BucketNameParam)` |
| Cross-module, need IDE | Annotation | `vpc_id: Ref[MyVPC] = ref()` |
| Cross-module, no IDE needed | String | `vpc_id = ref("MyVPC")` |
| GetAtt cross-module | Annotation | `role_arn: GetAtt[MyRole] = get_att("Arn")` |

---

## How It Works

This section explains the implementation for contributors and curious developers.

### PEP 563: `from __future__ import annotations`

Python 3.7+ supports [PEP 563](https://peps.python.org/pep-0563/), which changes how annotations are evaluated:

```python
# Without PEP 563 - annotation evaluated immediately
class Foo:
    bar: UndefinedClass  # NameError!

# With PEP 563 - annotation becomes a string
from __future__ import annotations

class Foo:
    bar: UndefinedClass  # No error - stored as string "UndefinedClass"
```

This is the key enabler: `Ref[MyBucket]` becomes the string `"Ref[MyBucket]"` at parse time, avoiding any `NameError` for undefined classes.

### Type Marker Classes

`Ref[T]` and `GetAtt[T]` are simple generic classes with no implementation:

```python
from typing import Generic, TypeVar

T = TypeVar("T")

class Ref(Generic[T]):
    """Type marker for resource references."""
    pass

class GetAtt(Generic[T]):
    """Type marker for GetAtt references."""
    pass
```

They exist purely for:
1. **Type hints** - IDE sees `Ref[MyBucket]` and provides autocomplete
2. **Runtime inspection** - The decorator extracts `MyBucket` from `__args__`

### Deferred Reference Objects

When you call `ref()` or `get_att()` without a class argument, they return deferred objects:

```python
ref()  # Returns DeferredRef(logical_id=None)
get_att("Arn")  # Returns DeferredGetAtt(logical_id=None, attribute_name="Arn")
```

The `logical_id=None` signals that resolution must happen later from the type annotation.

### Runtime Resolution in the Decorator

The `@cloudformation_dataclass` decorator resolves forward references when the wrapper is instantiated:

1. **Get type hints with registry context**:
   ```python
   from typing import get_type_hints

   # The registry contains all auto-discovered wrapper classes
   localns = {cls.__name__: cls for cls in registry.get_all()}
   hints = get_type_hints(wrapper_class, globalns=module_globals, localns=localns)
   ```

2. **Extract generic arguments**:
   ```python
   # For annotation: bucket: Ref[MyBucket] = ref()
   hint = hints["bucket"]  # Ref[MyBucket]
   origin = hint.__origin__  # Ref
   args = hint.__args__  # (MyBucket,)
   target = args[0].__name__  # "MyBucket"
   ```

3. **Set the logical ID**:
   ```python
   deferred_ref.logical_id = target  # "MyBucket"
   ```

4. **Serialize to CloudFormation**:
   ```python
   deferred_ref.to_dict()  # {"Ref": "MyBucket"}
   ```

### Registry Integration

The [Resource Registry](REGISTRY.md) is critical for forward reference resolution:

- Every `@cloudformation_dataclass` that wraps a resource auto-registers
- The registry provides classes for `get_type_hints()` to resolve annotations
- This enables cross-module references without explicit imports

## Common Issues and Troubleshooting

### NameError at Import Time

**Symptom**: `NameError: name 'MyBucket' is not defined`

**Cause**: Using `ref(MyBucket)` without importing the class, or forgetting `from __future__ import annotations`.

**Solution**: Use annotation-based pattern:
```python
from __future__ import annotations

@cloudformation_dataclass
class MyPolicy:
    bucket: Ref[MyBucket] = ref()  # Not ref(MyBucket)
```

### IDE Not Recognizing Reference

**Symptom**: No autocomplete or go-to-definition on `Ref[MyBucket]`.

**Cause**: IDE doesn't know about `MyBucket` class.

**Solution**: Ensure the target class exists and your IDE has indexed the project. Some IDEs need the class to be defined somewhere, even if not imported in the current file.

### Reference Not Resolving at Runtime

**Symptom**: `ValueError: DeferredRef.logical_id must be set before serialization`

**Cause**: The target class isn't registered or the annotation couldn't be resolved.

**Solution**:
1. Ensure target class uses `@cloudformation_dataclass`
2. Ensure target class wraps a resource (has `resource: SomeResource` field)
3. Import the module containing the target before instantiation

### Circular Import Errors

**Symptom**: `ImportError: cannot import name 'X' from partially initialized module`

**Cause**: Two modules importing each other directly.

**Solution**: Use annotation-based references instead of direct imports:
```python
# Instead of:
from .bucket import MyBucket
bucket = ref(MyBucket)

# Use:
from __future__ import annotations
bucket: Ref[MyBucket] = ref()
```

## Why This Syntax?

You might wonder: why can't we simplify `bucket: Ref[Bucket] = ref()` to just `bucket = ref(Bucket)`?

**The fundamental issue**: Python evaluates expressions immediately at class definition time.

```python
@cloudformation_dataclass
class MyPolicy:
    bucket = ref(Bucket)  # Python evaluates Bucket RIGHT NOW → NameError
```

The `ref(Bucket)` call executes **before** the decorator runs. Python looks up `Bucket` as a name, and if it's not defined, you get a `NameError`.

**Why annotations work**: With `from __future__ import annotations`, Python converts annotations to strings without evaluating them:

```python
bucket: Ref[Bucket] = ref()  # "Ref[Bucket]" stored as string, ref() called with no args
```

The decorator can later parse the string `"Ref[Bucket]"` and resolve it when the registry is populated.

**Alternatives considered**:

| Approach | Syntax | Problem |
|----------|--------|---------|
| String literal | `ref("Bucket")` | Loses IDE support |
| Lambda | `ref(lambda: Bucket)` | Ugly, still no IDE autocomplete |
| Late binding | Complex metaclass | Can't intercept `ref()` before it executes |

The annotation-based approach is the only way to get **both** deferred evaluation **and** full IDE support in Python.

## See Also

- [Resource Registry](REGISTRY.md) - Auto-registration and multi-file organization
- [Template Importer](IMPORTER.md) - `cfn-import` generates annotation-based refs
- [Agent Guide](AGENT_GUIDE.md) - Workflows for AI assistants
