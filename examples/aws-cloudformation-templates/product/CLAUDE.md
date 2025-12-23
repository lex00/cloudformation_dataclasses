# Product

CloudFormation infrastructure using cloudformation_dataclasses.

## Key Patterns

1. **Wrapper classes** with `@cloudformation_dataclass` decorator
2. **DeploymentContext** for consistent naming
3. **Type-safe enums** - use enum values, not strings
4. **ref() for references** - `ref(MyResource)`, not string literals

## Commands

```bash
# Generate template
python -m product.main

# Type check
mypy product/

# Run tests
pytest product/tests/
```

## Validation

```python
template = Template.from_registry()
errors = template.validate()
assert errors == []
```

## Adding Resources

1. Create wrapper class in new file
2. Import in `__init__.py`
3. Instantiate in `main.py` before `Template.from_registry()`
