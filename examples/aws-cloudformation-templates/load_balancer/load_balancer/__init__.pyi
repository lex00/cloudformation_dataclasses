"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    Parameter,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import ec2, elasticloadbalancingv2
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .compute import LoadBalancerEgress as LoadBalancerEgress
from .network import LoadBalancer as LoadBalancer
from .network import LoadBalancerListener as LoadBalancerListener
from .network import LoadBalancerListenerAction as LoadBalancerListenerAction
from .network import LoadBalancerListenerCertificate as LoadBalancerListenerCertificate
from .network import LoadBalancerLoadBalancerAttribute as LoadBalancerLoadBalancerAttribute
from .network import LoadBalancerLoadBalancerAttribute1 as LoadBalancerLoadBalancerAttribute1
from .network import LoadBalancerSecurityGroup as LoadBalancerSecurityGroup
from .network import LoadBalancerSecurityGroupEgress as LoadBalancerSecurityGroupEgress
from .network import TargetGroup as TargetGroup
from .network import TargetGroupLoadBalancerAttribute as TargetGroupLoadBalancerAttribute
from .network import TargetGroupLoadBalancerAttribute1 as TargetGroupLoadBalancerAttribute1
from .outputs import LoadBalancerDNSOutput as LoadBalancerDNSOutput
from .params import CertificateArn as CertificateArn
from .params import DestinationSecurityGroupId as DestinationSecurityGroupId
from .params import PublicSubnet1 as PublicSubnet1
from .params import PublicSubnet2 as PublicSubnet2
from .params import VPCId as VPCId

__all__: list[str] = ['CertificateArn', 'DestinationSecurityGroupId', 'LoadBalancer', 'LoadBalancerDNSOutput', 'LoadBalancerEgress', 'LoadBalancerListener', 'LoadBalancerListenerAction', 'LoadBalancerListenerCertificate', 'LoadBalancerLoadBalancerAttribute', 'LoadBalancerLoadBalancerAttribute1', 'LoadBalancerSecurityGroup', 'LoadBalancerSecurityGroupEgress', 'Output', 'Parameter', 'PublicSubnet1', 'PublicSubnet2', 'STRING', 'TargetGroup', 'TargetGroupLoadBalancerAttribute', 'TargetGroupLoadBalancerAttribute1', 'Template', 'VPCId', 'cloudformation_dataclass', 'ec2', 'elasticloadbalancingv2', 'get_att', 'ref', 'setup_resources']
