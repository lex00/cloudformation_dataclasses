# Template

Imported from `LambdaSample.yaml`.

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m template
```

### Validate Template

```bash
python -m template --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `LambdaRole` | AWS::IAM::Role |
| `LambdaFunction` | AWS::Lambda::Function |
