from __future__ import annotations

"""NATGateway1 - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NATGateway1AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-nat-gw1')


@cloudformation_dataclass
class NATGateway1:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id: GetAtt[EIP1] = get_att("AllocationId")
    subnet_id: Ref[PublicSubnet1] = ref()
    tags = [NATGateway1AssociationParameter]
