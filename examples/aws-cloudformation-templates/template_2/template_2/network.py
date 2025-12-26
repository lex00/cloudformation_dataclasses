"""Network resources: VPC, InternetGateway, AttachGateway, PublicRouteTable, RouteInternetGateway, PublicSubnet1, PublicRouteTableAssociation1, PublicSubnet2, PublicRouteTableAssociation2, PublicSubnet3, PublicRouteTableAssociation3, EIP1, NATGateway1, EIP2, NATGateway2, EIP3, NATGateway3, PrivateSubnet1, PrivateRouteTable1, PrivateRouteTableAssociation1, PrivateRoute1, PrivateSubnet2, PrivateRouteTable2, PrivateRouteTableAssociation2, PrivateRoute2, PrivateSubnet3, PrivateRouteTable3, PrivateRouteTableAssociation3, PrivateRoute3, ControlPlaneSecurityGroup."""

from . import *  # noqa: F403


@cloudformation_dataclass
class VPCAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-vpc')


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    cidr_block = ref(VPCCidrBlock)
    enable_dns_support = True
    enable_dns_hostnames = True
    instance_tenancy = 'default'
    tags = [VPCAssociationParameter]


@cloudformation_dataclass
class InternetGatewayAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-ig')


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway
    tags = [InternetGatewayAssociationParameter]


@cloudformation_dataclass
class AttachGateway:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    vpc_id = ref(VPC)
    internet_gateway_id = ref(InternetGateway)


@cloudformation_dataclass
class PublicRouteTableAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-public-route-table')


@cloudformation_dataclass
class PublicRouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [PublicRouteTableAssociationParameter]


@cloudformation_dataclass
class RouteInternetGateway:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PublicRouteTable)
    gateway_id = ref(InternetGateway)
    destination_cidr_block = '0.0.0.0/0'


@cloudformation_dataclass
class PublicSubnet1AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-public-subnet1')


@cloudformation_dataclass
class PublicSubnet1AssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'kubernetes.io/role/elb'
    value = 1


@cloudformation_dataclass
class PublicSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(0, GetAZs(AWS_REGION))
    cidr_block = ref(PublicCidrBlock1)
    tags = [PublicSubnet1AssociationParameter, PublicSubnet1AssociationParameter1]


@cloudformation_dataclass
class PublicRouteTableAssociation1:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PublicRouteTable)
    subnet_id = ref(PublicSubnet1)


@cloudformation_dataclass
class PublicSubnet2AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-public-subnet2')


@cloudformation_dataclass
class PublicSubnet2AssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'kubernetes.io/role/elb'
    value = 1


@cloudformation_dataclass
class PublicSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(1, GetAZs(AWS_REGION))
    cidr_block = ref(PublicCidrBlock2)
    tags = [PublicSubnet2AssociationParameter, PublicSubnet2AssociationParameter1]


@cloudformation_dataclass
class PublicRouteTableAssociation2:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PublicRouteTable)
    subnet_id = ref(PublicSubnet2)


@cloudformation_dataclass
class PublicSubnet3AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-public-subnet3')


@cloudformation_dataclass
class PublicSubnet3AssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'kubernetes.io/role/elb'
    value = 1


@cloudformation_dataclass
class PublicSubnet3:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(2, GetAZs(AWS_REGION))
    cidr_block = ref(PublicCidrBlock3)
    tags = [PublicSubnet3AssociationParameter, PublicSubnet3AssociationParameter1]


@cloudformation_dataclass
class PublicRouteTableAssociation3:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PublicRouteTable)
    subnet_id = ref(PublicSubnet3)


@cloudformation_dataclass
class EIP1:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class NATGateway1AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-nat-gw1')


@cloudformation_dataclass
class NATGateway1:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(EIP1, "AllocationId")
    subnet_id = ref(PublicSubnet1)
    tags = [NATGateway1AssociationParameter]


@cloudformation_dataclass
class EIP2:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class NATGateway2AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-nat-gw2')


@cloudformation_dataclass
class NATGateway2:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(EIP2, "AllocationId")
    subnet_id = ref(PublicSubnet2)
    tags = [NATGateway2AssociationParameter]


@cloudformation_dataclass
class EIP3:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class NATGateway3AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-nat-gw3')


@cloudformation_dataclass
class NATGateway3:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(EIP3, "AllocationId")
    subnet_id = ref(PublicSubnet3)
    tags = [NATGateway3AssociationParameter]


@cloudformation_dataclass
class PrivateSubnet1AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-subnet1')


@cloudformation_dataclass
class PrivateSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(0, GetAZs(AWS_REGION))
    cidr_block = ref(PrivateCidrBlock1)
    map_public_ip_on_launch = False
    tags = [PrivateSubnet1AssociationParameter]


@cloudformation_dataclass
class PrivateRouteTable1AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-route-table1')


@cloudformation_dataclass
class PrivateRouteTable1:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [PrivateRouteTable1AssociationParameter]


@cloudformation_dataclass
class PrivateRouteTableAssociation1:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTable1)
    subnet_id = ref(PrivateSubnet1)


@cloudformation_dataclass
class PrivateRoute1:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PrivateRouteTable1)
    nat_gateway_id = ref(NATGateway1)
    destination_cidr_block = '0.0.0.0/0'


@cloudformation_dataclass
class PrivateSubnet2AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-subnet2')


@cloudformation_dataclass
class PrivateSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(1, GetAZs(AWS_REGION))
    cidr_block = ref(PrivateCidrBlock2)
    map_public_ip_on_launch = False
    tags = [PrivateSubnet2AssociationParameter]


@cloudformation_dataclass
class PrivateRouteTable2AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-route-table2')


@cloudformation_dataclass
class PrivateRouteTable2:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [PrivateRouteTable2AssociationParameter]


@cloudformation_dataclass
class PrivateRouteTableAssociation2:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTable2)
    subnet_id = ref(PrivateSubnet2)


@cloudformation_dataclass
class PrivateRoute2:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PrivateRouteTable2)
    nat_gateway_id = ref(NATGateway2)
    destination_cidr_block = '0.0.0.0/0'


@cloudformation_dataclass
class PrivateSubnet3AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-subnet3')


@cloudformation_dataclass
class PrivateSubnet3:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(2, GetAZs(AWS_REGION))
    cidr_block = ref(PrivateCidrBlock3)
    map_public_ip_on_launch = False
    tags = [PrivateSubnet3AssociationParameter]


@cloudformation_dataclass
class PrivateRouteTable3AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-route-table3')


@cloudformation_dataclass
class PrivateRouteTable3:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [PrivateRouteTable3AssociationParameter]


@cloudformation_dataclass
class PrivateRouteTableAssociation3:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTable3)
    subnet_id = ref(PrivateSubnet3)


@cloudformation_dataclass
class PrivateRoute3:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PrivateRouteTable3)
    nat_gateway_id = ref(NATGateway3)
    destination_cidr_block = '0.0.0.0/0'


@cloudformation_dataclass
class ControlPlaneSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Communication between the control plane and worker nodegroups'
    vpc_id = ref(VPC)
    group_name = Sub('${AWS::StackName}-eks-control-plane-sg')
