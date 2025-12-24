"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCPeeringConnectionIdOutput:
    """VPC Peering Connection ID"""

    resource: Output
    value = ref(VPCPeeringConnection)
    description = 'VPC Peering Connection ID'
