"""OriginAccessControl - AWS::CloudFront::OriginAccessControl resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class OriginAccessControlOriginAccessControlConfig:
    resource: cloudfront.origin_access_control.OriginAccessControlConfig
    name = Join('', [
    'rain-build-website-',
    Select(2, Split('/', AWS_STACK_ID)),
])
    origin_access_control_origin_type = 's3'
    signing_behavior = 'always'
    signing_protocol = 'sigv4'


@cloudformation_dataclass
class OriginAccessControl:
    """AWS::CloudFront::OriginAccessControl resource."""

    resource: cloudfront.OriginAccessControl
    origin_access_control_config = OriginAccessControlOriginAccessControlConfig
