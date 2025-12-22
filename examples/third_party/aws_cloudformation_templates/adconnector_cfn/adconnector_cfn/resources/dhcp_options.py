"""DHCPOptions - AWS::EC2::DHCPOptions resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DHCPOptionsAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = ref(DomainDNSName)


@cloudformation_dataclass
class DHCPOptions:
    """AWS::EC2::DHCPOptions resource."""

    resource: ec2.DHCPOptions
    domain_name = ref(DomainDNSName)
    domain_name_servers = [ref(DomainDNSServers)]
    tags = [DHCPOptionsAssociationParameter]
    condition = 'DHCPOptionSetCondition'
