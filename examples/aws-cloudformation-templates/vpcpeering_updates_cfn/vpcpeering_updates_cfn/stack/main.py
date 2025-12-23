"""Stack resources."""

from .. import *  # noqa: F403


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


@cloudformation_dataclass
class PeerIngressRule1:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(0, ref(SecurityGroupIds))
    cidr_ip = ref(PeerVPCCIDR)


@cloudformation_dataclass
class PeerIngressRule2:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer CIDR, ${PeerName}')
    group_id = Select(1, ref(SecurityGroupIds))
    cidr_ip = ref(PeerVPCCIDR)
    condition = '2SecurityGroupCondition'


@cloudformation_dataclass
class PeerIngressRule3:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(2, ref(SecurityGroupIds))
    cidr_ip = ref(PeerVPCCIDR)
    condition = '3SecurityGroupCondition'


@cloudformation_dataclass
class PeerIngressRule4:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(3, ref(SecurityGroupIds))
    cidr_ip = ref(PeerVPCCIDR)
    condition = '4SecurityGroupCondition'


@cloudformation_dataclass
class PeerIngressRule5:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(4, ref(SecurityGroupIds))
    cidr_ip = ref(PeerVPCCIDR)
    condition = '5SecurityGroupCondition'


@cloudformation_dataclass
class PeerIngressRule6:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    ip_protocol = '-1'
    description = Sub('LAB - Allow All Inbound Communications from VPC Peer, ${PeerName}')
    group_id = Select(5, ref(SecurityGroupIds))
    cidr_ip = ref(PeerVPCCIDR)
    condition = '6SecurityGroupCondition'
