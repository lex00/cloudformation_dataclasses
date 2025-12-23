"""WebServerGroup - AWS::AutoScaling::AutoScalingGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class WebServerGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: autoscaling.AutoScalingGroup
    availability_zones = ref(AZs)
    launch_template = {
        'LaunchTemplateId': ref(LaunchTemplate),
        'Version': get_att(LaunchTemplate, "LatestVersionNumber"),
    }
    min_size = '1'
    max_size = '3'
    target_group_ar_ns = [ref(TargetGroup)]
    notification_configurations = [{
        'TopicARN': ref(NotificationTopic),
        'NotificationTypes': [
            'autoscaling:EC2_INSTANCE_LAUNCH',
            'autoscaling:EC2_INSTANCE_LAUNCH_ERROR',
            'autoscaling:EC2_INSTANCE_TERMINATE',
            'autoscaling:EC2_INSTANCE_TERMINATE_ERROR',
        ],
    }]
    health_check_type = 'ELB'
    vpc_zone_identifier = ref(Subnets)
