"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class InstanceIdOutput:
    """InstanceId of the newly created EC2 instance"""

    resource: Output
    value = ref(EC2Instance)
    description = 'InstanceId of the newly created EC2 instance'


@cloudformation_dataclass
class InstanceIPAddressOutput:
    """IP address of the newly created EC2 instance"""

    resource: Output
    value = ref(IPAddress)
    description = 'IP address of the newly created EC2 instance'
