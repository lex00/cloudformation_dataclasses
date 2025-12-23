"""NetworkPublicSubnet1EIP - AWS::EC2::EIP resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet1EIPAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-1-eip'


@cloudformation_dataclass
class NetworkPublicSubnet1EIP:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'
    tags = [NetworkPublicSubnet1EIPAssociationParameter]
