"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Parameter,
    ParameterType,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.template import Condition as TemplateCondition
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import cloudformation
from cloudformation_dataclasses.intrinsics import Equals, Sub
from .params import *  # noqa: F403, F401

from .infra import VPCFlowLogsCloudWatchStack as VPCFlowLogsCloudWatchStack
from .infra import VPCFlowLogsS3Stack as VPCFlowLogsS3Stack
from .params import CreateVPCFlowLogsToCloudWatch as CreateVPCFlowLogsToCloudWatch
from .params import CreateVPCFlowLogsToS3 as CreateVPCFlowLogsToS3
from .params import S3AccessLogsBucketName as S3AccessLogsBucketName
from .params import TemplatesS3BucketName as TemplatesS3BucketName
from .params import TemplatesS3BucketRegion as TemplatesS3BucketRegion
from .params import VPCFlowLogsBucketKMSKey as VPCFlowLogsBucketKMSKey
from .params import VPCFlowLogsBucketKeyEnabled as VPCFlowLogsBucketKeyEnabled
from .params import VPCFlowLogsBucketName as VPCFlowLogsBucketName
from .params import VPCFlowLogsCloudWatchKMSKey as VPCFlowLogsCloudWatchKMSKey
from .params import VPCFlowLogsLogFormat as VPCFlowLogsLogFormat
from .params import VPCFlowLogsLogGroupRetention as VPCFlowLogsLogGroupRetention
from .params import VPCFlowLogsMaxAggregationInterval as VPCFlowLogsMaxAggregationInterval
from .params import VPCFlowLogsToCloudWatchConditionCondition as VPCFlowLogsToCloudWatchConditionCondition
from .params import VPCFlowLogsToS3ConditionCondition as VPCFlowLogsToS3ConditionCondition
from .params import VPCFlowLogsTrafficType as VPCFlowLogsTrafficType
from .params import VPCID as VPCID

__all__: list[str] = ['CreateVPCFlowLogsToCloudWatch', 'CreateVPCFlowLogsToS3', 'Equals', 'Parameter', 'ParameterType', 'S3AccessLogsBucketName', 'STRING', 'Sub', 'Template', 'TemplateCondition', 'TemplatesS3BucketName', 'TemplatesS3BucketRegion', 'VPCFlowLogsBucketKMSKey', 'VPCFlowLogsBucketKeyEnabled', 'VPCFlowLogsBucketName', 'VPCFlowLogsCloudWatchKMSKey', 'VPCFlowLogsCloudWatchStack', 'VPCFlowLogsLogFormat', 'VPCFlowLogsLogGroupRetention', 'VPCFlowLogsMaxAggregationInterval', 'VPCFlowLogsS3Stack', 'VPCFlowLogsToCloudWatchConditionCondition', 'VPCFlowLogsToS3ConditionCondition', 'VPCFlowLogsTrafficType', 'VPCID', 'cloudformation', 'cloudformation_dataclass', 'get_att', 'ref', 'setup_resources']
