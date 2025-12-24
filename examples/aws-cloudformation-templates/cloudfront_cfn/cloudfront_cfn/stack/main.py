"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EC2InstanceSGAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AppName}-${Environment}-ec2-instance-SG')


@cloudformation_dataclass
class EC2InstanceSGAssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Environment'
    value = ref(Environment)


@cloudformation_dataclass
class EC2InstanceSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'EC2 Instance Security Group'
    vpc_id = ref(VpcId)
    tags = [EC2InstanceSGAssociationParameter, EC2InstanceSGAssociationParameter1]


@cloudformation_dataclass
class ALBExternalAccessSGAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AppName}-${Environment}-alb-external-access-ingrees-SG')


@cloudformation_dataclass
class ALBExternalAccessSGAssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Environment'
    value = ref(Environment)


@cloudformation_dataclass
class ALBExternalAccessSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Allow external access to ALB'
    vpc_id = ref(VpcId)
    tags = [ALBExternalAccessSGAssociationParameter, ALBExternalAccessSGAssociationParameter1]


@cloudformation_dataclass
class EC2InstanceEbs:
    resource: ec2.instance.Ebs
    volume_size = ref(BootVolSize)
    volume_type = ref(BootVolType)


@cloudformation_dataclass
class EC2InstanceBlockDeviceMapping:
    resource: ec2.instance.BlockDeviceMapping
    device_name = '/dev/sda1'
    ebs = EC2InstanceEbs


@cloudformation_dataclass
class EC2InstanceAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AppName}-${Environment}-ec2-instance')


@cloudformation_dataclass
class EC2InstanceAssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Environment'
    value = ref(Environment)


@cloudformation_dataclass
class EC2Instance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    image_id = ref(EC2ImageId)
    instance_type = ref(EC2InstanceType)
    subnet_id = ref(PublicSubnetId1)
    block_device_mappings = [EC2InstanceBlockDeviceMapping]
    security_group_ids = [ref(EC2InstanceSG), ref(ALBExternalAccessSG)]
    key_name = ref(KeyPairName)
    tags = [EC2InstanceAssociationParameter, EC2InstanceAssociationParameter1]


@cloudformation_dataclass
class Tcp8080In:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    group_id = ref(EC2InstanceSG)
    to_port = '8080'
    ip_protocol = 'tcp'
    from_port = '8080'
    source_security_group_id = ref(ALBExternalAccessSG)


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


@cloudformation_dataclass
class OriginALBTGLoadBalancerAttribute:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'deregistration_delay.timeout_seconds'
    value = ref(ALBTargetGroupAttributeDeregistration)


@cloudformation_dataclass
class OriginALBTGTargetDescription:
    resource: elasticloadbalancingv2.target_group.TargetDescription
    id = ref(EC2Instance)
    port = ref(OriginALBTGPort)


@cloudformation_dataclass
class OriginALBTGLoadBalancerAttribute1:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'Name'
    value = Sub('${AppName}-${Environment}-alb-tg')


@cloudformation_dataclass
class OriginALBTGLoadBalancerAttribute2:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'Environment'
    value = ref(Environment)


@cloudformation_dataclass
class OriginALBTG:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    name = Sub('${AppName}-${Environment}-alb-tg')
    health_check_protocol = ref(HealthCheckProtocol)
    health_check_path = ref(HealthCheckPath)
    health_check_port = Sub('${OriginALBTGPort}')
    health_check_interval_seconds = ref(ALBTargetGroupHealthCheckIntervalSeconds)
    health_check_timeout_seconds = ref(ALBTargetGroupHealthCheckTimeoutSeconds)
    healthy_threshold_count = ref(ALBTargetGroupHealthyThresholdCount)
    unhealthy_threshold_count = ref(ALBTargetGroupUnhealthyThresholdCount)
    target_group_attributes = [OriginALBTGLoadBalancerAttribute]
    target_type = 'instance'
    targets = [OriginALBTGTargetDescription]
    port = ref(OriginALBTGPort)
    protocol = 'HTTP'
    vpc_id = ref(VpcId)
    tags = [OriginALBTGLoadBalancerAttribute1, OriginALBTGLoadBalancerAttribute2]
    depends_on = ["OriginALB"]


@cloudformation_dataclass
class OriginALBHttpsListenerAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    target_group_arn = ref(OriginALBTG)
    type_ = 'forward'


@cloudformation_dataclass
class OriginALBHttpsListenerCertificate:
    resource: elasticloadbalancingv2.listener_certificate.Certificate
    certificate_arn = Sub('arn:${AWS::Partition}:acm:${AWS::Region}:${AWS::AccountId}:certificate/${ACMCertificateIdentifier}')


@cloudformation_dataclass
class OriginALBHttpsListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: elasticloadbalancingv2.Listener
    default_actions = [OriginALBHttpsListenerAction]
    load_balancer_arn = ref(OriginALB)
    port = 443
    protocol = 'HTTPS'
    certificates = [OriginALBHttpsListenerCertificate]
    ssl_policy = 'ELBSecurityPolicy-FS-2018-06'
    depends_on = ["OriginALBTG"]


@cloudformation_dataclass
class OriginALBHttpsListenerRuleAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    type_ = 'forward'
    target_group_arn = ref(OriginALBTG)


@cloudformation_dataclass
class OriginALBHttpsListenerRuleRuleCondition:
    resource: elasticloadbalancingv2.listener_rule.RuleCondition
    field = 'path-pattern'
    values = ['/*']


@cloudformation_dataclass
class OriginALBHttpsListenerRule:
    """AWS::ElasticLoadBalancingV2::ListenerRule resource."""

    resource: elasticloadbalancingv2.ListenerRule
    actions = [OriginALBHttpsListenerRuleAction]
    conditions = [OriginALBHttpsListenerRuleRuleCondition]
    listener_arn = ref(OriginALBHttpsListener)
    priority = 1
    depends_on = ["OriginALBHttpsListener"]


@cloudformation_dataclass
class HTTPSTcpIn:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    group_id = ref(ALBExternalAccessSG)
    to_port = 443
    ip_protocol = 'tcp'
    from_port = 443
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class HTTPTcpIn:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    group_id = ref(ALBExternalAccessSG)
    to_port = 80
    ip_protocol = 'tcp'
    from_port = 80
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class Tcp8080Out:
    """AWS::EC2::SecurityGroupEgress resource."""

    resource: ec2.SecurityGroupEgress
    group_id = ref(ALBExternalAccessSG)
    to_port = 8080
    ip_protocol = 'tcp'
    from_port = 8080
    destination_security_group_id = ref(EC2InstanceSG)


@cloudformation_dataclass
class LambdaEdgeFunctionCode:
    resource: lambda_.function.Code
    zip_file = """'use strict';

 exports.handler = (event, context, callback) => {
    console.log('Adding additional headers to CloudFront response.');

    const response = event.Records[0].cf.response;
    response.headers['strict-transport-security'] = [{
    key: 'Strict-Transport-Security',
    value: 'max-age=86400; includeSubdomains; preload',
    }];
    response.headers['x-content-type-options'] = [{
    key: 'X-Content-Type-Options',
    value: 'nosniff',
    }];
    response.headers['x-frame-options'] = [{
        key:   'X-Frame-Options',
        value: "DENY"
    }];
    response.headers['content-security-policy'] = [{
        key:   'Content-Security-Policy',
        value: "default-src 'none'; img-src 'self'; script-src 'self'; style-src 'self'; object-src 'none'"
    }];
    response.headers['x-xss-protection'] = [{
        key:   'X-XSS-Protection',
        value: "1; mode=block"
    }];
    response.headers['referrer-policy'] = [{
        key:   'Referrer-Policy',
        value: "same-origin"
    }];
    callback(null, response);
  };
"""


@cloudformation_dataclass
class LambdaEdgeFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    description = 'A custom Lambda@Edge function for serving custom headers from CloudFront Distribution'
    function_name = Sub('${AppName}-lambda-edge-${Environment}')
    handler = 'index.handler'
    role = get_att(LambdaEdgeIAMRole, "Arn")
    memory_size = 128
    timeout = 5
    code = LambdaEdgeFunctionCode
    runtime = 'nodejs20.x'


@cloudformation_dataclass
class LambdaEdgeVersion:
    """AWS::Lambda::Version resource."""

    resource: lambda_.Version
    function_name = ref(LambdaEdgeFunction)


@cloudformation_dataclass
class CloudFrontDistributionCustomOriginConfig:
    resource: cloudfront.distribution.CustomOriginConfig
    http_port = 80
    https_port = 443
    origin_protocol_policy = ref(OriginProtocolPolicy)
    origin_keepalive_timeout = ref(OriginKeepaliveTimeout)
    origin_read_timeout = ref(OriginReadTimeout)
    origin_ssl_protocols = ['TLSv1', 'TLSv1.1', 'TLSv1.2', 'SSLv3']


@cloudformation_dataclass
class CloudFrontDistributionOrigin:
    resource: cloudfront.distribution.Origin
    domain_name = get_att(OriginALB, "DNSName")
    id = ref(OriginALB)
    custom_origin_config = CloudFrontDistributionCustomOriginConfig


@cloudformation_dataclass
class CloudFrontDistributionCookies:
    resource: cloudfront.distribution.Cookies
    forward = ref(ForwardCookies)


@cloudformation_dataclass
class CloudFrontDistributionForwardedValues:
    resource: cloudfront.distribution.ForwardedValues
    query_string = ref(QueryString)
    cookies = CloudFrontDistributionCookies


@cloudformation_dataclass
class CloudFrontDistributionLambdaFunctionAssociation:
    resource: cloudfront.distribution.LambdaFunctionAssociation
    event_type = ref(LambdaEventType)
    lambda_function_arn = ref(LambdaEdgeVersion)


@cloudformation_dataclass
class CloudFrontDistributionDefaultCacheBehavior:
    resource: cloudfront.distribution.DefaultCacheBehavior
    allowed_methods = ['GET', 'HEAD', 'DELETE', 'OPTIONS', 'PATCH', 'POST', 'PUT']
    compress = ref(Compress)
    default_ttl = ref(DefaultTTL)
    max_ttl = ref(MaxTTL)
    min_ttl = ref(MinTTL)
    smooth_streaming = 'false'
    target_origin_id = ref(OriginALB)
    forwarded_values = CloudFrontDistributionForwardedValues
    viewer_protocol_policy = ref(ViewerProtocolPolicy)
    lambda_function_associations = [CloudFrontDistributionLambdaFunctionAssociation]


@cloudformation_dataclass
class CloudFrontDistributionViewerCertificate:
    resource: cloudfront.distribution.ViewerCertificate
    acm_certificate_arn = Sub('arn:${AWS::Partition}:acm:${AWS::Region}:${AWS::AccountId}:certificate/${ACMCertificateIdentifier}')
    ssl_support_method = ref(SslSupportMethod)
    minimum_protocol_version = ref(MinimumProtocolVersion)


@cloudformation_dataclass
class CloudFrontDistributionLogging:
    resource: cloudfront.distribution.Logging
    bucket = Sub('${LoggingBucket}.s3.amazonaws.com')


@cloudformation_dataclass
class CloudFrontDistributionDistributionConfig:
    resource: cloudfront.distribution.DistributionConfig
    comment = 'Cloudfront Distribution pointing ALB Origin'
    origins = [CloudFrontDistributionOrigin]
    enabled = True
    http_version = 'http2'
    aliases = [ref(AlternateDomainNames)]
    default_cache_behavior = CloudFrontDistributionDefaultCacheBehavior
    price_class = ref(PriceClass)
    viewer_certificate = CloudFrontDistributionViewerCertificate
    ipv6_enabled = ref(IPV6Enabled)
    logging = CloudFrontDistributionLogging


@cloudformation_dataclass
class CloudFrontDistribution:
    """AWS::CloudFront::Distribution resource."""

    resource: cloudfront.Distribution
    distribution_config = CloudFrontDistributionDistributionConfig
    depends_on = ["LoggingBucket", "LambdaEdgeFunction"]
