"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Parameter,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import iotanalytics
from cloudformation_dataclasses.intrinsics import Sub
from .params import *  # noqa: F403, F401

from .main import Channel as Channel
from .main import Datastore as Datastore
from .main import Pipeline as Pipeline
from .main import PipelineActivity as PipelineActivity
from .main import PipelineChannel as PipelineChannel
from .main import PipelineDatastore as PipelineDatastore
from .main import SqlDataset as SqlDataset
from .main import SqlDatasetAction as SqlDatasetAction
from .main import SqlDatasetQueryAction as SqlDatasetQueryAction
from .main import SqlDatasetRetentionPeriod as SqlDatasetRetentionPeriod
from .main import SqlDatasetSchedule as SqlDatasetSchedule
from .main import SqlDatasetTrigger as SqlDatasetTrigger
from .params import ProjectName as ProjectName
from .params import ScheduleExpression as ScheduleExpression
from .params import SqlQuery as SqlQuery

__all__: list[str] = ['Channel', 'Datastore', 'Parameter', 'Pipeline', 'PipelineActivity', 'PipelineChannel', 'PipelineDatastore', 'ProjectName', 'STRING', 'ScheduleExpression', 'SqlDataset', 'SqlDatasetAction', 'SqlDatasetQueryAction', 'SqlDatasetRetentionPeriod', 'SqlDatasetSchedule', 'SqlDatasetTrigger', 'SqlQuery', 'Sub', 'Template', 'cloudformation_dataclass', 'get_att', 'iotanalytics', 'ref', 'setup_resources']
