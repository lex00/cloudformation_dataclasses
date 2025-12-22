from __future__ import annotations

"""TaskDefinition - AWS::ECS::TaskDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TaskDefinitionLogConfiguration:
    resource: LogConfiguration
    log_driver = 'awslogs'
    options = {
        'awslogs-group': ref("CloudwatchLogsGroup"),
        'awslogs-region': AWS_REGION,
        'awslogs-stream-prefix': 'ecs-demo-app',
    }


@cloudformation_dataclass
class TaskDefinitionMountPoint:
    resource: MountPoint
    container_path = '/usr/local/apache2/htdocs'
    source_volume = 'my-vol'


@cloudformation_dataclass
class TaskDefinitionPortMapping:
    resource: PortMapping
    container_port = 80


@cloudformation_dataclass
class TaskDefinitionContainerDefinition:
    resource: ContainerDefinition
    name = 'simple-app'
    cpu = '10'
    essential = 'true'
    image = 'httpd:2.4'
    memory = '300'
    log_configuration = TaskDefinitionLogConfiguration
    mount_points = [TaskDefinitionMountPoint]
    port_mappings = [TaskDefinitionPortMapping]


@cloudformation_dataclass
class TaskDefinitionLogConfiguration1:
    resource: LogConfiguration
    log_driver = 'awslogs'
    options = {
        'awslogs-group': ref("CloudwatchLogsGroup"),
        'awslogs-region': AWS_REGION,
        'awslogs-stream-prefix': 'ecs-demo-app',
    }


@cloudformation_dataclass
class TaskDefinitionVolumeFrom:
    resource: VolumeFrom
    source_container = 'simple-app'


@cloudformation_dataclass
class TaskDefinitionContainerDefinition1:
    resource: ContainerDefinition
    name = 'busybox'
    cpu = 10
    command = ['/bin/sh -c "while true; do echo \'<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p>\' > top; /bin/date > date ; echo \'</div></body></html>\' > bottom; cat top date bottom > /usr/local/apache2/htdocs/index.html ; sleep 1; done"']
    entry_point = ['sh', '-c']
    essential = False
    image = 'busybox'
    memory = 200
    log_configuration = TaskDefinitionLogConfiguration1
    volumes_from = [TaskDefinitionVolumeFrom]


@cloudformation_dataclass
class TaskDefinitionVolume:
    resource: Volume
    name = 'my-vol'


@cloudformation_dataclass
class TaskDefinition:
    """AWS::ECS::TaskDefinition resource."""

    resource: ecs.TaskDefinition
    family = Join('', [
    AWS_STACK_NAME,
    '-ecs-demo-app',
])
    container_definitions = [TaskDefinitionContainerDefinition, TaskDefinitionContainerDefinition1]
    volumes = [TaskDefinitionVolume]
