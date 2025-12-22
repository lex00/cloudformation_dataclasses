"""TestResourceOptions - AWS::ApiGateway::Method resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TestResourceOptionsIntegration:
    resource: apigateway.method.Integration
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${TestResourceHandler.Arn}/invocations')


@cloudformation_dataclass
class TestResourceOptions:
    """AWS::ApiGateway::Method resource."""

    resource: Method
    http_method = 'OPTIONS'
    resource_id = ref(TestResourceResource)
    rest_api_id = ref(RestApi)
    authorization_type = 'NONE'
    integration = TestResourceOptionsIntegration
