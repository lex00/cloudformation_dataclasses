"""DHCPOptions - AWS::EC2::DHCPOptions resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DHCPOptions:
    """AWS::EC2::DHCPOptions resource."""

    resource: ec2.DHCPOptions
    domain_name = ref(DomainDNSName)
    domain_name_servers = [ref(DomainDNSServers)]
    tags = [{
        'Key': 'Name',
        'Value': ref(DomainDNSName),
    }]
    condition = 'DHCPOptionSetCondition'
