"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class PeerName:
    """Name of the VPC Peer"""

    resource: Parameter
    type = STRING
    description = 'Name of the VPC Peer'
    max_length = 255


@cloudformation_dataclass
class PeerOwnerId:
    """AWS account ID of the owner of the accepter VPC"""

    resource: Parameter
    type = STRING
    description = 'AWS account ID of the owner of the accepter VPC'
    allowed_pattern = '^\\d{12}$'
    constraint_description = 'Must be 12 digits.'


@cloudformation_dataclass
class PeerRoleARN:
    """ARN of the VPC peer role for the peering connection in another AWS account. Required when you are peering a VPC in a different AWS account."""

    resource: Parameter
    type = STRING
    description = 'ARN of the VPC peer role for the peering connection in another AWS account. Required when you are peering a VPC in a different AWS account.'
    allowed_pattern = '^arn:(aws[a-zA-Z-]*)?:iam::\\d{12}:role\\/([\\w+=,.@-]*\\/)*[\\w+=,.@-]+'


@cloudformation_dataclass
class PeerVPCID:
    """ID of the VPC with which you are creating the VPC peering connection"""

    resource: Parameter
    type = STRING
    description = 'ID of the VPC with which you are creating the VPC peering connection'
    allowed_pattern = '^vpc-[0-9a-f]{17}$'
    constraint_description = 'Must have a prefix of "vpc-". Followed by 17 characters (numbers, letters "a-f")'


@cloudformation_dataclass
class VPCID:
    """ID of the VPC"""

    resource: Parameter
    type = ParameterType.AWS_EC2_VPC_ID
    description = 'ID of the VPC'


@cloudformation_dataclass
class PeerRoleConditionCondition:
    resource: TemplateCondition
    logical_id = 'PeerRoleCondition'
    expression = Not(Equals(ref(PeerRoleARN), ''))
