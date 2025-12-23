"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DirectoryIDOutput:
    """ID of the MS Directory"""

    resource: Output
    value = ref(rMSDirectory)
    description = 'ID of the MS Directory'


@cloudformation_dataclass
class PrimaryDNSOutput:
    """DNS IPs of the MS Directory"""

    resource: Output
    value = Select(0, get_att(rMSDirectory, "DnsIpAddresses"))
    description = 'DNS IPs of the MS Directory'


@cloudformation_dataclass
class SecondaryDNSOutput:
    """DNS IPs of the MSDirectory"""

    resource: Output
    value = Select(1, get_att(rMSDirectory, "DnsIpAddresses"))
    description = 'DNS IPs of the MSDirectory'


@cloudformation_dataclass
class DirectoryAliasOutput:
    """URL for the alias"""

    resource: Output
    value = get_att(rMSDirectory, "Alias")
    description = 'URL for the alias'
    condition = 'cAlias'
