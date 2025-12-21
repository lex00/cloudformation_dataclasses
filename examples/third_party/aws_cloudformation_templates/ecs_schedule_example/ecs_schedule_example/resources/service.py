from __future__ import annotations

"""Service - AWS::ECS::Service resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceLoadBalancer:
    resource: LoadBalancer
    container_name = 'simple-app'
    container_port = '80'
    target_group_arn: Ref[ECSTG] = ref()


@cloudformation_dataclass
class Service:
    """AWS::ECS::Service resource."""

    resource: ecs.Service
    cluster: Ref[ECSCluster] = ref()
    desired_count = '1'
    load_balancers = [ServiceLoadBalancer]
    role: Ref[ECSServiceRole] = ref()
    task_definition: Ref[TaskDefinition] = ref()
    depends_on = ["ALBListener"]
