"""TestResourceGet - AWS::ApiGateway::Method resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TestResourceGetIntegration:
    resource: apigateway.Integration
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
