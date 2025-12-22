"""Service - AWS::ECS::Service resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceLoadBalancer:
    resource: ecs.task_set.LoadBalancer
    container_name = 'simple-app'
    container_port = '80'
    target_group_arn = ref(ECSTG)


@cloudformation_dataclass
class Service:
    """AWS::ECS::Service resource."""

    resource: ecs.Service
    cluster = ref(ECSCluster)
    desired_count = '1'
    load_balancers = [ServiceLoadBalancer]
    role = ref(ECSServiceRole)
    task_definition = ref(TaskDefinition)
    depends_on = ["ALBListener"]
