"""NetworkPublicSubnet2EIP - AWS::EC2::EIP resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet2EIPAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitea-server-public-subnet-eip'


@cloudformation_dataclass
class NetworkPublicSubnet2EIP:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'
    tags = [NetworkPublicSubnet2EIPAssociationParameter]
