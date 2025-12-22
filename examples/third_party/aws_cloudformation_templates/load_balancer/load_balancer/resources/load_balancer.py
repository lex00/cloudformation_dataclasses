"""LoadBalancer - AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoadBalancerLoadBalancerAttribute:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'deletion_protection.enabled'
    value = False


@cloudformation_dataclass
class LoadBalancerLoadBalancerAttribute1:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'routing.http.drop_invalid_header_fields.enabled'
    value = True


@cloudformation_dataclass
class LoadBalancer:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    resource: elasticloadbalancingv2.LoadBalancer
    load_balancer_attributes = [LoadBalancerLoadBalancerAttribute, LoadBalancerLoadBalancerAttribute1]
    scheme = 'internet-facing'
    security_groups = [get_att(LoadBalancerSecurityGroup, "GroupId")]
    subnets = [ref(PublicSubnet1), ref(PublicSubnet2)]
    type_ = 'application'
