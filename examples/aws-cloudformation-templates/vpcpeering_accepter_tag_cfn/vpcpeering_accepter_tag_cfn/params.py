"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


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
    """Lambda logging level"""

    resource: Parameter
    type = STRING
    description = 'Lambda logging level'
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
class PeerName:
    """Name of the VPC Peer"""

    resource: Parameter
    type = STRING
    description = 'Name of the VPC Peer'
    max_length = 255


@cloudformation_dataclass
class VPCPeeringConnectionId:
    """ID of the VPC Peering Connection"""

    resource: Parameter
    type = STRING
    description = 'ID of the VPC Peering Connection'
    allowed_pattern = '^pcx-[0-9a-f]{17}$'
    constraint_description = 'Must have a prefix of "pcx-". Followed by 17 characters (numbers, letters "a-f")'


@cloudformation_dataclass
class LambdaLogsCloudWatchKMSKeyConditionCondition:
    resource: TemplateCondition
    logical_id = 'LambdaLogsCloudWatchKMSKeyCondition'
    expression = Not(Equals(ref(LambdaLogsCloudWatchKMSKey), ''))
