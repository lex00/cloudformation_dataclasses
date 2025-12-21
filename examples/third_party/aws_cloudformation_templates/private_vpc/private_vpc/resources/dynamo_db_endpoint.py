from __future__ import annotations

"""DynamoDBEndpoint - AWS::EC2::VPCEndpoint resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DynamoDBEndpointAllowStatement0:
    resource: PolicyStatement
    principal = '*'
    action = '*'
    resource_arn = '*'


@cloudformation_dataclass
class DynamoDBEndpointPolicyDocument:
    resource: PolicyDocument
    statement = [DynamoDBEndpointAllowStatement0]


@cloudformation_dataclass
class DynamoDBEndpoint:
    """AWS::EC2::VPCEndpoint resource."""

    resource: VPCEndpoint
    policy_document = DynamoDBEndpointPolicyDocument
    route_table_ids = [ref("PrivateRouteTableOne"), ref("PrivateRouteTableTwo")]
    service_name = Join('', [
    'com.amazonaws.',
    AWS_REGION,
    '.dynamodb',
])
    vpc_id: Ref[VPC] = ref()
