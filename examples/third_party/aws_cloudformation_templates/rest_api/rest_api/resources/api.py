from __future__ import annotations

"""Api - AWS::ApiGateway::RestApi resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Api:
    """AWS::ApiGateway::RestApi resource."""

    resource: RestApi
    name = ref(AppName)
