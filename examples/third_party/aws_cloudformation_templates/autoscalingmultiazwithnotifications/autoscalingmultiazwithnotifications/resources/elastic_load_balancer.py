from __future__ import annotations

"""ElasticLoadBalancer - AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ElasticLoadBalancer:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    resource: LoadBalancer
    scheme = 'internet-facing'
    security_groups = [ref(LoadBalancerSecurityGroup)]
    subnets = ref(Subnets)
    type_ = 'application'
