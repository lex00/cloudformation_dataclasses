"""LoggingBucketPolicy - AWS::S3::BucketPolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoggingBucketPolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'LoggingBucketPermissions'
    principal = {
        'AWS': Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:root'),
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${LoggingBucket}/AWSLogs/${AWS::AccountId}/*')]


@cloudformation_dataclass
class LoggingBucketPolicyDenyStatement1:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${LoggingBucket}/AWSLogs/${AWS::AccountId}/*')]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class LoggingBucketPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [LoggingBucketPolicyAllowStatement0, LoggingBucketPolicyDenyStatement1]


@cloudformation_dataclass
class LoggingBucketPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: BucketPolicy
    bucket = ref(LoggingBucket)
    policy_document = LoggingBucketPolicyPolicyDocument
