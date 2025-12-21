from __future__ import annotations

"""S3Endpoint - AWS::EC2::VPCEndpoint resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class S3EndpointAllowStatement0:
    resource: PolicyStatement
    principal = '*'
    action = ['s3:PutObject']
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::cloudformation-waitcondition-${AWS::Region}/*')]


@cloudformation_dataclass
class S3EndpointPolicyDocument:
    resource: PolicyDocument
    statement = [S3EndpointAllowStatement0]


@cloudformation_dataclass
class S3Endpoint:
    """AWS::EC2::VPCEndpoint resource."""

    resource: VPCEndpoint
    vpc_id: Ref[VPC] = ref()
    service_name = Sub('com.amazonaws.${AWS::Region}.s3')
    vpc_endpoint_type = 'Gateway'
    policy_document = S3EndpointPolicyDocument
    route_table_ids = [ref("PrivateRouteTable1"), ref("PrivateRouteTable2")]
