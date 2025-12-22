"""VPCPeeringConnection - AWS::EC2::VPCPeeringConnection resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCPeeringConnectionAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = ref(PeerName)


@cloudformation_dataclass
class VPCPeeringConnection:
    """AWS::EC2::VPCPeeringConnection resource."""

    resource: ec2.VPCPeeringConnection
    vpc_id = ref(VPCID)
    peer_vpc_id = ref(PeerVPCID)
    peer_owner_id = ref(PeerOwnerId)
    peer_role_arn = If("PeerRoleCondition", ref(PeerRoleARN), AWS_NO_VALUE)
    tags = [VPCPeeringConnectionAssociationParameter]
