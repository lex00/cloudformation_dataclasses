from __future__ import annotations

"""PrivateLoadBalancer - AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateLoadBalancerLoadBalancerAttribute:
    resource: LoadBalancerAttribute
    key = 'idle_timeout.timeout_seconds'
    value = '30'


@cloudformation_dataclass
class PrivateLoadBalancer:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    resource: LoadBalancer
    scheme = 'internal'
    load_balancer_attributes = [PrivateLoadBalancerLoadBalancerAttribute]
    subnets = [ref("PrivateSubnetOne"), ref("PrivateSubnetTwo")]
    security_groups = [ref("PrivateLoadBalancerSG")]
