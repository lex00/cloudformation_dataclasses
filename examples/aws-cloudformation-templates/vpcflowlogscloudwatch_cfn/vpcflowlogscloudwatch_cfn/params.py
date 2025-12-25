"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class VPCFlowLogsCloudWatchKMSKey:
    """(Optional) KMS Key ARN to use for encrypting the VPC flow logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys."""

    resource: Parameter
    type = STRING
    description = '(Optional) KMS Key ARN to use for encrypting the VPC flow logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys.'
    allowed_pattern = '^$|^arn:(aws[a-zA-Z-]*)?:kms:[a-z0-9-]+:\\d{12}:key\\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'
    constraint_description = 'Key ARN example:  arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'


@cloudformation_dataclass
class VPCFlowLogsLogFormat:
    """The fields to include in the flow log record, in the order in which they should appear. Specify the fields using the ${field-id} format, separated by spaces. Using the Default Format as the default value."""

    resource: Parameter
    type = STRING
    description = 'The fields to include in the flow log record, in the order in which they should appear. Specify the fields using the ${field-id} format, separated by spaces. Using the Default Format as the default value.'
    default = '${version} ${account-id} ${interface-id} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${protocol} ${packets} ${bytes} ${start} ${end} ${action} ${log-status}'
    allowed_pattern = '^(\\$\\{[a-z-]+\\})$|^((\\$\\{[a-z-]+\\} )*\\$\\{[a-z-]+\\})$'


@cloudformation_dataclass
class VPCFlowLogsLogGroupRetention:
    """Number of days to retain the VPC Flow Logs in CloudWatch"""

    resource: Parameter
    type = STRING
    description = 'Number of days to retain the VPC Flow Logs in CloudWatch'
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
class VPCFlowLogsMaxAggregationInterval:
    """The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. You can specify 60 seconds (1 minute) or 600 seconds (10 minutes)."""

    resource: Parameter
    type = STRING
    description = 'The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).'
    default = 600
    allowed_values = [
    60,
    600,
]


@cloudformation_dataclass
class VPCFlowLogsTrafficType:
    """The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic."""

    resource: Parameter
    type = STRING
    description = 'The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.'
    default = 'REJECT'
    allowed_values = [
    'ACCEPT',
    'ALL',
    'REJECT',
]


@cloudformation_dataclass
class VPCID:
    """ID of the VPC (e.g., vpc-0343606e)"""

    resource: Parameter
    type = ParameterType.AWS_EC2_VPC_ID
    description = 'ID of the VPC (e.g., vpc-0343606e)'


@cloudformation_dataclass
class VPCFlowLogsCloudWatchKMSKeyConditionCondition:
    resource: TemplateCondition
    logical_id = 'VPCFlowLogsCloudWatchKMSKeyCondition'
    expression = Not(Equals(ref(VPCFlowLogsCloudWatchKMSKey), ''))
