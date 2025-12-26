"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class DirectoryIDOutput:
    """ID of the SimpleAD"""

    resource: Output
    value = ref(SimpleAD)
    description = 'ID of the SimpleAD'


@cloudformation_dataclass
class PrimaryDNSOutput:
    """DNS IPs of the SimpleAD"""

    resource: Output
    value = Select(0, get_att(SimpleAD, "DnsIpAddresses"))
    description = 'DNS IPs of the SimpleAD'


@cloudformation_dataclass
class SecondaryDNSOutput:
    """DNS IPs of the SimpleAD"""

    resource: Output
    value = Select(1, get_att(SimpleAD, "DnsIpAddresses"))
    description = 'DNS IPs of the SimpleAD'


@cloudformation_dataclass
class DirectoryAliasOutput:
    """URL for the alias"""

    resource: Output
    value = get_att(SimpleAD, "Alias")
    description = 'URL for the alias'
    condition = 'Alias'
