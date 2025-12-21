# Lambda Trigger

Migrated from [S3_LambdaTrigger.yaml](https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/S3/S3_LambdaTrigger.yaml).

**Original Author/Source**: AWS CloudFormation Templates (Apache-2.0)

A Lambda function that is triggered when objects are uploaded to an S3 bucket.

## Features Demonstrated

- Lambda function with inline Python code
- IAM role with CloudWatch Logs permissions
- Lambda permission for S3 invocation
- S3 bucket with notification configuration
- `depends_on` with class references (not strings)

## Run Tests

```bash
uv run pytest examples/third_party/aws_cloudformation_templates/S3/lambda_trigger/tests/ -v
```

## Generate Template

```bash
uv run python -m third_party.aws_cloudformation_templates.S3.lambda_trigger.main
```

## Resources

| Logical ID | Type | Description |
|---|---|---|
| `LambdaIAMRole` | AWS::IAM::Role | Lambda execution role with CloudWatch Logs permissions |
| `S3TriggerLambdaFunction` | AWS::Lambda::Function | Lambda function triggered by S3 events |
| `LambdaInvokePermission` | AWS::Lambda::Permission | Permission for S3 to invoke Lambda |
| `S3BucketNotification` | AWS::S3::Bucket | S3 bucket with Lambda notification |
