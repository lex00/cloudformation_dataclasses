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
class PrivateSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Traffic from Bastion'
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': 22,
        'ToPort': 22,
        'CidrIp': ref(VpcCIDR),
    }]
    vpc_id = ref(VPC)
    tags = [{
        'Key': 'Name',
        'Value': 'PrivateSG',
    }]


@cloudformation_dataclass
class PrivateInstance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    instance_type = 't3.micro'
    security_group_ids = [ref(PrivateSG)]
    subnet_id = ref(PrivateSubnet1)
    image_id = ref(LinuxAMI)
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
