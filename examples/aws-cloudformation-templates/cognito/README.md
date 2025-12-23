# Cognito

Migrated from [cognito.yml](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m cognito
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `UserPool` | AWS::Cognito::UserPool |
| `Domain` | AWS::Cognito::UserPoolDomain |
| `Client` | AWS::Cognito::UserPoolClient |
