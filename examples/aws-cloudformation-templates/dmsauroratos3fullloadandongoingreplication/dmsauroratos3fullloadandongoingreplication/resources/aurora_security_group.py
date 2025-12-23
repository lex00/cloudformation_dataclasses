"""AuroraSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


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
