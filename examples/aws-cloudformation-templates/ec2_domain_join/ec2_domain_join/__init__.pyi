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
from cloudformation_dataclasses.aws import ec2, iam, ssm
from .params import *  # noqa: F403, F401

from .compute import myEC2InstanceSSM as myEC2InstanceSSM
from .compute import myEC2InstanceSSMAssociationParameter as myEC2InstanceSSMAssociationParameter
from .compute import myEC2InstanceSSMAssociationParameter1 as myEC2InstanceSSMAssociationParameter1
from .compute import myEC2InstanceSSMAssociationParameter2 as myEC2InstanceSSMAssociationParameter2
from .compute import myEC2InstanceSSMAssociationParameter3 as myEC2InstanceSSMAssociationParameter3
from .compute import myEC2InstanceSSMSsmAssociation as myEC2InstanceSSMSsmAssociation
from .network import InstanceSecurityGroup as InstanceSecurityGroup
from .network import InstanceSecurityGroupEgress as InstanceSecurityGroupEgress
from .params import ADDirectoryId as ADDirectoryId
from .params import ADDirectoryName as ADDirectoryName
from .params import ADDnsIpAddresses1 as ADDnsIpAddresses1
from .params import ADDnsIpAddresses2 as ADDnsIpAddresses2
from .params import AMI as AMI
from .params import InstanceType as InstanceType
from .params import KeyPair as KeyPair
from .params import PublicSubnet as PublicSubnet
from .params import VPC as VPC
from .security import myEC2SSMRole as myEC2SSMRole
from .security import myEC2SSMRoleAllowStatement0 as myEC2SSMRoleAllowStatement0
from .security import myEC2SSMRoleAssumeRolePolicyDocument as myEC2SSMRoleAssumeRolePolicyDocument
from .security import myInstanceProfile as myInstanceProfile
from .security import myssmdocument as myssmdocument

__all__: list[str] = ['ADDirectoryId', 'ADDirectoryName', 'ADDnsIpAddresses1', 'ADDnsIpAddresses2', 'AMI', 'InstanceSecurityGroup', 'InstanceSecurityGroupEgress', 'InstanceType', 'KeyPair', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'PublicSubnet', 'STRING', 'Template', 'VPC', 'cloudformation_dataclass', 'ec2', 'get_att', 'iam', 'myEC2InstanceSSM', 'myEC2InstanceSSMAssociationParameter', 'myEC2InstanceSSMAssociationParameter1', 'myEC2InstanceSSMAssociationParameter2', 'myEC2InstanceSSMAssociationParameter3', 'myEC2InstanceSSMSsmAssociation', 'myEC2SSMRole', 'myEC2SSMRoleAllowStatement0', 'myEC2SSMRoleAssumeRolePolicyDocument', 'myInstanceProfile', 'myssmdocument', 'ref', 'setup_resources', 'ssm']
