# CompliantBucket

Migrated from [compliant-bucket.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates).

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
uv run python -m compliant_bucket
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `ObjectStorageBucket` | AWS::S3::Bucket |
| `ObjectStorageBucketPolicyPolicy` | AWS::S3::BucketPolicy |
| `ObjectStorageLogBucket` | AWS::S3::Bucket |
| `ObjectStorageLogBucketPolicyPolicy` | AWS::S3::BucketPolicy |
| `ObjectStorageReplicaBucket` | AWS::S3::Bucket |
| `ObjectStorageReplicaBucketPolicyPolicy` | AWS::S3::BucketPolicy |
| `ObjectStorageReplicationPolicy` | AWS::IAM::RolePolicy |
| `ObjectStorageReplicationRole` | AWS::IAM::Role |
