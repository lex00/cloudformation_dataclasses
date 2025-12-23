# Windows1

CloudFormation infrastructure using cloudformation_dataclasses.

## Key Patterns

1. **Wrapper classes** with `@cloudformation_dataclass` decorator
2. **DeploymentContext** for consistent naming
3. **Type-safe enums** - use enum values, not strings
4. **ref() for references** - `ref(MyResource)`, not string literals

## Commands

```bash
# Generate template
python -m windows_1.main

# Type check
mypy windows_1/

# Run tests
pytest windows_1/tests/
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
