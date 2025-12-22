from __future__ import annotations

"""VPC - AWS::EC2::VPC resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-vpc')


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    cidr_block = ref(VPCCidrBlock)
    enable_dns_support = True
    enable_dns_hostnames = True
    instance_tenancy = 'default'
    tags = [VPCAssociationParameter]
