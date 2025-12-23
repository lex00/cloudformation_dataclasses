"""Compute resources: TestResourceHandler, TestResourcePermission, TestResourceRootPermission, JwtResourceHandler, JwtResourcePermission, JwtResourceRootPermission."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TestResourceHandlerContent:
    resource: lambda_.layer_version.Content
    s3_bucket = ref(LambdaCodeS3Bucket)
    s3_key = ref(LambdaCodeS3Key)


@cloudformation_dataclass
class TestResourceHandlerEnvironment:
    resource: lambda_.function.Environment
    variables = {
        'TABLE_NAME': ref(TestTable),
    }


@cloudformation_dataclass
class TestResourceHandler:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    handler = 'bootstrap'
    function_name = Sub('${AppName}-test-handler')
    runtime = 'provided.al2023'
    code = TestResourceHandlerContent
    role = get_att(TestResourceHandlerRole, "Arn")
    environment = TestResourceHandlerEnvironment


@cloudformation_dataclass
class TestResourcePermission:
    """AWS::Lambda::Permission resource."""

    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = get_att(TestResourceHandler, "Arn")
    principal = 'apigateway.amazonaws.com'
    source_arn = Sub('arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/*')


@cloudformation_dataclass
class TestResourceRootPermission:
    """AWS::Lambda::Permission resource."""

    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = get_att(TestResourceHandler, "Arn")
    principal = 'apigateway.amazonaws.com'
    source_arn = Sub('arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/')


@cloudformation_dataclass
class JwtResourceHandlerContent:
    resource: lambda_.layer_version.Content
    s3_bucket = 'rain-artifacts-207567786752-us-east-1'
    s3_key = '15d7c92b571beed29cf6c012a96022482eee1df1b477ad528ddc03a4be52c076'


@cloudformation_dataclass
class JwtResourceHandlerEnvironment:
    resource: lambda_.function.Environment
    variables = {
        'COGNITO_REGION': 'us-east-1',
        'COGNITO_POOL_ID': ref(CognitoUserPool),
        'COGNITO_REDIRECT_URI': Sub('https://${SiteDistribution.DomainName}/index.html'),
        'COGNITO_DOMAIN_PREFIX': ref(AppName),
        'COGNITO_APP_CLIENT_ID': ref(CognitoClient),
    }


@cloudformation_dataclass
class JwtResourceHandler:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    handler = 'bootstrap'
    function_name = Sub('${AppName}-jwt-handler')
    runtime = 'provided.al2023'
    code = JwtResourceHandlerContent
    role = get_att(JwtResourceHandlerRole, "Arn")
    environment = JwtResourceHandlerEnvironment


@cloudformation_dataclass
class JwtResourcePermission:
    """AWS::Lambda::Permission resource."""

    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = get_att(JwtResourceHandler, "Arn")
    principal = 'apigateway.amazonaws.com'
    source_arn = Sub('arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/*')


@cloudformation_dataclass
class JwtResourceRootPermission:
    """AWS::Lambda::Permission resource."""

    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = get_att(JwtResourceHandler, "Arn")
    principal = 'apigateway.amazonaws.com'
    source_arn = Sub('arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/')
