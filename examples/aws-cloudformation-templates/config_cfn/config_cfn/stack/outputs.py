"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceIdOutput:
    """InstanceId of the newly created EC2 instance"""

    resource: Output
    value = ref(EC2Instance)
    description = 'InstanceId of the newly created EC2 instance'


@cloudformation_dataclass
class AZOutput:
    """Availability Zone of the newly created EC2 instance"""

    resource: Output
    value = get_att(EC2Instance, "AvailabilityZone")
    description = 'Availability Zone of the newly created EC2 instance'


@cloudformation_dataclass
class PublicDNSOutput:
    """Public DNSName of the newly created EC2 instance"""

    resource: Output
    value = get_att(EC2Instance, "PublicDnsName")
    description = 'Public DNSName of the newly created EC2 instance'


@cloudformation_dataclass
class PublicIPOutput:
    """Public IP address of the newly created EC2 instance"""

    resource: Output
    value = get_att(EC2Instance, "PublicIp")
    description = 'Public IP address of the newly created EC2 instance'
