# Example3

Migrated from [example_3.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m example_3
```

### Validate Template

```bash
python -m example_3 --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `Bucket` | AWS::S3::Bucket |
| `Object1` | AWS::S3::Object |
| `Object2` | AWS::S3::Object |
| `Object3` | AWS::S3::Object |
| `Object4` | AWS::S3::Object |
