"""AutoScalingGroup - AWS::AutoScaling::AutoScalingGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AutoScalingGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: autoscaling.AutoScalingGroup
    launch_configuration_name = ref(LaunchConfig)
    load_balancer_names = [ref(ElasticLoadBalancer)]
    max_size = '3'
    min_size = '1'
    vpc_zone_identifier = ref(Subnets)
