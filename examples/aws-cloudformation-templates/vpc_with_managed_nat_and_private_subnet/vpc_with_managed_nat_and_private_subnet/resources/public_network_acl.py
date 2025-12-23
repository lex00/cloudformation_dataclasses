"""PublicNetworkAcl - AWS::EC2::NetworkAcl resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicNetworkAclAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class PublicNetworkAclAssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Network'
    value = 'Public'


@cloudformation_dataclass
class PublicNetworkAclAssociationParameter2:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-public-nacl',
])


@cloudformation_dataclass
class PublicNetworkAcl:
    """AWS::EC2::NetworkAcl resource."""

    resource: ec2.NetworkAcl
    vpc_id = ref(VPC)
    tags = [PublicNetworkAclAssociationParameter, PublicNetworkAclAssociationParameter1, PublicNetworkAclAssociationParameter2]
