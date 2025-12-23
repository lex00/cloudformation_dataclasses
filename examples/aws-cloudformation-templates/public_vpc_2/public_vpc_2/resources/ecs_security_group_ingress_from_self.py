"""EcsSecurityGroupIngressFromSelf - AWS::EC2::SecurityGroupIngress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EcsSecurityGroupIngressFromSelf:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    description = 'Ingress from other containers in the same security group'
    group_id = ref(FargateContainerSecurityGroup)
    ip_protocol = '-1'
    source_security_group_id = ref(FargateContainerSecurityGroup)
