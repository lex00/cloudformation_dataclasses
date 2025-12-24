"""Network resources: VPC, InternetGateway, InternetGatewayAttachment, PrivateSubnet1, PrivateSubnet2, EndpointSG, CfnEndpoint, PublicSubnet1, PublicSubnet2, PublicRouteTable, DefaultPublicRoute, PublicSubnet1RouteTableAssociation, PublicSubnet2RouteTableAssociation, PrivateRouteTable1, PrivateSubnet1RouteTableAssociation, PrivateRouteTable2, PrivateSubnet2RouteTableAssociation, BastionSG, PrivateSG."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = ref(EnvironmentName)


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    enable_dns_support = True
    enable_dns_hostnames = True
    cidr_block = ref(VpcCIDR)
    tags = [VPCAssociationParameter]


@cloudformation_dataclass
class InternetGatewayAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = ref(EnvironmentName)


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway
    tags = [InternetGatewayAssociationParameter]


@cloudformation_dataclass
class InternetGatewayAttachment:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = ref(InternetGateway)
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PrivateSubnet1AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Private Subnet (AZ1)')


@cloudformation_dataclass
class PrivateSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(0, GetAZs())
    cidr_block = ref(PrivateSubnet1CIDR)
    map_public_ip_on_launch = False
    tags = [PrivateSubnet1AssociationParameter]


@cloudformation_dataclass
class PrivateSubnet2AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Private Subnet (AZ2)')


@cloudformation_dataclass
class PrivateSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(1, GetAZs())
    cidr_block = ref(PrivateSubnet2CIDR)
    map_public_ip_on_launch = False
    tags = [PrivateSubnet2AssociationParameter]


@cloudformation_dataclass
class EndpointSGEgress:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = 443
    to_port = 443
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class EndpointSGAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'EndpointSG'


@cloudformation_dataclass
class EndpointSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Traffic into CloudFormation Endpoint'
    security_group_ingress = [EndpointSGEgress]
    vpc_id = ref(VPC)
    tags = [EndpointSGAssociationParameter]


@cloudformation_dataclass
class CfnEndpoint:
    """AWS::EC2::VPCEndpoint resource."""

    resource: ec2.VPCEndpoint
    vpc_id = ref(VPC)
    service_name = Sub('com.amazonaws.${AWS::Region}.cloudformation')
    vpc_endpoint_type = 'Interface'
    private_dns_enabled = True
    subnet_ids = [ref(PrivateSubnet1), ref(PrivateSubnet2)]
    security_group_ids = [ref(EndpointSG)]


@cloudformation_dataclass
class PublicSubnet1AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Public Subnet (AZ1)')


@cloudformation_dataclass
class PublicSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(0, GetAZs())
    cidr_block = ref(PublicSubnet1CIDR)
    map_public_ip_on_launch = True
    tags = [PublicSubnet1AssociationParameter]


@cloudformation_dataclass
class PublicSubnet2AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Public Subnet (AZ2)')


@cloudformation_dataclass
class PublicSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(1, GetAZs())
    cidr_block = ref(PublicSubnet2CIDR)
    map_public_ip_on_launch = True
    tags = [PublicSubnet2AssociationParameter]


@cloudformation_dataclass
class PublicRouteTableAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Public Routes')


@cloudformation_dataclass
class PublicRouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [PublicRouteTableAssociationParameter]


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
class PrivateRouteTable1AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Private Routes (AZ1)')


@cloudformation_dataclass
class PrivateRouteTable1:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [PrivateRouteTable1AssociationParameter]


@cloudformation_dataclass
class PrivateSubnet1RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTable1)
    subnet_id = ref(PrivateSubnet1)


@cloudformation_dataclass
class PrivateRouteTable2AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Private Routes (AZ2)')


@cloudformation_dataclass
class PrivateRouteTable2:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [PrivateRouteTable2AssociationParameter]


@cloudformation_dataclass
class PrivateSubnet2RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTable2)
    subnet_id = ref(PrivateSubnet2)


@cloudformation_dataclass
class BastionSGEgress:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = 22
    to_port = 22
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class BastionSGAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'BastionSG'


@cloudformation_dataclass
class BastionSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Inbound Bastion Traffic'
    security_group_ingress = [BastionSGEgress]
    vpc_id = ref(VPC)
    tags = [BastionSGAssociationParameter]


@cloudformation_dataclass
class PrivateSGIngress:
    resource: ec2.security_group.Ingress
    ip_protocol = 'tcp'
    from_port = 22
    to_port = 22
    source_security_group_id = ref(BastionSG)


@cloudformation_dataclass
class PrivateSGAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'PrivateSG'


@cloudformation_dataclass
class PrivateSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Traffic from Bastion'
    security_group_ingress = [PrivateSGIngress]
    vpc_id = ref(VPC)
    tags = [PrivateSGAssociationParameter]
