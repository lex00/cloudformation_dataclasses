from __future__ import annotations

"""PrivateProfile - AWS::IAM::InstanceProfile resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: InstanceProfile
    path = '/'
    roles = [ref("RootRole")]
