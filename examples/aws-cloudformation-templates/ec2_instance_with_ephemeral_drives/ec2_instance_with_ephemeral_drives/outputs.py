"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class InstanceOutput:
    """DNS Name of the newly created EC2 instance"""

    resource: Output
    value = get_att(EC2Instance, "PublicDnsName")
    description = 'DNS Name of the newly created EC2 instance'
