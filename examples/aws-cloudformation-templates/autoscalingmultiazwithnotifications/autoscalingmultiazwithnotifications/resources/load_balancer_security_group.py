"""LoadBalancerSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoadBalancerSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    # Unknown resource type: AWS::EC2::SecurityGroup
    resource: CloudFormationResource
    group_description = 'Allows inbound traffic on port 443'
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': 443,
        'ToPort': 443,
        'CidrIp': '0.0.0.0/0',
    }]
    vpc_id = ref(VPC)
