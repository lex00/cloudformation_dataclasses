from __future__ import annotations

"""LoadBalancerListener - AWS::ElasticLoadBalancingV2::Listener resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoadBalancerListenerAction:
    resource: Action
    target_group_arn: Ref[TargetGroup] = ref()
    type_ = 'forward'


@cloudformation_dataclass
class LoadBalancerListenerCertificate:
    resource: Certificate
    certificate_arn = ref(CertificateArn)


@cloudformation_dataclass
class LoadBalancerListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: Listener
    default_actions = [LoadBalancerListenerAction]
    load_balancer_arn: Ref[LoadBalancer] = ref()
    port = 443
    protocol = 'HTTPS'
    certificates = [LoadBalancerListenerCertificate]
    ssl_policy = 'ELBSecurityPolicy-TLS13-1-2-2021-06'
