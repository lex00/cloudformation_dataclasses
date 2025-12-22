"""ApiStage - AWS::ApiGateway::Stage resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ApiStage:
    """AWS::ApiGateway::Stage resource."""

    resource: Stage
    rest_api_id = ref(Api)
    deployment_id = ref(ApiDeployment)
    stage_name = 'prod'
