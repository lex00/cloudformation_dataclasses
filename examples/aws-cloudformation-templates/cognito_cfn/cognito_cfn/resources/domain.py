"""Domain - AWS::Cognito::UserPoolDomain resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Domain:
    """AWS::Cognito::UserPoolDomain resource."""

    resource: cognito.UserPoolDomain
    domain = ref(AppName)
    user_pool_id = ref(UserPool)
