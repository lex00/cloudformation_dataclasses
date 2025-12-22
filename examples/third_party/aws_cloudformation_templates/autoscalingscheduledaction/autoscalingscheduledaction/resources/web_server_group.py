"""WebServerGroup - AWS::AutoScaling::AutoScalingGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class WebServerGroupLaunchTemplateSpecification:
    resource: autoscaling.LaunchTemplateSpecification
    launch_template_id = ref(LaunchTemplate)
    version = get_att(LaunchTemplate, "LatestVersionNumber")


@cloudformation_dataclass
class WebServerGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: AutoScalingGroup
    availability_zones = GetAZs()
    launch_template = WebServerGroupLaunchTemplateSpecification
    min_size = 2
    max_size = 5
    load_balancer_names = [ref(ElasticLoadBalancer)]
