"""CachePolicy - AWS::CloudFront::CachePolicy resource."""

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
