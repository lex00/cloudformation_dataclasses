"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import ARN, ARN_EQUALS, ARN_LIKE, AWS_ACCOUNT_ID, AWS_NOTIFICATION_ARNS, AWS_NO_VALUE, AWS_PARTITION, AWS_REGION, AWS_STACK_ID, AWS_STACK_NAME, AWS_URL_SUFFIX, BOOL, Base64, Cidr, CloudFormationResource, Condition, ConditionOperator, DenyStatement, FindInMap, GetAZs, GetAtt, IP_ADDRESS, If, ImportValue, IpProtocol, Join, Mapping, NUMBER, Output, Parameter, ParameterType, PolicyDocument, PolicyStatement, Ref, ResourceRegistry, STRING, STRING_EQUALS, STRING_LIKE, STRING_NOT_EQUALS, STRING_NOT_LIKE, Select, Split, Sub, Tag, Template, Transform, cloudformation_dataclass, get_att, ref, registry, setup_resources
from cloudformation_dataclasses.aws import ec2, ecs, iam, logs
from cloudformation_dataclasses.aws.ecs import service, task_definition

from .stack.params import AlbSecurityGroupIdParam as AlbSecurityGroupIdParam
from .stack.params import DbEndpointParam as DbEndpointParam
from .stack.params import DbSecretArnParam as DbSecretArnParam
from .stack.params import PrivateSubnetIdsParam as PrivateSubnetIdsParam
from .stack.params import TargetGroupArnParam as TargetGroupArnParam
from .stack.params import VpcIdParam as VpcIdParam
from .stack.compute import EcsCluster as EcsCluster
from .stack.compute import ServiceLoadBalancer as ServiceLoadBalancer
from .stack.compute import ServiceNetworkConfig as ServiceNetworkConfig
from .stack.compute import ServiceVpcConfig as ServiceVpcConfig
from .stack.compute import WebContainerDbEnv as WebContainerDbEnv
from .stack.compute import WebContainerDefinition as WebContainerDefinition
from .stack.compute import WebContainerLogConfig as WebContainerLogConfig
from .stack.compute import WebContainerPortMapping as WebContainerPortMapping
from .stack.compute import WebService as WebService
from .stack.compute import WebTaskDefinition as WebTaskDefinition
from .stack.monitoring import EcsLogGroup as EcsLogGroup
from .stack.network import TaskSecurityGroup as TaskSecurityGroup
from .stack.network import TaskSecurityGroupIngress as TaskSecurityGroupIngress
from .stack.security import TaskExecutionRole as TaskExecutionRole
from .stack.security import TaskExecutionRoleAssumePolicy as TaskExecutionRoleAssumePolicy
from .stack.security import TaskExecutionRoleAssumeStatement as TaskExecutionRoleAssumeStatement
from .stack.security import TaskRole as TaskRole
from .stack.security import TaskRoleAssumePolicy as TaskRoleAssumePolicy
from .stack.security import TaskRoleAssumeStatement as TaskRoleAssumeStatement

__all__: list[str] = ['ARN', 'ARN_EQUALS', 'ARN_LIKE', 'AWS_ACCOUNT_ID', 'AWS_NOTIFICATION_ARNS', 'AWS_NO_VALUE', 'AWS_PARTITION', 'AWS_REGION', 'AWS_STACK_ID', 'AWS_STACK_NAME', 'AWS_URL_SUFFIX', 'AlbSecurityGroupIdParam', 'BOOL', 'Base64', 'Cidr', 'CloudFormationResource', 'Condition', 'ConditionOperator', 'DbEndpointParam', 'DbSecretArnParam', 'DenyStatement', 'EcsCluster', 'EcsLogGroup', 'FindInMap', 'GetAZs', 'GetAtt', 'IP_ADDRESS', 'If', 'ImportValue', 'IpProtocol', 'Join', 'Mapping', 'NUMBER', 'Output', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'PrivateSubnetIdsParam', 'Ref', 'ResourceRegistry', 'STRING', 'STRING_EQUALS', 'STRING_LIKE', 'STRING_NOT_EQUALS', 'STRING_NOT_LIKE', 'Select', 'ServiceLoadBalancer', 'ServiceNetworkConfig', 'ServiceVpcConfig', 'Split', 'Sub', 'Tag', 'TargetGroupArnParam', 'TaskExecutionRole', 'TaskExecutionRoleAssumePolicy', 'TaskExecutionRoleAssumeStatement', 'TaskRole', 'TaskRoleAssumePolicy', 'TaskRoleAssumeStatement', 'TaskSecurityGroup', 'TaskSecurityGroupIngress', 'Template', 'Transform', 'VpcIdParam', 'WebContainerDbEnv', 'WebContainerDefinition', 'WebContainerLogConfig', 'WebContainerPortMapping', 'WebService', 'WebTaskDefinition', 'cloudformation_dataclass', 'ec2', 'ecs', 'get_att', 'iam', 'logs', 'ref', 'registry', 'service', 'setup_resources', 'task_definition']
