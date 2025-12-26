"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Parameter,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import cloudfront
from cloudformation_dataclasses.intrinsics import Sub

from .network import CachePolicy as CachePolicy
from .network import CachePolicyCachePolicyConfig as CachePolicyCachePolicyConfig
from .network import CachePolicyCookiesConfig as CachePolicyCookiesConfig
from .network import CachePolicyHeadersConfig as CachePolicyHeadersConfig
from .network import CachePolicyParametersInCacheKeyAndForwardedToOrigin as CachePolicyParametersInCacheKeyAndForwardedToOrigin
from .network import CachePolicyQueryStringsConfig as CachePolicyQueryStringsConfig
from .network import Distribution as Distribution
from .network import DistributionCacheBehavior as DistributionCacheBehavior
from .network import DistributionCustomOriginConfig as DistributionCustomOriginConfig
from .network import DistributionDefaultCacheBehavior as DistributionDefaultCacheBehavior
from .network import DistributionDistributionConfig as DistributionDistributionConfig
from .network import DistributionOrigin as DistributionOrigin
from .params import DomainName as DomainName
from .params import Name as Name
from .params import Port as Port

__all__: list[str] = ['CachePolicy', 'CachePolicyCachePolicyConfig', 'CachePolicyCookiesConfig', 'CachePolicyHeadersConfig', 'CachePolicyParametersInCacheKeyAndForwardedToOrigin', 'CachePolicyQueryStringsConfig', 'Distribution', 'DistributionCacheBehavior', 'DistributionCustomOriginConfig', 'DistributionDefaultCacheBehavior', 'DistributionDistributionConfig', 'DistributionOrigin', 'DomainName', 'Name', 'Parameter', 'Port', 'STRING', 'Sub', 'Template', 'cloudformation_dataclass', 'cloudfront', 'get_att', 'ref', 'setup_resources']
