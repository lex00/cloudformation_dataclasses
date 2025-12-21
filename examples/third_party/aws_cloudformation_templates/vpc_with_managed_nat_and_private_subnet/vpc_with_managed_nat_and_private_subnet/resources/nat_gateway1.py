from __future__ import annotations

"""NATGateway1 - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NATGateway1:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id: GetAtt[ElasticIP1] = get_att("AllocationId")
    subnet_id: Ref[PublicSubnet1] = ref()
