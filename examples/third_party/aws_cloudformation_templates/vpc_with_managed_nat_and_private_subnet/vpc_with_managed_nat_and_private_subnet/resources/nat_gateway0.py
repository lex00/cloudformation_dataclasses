from __future__ import annotations

"""NATGateway0 - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NATGateway0:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id = get_att(ElasticIP0, "AllocationId")
    subnet_id = ref(PublicSubnet0)
