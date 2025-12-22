"""TestResourceResource - AWS::ApiGateway::Resource resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TestResourceResource:
    """AWS::ApiGateway::Resource resource."""

    resource: apigateway.Resource
    parent_id = Sub('${RestApi.RootResourceId}')
    path_part = 'test'
    rest_api_id = ref(RestApi)
