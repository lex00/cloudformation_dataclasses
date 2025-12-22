"""InternetGateway - AWS::EC2::InternetGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InternetGatewayAssociationParameter:
    resource: AssociationParameter
    key = 'Application'
    value = AWS_STACK_ID


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway
    tags = [InternetGatewayAssociationParameter]
