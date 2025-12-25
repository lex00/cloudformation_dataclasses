"""Fargate stack - ECS service with task definition."""

from cloudformation_dataclasses.core import *  # noqa: F403, F401
from cloudformation_dataclasses.aws import ec2, ecs, iam, logs
from cloudformation_dataclasses.aws.ecs import service, task_definition

from .stack import *  # noqa: F403, F401
