"""Network resources: VPC, InternetGateway, InternetGatewayAttachment, PublicSubnet1, PublicSubnet2, PrivateSubnet1, PrivateSubnet2, NatGateway1EIP, NatGateway2EIP, NatGateway1, NatGateway2, PublicRouteTable, DefaultPublicRoute, PublicSubnet1RouteTableAssociation, PublicSubnet2RouteTableAssociation, PrivateRouteTable1, DefaultPrivateRoute1, PrivateSubnet1RouteTableAssociation, PrivateRouteTable2, DefaultPrivateRoute2, PrivateSubnet2RouteTableAssociation, NoIngressSecurityGroup."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    cidr_block = ref(VpcCIDR)
    enable_dns_support = True
    enable_dns_hostnames = True


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway


@cloudformation_dataclass
class InternetGatewayAttachment:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = ref(InternetGateway)
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(0, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = ref(PublicSubnet1CIDR)
    map_public_ip_on_launch = True


@cloudformation_dataclass
class PublicSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(1, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = ref(PublicSubnet2CIDR)
    map_public_ip_on_launch = True


@cloudformation_dataclass
class PrivateSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(0, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = ref(PrivateSubnet1CIDR)
    map_public_ip_on_launch = False


@cloudformation_dataclass
class PrivateSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(1, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = ref(PrivateSubnet2CIDR)
    map_public_ip_on_launch = False


@cloudformation_dataclass
class NatGateway1EIP:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'
    depends_on = ["InternetGatewayAttachment"]


@cloudformation_dataclass
class NatGateway2EIP:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'
    depends_on = ["InternetGatewayAttachment"]


@cloudformation_dataclass
class NatGateway1:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(NatGateway1EIP, "AllocationId")
    subnet_id = ref(PublicSubnet1)


@cloudformation_dataclass
class NatGateway2:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(NatGateway2EIP, "AllocationId")
    subnet_id = ref(PublicSubnet2)


@cloudformation_dataclass
class PublicRouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)


@cloudformation_dataclass
class DefaultPublicRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PublicRouteTable)
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = ref(InternetGateway)
    depends_on = ["InternetGatewayAttachment"]


@cloudformation_dataclass
class PublicSubnet1RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PublicRouteTable)
    subnet_id = ref(PublicSubnet1)


@cloudformation_dataclass
class PublicSubnet2RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PublicRouteTable)
    subnet_id = ref(PublicSubnet2)


@cloudformation_dataclass
class PrivateRouteTable1:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)


@cloudformation_dataclass
class DefaultPrivateRoute1:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PrivateRouteTable1)
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = ref(NatGateway1)


@cloudformation_dataclass
class PrivateSubnet1RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTable1)
    subnet_id = ref(PrivateSubnet1)


@cloudformation_dataclass
class PrivateRouteTable2:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)


@cloudformation_dataclass
class DefaultPrivateRoute2:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PrivateRouteTable2)
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = ref(NatGateway2)


@cloudformation_dataclass
class PrivateSubnet2RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTable2)
    subnet_id = ref(PrivateSubnet2)


@cloudformation_dataclass
class NoIngressSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_name = 'no-ingress-sg'
    group_description = 'Security group with no ingress rule'
    vpc_id = ref(VPC)
