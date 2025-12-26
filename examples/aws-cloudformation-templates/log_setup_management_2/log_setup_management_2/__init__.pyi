"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
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
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import (
    cloudformation,
    events,
    kms,
    logs,
    sqs,
)
from cloudformation_dataclasses.intrinsics import Sub

from .infra import TargetAccountLogging as TargetAccountLogging
from .infra import TargetAccountLoggingAutoDeployment as TargetAccountLoggingAutoDeployment
from .infra import TargetAccountLoggingDeploymentTargets as TargetAccountLoggingDeploymentTargets
from .infra import TargetAccountLoggingOperationPreferences as TargetAccountLoggingOperationPreferences
from .infra import TargetAccountLoggingParameter as TargetAccountLoggingParameter
from .infra import TargetAccountLoggingParameter1 as TargetAccountLoggingParameter1
from .infra import TargetAccountLoggingStackInstances as TargetAccountLoggingStackInstances
from .main import CentralEventBus as CentralEventBus
from .main import CentralEventBusDeadLetterConfig as CentralEventBusDeadLetterConfig
from .main import CentralEventBusPolicy as CentralEventBusPolicy
from .main import CentralEventLog as CentralEventLog
from .main import CentralEventLogPolicy as CentralEventLogPolicy
from .main import CentralEventLogQuery as CentralEventLogQuery
from .main import CentralEventLogQueryReason as CentralEventLogQueryReason
from .main import CentralEventRule as CentralEventRule
from .main import CentralEventRuleDeadLetterConfig as CentralEventRuleDeadLetterConfig
from .main import CentralEventRuleTarget as CentralEventRuleTarget
from .main import DeadLetterQueue as DeadLetterQueue
from .params import CentralEventBusName as CentralEventBusName
from .params import CentralEventLogName as CentralEventLogName
from .params import KmsKeyId as KmsKeyId
from .params import OUID as OUID
from .params import OrgID as OrgID
from .params import StackSetRegions as StackSetRegions
from .security import CentralEventLogKey as CentralEventLogKey
from .security import CentralEventLogKeyAllowStatement0 as CentralEventLogKeyAllowStatement0
from .security import CentralEventLogKeyAllowStatement1 as CentralEventLogKeyAllowStatement1
from .security import CentralEventLogKeyKeyPolicy as CentralEventLogKeyKeyPolicy

__all__: list[str] = ['CentralEventBus', 'CentralEventBusDeadLetterConfig', 'CentralEventBusName', 'CentralEventBusPolicy', 'CentralEventLog', 'CentralEventLogKey', 'CentralEventLogKeyAllowStatement0', 'CentralEventLogKeyAllowStatement1', 'CentralEventLogKeyKeyPolicy', 'CentralEventLogName', 'CentralEventLogPolicy', 'CentralEventLogQuery', 'CentralEventLogQueryReason', 'CentralEventRule', 'CentralEventRuleDeadLetterConfig', 'CentralEventRuleTarget', 'DeadLetterQueue', 'KmsKeyId', 'OUID', 'OrgID', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'STRING', 'StackSetRegions', 'Sub', 'TargetAccountLogging', 'TargetAccountLoggingAutoDeployment', 'TargetAccountLoggingDeploymentTargets', 'TargetAccountLoggingOperationPreferences', 'TargetAccountLoggingParameter', 'TargetAccountLoggingParameter1', 'TargetAccountLoggingStackInstances', 'Template', 'cloudformation', 'cloudformation_dataclass', 'events', 'get_att', 'kms', 'logs', 'ref', 'setup_resources', 'sqs']
