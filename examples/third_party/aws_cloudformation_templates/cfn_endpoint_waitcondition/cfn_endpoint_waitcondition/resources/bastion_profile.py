from __future__ import annotations

"""BastionProfile - AWS::IAM::InstanceProfile resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BastionProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: InstanceProfile
    path = '/'
    roles = [ref("RootRole")]
