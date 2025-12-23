"""Network resources: VPC, DBSubnet1, DBSubnet2, InternetGateway, AttachGateway, RouteTable, Route, SubnetRouteTableAssociation, SubnetRouteTableAssociation1, AuroraSecurityGroup, DMSSecurityGroup."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    cidr_block = '10.0.0.0/24'
    enable_dns_support = 'true'
    enable_dns_hostnames = 'true'
    tags = [{
        'Key': 'Application',
        'Value': AWS_STACK_ID,
    }, {
        'Key': 'Name',
        'Value': AWS_STACK_NAME,
    }]


@cloudformation_dataclass
class DBSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    cidr_block = '10.0.0.0/26'
    availability_zone = Select(0, GetAZs())
    tags = [{
        'Key': 'Application',
        'Value': AWS_STACK_ID,
    }]


@cloudformation_dataclass
class DBSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    cidr_block = '10.0.0.64/26'
    availability_zone = Select(1, GetAZs())
    tags = [{
        'Key': 'Application',
        'Value': AWS_STACK_ID,
    }]


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway
    tags = [{
        'Key': 'Application',
        'Value': AWS_STACK_ID,
    }]


@cloudformation_dataclass
class AttachGateway:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    vpc_id = ref(VPC)
    internet_gateway_id = ref(InternetGateway)


@cloudformation_dataclass
class RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [{
        'Key': 'Application',
        'Value': AWS_STACK_ID,
    }]


@cloudformation_dataclass
class Route:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(RouteTable)
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = ref(InternetGateway)
    depends_on = ["AttachGateway"]


@cloudformation_dataclass
class SubnetRouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(DBSubnet1)
    route_table_id = ref(RouteTable)


@cloudformation_dataclass
class SubnetRouteTableAssociation1:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(DBSubnet2)
    route_table_id = ref(RouteTable)


@cloudformation_dataclass
class AuroraSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Security group for Aurora SampleDB DB Instance'
    group_name = 'Aurora SampleDB Security Group'
    vpc_id = ref(VPC)
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': '3306',
        'ToPort': '3306',
        'CidrIp': ref(ClientIP),
    }, {
        'IpProtocol': 'tcp',
        'FromPort': '3306',
        'ToPort': '3306',
        'CidrIp': '10.0.0.0/24',
    }]


@cloudformation_dataclass
class DMSSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Security group for DMS Instance'
    group_name = 'DMS Demo Security Group'
    vpc_id = ref(VPC)
