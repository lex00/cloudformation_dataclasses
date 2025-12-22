"""ApiAuthorizer - AWS::ApiGateway::Authorizer resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ApiAuthorizer:
    """AWS::ApiGateway::Authorizer resource."""

    resource: Authorizer
    identity_source = 'method.request.header.authorization'
    name = 'CognitoApiAuthorizer'
    provider_ar_ns = [ref(UserPoolArn)]
    rest_api_id = ref(Api)
    type_ = 'COGNITO_USER_POOLS'
