from __future__ import annotations

"""WebServerGroup - AWS::AutoScaling::AutoScalingGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class WebServerGroupLaunchTemplateSpecification:
    resource: LaunchTemplateSpecification
    launch_template_id: Ref[LaunchTemplate] = ref()
    version: GetAtt[LaunchTemplate] = get_att("LatestVersionNumber")


@cloudformation_dataclass
class WebServerGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: AutoScalingGroup
    availability_zones = GetAZs()
    launch_template = WebServerGroupLaunchTemplateSpecification
    min_size = 2
    max_size = 4
    load_balancer_names = [ref("ElasticLoadBalancer")]
