# LambdaIotTopicrule

Imported from `RDS_PIOPS.yaml`.

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
uv run python -m lambda_iot_topicrule
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `DBCredential` | AWS::SecretsManager::Secret |
| `myDB` | AWS::RDS::DBInstance |
