"""UserPool - AWS::Cognito::UserPool resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class UserPoolAdminCreateUserConfig:
    resource: AdminCreateUserConfig
    allow_admin_create_user_only = True


@cloudformation_dataclass
class UserPoolSchemaAttribute:
    resource: SchemaAttribute
    name = 'email'
    required = True


@cloudformation_dataclass
class UserPoolSchemaAttribute1:
    resource: SchemaAttribute
    name = 'given_name'
    required = True


@cloudformation_dataclass
class UserPoolSchemaAttribute2:
    resource: SchemaAttribute
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
