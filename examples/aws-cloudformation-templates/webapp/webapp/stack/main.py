"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class RestApi:
    """AWS::ApiGateway::RestApi resource."""

    resource: apigateway.RestApi
    name = ref(AppName)


@cloudformation_dataclass
class TestResourceResource:
    """AWS::ApiGateway::Resource resource."""

    resource: apigateway.Resource
    parent_id = Sub('${RestApi.RootResourceId}')
    path_part = 'test'
    rest_api_id = ref(RestApi)


@cloudformation_dataclass
class TestResourceOptionsIntegration:
    resource: apigateway.method.Integration
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${TestResourceHandler.Arn}/invocations')


@cloudformation_dataclass
class TestResourceOptions:
    """AWS::ApiGateway::Method resource."""

    resource: apigateway.Method
    http_method = 'OPTIONS'
    resource_id = ref(TestResourceResource)
    rest_api_id = ref(RestApi)
    authorization_type = 'NONE'
    integration = TestResourceOptionsIntegration


@cloudformation_dataclass
class RestApiAuthorizer:
    """AWS::ApiGateway::Authorizer resource."""

    resource: apigateway.Authorizer
    identity_source = 'method.request.header.authorization'
    name = 'CognitoApiAuthorizer'
    provider_ar_ns = [get_att(CognitoUserPool, "Arn")]
    rest_api_id = ref(RestApi)
    type_ = 'COGNITO_USER_POOLS'


@cloudformation_dataclass
class TestResourceGetIntegration:
    resource: apigateway.method.Integration
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${TestResourceHandler.Arn}/invocations')


@cloudformation_dataclass
class TestResourceGet:
    """AWS::ApiGateway::Method resource."""

    resource: apigateway.Method
    http_method = 'GET'
    resource_id = ref(TestResourceResource)
    rest_api_id = ref(RestApi)
    authorization_type = 'COGNITO_USER_POOLS'
    authorizer_id = ref(RestApiAuthorizer)
    integration = TestResourceGetIntegration


@cloudformation_dataclass
class JwtResourceResource:
    """AWS::ApiGateway::Resource resource."""

    resource: apigateway.Resource
    parent_id = Sub('${RestApi.RootResourceId}')
    path_part = 'jwt'
    rest_api_id = ref(RestApi)


@cloudformation_dataclass
class JwtResourceOptionsIntegration:
    resource: apigateway.method.Integration
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${JwtResourceHandler.Arn}/invocations')


@cloudformation_dataclass
class JwtResourceOptions:
    """AWS::ApiGateway::Method resource."""

    resource: apigateway.Method
    http_method = 'OPTIONS'
    resource_id = ref(JwtResourceResource)
    rest_api_id = ref(RestApi)
    authorization_type = 'NONE'
    integration = JwtResourceOptionsIntegration


@cloudformation_dataclass
class JwtResourceGetIntegration:
    resource: apigateway.method.Integration
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${JwtResourceHandler.Arn}/invocations')


@cloudformation_dataclass
class JwtResourceGet:
    """AWS::ApiGateway::Method resource."""

    resource: apigateway.Method
    http_method = 'GET'
    resource_id = ref(JwtResourceResource)
    rest_api_id = ref(RestApi)
    authorization_type = 'NONE'
    authorizer_id = 'AWS::NoValue'
    integration = JwtResourceGetIntegration


@cloudformation_dataclass
class RestApiDeployment:
    """AWS::ApiGateway::Deployment resource."""

    resource: apigateway.Deployment
    rest_api_id = ref(RestApi)
    depends_on = ["TestResourceGet", "TestResourceOptions", "JwtResourceGet", "JwtResourceOptions"]


@cloudformation_dataclass
class RestApiStage:
    """AWS::ApiGateway::Stage resource."""

    resource: apigateway.Stage
    rest_api_id = ref(RestApi)
    deployment_id = ref(RestApiDeployment)
    stage_name = 'prod'
