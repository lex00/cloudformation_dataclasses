# Macro5

Migrated from [macro_5.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m macro_5
```

### Validate Template

```bash
python -m macro_5 --validate
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
