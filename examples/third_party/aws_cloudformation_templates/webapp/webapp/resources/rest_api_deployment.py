from __future__ import annotations

"""RestApiDeployment - AWS::ApiGateway::Deployment resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class RestApiDeployment:
    """AWS::ApiGateway::Deployment resource."""

    resource: Deployment
    rest_api_id = ref(RestApi)
    depends_on = ["TestResourceGet", "TestResourceOptions", "JwtResourceGet", "JwtResourceOptions"]
