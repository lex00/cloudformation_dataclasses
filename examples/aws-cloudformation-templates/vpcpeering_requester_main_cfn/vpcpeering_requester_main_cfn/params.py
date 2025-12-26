"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class NumberOfRouteTables:
    """Number of Route Table IDs to update. This must match your items in the comma-separated list of RouteTableIds parameter."""

    resource: Parameter
    type = STRING
    description = 'Number of Route Table IDs to update. This must match your items in the comma-separated list of RouteTableIds parameter.'
    allowed_values = [
    1,
    2,
    3,
    4,
    5,
    6,
]


@cloudformation_dataclass
class NumberOfSecurityGroups:
    """Number of Security Group IDs. This must match your selections in the list of SecurityGroupIds parameter."""

    resource: Parameter
    type = STRING
    description = 'Number of Security Group IDs. This must match your selections in the list of SecurityGroupIds parameter.'
    allowed_values = [
    1,
    2,
    3,
    4,
    5,
    6,
]


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
class PeerVPCCIDR:
    """CIDR of the VPC Peer"""

    resource: Parameter
    type = STRING
    description = 'CIDR of the VPC Peer'
    allowed_pattern = '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\/(1[6-9]|2[0-8]))$'
    constraint_description = 'CIDR block parameter must be in the form x.x.x.x/16-28'


@cloudformation_dataclass
class PeerVPCID:
    """ID of the VPC with which you are creating the VPC peering connection"""

    resource: Parameter
    type = STRING
    description = 'ID of the VPC with which you are creating the VPC peering connection'
    allowed_pattern = '^vpc-[0-9a-f]{17}$'
    constraint_description = 'Must have a prefix of "vpc-". Followed by 17 characters (numbers, letters "a-f")'


@cloudformation_dataclass
class RouteTableIds:
    """Route Table IDs that will be updated to allow communications via the VPC peering connection. Note, the logical order is preserved."""

    resource: Parameter
    type = STRING
    description = 'Route Table IDs that will be updated to allow communications via the VPC peering connection. Note, the logical order is preserved.'
    allowed_pattern = '^(rtb-[0-9a-f]{17})$|^((rtb-[0-9a-f]{17}(,|, ))*rtb-[0-9a-f]{17})$'
    constraint_description = 'Must have a prefix of "rtb-". Followed by 17 characters (numbers, letters "a-f"). Additional route tables can be provided, separated by a "comma".'


@cloudformation_dataclass
class SecurityGroupIds:
    """Security Group IDs that will be updated to allow communications via the VPC peering connection. Note, the logical order is preserved."""

    resource: Parameter
    type = ParameterType.LIST_AWS_EC2_SECURITY_GROUP_ID
    description = 'Security Group IDs that will be updated to allow communications via the VPC peering connection. Note, the logical order is preserved.'


@cloudformation_dataclass
class TemplatesS3BucketName:
    """Templates S3 bucket name for the CloudFormation templates. S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-)."""

    resource: Parameter
    type = STRING
    description = 'Templates S3 bucket name for the CloudFormation templates. S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'
    allowed_pattern = '^(?=^.{3,63}$)(?!.*[.-]{2})(?!.*[--]{2})(?!^(?:(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\\.(?!$)|$)){4}$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)'
    constraint_description = 'Templates S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'


@cloudformation_dataclass
class TemplatesS3BucketRegion:
    """AWS Region where the S3 bucket (TemplatesS3BucketName) is hosted."""

    resource: Parameter
    type = STRING
    description = 'AWS Region where the S3 bucket (TemplatesS3BucketName) is hosted.'


@cloudformation_dataclass
class TemplatesS3KeyPrefix:
    """S3 key prefix for the AWS CloudFormation templates. Key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/)."""

    resource: Parameter
    type = STRING
    description = 'S3 key prefix for the AWS CloudFormation templates. Key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/).'
    allowed_pattern = '^[0-9a-zA-Z-/]*$'
    constraint_description = 'Templates key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/).'


@cloudformation_dataclass
class VPCID:
    """ID of the VPC"""

    resource: Parameter
    type = ParameterType.AWS_EC2_VPC_ID
    description = 'ID of the VPC'
