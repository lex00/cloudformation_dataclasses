from __future__ import annotations

"""TestResourceGet - AWS::ApiGateway::Method resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TestResourceGetIntegration:
    resource: Integration
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${TestResourceHandler.Arn}/invocations')


@cloudformation_dataclass
class TestResourceGet:
    """AWS::ApiGateway::Method resource."""

    resource: Method
    http_method = 'GET'
    resource_id: Ref[TestResourceResource] = ref()
    rest_api_id: Ref[RestApi] = ref()
    authorization_type = 'COGNITO_USER_POOLS'
    authorizer_id: Ref[RestApiAuthorizer] = ref()
    integration = TestResourceGetIntegration
