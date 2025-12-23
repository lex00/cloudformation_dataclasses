"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CachePolicyCookiesConfig:
    resource: cloudfront.cache_policy.CookiesConfig
    cookie_behavior = 'all'


@cloudformation_dataclass
class CachePolicyHeadersConfig:
    resource: cloudfront.cache_policy.HeadersConfig
    header_behavior = 'whitelist'
    headers = ['Accept-Charset', 'Authorization', 'Origin', 'Accept', 'Referer', 'Host', 'Accept-Language', 'Accept-Encoding', 'Accept-Datetime']


@cloudformation_dataclass
class CachePolicyQueryStringsConfig:
    resource: cloudfront.cache_policy.QueryStringsConfig
    query_string_behavior = 'all'


@cloudformation_dataclass
class CachePolicyParametersInCacheKeyAndForwardedToOrigin:
    resource: cloudfront.cache_policy.ParametersInCacheKeyAndForwardedToOrigin
    cookies_config = CachePolicyCookiesConfig
    enable_accept_encoding_gzip = False
    headers_config = CachePolicyHeadersConfig
    query_strings_config = CachePolicyQueryStringsConfig


@cloudformation_dataclass
class CachePolicyCachePolicyConfig:
    resource: cloudfront.cache_policy.CachePolicyConfig
    default_ttl = 86400
    max_ttl = 31536000
    min_ttl = 1
    name = ref(Name)
    parameters_in_cache_key_and_forwarded_to_origin = CachePolicyParametersInCacheKeyAndForwardedToOrigin


@cloudformation_dataclass
class CachePolicy:
    """AWS::CloudFront::CachePolicy resource."""

    resource: cloudfront.CachePolicy
    cache_policy_config = CachePolicyCachePolicyConfig


@cloudformation_dataclass
class DistributionCacheBehavior:
    resource: cloudfront.distribution.CacheBehavior
    allowed_methods = ['GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'POST', 'DELETE']
    cache_policy_id = '4135ea2d-6df8-44a3-9df3-4b5a84be39ad'
    compress = False
    origin_request_policy_id = '216adef6-5c7f-47e4-b989-5492eafa07d3'
    target_origin_id = Sub('CloudFront-${AWS::StackName}')
    viewer_protocol_policy = 'allow-all'
    path_pattern = '/proxy/*'


@cloudformation_dataclass
class DistributionDefaultCacheBehavior:
    resource: cloudfront.distribution.DefaultCacheBehavior
    allowed_methods = ['GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'POST', 'DELETE']
    cache_policy_id = ref(CachePolicy)
    origin_request_policy_id = '216adef6-5c7f-47e4-b989-5492eafa07d3'
    target_origin_id = Sub('CloudFront-${AWS::StackName}')
    viewer_protocol_policy = 'allow-all'


@cloudformation_dataclass
class DistributionCustomOriginConfig:
    resource: cloudfront.distribution.CustomOriginConfig
    http_port = ref(Port)
    origin_protocol_policy = 'http-only'


@cloudformation_dataclass
class DistributionOrigin:
    resource: cloudfront.distribution.Origin
    domain_name = ref(DomainName)
    id = Sub('CloudFront-${AWS::StackName}')
    custom_origin_config = DistributionCustomOriginConfig


@cloudformation_dataclass
class DistributionDistributionConfig:
    resource: cloudfront.distribution.DistributionConfig
    enabled = True
    http_version = 'http2'
    cache_behaviors = [DistributionCacheBehavior]
    default_cache_behavior = DistributionDefaultCacheBehavior
    origins = [DistributionOrigin]


@cloudformation_dataclass
class Distribution:
    """AWS::CloudFront::Distribution resource."""

    resource: cloudfront.Distribution
    tags = [{
        'Key': 'Name',
        'Value': ref(Name),
    }, {
        'Key': 'Description',
        'Value': ref(Name),
    }]
    distribution_config = DistributionDistributionConfig
