from __future__ import annotations

"""PrivateLoadBalancerSG - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateLoadBalancerSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'Access to the internal load balancer'
    vpc_id: Ref[VPC] = ref()
