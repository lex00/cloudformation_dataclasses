"""TaskDefinition - AWS::ECS::TaskDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TaskDefinitionPortMapping:
    resource: PortMapping
    container_port = ref(ContainerPort)


@cloudformation_dataclass
class TaskDefinitionContainerDefinition:
    resource: ContainerDefinition
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
