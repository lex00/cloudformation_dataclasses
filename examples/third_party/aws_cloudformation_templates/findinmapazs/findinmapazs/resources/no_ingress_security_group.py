"""NoIngressSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NoIngressSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_name = 'no-ingress-sg'
    group_description = 'Security group with no ingress rule'
    vpc_id = ref(VPC)
