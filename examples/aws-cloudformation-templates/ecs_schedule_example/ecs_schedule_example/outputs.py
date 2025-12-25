"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class EcsServiceOutput:
    resource: Output
    value = ref(Service)


@cloudformation_dataclass
class EcsClusterOutput:
    resource: Output
    value = ref(ECSCluster)


@cloudformation_dataclass
class EcsTaskDefOutput:
    resource: Output
    value = ref(TaskDefinition)


@cloudformation_dataclass
class ECSALBOutput:
    """Your ALB DNS URL"""

    resource: Output
    value = Join('', [get_att(ECSALB, "DNSName")])
    description = 'Your ALB DNS URL'
