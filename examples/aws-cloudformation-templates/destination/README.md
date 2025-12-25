# Destination

Migrated from [destination.yaml](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m destination
```

### Validate Template

```bash
python -m destination --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `KmsKey` | AWS::KMS::Key |
| `KmsKeyAlias` | AWS::KMS::Alias |
| `S3BucketDestination` | AWS::S3::Bucket |
| `S3BucketDestinationPolicy` | AWS::S3::BucketPolicy |
