# Generated Stack Package Restructuring

**Date:** 2025-12-25
**Status:** IMPLEMENTED
**Focus:** Flattening the structure of packages created by `cfn-dataclasses init` and `cfn-dataclasses import`

---

## Implementation Status

**Date Implemented:** 2025-12-25

All proposed changes have been implemented:
- ✅ Resources now live directly in package root (no `stack/` subfolder)
- ✅ Single `__init__.py` with `setup_resources()` call
- ✅ Single `__init__.pyi` stub file
- ✅ `__main__.py` uses `run_package_cli()` instead of custom main.py
- ✅ No generated tests/ directory
- ✅ Import pattern is `from . import *` not `from .. import *`

---

## Original Proposal

---

## Current Generated Package Structure

When you run `cfn-dataclasses init -o fargate` or import a template, you get:

```
fargate/                      # Project root
├── pyproject.toml
├── fargate/                  # Package (same name as project)
│   ├── __init__.py          # Imports + AWS modules
│   ├── __init__.pyi         # IDE stubs
│   ├── __main__.py          # python -m fargate
│   ├── main.py              # build_template()
│   └── stack/               # Nested subpackage for resources
│       ├── __init__.py      # setup_resources() magic
│       ├── __init__.pyi     # Resource stubs
│       ├── params.py        # Parameters
│       ├── outputs.py       # Outputs
│       ├── compute.py       # Resources by category
│       ├── network.py
│       ├── security.py
│       └── monitoring.py
└── tests/
    └── test_fargate.py
```

**Current import pattern:**
```python
# In fargate/__init__.py
from cloudformation_dataclasses.core import *  # noqa: F403, F401
from cloudformation_dataclasses.aws import ec2, ecs, iam
from .stack import *  # noqa: F403, F401

# In fargate/stack/__init__.py
from .params import *  # noqa: F403, F401
from cloudformation_dataclasses.core.resource_loader import setup_resources
setup_resources(__file__, __name__, globals())
from .outputs import *  # noqa: F403, F401
```

**Problems with current structure:**
1. `stack/` subdirectory adds an extra nesting level
2. Two `__init__.py` files with complex import logic
3. Two `__init__.pyi` files to maintain
4. `from .stack import *` then `from .. import *` is confusing
5. Generated `tests/` directory with boilerplate that duplicates framework validation
6. Generated `main.py` with boilerplate that can be abstracted into the framework

---

## Proposed Flattened Structure

Eliminate `stack/` subdirectory. Resource files live directly in the package:

```
fargate/                      # Project root
├── .gitignore
├── .vscode/
│   └── settings.json
├── CLAUDE.md
├── py.typed
├── pyproject.toml
├── README.md
└── fargate/                  # Package (resources live here directly)
    ├── __init__.py           # Core imports + setup_resources()
    ├── __init__.pyi          # Single stub file
    ├── __main__.py           # python -m fargate (uses framework CLI)
    ├── params.py             # Parameters
    ├── outputs.py            # Outputs
    ├── compute.py            # Resources by category
    ├── network.py
    ├── security.py
    └── monitoring.py
```

No `tests/` directory or `main.py` - both are provided by the framework (see below).

**Flattened import pattern:**
```python
# In fargate/__init__.py
from cloudformation_dataclasses.core import *  # noqa: F403, F401
from cloudformation_dataclasses.aws import ec2, ecs, iam, logs
from cloudformation_dataclasses.core.resource_loader import setup_resources
setup_resources(__file__, __name__, globals())
```

**In resource files (e.g., fargate/compute.py):**
```python
from . import *  # noqa: F403, F401

# ... resource definitions
```

---

## Key Changes

### 1. Eliminate `stack/` Subdirectory

**Before:** `fargate/fargate/stack/compute.py`
**After:** `fargate/fargate/compute.py`

Resource files move up one level into the package directory. Project root structure unchanged.

### 2. Keep `setup_resources()` - It Does the Work

`setup_resources()` handles:
- Discovering resource files in the package directory
- Loading them in topological (dependency) order
- Populating the module's namespace

Users don't need to think about import ordering - the function handles it.

### 3. Single Asterisk Import in Resource Files

**Before (in stack/compute.py):**
```python
from .. import *  # noqa: F403, F401
```

**After (in compute.py):**
```python
from . import *  # noqa: F403, F401
```

One level, not two.

### 4. Single Stub File

**Before:** Two `.pyi` files (`fargate/__init__.pyi` + `fargate/stack/__init__.pyi`)

**After:** One `.pyi` file (`fargate/__init__.pyi`) in the package

---

## How `setup_resources()` Works

```python
# fargate/__init__.py
from cloudformation_dataclasses.core import *  # noqa: F403, F401
from cloudformation_dataclasses.aws import ec2, ecs, iam, logs
from cloudformation_dataclasses.core.resource_loader import setup_resources
setup_resources(__file__, __name__, globals())
```

`setup_resources()`:
1. Finds all `.py` files in the package directory (excluding `__init__.py`, `__main__.py`, `main.py`)
2. Analyzes dependencies between resources
3. Loads files in topological order
4. Exports all resources to the package namespace

---

## Will Star Imports Still Work?

**Yes.** The pattern is simpler:

```python
# User code
from fargate import *
# Gets: all params, all resources, all outputs, all core types

from fargate import VpcIdParam, EcsCluster, WebService
# Direct imports work

from fargate import ec2, ecs
# AWS modules still available
```

---

## Implementation Changes Required

### 1. Update `cfn-dataclasses init`

Modify the init command to generate the flat structure:
- Generate resource files directly in package directory (no `stack/` subdirectory)
- Single `__init__.py` with `setup_resources()` call
- Single `__init__.pyi` stub

### 2. Update `cfn-dataclasses import`

Modify package generation in `codegen/package.py`:
- Generate resource files directly in package directory
- No `stack/` subdirectory
- `setup_resources()` handles import ordering at runtime

### 3. Update `cfn-dataclasses stubs`

Modify stub generation:
- Generate single `.pyi` file in package directory
- No `stack/__init__.pyi`

### 4. Update `cfn-dataclasses lint --fix` (CFD012)

When splitting a large file:
- Create category files in package directory
- `setup_resources()` will discover them automatically

### 5. Update `setup_resources()`

Adapt to work at package level (instead of `stack/` sublevel):
- Exclude `main.py`, `__main__.py`, etc.

### 6. Abstract `main.py` into Framework

Currently each package has a `main.py` with boilerplate:

```python
# Current main.py - mostly boilerplate
def build_template() -> Template:
    template = Template.from_registry(description="...")
    template.add_parameter("VpcId", VpcIdParam)
    template.add_parameter("PrivateSubnetIds", PrivateSubnetIdsParam)
    # ... add each param/output explicitly
    return template
```

Since `setup_resources()` already registers all resources, params, and outputs, the framework can build the template automatically:

```python
# New __main__.py - just calls framework
from cloudformation_dataclasses import run_package_cli
run_package_cli(__name__, description="Fargate stack - ECS service")
```

**`run_package_cli()` provides:**
- `python -m fargate` → output JSON
- `python -m fargate --yaml` → output YAML
- `python -m fargate --validate` → run validation checks
- `python -m fargate --diff` → compare against deployed stack (future)

**For custom build logic**, users can still define their own `build_template()`:

```python
# Custom __main__.py
from cloudformation_dataclasses import run_package_cli

def build_template() -> Template:
    # Custom logic here
    ...

run_package_cli(__name__, build_fn=build_template)
```

### 7. Remove Generated `tests/` Directory

Replace with framework-provided validation (via `--validate` flag above):

**Framework-provided validation checks:**
- Template builds successfully
- Output is valid CloudFormation JSON/YAML
- All `Ref()` and `GetAtt()` targets exist
- No circular dependencies
- Resource names are unique
- Required parameters have values or defaults

Users who want custom tests can add their own `tests/` directory.

---

## Migration Path for Existing Projects

### Option A: Manual Migration

1. Move files from `package/stack/` to `package/`
2. Update imports in resource files (`from .. import *` → `from . import *`)
3. Update `package/__init__.py` to call `setup_resources()` directly
4. Delete `stack/` directory
5. Regenerate stubs with `cfn-dataclasses stubs`

### Option B: CLI Migration Command

```bash
cfn-dataclasses migrate --flatten
```

This could:
1. Detect `stack/` subdirectory
2. Move resource files up to package directory
3. Update imports in resource files
4. Update `__init__.py`
5. Regenerate stubs

---

## Comparison

| Aspect | Current | Proposed |
|--------|---------|----------|
| Resource file path | `project/package/stack/file.py` | `project/package/file.py` |
| `__init__.py` files in package | 2 (`package/` + `stack/`) | 1 (`package/` only) |
| `.pyi` stub files | 2 | 1 |
| Import in resources | `from .. import *` | `from . import *` |
| Resource discovery | `setup_resources()` | `setup_resources()` |
| Package subdirectories | `stack/` | None |
| `main.py` | Generated boilerplate | Framework-provided via `run_package_cli()` |
| Testing | Generated `tests/` directory | Framework-provided validation |

---

## Risks and Mitigations

### Risk: Breaking Existing Projects

**Mitigation:**
- Existing nested structure continues to work
- New structure only for new projects
- Provide migration tooling

### Risk: File Clutter in Package Directory

**Mitigation:**
- Only resource files + standard package files
- Clear naming conventions (params.py, outputs.py, etc.)

---

## Recommendation

**Proceed with flattening.**

1. **Phase 1:** Update `init` and `import` to generate flat structure
2. **Phase 2:** Update `setup_resources()` to work at package level
3. **Phase 3:** Update stub generator for flat structure
4. **Phase 4:** Add `run_package_cli()` to replace `main.py` boilerplate
5. **Phase 5:** Add `migrate --flatten` command

**Benefits:**
- Simpler structure - no `stack/` subdirectory
- Single `__init__.py` and `.pyi` in package
- `setup_resources()` still handles the complexity
- Resource files just need `from . import *`
- No generated `main.py` boilerplate - `run_package_cli()` handles it
- No generated test boilerplate - validation built into framework CLI

---

## Open Questions

1. **Should we auto-migrate existing projects?**
   - Probably not - too risky
   - Provide tooling, let users opt-in

2. **What about very large templates?**
   - Same category-based splitting, just at package level instead of `stack/` level
