"""Network resources: EC2SecurityGroup."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EC2SecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'SSH access'
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': '22',
        'ToPort': '22',
        'CidrIp': ref(SSHLocation),
    }]
