from __future__ import annotations

"""TestResourceOptions - AWS::ApiGateway::Method resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TestResourceOptionsIntegration:
    resource: Integration
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${TestResourceHandler.Arn}/invocations')


@cloudformation_dataclass
class TestResourceOptions:
    """AWS::ApiGateway::Method resource."""

    resource: Method
    http_method = 'OPTIONS'
    resource_id: Ref[TestResourceResource] = ref()
    rest_api_id: Ref[RestApi] = ref()
    authorization_type = 'NONE'
    integration = TestResourceOptionsIntegration
