"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    CloudFormationResource,
    Parameter,
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
from cloudformation_dataclasses.aws import iam, lambda_, logs
from cloudformation_dataclasses.intrinsics import (
    AWS_NO_VALUE,
    AWS_STACK_NAME,
    Equals,
    If,
    Not,
    Sub,
)
from .params import *  # noqa: F403, F401

from .compute import TagVpcPeeringConnectionsLambdaFunction as TagVpcPeeringConnectionsLambdaFunction
from .compute import TagVpcPeeringConnectionsLambdaFunctionCode as TagVpcPeeringConnectionsLambdaFunctionCode
from .compute import TagVpcPeeringConnectionsLambdaFunctionEnvironment as TagVpcPeeringConnectionsLambdaFunctionEnvironment
from .main import TagVpcPeeringConnectionsResource as TagVpcPeeringConnectionsResource
from .monitoring import TagVpcPeeringConnectionsLambdaLogsLogGroup as TagVpcPeeringConnectionsLambdaLogsLogGroup
from .params import LambdaFunctionName as LambdaFunctionName
from .params import LambdaLogLevel as LambdaLogLevel
from .params import LambdaLogsCloudWatchKMSKey as LambdaLogsCloudWatchKMSKey
from .params import LambdaLogsCloudWatchKMSKeyConditionCondition as LambdaLogsCloudWatchKMSKeyConditionCondition
from .params import LambdaLogsLogGroupRetention as LambdaLogsLogGroupRetention
from .params import PeerName as PeerName
from .params import VPCPeeringConnectionId as VPCPeeringConnectionId
from .security import TagVpcPeeringConnectionsLambdaRole as TagVpcPeeringConnectionsLambdaRole
from .security import TagVpcPeeringConnectionsLambdaRoleAllowStatement0 as TagVpcPeeringConnectionsLambdaRoleAllowStatement0
from .security import TagVpcPeeringConnectionsLambdaRoleAllowStatement0_1 as TagVpcPeeringConnectionsLambdaRoleAllowStatement0_1
from .security import TagVpcPeeringConnectionsLambdaRoleAllowStatement0_2 as TagVpcPeeringConnectionsLambdaRoleAllowStatement0_2
from .security import TagVpcPeeringConnectionsLambdaRoleAllowStatement1 as TagVpcPeeringConnectionsLambdaRoleAllowStatement1
from .security import TagVpcPeeringConnectionsLambdaRoleAssumeRolePolicyDocument as TagVpcPeeringConnectionsLambdaRoleAssumeRolePolicyDocument
from .security import TagVpcPeeringConnectionsLambdaRolePolicies0PolicyDocument as TagVpcPeeringConnectionsLambdaRolePolicies0PolicyDocument
from .security import TagVpcPeeringConnectionsLambdaRolePolicies1PolicyDocument as TagVpcPeeringConnectionsLambdaRolePolicies1PolicyDocument
from .security import TagVpcPeeringConnectionsLambdaRolePolicy as TagVpcPeeringConnectionsLambdaRolePolicy
from .security import TagVpcPeeringConnectionsLambdaRolePolicy1 as TagVpcPeeringConnectionsLambdaRolePolicy1

__all__: list[str] = ['AWS_NO_VALUE', 'AWS_STACK_NAME', 'CloudFormationResource', 'Equals', 'If', 'LambdaFunctionName', 'LambdaLogLevel', 'LambdaLogsCloudWatchKMSKey', 'LambdaLogsCloudWatchKMSKeyConditionCondition', 'LambdaLogsLogGroupRetention', 'Not', 'Parameter', 'PeerName', 'PolicyDocument', 'PolicyStatement', 'STRING', 'Sub', 'TagVpcPeeringConnectionsLambdaFunction', 'TagVpcPeeringConnectionsLambdaFunctionCode', 'TagVpcPeeringConnectionsLambdaFunctionEnvironment', 'TagVpcPeeringConnectionsLambdaLogsLogGroup', 'TagVpcPeeringConnectionsLambdaRole', 'TagVpcPeeringConnectionsLambdaRoleAllowStatement0', 'TagVpcPeeringConnectionsLambdaRoleAllowStatement0_1', 'TagVpcPeeringConnectionsLambdaRoleAllowStatement0_2', 'TagVpcPeeringConnectionsLambdaRoleAllowStatement1', 'TagVpcPeeringConnectionsLambdaRoleAssumeRolePolicyDocument', 'TagVpcPeeringConnectionsLambdaRolePolicies0PolicyDocument', 'TagVpcPeeringConnectionsLambdaRolePolicies1PolicyDocument', 'TagVpcPeeringConnectionsLambdaRolePolicy', 'TagVpcPeeringConnectionsLambdaRolePolicy1', 'TagVpcPeeringConnectionsResource', 'Template', 'TemplateCondition', 'VPCPeeringConnectionId', 'cloudformation_dataclass', 'get_att', 'iam', 'lambda_', 'logs', 'ref', 'setup_resources']
