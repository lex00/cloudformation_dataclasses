"""Distribution - AWS::CloudFront::Distribution resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DistributionCacheBehavior:
    resource: CacheBehavior
    allowed_methods = ['GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'POST', 'DELETE']
    cache_policy_id = '4135ea2d-6df8-44a3-9df3-4b5a84be39ad'
    compress = False
    origin_request_policy_id = '216adef6-5c7f-47e4-b989-5492eafa07d3'
    target_origin_id = Sub('CloudFront-${AWS::StackName}')
    viewer_protocol_policy = 'allow-all'
    path_pattern = '/proxy/*'


@cloudformation_dataclass
class DistributionDefaultCacheBehavior:
    resource: DefaultCacheBehavior
    allowed_methods = ['GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'POST', 'DELETE']
    cache_policy_id = ref(CachePolicy)
    origin_request_policy_id = '216adef6-5c7f-47e4-b989-5492eafa07d3'
    target_origin_id = Sub('CloudFront-${AWS::StackName}')
    viewer_protocol_policy = 'allow-all'


@cloudformation_dataclass
class DistributionCustomOriginConfig:
    resource: CustomOriginConfig
    http_port = ref(Port)
    origin_protocol_policy = 'http-only'


@cloudformation_dataclass
class DistributionOrigin:
    resource: Origin
    domain_name = ref(DomainName)
    id = Sub('CloudFront-${AWS::StackName}')
    custom_origin_config = DistributionCustomOriginConfig


@cloudformation_dataclass
class DistributionDistributionConfig:
    resource: DistributionConfig
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
