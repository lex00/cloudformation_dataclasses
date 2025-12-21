from __future__ import annotations

"""PublicSubnetNetworkAclAssociation1 - AWS::EC2::SubnetNetworkAclAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnetNetworkAclAssociation1:
    """AWS::EC2::SubnetNetworkAclAssociation resource."""

    resource: SubnetNetworkAclAssociation
    subnet_id: Ref[PublicSubnet1] = ref()
    network_acl_id: Ref[PublicNetworkAcl] = ref()
