"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class EC2IPAddressOutput:
    """EC2 Instance Public IP Address"""

    resource: Output
    value = get_att("GreengrassInstance", "PublicIp")
    description = 'EC2 Instance Public IP Address'
