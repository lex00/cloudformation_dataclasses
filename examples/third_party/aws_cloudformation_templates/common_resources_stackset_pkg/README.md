# CommonResourcesStacksetPkg

Imported from `common-resources-stackset-pkg.json`.

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Run Tests

```bash
uv run pytest tests/ -v
```

### Generate Template

```bash
uv run python -m common_resources_stackset_pkg
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `StackSet` | AWS::CloudFormation::StackSet |
