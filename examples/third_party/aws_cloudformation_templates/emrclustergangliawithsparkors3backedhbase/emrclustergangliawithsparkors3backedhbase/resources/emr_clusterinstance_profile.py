from __future__ import annotations

"""EMRClusterinstanceProfile - AWS::IAM::InstanceProfile resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EMRClusterinstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: InstanceProfile
    path = '/'
    roles = [ref("EMRClusterinstanceProfileRole")]
