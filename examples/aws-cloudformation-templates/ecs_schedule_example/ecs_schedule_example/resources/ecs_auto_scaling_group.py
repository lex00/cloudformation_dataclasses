"""ECSAutoScalingGroup - AWS::AutoScaling::AutoScalingGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ECSAutoScalingGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: AutoScalingGroup
    vpc_zone_identifier = ref(SubnetId)
    launch_configuration_name = ref(ContainerInstances)
    min_size = '1'
    max_size = ref(MaxSize)
    desired_capacity = ref(DesiredCapacity)
