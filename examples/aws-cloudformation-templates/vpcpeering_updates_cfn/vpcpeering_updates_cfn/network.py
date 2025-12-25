"""Network resources: PeerRoute1, PeerRoute2, PeerRoute3, PeerRoute4, PeerRoute5, PeerRoute6."""

from . import *  # noqa: F403


@cloudformation_dataclass
class PeerRoute1:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = Select(0, Split(',', ref(RouteTableIds)))
    destination_cidr_block = ref(PeerVPCCIDR)
    vpc_peering_connection_id = ref(VPCPeeringConnectionId)


@cloudformation_dataclass
class PeerRoute2:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = Select(1, Split(',', ref(RouteTableIds)))
    destination_cidr_block = ref(PeerVPCCIDR)
    vpc_peering_connection_id = ref(VPCPeeringConnectionId)
    condition = '2RouteTableCondition'


@cloudformation_dataclass
class PeerRoute3:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = Select(2, Split(',', ref(RouteTableIds)))
    destination_cidr_block = ref(PeerVPCCIDR)
    vpc_peering_connection_id = ref(VPCPeeringConnectionId)
    condition = '3RouteTableCondition'


@cloudformation_dataclass
class PeerRoute4:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = Select(3, Split(',', ref(RouteTableIds)))
    destination_cidr_block = ref(PeerVPCCIDR)
    vpc_peering_connection_id = ref(VPCPeeringConnectionId)
    condition = '4RouteTableCondition'


@cloudformation_dataclass
class PeerRoute5:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = Select(4, Split(',', ref(RouteTableIds)))
    destination_cidr_block = ref(PeerVPCCIDR)
    vpc_peering_connection_id = ref(VPCPeeringConnectionId)
    condition = '5RouteTableCondition'


@cloudformation_dataclass
class PeerRoute6:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = Select(5, Split(',', ref(RouteTableIds)))
    destination_cidr_block = ref(PeerVPCCIDR)
    vpc_peering_connection_id = ref(VPCPeeringConnectionId)
    condition = '6RouteTableCondition'
