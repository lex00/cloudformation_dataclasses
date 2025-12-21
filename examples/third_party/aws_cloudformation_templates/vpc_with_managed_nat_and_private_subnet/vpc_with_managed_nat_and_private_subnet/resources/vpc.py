from __future__ import annotations

"""VPC - AWS::EC2::VPC resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCAssociationParameter:
    resource: AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class VPCAssociationParameter1:
    resource: AssociationParameter
    key = 'Network'
    value = 'Public'


@cloudformation_dataclass
class VPCAssociationParameter2:
    resource: AssociationParameter
    key = 'Name'
    value = ref(VPCName)


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    enable_dns_support = 'true'
    enable_dns_hostnames = 'true'
    cidr_block = FindInMap("SubnetConfig", 'VPC', 'CIDR')
    tags = [VPCAssociationParameter, VPCAssociationParameter1, VPCAssociationParameter2]
