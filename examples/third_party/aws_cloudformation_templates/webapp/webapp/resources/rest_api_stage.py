"""RestApiStage - AWS::ApiGateway::Stage resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class RestApiStage:
    """AWS::ApiGateway::Stage resource."""

    resource: Stage
    rest_api_id = ref(RestApi)
    deployment_id = ref(RestApiDeployment)
    stage_name = 'prod'
