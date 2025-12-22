from __future__ import annotations

"""OriginALBHttpsListener - AWS::ElasticLoadBalancingV2::Listener resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class OriginALBHttpsListenerAction:
    resource: Action
    target_group_arn = ref(OriginALBTG)
    type_ = 'forward'


@cloudformation_dataclass
class OriginALBHttpsListenerCertificate:
    resource: Certificate
    certificate_arn = Sub('arn:${AWS::Partition}:acm:${AWS::Region}:${AWS::AccountId}:certificate/${ACMCertificateIdentifier}')


@cloudformation_dataclass
class OriginALBHttpsListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: Listener
    default_actions = [OriginALBHttpsListenerAction]
    load_balancer_arn = ref(OriginALB)
    port = 443
    protocol = 'HTTPS'
    certificates = [OriginALBHttpsListenerCertificate]
    ssl_policy = 'ELBSecurityPolicy-FS-2018-06'
    depends_on = ["OriginALBTG"]
