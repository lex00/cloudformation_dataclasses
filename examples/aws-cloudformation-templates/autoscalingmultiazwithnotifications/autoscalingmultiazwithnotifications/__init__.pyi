"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Mapping,
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
from cloudformation_dataclasses.aws import (
    autoscaling,
    cloudwatch,
    ec2,
    elasticloadbalancingv2,
    sns,
)
from cloudformation_dataclasses.aws.ec2.instance import AssociationParameter
from cloudformation_dataclasses.intrinsics import Base64, Join, Sub

from .compute import LaunchTemplate as LaunchTemplate
from .compute import LaunchTemplateBlockDeviceMapping as LaunchTemplateBlockDeviceMapping
from .compute import LaunchTemplateEbs as LaunchTemplateEbs
from .compute import LaunchTemplateLaunchTemplateData as LaunchTemplateLaunchTemplateData
from .compute import LaunchTemplateTagSpecification as LaunchTemplateTagSpecification
from .compute import WebServerGroup as WebServerGroup
from .compute import WebServerGroupLaunchTemplateSpecification as WebServerGroupLaunchTemplateSpecification
from .compute import WebServerGroupNotificationConfiguration as WebServerGroupNotificationConfiguration
from .compute import WebServerScaleDownPolicy as WebServerScaleDownPolicy
from .compute import WebServerScaleUpPolicy as WebServerScaleUpPolicy
from .messaging import NotificationTopic as NotificationTopic
from .messaging import NotificationTopicSubscription as NotificationTopicSubscription
from .monitoring import CPUAlarmHigh as CPUAlarmHigh
from .monitoring import CPUAlarmHighDimension as CPUAlarmHighDimension
from .monitoring import CPUAlarmLow as CPUAlarmLow
from .monitoring import CPUAlarmLowDimension as CPUAlarmLowDimension
from .network import ElasticLoadBalancer as ElasticLoadBalancer
from .network import InstanceSecurityGroup as InstanceSecurityGroup
from .network import InstanceSecurityGroupEgress as InstanceSecurityGroupEgress
from .network import InstanceSecurityGroupIngress as InstanceSecurityGroupIngress
from .network import LoadBalancerListener as LoadBalancerListener
from .network import LoadBalancerListenerAction as LoadBalancerListenerAction
from .network import LoadBalancerListenerCertificate as LoadBalancerListenerCertificate
from .network import LoadBalancerSecurityGroup as LoadBalancerSecurityGroup
from .network import LoadBalancerSecurityGroupEgress as LoadBalancerSecurityGroupEgress
from .network import TargetGroup as TargetGroup
from .outputs import URLOutput as URLOutput
from .params import AZs as AZs
from .params import CertificateArn as CertificateArn
from .params import InstanceType as InstanceType
from .params import KeyName as KeyName
from .params import KmsKeyArn as KmsKeyArn
from .params import LatestAmiId as LatestAmiId
from .params import OperatorEMail as OperatorEMail
from .params import Region2ExamplesMapping as Region2ExamplesMapping
from .params import SSHLocation as SSHLocation
from .params import SecurityGroups as SecurityGroups
from .params import Subnets as Subnets
from .params import VPC as VPC

__all__: list[str] = ['AZs', 'AssociationParameter', 'Base64', 'CPUAlarmHigh', 'CPUAlarmHighDimension', 'CPUAlarmLow', 'CPUAlarmLowDimension', 'CertificateArn', 'ElasticLoadBalancer', 'InstanceSecurityGroup', 'InstanceSecurityGroupEgress', 'InstanceSecurityGroupIngress', 'InstanceType', 'Join', 'KeyName', 'KmsKeyArn', 'LatestAmiId', 'LaunchTemplate', 'LaunchTemplateBlockDeviceMapping', 'LaunchTemplateEbs', 'LaunchTemplateLaunchTemplateData', 'LaunchTemplateTagSpecification', 'LoadBalancerListener', 'LoadBalancerListenerAction', 'LoadBalancerListenerCertificate', 'LoadBalancerSecurityGroup', 'LoadBalancerSecurityGroupEgress', 'Mapping', 'NotificationTopic', 'NotificationTopicSubscription', 'OperatorEMail', 'Output', 'Parameter', 'ParameterType', 'Region2ExamplesMapping', 'SSHLocation', 'STRING', 'SecurityGroups', 'Sub', 'Subnets', 'TargetGroup', 'Template', 'URLOutput', 'VPC', 'WebServerGroup', 'WebServerGroupLaunchTemplateSpecification', 'WebServerGroupNotificationConfiguration', 'WebServerScaleDownPolicy', 'WebServerScaleUpPolicy', 'autoscaling', 'cloudformation_dataclass', 'cloudwatch', 'ec2', 'elasticloadbalancingv2', 'get_att', 'ref', 'setup_resources', 'sns']
