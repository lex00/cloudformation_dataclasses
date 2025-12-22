from __future__ import annotations

"""NATGateway0 - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NATGateway0:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id: GetAtt[ElasticIP0] = get_att("AllocationId")
    subnet_id: Ref[PublicSubnet0] = ref()
