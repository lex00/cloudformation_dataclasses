"""WebServerGroup - AWS::AutoScaling::AutoScalingGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class WebServerGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    # Unknown resource type: AWS::AutoScaling::AutoScalingGroup
    resource: CloudFormationResource
    availability_zones = GetAZs()
    launch_template = {
        'LaunchTemplateId': ref(LaunchTemplate),
        'Version': get_att(LaunchTemplate, "LatestVersionNumber"),
    }
    min_size = 2
    max_size = 4
    load_balancer_names = [ref(ElasticLoadBalancer)]
