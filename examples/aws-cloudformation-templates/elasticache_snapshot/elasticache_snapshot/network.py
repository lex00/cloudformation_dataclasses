"""Network resources: VPC, InternetGateway, PublicInternetRouteTable, PublicInternetRoute, VPCGatewayAttachment, PublicSubnetA, PublicSubnetB, PublicSubnetARouteTableAssociation, PublicSubnetBRouteTableAssociation, RedisSecurityGroup."""

from . import *  # noqa: F403

from cloudformation_dataclasses.core.constants import IpProtocol


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    cidr_block = '10.0.0.0/24'


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway


@cloudformation_dataclass
class PublicInternetRouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicInternetRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = ref(InternetGateway)
    route_table_id = ref(PublicInternetRouteTable)
    depends_on = ["InternetGateway", "PublicInternetRouteTable"]


@cloudformation_dataclass
class VPCGatewayAttachment:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = ref(InternetGateway)
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicSubnetA:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = FindInMap("AWSRegion2AZ", AWS_REGION, 'A')
    cidr_block = '10.0.0.0/25'
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicSubnetB:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = FindInMap("AWSRegion2AZ", AWS_REGION, 'B')
    cidr_block = '10.0.0.128/25'
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicSubnetARouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PublicInternetRouteTable)
    subnet_id = ref(PublicSubnetA)


@cloudformation_dataclass
class PublicSubnetBRouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PublicInternetRouteTable)
    subnet_id = ref(PublicSubnetB)


@cloudformation_dataclass
class RedisSecurityGroupEgress:
    resource: ec2.security_group.Egress
    ip_protocol = IpProtocol.TCP
    from_port = '6379'
    to_port = '6379'
    cidr_ip = '192.168.1.0/32'


@cloudformation_dataclass
class RedisSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'RedisSecurityGroup'
    vpc_id = ref(VPC)
    security_group_ingress = [RedisSecurityGroupEgress]
