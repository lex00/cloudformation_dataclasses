# CompliantStaticWebsite

Migrated from [compliant-static-website.yaml](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m compliant_static_website
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `CloudFrontLogsBucket` | AWS::S3::Bucket |
| `CloudFrontLogsBucketPolicyPolicy` | AWS::S3::BucketPolicy |
| `CloudFrontLogsLogBucket` | AWS::S3::Bucket |
| `CloudFrontLogsLogBucketPolicyPolicy` | AWS::S3::BucketPolicy |
| `CloudFrontLogsReplicaBucket` | AWS::S3::Bucket |
| `CloudFrontLogsReplicaBucketPolicyPolicy` | AWS::S3::BucketPolicy |
| `CloudFrontLogsReplicationPolicy` | AWS::IAM::RolePolicy |
| `CloudFrontLogsReplicationRole` | AWS::IAM::Role |
| `ContentBucket` | AWS::S3::Bucket |
| `ContentBucketPolicyPolicy` | AWS::S3::BucketPolicy |
| `ContentLogBucket` | AWS::S3::Bucket |
| `ContentLogBucketPolicyPolicy` | AWS::S3::BucketPolicy |
| `ContentReplicaBucket` | AWS::S3::Bucket |
| `ContentReplicaBucketPolicyPolicy` | AWS::S3::BucketPolicy |
| `ContentReplicationPolicy` | AWS::IAM::RolePolicy |
| `ContentReplicationRole` | AWS::IAM::Role |
| `Distribution` | AWS::CloudFront::Distribution |
| `OriginAccessControl` | AWS::CloudFront::OriginAccessControl |
