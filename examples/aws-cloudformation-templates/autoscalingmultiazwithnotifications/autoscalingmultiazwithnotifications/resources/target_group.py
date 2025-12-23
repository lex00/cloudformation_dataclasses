"""TargetGroup - AWS::ElasticLoadBalancingV2::TargetGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TargetGroup:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    health_check_path = '/'
    name = 'MyTargetGroup'
    port = 80
    protocol = 'HTTP'
    target_type = 'instance'
    vpc_id = ref(VPC)
