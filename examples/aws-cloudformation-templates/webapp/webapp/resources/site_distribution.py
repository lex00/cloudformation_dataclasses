"""SiteDistribution - AWS::CloudFront::Distribution resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteDistributionDefaultCacheBehavior:
    resource: cloudfront.distribution.DefaultCacheBehavior
    cache_policy_id = '658327ea-f89d-4fab-a63d-7e88639e58f6'
    compress = True
    target_origin_id = Sub('${AppName}-origin-1')
    viewer_protocol_policy = 'redirect-to-https'


@cloudformation_dataclass
class SiteDistributionLogging:
    resource: cloudfront.distribution.Logging
    bucket = get_att(SiteCloudFrontLogsBucket, "RegionalDomainName")


@cloudformation_dataclass
class SiteDistributionS3OriginConfig:
    resource: cloudfront.distribution.S3OriginConfig
    origin_access_identity = ''


@cloudformation_dataclass
class SiteDistributionOrigin:
    resource: cloudfront.distribution.Origin
    domain_name = get_att(SiteContentBucket, "RegionalDomainName")
    id = Sub('${AppName}-origin-1')
    origin_access_control_id = get_att(SiteOriginAccessControl, "Id")
    s3_origin_config = SiteDistributionS3OriginConfig


@cloudformation_dataclass
class SiteDistributionViewerCertificate:
    resource: cloudfront.distribution.ViewerCertificate
    cloud_front_default_certificate = True


@cloudformation_dataclass
class SiteDistributionDistributionConfig:
    resource: cloudfront.distribution.DistributionConfig
    default_cache_behavior = SiteDistributionDefaultCacheBehavior
    default_root_object = 'index.html'
    enabled = True
    http_version = 'http2'
    ipv6_enabled = True
    logging = SiteDistributionLogging
    origins = [SiteDistributionOrigin]
    viewer_certificate = SiteDistributionViewerCertificate
    web_acl_id = get_att(SiteWebACL, "Arn")


@cloudformation_dataclass
class SiteDistribution:
    """AWS::CloudFront::Distribution resource."""

    resource: cloudfront.Distribution
    distribution_config = SiteDistributionDistributionConfig
