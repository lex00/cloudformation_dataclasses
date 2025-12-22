from __future__ import annotations

"""PublicSubnetNetworkAclAssociation0 - AWS::EC2::SubnetNetworkAclAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnetNetworkAclAssociation0:
    """AWS::EC2::SubnetNetworkAclAssociation resource."""

    resource: SubnetNetworkAclAssociation
    subnet_id: Ref[PublicSubnet0] = ref()
    network_acl_id: Ref[PublicNetworkAcl] = ref()
