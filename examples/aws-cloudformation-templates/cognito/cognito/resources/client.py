"""Client - AWS::Cognito::UserPoolClient resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Client:
    """AWS::Cognito::UserPoolClient resource."""

    resource: UserPoolClient
    client_name = ref(AppName)
    generate_secret = False
    user_pool_id = ref(UserPool)
    callback_ur_ls = [ref(CallbackURL)]
    allowed_o_auth_flows = ['code']
    allowed_o_auth_flows_user_pool_client = True
    allowed_o_auth_scopes = ['phone', 'email', 'openid']
    supported_identity_providers = ['COGNITO']
