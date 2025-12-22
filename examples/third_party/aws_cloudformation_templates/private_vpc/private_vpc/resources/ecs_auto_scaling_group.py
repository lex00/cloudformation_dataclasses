from __future__ import annotations

"""ECSAutoScalingGroup - AWS::AutoScaling::AutoScalingGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ECSAutoScalingGroupLaunchTemplateSpecification:
    resource: LaunchTemplateSpecification
    launch_template_id: Ref[ContainerInstances] = ref()
    version: GetAtt[ContainerInstances] = get_att("LatestVersionNumber")


@cloudformation_dataclass
class ECSAutoScalingGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: AutoScalingGroup
    vpc_zone_identifier = [ref("PrivateSubnetOne"), ref("PrivateSubnetTwo")]
    launch_template = ECSAutoScalingGroupLaunchTemplateSpecification
    min_size = 1
    max_size = ref(MaxSize)
    desired_capacity = ref(DesiredCapacity)
