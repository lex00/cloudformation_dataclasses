from __future__ import annotations

"""Association2 - AWS::EC2::EIPAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Association2:
    """AWS::EC2::EIPAssociation resource."""

    resource: EIPAssociation
    allocation_id: GetAtt[EIP2] = get_att("AllocationId")
    network_interface_id: Ref[ENI] = ref()
    private_ip_address = Select(1, get_att("ENI", "SecondaryPrivateIpAddresses"))
    depends_on = ["ENI", "EIP2"]
