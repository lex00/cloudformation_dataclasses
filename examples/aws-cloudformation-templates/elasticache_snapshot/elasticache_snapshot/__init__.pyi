"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    CloudFormationResource,
    Mapping,
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
from cloudformation_dataclasses.aws import (
    ec2,
    elasticache,
    iam,
    lambda_,
)
from cloudformation_dataclasses.intrinsics import (
    AWS_REGION,
    Equals,
    FindInMap,
    Sub,
)
from .params import *  # noqa: F403, F401

from .compute import EnableShapshot as EnableShapshot
from .compute import EnableShapshotCode as EnableShapshotCode
from .compute import LambdaExecutePermission as LambdaExecutePermission
from .database import RedisParameterGroup as RedisParameterGroup
from .database import RedisReplicationGroup as RedisReplicationGroup
from .database import RedisSubnetGroup as RedisSubnetGroup
from .main import EnableShapshotTrigger as EnableShapshotTrigger
from .network import InternetGateway as InternetGateway
from .network import PublicInternetRoute as PublicInternetRoute
from .network import PublicInternetRouteTable as PublicInternetRouteTable
from .network import PublicSubnetA as PublicSubnetA
from .network import PublicSubnetARouteTableAssociation as PublicSubnetARouteTableAssociation
from .network import PublicSubnetB as PublicSubnetB
from .network import PublicSubnetBRouteTableAssociation as PublicSubnetBRouteTableAssociation
from .network import RedisSecurityGroup as RedisSecurityGroup
from .network import RedisSecurityGroupEgress as RedisSecurityGroupEgress
from .network import VPC as VPC
from .network import VPCGatewayAttachment as VPCGatewayAttachment
from .params import AWSRegion2AZMapping as AWSRegion2AZMapping
from .params import EnableBackupsCondition as EnableBackupsCondition
from .params import EnableSnapshotting as EnableSnapshotting
from .params import RedisNodeType as RedisNodeType
from .params import SnapshotRetentionLimit as SnapshotRetentionLimit
from .params import SnapshotWindow as SnapshotWindow
from .security import IamRoleLambda as IamRoleLambda
from .security import IamRoleLambdaAllowStatement0 as IamRoleLambdaAllowStatement0
from .security import IamRoleLambdaAllowStatement0_1 as IamRoleLambdaAllowStatement0_1
from .security import IamRoleLambdaAssumeRolePolicyDocument as IamRoleLambdaAssumeRolePolicyDocument
from .security import IamRoleLambdaPolicies0PolicyDocument as IamRoleLambdaPolicies0PolicyDocument
from .security import IamRoleLambdaPolicy as IamRoleLambdaPolicy

__all__: list[str] = ['AWSRegion2AZMapping', 'AWS_REGION', 'CloudFormationResource', 'EnableBackupsCondition', 'EnableShapshot', 'EnableShapshotCode', 'EnableShapshotTrigger', 'EnableSnapshotting', 'Equals', 'FindInMap', 'IamRoleLambda', 'IamRoleLambdaAllowStatement0', 'IamRoleLambdaAllowStatement0_1', 'IamRoleLambdaAssumeRolePolicyDocument', 'IamRoleLambdaPolicies0PolicyDocument', 'IamRoleLambdaPolicy', 'InternetGateway', 'LambdaExecutePermission', 'Mapping', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PublicInternetRoute', 'PublicInternetRouteTable', 'PublicSubnetA', 'PublicSubnetARouteTableAssociation', 'PublicSubnetB', 'PublicSubnetBRouteTableAssociation', 'RedisNodeType', 'RedisParameterGroup', 'RedisReplicationGroup', 'RedisSecurityGroup', 'RedisSecurityGroupEgress', 'RedisSubnetGroup', 'STRING', 'SnapshotRetentionLimit', 'SnapshotWindow', 'Sub', 'Template', 'TemplateCondition', 'VPC', 'VPCGatewayAttachment', 'cloudformation_dataclass', 'ec2', 'elasticache', 'get_att', 'iam', 'lambda_', 'ref', 'setup_resources']
