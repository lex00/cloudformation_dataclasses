# CLI Improvements

**Date**: 2025-12-25
**Status**: DRAFT
**Purpose**: Improve the `cfn-dataclasses` CLI without separating into a different package

---

## Background

Analysis concluded that separating the CLI into its own package is not recommended due to version management complexity and minimal benefits. Instead, this document focuses on improvements to the existing CLI structure.

---

## Current CLI Architecture

### Commands

| Command | Purpose | Dependencies |
|---------|---------|--------------|
| `init` | Create new project skeleton | package_templates/ |
| `import` | Convert CloudFormation YAML/JSON to Python | PyYAML |
| `lint` | Check and auto-fix code style | Core library |
| `split` | Split large files by resource category | AST (stdlib) |
| `stubs` | Generate .pyi files for IDE support | Optional: watchdog |

### Entry Point

```toml
[project.scripts]
cfn-dataclasses = "cloudformation_dataclasses.importer.cli:main"
```

### Current Dependency Structure

```toml
dependencies = []  # Zero runtime dependencies!

[project.optional-dependencies]
importer = ["pyyaml>=6.0"]
stubs = ["watchdog>=3.0"]
```

---

## Improvement 1: Lazy Import PyYAML

**Problem**: CLI code imports `yaml` at module level, requiring PyYAML even when not using the `import` command.

**Solution**: Lazy import PyYAML only when the `import` command runs.

```python
# importer/cli.py

def _run_import_command(args):
    try:
        from cloudformation_dataclasses.importer.parser import parse_template
    except ImportError as e:
        if "yaml" in str(e).lower():
            print("Error: PyYAML required for import command")
            print("Install with: pip install cloudformation-dataclasses[importer]")
            return 1
        raise

    # ... rest of import logic
```

```python
# importer/parser.py

def parse_template(source: str) -> dict:
    try:
        import yaml
    except ImportError:
        raise ImportError(
            "PyYAML required for template parsing.\n"
            "Install with: pip install cloudformation-dataclasses[importer]"
        )

    # ... rest of implementation
```

**Benefits**:
- Core library has zero deps
- CLI available without PyYAML
- Clear error message when PyYAML needed
- `init`, `lint`, `split`, `stubs` work without extras

---

## Improvement 2: Lazy Import Watchdog

**Problem**: `stubs --watch` requires watchdog, but users get confusing error if not installed.

**Solution**: Clear error message when watchdog missing.

```python
# stubs/__init__.py

def watch_and_regenerate(package_path: Path):
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        print("Error: watchdog required for --watch mode")
        print("Install with: pip install cloudformation-dataclasses[stubs]")
        return 1

    # ... rest of implementation
```

---

## Improvement 3: Modular CLI Entry Points

**Current**: Single `cfn-dataclasses` command for all operations.

**Proposed**: Add separate entry points for common commands.

```toml
[project.scripts]
cfn-dataclasses = "cloudformation_dataclasses.importer.cli:main"

# Convenience aliases
cfn-init = "cloudformation_dataclasses.importer.cli:init_main"
cfn-import = "cloudformation_dataclasses.importer.cli:import_main"
cfn-lint = "cloudformation_dataclasses.linter:lint_main"
cfn-stubs = "cloudformation_dataclasses.stubs:stubs_main"
```

**Benefits**:
- Users can use specific tools directly
- Shorter commands for common operations
- Clearer error messages per command
- Easier to make subcommands optional

**Usage**:
```bash
# Either works:
cfn-dataclasses init -o my_stack/
cfn-init -o my_stack/

cfn-dataclasses lint my_stack/
cfn-lint my_stack/
```

---

## Improvement 4: Plugin Architecture (Future)

For extensibility, consider a plugin system where subcommands are auto-discovered.

```python
# Core CLI framework
[project.entry-points."cloudformation_dataclasses.commands"]
init = "cloudformation_dataclasses.importer.cli:InitCommand"
import = "cloudformation_dataclasses.importer.cli:ImportCommand"
lint = "cloudformation_dataclasses.linter:LintCommand"
stubs = "cloudformation_dataclasses.stubs:StubsCommand"
split = "cloudformation_dataclasses.linter:SplitCommand"
```

```python
# cli.py - discovers plugins
import importlib.metadata

def discover_commands():
    commands = {}
    for ep in importlib.metadata.entry_points(group="cloudformation_dataclasses.commands"):
        commands[ep.name] = ep.load()
    return commands

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    for name, command_cls in discover_commands().items():
        cmd = command_cls()
        sub = subparsers.add_parser(name, help=cmd.help)
        cmd.configure_parser(sub)
        sub.set_defaults(func=cmd.run)

    args = parser.parse_args()
    return args.func(args)
```

**Benefits**:
- Third-party plugins possible
- Commands can be optional packages
- Easy to add new commands
- Each command controls its own dependencies

---

## Improvement 5: Startup Time Optimization

**Problem**: CLI startup may be slow due to importing large modules.

**Solutions**:

### 5a. Defer AWS Resource Imports

Don't import `cloudformation_dataclasses.aws` until actually needed:

```python
# Only import aws modules when generating code
def generate_import_statement(resource_type: str) -> str:
    # Parse "AWS::EC2::Instance" -> "ec2"
    service = resource_type.split("::")[1].lower()
    return f"from cloudformation_dataclasses.aws import {service}"
```

### 5b. Cache Expensive Operations

```python
# Cache parsed CloudFormation spec
import functools

@functools.lru_cache(maxsize=1)
def get_cfn_spec():
    # Load and parse spec once
    ...
```

### 5c. Profile and Measure

```bash
# Measure CLI startup time
python -c "import timeit; print(timeit.timeit('import cloudformation_dataclasses.importer.cli', number=1))"
```

---

## Improvement 6: Better Error Messages

**Current**: Some errors are cryptic (e.g., missing dependencies, invalid templates).

**Proposed**: User-friendly error messages with actionable suggestions.

```python
class CLIError(Exception):
    """Base class for CLI errors with user-friendly messages."""

    def __init__(self, message: str, suggestion: str = None):
        self.message = message
        self.suggestion = suggestion
        super().__init__(message)

    def __str__(self):
        if self.suggestion:
            return f"Error: {self.message}\n\nSuggestion: {self.suggestion}"
        return f"Error: {self.message}"

# Usage
raise CLIError(
    "Template contains unsupported intrinsic function: !Transform",
    suggestion="Remove the !Transform macro or manually convert it after import."
)
```

---

## Improvement 7: Progress Indicators

**Problem**: Long operations (import, stubs) appear to hang.

**Proposed**: Add progress output for operations.

```python
def import_template(template_path: Path, output_dir: Path, verbose: bool = False):
    if verbose:
        print(f"Parsing {template_path}...")

    template = parse_template(template_path.read_text())
    resources = list(template.get("Resources", {}).items())

    if verbose:
        print(f"Found {len(resources)} resources")

    for i, (name, resource) in enumerate(resources, 1):
        if verbose:
            print(f"  [{i}/{len(resources)}] {name}: {resource['Type']}")
        # ... process resource

    if verbose:
        print(f"Generated package at {output_dir}")
```

---

## Improvement 8: Dry Run Mode

**Problem**: Users want to preview changes before `lint --fix` or `split` modifies files.

**Proposed**: Add `--dry-run` flag.

```bash
# Preview what lint would fix
cfn-dataclasses lint my_stack/ --fix --dry-run

# Preview file splits
cfn-dataclasses split my_stack/resources.py --dry-run
```

```python
def run_lint(args):
    issues = find_issues(args.path)

    if args.fix:
        if args.dry_run:
            print("Would fix the following issues:")
            for issue in issues:
                print(f"  {issue.file}:{issue.line} - {issue.message}")
            return 0
        else:
            for issue in issues:
                issue.apply_fix()

    return 0 if not issues else 1
```

---

## Improvement 9: Configuration File

**Problem**: CLI options must be repeated on every invocation.

**Proposed**: Support `.cfn-dataclasses.toml` or section in `pyproject.toml`.

```toml
# pyproject.toml
[tool.cfn-dataclasses]
# Default options for all commands
verbose = true

[tool.cfn-dataclasses.lint]
# Lint-specific options
fix = true
rules = ["CFD001", "CFD002", "CFD005"]
ignore = ["CFD012"]

[tool.cfn-dataclasses.stubs]
# Stubs-specific options
watch = false
```

```python
def load_config(project_path: Path) -> dict:
    pyproject = project_path / "pyproject.toml"
    if pyproject.exists():
        import tomllib
        with open(pyproject, "rb") as f:
            data = tomllib.load(f)
        return data.get("tool", {}).get("cfn-dataclasses", {})
    return {}
```

---

## Improvement 10: Shell Completion

**Problem**: No tab completion for commands and options.

**Proposed**: Generate shell completion scripts.

```bash
# Generate completion script
cfn-dataclasses --generate-completion bash > ~/.cfn-dataclasses-complete.bash
source ~/.cfn-dataclasses-complete.bash

# Or use argcomplete
pip install argcomplete
activate-global-python-argcomplete
```

```python
# cli.py
import argparse

try:
    import argcomplete
    HAS_ARGCOMPLETE = True
except ImportError:
    HAS_ARGCOMPLETE = False

def main():
    parser = argparse.ArgumentParser()
    # ... configure parser ...

    if HAS_ARGCOMPLETE:
        argcomplete.autocomplete(parser)

    args = parser.parse_args()
    # ...
```

---

## Implementation Priority

| Improvement | Impact | Effort | Priority |
|-------------|--------|--------|----------|
| 1. Lazy PyYAML | High | Low | P0 |
| 2. Lazy Watchdog | Medium | Low | P0 |
| 6. Better Errors | High | Medium | P1 |
| 8. Dry Run | Medium | Low | P1 |
| 7. Progress | Medium | Low | P2 |
| 3. Entry Points | Low | Low | P2 |
| 9. Config File | Medium | Medium | P3 |
| 5. Startup Time | Low | Medium | P3 |
| 10. Completion | Low | Low | P3 |
| 4. Plugins | Low | High | Future |

---

## Summary

Focus on quick wins first:
1. **Lazy imports** - Make PyYAML/watchdog truly optional with clear error messages
2. **Better errors** - User-friendly messages with actionable suggestions
3. **Dry run mode** - Preview changes before modifying files

These improvements enhance the CLI without the complexity of package separation.
