"""LoadBalancerListener - AWS::ElasticLoadBalancingV2::Listener resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoadBalancerListenerAction:
    resource: elasticloadbalancingv2.Action
    target_group_arn = ref(TargetGroup)
    type_ = 'forward'


@cloudformation_dataclass
class LoadBalancerListenerCertificate:
    resource: elasticloadbalancingv2.Certificate
    certificate_arn = ref(CertificateArn)


@cloudformation_dataclass
class LoadBalancerListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: elasticloadbalancingv2.Listener
    default_actions = [LoadBalancerListenerAction]
    load_balancer_arn = ref(LoadBalancer)
    port = 443
    protocol = 'HTTPS'
    certificates = [LoadBalancerListenerCertificate]
    ssl_policy = 'ELBSecurityPolicy-TLS13-1-2-2021-06'
