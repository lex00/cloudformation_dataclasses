"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class URLOutput:
    resource: Output
    value = Sub('https://${CloudFrontDistribution.DomainName}')
