# S3Bucket

CloudFormation infrastructure using cloudformation_dataclasses.

## Key Patterns

1. **Wrapper classes** with `@cloudformation_dataclass` decorator
2. **Template-level context** - pass `context=ctx` to `Template.from_registry()`
3. **Type-safe enums** - use enum values, not strings
4. **ref() for references** - `ref(MyResource)`, not string literals

## Context

Context is applied at the template level:

```python
# main.py
Template.from_registry(
    description='...',
    context=ctx,  # Auto-names resources and applies tags
)
```

This automatically:
- Sets physical names (e.g., `bucket_name`) from the naming pattern
- Merges context tags with resource-specific tags

## Commands

```bash
# Generate template
python -m s3_bucket.main

# Type check
mypy s3_bucket/

# Run tests
pytest tests/
```

## Adding Resources

1. Create wrapper class in `resources/` directory
2. Import in `resources/__init__.py`
3. Resource auto-registers and gets context from template
