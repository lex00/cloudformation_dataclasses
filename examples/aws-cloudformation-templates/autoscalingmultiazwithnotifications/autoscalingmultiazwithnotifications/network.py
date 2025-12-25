"""Network resources: TargetGroup, LoadBalancerSecurityGroup, ElasticLoadBalancer, LoadBalancerListener, InstanceSecurityGroup."""

from . import *  # noqa: F403

from cloudformation_dataclasses.core.constants import IpProtocol


@cloudformation_dataclass
class TargetGroup:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    health_check_path = '/'
    name = 'MyTargetGroup'
    port = 80
    protocol = 'HTTP'
    target_type = 'instance'
    vpc_id = ref(VPC)


@cloudformation_dataclass
class LoadBalancerSecurityGroupEgress:
    resource: ec2.security_group.Egress
    ip_protocol = IpProtocol.TCP
    from_port = 443
    to_port = 443
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class LoadBalancerSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Allows inbound traffic on port 443'
    security_group_ingress = [LoadBalancerSecurityGroupEgress]
    vpc_id = ref(VPC)


@cloudformation_dataclass
class ElasticLoadBalancer:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    resource: elasticloadbalancingv2.LoadBalancer
    scheme = 'internet-facing'
    security_groups = [ref(LoadBalancerSecurityGroup)]
    subnets = ref(Subnets)
    type_ = 'application'


@cloudformation_dataclass
class LoadBalancerListenerAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    type_ = 'forward'
    target_group_arn = ref(TargetGroup)


@cloudformation_dataclass
class LoadBalancerListenerCertificate:
    resource: elasticloadbalancingv2.listener_certificate.Certificate
    certificate_arn = ref(CertificateArn)


@cloudformation_dataclass
class LoadBalancerListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: elasticloadbalancingv2.Listener
    default_actions = [LoadBalancerListenerAction]
    load_balancer_arn = ref(ElasticLoadBalancer)
    port = 443
    protocol = 'HTTPS'
    ssl_policy = 'ELBSecurityPolicy-2016-08'
    certificates = [LoadBalancerListenerCertificate]


@cloudformation_dataclass
class InstanceSecurityGroupEgress:
    resource: ec2.security_group.Egress
    ip_protocol = IpProtocol.TCP
    from_port = 22
    to_port = 22
    cidr_ip = ref(SSHLocation)


@cloudformation_dataclass
class InstanceSecurityGroupIngress:
    resource: ec2.security_group.Ingress
    ip_protocol = IpProtocol.TCP
    from_port = 80
    to_port = 80
    source_security_group_id = ref(LoadBalancerSecurityGroup)


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable SSH access and HTTP from the load balancer only'
    security_group_ingress = [InstanceSecurityGroupEgress, InstanceSecurityGroupIngress]
