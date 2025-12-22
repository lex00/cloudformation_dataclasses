from __future__ import annotations

"""Service - AWS::ECS::Service resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServiceDeploymentConfiguration:
    resource: DeploymentConfiguration
    maximum_percent = 200
    minimum_healthy_percent = 75


@cloudformation_dataclass
class ServiceLoadBalancer:
    resource: LoadBalancer
    container_name = ref(ServiceName)
    container_port = ref(ContainerPort)
    target_group_arn = ref(TargetGroup)


@cloudformation_dataclass
class Service:
    """AWS::ECS::Service resource."""

    resource: ecs.Service
    service_name = ref(ServiceName)
    cluster = ImportValue(Join(':', [
    ref(StackName),
    'ClusterName',
]))
    deployment_configuration = ServiceDeploymentConfiguration
    desired_count = ref(DesiredCount)
    task_definition = ref(TaskDefinition)
    load_balancers = [ServiceLoadBalancer]
    depends_on = ["LoadBalancerRule"]
