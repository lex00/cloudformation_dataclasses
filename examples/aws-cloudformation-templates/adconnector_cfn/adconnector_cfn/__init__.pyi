"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    BOOL,
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
    ec2,
    iam,
    lambda_,
    logs,
    secretsmanager,
)
from cloudformation_dataclasses.aws.iam.user import Policy
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

from .main import ADConnectorLambdaFunction as ADConnectorLambdaFunction
from .main import ADConnectorLambdaFunctionCapacityProviderVpcConfig as ADConnectorLambdaFunctionCapacityProviderVpcConfig
from .main import ADConnectorLambdaFunctionContent as ADConnectorLambdaFunctionContent
from .main import ADConnectorLambdaFunctionEnvironment as ADConnectorLambdaFunctionEnvironment
from .main import ADConnectorLambdaRole as ADConnectorLambdaRole
from .main import ADConnectorLambdaRoleAllowStatement0 as ADConnectorLambdaRoleAllowStatement0
from .main import ADConnectorLambdaRoleAllowStatement0_1 as ADConnectorLambdaRoleAllowStatement0_1
from .main import ADConnectorLambdaRoleAllowStatement0_2 as ADConnectorLambdaRoleAllowStatement0_2
from .main import ADConnectorLambdaRoleAllowStatement0_3 as ADConnectorLambdaRoleAllowStatement0_3
from .main import ADConnectorLambdaRoleAllowStatement1 as ADConnectorLambdaRoleAllowStatement1
from .main import ADConnectorLambdaRoleAllowStatement1_1 as ADConnectorLambdaRoleAllowStatement1_1
from .main import ADConnectorLambdaRoleAllowStatement2 as ADConnectorLambdaRoleAllowStatement2
from .main import ADConnectorLambdaRoleAssumeRolePolicyDocument as ADConnectorLambdaRoleAssumeRolePolicyDocument
from .main import ADConnectorLambdaRolePolicies0PolicyDocument as ADConnectorLambdaRolePolicies0PolicyDocument
from .main import ADConnectorLambdaRolePolicies1PolicyDocument as ADConnectorLambdaRolePolicies1PolicyDocument
from .main import ADConnectorLambdaRolePolicies2PolicyDocument as ADConnectorLambdaRolePolicies2PolicyDocument
from .main import ADConnectorLambdaRolePolicy as ADConnectorLambdaRolePolicy
from .main import ADConnectorLambdaRolePolicy1 as ADConnectorLambdaRolePolicy1
from .main import ADConnectorLambdaRolePolicy2 as ADConnectorLambdaRolePolicy2
from .main import ADConnectorLinuxEC2DomainJoinInstanceProfile as ADConnectorLinuxEC2DomainJoinInstanceProfile
from .main import ADConnectorLinuxEC2DomainJoinRole as ADConnectorLinuxEC2DomainJoinRole
from .main import ADConnectorLinuxEC2DomainJoinRoleAllowStatement0 as ADConnectorLinuxEC2DomainJoinRoleAllowStatement0
from .main import ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_1 as ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_1
from .main import ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_2 as ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_2
from .main import ADConnectorLinuxEC2DomainJoinRoleAssumeRolePolicyDocument as ADConnectorLinuxEC2DomainJoinRoleAssumeRolePolicyDocument
from .main import ADConnectorLinuxEC2DomainJoinRolePolicies0PolicyDocument as ADConnectorLinuxEC2DomainJoinRolePolicies0PolicyDocument
from .main import ADConnectorLinuxEC2DomainJoinRolePolicies2PolicyDocument as ADConnectorLinuxEC2DomainJoinRolePolicies2PolicyDocument
from .main import ADConnectorLinuxEC2DomainJoinRolePolicy as ADConnectorLinuxEC2DomainJoinRolePolicy
from .main import ADConnectorLinuxEC2DomainJoinRolePolicy1 as ADConnectorLinuxEC2DomainJoinRolePolicy1
from .main import ADConnectorLinuxEC2SeamlessDomainJoinSecret as ADConnectorLinuxEC2SeamlessDomainJoinSecret
from .main import ADConnectorResource as ADConnectorResource
from .main import ADConnectorServiceAccountSecret as ADConnectorServiceAccountSecret
from .main import ADConnectorWindowsEC2DomainJoinInstanceProfile as ADConnectorWindowsEC2DomainJoinInstanceProfile
from .main import ADConnectorWindowsEC2DomainJoinRole as ADConnectorWindowsEC2DomainJoinRole
from .main import ADConnectorWindowsEC2DomainJoinRoleAllowStatement0 as ADConnectorWindowsEC2DomainJoinRoleAllowStatement0
from .main import ADConnectorWindowsEC2DomainJoinRoleAllowStatement0_1 as ADConnectorWindowsEC2DomainJoinRoleAllowStatement0_1
from .main import ADConnectorWindowsEC2DomainJoinRoleAssumeRolePolicyDocument as ADConnectorWindowsEC2DomainJoinRoleAssumeRolePolicyDocument
from .main import ADConnectorWindowsEC2DomainJoinRolePolicies0PolicyDocument as ADConnectorWindowsEC2DomainJoinRolePolicies0PolicyDocument
from .main import ADConnectorWindowsEC2DomainJoinRolePolicy as ADConnectorWindowsEC2DomainJoinRolePolicy
from .main import DHCPOptions as DHCPOptions
from .main import DHCPOptionsAssociationParameter as DHCPOptionsAssociationParameter
from .main import DHCPOptionsVPCAssociation as DHCPOptionsVPCAssociation
from .monitoring import ADConnectorLambdaLogsLogGroup as ADConnectorLambdaLogsLogGroup
from .network import ADConnectorDomainMembersSG as ADConnectorDomainMembersSG
from .network import ADConnectorDomainMembersSGAssociationParameter as ADConnectorDomainMembersSGAssociationParameter
from .network import ADConnectorDomainMembersSGEgress as ADConnectorDomainMembersSGEgress
from .network import ADConnectorDomainMembersSGEgress1 as ADConnectorDomainMembersSGEgress1
from .network import ADConnectorDomainMembersSGEgress2 as ADConnectorDomainMembersSGEgress2
from .network import ADConnectorDomainMembersSGEgress3 as ADConnectorDomainMembersSGEgress3
from .outputs import ADConnectorADConnectorDomainMembersSGOutput as ADConnectorADConnectorDomainMembersSGOutput
from .outputs import ADConnectorDirectoryIdOutput as ADConnectorDirectoryIdOutput
from .outputs import ADConnectorDirectoryNameOutput as ADConnectorDirectoryNameOutput
from .outputs import ADConnectorLinuxEC2SeamlessDomainJoinInstanceProfileOutput as ADConnectorLinuxEC2SeamlessDomainJoinInstanceProfileOutput
from .outputs import ADConnectorLinuxEC2SeamlessDomainJoinRoleOutput as ADConnectorLinuxEC2SeamlessDomainJoinRoleOutput
from .outputs import ADConnectorWindowsEC2SeamlessDomainJoinInstanceProfileOutput as ADConnectorWindowsEC2SeamlessDomainJoinInstanceProfileOutput
from .outputs import ADConnectorWindowsEC2SeamlessDomainJoinRoleOutput as ADConnectorWindowsEC2SeamlessDomainJoinRoleOutput
from .params import ADConnectorDescription as ADConnectorDescription
from .params import ADConnectorSize as ADConnectorSize
from .params import CreateADConnectorDomainMembersSG as CreateADConnectorDomainMembersSG
from .params import CreateDHCPOptionSet as CreateDHCPOptionSet
from .params import CreateLinuxEC2DomainJoinResources as CreateLinuxEC2DomainJoinResources
from .params import CreateWindowsEC2DomainJoinResources as CreateWindowsEC2DomainJoinResources
from .params import DHCPOptionSetConditionCondition as DHCPOptionSetConditionCondition
from .params import DomainDNSName as DomainDNSName
from .params import DomainDNSServers as DomainDNSServers
from .params import DomainJoinUser as DomainJoinUser
from .params import DomainJoinUserPassword as DomainJoinUserPassword
from .params import DomainMembersSGConditionCondition as DomainMembersSGConditionCondition
from .params import DomainNetBiosName as DomainNetBiosName
from .params import LambdaFunctionName as LambdaFunctionName
from .params import LambdaLogLevel as LambdaLogLevel
from .params import LambdaLogsCloudWatchKMSKey as LambdaLogsCloudWatchKMSKey
from .params import LambdaLogsCloudWatchKMSKeyConditionCondition as LambdaLogsCloudWatchKMSKeyConditionCondition
from .params import LambdaLogsLogGroupRetention as LambdaLogsLogGroupRetention
from .params import LambdaS3BucketName as LambdaS3BucketName
from .params import LambdaZipFileName as LambdaZipFileName
from .params import LinuxEC2DomainJoinResourcesConditionCondition as LinuxEC2DomainJoinResourcesConditionCondition
from .params import PrivateSubnet1ID as PrivateSubnet1ID
from .params import PrivateSubnet2ID as PrivateSubnet2ID
from .params import SSMLogsBucketName as SSMLogsBucketName
from .params import SSMLogsBucketNameConditionCondition as SSMLogsBucketNameConditionCondition
from .params import SecretsManagerDomainCredentialsSecretsKMSKey as SecretsManagerDomainCredentialsSecretsKMSKey
from .params import SecretsManagerDomainCredentialsSecretsKMSKeyConditionCondition as SecretsManagerDomainCredentialsSecretsKMSKeyConditionCondition
from .params import VPCID as VPCID
from .params import WindowsEC2DomainJoinResourcesConditionCondition as WindowsEC2DomainJoinResourcesConditionCondition

__all__: list[str] = ['ADConnectorADConnectorDomainMembersSGOutput', 'ADConnectorDescription', 'ADConnectorDirectoryIdOutput', 'ADConnectorDirectoryNameOutput', 'ADConnectorDomainMembersSG', 'ADConnectorDomainMembersSGAssociationParameter', 'ADConnectorDomainMembersSGEgress', 'ADConnectorDomainMembersSGEgress1', 'ADConnectorDomainMembersSGEgress2', 'ADConnectorDomainMembersSGEgress3', 'ADConnectorLambdaFunction', 'ADConnectorLambdaFunctionCapacityProviderVpcConfig', 'ADConnectorLambdaFunctionContent', 'ADConnectorLambdaFunctionEnvironment', 'ADConnectorLambdaLogsLogGroup', 'ADConnectorLambdaRole', 'ADConnectorLambdaRoleAllowStatement0', 'ADConnectorLambdaRoleAllowStatement0_1', 'ADConnectorLambdaRoleAllowStatement0_2', 'ADConnectorLambdaRoleAllowStatement0_3', 'ADConnectorLambdaRoleAllowStatement1', 'ADConnectorLambdaRoleAllowStatement1_1', 'ADConnectorLambdaRoleAllowStatement2', 'ADConnectorLambdaRoleAssumeRolePolicyDocument', 'ADConnectorLambdaRolePolicies0PolicyDocument', 'ADConnectorLambdaRolePolicies1PolicyDocument', 'ADConnectorLambdaRolePolicies2PolicyDocument', 'ADConnectorLambdaRolePolicy', 'ADConnectorLambdaRolePolicy1', 'ADConnectorLambdaRolePolicy2', 'ADConnectorLinuxEC2DomainJoinInstanceProfile', 'ADConnectorLinuxEC2DomainJoinRole', 'ADConnectorLinuxEC2DomainJoinRoleAllowStatement0', 'ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_1', 'ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_2', 'ADConnectorLinuxEC2DomainJoinRoleAssumeRolePolicyDocument', 'ADConnectorLinuxEC2DomainJoinRolePolicies0PolicyDocument', 'ADConnectorLinuxEC2DomainJoinRolePolicies2PolicyDocument', 'ADConnectorLinuxEC2DomainJoinRolePolicy', 'ADConnectorLinuxEC2DomainJoinRolePolicy1', 'ADConnectorLinuxEC2SeamlessDomainJoinInstanceProfileOutput', 'ADConnectorLinuxEC2SeamlessDomainJoinRoleOutput', 'ADConnectorLinuxEC2SeamlessDomainJoinSecret', 'ADConnectorResource', 'ADConnectorServiceAccountSecret', 'ADConnectorSize', 'ADConnectorWindowsEC2DomainJoinInstanceProfile', 'ADConnectorWindowsEC2DomainJoinRole', 'ADConnectorWindowsEC2DomainJoinRoleAllowStatement0', 'ADConnectorWindowsEC2DomainJoinRoleAllowStatement0_1', 'ADConnectorWindowsEC2DomainJoinRoleAssumeRolePolicyDocument', 'ADConnectorWindowsEC2DomainJoinRolePolicies0PolicyDocument', 'ADConnectorWindowsEC2DomainJoinRolePolicy', 'ADConnectorWindowsEC2SeamlessDomainJoinInstanceProfileOutput', 'ADConnectorWindowsEC2SeamlessDomainJoinRoleOutput', 'AWS_NO_VALUE', 'AWS_STACK_NAME', 'BOOL', 'CloudFormationResource', 'CreateADConnectorDomainMembersSG', 'CreateDHCPOptionSet', 'CreateLinuxEC2DomainJoinResources', 'CreateWindowsEC2DomainJoinResources', 'DHCPOptionSetConditionCondition', 'DHCPOptions', 'DHCPOptionsAssociationParameter', 'DHCPOptionsVPCAssociation', 'DomainDNSName', 'DomainDNSServers', 'DomainJoinUser', 'DomainJoinUserPassword', 'DomainMembersSGConditionCondition', 'DomainNetBiosName', 'Equals', 'If', 'LambdaFunctionName', 'LambdaLogLevel', 'LambdaLogsCloudWatchKMSKey', 'LambdaLogsCloudWatchKMSKeyConditionCondition', 'LambdaLogsLogGroupRetention', 'LambdaS3BucketName', 'LambdaZipFileName', 'LinuxEC2DomainJoinResourcesConditionCondition', 'Not', 'Output', 'Parameter', 'ParameterType', 'Policy', 'PolicyDocument', 'PolicyStatement', 'PrivateSubnet1ID', 'PrivateSubnet2ID', 'SSMLogsBucketName', 'SSMLogsBucketNameConditionCondition', 'STRING', 'SecretsManagerDomainCredentialsSecretsKMSKey', 'SecretsManagerDomainCredentialsSecretsKMSKeyConditionCondition', 'Sub', 'Template', 'TemplateCondition', 'VPCID', 'WindowsEC2DomainJoinResourcesConditionCondition', 'cloudformation_dataclass', 'ec2', 'get_att', 'iam', 'lambda_', 'logs', 'ref', 'secretsmanager', 'setup_resources']
