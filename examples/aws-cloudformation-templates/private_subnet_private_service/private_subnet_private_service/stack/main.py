"""Stack resources."""

from .. import *  # noqa: F403


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
class TargetGroup:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    health_check_interval_seconds = 6
    health_check_path = '/'
    health_check_protocol = 'HTTP'
    health_check_timeout_seconds = 5
    healthy_threshold_count = 2
    target_type = 'ip'
    name = ref(ServiceName)
    port = ref(ContainerPort)
    protocol = 'HTTP'
    unhealthy_threshold_count = 2
    vpc_id = ImportValue(Join(':', [
    ref(StackName),
    'VPCId',
]))


@cloudformation_dataclass
class ServiceDeploymentConfiguration:
    resource: ecs.service.DeploymentConfiguration
    maximum_percent = 200
    minimum_healthy_percent = 75


@cloudformation_dataclass
class ServiceAwsVpcConfiguration:
    resource: ecs.service.AwsVpcConfiguration
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


@cloudformation_dataclass
class LoadBalancerRuleAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    target_group_arn = ref(TargetGroup)
    type_ = 'forward'


@cloudformation_dataclass
class LoadBalancerRuleRuleCondition:
    resource: elasticloadbalancingv2.listener_rule.RuleCondition
    field = 'path-pattern'
    values = [ref(Path)]


@cloudformation_dataclass
class LoadBalancerRule:
    """AWS::ElasticLoadBalancingV2::ListenerRule resource."""

    resource: elasticloadbalancingv2.ListenerRule
    actions = [LoadBalancerRuleAction]
    conditions = [LoadBalancerRuleRuleCondition]
    listener_arn = ImportValue(Join(':', [
    ref(StackName),
    'PrivateListener',
]))
    priority = ref(Priority)
