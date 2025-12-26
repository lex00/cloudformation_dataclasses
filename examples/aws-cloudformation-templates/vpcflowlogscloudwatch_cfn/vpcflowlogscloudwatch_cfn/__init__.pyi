"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    Parameter,
    ParameterType,
    PolicyDocument,
    PolicyStatement,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.template import Condition as TemplateCondition
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import ec2, iam, logs
from cloudformation_dataclasses.intrinsics import (
    AWS_NO_VALUE,
    AWS_STACK_NAME,
    Equals,
    If,
    Not,
)

from .compute import VPCFlowLogsToCloudWatch as VPCFlowLogsToCloudWatch
from .compute import VPCFlowLogsToCloudWatchAssociationParameter as VPCFlowLogsToCloudWatchAssociationParameter
from .monitoring import VPCFlowLogsLogGroup as VPCFlowLogsLogGroup
from .outputs import VPCFlowLogsLogGroupOutput as VPCFlowLogsLogGroupOutput
from .params import VPCFlowLogsCloudWatchKMSKey as VPCFlowLogsCloudWatchKMSKey
from .params import VPCFlowLogsCloudWatchKMSKeyConditionCondition as VPCFlowLogsCloudWatchKMSKeyConditionCondition
from .params import VPCFlowLogsLogFormat as VPCFlowLogsLogFormat
from .params import VPCFlowLogsLogGroupRetention as VPCFlowLogsLogGroupRetention
from .params import VPCFlowLogsMaxAggregationInterval as VPCFlowLogsMaxAggregationInterval
from .params import VPCFlowLogsTrafficType as VPCFlowLogsTrafficType
from .params import VPCID as VPCID
from .security import VPCFlowLogsRole as VPCFlowLogsRole
from .security import VPCFlowLogsRoleAllowStatement0 as VPCFlowLogsRoleAllowStatement0
from .security import VPCFlowLogsRoleAllowStatement0_1 as VPCFlowLogsRoleAllowStatement0_1
from .security import VPCFlowLogsRoleAssumeRolePolicyDocument as VPCFlowLogsRoleAssumeRolePolicyDocument
from .security import VPCFlowLogsRolePolicies0PolicyDocument as VPCFlowLogsRolePolicies0PolicyDocument
from .security import VPCFlowLogsRolePolicy as VPCFlowLogsRolePolicy

__all__: list[str] = ['AWS_NO_VALUE', 'AWS_STACK_NAME', 'Equals', 'If', 'Not', 'Output', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'STRING', 'Template', 'TemplateCondition', 'VPCFlowLogsCloudWatchKMSKey', 'VPCFlowLogsCloudWatchKMSKeyConditionCondition', 'VPCFlowLogsLogFormat', 'VPCFlowLogsLogGroup', 'VPCFlowLogsLogGroupOutput', 'VPCFlowLogsLogGroupRetention', 'VPCFlowLogsMaxAggregationInterval', 'VPCFlowLogsRole', 'VPCFlowLogsRoleAllowStatement0', 'VPCFlowLogsRoleAllowStatement0_1', 'VPCFlowLogsRoleAssumeRolePolicyDocument', 'VPCFlowLogsRolePolicies0PolicyDocument', 'VPCFlowLogsRolePolicy', 'VPCFlowLogsToCloudWatch', 'VPCFlowLogsToCloudWatchAssociationParameter', 'VPCFlowLogsTrafficType', 'VPCID', 'cloudformation_dataclass', 'ec2', 'get_att', 'iam', 'logs', 'ref', 'setup_resources']
