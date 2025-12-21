# Cross-Account Access

Migrated from [s3-bucket-and-policy-for-caa-v1.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/S3/s3-bucket-and-policy-for-caa-v1.yaml).

**Original Author/Source**: AWS CloudFormation Templates (Apache-2.0)

An S3 bucket with a bucket policy enabling cross-account access from another AWS account.

## Features Demonstrated

- Parameters for bucket name and cross-account ID
- `ref()` with string references (no cross-module imports)
- `Sub()` for ARN patterns with parameters
- Multiple policy statements (Allow + Deny)
- Cross-account IAM principal patterns
- Secure transport enforcement (deny non-HTTPS)
- Outputs with `ref()` references

## Run Tests

```bash
uv run pytest examples/third_party/aws_cloudformation_templates/S3/cross_account_access/tests/ -v
```

## Generate Template

```bash
uv run python -m third_party.aws_cloudformation_templates.S3.cross_account_access.main
```

## Resources

| Logical ID | Type | Description |
|---|---|---|
| `BucketName` | Parameter | Name for the S3 bucket |
| `PublisherAccountID` | Parameter | AWS account ID to grant access |
| `Bucket` | AWS::S3::Bucket | S3 bucket with encryption and versioning |
| `BucketPolicy` | AWS::S3::BucketPolicy | Policy with cross-account access + secure transport |
| `BucketOutput` | Output | S3 bucket name |
| `BucketPolicyOutput` | Output | Bucket policy name |
