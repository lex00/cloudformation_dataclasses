"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DestinationBucketName:
    """Name of an existing Amazon S3 bucket"""

    resource: Parameter
    type = STRING
    description = 'Name of an existing Amazon S3 bucket'


@cloudformation_dataclass
class LogStreamName:
    """Name of the Amazon CloudWatch log stream that will be created."""

    resource: Parameter
    type = STRING
    description = 'Name of the Amazon CloudWatch log stream that will be created.'


@cloudformation_dataclass
class LogGroupName:
    """Name of the Amazon CloudWatch log group that will be created."""

    resource: Parameter
    type = STRING
    description = 'Name of the Amazon CloudWatch log group that will be created.'


@cloudformation_dataclass
class CloudWatchLogsKMSKey:
    """(Optional) KMS Key ARN to use for encrypting the delivery stream destination error log data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys."""

    resource: Parameter
    type = STRING
    description = '(Optional) KMS Key ARN to use for encrypting the delivery stream destination error log data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys.'
    allowed_pattern = '^$|^arn:(aws[a-zA-Z-]*){1}:kms:[a-z0-9-]+:\\d{12}:key\\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'
    constraint_description = 'Key ARN example:  arn:aws:kms:us-east-2:012345678901:key/1234abcd-12ab-34cd-56ef-1234567890ab'


@cloudformation_dataclass
class CloudWatchLogGroupRetention:
    """Define the number of days to retain destination error logs."""

    resource: Parameter
    type = STRING
    description = 'Define the number of days to retain destination error logs.'
    default = 3
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
class DeliveryStreamName:
    """Name of Amazon Data Firehose delivery stream"""

    resource: Parameter
    type = STRING
    description = 'Name of Amazon Data Firehose delivery stream'
    default = 'my-delivery-stream'


@cloudformation_dataclass
class CloudWatchLogsKMSKeyConditionCondition:
    resource: Condition
    expression = Not(Equals(ref(CloudWatchLogsKMSKey), ''))
