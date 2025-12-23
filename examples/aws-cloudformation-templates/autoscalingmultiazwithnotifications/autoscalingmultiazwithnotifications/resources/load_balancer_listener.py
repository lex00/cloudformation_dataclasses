"""LoadBalancerListener - AWS::ElasticLoadBalancingV2::Listener resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoadBalancerListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    # Unknown resource type: AWS::ElasticLoadBalancingV2::Listener
    resource: CloudFormationResource
    default_actions = [{
        'Type': 'forward',
        'TargetGroupArn': ref(TargetGroup),
    }]
    load_balancer_arn = ref(ElasticLoadBalancer)
    port = 443
    protocol = 'HTTPS'
    ssl_policy = 'ELBSecurityPolicy-2016-08'
    certificates = [{
        'CertificateArn': ref(CertificateArn),
    }]
