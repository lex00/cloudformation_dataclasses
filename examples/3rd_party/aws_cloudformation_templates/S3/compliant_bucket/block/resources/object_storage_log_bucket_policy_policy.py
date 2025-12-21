"""ObjectStorageLogBucketPolicyPolicy - AWS::S3::BucketPolicy resource."""

from .. import *  # noqa: F403
from ..config import AppName
from .object_storage_log_bucket import ObjectStorageLogBucket


@cloudformation_dataclass
class ObjectStorageLogBucketPolicyPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        get_att(ObjectStorageLogBucket, ARN),
        Join('', [get_att(ObjectStorageLogBucket, ARN), '/*']),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class ObjectStorageLogBucketPolicyPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Join('', [get_att(ObjectStorageLogBucket, ARN), '/*'])]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': get_att(ObjectStorageLogBucket, ARN),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class ObjectStorageLogBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ObjectStorageLogBucketPolicyPolicyDenyStatement0, ObjectStorageLogBucketPolicyPolicyAllowStatement1]


@cloudformation_dataclass
class ObjectStorageLogBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: BucketPolicy
    bucket = ref(ObjectStorageLogBucket)
    policy_document = ObjectStorageLogBucketPolicyPolicyPolicyDocument
