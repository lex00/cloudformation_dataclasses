"""LogsBucketPolicy - AWS::S3::BucketPolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LogsBucketPolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'ELBAccessLogs20130930'
    principal = {
        'AWS': FindInMap("Region2ELBAccountId", AWS_REGION, 'AccountId'),
    }
    action = ['s3:PutObject']
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${LogsBucket}/Logs/AWSLogs/${AWS::AccountId}/*')]


@cloudformation_dataclass
class LogsBucketPolicyDenyStatement1:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${LogsBucket}/Logs/AWSLogs/${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${LogsBucket}/Logs/AWSLogs/${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class LogsBucketPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [LogsBucketPolicyAllowStatement0, LogsBucketPolicyDenyStatement1]


@cloudformation_dataclass
class LogsBucketPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(LogsBucket)
    policy_document = LogsBucketPolicyPolicyDocument
