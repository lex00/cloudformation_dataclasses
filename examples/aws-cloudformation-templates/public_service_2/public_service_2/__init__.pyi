"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    NUMBER,
    Parameter,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.template import Condition as TemplateCondition
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import ecs, elasticloadbalancingv2
from cloudformation_dataclasses.intrinsics import (
    AWS_NO_VALUE,
    Equals,
    If,
    ImportValue,
    Join,
    Not,
)

from .compute import Service as Service
from .compute import ServiceAwsVpcConfiguration as ServiceAwsVpcConfiguration
from .compute import ServiceDeploymentConfiguration as ServiceDeploymentConfiguration
from .compute import ServiceLoadBalancer as ServiceLoadBalancer
from .compute import ServiceNetworkConfiguration as ServiceNetworkConfiguration
from .compute import TaskDefinition as TaskDefinition
from .compute import TaskDefinitionContainerDefinition as TaskDefinitionContainerDefinition
from .compute import TaskDefinitionPortMapping as TaskDefinitionPortMapping
from .network import LoadBalancerRule as LoadBalancerRule
from .network import LoadBalancerRuleAction as LoadBalancerRuleAction
from .network import LoadBalancerRuleRuleCondition as LoadBalancerRuleRuleCondition
from .network import TargetGroup as TargetGroup
from .params import ContainerCpu as ContainerCpu
from .params import ContainerMemory as ContainerMemory
from .params import ContainerPort as ContainerPort
from .params import DesiredCount as DesiredCount
from .params import HasCustomRoleCondition as HasCustomRoleCondition
from .params import ImageUrl as ImageUrl
from .params import Path as Path
from .params import Priority as Priority
from .params import Role as Role
from .params import ServiceName as ServiceName
from .params import StackName as StackName

__all__: list[str] = ['AWS_NO_VALUE', 'ContainerCpu', 'ContainerMemory', 'ContainerPort', 'DesiredCount', 'Equals', 'HasCustomRoleCondition', 'If', 'ImageUrl', 'ImportValue', 'Join', 'LoadBalancerRule', 'LoadBalancerRuleAction', 'LoadBalancerRuleRuleCondition', 'NUMBER', 'Not', 'Parameter', 'Path', 'Priority', 'Role', 'STRING', 'Service', 'ServiceAwsVpcConfiguration', 'ServiceDeploymentConfiguration', 'ServiceLoadBalancer', 'ServiceName', 'ServiceNetworkConfiguration', 'StackName', 'TargetGroup', 'TaskDefinition', 'TaskDefinitionContainerDefinition', 'TaskDefinitionPortMapping', 'Template', 'TemplateCondition', 'cloudformation_dataclass', 'ecs', 'elasticloadbalancingv2', 'get_att', 'ref', 'setup_resources']
