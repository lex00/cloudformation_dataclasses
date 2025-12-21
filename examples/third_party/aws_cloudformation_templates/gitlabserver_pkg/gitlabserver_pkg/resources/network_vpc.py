from __future__ import annotations

"""NetworkVPC - AWS::EC2::VPC resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkVPCAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'gitlab-server'


@cloudformation_dataclass
class NetworkVPC:
    """AWS::EC2::VPC resource."""

    resource: VPC
    cidr_block = '10.0.0.0/16'
    enable_dns_hostnames = True
    enable_dns_support = True
    instance_tenancy = 'default'
    tags = [NetworkVPCAssociationParameter]
