# IDE Support & Type Checking

cloudformation_dataclasses provides full IDE support through:
- Type annotations on all classes and functions
- Generated `.pyi` stub files for dynamic imports
- Compatibility with Pylance, mypy, and pyright

## Quick Setup

Generate stub files for your stack:

```bash
cfn-dataclasses stubs
```

Or run in watch mode during development:

```bash
cfn-dataclasses stubs --watch
```

## How It Works

### The Challenge

Stack files use `from .. import *` for clean, concise code:

```python
from .. import *  # noqa: F403, F401

@cloudformation_dataclass
class MyBucket:
    resource: s3.Bucket
    bucket_name = ref(BucketNameParam)
```

This works at runtime because `setup_resources()` dynamically loads
modules and injects the namespace. However, static analyzers like
Pylance can't see these dynamic exports.

### The Solution: .pyi Stub Files

The `cfn-dataclasses stubs` command generates `.pyi` type stub files
that declare what's exported:

```
mystack/
├── __init__.py      # Your code
├── __init__.pyi     # Generated stub (declares exports)
└── stack/
    ├── __init__.py
    ├── __init__.pyi  # Generated stub
    ├── params.py
    └── resources.py
```

The stub files tell Pylance/mypy:
- What names are available via star imports
- Type information for all exported classes
- Re-exports from cloudformation_dataclasses

### When to Regenerate

Run `cfn-dataclasses stubs` after:
- Creating new resource classes
- Adding new parameters
- Renaming classes
- Modifying the parent `__init__.py` imports

Or use `--watch` mode for automatic regeneration.

## Watch Mode

Watch mode monitors your stack files and automatically regenerates
stubs when changes are detected:

```bash
cfn-dataclasses stubs --watch
```

Watch mode requires the `watchdog` package:

```bash
pip install watchdog
# or
pip install cloudformation_dataclasses[stubs]
```

## VSCode/Pylance Setup

Pylance should work automatically once stubs are generated. If you
see "unknown" errors:

1. Ensure stubs are generated: `cfn-dataclasses stubs`
2. Reload VSCode window: Cmd/Ctrl+Shift+P → "Reload Window"
3. Check Python interpreter is set to your venv

## Mypy Configuration

Add to `pyproject.toml`:

```toml
[tool.mypy]
python_version = "3.10"
strict = true

# Allow star imports in stack files
[[tool.mypy.overrides]]
module = "*.stack.*"
disable_error_code = ["no-redef"]
```

## Troubleshooting

### "Cannot find module" errors

- Run `cfn-dataclasses stubs` to generate stub files
- Ensure you're in the project root directory

### Stubs out of date

- Run `cfn-dataclasses stubs` again after adding/renaming classes
- Use `--watch` mode during active development

### Star import warnings

Add `# noqa: F403, F401` to suppress flake8/ruff warnings:

```python
from .. import *  # noqa: F403, F401
```

These warnings are expected for the cloudformation_dataclasses pattern.

### Pylance shows "partially unknown" types

Regenerate stubs and reload the VSCode window. If the issue persists,
check that the generated `.pyi` files include your new classes.
