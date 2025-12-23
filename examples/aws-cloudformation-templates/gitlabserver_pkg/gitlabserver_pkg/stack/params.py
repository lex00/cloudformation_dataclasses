"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LambdaFunctionName:
    """Lambda Function Name for Custom Resource"""

    resource: Parameter
    type = STRING
    description = 'Lambda Function Name for Custom Resource'
    default = 'CR-TagVpcPeeringConnections'
    allowed_pattern = '^[\\w-]{1,64}$'
    constraint_description = 'Max 64 alphanumeric characters. Also special characters supported [_, -]'


@cloudformation_dataclass
class LambdaLogLevel:
    resource: Parameter
    type = STRING
    default = 'INFO'
    allowed_values = [
    'INFO',
    'DEBUG',
]


@cloudformation_dataclass
class LambdaLogsCloudWatchKMSKey:
    """(Optional) KMS Key ARN to use for encrypting the Lambda logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys."""

    resource: Parameter
    type = STRING
    description = '(Optional) KMS Key ARN to use for encrypting the Lambda logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys.'
    default = ''
    allowed_pattern = '^$|^arn:(aws[a-zA-Z-]*)?:kms:[a-z0-9-]+:\\d{12}:key\\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'
    constraint_description = 'Key ARN example:  arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'


@cloudformation_dataclass
class LambdaLogsLogGroupRetention:
    """Specifies the number of days you want to retain Lambda log events in the CloudWatch Logs"""

    resource: Parameter
    type = STRING
    description = 'Specifies the number of days you want to retain Lambda log events in the CloudWatch Logs'
    default = 14
    allowed_values = [
    1,
    3,
    5,
    7,
    14,
    30,
    60,
    90,
    120,
    150,
    180,
    365,
    400,
    545,
    731,
    1827,
    3653,
]


@cloudformation_dataclass
class LambdaRoleName:
    """Lambda Execution Role Name for the Custom Resource to Tag VPC Peering Connections"""

    resource: Parameter
    type = STRING
    description = 'Lambda Execution Role Name for the Custom Resource to Tag VPC Peering Connections'
    default = 'Lambda-Role-CR-TagVpcPeeringConnections'
    allowed_pattern = '^[\\w+=,.@-]{1,64}$'
    constraint_description = 'Max 64 alphanumeric characters. Also special characters supported [+, =, ., @, -]'


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
class PeerVPCCIDR:
    """CIDR of the VPC Peer"""

    resource: Parameter
    type = STRING
    description = 'CIDR of the VPC Peer'
    allowed_pattern = '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\/(1[6-9]|2[0-8]))$'
    constraint_description = 'CIDR block parameter must be in the form x.x.x.x/16-28'


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
class VPCPeeringConnectionId:
    """ID of the VPC Peering Connection"""

    resource: Parameter
    type = STRING
    description = 'ID of the VPC Peering Connection'
    allowed_pattern = '^pcx-[0-9a-f]{17}$'
    constraint_description = 'Must have a prefix of "pcx-". Followed by 17 characters (numbers, letters "a-f")'
