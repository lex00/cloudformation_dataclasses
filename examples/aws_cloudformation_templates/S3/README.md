# S3 CloudFormation Examples

Migrated from [aws-cloudformation-templates/S3](https://github.com/awslabs/aws-cloudformation-templates/tree/main/S3).

## Examples

### cross_account_access.py

S3 bucket with cross-account access policy.

**Original:** `s3-bucket-and-policy-for-caa-v1.yaml`

**Features demonstrated:**
- S3 Bucket with AES256 encryption and versioning
- `PublicAccessBlockConfiguration` for security
- `BucketPolicy` with cross-account IAM statements
- `Sub` intrinsic with `${AWS::Partition}` pseudo-parameter
- Policy conditions (deny non-HTTPS requests)
- `DeploymentContext` for resource naming and tagging

**Run tests:**
```bash
uv run pytest examples/aws_cloudformation_templates/S3/tests/ -v
```

**Generate template:**
```bash
uv run python -m examples.aws_cloudformation_templates.S3.cross_account_access
```
