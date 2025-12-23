"""ECSScheduledTask - AWS::Events::Rule resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ECSScheduledTask:
    """AWS::Events::Rule resource."""

    resource: events.Rule
    description = 'Creating a Schedule with CloudFormation as an example'
    schedule_expression = If("CronRate", ref(CronSchedule), ref(RateSchedule))
    state = 'ENABLED'
    targets = [{
        'Arn': get_att(ECSCluster, "Arn"),
        'Id': 'Target1',
        'RoleArn': get_att(ECSEventRole, "Arn"),
        'EcsParameters': {
            'TaskCount': ref(SchedulerTasksCount),
            'TaskDefinitionArn': ref(TaskDefinition),
        },
    }]
    depends_on = ["ECSEventRole"]
