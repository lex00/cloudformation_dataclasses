# Compliant S3 Bucket

Migrated from [S3/compliant-bucket.yaml](https://github.com/awslabs/aws-cloudformation-templates/blob/main/S3/compliant-bucket.yaml).

**Original Author/Source**: AWS Labs (Apache-2.0)

## Description

A secure bucket that passes default security scanning checks. Includes:
- Main bucket with replication enabled
- Replica bucket for cross-region/account replication
- Access log bucket with object lock
- Bucket policies requiring secure transport (HTTPS)
- IAM role for S3 replication

## Features Demonstrated

- `@cloudformation_dataclass` wrapper pattern
- `Bucket` and `BucketPolicy` resources
- `ServerSideEncryption.AES256` enum for SSE configuration
- `BucketVersioningStatus.ENABLED` enum for versioning
- `BOOL`, `ARN_LIKE`, `STRING_EQUALS` condition operators
- `Sub()` intrinsic with pseudo-parameters
- `ref()` and `get_att()` for cross-resource references
- `AWS_ACCOUNT_ID` pseudo-parameter constant
- IAM role with assume role policy

## Run Tests

```bash
uv run pytest examples/generated/aws_cloudformation_templates/S3/compliant_bucket/tests/ -v
```

## Generate Template

```bash
uv run python -m examples.generated.aws_cloudformation_templates.S3.compliant_bucket.main
```

## Resources Created

| Resource | Type | Description |
|----------|------|-------------|
| ObjectStorageBucket | AWS::S3::Bucket | Main bucket with replication |
| ObjectStorageLogBucket | AWS::S3::Bucket | Access log bucket with object lock |
| ObjectStorageReplicaBucket | AWS::S3::Bucket | Replication target bucket |
| ObjectStorageBucketPolicyPolicy | AWS::S3::BucketPolicy | Requires HTTPS for main bucket |
| ObjectStorageLogBucketPolicyPolicy | AWS::S3::BucketPolicy | Requires HTTPS for log bucket |
| ObjectStorageReplicaBucketPolicyPolicy | AWS::S3::BucketPolicy | Requires HTTPS for replica bucket |
| ObjectStorageReplicationRole | AWS::IAM::Role | Role for S3 replication |
| ObjectStorageReplicationPolicy | AWS::IAM::RolePolicy | Policy for replication permissions |
