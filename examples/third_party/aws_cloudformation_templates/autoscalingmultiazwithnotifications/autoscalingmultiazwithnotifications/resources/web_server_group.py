from __future__ import annotations

"""WebServerGroup - AWS::AutoScaling::AutoScalingGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class WebServerGroupLaunchTemplateSpecification:
    resource: LaunchTemplateSpecification
    launch_template_id: Ref[LaunchTemplate] = ref()
    version: GetAtt[LaunchTemplate] = get_att("LatestVersionNumber")


@cloudformation_dataclass
class WebServerGroupNotificationConfiguration:
    resource: NotificationConfiguration
    topic_arn: Ref[NotificationTopic] = ref()
    notification_types = ['autoscaling:EC2_INSTANCE_LAUNCH', 'autoscaling:EC2_INSTANCE_LAUNCH_ERROR', 'autoscaling:EC2_INSTANCE_TERMINATE', 'autoscaling:EC2_INSTANCE_TERMINATE_ERROR']


@cloudformation_dataclass
class WebServerGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: AutoScalingGroup
    availability_zones = ref(AZs)
    launch_template = WebServerGroupLaunchTemplateSpecification
    min_size = '1'
    max_size = '3'
    target_group_ar_ns = [ref("TargetGroup")]
    notification_configurations = [WebServerGroupNotificationConfiguration]
    health_check_type = 'ELB'
    vpc_zone_identifier = ref(Subnets)
