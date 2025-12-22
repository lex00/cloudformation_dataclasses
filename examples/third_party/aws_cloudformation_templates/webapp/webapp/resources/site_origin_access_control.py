"""SiteOriginAccessControl - AWS::CloudFront::OriginAccessControl resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteOriginAccessControlOriginAccessControlConfig:
    resource: cloudfront.origin_access_control.OriginAccessControlConfig
    name = Join('', [
    ref(AppName),
    Select(2, Split('/', AWS_STACK_ID)),
])
    origin_access_control_origin_type = 's3'
    signing_behavior = 'always'
    signing_protocol = 'sigv4'


@cloudformation_dataclass
class SiteOriginAccessControl:
    """AWS::CloudFront::OriginAccessControl resource."""

    resource: OriginAccessControl
    origin_access_control_config = SiteOriginAccessControlOriginAccessControlConfig
