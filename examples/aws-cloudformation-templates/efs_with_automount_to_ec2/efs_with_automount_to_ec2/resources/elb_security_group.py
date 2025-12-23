"""ELBSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ELBSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable public access HTTP and HTTPS'
    security_group_ingress = [{
        'CidrIp': '0.0.0.0/0',
        'FromPort': '80',
        'IpProtocol': 'tcp',
        'ToPort': '80',
    }, {
        'CidrIp': '0.0.0.0/0',
        'FromPort': '443',
        'IpProtocol': 'tcp',
        'ToPort': '443',
    }]
    vpc_id = ref(VPC)
