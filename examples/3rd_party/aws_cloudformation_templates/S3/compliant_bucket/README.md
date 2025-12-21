# Compliant Bucket

Migrated from [compliant-bucket.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/S3/compliant-bucket.yaml).

**Original Author/Source**: AWS CloudFormation Templates (Apache-2.0)

A secure S3 bucket that passes default security scanning checks. Includes:
- A primary bucket with replication enabled
- A replica bucket in the same region
- An access log bucket
- Server-side encryption (AES256)
- Public access blocked
- Bucket policies requiring secure transport
- Object lock with COMPLIANCE retention

## Versions

This example is generated in 2 different styles to demonstrate the importer's output modes:

| Folder | Mode | Description |
|--------|------|-------------|
| `block/` | block | Wrapper classes for all PropertyTypes (maximum type safety) |
| `mixed/` | mixed | Wrapper classes for resources, inline dicts for PropertyTypes |

### Which version to use?

- **block**: Recommended for production use - maximum type safety with wrapper classes for everything
- **mixed**: Good balance of readability and conciseness - fewer files, inline PropertyTypes

## Features Demonstrated

- `get_att()` with `ARN` constant for type-safe attribute access
- `ref()` for resource references (auto-detected from implicit refs)
- `Join()` for ARN wildcard patterns (e.g., `bucket-arn/*`)
- `BucketVersioningStatus` enum for versioning configuration
- `ServerSideEncryption` enum for SSE algorithm
- Nested PolicyDocument with DenyStatement and PolicyStatement
- Cross-resource dependencies (bucket policies, replication role)

## Run Tests

```bash
uv run pytest examples/3rd_party/aws_cloudformation_templates/S3/compliant_bucket/tests/ -v
```

## Generate Template

```bash
# Both versions produce the same CloudFormation output
uv run python -m examples.3rd_party.aws_cloudformation_templates.S3.compliant_bucket.block.main
uv run python -m examples.3rd_party.aws_cloudformation_templates.S3.compliant_bucket.mixed.main
```

## Resources

| Logical ID | Type | Description |
|------------|------|-------------|
| `AppName` | Parameter | Application name prefix for resource naming |
| `ObjectStorageBucket` | AWS::S3::Bucket | Primary bucket with replication |
| `ObjectStorageLogBucket` | AWS::S3::Bucket | Access log bucket |
| `ObjectStorageReplicaBucket` | AWS::S3::Bucket | Replication destination bucket |
| `ObjectStorageBucketPolicyPolicy` | AWS::S3::BucketPolicy | Policy for primary bucket |
| `ObjectStorageLogBucketPolicyPolicy` | AWS::S3::BucketPolicy | Policy for log bucket |
| `ObjectStorageReplicaBucketPolicyPolicy` | AWS::S3::BucketPolicy | Policy for replica bucket |
| `ObjectStorageReplicationRole` | AWS::IAM::Role | IAM role for replication |
| `ObjectStorageReplicationPolicy` | AWS::IAM::RolePolicy | Policy for replication role |
