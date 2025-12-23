# Webapp

Migrated from [webapp.yaml](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m webapp
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `TestResourceHandlerPolicy` | AWS::IAM::RolePolicy |
| `TestTable` | AWS::DynamoDB::Table |
| `SiteOriginAccessControl` | AWS::CloudFront::OriginAccessControl |
| `SiteDistribution` | AWS::CloudFront::Distribution |
| `SiteWebACL` | AWS::WAFv2::WebACL |
| `SiteContentLogBucket` | AWS::S3::Bucket |
| `SiteContentBucket` | AWS::S3::Bucket |
| `SiteContentReplicaBucket` | AWS::S3::Bucket |
| `SiteContentReplicationPolicy` | AWS::IAM::RolePolicy |
| `SiteContentReplicationRole` | AWS::IAM::Role |
| `SiteContentLogBucketAccessPolicy` | AWS::S3::BucketPolicy |
| `SiteContentBucketAccessPolicy` | AWS::S3::BucketPolicy |
| `SiteContentReplicaBucketAccessPolicy` | AWS::S3::BucketPolicy |
| `SiteCloudFrontLogsLogBucket` | AWS::S3::Bucket |
| `SiteCloudFrontLogsBucket` | AWS::S3::Bucket |
| `SiteCloudFrontLogsReplicaBucket` | AWS::S3::Bucket |
| `SiteCloudFrontLogsReplicationPolicy` | AWS::IAM::RolePolicy |
| `SiteCloudFrontLogsReplicationRole` | AWS::IAM::Role |
| `SiteCloudFrontLogsLogBucketAccessPolicy` | AWS::S3::BucketPolicy |
| `SiteCloudFrontLogsBucketAccessPolicy` | AWS::S3::BucketPolicy |
| `SiteCloudFrontLogsReplicaBucketAccessPolicy` | AWS::S3::BucketPolicy |
| `CognitoUserPool` | AWS::Cognito::UserPool |
| `CognitoDomain` | AWS::Cognito::UserPoolDomain |
| `CognitoClient` | AWS::Cognito::UserPoolClient |
| `TestResourceHandler` | AWS::Lambda::Function |
| `TestResourceHandlerRole` | AWS::IAM::Role |
| `TestResourceResource` | AWS::ApiGateway::Resource |
| `TestResourcePermission` | AWS::Lambda::Permission |
| `TestResourceRootPermission` | AWS::Lambda::Permission |
| `TestResourceOptions` | AWS::ApiGateway::Method |
| `TestResourceGet` | AWS::ApiGateway::Method |
| `JwtResourceHandler` | AWS::Lambda::Function |
| `JwtResourceHandlerRole` | AWS::IAM::Role |
| `JwtResourceResource` | AWS::ApiGateway::Resource |
| `JwtResourcePermission` | AWS::Lambda::Permission |
| `JwtResourceRootPermission` | AWS::Lambda::Permission |
| `JwtResourceOptions` | AWS::ApiGateway::Method |
| `JwtResourceGet` | AWS::ApiGateway::Method |
| `RestApi` | AWS::ApiGateway::RestApi |
| `RestApiDeployment` | AWS::ApiGateway::Deployment |
| `RestApiStage` | AWS::ApiGateway::Stage |
| `RestApiAuthorizer` | AWS::ApiGateway::Authorizer |
