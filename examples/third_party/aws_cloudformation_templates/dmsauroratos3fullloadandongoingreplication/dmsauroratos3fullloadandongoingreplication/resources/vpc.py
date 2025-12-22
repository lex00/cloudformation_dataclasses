from __future__ import annotations

"""VPC - AWS::EC2::VPC resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCAssociationParameter:
    resource: AssociationParameter
    key = 'Application'
    value = AWS_STACK_ID


@cloudformation_dataclass
class VPCAssociationParameter1:
    resource: AssociationParameter
    key = 'Name'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    cidr_block = '10.0.0.0/24'
    enable_dns_support = 'true'
    enable_dns_hostnames = 'true'
    tags = [VPCAssociationParameter, VPCAssociationParameter1]
