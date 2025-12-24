"""Messaging resources: ECSScheduledTask."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ECSScheduledTaskEcsParameters:
    resource: events.rule.EcsParameters
    task_count = ref(SchedulerTasksCount)
    task_definition_arn = ref(TaskDefinition)


@cloudformation_dataclass
class ECSScheduledTaskTarget:
    resource: events.rule.Target
    arn = get_att(ECSCluster, "Arn")
    id = 'Target1'
    role_arn = get_att(ECSEventRole, "Arn")
    ecs_parameters = ECSScheduledTaskEcsParameters


@cloudformation_dataclass
class ECSScheduledTask:
    """AWS::Events::Rule resource."""

    resource: events.Rule
    description = 'Creating a Schedule with CloudFormation as an example'
    schedule_expression = If("CronRate", ref(CronSchedule), ref(RateSchedule))
    state = 'ENABLED'
    targets = [ECSScheduledTaskTarget]
    depends_on = ["ECSEventRole"]
