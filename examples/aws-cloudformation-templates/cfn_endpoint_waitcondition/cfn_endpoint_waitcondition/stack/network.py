"""Network resources: VPC, InternetGateway, InternetGatewayAttachment, PrivateSubnet1, PrivateSubnet2, EndpointSG, CfnEndpoint, PrivateRouteTable1, PrivateRouteTable2, S3Endpoint, PublicSubnet1, PublicSubnet2, PublicRouteTable, DefaultPublicRoute, PublicSubnet1RouteTableAssociation, PublicSubnet2RouteTableAssociation, PrivateSubnet1RouteTableAssociation, PrivateSubnet2RouteTableAssociation, BastionSG, PrivateSG."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    enable_dns_support = True
    enable_dns_hostnames = True
    cidr_block = ref(VpcCIDR)
    tags = [{
        'Key': 'Name',
        'Value': ref(EnvironmentName),
    }]


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway
    tags = [{
        'Key': 'Name',
        'Value': ref(EnvironmentName),
    }]


@cloudformation_dataclass
class InternetGatewayAttachment:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = ref(InternetGateway)
    vpc_id = ref(VPC)


@cloudformation_dataclass
class PrivateSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(0, GetAZs())
    cidr_block = ref(PrivateSubnet1CIDR)
    map_public_ip_on_launch = False
    tags = [{
        'Key': 'Name',
        'Value': Sub('${EnvironmentName} Private Subnet (AZ1)'),
    }]


@cloudformation_dataclass
class PrivateSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(1, GetAZs())
    cidr_block = ref(PrivateSubnet2CIDR)
    map_public_ip_on_launch = False
    tags = [{
        'Key': 'Name',
        'Value': Sub('${EnvironmentName} Private Subnet (AZ2)'),
    }]


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
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': 443,
        'ToPort': 443,
        'CidrIp': '0.0.0.0/0',
    }]
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
class S3EndpointAllowStatement0:
    resource: PolicyStatement
    principal = '*'
    action = ['s3:PutObject']
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::cloudformation-waitcondition-${AWS::Region}/*')]


@cloudformation_dataclass
class S3EndpointPolicyDocument:
    resource: PolicyDocument
    statement = [S3EndpointAllowStatement0]


@cloudformation_dataclass
class S3Endpoint:
    """AWS::EC2::VPCEndpoint resource."""

    resource: ec2.VPCEndpoint
    vpc_id = ref(VPC)
    service_name = Sub('com.amazonaws.${AWS::Region}.s3')
    vpc_endpoint_type = 'Gateway'
    policy_document = S3EndpointPolicyDocument
    route_table_ids = [ref(PrivateRouteTable1), ref(PrivateRouteTable2)]


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
class PrivateSubnet1RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTable1)
    subnet_id = ref(PrivateSubnet1)


@cloudformation_dataclass
class PrivateSubnet2RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTable2)
    subnet_id = ref(PrivateSubnet2)


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
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': 22,
        'ToPort': 22,
        'CidrIp': '0.0.0.0/0',
    }]
    vpc_id = ref(VPC)
    tags = [BastionSGAssociationParameter]


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
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': 22,
        'ToPort': 22,
        'SourceSecurityGroupId': ref(BastionSG),
    }]
    vpc_id = ref(VPC)
    tags = [PrivateSGAssociationParameter]
