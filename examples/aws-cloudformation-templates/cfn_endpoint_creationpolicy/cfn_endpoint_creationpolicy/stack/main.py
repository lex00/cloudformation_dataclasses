"""Stack resources."""

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
    tags = [{
        'Key': 'Name',
        'Value': 'EndpointSG',
    }]


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
class PublicSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(0, GetAZs())
    cidr_block = ref(PublicSubnet1CIDR)
    map_public_ip_on_launch = True
    tags = [{
        'Key': 'Name',
        'Value': Sub('${EnvironmentName} Public Subnet (AZ1)'),
    }]


@cloudformation_dataclass
class PublicSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(1, GetAZs())
    cidr_block = ref(PublicSubnet2CIDR)
    map_public_ip_on_launch = True
    tags = [{
        'Key': 'Name',
        'Value': Sub('${EnvironmentName} Public Subnet (AZ2)'),
    }]


@cloudformation_dataclass
class PublicRouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${EnvironmentName} Public Routes'),
    }]


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
    tags = [{
        'Key': 'Name',
        'Value': Sub('${EnvironmentName} Private Routes (AZ1)'),
    }]


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
    tags = [{
        'Key': 'Name',
        'Value': Sub('${EnvironmentName} Private Routes (AZ2)'),
    }]


@cloudformation_dataclass
class PrivateSubnet2RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTable2)
    subnet_id = ref(PrivateSubnet2)


@cloudformation_dataclass
class RootRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class RootRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [RootRoleAllowStatement0]


@cloudformation_dataclass
class RootRoleAllowStatement0_1:
    resource: PolicyStatement
    action = 'cloudformation:*'
    resource_arn = '*'


@cloudformation_dataclass
class RootRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [RootRoleAllowStatement0_1]


@cloudformation_dataclass
class RootRolePolicy:
    resource: iam.user.Policy
    policy_name = 'root'
    policy_document = RootRolePolicies0PolicyDocument


@cloudformation_dataclass
class RootRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = RootRoleAssumeRolePolicyDocument
    path = '/'
    policies = [RootRolePolicy]


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
    tags = [{
        'Key': 'Name',
        'Value': 'BastionSG',
    }]


@cloudformation_dataclass
class BastionProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    path = '/'
    roles = [ref(RootRole)]


@cloudformation_dataclass
class BastionInstance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    key_name = ref(KeyName)
    instance_type = 't2.micro'
    security_group_ids = [ref(BastionSG)]
    subnet_id = ref(PublicSubnet1)
    image_id = ref(LinuxAMI)
    iam_instance_profile = ref(BastionProfile)
    tags = [{
        'Key': 'Name',
        'Value': 'Bastion',
    }]


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
    tags = [{
        'Key': 'Name',
        'Value': 'PrivateSG',
    }]


@cloudformation_dataclass
class PrivateProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    path = '/'
    roles = [ref(RootRole)]


@cloudformation_dataclass
class PrivateInstance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    key_name = ref(KeyName)
    instance_type = 't2.micro'
    security_group_ids = [ref(PrivateSG)]
    subnet_id = ref(PrivateSubnet1)
    image_id = ref(LinuxAMI)
    iam_instance_profile = ref(PrivateProfile)
    user_data = Base64(Sub("""#!/bin/bash -x
date > /tmp/datefile
cat /tmp/datefile
# Signal the status from instance
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource PrivateInstance --region ${AWS::Region}
"""))
    tags = [{
        'Key': 'Name',
        'Value': 'Private',
    }]
    depends_on = ["CfnEndpoint"]
