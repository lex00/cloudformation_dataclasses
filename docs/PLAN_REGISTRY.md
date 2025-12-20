# Plan: Auto-Registration for @cloudformation_dataclass Resources

## Problem Statement

Currently, building a template requires manually listing all resources:
```python
@cloudformation_dataclass
class CompliantBucketTemplate:
    resource: Template
    resources = [ObjectStorageBucket, ObjectStorageBucketPolicy, ObjectStorageLogBucket, ...]
```

This is problematic when:
1. **Splitting across files**: Resources in separate files must be imported and manually added
2. **Querying by type**: No way to get "all DynamoDB tables" from a project for DynamoDB Local export
3. **Large templates**: Long resource lists are error-prone

## Proposed Solution: Resource Registry

### Concept

Resources auto-register when their class is defined:

```python
# tables/users.py
@cloudformation_dataclass
class UsersTable:
    resource: Table
    table_name = "users"
    # Automatically registered!

# tables/orders.py
@cloudformation_dataclass
class OrdersTable:
    resource: Table
    table_name = "orders"
    # Also registered!

# main.py
from cloudformation_dataclasses import registry

# Get all registered resources
all_resources = registry.get_all()

# Query by type
tables = registry.get_by_type(Table)  # [UsersTable, OrdersTable]
tables = registry.get_by_type("AWS::DynamoDB::Table")  # same

# Build template from registry
template = Template(resources=registry.get_all())

# Export just tables for DynamoDB Local
for table_cls in registry.get_by_type(Table):
    table = table_cls().resource
    print(table.to_dict())
```

---

## Implementation Plan

### Step 1: Create ResourceRegistry Class

**File:** `src/cloudformation_dataclasses/core/registry.py` (new)

```python
from typing import Any, Type
from threading import Lock

class ResourceRegistry:
    """
    Global registry for @cloudformation_dataclass wrapper classes.

    Resources auto-register when decorated, enabling:
    - Multi-file template organization
    - Type-based queries (e.g., all DynamoDB tables)
    - Automatic template building
    """

    def __init__(self):
        self._resources: dict[str, Type] = {}  # class_name -> class
        self._by_type: dict[str, list[Type]] = {}  # cf_type -> [classes]
        self._lock = Lock()

    def register(self, wrapper_cls: Type, resource_type: str) -> None:
        """Register a wrapper class."""
        with self._lock:
            name = wrapper_cls.__name__
            self._resources[name] = wrapper_cls

            if resource_type not in self._by_type:
                self._by_type[resource_type] = []
            self._by_type[resource_type].append(wrapper_cls)

    def get_all(self) -> list[Type]:
        """Get all registered wrapper classes."""
        return list(self._resources.values())

    def get_by_type(self, resource_type: Type | str) -> list[Type]:
        """
        Get wrapper classes by resource type.

        Args:
            resource_type: Either a class (Table) or CF type string ("AWS::DynamoDB::Table")
        """
        if isinstance(resource_type, type):
            # Get CF type from class
            cf_type = getattr(resource_type, 'resource_type', None)
            if cf_type is None:
                return []
        else:
            cf_type = resource_type

        return self._by_type.get(cf_type, [])

    def get_by_name(self, name: str) -> Type | None:
        """Get a wrapper class by its class name."""
        return self._resources.get(name)

    def clear(self) -> None:
        """Clear the registry (useful for testing)."""
        with self._lock:
            self._resources.clear()
            self._by_type.clear()


# Global registry instance
registry = ResourceRegistry()
```

### Step 2: Update Decorator to Auto-Register

**File:** `src/cloudformation_dataclasses/core/wrapper.py`

Modify `cloudformation_dataclass` to register the class:

```python
def cloudformation_dataclass(maybe_cls=None, *, register=True):
    """
    Decorator that enables the CloudFormation dataclass pattern.

    Args:
        register: If True (default), auto-register with global registry
    """
    def decorator(cls: Type[Any]) -> Type[Any]:
        # ... existing decorator logic ...

        # Auto-register if requested
        if register:
            from cloudformation_dataclasses.core.registry import registry

            # Get the wrapped resource type
            wrapped_type = get_wrapped_resource_type(cls)
            if wrapped_type is not None:
                cf_type = getattr(wrapped_type, 'resource_type', None)
                if cf_type:
                    registry.register(cls, cf_type)

        return cls

    # Handle @cloudformation_dataclass and @cloudformation_dataclass() syntax
    if maybe_cls is None:
        return decorator
    else:
        return decorator(maybe_cls)
```

### Step 3: Add Registry Exports

**File:** `src/cloudformation_dataclasses/core/__init__.py`

```python
from cloudformation_dataclasses.core.registry import registry, ResourceRegistry
```

### Step 4: Template Auto-Discovery from Registry

**The key insight**: Templates should not need to specify resources at all. With auto-registration, the template can discover all resources from the registry.

**File:** `src/cloudformation_dataclasses/core/template.py`

Add `Template.from_registry()` class method:

```python
@classmethod
def from_registry(
    cls,
    description: str = "",
    parameters: dict[str, Parameter] | None = None,
    **kwargs
) -> "Template":
    """
    Build a template from all registered resources.

    Resources are automatically discovered from the global registry.
    No need to list them manually.
    """
    from cloudformation_dataclasses.core.registry import registry

    return cls(
        description=description,
        parameters=parameters or {},
        resources=registry.get_all(),
        **kwargs
    )
```

**Generated code becomes simpler** - no more long resource lists:

Before:
```python
@cloudformation_dataclass
class CompliantBucketTemplate:
    resource: Template
    description = "A secure bucket..."
    resources = [ObjectStorageBucket, ObjectStorageBucketPolicy, ObjectStorageLogBucket,
                 ObjectStorageLogBucketPolicy, ObjectStorageReplicaBucket, ...]  # ugly!
```

After:
```python
# Just define resources, no template wrapper needed
# Then in main.py:
template = Template.from_registry(description="A secure bucket...")
```

Or if you want a wrapper class:
```python
@cloudformation_dataclass
class CompliantBucketTemplate:
    resource: Template
    description = "A secure bucket..."
    # resources auto-populated from registry - no need to specify!
```

---

## Usage Examples

### Multi-File Organization

```python
# infrastructure/tables.py
@cloudformation_dataclass
class UsersTable:
    resource: Table
    ...

@cloudformation_dataclass
class OrdersTable:
    resource: Table
    ...

# infrastructure/queues.py
@cloudformation_dataclass
class OrderQueue:
    resource: Queue
    ...

# main.py
from infrastructure import tables, queues  # Just import to trigger registration
from cloudformation_dataclasses import registry, Template

template = Template(
    description="My Infrastructure",
    resources=registry.get_all()
)
```

### DynamoDB Local Export

```python
from cloudformation_dataclasses import registry
from cloudformation_dataclasses.aws.dynamodb import Table

# Get only tables, skip autoscaling
for table_cls in registry.get_by_type(Table):
    table = table_cls().resource
    # Export for DynamoDB Local
    print(json.dumps(table.to_dict()))
```

---

### Step 5: Update Importer to Use Registry

**File:** `src/cloudformation_dataclasses/importer/codegen.py`

The importer should:
1. Generate resource classes (which auto-register)
2. Generate a simple `build_template()` function that uses `Template.from_registry()`
3. **No longer generate the long `resources = [...]` list**

Generated output:
```python
# ... resource definitions ...

def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description="A secure bucket that passes default security scanning checks..."
    )
```

---

## Files Modified

| File | Change |
|------|--------|
| `src/cloudformation_dataclasses/core/registry.py` | New file: `ResourceRegistry` class |
| `src/cloudformation_dataclasses/core/wrapper.py` | Add auto-registration in decorator |
| `src/cloudformation_dataclasses/core/__init__.py` | Export `registry` |
| `src/cloudformation_dataclasses/core/template.py` | Add `Template.from_registry()` |
| `src/cloudformation_dataclasses/importer/codegen.py` | Use `Template.from_registry()` instead of resource list |

---

## Design Decisions

1. **Registration scope**: Global by default, no opt-in required. Use `registry.clear()` in test setup for isolation.

2. **Duplicate handling**: Overwrite silently. Last class with same name wins.

3. **PropertyTypes**: Only top-level resources register. The check is `hasattr(wrapped_type, 'resource_type')` - only `CloudFormationResource` subclasses have this, not `PropertyType` or `PolicyDocument`.
