from __future__ import annotations

"""TargetGroup - AWS::ElasticLoadBalancingV2::TargetGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TargetGroup:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    health_check_interval_seconds = 6
    health_check_path = '/'
    health_check_protocol = 'HTTP'
    health_check_timeout_seconds = 5
    healthy_threshold_count = 2
    target_type = 'ip'
    name = ref(ServiceName)
    port = ref(ContainerPort)
    protocol = 'HTTP'
    unhealthy_threshold_count = 2
    vpc_id = ImportValue({
    'Fn::Join': [
        ':',
        [
            ref(StackName),
            'VPCId',
        ],
    ],
})
