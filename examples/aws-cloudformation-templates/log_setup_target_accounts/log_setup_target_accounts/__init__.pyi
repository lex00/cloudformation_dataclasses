"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    ARN_LIKE,
    Parameter,
    PolicyDocument,
    PolicyStatement,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import events, iam, sqs
from cloudformation_dataclasses.intrinsics import Sub

from .messaging import CloudFormationEventRule as CloudFormationEventRule
from .messaging import CloudFormationEventRuleDeadLetterConfig as CloudFormationEventRuleDeadLetterConfig
from .messaging import CloudFormationEventRuleTarget as CloudFormationEventRuleTarget
from .messaging import DeadLetterQueue as DeadLetterQueue
from .messaging import DeadLetterQueuePolicy as DeadLetterQueuePolicy
from .messaging import DeadLetterQueuePolicyAllowStatement0 as DeadLetterQueuePolicyAllowStatement0
from .messaging import DeadLetterQueuePolicyPolicyDocument as DeadLetterQueuePolicyPolicyDocument
from .params import CentralEventBusArn as CentralEventBusArn
from .security import EventBridgeRole as EventBridgeRole
from .security import EventBridgeRoleAllowStatement0 as EventBridgeRoleAllowStatement0
from .security import EventBridgeRoleAssumeRolePolicyDocument as EventBridgeRoleAssumeRolePolicyDocument
from .security import EventBridgeRolePolicy as EventBridgeRolePolicy
from .security import EventBridgeRolePolicyAllowStatement0 as EventBridgeRolePolicyAllowStatement0
from .security import EventBridgeRolePolicyPolicyDocument as EventBridgeRolePolicyPolicyDocument

__all__: list[str] = ['ARN_LIKE', 'CentralEventBusArn', 'CloudFormationEventRule', 'CloudFormationEventRuleDeadLetterConfig', 'CloudFormationEventRuleTarget', 'DeadLetterQueue', 'DeadLetterQueuePolicy', 'DeadLetterQueuePolicyAllowStatement0', 'DeadLetterQueuePolicyPolicyDocument', 'EventBridgeRole', 'EventBridgeRoleAllowStatement0', 'EventBridgeRoleAssumeRolePolicyDocument', 'EventBridgeRolePolicy', 'EventBridgeRolePolicyAllowStatement0', 'EventBridgeRolePolicyPolicyDocument', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'STRING', 'Sub', 'Template', 'cloudformation_dataclass', 'events', 'get_att', 'iam', 'ref', 'setup_resources', 'sqs']
