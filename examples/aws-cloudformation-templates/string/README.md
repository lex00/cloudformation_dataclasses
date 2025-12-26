# String

Migrated from [string.json](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m string
```

### Validate Template

```bash
python -m string --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `TransformExecutionRole` | AWS::IAM::Role |
| `TransformFunction` | AWS::Lambda::Function |
| `TransformFunctionPermissions` | AWS::Lambda::Permission |
| `Transform` | AWS::CloudFormation::Macro |
