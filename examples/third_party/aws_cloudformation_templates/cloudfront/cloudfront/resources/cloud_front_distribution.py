"""CloudFrontDistribution - AWS::CloudFront::Distribution resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CloudFrontDistributionCustomOriginConfig:
    resource: CustomOriginConfig
    http_port = 80
    https_port = 443
    origin_protocol_policy = ref(OriginProtocolPolicy)
    origin_keepalive_timeout = ref(OriginKeepaliveTimeout)
    origin_read_timeout = ref(OriginReadTimeout)
    origin_ssl_protocols = ['TLSv1', 'TLSv1.1', 'TLSv1.2', 'SSLv3']


@cloudformation_dataclass
class CloudFrontDistributionOrigin:
    resource: Origin
    domain_name = get_att(OriginALB, "DNSName")
    id = ref(OriginALB)
    custom_origin_config = CloudFrontDistributionCustomOriginConfig


@cloudformation_dataclass
class CloudFrontDistributionCookies:
    resource: Cookies
    forward = ref(ForwardCookies)


@cloudformation_dataclass
class CloudFrontDistributionForwardedValues:
    resource: ForwardedValues
    query_string = ref(QueryString)
    cookies = CloudFrontDistributionCookies


@cloudformation_dataclass
class CloudFrontDistributionLambdaFunctionAssociation:
    resource: LambdaFunctionAssociation
    event_type = ref(LambdaEventType)
    lambda_function_arn = ref(LambdaEdgeVersion)


@cloudformation_dataclass
class CloudFrontDistributionDefaultCacheBehavior:
    resource: DefaultCacheBehavior
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
    resource: ViewerCertificate
    acm_certificate_arn = Sub('arn:${AWS::Partition}:acm:${AWS::Region}:${AWS::AccountId}:certificate/${ACMCertificateIdentifier}')
    ssl_support_method = ref(SslSupportMethod)
    minimum_protocol_version = ref(MinimumProtocolVersion)


@cloudformation_dataclass
class CloudFrontDistributionLogging:
    resource: Logging
    bucket = Sub('${LoggingBucket}.s3.amazonaws.com')


@cloudformation_dataclass
class CloudFrontDistributionDistributionConfig:
    resource: DistributionConfig
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

    resource: Distribution
    distribution_config = CloudFrontDistributionDistributionConfig
    depends_on = ["LoggingBucket", "LambdaEdgeFunction"]
