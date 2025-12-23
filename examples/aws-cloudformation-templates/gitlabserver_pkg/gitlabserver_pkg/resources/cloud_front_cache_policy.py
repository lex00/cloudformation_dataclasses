"""CloudFrontCachePolicy - AWS::CloudFront::CachePolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CloudFrontCachePolicyCookiesConfig:
    resource: cloudfront.cache_policy.CookiesConfig
    cookie_behavior = 'all'


@cloudformation_dataclass
class CloudFrontCachePolicyHeadersConfig:
    resource: cloudfront.cache_policy.HeadersConfig
    header_behavior = 'whitelist'
    headers = ['Accept-Charset', 'Authorization', 'Origin', 'Accept', 'Referer', 'Host', 'Accept-Language', 'Accept-Encoding', 'Accept-Datetime']


@cloudformation_dataclass
class CloudFrontCachePolicyQueryStringsConfig:
    resource: cloudfront.cache_policy.QueryStringsConfig
    query_string_behavior = 'all'


@cloudformation_dataclass
class CloudFrontCachePolicyParametersInCacheKeyAndForwardedToOrigin:
    resource: cloudfront.cache_policy.ParametersInCacheKeyAndForwardedToOrigin
    cookies_config = CloudFrontCachePolicyCookiesConfig
    enable_accept_encoding_gzip = False
    headers_config = CloudFrontCachePolicyHeadersConfig
    query_strings_config = CloudFrontCachePolicyQueryStringsConfig


@cloudformation_dataclass
class CloudFrontCachePolicyCachePolicyConfig:
    resource: cloudfront.cache_policy.CachePolicyConfig
    default_ttl = 86400
    max_ttl = 31536000
    min_ttl = 1
    name = 'gitlab-server'
    parameters_in_cache_key_and_forwarded_to_origin = CloudFrontCachePolicyParametersInCacheKeyAndForwardedToOrigin


@cloudformation_dataclass
class CloudFrontCachePolicy:
    """AWS::CloudFront::CachePolicy resource."""

    resource: cloudfront.CachePolicy
    cache_policy_config = CloudFrontCachePolicyCachePolicyConfig
