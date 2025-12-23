"""LoggingBucketKMSKey - AWS::KMS::Key resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoggingBucketKMSKeyAllowStatement0:
    resource: PolicyStatement
    sid = 'Enable IAM policies to allow access to the Key'
    principal = {
        'AWS': Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:root'),
    }
    action = ['kms:*']
    resource_arn = '*'


@cloudformation_dataclass
class LoggingBucketKMSKeyAllowStatement1:
    resource: PolicyStatement
    sid = 'Allow administration of the key'
    principal = {
        'AWS': [Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:role/AdministratorAccess-${AppName}')],
    }
    action = [
        'kms:Put*',
        'kms:ScheduleKeyDeletion',
        'kms:CancelKeyDeletion',
        'kms:Describe*',
        'kms:Revoke*',
        'kms:Disable*',
        'kms:Enable*',
        'kms:Delete*',
        'kms:List*',
        'kms:Update*',
        'kms:Create*',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class LoggingBucketKMSKeyKeyPolicy:
    resource: PolicyDocument
    statement = [LoggingBucketKMSKeyAllowStatement0, LoggingBucketKMSKeyAllowStatement1]


@cloudformation_dataclass
class LoggingBucketKMSKey:
    """AWS::KMS::Key resource."""

    resource: kms.Key
    description = 'Logging S3 Bucket KMS Key'
    enabled = True
    enable_key_rotation = True
    key_policy = LoggingBucketKMSKeyKeyPolicy
    depends_on = ["AdministratorAccessIAMRole"]
