"""Fargate resources - ECS cluster, task definition, and service."""

from .. import *  # noqa: F403, F401


@cloudformation_dataclass
class EcsLogGroup:
    """CloudWatch Log Group for ECS tasks."""

    resource: logs.LogGroup
    retention_in_days = 30
