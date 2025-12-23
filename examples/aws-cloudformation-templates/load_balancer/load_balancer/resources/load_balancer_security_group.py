"""LoadBalancerSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoadBalancerSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Automatically created Security Group for ELB'
    security_group_ingress = [{
        'CidrIp': '0.0.0.0/0',
        'Description': 'Allow from anyone on port 443',
        'FromPort': 443,
        'IpProtocol': 'tcp',
        'ToPort': 443,
    }]
    vpc_id = ref(VPCId)
