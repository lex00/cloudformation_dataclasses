"""PublicSubnetNetworkAclAssociation1 - AWS::EC2::SubnetNetworkAclAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnetNetworkAclAssociation1:
    """AWS::EC2::SubnetNetworkAclAssociation resource."""

    resource: ec2.SubnetNetworkAclAssociation
    subnet_id = ref(PublicSubnet1)
    network_acl_id = ref(PublicNetworkAcl)
