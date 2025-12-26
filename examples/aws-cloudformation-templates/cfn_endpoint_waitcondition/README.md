# CfnEndpointWaitcondition

Imported from `destination.yaml`.

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m cfn_endpoint_waitcondition
```

### Validate Template

```bash
python -m cfn_endpoint_waitcondition --validate
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
