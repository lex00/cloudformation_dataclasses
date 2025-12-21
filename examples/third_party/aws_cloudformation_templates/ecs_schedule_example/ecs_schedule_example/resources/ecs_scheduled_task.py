from __future__ import annotations

"""ECSScheduledTask - AWS::Events::Rule resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ECSScheduledTaskEcsParameters:
    resource: EcsParameters
    task_count = ref(SchedulerTasksCount)
    task_definition_arn: Ref[TaskDefinition] = ref()


@cloudformation_dataclass
class ECSScheduledTaskTarget:
    resource: Target
    arn: GetAtt[ECSCluster] = get_att("Arn")
    id = 'Target1'
    role_arn: GetAtt[ECSEventRole] = get_att("Arn")
    ecs_parameters = ECSScheduledTaskEcsParameters


@cloudformation_dataclass
class ECSScheduledTask:
    """AWS::Events::Rule resource."""

    resource: Rule
    description = 'Creating a Schedule with CloudFormation as an example'
    schedule_expression = If("CronRate", ref(CronSchedule), ref(RateSchedule))
    state = 'ENABLED'
    targets = [ECSScheduledTaskTarget]
    depends_on = ["ECSEventRole"]
