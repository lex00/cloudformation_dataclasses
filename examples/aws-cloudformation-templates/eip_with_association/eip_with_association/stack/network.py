"""Network resources: InstanceSecurityGroup, IPAddress."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable SSH access'
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': '22',
        'ToPort': '22',
        'CidrIp': ref(SSHLocation),
    }]


@cloudformation_dataclass
class IPAddress:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
