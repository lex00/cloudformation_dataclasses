"""KWOSSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class KWOSSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    vpc_id = ref(VpcId)
    group_description = 'Enable HTTP access via port 80/22/443 and ICMP access via port *'
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': '80',
        'ToPort': '80',
        'CidrIp': '0.0.0.0/0',
    }, {
        'IpProtocol': 'tcp',
        'FromPort': '8888',
        'ToPort': '8888',
        'CidrIp': '0.0.0.0/0',
    }, {
        'IpProtocol': 'tcp',
        'FromPort': '443',
        'ToPort': '443',
        'CidrIp': '0.0.0.0/0',
    }, {
        'IpProtocol': 'icmp',
        'FromPort': '-1',
        'ToPort': '-1',
        'CidrIp': '0.0.0.0/0',
    }, {
        'IpProtocol': 'tcp',
        'FromPort': '22',
        'ToPort': '22',
        'CidrIp': ref(SSHLocation),
    }]
