"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class FirehoseLogGroup:
    """AWS::Logs::LogGroup resource."""

    resource: logs.LogGroup
    log_group_name = Join('', [
    '/aws/kinesisfirehose/',
    ref(LogGroupName),
])
    retention_in_days = ref(CloudWatchLogGroupRetention)
    kms_key_id = If("CloudWatchLogsKMSKeyCondition", ref(CloudWatchLogsKMSKey), AWS_NO_VALUE)


@cloudformation_dataclass
class FirehoseLogStream:
    """AWS::Logs::LogStream resource."""

    resource: logs.LogStream
    log_group_name = ref(FirehoseLogGroup)
    log_stream_name = ref(LogStreamName)


@cloudformation_dataclass
class DeliveryRoleAllowStatement0:
    resource: PolicyStatement
    sid = ''
    principal = {
        'Service': 'firehose.amazonaws.com',
    }
    action = 'sts:AssumeRole'
    condition = {
        STRING_EQUALS: {
            'sts:ExternalId': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class DeliveryRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DeliveryRoleAllowStatement0]


@cloudformation_dataclass
class DeliveryRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = DeliveryRoleAssumeRolePolicyDocument
    path = '/'
    policies = [{
        'PolicyName': 'firehose_delivery_policy',
        'PolicyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Effect': 'Allow',
                    'Action': [
                        's3:AbortMultipartUpload',
                        's3:GetBucketLocation',
                        's3:GetObject',
                        's3:ListBucket',
                        's3:ListBucketMultipartUploads',
                        's3:PutObject',
                    ],
                    'Resource': [
                        Join('', [
    'arn:aws:s3:::',
    ref(DestinationBucketName),
]),
                        Join('', [
    'arn:aws:s3:::',
    ref(DestinationBucketName),
    '/*',
]),
                    ],
                },
                {
                    'Effect': 'Allow',
                    'Action': ['logs:PutLogEvents'],
                    'Resource': Join('', [
    Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/kinesisfirehose/'),
    ref(LogGroupName),
    ':*',
]),
                },
            ],
        },
    }]


@cloudformation_dataclass
class DeliveryStream:
    """AWS::KinesisFirehose::DeliveryStream resource."""

    resource: kinesisfirehose.DeliveryStream
    delivery_stream_name = ref(DeliveryStreamName)
    delivery_stream_type = 'DirectPut'
    delivery_stream_encryption_configuration_input = {
        'KeyType': 'AWS_OWNED_CMK',
    }
    extended_s3_destination_configuration = {
        'CloudWatchLoggingOptions': {
            'Enabled': True,
            'LogGroupName': ref(FirehoseLogGroup),
            'LogStreamName': ref(FirehoseLogStream),
        },
        'RoleARN': get_att(DeliveryRole, "Arn"),
        'BucketARN': Join('', [
    'arn:aws:s3:::',
    ref(DestinationBucketName),
]),
        'ErrorOutputPrefix': 'errors/',
        'ProcessingConfiguration': {
            'Enabled': True,
            'Processors': [{
                'Type': 'AppendDelimiterToRecord',
                'Parameters': [{
                    'ParameterName': 'Delimiter',
                    'ParameterValue': '\\n',
                }],
            }],
        },
    }
