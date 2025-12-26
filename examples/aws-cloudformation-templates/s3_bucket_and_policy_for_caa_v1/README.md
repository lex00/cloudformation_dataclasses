# S3BucketAndPolicyForCaaV1

Migrated from [s3-bucket-and-policy-for-caa-v1.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m s3_bucket_and_policy_for_caa_v1
```

### Validate Template

```bash
python -m s3_bucket_and_policy_for_caa_v1 --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `Bucket` | AWS::S3::Bucket |
| `BucketPolicy` | AWS::S3::BucketPolicy |
