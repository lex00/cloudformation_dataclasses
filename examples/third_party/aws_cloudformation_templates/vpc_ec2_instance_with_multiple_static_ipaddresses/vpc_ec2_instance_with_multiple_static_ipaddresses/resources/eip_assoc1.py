from __future__ import annotations

"""EIPAssoc1 - AWS::EC2::EIPAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EIPAssoc1:
    """AWS::EC2::EIPAssociation resource."""

    resource: EIPAssociation
    network_interface_id: Ref[Eth0] = ref()
    allocation_id: GetAtt[EIP1] = get_att("AllocationId")
