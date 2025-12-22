"""RouteTable - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class RouteTableAssociationParameter:
    resource: AssociationParameter
    key = 'Application'
    value = AWS_STACK_ID


@cloudformation_dataclass
class RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [RouteTableAssociationParameter]
