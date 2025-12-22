from __future__ import annotations

"""JwtResourceResource - AWS::ApiGateway::Resource resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class JwtResourceResource:
    """AWS::ApiGateway::Resource resource."""

    resource: Resource
    parent_id = Sub('${RestApi.RootResourceId}')
    path_part = 'jwt'
    rest_api_id = ref(RestApi)
