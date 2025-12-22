"""RestApiAuthorizer - AWS::ApiGateway::Authorizer resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class RestApiAuthorizer:
    """AWS::ApiGateway::Authorizer resource."""

    resource: Authorizer
    identity_source = 'method.request.header.authorization'
    name = 'CognitoApiAuthorizer'
    provider_ar_ns = [get_att(CognitoUserPool, "Arn")]
    rest_api_id = ref(RestApi)
    type_ = 'COGNITO_USER_POOLS'
