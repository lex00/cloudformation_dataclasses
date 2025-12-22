"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class URLOutput:
    """The URL of the website"""

    resource: Output
    value = Join('', [
    'https://',
    get_att(ElasticLoadBalancer, "DNSName"),
])
    description = 'The URL of the website'
