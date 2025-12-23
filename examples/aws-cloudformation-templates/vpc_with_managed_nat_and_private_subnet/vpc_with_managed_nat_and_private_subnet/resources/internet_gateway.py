"""InternetGateway - AWS::EC2::InternetGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InternetGatewayAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class InternetGatewayAssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Network'
    value = 'Public'


@cloudformation_dataclass
class InternetGatewayAssociationParameter2:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-IGW',
])


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway
    tags = [InternetGatewayAssociationParameter, InternetGatewayAssociationParameter1, InternetGatewayAssociationParameter2]
