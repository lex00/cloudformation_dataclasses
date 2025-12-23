"""ApiDeployment - AWS::ApiGateway::Deployment resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ApiDeployment:
    """AWS::ApiGateway::Deployment resource."""

    resource: apigateway.Deployment
    rest_api_id = ref(Api)
