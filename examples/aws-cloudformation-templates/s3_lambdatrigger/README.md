# S3Lambdatrigger

Migrated from [S3_LambdaTrigger.yaml](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m s3_lambdatrigger
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `S3TriggerLambdaFunction` | AWS::Lambda::Function |
| `LambdaInvokePermission` | AWS::Lambda::Permission |
| `LambdaIAMRole` | AWS::IAM::Role |
| `S3BucketNotification` | AWS::S3::Bucket |
