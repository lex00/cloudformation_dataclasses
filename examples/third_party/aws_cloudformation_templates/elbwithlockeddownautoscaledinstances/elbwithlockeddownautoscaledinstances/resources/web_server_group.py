from __future__ import annotations

"""WebServerGroup - AWS::AutoScaling::AutoScalingGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class WebServerGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: AutoScalingGroup
    availability_zones = GetAZs()
    launch_configuration_name: Ref[LaunchConfig] = ref()
    min_size = '2'
    max_size = '2'
    load_balancer_names = [ref("ElasticLoadBalancer")]
