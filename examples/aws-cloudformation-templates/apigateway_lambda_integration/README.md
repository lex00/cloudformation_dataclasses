# ApigatewayLambdaIntegration

Migrated from [apigateway_lambda_integration.json](https://github.com/aws-cloudformation/cfn-lint).

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
uv run python -m apigateway_lambda_integration
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
