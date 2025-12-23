"""InstanceSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable SSH public access and HTTP from the load balancer only'
    security_group_ingress = [{
        'CidrIp': '0.0.0.0/0',
        'FromPort': '22',
        'IpProtocol': 'tcp',
        'ToPort': '22',
    }, {
        'FromPort': '80',
        'IpProtocol': 'tcp',
        'SourceSecurityGroupId': get_att(ELBSecurityGroup, "GroupId"),
        'ToPort': '80',
    }]
    vpc_id = ref(VPC)
