"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PeerRoleARNOutput:
    """VPC Peer Role ARN"""

    resource: Output
    value = get_att(PeerRole, "Arn")
    description = 'VPC Peer Role ARN'
