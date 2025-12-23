"""CloudFrontDistribution - AWS::CloudFront::Distribution resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CloudFrontDistributionCacheBehavior:
    resource: cloudfront.distribution.CacheBehavior
    allowed_methods = ['GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'POST', 'DELETE']
    cache_policy_id = '4135ea2d-6df8-44a3-9df3-4b5a84be39ad'
    compress = False
    origin_request_policy_id = '216adef6-5c7f-47e4-b989-5492eafa07d3'
    target_origin_id = Sub('CloudFront-${AWS::StackName}')
    viewer_protocol_policy = 'allow-all'
    path_pattern = '/proxy/*'


@cloudformation_dataclass
class CloudFrontDistributionDefaultCacheBehavior:
    resource: cloudfront.distribution.DefaultCacheBehavior
    allowed_methods = ['GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'POST', 'DELETE']
    cache_policy_id = ref(CloudFrontCachePolicy)
    origin_request_policy_id = '216adef6-5c7f-47e4-b989-5492eafa07d3'
    target_origin_id = Sub('CloudFront-${AWS::StackName}')
    viewer_protocol_policy = 'allow-all'


@cloudformation_dataclass
class CloudFrontDistributionCustomOriginConfig:
    resource: cloudfront.distribution.CustomOriginConfig
    http_port = 8080
    origin_protocol_policy = 'http-only'


@cloudformation_dataclass
class CloudFrontDistributionOrigin:
    resource: cloudfront.distribution.Origin
    domain_name = get_att(Server, "PublicDnsName")
    id = Sub('CloudFront-${AWS::StackName}')
    custom_origin_config = CloudFrontDistributionCustomOriginConfig


@cloudformation_dataclass
class CloudFrontDistributionDistributionConfig:
    resource: cloudfront.distribution.DistributionConfig
    enabled = True
    http_version = 'http2'
    cache_behaviors = [CloudFrontDistributionCacheBehavior]
    default_cache_behavior = CloudFrontDistributionDefaultCacheBehavior
    origins = [CloudFrontDistributionOrigin]


@cloudformation_dataclass
class CloudFrontDistribution:
    """AWS::CloudFront::Distribution resource."""

    resource: cloudfront.Distribution
    tags = [{
        'Key': 'Name',
        'Value': 'gitea-server',
    }, {
        'Key': 'Description',
        'Value': 'gitea-server',
    }]
    distribution_config = CloudFrontDistributionDistributionConfig
    depends_on = ["Server"]
