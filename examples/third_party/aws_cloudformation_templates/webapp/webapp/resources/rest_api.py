from __future__ import annotations

"""RestApi - AWS::ApiGateway::RestApi resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class RestApi:
    """AWS::ApiGateway::RestApi resource."""

    resource: apigateway.RestApi
    name = ref(AppName)
