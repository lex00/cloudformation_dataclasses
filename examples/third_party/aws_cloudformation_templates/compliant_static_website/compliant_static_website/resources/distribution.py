from __future__ import annotations

"""Distribution - AWS::CloudFront::Distribution resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DistributionDefaultCacheBehavior:
    resource: DefaultCacheBehavior
    cache_policy_id = 'rain-build-cache-policy-1'
    compress = True
    target_origin_id = 'rain-build-origin-1'
    viewer_protocol_policy = 'redirect-to-https'


@cloudformation_dataclass
class DistributionLogging:
    resource: Logging
    bucket: GetAtt[CloudFrontLogsBucket] = get_att("RegionalDomainName")


@cloudformation_dataclass
class DistributionS3OriginConfig:
    resource: S3OriginConfig
    origin_access_identity = ''


@cloudformation_dataclass
class DistributionOrigin:
    resource: Origin
    domain_name: GetAtt[ContentBucket] = get_att("RegionalDomainName")
    id = 'rain-build-origin-1'
    origin_access_control_id: GetAtt[OriginAccessControl] = get_att("Id")
    s3_origin_config = DistributionS3OriginConfig


@cloudformation_dataclass
class DistributionViewerCertificate:
    resource: ViewerCertificate
    cloud_front_default_certificate = True


@cloudformation_dataclass
class DistributionDistributionConfig:
    resource: DistributionConfig
    default_cache_behavior = DistributionDefaultCacheBehavior
    default_root_object = 'index.html'
    enabled = True
    http_version = 'http2'
    ipv6_enabled = True
    logging = DistributionLogging
    origins = [DistributionOrigin]
    viewer_certificate = DistributionViewerCertificate
    web_acl_id = ref(WebACL)


@cloudformation_dataclass
class Distribution:
    """AWS::CloudFront::Distribution resource."""

    resource: cloudfront.Distribution
    distribution_config = DistributionDistributionConfig
