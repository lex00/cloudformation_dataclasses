from __future__ import annotations

"""VPC - AWS::EC2::VPC resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = ref(EnvironmentName)


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    enable_dns_support = True
    enable_dns_hostnames = True
    cidr_block = ref(VpcCIDR)
    tags = [VPCAssociationParameter]
