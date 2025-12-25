"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Mapping,
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
    autoscaling,
    ec2,
    elasticloadbalancing,
    iam,
)
from cloudformation_dataclasses.intrinsics import (
    Base64,
    GetAZs,
    Join,
    Sub,
)
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .compute import LaunchConfig as LaunchConfig
from .compute import WebServerGroup as WebServerGroup
from .network import ElasticLoadBalancer as ElasticLoadBalancer
from .network import ElasticLoadBalancerHealthCheck as ElasticLoadBalancerHealthCheck
from .network import ElasticLoadBalancerListeners as ElasticLoadBalancerListeners
from .network import InstanceSecurityGroup as InstanceSecurityGroup
from .network import InstanceSecurityGroupEgress as InstanceSecurityGroupEgress
from .network import InstanceSecurityGroupEgress1 as InstanceSecurityGroupEgress1
from .outputs import URLOutput as URLOutput
from .params import InstanceType as InstanceType
from .params import KeyName as KeyName
from .params import LatestAmiId as LatestAmiId
from .params import Region2ExamplesMapping as Region2ExamplesMapping
from .params import SSHLocation as SSHLocation
from .security import DescribeHealthRole as DescribeHealthRole
from .security import DescribeHealthRoleAllowStatement0 as DescribeHealthRoleAllowStatement0
from .security import DescribeHealthRoleAllowStatement0_1 as DescribeHealthRoleAllowStatement0_1
from .security import DescribeHealthRoleAssumeRolePolicyDocument as DescribeHealthRoleAssumeRolePolicyDocument
from .security import DescribeHealthRolePolicies0PolicyDocument as DescribeHealthRolePolicies0PolicyDocument
from .security import DescribeHealthRolePolicy as DescribeHealthRolePolicy
from .security import WebServerInstanceProfile as WebServerInstanceProfile

__all__: list[str] = ['Base64', 'DescribeHealthRole', 'DescribeHealthRoleAllowStatement0', 'DescribeHealthRoleAllowStatement0_1', 'DescribeHealthRoleAssumeRolePolicyDocument', 'DescribeHealthRolePolicies0PolicyDocument', 'DescribeHealthRolePolicy', 'ElasticLoadBalancer', 'ElasticLoadBalancerHealthCheck', 'ElasticLoadBalancerListeners', 'GetAZs', 'InstanceSecurityGroup', 'InstanceSecurityGroupEgress', 'InstanceSecurityGroupEgress1', 'InstanceType', 'Join', 'KeyName', 'LatestAmiId', 'LaunchConfig', 'Mapping', 'Output', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'Region2ExamplesMapping', 'SSHLocation', 'STRING', 'Sub', 'Template', 'URLOutput', 'WebServerGroup', 'WebServerInstanceProfile', 'autoscaling', 'cloudformation_dataclass', 'ec2', 'elasticloadbalancing', 'get_att', 'iam', 'ref', 'setup_resources']
