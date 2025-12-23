"""Network resources: LoadBalancerSecurityGroup, LoadBalancer, TargetGroup, LoadBalancerListener."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoadBalancerSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Automatically created Security Group for ELB'
    security_group_ingress = [{
        'CidrIp': '0.0.0.0/0',
        'Description': 'Allow from anyone on port 443',
        'FromPort': 443,
        'IpProtocol': 'tcp',
        'ToPort': 443,
    }]
    vpc_id = ref(VPCId)


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


@cloudformation_dataclass
class TargetGroupLoadBalancerAttribute:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'deregistration_delay.timeout_seconds'
    value = '10'


@cloudformation_dataclass
class TargetGroupLoadBalancerAttribute1:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'stickiness.enabled'
    value = 'false'


@cloudformation_dataclass
class TargetGroup:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    port = 80
    protocol = 'HTTP'
    target_group_attributes = [TargetGroupLoadBalancerAttribute, TargetGroupLoadBalancerAttribute1]
    target_type = 'ip'
    vpc_id = ref(VPCId)


@cloudformation_dataclass
class LoadBalancerListenerAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    target_group_arn = ref(TargetGroup)
    type_ = 'forward'


@cloudformation_dataclass
class LoadBalancerListenerCertificate:
    resource: elasticloadbalancingv2.listener_certificate.Certificate
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
