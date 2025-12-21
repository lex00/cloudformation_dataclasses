# RdsPiops

Migrated from [RDS_PIOPS.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

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
uv run python -m rds_piops
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
