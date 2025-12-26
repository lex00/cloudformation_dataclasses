"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    BOOL,
    DenyStatement,
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
    s3,
)
from cloudformation_dataclasses.intrinsics import (
    AWS_REGION,
    Base64,
    FindInMap,
    GetAZs,
    Join,
    Sub,
)

from .compute import LaunchConfig as LaunchConfig
from .compute import WebServerGroup as WebServerGroup
from .network import ElasticLoadBalancer as ElasticLoadBalancer
from .network import ElasticLoadBalancerAccessLoggingPolicy as ElasticLoadBalancerAccessLoggingPolicy
from .network import ElasticLoadBalancerConnectionDrainingPolicy as ElasticLoadBalancerConnectionDrainingPolicy
from .network import ElasticLoadBalancerHealthCheck as ElasticLoadBalancerHealthCheck
from .network import ElasticLoadBalancerListeners as ElasticLoadBalancerListeners
from .network import InstanceSecurityGroup as InstanceSecurityGroup
from .network import InstanceSecurityGroupEgress as InstanceSecurityGroupEgress
from .network import InstanceSecurityGroupEgress1 as InstanceSecurityGroupEgress1
from .outputs import URLOutput as URLOutput
from .params import InstanceType as InstanceType
from .params import KeyName as KeyName
from .params import LatestAmiId as LatestAmiId
from .params import Region2ELBAccountIdMapping as Region2ELBAccountIdMapping
from .params import Region2ExamplesMapping as Region2ExamplesMapping
from .params import SSHLocation as SSHLocation
from .storage import LogsBucket as LogsBucket
from .storage import LogsBucketPolicy as LogsBucketPolicy
from .storage import LogsBucketPolicyAllowStatement0 as LogsBucketPolicyAllowStatement0
from .storage import LogsBucketPolicyDenyStatement1 as LogsBucketPolicyDenyStatement1
from .storage import LogsBucketPolicyPolicyDocument as LogsBucketPolicyPolicyDocument

__all__: list[str] = ['AWS_REGION', 'BOOL', 'Base64', 'DenyStatement', 'ElasticLoadBalancer', 'ElasticLoadBalancerAccessLoggingPolicy', 'ElasticLoadBalancerConnectionDrainingPolicy', 'ElasticLoadBalancerHealthCheck', 'ElasticLoadBalancerListeners', 'FindInMap', 'GetAZs', 'InstanceSecurityGroup', 'InstanceSecurityGroupEgress', 'InstanceSecurityGroupEgress1', 'InstanceType', 'Join', 'KeyName', 'LatestAmiId', 'LaunchConfig', 'LogsBucket', 'LogsBucketPolicy', 'LogsBucketPolicyAllowStatement0', 'LogsBucketPolicyDenyStatement1', 'LogsBucketPolicyPolicyDocument', 'Mapping', 'Output', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'Region2ELBAccountIdMapping', 'Region2ExamplesMapping', 'SSHLocation', 'STRING', 'Sub', 'Template', 'URLOutput', 'WebServerGroup', 'autoscaling', 'cloudformation_dataclass', 'ec2', 'elasticloadbalancing', 'get_att', 'ref', 's3', 'setup_resources']
