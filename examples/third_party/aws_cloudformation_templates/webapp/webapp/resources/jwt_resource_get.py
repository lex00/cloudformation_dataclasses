"""JwtResourceGet - AWS::ApiGateway::Method resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class JwtResourceGetIntegration:
    resource: Integration
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${JwtResourceHandler.Arn}/invocations')


@cloudformation_dataclass
class JwtResourceGet:
    """AWS::ApiGateway::Method resource."""

    resource: Method
    http_method = 'GET'
    resource_id = ref(JwtResourceResource)
    rest_api_id = ref(RestApi)
    authorization_type = 'NONE'
    authorizer_id = 'AWS::NoValue'
    integration = JwtResourceGetIntegration
