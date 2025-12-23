"""InstanceSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Allow inbound SSH access'
    security_group_ingress = [{
        'CidrIp': ref(SecurityAccessCIDR),
        'FromPort': 22,
        'IpProtocol': 'tcp',
        'ToPort': 22,
    }]
    vpc_id = ref(VPC)
