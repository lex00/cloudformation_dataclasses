"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    NUMBER,
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
from cloudformation_dataclasses.aws import emr, iam
from cloudformation_dataclasses.aws.emr.cluster import BootstrapActionConfig
from cloudformation_dataclasses.intrinsics import AWS_NO_VALUE, Equals, If

from .main import EMRCluster as EMRCluster
from .main import EMRClusterBootstrapActionConfig as EMRClusterBootstrapActionConfig
from .main import EMRClusterConfiguration as EMRClusterConfiguration
from .main import EMRClusterConfiguration1 as EMRClusterConfiguration1
from .main import EMRClusterInstanceGroupConfig as EMRClusterInstanceGroupConfig
from .main import EMRClusterInstanceGroupConfig1 as EMRClusterInstanceGroupConfig1
from .main import EMRClusterJobFlowInstancesConfig as EMRClusterJobFlowInstancesConfig
from .params import Applications as Applications
from .params import CoreInstanceType as CoreInstanceType
from .params import EMRClusterName as EMRClusterName
from .params import HbaseCondition as HbaseCondition
from .params import KeyName as KeyName
from .params import LogUri as LogUri
from .params import MasterInstanceType as MasterInstanceType
from .params import NumberOfCoreInstances as NumberOfCoreInstances
from .params import ReleaseLabel as ReleaseLabel
from .params import S3DataUri as S3DataUri
from .params import SparkCondition as SparkCondition
from .params import SubnetID as SubnetID
from .security import EMRClusterServiceRole as EMRClusterServiceRole
from .security import EMRClusterServiceRoleAllowStatement0 as EMRClusterServiceRoleAllowStatement0
from .security import EMRClusterServiceRoleAssumeRolePolicyDocument as EMRClusterServiceRoleAssumeRolePolicyDocument
from .security import EMRClusterinstanceProfile as EMRClusterinstanceProfile
from .security import EMRClusterinstanceProfileRole as EMRClusterinstanceProfileRole
from .security import EMRClusterinstanceProfileRoleAllowStatement0 as EMRClusterinstanceProfileRoleAllowStatement0
from .security import EMRClusterinstanceProfileRoleAssumeRolePolicyDocument as EMRClusterinstanceProfileRoleAssumeRolePolicyDocument

__all__: list[str] = ['AWS_NO_VALUE', 'Applications', 'BootstrapActionConfig', 'CoreInstanceType', 'EMRCluster', 'EMRClusterBootstrapActionConfig', 'EMRClusterConfiguration', 'EMRClusterConfiguration1', 'EMRClusterInstanceGroupConfig', 'EMRClusterInstanceGroupConfig1', 'EMRClusterJobFlowInstancesConfig', 'EMRClusterName', 'EMRClusterServiceRole', 'EMRClusterServiceRoleAllowStatement0', 'EMRClusterServiceRoleAssumeRolePolicyDocument', 'EMRClusterinstanceProfile', 'EMRClusterinstanceProfileRole', 'EMRClusterinstanceProfileRoleAllowStatement0', 'EMRClusterinstanceProfileRoleAssumeRolePolicyDocument', 'Equals', 'HbaseCondition', 'If', 'KeyName', 'LogUri', 'MasterInstanceType', 'NUMBER', 'NumberOfCoreInstances', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'ReleaseLabel', 'S3DataUri', 'STRING', 'SparkCondition', 'SubnetID', 'Template', 'TemplateCondition', 'cloudformation_dataclass', 'emr', 'get_att', 'iam', 'ref', 'setup_resources']
