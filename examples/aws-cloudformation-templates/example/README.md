# Example

Imported from `macro_5.yaml`.

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
uv run python -m example
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `ResourceFunction` | AWS::Serverless::Function |
| `MacroFunction` | AWS::Serverless::Function |
| `Macro` | AWS::CloudFormation::Macro |
| `Dashboard` | AWS::CloudWatch::Dashboard |
