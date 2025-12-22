"""WebServerGroup - AWS::AutoScaling::AutoScalingGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class WebServerGroupLaunchTemplateSpecification:
    resource: autoscaling.LaunchTemplateSpecification
    launch_template_id = ref(LaunchTemplate)
    version = get_att(LaunchTemplate, "LatestVersionNumber")


@cloudformation_dataclass
class WebServerGroupNotificationConfiguration:
    resource: autoscaling.NotificationConfiguration
    topic_arn = ref(NotificationTopic)
    notification_types = ['autoscaling:EC2_INSTANCE_LAUNCH', 'autoscaling:EC2_INSTANCE_LAUNCH_ERROR', 'autoscaling:EC2_INSTANCE_TERMINATE', 'autoscaling:EC2_INSTANCE_TERMINATE_ERROR']


@cloudformation_dataclass
class WebServerGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: AutoScalingGroup
    availability_zones = ref(AZs)
    launch_template = WebServerGroupLaunchTemplateSpecification
    min_size = '1'
    max_size = '3'
    target_group_ar_ns = [ref(TargetGroup)]
    notification_configurations = [WebServerGroupNotificationConfiguration]
    health_check_type = 'ELB'
    vpc_zone_identifier = ref(Subnets)
