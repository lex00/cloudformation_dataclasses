from __future__ import annotations

"""TestResourceResource - AWS::ApiGateway::Resource resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TestResourceResource:
    """AWS::ApiGateway::Resource resource."""

    resource: Resource
    parent_id = Sub('${RestApi.RootResourceId}')
    path_part = 'test'
    rest_api_id: Ref[RestApi] = ref()
