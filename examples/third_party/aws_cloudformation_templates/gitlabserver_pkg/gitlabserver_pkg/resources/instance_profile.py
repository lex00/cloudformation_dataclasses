from __future__ import annotations

"""InstanceProfile - AWS::IAM::InstanceProfile resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    roles = [ref("InstanceRole")]
