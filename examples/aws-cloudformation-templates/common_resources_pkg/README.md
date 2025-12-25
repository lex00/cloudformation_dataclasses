# CommonResourcesPkg

Migrated from [common-resources-pkg.json](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m common_resources_pkg
```

### Validate Template

```bash
python -m common_resources_pkg --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `TestQ` | AWS::SQS::Queue |
| `StorageLogBucket` | AWS::S3::Bucket |
| `StorageBucket` | AWS::S3::Bucket |
| `StorageReplicaBucket` | AWS::S3::Bucket |
| `StorageReplicationPolicy` | AWS::IAM::RolePolicy |
| `StorageReplicationRole` | AWS::IAM::Role |
| `StorageLogBucketPolicyPolicy` | AWS::S3::BucketPolicy |
| `StorageBucketPolicyPolicy` | AWS::S3::BucketPolicy |
| `StorageReplicaBucketPolicyPolicy` | AWS::S3::BucketPolicy |
