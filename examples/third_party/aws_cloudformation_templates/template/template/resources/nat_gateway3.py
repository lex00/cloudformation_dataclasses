from __future__ import annotations

"""NATGateway3 - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NATGateway3AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-nat-gw3')


@cloudformation_dataclass
class NATGateway3:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id: GetAtt[EIP3] = get_att("AllocationId")
    subnet_id: Ref[PublicSubnet3] = ref()
    tags = [NATGateway3AssociationParameter]
