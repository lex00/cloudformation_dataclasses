from __future__ import annotations

"""LoadBalancerListener - AWS::ElasticLoadBalancingV2::Listener resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoadBalancerListenerAction:
    resource: Action
    type_ = 'forward'
    target_group_arn: Ref[TargetGroup] = ref()


@cloudformation_dataclass
class LoadBalancerListenerCertificate:
    resource: Certificate
    certificate_arn = ref(CertificateArn)


@cloudformation_dataclass
class LoadBalancerListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: Listener
    default_actions = [LoadBalancerListenerAction]
    load_balancer_arn: Ref[ElasticLoadBalancer] = ref()
    port = 443
    protocol = 'HTTPS'
    ssl_policy = 'ELBSecurityPolicy-2016-08'
    certificates = [LoadBalancerListenerCertificate]
