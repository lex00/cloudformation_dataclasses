"""Compute resources: TaskDefinition, Service."""

from . import *  # noqa: F403


@cloudformation_dataclass
class TaskDefinitionPortMapping:
    resource: ecs.task_definition.PortMapping
    container_port = ref(ContainerPort)


@cloudformation_dataclass
class TaskDefinitionContainerDefinition:
    resource: ecs.task_definition.ContainerDefinition
    name = ref(ServiceName)
    essential = True
    cpu = ref(ContainerCpu)
    memory = ref(ContainerMemory)
    image = ref(ImageUrl)
    port_mappings = [TaskDefinitionPortMapping]


@cloudformation_dataclass
class TaskDefinition:
    """AWS::ECS::TaskDefinition resource."""

    resource: ecs.TaskDefinition
    family = ref(ServiceName)
    cpu = ref(ContainerCpu)
    memory = ref(ContainerMemory)
    network_mode = 'awsvpc'
    requires_compatibilities = ['FARGATE']
    execution_role_arn = ImportValue(Join(':', [
    ref(StackName),
    'ECSTaskExecutionRole',
]))
    task_role_arn = If("HasCustomRole", ref(Role), AWS_NO_VALUE)
    container_definitions = [TaskDefinitionContainerDefinition]


@cloudformation_dataclass
class ServiceDeploymentConfiguration:
    resource: ecs.service.DeploymentConfiguration
    maximum_percent = 200
    minimum_healthy_percent = 75


@cloudformation_dataclass
class ServiceAwsVpcConfiguration:
    resource: ecs.service.AwsVpcConfiguration
    assign_public_ip = 'ENABLED'
    security_groups = [ImportValue(Join(':', [
    ref(StackName),
    'FargateContainerSecurityGroup',
]))]
    subnets = [ImportValue(Join(':', [
    ref(StackName),
    'PrivateSubnetOne',
])), ImportValue(Join(':', [
    ref(StackName),
    'PrivateSubnetTwo',
]))]


@cloudformation_dataclass
class ServiceNetworkConfiguration:
    resource: ecs.service.NetworkConfiguration
    awsvpc_configuration = ServiceAwsVpcConfiguration


@cloudformation_dataclass
class ServiceLoadBalancer:
    resource: ecs.task_set.LoadBalancer
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
    launch_type = 'FARGATE'
    deployment_configuration = ServiceDeploymentConfiguration
    desired_count = ref(DesiredCount)
    network_configuration = ServiceNetworkConfiguration
    task_definition = ref(TaskDefinition)
    load_balancers = [ServiceLoadBalancer]
    depends_on = ["LoadBalancerRule"]
