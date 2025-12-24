"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class URLOutput:
    """URL of the website"""

    resource: Output
    value = Join('', [
    'http://',
    get_att(ElasticLoadBalancer, "DNSName"),
])
    description = 'URL of the website'
