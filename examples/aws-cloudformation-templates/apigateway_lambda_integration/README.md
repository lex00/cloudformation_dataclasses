# ApigatewayLambdaIntegration

Migrated from [apigateway_lambda_integration.json](https://github.com/aws-cloudformation/cfn-lint).

**Source**: AWS CloudFormation Sample Templates
**License**: Apache-2.0

**Requires [uv](https://docs.astral.sh/uv/getting-started/installation/)**

## Usage

This is a portable Python package. You can copy this folder into another
project and use it directly.

### Generate Template

```bash
python -m apigateway_lambda_integration
```

### Validate Template

```bash
python -m apigateway_lambda_integration --validate
```

### Install as Dependency

```bash
pip install .
```

## Resources

| Logical ID | Type |
|------------|------|
| `RestApi` | AWS::ApiGateway::RestApi |
| `ApiResource` | AWS::ApiGateway::Resource |
| `RequestModel` | AWS::ApiGateway::Model |
| `ApiMethod` | AWS::ApiGateway::Method |
| `LambdaFunction` | AWS::Lambda::Function |
| `LambdaIamRole` | AWS::IAM::Role |
| `LambdaApiGatewayInvoke` | AWS::Lambda::Permission |
