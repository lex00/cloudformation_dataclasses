from __future__ import annotations

"""NetworkPublicSubnet2EIP - AWS::EC2::EIP resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet2EIPAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-eip'


@cloudformation_dataclass
class NetworkPublicSubnet2EIP:
    """AWS::EC2::EIP resource."""

    resource: EIP
    domain = 'vpc'
    tags = [NetworkPublicSubnet2EIPAssociationParameter]
