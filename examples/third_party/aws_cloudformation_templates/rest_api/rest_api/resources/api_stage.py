from __future__ import annotations

"""ApiStage - AWS::ApiGateway::Stage resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ApiStage:
    """AWS::ApiGateway::Stage resource."""

    resource: Stage
    rest_api_id: Ref[Api] = ref()
    deployment_id: Ref[ApiDeployment] = ref()
    stage_name = 'prod'
