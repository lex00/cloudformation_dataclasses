"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class UserPoolAdminCreateUserConfig:
    resource: cognito.user_pool.AdminCreateUserConfig
    allow_admin_create_user_only = True


@cloudformation_dataclass
class UserPoolSchemaAttribute:
    resource: cognito.user_pool.SchemaAttribute
    name = 'email'
    required = True


@cloudformation_dataclass
class UserPoolSchemaAttribute1:
    resource: cognito.user_pool.SchemaAttribute
    name = 'given_name'
    required = True


@cloudformation_dataclass
class UserPoolSchemaAttribute2:
    resource: cognito.user_pool.SchemaAttribute
    name = 'family_name'
    required = True


@cloudformation_dataclass
class UserPool:
    """AWS::Cognito::UserPool resource."""

    resource: cognito.UserPool
    user_pool_name = ref(AppName)
    admin_create_user_config = UserPoolAdminCreateUserConfig
    auto_verified_attributes = ['email']
    mfa_configuration = 'OFF'
    schema = [UserPoolSchemaAttribute, UserPoolSchemaAttribute1, UserPoolSchemaAttribute2]


@cloudformation_dataclass
class Domain:
    """AWS::Cognito::UserPoolDomain resource."""

    resource: cognito.UserPoolDomain
    domain = ref(AppName)
    user_pool_id = ref(UserPool)


@cloudformation_dataclass
class Client:
    """AWS::Cognito::UserPoolClient resource."""

    resource: cognito.UserPoolClient
    client_name = ref(AppName)
    generate_secret = False
    user_pool_id = ref(UserPool)
    callback_ur_ls = [ref(CallbackURL)]
    allowed_o_auth_flows = ['code']
    allowed_o_auth_flows_user_pool_client = True
    allowed_o_auth_scopes = ['phone', 'email', 'openid']
    supported_identity_providers = ['COGNITO']
