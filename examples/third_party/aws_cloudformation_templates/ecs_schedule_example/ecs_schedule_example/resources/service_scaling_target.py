from __future__ import annotations

"""ServiceScalingTarget - AWS::ApplicationAutoScaling::ScalableTarget resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceScalingTarget:
    """AWS::ApplicationAutoScaling::ScalableTarget resource."""

    resource: ScalableTarget
    max_capacity = 2
    min_capacity = 1
    resource_id = Join('', [
    'service/',
    ref("ECSCluster"),
    '/',
    get_att("Service", "Name"),
])
    role_arn: GetAtt[AutoscalingRole] = get_att("Arn")
    scalable_dimension = 'ecs:service:DesiredCount'
    service_namespace = 'ecs'
    depends_on = ["Service"]
