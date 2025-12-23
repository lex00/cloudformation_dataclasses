"""Configuration - Parameters, Mappings, Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class ProjectName:
    resource: Parameter
    type = STRING
    default = 'myIoTAnalyticsProject'


@cloudformation_dataclass
class SqlQuery:
    resource: Parameter
    type = STRING
    default = 'select * from myIoTAnalyticsProject_datastore '


@cloudformation_dataclass
class ScheduleExpression:
    resource: Parameter
    type = STRING
    default = 'cron(1/5 * * * ? *)'
