"""Fargate resources - ECS cluster, task definition, and service."""

from .. import *  # noqa: F403, F401


@cloudformation_dataclass
class TaskExecutionRoleAssumeStatement:
    resource: PolicyStatement
    effect = "Allow"
    principal = {"Service": "ecs-tasks.amazonaws.com"}
    action = "sts:AssumeRole"

@cloudformation_dataclass
class TaskExecutionRoleAssumePolicy:
    resource: PolicyDocument
    statement = [TaskExecutionRoleAssumeStatement]

@cloudformation_dataclass
class TaskExecutionRole:
    """IAM role for ECS task execution (pulling images, logging)."""

    resource: iam.Role
    assume_role_policy_document = TaskExecutionRoleAssumePolicy
    managed_policy_arns = [
        "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy",
    ]

@cloudformation_dataclass
class TaskRoleAssumeStatement:
    resource: PolicyStatement
    effect = "Allow"
    principal = {"Service": "ecs-tasks.amazonaws.com"}
    action = "sts:AssumeRole"

@cloudformation_dataclass
class TaskRoleAssumePolicy:
    resource: PolicyDocument
    statement = [TaskRoleAssumeStatement]

@cloudformation_dataclass
class TaskRole:
    """IAM role for ECS task (application permissions)."""

    resource: iam.Role
    assume_role_policy_document = TaskRoleAssumePolicy
