"""OriginALB - AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class OriginALBLoadBalancerAttribute:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'idle_timeout.timeout_seconds'
    value = ref(ALBAttributeIdleTimeOut)


@cloudformation_dataclass
class OriginALBLoadBalancerAttribute1:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'deletion_protection.enabled'
    value = ref(ALBAttributeDeletionProtection)


@cloudformation_dataclass
class OriginALBLoadBalancerAttribute2:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'routing.http2.enabled'
    value = ref(ALBAttributeRoutingHttp2)


@cloudformation_dataclass
class OriginALBLoadBalancerAttribute3:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'Name'
    value = Sub('${AppName}-${Environment}-alb')


@cloudformation_dataclass
class OriginALBLoadBalancerAttribute4:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'Environment'
    value = ref(Environment)


@cloudformation_dataclass
class OriginALB:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    resource: elasticloadbalancingv2.LoadBalancer
    name = Sub('${AppName}-${Environment}-alb')
    scheme = ref(ALBScheme)
    type_ = ref(ALBType)
    load_balancer_attributes = [OriginALBLoadBalancerAttribute, OriginALBLoadBalancerAttribute1, OriginALBLoadBalancerAttribute2]
    subnets = [ref(PublicSubnetId1), ref(PublicSubnetId2)]
    security_groups = [ref(ALBExternalAccessSG)]
    tags = [OriginALBLoadBalancerAttribute3, OriginALBLoadBalancerAttribute4]
