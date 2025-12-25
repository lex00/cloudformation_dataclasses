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
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import (
    ec2,
    greengrass,
    iam,
    lambda_,
)
from cloudformation_dataclasses.intrinsics import (
    AWS_ACCOUNT_ID,
    AWS_PARTITION,
    AWS_REGION,
    AWS_STACK_NAME,
    Base64,
    Join,
    Split,
    Sub,
)
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .main import CreateThingFunction as CreateThingFunction
from .main import CreateThingFunctionCode as CreateThingFunctionCode
from .main import FunctionDefinition as FunctionDefinition
from .main import FunctionDefinitionDefaultConfig as FunctionDefinitionDefaultConfig
from .main import FunctionDefinitionEnvironment as FunctionDefinitionEnvironment
from .main import FunctionDefinitionExecution as FunctionDefinitionExecution
from .main import FunctionDefinitionExecution1 as FunctionDefinitionExecution1
from .main import FunctionDefinitionFunction as FunctionDefinitionFunction
from .main import FunctionDefinitionFunctionConfiguration as FunctionDefinitionFunctionConfiguration
from .main import FunctionDefinitionFunctionDefinitionVersion as FunctionDefinitionFunctionDefinitionVersion
from .main import FunctionDefinitionRunAs as FunctionDefinitionRunAs
from .main import GGSampleFunction as GGSampleFunction
from .main import GGSampleFunctionCode as GGSampleFunctionCode
from .main import GGSampleFunctionVersion as GGSampleFunctionVersion
from .main import GreengrassCoreDefinition as GreengrassCoreDefinition
from .main import GreengrassCoreDefinitionVersion as GreengrassCoreDefinitionVersion
from .main import GreengrassCoreDefinitionVersionDevice as GreengrassCoreDefinitionVersionDevice
from .main import GreengrassGroup as GreengrassGroup
from .main import GreengrassGroupGroupVersion as GreengrassGroupGroupVersion
from .main import GreengrassInstance as GreengrassInstance
from .main import GreengrassInstanceAssociationParameter as GreengrassInstanceAssociationParameter
from .main import GroupDeploymentReset as GroupDeploymentReset
from .main import GroupDeploymentResetFunction as GroupDeploymentResetFunction
from .main import GroupDeploymentResetFunctionCode as GroupDeploymentResetFunctionCode
from .main import GroupDeploymentResetFunctionEnvironment as GroupDeploymentResetFunctionEnvironment
from .main import InstanceAZ as InstanceAZ
from .main import InstanceAZFunction as InstanceAZFunction
from .main import InstanceAZFunctionCode as InstanceAZFunctionCode
from .main import InstanceSecurityGroup as InstanceSecurityGroup
from .main import InstanceSecurityGroupEgress as InstanceSecurityGroupEgress
from .main import InternetGateway as InternetGateway
from .main import IoTThing as IoTThing
from .main import RouteTableAssociationAPublic as RouteTableAssociationAPublic
from .main import RouteTablePublic as RouteTablePublic
from .main import RouteTablePublicInternetRoute as RouteTablePublicInternetRoute
from .main import SubnetAPublic as SubnetAPublic
from .main import SubscriptionDefinition as SubscriptionDefinition
from .main import SubscriptionDefinitionSubscription as SubscriptionDefinitionSubscription
from .main import SubscriptionDefinitionSubscription1 as SubscriptionDefinitionSubscription1
from .main import SubscriptionDefinitionSubscription2 as SubscriptionDefinitionSubscription2
from .main import SubscriptionDefinitionSubscriptionDefinitionVersion as SubscriptionDefinitionSubscriptionDefinitionVersion
from .main import VPC as VPC
from .main import VPCGatewayAttachment as VPCGatewayAttachment
from .outputs import EC2IPAddressOutput as EC2IPAddressOutput
from .params import CoreName as CoreName
from .params import InstanceType as InstanceType
from .params import LatestAmiId as LatestAmiId
from .params import SecurityAccessCIDR as SecurityAccessCIDR
from .params import myKeyPair as myKeyPair
from .security import GreengrassResourceRole as GreengrassResourceRole
from .security import GreengrassResourceRoleAllowStatement0 as GreengrassResourceRoleAllowStatement0
from .security import GreengrassResourceRoleAllowStatement0_1 as GreengrassResourceRoleAllowStatement0_1
from .security import GreengrassResourceRoleAllowStatement1 as GreengrassResourceRoleAllowStatement1
from .security import GreengrassResourceRoleAssumeRolePolicyDocument as GreengrassResourceRoleAssumeRolePolicyDocument
from .security import GreengrassResourceRolePolicies0PolicyDocument as GreengrassResourceRolePolicies0PolicyDocument
from .security import GreengrassResourceRolePolicy as GreengrassResourceRolePolicy
from .security import LambdaExecutionRole as LambdaExecutionRole
from .security import LambdaExecutionRoleAllowStatement0 as LambdaExecutionRoleAllowStatement0
from .security import LambdaExecutionRoleAllowStatement0_1 as LambdaExecutionRoleAllowStatement0_1
from .security import LambdaExecutionRoleAllowStatement1 as LambdaExecutionRoleAllowStatement1
from .security import LambdaExecutionRoleAllowStatement2 as LambdaExecutionRoleAllowStatement2
from .security import LambdaExecutionRoleAllowStatement3 as LambdaExecutionRoleAllowStatement3
from .security import LambdaExecutionRoleAllowStatement4 as LambdaExecutionRoleAllowStatement4
from .security import LambdaExecutionRoleAssumeRolePolicyDocument as LambdaExecutionRoleAssumeRolePolicyDocument
from .security import LambdaExecutionRolePolicies0PolicyDocument as LambdaExecutionRolePolicies0PolicyDocument
from .security import LambdaExecutionRolePolicy as LambdaExecutionRolePolicy

__all__: list[str] = ['AWS_ACCOUNT_ID', 'AWS_PARTITION', 'AWS_REGION', 'AWS_STACK_NAME', 'Base64', 'CloudFormationResource', 'CoreName', 'CreateThingFunction', 'CreateThingFunctionCode', 'EC2IPAddressOutput', 'FunctionDefinition', 'FunctionDefinitionDefaultConfig', 'FunctionDefinitionEnvironment', 'FunctionDefinitionExecution', 'FunctionDefinitionExecution1', 'FunctionDefinitionFunction', 'FunctionDefinitionFunctionConfiguration', 'FunctionDefinitionFunctionDefinitionVersion', 'FunctionDefinitionRunAs', 'GGSampleFunction', 'GGSampleFunctionCode', 'GGSampleFunctionVersion', 'GreengrassCoreDefinition', 'GreengrassCoreDefinitionVersion', 'GreengrassCoreDefinitionVersionDevice', 'GreengrassGroup', 'GreengrassGroupGroupVersion', 'GreengrassInstance', 'GreengrassInstanceAssociationParameter', 'GreengrassResourceRole', 'GreengrassResourceRoleAllowStatement0', 'GreengrassResourceRoleAllowStatement0_1', 'GreengrassResourceRoleAllowStatement1', 'GreengrassResourceRoleAssumeRolePolicyDocument', 'GreengrassResourceRolePolicies0PolicyDocument', 'GreengrassResourceRolePolicy', 'GroupDeploymentReset', 'GroupDeploymentResetFunction', 'GroupDeploymentResetFunctionCode', 'GroupDeploymentResetFunctionEnvironment', 'InstanceAZ', 'InstanceAZFunction', 'InstanceAZFunctionCode', 'InstanceSecurityGroup', 'InstanceSecurityGroupEgress', 'InstanceType', 'InternetGateway', 'IoTThing', 'Join', 'LambdaExecutionRole', 'LambdaExecutionRoleAllowStatement0', 'LambdaExecutionRoleAllowStatement0_1', 'LambdaExecutionRoleAllowStatement1', 'LambdaExecutionRoleAllowStatement2', 'LambdaExecutionRoleAllowStatement3', 'LambdaExecutionRoleAllowStatement4', 'LambdaExecutionRoleAssumeRolePolicyDocument', 'LambdaExecutionRolePolicies0PolicyDocument', 'LambdaExecutionRolePolicy', 'LatestAmiId', 'Output', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'RouteTableAssociationAPublic', 'RouteTablePublic', 'RouteTablePublicInternetRoute', 'STRING', 'SecurityAccessCIDR', 'Split', 'Sub', 'SubnetAPublic', 'SubscriptionDefinition', 'SubscriptionDefinitionSubscription', 'SubscriptionDefinitionSubscription1', 'SubscriptionDefinitionSubscription2', 'SubscriptionDefinitionSubscriptionDefinitionVersion', 'Template', 'VPC', 'VPCGatewayAttachment', 'cloudformation_dataclass', 'ec2', 'get_att', 'greengrass', 'iam', 'lambda_', 'myKeyPair', 'ref', 'setup_resources']
