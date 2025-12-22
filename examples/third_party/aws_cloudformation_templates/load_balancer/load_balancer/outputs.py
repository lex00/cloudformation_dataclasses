"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class LoadBalancerDNSOutput:
    resource: Output
    value = get_att("LoadBalancer", "DNSName")
