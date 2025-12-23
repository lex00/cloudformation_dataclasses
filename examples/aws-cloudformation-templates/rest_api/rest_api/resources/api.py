"""Api - AWS::ApiGateway::RestApi resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Api:
    """AWS::ApiGateway::RestApi resource."""

    resource: apigateway.RestApi
    name = ref(AppName)
