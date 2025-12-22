from __future__ import annotations

"""CloudFrontCachePolicy - AWS::CloudFront::CachePolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CloudFrontCachePolicyCookiesConfig:
    resource: CookiesConfig
    cookie_behavior = 'all'


@cloudformation_dataclass
class CloudFrontCachePolicyHeadersConfig:
    resource: HeadersConfig
    header_behavior = 'whitelist'
    headers = ['Accept-Charset', 'Authorization', 'Origin', 'Accept', 'Referer', 'Host', 'Accept-Language', 'Accept-Encoding', 'Accept-Datetime']


@cloudformation_dataclass
class CloudFrontCachePolicyQueryStringsConfig:
    resource: QueryStringsConfig
    query_string_behavior = 'all'


@cloudformation_dataclass
class CloudFrontCachePolicyParametersInCacheKeyAndForwardedToOrigin:
    resource: ParametersInCacheKeyAndForwardedToOrigin
    cookies_config = CloudFrontCachePolicyCookiesConfig
    enable_accept_encoding_gzip = False
    headers_config = CloudFrontCachePolicyHeadersConfig
    query_strings_config = CloudFrontCachePolicyQueryStringsConfig


@cloudformation_dataclass
class CloudFrontCachePolicyCachePolicyConfig:
    resource: CachePolicyConfig
    default_ttl = 86400
    max_ttl = 31536000
    min_ttl = 1
    name = 'vscode-server'
    parameters_in_cache_key_and_forwarded_to_origin = CloudFrontCachePolicyParametersInCacheKeyAndForwardedToOrigin


@cloudformation_dataclass
class CloudFrontCachePolicy:
    """AWS::CloudFront::CachePolicy resource."""

    resource: CachePolicy
    cache_policy_config = CloudFrontCachePolicyCachePolicyConfig
