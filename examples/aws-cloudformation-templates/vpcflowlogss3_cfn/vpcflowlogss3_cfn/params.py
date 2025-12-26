"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class S3AccessLogsBucketName:
    """(Optional) S3 Server Access Logs bucket name for where Amazon S3 should store server access log files. S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-). If empty, a new S3 bucket will be created as a destination for S3 server access logs, it will follow the format, aws-s3-access-logs-<account>-<region>"""

    resource: Parameter
    type = STRING
    description = '(Optional) S3 Server Access Logs bucket name for where Amazon S3 should store server access log files. S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-). If empty, a new S3 bucket will be created as a destination for S3 server access logs, it will follow the format, aws-s3-access-logs-<account>-<region>'
    allowed_pattern = '^$|^(?=^.{3,63}$)(?!.*[.-]{2})(?!.*[--]{2})(?!^(?:(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\\.(?!$)|$)){4}$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)'
    constraint_description = 'S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'


@cloudformation_dataclass
class VPCFlowLogsBucketKeyEnabled:
    """Set to true to have Amazon S3 use an S3 Bucket Key with server-side encryption using KMS (SSE-KMS). If false, S3 Bucket Key is not enabled. Note, will only be set if KMS Key parameter, 'VPCFlowLogsBucketKMSKey', was provided."""

    resource: Parameter
    type = STRING
    description = "Set to true to have Amazon S3 use an S3 Bucket Key with server-side encryption using KMS (SSE-KMS). If false, S3 Bucket Key is not enabled. Note, will only be set if KMS Key parameter, 'VPCFlowLogsBucketKMSKey', was provided."
    default = False
    allowed_values = [
    True,
    False,
]


@cloudformation_dataclass
class VPCFlowLogsBucketKMSKey:
    """(Optional) KMS Key ID or ARN to use for the default encryption. If empty, server-side encryption with Amazon S3-managed encryption keys (SSE-S3) will be used. Note, will only be set if S3 Bucket parameter, 'VPCFlowLogsBucketName', was not provided, thus a new S3 bucket is being created."""

    resource: Parameter
    type = STRING
    description = "(Optional) KMS Key ID or ARN to use for the default encryption. If empty, server-side encryption with Amazon S3-managed encryption keys (SSE-S3) will be used. Note, will only be set if S3 Bucket parameter, 'VPCFlowLogsBucketName', was not provided, thus a new S3 bucket is being created."
    allowed_pattern = '^$|^[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}$|^arn:(aws[a-zA-Z-]*)?:kms:[a-z0-9-]+:\\d{12}:key\\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'
    constraint_description = 'Key ID example: 1234abcd-12ab-34cd-56ef-1234567890ab  Key ARN example:  arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'


@cloudformation_dataclass
class VPCFlowLogsBucketName:
    """(Optional) S3 bucket name where VPC Flow Log data can be published. S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-). If empty, a new S3 bucket will be created for VPC Flow Log data to be published."""

    resource: Parameter
    type = STRING
    description = '(Optional) S3 bucket name where VPC Flow Log data can be published. S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-). If empty, a new S3 bucket will be created for VPC Flow Log data to be published.'
    allowed_pattern = '^$|^(?=^.{3,63}$)(?!.*[.-]{2})(?!.*[--]{2})(?!^(?:(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\\.(?!$)|$)){4}$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)'
    constraint_description = 'S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'


@cloudformation_dataclass
class VPCFlowLogsLogFormat:
    """The fields to include in the flow log record, in the order in which they should appear. Specify the fields using the ${field-id} format, separated by spaces. Using the Default Format as the default value."""

    resource: Parameter
    type = STRING
    description = 'The fields to include in the flow log record, in the order in which they should appear. Specify the fields using the ${field-id} format, separated by spaces. Using the Default Format as the default value.'
    default = '${version} ${account-id} ${interface-id} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${protocol} ${packets} ${bytes} ${start} ${end} ${action} ${log-status}'
    allowed_pattern = '^(\\$\\{[a-z-]+\\})$|^((\\$\\{[a-z-]+\\} )*\\$\\{[a-z-]+\\})$'


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
class S3AccessLogsConditionCondition:
    resource: TemplateCondition
    logical_id = 'S3AccessLogsCondition'
    expression = Not(Equals(ref(S3AccessLogsBucketName), ''))


@cloudformation_dataclass
class VPCFlowLogsNewBucketConditionCondition:
    resource: TemplateCondition
    logical_id = 'VPCFlowLogsNewBucketCondition'
    expression = Equals(ref(VPCFlowLogsBucketName), '')


@cloudformation_dataclass
class VPCFlowLogsBucketKMSKeyConditionCondition:
    resource: TemplateCondition
    logical_id = 'VPCFlowLogsBucketKMSKeyCondition'
    expression = Not(Equals(ref(VPCFlowLogsBucketKMSKey), ''))
