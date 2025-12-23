"""CognitoUserPool - AWS::Cognito::UserPool resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CognitoUserPoolAdminCreateUserConfig:
    resource: cognito.user_pool.AdminCreateUserConfig
    allow_admin_create_user_only = True


@cloudformation_dataclass
class CognitoUserPoolSchemaAttribute:
    resource: cognito.user_pool.SchemaAttribute
    name = 'email'
    required = True


@cloudformation_dataclass
class CognitoUserPoolSchemaAttribute1:
    resource: cognito.user_pool.SchemaAttribute
    name = 'given_name'
    required = True


@cloudformation_dataclass
class CognitoUserPoolSchemaAttribute2:
    resource: cognito.user_pool.SchemaAttribute
    name = 'family_name'
    required = True


@cloudformation_dataclass
class CognitoUserPool:
    """AWS::Cognito::UserPool resource."""

    resource: cognito.UserPool
    user_pool_name = ref(AppName)
    admin_create_user_config = CognitoUserPoolAdminCreateUserConfig
    auto_verified_attributes = ['email']
    schema = [CognitoUserPoolSchemaAttribute, CognitoUserPoolSchemaAttribute1, CognitoUserPoolSchemaAttribute2]
    depends_on = ["SiteDistribution"]
