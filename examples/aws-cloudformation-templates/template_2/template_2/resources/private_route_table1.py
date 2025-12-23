"""PrivateRouteTable1 - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteTable1:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(VPC)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-private-route-table1'),
    }]
