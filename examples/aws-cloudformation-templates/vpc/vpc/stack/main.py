"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    cidr_block = '10.0.0.0/16'
    enable_dns_hostnames = True
    enable_dns_support = True
    instance_tenancy = 'default'


@cloudformation_dataclass
class PublicSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = Select(0, {
    'Fn::GetAZs': AWS_REGION,
})
    cidr_block = '10.0.0.0/18'
    map_public_ip_on_launch = True
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicSubnet1RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicSubnet1RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PublicSubnet1RouteTable)
    subnet_id = ref(PublicSubnet1)


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway


@cloudformation_dataclass
class PublicSubnet1DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = ref(InternetGateway)
    route_table_id = ref(PublicSubnet1RouteTable)
    depends_on = ["VPCGW"]


@cloudformation_dataclass
class PublicSubnet1EIP:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class PublicSubnet1NATGateway:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(PublicSubnet1EIP, "AllocationId")
    subnet_id = ref(PublicSubnet1)
    depends_on = ["PublicSubnet1DefaultRoute", "PublicSubnet1RouteTableAssociation"]


@cloudformation_dataclass
class PublicSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = Select(1, {
    'Fn::GetAZs': AWS_REGION,
})
    cidr_block = '10.0.64.0/18'
    map_public_ip_on_launch = True
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicSubnet2RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PublicSubnet2RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PublicSubnet2RouteTable)
    subnet_id = ref(PublicSubnet2)


@cloudformation_dataclass
class PublicSubnet2DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = ref(InternetGateway)
    route_table_id = ref(PublicSubnet2RouteTable)
    depends_on = ["VPCGW"]


@cloudformation_dataclass
class PublicSubnet2EIP:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class PublicSubnet2NATGateway:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(PublicSubnet2EIP, "AllocationId")
    subnet_id = ref(PublicSubnet2)
    depends_on = ["PublicSubnet2DefaultRoute", "PublicSubnet2RouteTableAssociation"]


@cloudformation_dataclass
class PrivateSubnet1Subnet:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = Select(0, {
    'Fn::GetAZs': AWS_REGION,
})
    cidr_block = '10.0.128.0/18'
    map_public_ip_on_launch = False
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PrivateSubnet1RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PrivateSubnet1RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateSubnet1RouteTable)
    subnet_id = ref(PrivateSubnet1Subnet)


@cloudformation_dataclass
class PrivateSubnet1DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = ref(PublicSubnet1NATGateway)
    route_table_id = ref(PrivateSubnet1RouteTable)


@cloudformation_dataclass
class PrivateSubnet2Subnet:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = Select(1, {
    'Fn::GetAZs': AWS_REGION,
})
    cidr_block = '10.0.192.0/18'
    map_public_ip_on_launch = False
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PrivateSubnet2RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PrivateSubnet2RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateSubnet2RouteTable)
    subnet_id = ref(PrivateSubnet2Subnet)


@cloudformation_dataclass
class PrivateSubnet2DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = ref(PublicSubnet2NATGateway)
    route_table_id = ref(PrivateSubnet2RouteTable)


@cloudformation_dataclass
class VPCGW:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = ref(InternetGateway)
    vpc_id = ref(VPC)
