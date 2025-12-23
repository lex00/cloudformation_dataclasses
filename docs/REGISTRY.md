# Resource Registry

The resource registry enables automatic registration of CloudFormation resources, eliminating the need to manually list resources in templates.

## Overview

When you decorate a class with `@cloudformation_dataclass`, it automatically registers with a global registry. This enables:

- **Multi-file organization** - Split resources across files without manual imports
- **Type-based queries** - Get all DynamoDB tables, all S3 buckets, etc.
- **Automatic template building** - Use `Template.from_registry()` instead of listing resources

## Quick Start

```python
from cloudformation_dataclasses.core import Template, cloudformation_dataclass
from cloudformation_dataclasses.aws.s3 import Bucket

# Resources auto-register when defined
@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    bucket_name = "my-bucket"

@cloudformation_dataclass
class LogBucket:
    resource: Bucket
    bucket_name = "my-logs"

# Build template from all registered resources
template = Template.from_registry(description="My Infrastructure")
print(template.to_json())
```

No need to manually list `resources = [MyBucket, LogBucket]` - they're automatically discovered.

## Auto-Registration

Every `@cloudformation_dataclass` that wraps a CloudFormation resource (has a `resource_type` attribute) automatically registers:

```python
@cloudformation_dataclass
class MyTable:
    resource: Table
    table_name = "users"
    # ✓ Registered as "AWS::DynamoDB::Table"

@cloudformation_dataclass
class MyQueue:
    resource: Queue
    queue_name = "orders"
    # ✓ Registered as "AWS::SQS::Queue"
```

**What doesn't register:**
- PropertyTypes (like `BucketEncryption`, `KeySchema`) - they're nested configuration, not top-level resources
- `PolicyDocument`, `PolicyStatement` - these are IAM policy components
- `DeploymentContext` - this is infrastructure configuration, not a CF resource

## Template.from_registry()

Build templates without listing resources manually:

```python
from cloudformation_dataclasses.core import Template

# All registered resources
template = Template.from_registry(
    description="My Application Stack",
    parameters=[EnvironmentParam, BucketNameParam],
    outputs=[TableArnOutput, BucketNameOutput],
)
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `description` | `str` | Template description |
| `context` | `DeploymentContext` | Context for auto-naming and tags (applied to all resources) |
| `parameters` | `list` | Parameter wrapper classes |
| `outputs` | `list` | Output wrapper classes |
| `conditions` | `list` | Condition wrapper classes |
| `mappings` | `list` | Mapping wrapper classes |

### Context Injection

Pass a `DeploymentContext` to automatically apply naming and tags to all resources:

```python
from .context import ctx

template = Template.from_registry(
    description="My Application Stack",
    context=ctx,  # Auto-names resources and applies tags
)
```

This automatically:
- Sets physical names (e.g., `bucket_name`, `function_name`) using the naming pattern
- Merges context tags with resource-specific tags
- Only applies to resources that don't already have a context set

## Querying Resources

Access the registry directly for advanced use cases:

```python
from cloudformation_dataclasses.core import registry
from cloudformation_dataclasses.aws.dynamodb import Table

# Get all registered resources
all_resources = registry.get_all()

# Query by CloudFormation type (class)
tables = registry.get_by_type(Table)

# Query by CloudFormation type (string)
tables = registry.get_by_type("AWS::DynamoDB::Table")

# Get a specific resource by class name
my_table = registry.get_by_name("UsersTable")
```

## Multi-File Organization

Split resources across files - they all register automatically:

```python
# infrastructure/tables.py
@cloudformation_dataclass
class UsersTable:
    resource: Table
    table_name = "users"

@cloudformation_dataclass
class OrdersTable:
    resource: Table
    table_name = "orders"

# infrastructure/queues.py
@cloudformation_dataclass
class OrderQueue:
    resource: Queue
    queue_name = "orders"

# main.py
from infrastructure import tables, queues  # Import triggers registration
from cloudformation_dataclasses.core import Template

template = Template.from_registry(description="My Infrastructure")
# Contains: UsersTable, OrdersTable, OrderQueue
```

## DynamoDB Local Export

Use type-based queries to export only specific resource types:

```python
import json
from cloudformation_dataclasses.core import registry
from cloudformation_dataclasses.aws.dynamodb import Table

# Get only DynamoDB tables (skip autoscaling, IAM, etc.)
for table_cls in registry.get_by_type(Table):
    table = table_cls().resource
    print(json.dumps(table.to_dict()))
```

This is useful for:
- Exporting table definitions for DynamoDB Local
- Generating documentation for specific resource types
- Building partial templates

## Testing

Use `registry.clear()` to isolate tests:

```python
import pytest
from cloudformation_dataclasses.core import registry

@pytest.fixture(autouse=True)
def clear_registry():
    """Clear registry before each test."""
    registry.clear()
    yield
    registry.clear()

def test_my_resources():
    # Define resources - they register fresh
    @cloudformation_dataclass
    class TestBucket:
        resource: Bucket
        bucket_name = "test"

    assert len(registry.get_all()) == 1
```

## Disabling Auto-Registration

For resources you don't want in the registry:

```python
@cloudformation_dataclass(register=False)
class HelperBucket:
    resource: Bucket
    bucket_name = "helper"
    # Not registered - won't appear in Template.from_registry()
```

## API Reference

### `registry.register(wrapper_cls, resource_type)`
Register a wrapper class manually.

### `registry.get_all() -> list[Type]`
Get all registered wrapper classes.

### `registry.get_by_type(resource_type) -> list[Type]`
Get wrapper classes by CloudFormation resource type. Accepts either a class (`Table`) or string (`"AWS::DynamoDB::Table"`).

### `registry.get_by_name(name) -> Type | None`
Get a wrapper class by its class name.

### `registry.clear()`
Clear all registered resources. Useful for test isolation.

### `len(registry)`
Get the count of registered resources.

### `"MyBucket" in registry`
Check if a resource with the given name is registered.
