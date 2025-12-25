"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    NUMBER,
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
    applicationautoscaling,
    autoscaling,
    cloudwatch,
    ec2,
    ecs,
    elasticloadbalancingv2,
    events,
    iam,
    kms,
    logs,
)
from cloudformation_dataclasses.intrinsics import (
    AWS_REGION,
    AWS_STACK_NAME,
    Base64,
    Equals,
    If,
    Join,
    Sub,
)

from .main import ALB500sAlarmScaleUp as ALB500sAlarmScaleUp
from .main import ALB500sAlarmScaleUpDimension as ALB500sAlarmScaleUpDimension
from .main import CloudwatchLogsGroup as CloudwatchLogsGroup
from .main import ContainerInstances as ContainerInstances
from .main import ECSAutoScalingGroup as ECSAutoScalingGroup
from .main import ECSCluster as ECSCluster
from .main import EcsSecurityGroupALBports as EcsSecurityGroupALBports
from .main import EcsSecurityGroupHTTPinbound as EcsSecurityGroupHTTPinbound
from .main import EcsSecurityGroupSSHinbound as EcsSecurityGroupSSHinbound
from .main import Service as Service
from .main import ServiceLoadBalancer as ServiceLoadBalancer
from .main import ServiceScalingPolicy as ServiceScalingPolicy
from .main import ServiceScalingPolicyStepAdjustment as ServiceScalingPolicyStepAdjustment
from .main import ServiceScalingPolicyStepScalingPolicyConfiguration as ServiceScalingPolicyStepScalingPolicyConfiguration
from .main import ServiceScalingTarget as ServiceScalingTarget
from .main import TaskDefinition as TaskDefinition
from .main import TaskDefinitionContainerDefinition as TaskDefinitionContainerDefinition
from .main import TaskDefinitionContainerDefinition1 as TaskDefinitionContainerDefinition1
from .main import TaskDefinitionLogConfiguration as TaskDefinitionLogConfiguration
from .main import TaskDefinitionLogConfiguration1 as TaskDefinitionLogConfiguration1
from .main import TaskDefinitionMountPoint as TaskDefinitionMountPoint
from .main import TaskDefinitionPortMapping as TaskDefinitionPortMapping
from .main import TaskDefinitionSecret as TaskDefinitionSecret
from .main import TaskDefinitionVolumeFrom as TaskDefinitionVolumeFrom
from .messaging import ECSScheduledTask as ECSScheduledTask
from .messaging import ECSScheduledTaskEcsParameters as ECSScheduledTaskEcsParameters
from .messaging import ECSScheduledTaskTarget as ECSScheduledTaskTarget
from .network import ALBListener as ALBListener
from .network import ALBListenerAction as ALBListenerAction
from .network import ECSALB as ECSALB
from .network import ECSALBListenerRule as ECSALBListenerRule
from .network import ECSALBListenerRuleAction as ECSALBListenerRuleAction
from .network import ECSALBListenerRuleRuleCondition as ECSALBListenerRuleRuleCondition
from .network import ECSALBLoadBalancerAttribute as ECSALBLoadBalancerAttribute
from .network import ECSTG as ECSTG
from .network import EcsSecurityGroup as EcsSecurityGroup
from .outputs import ECSALBOutput as ECSALBOutput
from .outputs import EcsClusterOutput as EcsClusterOutput
from .outputs import EcsServiceOutput as EcsServiceOutput
from .outputs import EcsTaskDefOutput as EcsTaskDefOutput
from .params import CronOrRate as CronOrRate
from .params import CronRateCondition as CronRateCondition
from .params import CronSchedule as CronSchedule
from .params import DesiredCapacity as DesiredCapacity
from .params import InstanceType as InstanceType
from .params import KeyName as KeyName
from .params import LatestAmiId as LatestAmiId
from .params import MaxSize as MaxSize
from .params import RateSchedule as RateSchedule
from .params import SchedulerTasksCount as SchedulerTasksCount
from .params import SubnetId as SubnetId
from .params import VpcId as VpcId
from .security import AutoscalingRole as AutoscalingRole
from .security import AutoscalingRoleAllowStatement0 as AutoscalingRoleAllowStatement0
from .security import AutoscalingRoleAllowStatement0_1 as AutoscalingRoleAllowStatement0_1
from .security import AutoscalingRoleAssumeRolePolicyDocument as AutoscalingRoleAssumeRolePolicyDocument
from .security import AutoscalingRolePolicies0PolicyDocument as AutoscalingRolePolicies0PolicyDocument
from .security import AutoscalingRolePolicy as AutoscalingRolePolicy
from .security import EC2InstanceProfile as EC2InstanceProfile
from .security import EC2Role as EC2Role
from .security import EC2RoleAllowStatement0 as EC2RoleAllowStatement0
from .security import EC2RoleAllowStatement0_1 as EC2RoleAllowStatement0_1
from .security import EC2RoleAssumeRolePolicyDocument as EC2RoleAssumeRolePolicyDocument
from .security import EC2RolePolicies0PolicyDocument as EC2RolePolicies0PolicyDocument
from .security import EC2RolePolicy as EC2RolePolicy
from .security import ECSEventRole as ECSEventRole
from .security import ECSEventRoleAllowStatement0 as ECSEventRoleAllowStatement0
from .security import ECSEventRoleAllowStatement0_1 as ECSEventRoleAllowStatement0_1
from .security import ECSEventRoleAssumeRolePolicyDocument as ECSEventRoleAssumeRolePolicyDocument
from .security import ECSEventRolePolicies0PolicyDocument as ECSEventRolePolicies0PolicyDocument
from .security import ECSEventRolePolicy as ECSEventRolePolicy
from .security import ECSServiceRole as ECSServiceRole
from .security import ECSServiceRoleAllowStatement0 as ECSServiceRoleAllowStatement0
from .security import ECSServiceRoleAllowStatement0_1 as ECSServiceRoleAllowStatement0_1
from .security import ECSServiceRoleAssumeRolePolicyDocument as ECSServiceRoleAssumeRolePolicyDocument
from .security import ECSServiceRolePolicies0PolicyDocument as ECSServiceRolePolicies0PolicyDocument
from .security import ECSServiceRolePolicy as ECSServiceRolePolicy
from .security import LogsKmsKey as LogsKmsKey

__all__: list[str] = ['ALB500sAlarmScaleUp', 'ALB500sAlarmScaleUpDimension', 'ALBListener', 'ALBListenerAction', 'AWS_REGION', 'AWS_STACK_NAME', 'AutoscalingRole', 'AutoscalingRoleAllowStatement0', 'AutoscalingRoleAllowStatement0_1', 'AutoscalingRoleAssumeRolePolicyDocument', 'AutoscalingRolePolicies0PolicyDocument', 'AutoscalingRolePolicy', 'Base64', 'CloudwatchLogsGroup', 'ContainerInstances', 'CronOrRate', 'CronRateCondition', 'CronSchedule', 'DesiredCapacity', 'EC2InstanceProfile', 'EC2Role', 'EC2RoleAllowStatement0', 'EC2RoleAllowStatement0_1', 'EC2RoleAssumeRolePolicyDocument', 'EC2RolePolicies0PolicyDocument', 'EC2RolePolicy', 'ECSALB', 'ECSALBListenerRule', 'ECSALBListenerRuleAction', 'ECSALBListenerRuleRuleCondition', 'ECSALBLoadBalancerAttribute', 'ECSALBOutput', 'ECSAutoScalingGroup', 'ECSCluster', 'ECSEventRole', 'ECSEventRoleAllowStatement0', 'ECSEventRoleAllowStatement0_1', 'ECSEventRoleAssumeRolePolicyDocument', 'ECSEventRolePolicies0PolicyDocument', 'ECSEventRolePolicy', 'ECSScheduledTask', 'ECSScheduledTaskEcsParameters', 'ECSScheduledTaskTarget', 'ECSServiceRole', 'ECSServiceRoleAllowStatement0', 'ECSServiceRoleAllowStatement0_1', 'ECSServiceRoleAssumeRolePolicyDocument', 'ECSServiceRolePolicies0PolicyDocument', 'ECSServiceRolePolicy', 'ECSTG', 'EcsClusterOutput', 'EcsSecurityGroup', 'EcsSecurityGroupALBports', 'EcsSecurityGroupHTTPinbound', 'EcsSecurityGroupSSHinbound', 'EcsServiceOutput', 'EcsTaskDefOutput', 'Equals', 'If', 'InstanceType', 'Join', 'KeyName', 'LatestAmiId', 'LogsKmsKey', 'MaxSize', 'NUMBER', 'Output', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'RateSchedule', 'STRING', 'SchedulerTasksCount', 'Service', 'ServiceLoadBalancer', 'ServiceScalingPolicy', 'ServiceScalingPolicyStepAdjustment', 'ServiceScalingPolicyStepScalingPolicyConfiguration', 'ServiceScalingTarget', 'Sub', 'SubnetId', 'TaskDefinition', 'TaskDefinitionContainerDefinition', 'TaskDefinitionContainerDefinition1', 'TaskDefinitionLogConfiguration', 'TaskDefinitionLogConfiguration1', 'TaskDefinitionMountPoint', 'TaskDefinitionPortMapping', 'TaskDefinitionSecret', 'TaskDefinitionVolumeFrom', 'Template', 'TemplateCondition', 'VpcId', 'applicationautoscaling', 'autoscaling', 'cloudformation_dataclass', 'cloudwatch', 'ec2', 'ecs', 'elasticloadbalancingv2', 'events', 'get_att', 'iam', 'kms', 'logs', 'ref', 'setup_resources']
