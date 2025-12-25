"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    CloudFormationResource,
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
from cloudformation_dataclasses.aws import (
    iam,
    lambda_,
    logs,
    sns,
)
from cloudformation_dataclasses.intrinsics import (
    AWS_NO_VALUE,
    AWS_STACK_NAME,
    Equals,
    If,
    Not,
    Sub,
)
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .compute import DirectorySettingsLambdaFunction as DirectorySettingsLambdaFunction
from .compute import DirectorySettingsLambdaFunctionCapacityProviderVpcConfig as DirectorySettingsLambdaFunctionCapacityProviderVpcConfig
from .compute import DirectorySettingsLambdaFunctionContent as DirectorySettingsLambdaFunctionContent
from .compute import DirectorySettingsLambdaFunctionEnvironment as DirectorySettingsLambdaFunctionEnvironment
from .main import DirectorySettingsResource as DirectorySettingsResource
from .messaging import DirectoryMonitoringTopic as DirectoryMonitoringTopic
from .messaging import DirectoryMonitoringTopicSubscription as DirectoryMonitoringTopicSubscription
from .monitoring import DirectorySettingsLambdaLogsLogGroup as DirectorySettingsLambdaLogsLogGroup
from .outputs import DirectoryAliasUrlOutput as DirectoryAliasUrlOutput
from .params import CreateDirectoryAlias as CreateDirectoryAlias
from .params import CreateDirectoryConsoleDelegatedAccessRoles as CreateDirectoryConsoleDelegatedAccessRoles
from .params import DirectoryAlias as DirectoryAlias
from .params import DirectoryConsoleDelegatedAccessRolesConditionCondition as DirectoryConsoleDelegatedAccessRolesConditionCondition
from .params import DirectoryID as DirectoryID
from .params import DirectoryMonitoringEmail as DirectoryMonitoringEmail
from .params import DirectoryMonitoringSNSTopicKMSKey as DirectoryMonitoringSNSTopicKMSKey
from .params import DirectoryMonitoringSNSTopicKMSKeyConditionCondition as DirectoryMonitoringSNSTopicKMSKeyConditionCondition
from .params import EnableDirectorySSO as EnableDirectorySSO
from .params import LambdaFunctionName as LambdaFunctionName
from .params import LambdaLogLevel as LambdaLogLevel
from .params import LambdaLogsCloudWatchKMSKey as LambdaLogsCloudWatchKMSKey
from .params import LambdaLogsCloudWatchKMSKeyConditionCondition as LambdaLogsCloudWatchKMSKeyConditionCondition
from .params import LambdaLogsLogGroupRetention as LambdaLogsLogGroupRetention
from .params import LambdaS3BucketName as LambdaS3BucketName
from .params import LambdaZipFileName as LambdaZipFileName
from .params import SecurityGroups as SecurityGroups
from .params import Subnets as Subnets
from .security import DirectoryConsoleDelegatedAccessEC2ReadOnlyRole as DirectoryConsoleDelegatedAccessEC2ReadOnlyRole
from .security import DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAllowStatement0 as DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAllowStatement0
from .security import DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAssumeRolePolicyDocument as DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAssumeRolePolicyDocument
from .security import DirectoryConsoleDelegatedAccessSecurityAuditRole as DirectoryConsoleDelegatedAccessSecurityAuditRole
from .security import DirectoryConsoleDelegatedAccessSecurityAuditRoleAllowStatement0 as DirectoryConsoleDelegatedAccessSecurityAuditRoleAllowStatement0
from .security import DirectoryConsoleDelegatedAccessSecurityAuditRoleAssumeRolePolicyDocument as DirectoryConsoleDelegatedAccessSecurityAuditRoleAssumeRolePolicyDocument
from .security import DirectorySettingsLambdaRole as DirectorySettingsLambdaRole
from .security import DirectorySettingsLambdaRoleAllowStatement0 as DirectorySettingsLambdaRoleAllowStatement0
from .security import DirectorySettingsLambdaRoleAllowStatement0_1 as DirectorySettingsLambdaRoleAllowStatement0_1
from .security import DirectorySettingsLambdaRoleAllowStatement0_2 as DirectorySettingsLambdaRoleAllowStatement0_2
from .security import DirectorySettingsLambdaRoleAllowStatement1 as DirectorySettingsLambdaRoleAllowStatement1
from .security import DirectorySettingsLambdaRoleAllowStatement1_1 as DirectorySettingsLambdaRoleAllowStatement1_1
from .security import DirectorySettingsLambdaRoleAllowStatement2 as DirectorySettingsLambdaRoleAllowStatement2
from .security import DirectorySettingsLambdaRoleAssumeRolePolicyDocument as DirectorySettingsLambdaRoleAssumeRolePolicyDocument
from .security import DirectorySettingsLambdaRolePolicies0PolicyDocument as DirectorySettingsLambdaRolePolicies0PolicyDocument
from .security import DirectorySettingsLambdaRolePolicies1PolicyDocument as DirectorySettingsLambdaRolePolicies1PolicyDocument
from .security import DirectorySettingsLambdaRolePolicy as DirectorySettingsLambdaRolePolicy
from .security import DirectorySettingsLambdaRolePolicy1 as DirectorySettingsLambdaRolePolicy1

__all__: list[str] = ['AWS_NO_VALUE', 'AWS_STACK_NAME', 'CloudFormationResource', 'CreateDirectoryAlias', 'CreateDirectoryConsoleDelegatedAccessRoles', 'DirectoryAlias', 'DirectoryAliasUrlOutput', 'DirectoryConsoleDelegatedAccessEC2ReadOnlyRole', 'DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAllowStatement0', 'DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAssumeRolePolicyDocument', 'DirectoryConsoleDelegatedAccessRolesConditionCondition', 'DirectoryConsoleDelegatedAccessSecurityAuditRole', 'DirectoryConsoleDelegatedAccessSecurityAuditRoleAllowStatement0', 'DirectoryConsoleDelegatedAccessSecurityAuditRoleAssumeRolePolicyDocument', 'DirectoryID', 'DirectoryMonitoringEmail', 'DirectoryMonitoringSNSTopicKMSKey', 'DirectoryMonitoringSNSTopicKMSKeyConditionCondition', 'DirectoryMonitoringTopic', 'DirectoryMonitoringTopicSubscription', 'DirectorySettingsLambdaFunction', 'DirectorySettingsLambdaFunctionCapacityProviderVpcConfig', 'DirectorySettingsLambdaFunctionContent', 'DirectorySettingsLambdaFunctionEnvironment', 'DirectorySettingsLambdaLogsLogGroup', 'DirectorySettingsLambdaRole', 'DirectorySettingsLambdaRoleAllowStatement0', 'DirectorySettingsLambdaRoleAllowStatement0_1', 'DirectorySettingsLambdaRoleAllowStatement0_2', 'DirectorySettingsLambdaRoleAllowStatement1', 'DirectorySettingsLambdaRoleAllowStatement1_1', 'DirectorySettingsLambdaRoleAllowStatement2', 'DirectorySettingsLambdaRoleAssumeRolePolicyDocument', 'DirectorySettingsLambdaRolePolicies0PolicyDocument', 'DirectorySettingsLambdaRolePolicies1PolicyDocument', 'DirectorySettingsLambdaRolePolicy', 'DirectorySettingsLambdaRolePolicy1', 'DirectorySettingsResource', 'EnableDirectorySSO', 'Equals', 'If', 'LambdaFunctionName', 'LambdaLogLevel', 'LambdaLogsCloudWatchKMSKey', 'LambdaLogsCloudWatchKMSKeyConditionCondition', 'LambdaLogsLogGroupRetention', 'LambdaS3BucketName', 'LambdaZipFileName', 'Not', 'Output', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'STRING', 'SecurityGroups', 'Sub', 'Subnets', 'Template', 'TemplateCondition', 'cloudformation_dataclass', 'get_att', 'iam', 'lambda_', 'logs', 'ref', 'setup_resources', 'sns']
