"""ECSAutoScalingGroup - AWS::AutoScaling::AutoScalingGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ECSAutoScalingGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: autoscaling.AutoScalingGroup
    vpc_zone_identifier = [ref(PrivateSubnetOne), ref(PrivateSubnetTwo)]
    launch_template = {
        'LaunchTemplateId': ref(ContainerInstances),
        'Version': get_att(ContainerInstances, "LatestVersionNumber"),
    }
    min_size = 1
    max_size = ref(MaxSize)
    desired_capacity = ref(DesiredCapacity)
