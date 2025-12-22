from __future__ import annotations

"""Domain - AWS::Cognito::UserPoolDomain resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Domain:
    """AWS::Cognito::UserPoolDomain resource."""

    resource: UserPoolDomain
    domain = ref(AppName)
    user_pool_id: Ref[UserPool] = ref()
