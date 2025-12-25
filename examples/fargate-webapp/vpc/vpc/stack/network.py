"""VPC network resources - VPC, subnets, gateways, route tables."""

from .. import *  # noqa: F403, F401


# =============================================================================
# VPC
# =============================================================================


@cloudformation_dataclass
class Vpc:
    resource: ec2.VPC
    cidr_block = "10.0.0.0/16"
    enable_dns_support = True
    enable_dns_hostnames = True


# =============================================================================
# Internet Gateway
# =============================================================================


@cloudformation_dataclass
class InternetGateway:
    resource: ec2.InternetGateway


@cloudformation_dataclass
class InternetGatewayAttachment:
    resource: ec2.VPCGatewayAttachment
    vpc_id = ref(Vpc)
    internet_gateway_id = ref(InternetGateway)


# =============================================================================
# Public Subnets (3 AZs)
# =============================================================================


@cloudformation_dataclass
class PublicSubnet1:
    resource: ec2.Subnet
    vpc_id = ref(Vpc)
    cidr_block = "10.0.1.0/24"
    availability_zone = Select(index=0, objects=GetAZs())
    map_public_ip_on_launch = True


@cloudformation_dataclass
class PublicSubnet2:
    resource: ec2.Subnet
    vpc_id = ref(Vpc)
    cidr_block = "10.0.2.0/24"
    availability_zone = Select(index=1, objects=GetAZs())
    map_public_ip_on_launch = True


@cloudformation_dataclass
class PublicSubnet3:
    resource: ec2.Subnet
    vpc_id = ref(Vpc)
    cidr_block = "10.0.3.0/24"
    availability_zone = Select(index=2, objects=GetAZs())
    map_public_ip_on_launch = True


# =============================================================================
# Private Subnets (3 AZs)
# =============================================================================


@cloudformation_dataclass
class PrivateSubnet1:
    resource: ec2.Subnet
    vpc_id = ref(Vpc)
    cidr_block = "10.0.11.0/24"
    availability_zone = Select(index=0, objects=GetAZs())


@cloudformation_dataclass
class PrivateSubnet2:
    resource: ec2.Subnet
    vpc_id = ref(Vpc)
    cidr_block = "10.0.12.0/24"
    availability_zone = Select(index=1, objects=GetAZs())


@cloudformation_dataclass
class PrivateSubnet3:
    resource: ec2.Subnet
    vpc_id = ref(Vpc)
    cidr_block = "10.0.13.0/24"
    availability_zone = Select(index=2, objects=GetAZs())


# =============================================================================
# Elastic IPs for NAT Gateways
# =============================================================================


@cloudformation_dataclass
class NatEip1:
    resource: ec2.EIP
    domain = "vpc"


@cloudformation_dataclass
class NatEip2:
    resource: ec2.EIP
    domain = "vpc"


@cloudformation_dataclass
class NatEip3:
    resource: ec2.EIP
    domain = "vpc"


# =============================================================================
# NAT Gateways (one per AZ for high availability)
# =============================================================================


@cloudformation_dataclass
class NatGateway1:
    resource: ec2.NatGateway
    allocation_id = get_att(NatEip1, "AllocationId")
    subnet_id = ref(PublicSubnet1)


@cloudformation_dataclass
class NatGateway2:
    resource: ec2.NatGateway
    allocation_id = get_att(NatEip2, "AllocationId")
    subnet_id = ref(PublicSubnet2)


@cloudformation_dataclass
class NatGateway3:
    resource: ec2.NatGateway
    allocation_id = get_att(NatEip3, "AllocationId")
    subnet_id = ref(PublicSubnet3)


# =============================================================================
# Public Route Table
# =============================================================================


@cloudformation_dataclass
class PublicRouteTable:
    resource: ec2.RouteTable
    vpc_id = ref(Vpc)


@cloudformation_dataclass
class PublicRoute:
    resource: ec2.Route
    route_table_id = ref(PublicRouteTable)
    destination_cidr_block = "0.0.0.0/0"
    gateway_id = ref(InternetGateway)


@cloudformation_dataclass
class PublicSubnet1RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(PublicSubnet1)
    route_table_id = ref(PublicRouteTable)


@cloudformation_dataclass
class PublicSubnet2RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(PublicSubnet2)
    route_table_id = ref(PublicRouteTable)


@cloudformation_dataclass
class PublicSubnet3RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(PublicSubnet3)
    route_table_id = ref(PublicRouteTable)


# =============================================================================
# Private Route Tables (one per AZ for NAT routing)
# =============================================================================


@cloudformation_dataclass
class PrivateRouteTable1:
    resource: ec2.RouteTable
    vpc_id = ref(Vpc)


@cloudformation_dataclass
class PrivateRoute1:
    resource: ec2.Route
    route_table_id = ref(PrivateRouteTable1)
    destination_cidr_block = "0.0.0.0/0"
    nat_gateway_id = ref(NatGateway1)


@cloudformation_dataclass
class PrivateSubnet1RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(PrivateSubnet1)
    route_table_id = ref(PrivateRouteTable1)


@cloudformation_dataclass
class PrivateRouteTable2:
    resource: ec2.RouteTable
    vpc_id = ref(Vpc)


@cloudformation_dataclass
class PrivateRoute2:
    resource: ec2.Route
    route_table_id = ref(PrivateRouteTable2)
    destination_cidr_block = "0.0.0.0/0"
    nat_gateway_id = ref(NatGateway2)


@cloudformation_dataclass
class PrivateSubnet2RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(PrivateSubnet2)
    route_table_id = ref(PrivateRouteTable2)


@cloudformation_dataclass
class PrivateRouteTable3:
    resource: ec2.RouteTable
    vpc_id = ref(Vpc)


@cloudformation_dataclass
class PrivateRoute3:
    resource: ec2.Route
    route_table_id = ref(PrivateRouteTable3)
    destination_cidr_block = "0.0.0.0/0"
    nat_gateway_id = ref(NatGateway3)


@cloudformation_dataclass
class PrivateSubnet3RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(PrivateSubnet3)
    route_table_id = ref(PrivateRouteTable3)
