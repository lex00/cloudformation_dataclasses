"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    Parameter,
    ParameterType,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import cloudformation, ec2
from cloudformation_dataclasses.intrinsics import (
    AWS_REGION,
    AWS_STACK_ID,
    Base64,
    Join,
)

from .compute import KWOSInstance as KWOSInstance
from .compute import KWOSInstanceAssociationParameter as KWOSInstanceAssociationParameter
from .compute import KWOSInstanceAssociationParameter1 as KWOSInstanceAssociationParameter1
from .compute import KWOSInstanceAssociationParameter2 as KWOSInstanceAssociationParameter2
from .compute import KWOSInstanceAssociationParameter3 as KWOSInstanceAssociationParameter3
from .compute import KWOSInstanceAssociationParameter4 as KWOSInstanceAssociationParameter4
from .compute import KWOSInstanceAssociationParameter5 as KWOSInstanceAssociationParameter5
from .compute import KWOSInstanceAssociationParameter6 as KWOSInstanceAssociationParameter6
from .compute import KWOSInstanceAssociationParameter7 as KWOSInstanceAssociationParameter7
from .compute import KWOSInstanceAssociationParameter8 as KWOSInstanceAssociationParameter8
from .infra import KWOSWaitCondition as KWOSWaitCondition
from .infra import KWOSWaitHandle as KWOSWaitHandle
from .network import KWOSSecurityGroup as KWOSSecurityGroup
from .network import KWOSSecurityGroupEgress as KWOSSecurityGroupEgress
from .network import KWOSSecurityGroupEgress1 as KWOSSecurityGroupEgress1
from .network import KWOSSecurityGroupEgress2 as KWOSSecurityGroupEgress2
from .network import KWOSSecurityGroupEgress3 as KWOSSecurityGroupEgress3
from .network import KWOSSecurityGroupEgress4 as KWOSSecurityGroupEgress4
from .outputs import InstanceIdOutput as InstanceIdOutput
from .outputs import WebsiteURLOutput as WebsiteURLOutput
from .params import AgentID as AgentID
from .params import BudgetCode as BudgetCode
from .params import ImageId as ImageId
from .params import InstanceName as InstanceName
from .params import InstanceType as InstanceType
from .params import IsMaster as IsMaster
from .params import KeyName as KeyName
from .params import LaunchPlatform as LaunchPlatform
from .params import LaunchUser as LaunchUser
from .params import MasterID as MasterID
from .params import SSHLocation as SSHLocation
from .params import SubnetId as SubnetId
from .params import TestID as TestID
from .params import TestTarget as TestTarget
from .params import VpcId as VpcId

__all__: list[str] = ['AWS_REGION', 'AWS_STACK_ID', 'AgentID', 'Base64', 'BudgetCode', 'ImageId', 'InstanceIdOutput', 'InstanceName', 'InstanceType', 'IsMaster', 'Join', 'KWOSInstance', 'KWOSInstanceAssociationParameter', 'KWOSInstanceAssociationParameter1', 'KWOSInstanceAssociationParameter2', 'KWOSInstanceAssociationParameter3', 'KWOSInstanceAssociationParameter4', 'KWOSInstanceAssociationParameter5', 'KWOSInstanceAssociationParameter6', 'KWOSInstanceAssociationParameter7', 'KWOSInstanceAssociationParameter8', 'KWOSSecurityGroup', 'KWOSSecurityGroupEgress', 'KWOSSecurityGroupEgress1', 'KWOSSecurityGroupEgress2', 'KWOSSecurityGroupEgress3', 'KWOSSecurityGroupEgress4', 'KWOSWaitCondition', 'KWOSWaitHandle', 'KeyName', 'LaunchPlatform', 'LaunchUser', 'MasterID', 'Output', 'Parameter', 'ParameterType', 'SSHLocation', 'STRING', 'SubnetId', 'Template', 'TestID', 'TestTarget', 'VpcId', 'WebsiteURLOutput', 'cloudformation', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'setup_resources']
