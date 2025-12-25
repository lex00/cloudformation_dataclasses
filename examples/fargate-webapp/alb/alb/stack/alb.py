"""ALB resources - Load balancer, listeners, target group, Route53 record."""

from .. import *  # noqa: F403, F401

# =============================================================================
# Security Group Ingress Rules
# =============================================================================


@cloudformation_dataclass
class HttpIngress:
    resource: ec2.security_group.Ingress
    ip_protocol = IpProtocol.TCP
    from_port = 80
    to_port = 80
    cidr_ip = "0.0.0.0/0"


@cloudformation_dataclass
class HttpsIngress:
    resource: ec2.security_group.Ingress
    ip_protocol = IpProtocol.TCP
    from_port = 443
    to_port = 443
    cidr_ip = "0.0.0.0/0"


# =============================================================================
# Security Group
# =============================================================================


@cloudformation_dataclass
class AlbSecurityGroup:
    resource: ec2.SecurityGroup
    group_description = "ALB security group - allows HTTP/HTTPS from anywhere"
    vpc_id = ref(VpcIdParam)
    security_group_ingress = [HttpIngress, HttpsIngress]


# =============================================================================
# Application Load Balancer
# =============================================================================


@cloudformation_dataclass
class ApplicationLoadBalancer:
    resource: elasticloadbalancingv2.LoadBalancer
    scheme = "internet-facing"
    type_ = "application"
    security_groups = [ref(AlbSecurityGroup)]
    subnets = ref(PublicSubnetIdsParam)


# =============================================================================
# Target Group (for Fargate service)
# =============================================================================


@cloudformation_dataclass
class TargetGroup:
    resource: elasticloadbalancingv2.TargetGroup
    vpc_id = ref(VpcIdParam)
    port = 80
    protocol = "HTTP"
    target_type = "ip"
    health_check_path = "/"
    health_check_interval_seconds = 30
    health_check_timeout_seconds = 5
    healthy_threshold_count = 2
    unhealthy_threshold_count = 3


# =============================================================================
# Listener Actions
# =============================================================================


@cloudformation_dataclass
class HttpToHttpsRedirectConfig:
    resource: elasticloadbalancingv2.listener.RedirectConfig
    protocol = "HTTPS"
    port = "443"
    status_code = "HTTP_301"


@cloudformation_dataclass
class HttpRedirectAction:
    resource: elasticloadbalancingv2.listener.Action
    type_ = "redirect"
    redirect_config = HttpToHttpsRedirectConfig


@cloudformation_dataclass
class HttpsForwardAction:
    resource: elasticloadbalancingv2.listener.Action
    type_ = "forward"
    target_group_arn = ref(TargetGroup)


@cloudformation_dataclass
class HttpsListenerCertificate:
    resource: elasticloadbalancingv2.listener.Certificate
    certificate_arn = ref(CertificateArnParam)


# =============================================================================
# Listeners
# =============================================================================


@cloudformation_dataclass
class HttpListener:
    resource: elasticloadbalancingv2.Listener
    load_balancer_arn = ref(ApplicationLoadBalancer)
    port = 80
    protocol = "HTTP"
    default_actions = [HttpRedirectAction]


@cloudformation_dataclass
class HttpsListener:
    resource: elasticloadbalancingv2.Listener
    load_balancer_arn = ref(ApplicationLoadBalancer)
    port = 443
    protocol = "HTTPS"
    ssl_policy = "ELBSecurityPolicy-TLS13-1-2-2021-06"
    certificates = [HttpsListenerCertificate]
    default_actions = [HttpsForwardAction]


# =============================================================================
# Route53 DNS Record
# =============================================================================


@cloudformation_dataclass
class DnsRecordAliasTarget:
    resource: route53.record_set.AliasTarget
    dns_name = get_att(ApplicationLoadBalancer, "DNSName")
    hosted_zone_id = get_att(ApplicationLoadBalancer, "CanonicalHostedZoneID")
    evaluate_target_health = True


@cloudformation_dataclass
class DnsRecord:
    resource: route53.RecordSet
    hosted_zone_id = ref(HostedZoneIdParam)
    name = ref(DomainNameParam)
    type_ = "A"
    alias_target = DnsRecordAliasTarget
