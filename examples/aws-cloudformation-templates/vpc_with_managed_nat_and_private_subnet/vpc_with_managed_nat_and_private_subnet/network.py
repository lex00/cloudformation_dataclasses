"""Network resources: VPC, PublicSubnet0, PublicSubnet1, PrivateSubnet0, PrivateSubnet1, InternetGateway, GatewayToInternet, PublicRouteTable, PublicRoute, PublicSubnetRouteTableAssociation0, PublicSubnetRouteTableAssociation1, PublicNetworkAcl, ElasticIP0, ElasticIP1, NATGateway0, NATGateway1, PrivateRouteTable0, PrivateRouteTable1, PrivateRouteToInternet0, PrivateRouteToInternet1, PrivateSubnetRouteTableAssociation0, PrivateSubnetRouteTableAssociation1."""

from . import *  # noqa: F403


@cloudformation_dataclass
class VPCAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class VPCAssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Network'
    value = 'Public'


@cloudformation_dataclass
class VPCAssociationParameter2:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = ref(VPCName)


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    enable_dns_support = 'true'
    enable_dns_hostnames = 'true'
    cidr_block = FindInMap("SubnetConfig", 'VPC', 'CIDR')
    tags = [VPCAssociationParameter, VPCAssociationParameter1, VPCAssociationParameter2]


@cloudformation_dataclass
class PublicSubnet0AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class PublicSubnet0AssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Network'
    value = 'Public'


@cloudformation_dataclass
class PublicSubnet0AssociationParameter2:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-public-',
    Select(0, GetAZs()),
])


@cloudformation_dataclass
class PublicSubnet0:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(0, GetAZs())
    cidr_block = FindInMap("SubnetConfig", 'Public0', 'CIDR')
    map_public_ip_on_launch = 'true'
    tags = [PublicSubnet0AssociationParameter, PublicSubnet0AssociationParameter1, PublicSubnet0AssociationParameter2]


@cloudformation_dataclass
class PublicSubnet1AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class PublicSubnet1AssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Network'
    value = 'Public'


@cloudformation_dataclass
class PublicSubnet1AssociationParameter2:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-public-',
    Select(1, GetAZs()),
])


@cloudformation_dataclass
class PublicSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(1, GetAZs())
    cidr_block = FindInMap("SubnetConfig", 'Public1', 'CIDR')
    map_public_ip_on_launch = 'true'
    tags = [PublicSubnet1AssociationParameter, PublicSubnet1AssociationParameter1, PublicSubnet1AssociationParameter2]


@cloudformation_dataclass
class PrivateSubnet0AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class PrivateSubnet0AssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Network'
    value = 'Private'


@cloudformation_dataclass
class PrivateSubnet0AssociationParameter2:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-private-',
    Select(0, GetAZs()),
])


@cloudformation_dataclass
class PrivateSubnet0:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(0, GetAZs())
    cidr_block = FindInMap("SubnetConfig", 'Private0', 'CIDR')
    tags = [PrivateSubnet0AssociationParameter, PrivateSubnet0AssociationParameter1, PrivateSubnet0AssociationParameter2]


@cloudformation_dataclass
class PrivateSubnet1AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class PrivateSubnet1AssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Network'
    value = 'Private'


@cloudformation_dataclass
class PrivateSubnet1AssociationParameter2:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-private-',
    Select(1, GetAZs()),
])


@cloudformation_dataclass
class PrivateSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(1, GetAZs())
    cidr_block = FindInMap("SubnetConfig", 'Private1', 'CIDR')
    tags = [PrivateSubnet1AssociationParameter, PrivateSubnet1AssociationParameter1, PrivateSubnet1AssociationParameter2]


@cloudformation_dataclass
class InternetGatewayAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class InternetGatewayAssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Network'
    value = 'Public'


@cloudformation_dataclass
class InternetGatewayAssociationParameter2:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-IGW',
])


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway
    tags = [InternetGatewayAssociationParameter, InternetGatewayAssociationParameter1, InternetGatewayAssociationParameter2]


@cloudformation_dataclass
class GatewayToInternet:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    vpc_id = ref(VPC)
    internet_gateway_id = ref(InternetGateway)


@cloudformation_dataclass
class PublicRouteTableAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class PublicRouteTableAssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Network'
    value = 'Public'


@cloudformation_dataclass
class PublicRouteTableAssociationParameter2:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-public-route-table',
])


@cloudformation_dataclass
class PublicRouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [PublicRouteTableAssociationParameter, PublicRouteTableAssociationParameter1, PublicRouteTableAssociationParameter2]


@cloudformation_dataclass
class PublicRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PublicRouteTable)
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = ref(InternetGateway)
    depends_on = [GatewayToInternet]


@cloudformation_dataclass
class PublicSubnetRouteTableAssociation0:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(PublicSubnet0)
    route_table_id = ref(PublicRouteTable)


@cloudformation_dataclass
class PublicSubnetRouteTableAssociation1:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(PublicSubnet1)
    route_table_id = ref(PublicRouteTable)


@cloudformation_dataclass
class PublicNetworkAclAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class PublicNetworkAclAssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Network'
    value = 'Public'


@cloudformation_dataclass
class PublicNetworkAclAssociationParameter2:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-public-nacl',
])


@cloudformation_dataclass
class PublicNetworkAcl:
    """AWS::EC2::NetworkAcl resource."""

    resource: ec2.NetworkAcl
    vpc_id = ref(VPC)
    tags = [PublicNetworkAclAssociationParameter, PublicNetworkAclAssociationParameter1, PublicNetworkAclAssociationParameter2]


@cloudformation_dataclass
class ElasticIP0:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class ElasticIP1:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class NATGateway0:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(ElasticIP0, "AllocationId")
    subnet_id = ref(PublicSubnet0)


@cloudformation_dataclass
class NATGateway1:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(ElasticIP1, "AllocationId")
    subnet_id = ref(PublicSubnet1)


@cloudformation_dataclass
class PrivateRouteTable0AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-private-route-table-0',
])


@cloudformation_dataclass
class PrivateRouteTable0:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [PrivateRouteTable0AssociationParameter]


@cloudformation_dataclass
class PrivateRouteTable1AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-private-route-table-1',
])


@cloudformation_dataclass
class PrivateRouteTable1:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [PrivateRouteTable1AssociationParameter]


@cloudformation_dataclass
class PrivateRouteToInternet0:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PrivateRouteTable0)
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = ref(NATGateway0)


@cloudformation_dataclass
class PrivateRouteToInternet1:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PrivateRouteTable1)
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = ref(NATGateway1)


@cloudformation_dataclass
class PrivateSubnetRouteTableAssociation0:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(PrivateSubnet0)
    route_table_id = ref(PrivateRouteTable0)


@cloudformation_dataclass
class PrivateSubnetRouteTableAssociation1:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(PrivateSubnet1)
    route_table_id = ref(PrivateRouteTable1)
