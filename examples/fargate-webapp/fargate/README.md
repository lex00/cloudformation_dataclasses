# Fargate

CloudFormation infrastructure as Python code.

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
uv run python -m fargate
```

### Install as Dependency

```bash
pip install .
```
