"""Fargate resources - ECS cluster, task definition, and service."""

from .. import *  # noqa: F403, F401


@cloudformation_dataclass
class EcsCluster:
    """ECS cluster for Fargate tasks."""

    resource: ecs.Cluster

@cloudformation_dataclass
class WebContainerPortMapping:
    resource: ecs.task_definition.PortMapping
    container_port = 80
    protocol = "tcp"

@cloudformation_dataclass
class WebContainerLogConfig:
    resource: ecs.task_definition.LogConfiguration
    log_driver = "awslogs"
    options = {
        "awslogs-group": ref(EcsLogGroup),
        "awslogs-region": AWS_REGION,
        "awslogs-stream-prefix": "webapp",
    }

@cloudformation_dataclass
class WebContainerDbEnv:
    resource: ecs.task_definition.KeyValuePair
    name = "DB_HOST"
    value = ref(DbEndpointParam)

@cloudformation_dataclass
class WebContainerDefinition:
    resource: ecs.task_definition.ContainerDefinition
    name = "webapp"
    image = "nginx:alpine"
    essential = True
    port_mappings = [WebContainerPortMapping]
    log_configuration = WebContainerLogConfig
    environment = [WebContainerDbEnv]

@cloudformation_dataclass
class WebTaskDefinition:
    """Task definition for the web application."""

    resource: ecs.TaskDefinition
    family = "webapp"
    requires_compatibilities = ["FARGATE"]
    network_mode = "awsvpc"
    cpu = "256"
    memory = "512"
    execution_role_arn = get_att(TaskExecutionRole, "Arn")
    task_role_arn = get_att(TaskRole, "Arn")
    container_definitions = [WebContainerDefinition]

@cloudformation_dataclass
class ServiceVpcConfig:
    resource: ecs.service.AwsVpcConfiguration
    assign_public_ip = "DISABLED"
    subnets = ref(PrivateSubnetIdsParam)
    security_groups = [ref(TaskSecurityGroup)]

@cloudformation_dataclass
class ServiceNetworkConfig:
    resource: ecs.service.NetworkConfiguration
    awsvpc_configuration = ServiceVpcConfig

@cloudformation_dataclass
class ServiceLoadBalancer:
    resource: ecs.service.LoadBalancer
    target_group_arn = ref(TargetGroupArnParam)
    container_name = "webapp"
    container_port = 80

@cloudformation_dataclass
class WebService:
    """ECS service running the web application."""

    resource: ecs.Service
    cluster = ref(EcsCluster)
    desired_count = 2
    launch_type = "FARGATE"
    task_definition = ref(WebTaskDefinition)
    health_check_grace_period_seconds = 60
    network_configuration = ServiceNetworkConfig
    load_balancers = [ServiceLoadBalancer]
