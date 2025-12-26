"""Stack resources."""

from . import *  # noqa: F403


@cloudformation_dataclass
class Api:
    """AWS::ApiGateway::RestApi resource."""

    resource: RestApi
    name = ref(AppName)


@cloudformation_dataclass
class ApiDeployment:
    """AWS::ApiGateway::Deployment resource."""

    resource: apigateway.Deployment
    rest_api_id = ref(Api)


@cloudformation_dataclass
class ApiStage:
    """AWS::ApiGateway::Stage resource."""

    resource: apigateway.Stage
    rest_api_id = ref(Api)
    deployment_id = ref(ApiDeployment)
    stage_name = 'prod'


@cloudformation_dataclass
class ApiAuthorizer:
    """AWS::ApiGateway::Authorizer resource."""

    resource: apigateway.Authorizer
    identity_source = 'method.request.header.authorization'
    name = 'CognitoApiAuthorizer'
    provider_ar_ns = [ref(UserPoolArn)]
    rest_api_id = ref(Api)
    type_ = 'COGNITO_USER_POOLS'
