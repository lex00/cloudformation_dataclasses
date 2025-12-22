"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class InstanceIdOutput:
    """Instance Id of newly created instance"""

    resource: Output
    value = ref(EC2Instance)
    description = 'Instance Id of newly created instance'


@cloudformation_dataclass
class EIP1Output:
    """Primary public IP of Eth0"""

    resource: Output
    value = Join(' ', [
    'IP address',
    ref(EIP1),
    'on subnet',
    ref(SubnetId),
])
    description = 'Primary public IP of Eth0'


@cloudformation_dataclass
class PrimaryPrivateIPAddressOutput:
    """Primary private IP address of Eth0"""

    resource: Output
    value = Join(' ', [
    'IP address',
    get_att(Eth0, "PrimaryPrivateIpAddress"),
    'on subnet',
    ref(SubnetId),
])
    description = 'Primary private IP address of Eth0'


@cloudformation_dataclass
class SecondaryPrivateIPAddressesOutput:
    """Secondary private IP address of Eth0"""

    resource: Output
    value = Join(' ', [
    'IP address',
    Select(0, get_att(Eth0, "SecondaryPrivateIpAddresses")),
    'on subnet',
    ref(SubnetId),
])
    description = 'Secondary private IP address of Eth0'
