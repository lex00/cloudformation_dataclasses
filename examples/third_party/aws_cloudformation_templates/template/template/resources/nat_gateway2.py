from __future__ import annotations

"""NATGateway2 - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NATGateway2AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-nat-gw2')


@cloudformation_dataclass
class NATGateway2:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id: GetAtt[EIP2] = get_att("AllocationId")
    subnet_id: Ref[PublicSubnet2] = ref()
    tags = [NATGateway2AssociationParameter]
