"""VPC - AWS::EC2::VPC resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    cidr_block = ref(VpcCIDR)
    enable_dns_support = True
    enable_dns_hostnames = True
