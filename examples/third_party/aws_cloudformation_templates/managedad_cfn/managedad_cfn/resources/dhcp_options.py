from __future__ import annotations

"""DHCPOptions - AWS::EC2::DHCPOptions resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DHCPOptionsAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = ref(AWSManagedADDomainDNSName)


@cloudformation_dataclass
class DHCPOptions:
    """AWS::EC2::DHCPOptions resource."""

    resource: ec2.DHCPOptions
    domain_name = ref(AWSManagedADDomainDNSName)
    domain_name_servers = get_att(AWSManagedAD, "DnsIpAddresses")
    tags = [DHCPOptionsAssociationParameter]
    condition = 'DHCPOptionSetCondition'
