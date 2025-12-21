"""ObjectStorageLogBucketPolicyPolicy - AWS::S3::BucketPolicy resource."""

from .. import *  # noqa: F403
from ..config import AppName
from .object_storage_log_bucket import ObjectStorageLogBucket


@cloudformation_dataclass
class ObjectStorageLogBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: BucketPolicy
    bucket = ref(ObjectStorageLogBucket)
    policy_document = PolicyDocument(statement=[
            PolicyStatement(
                effect='Deny',
                principal={
                    'AWS': '*',
                },
                action='s3:*',
                resource_arn=[
                    get_att(ObjectStorageLogBucket, ARN),
                    Join('', [get_att(ObjectStorageLogBucket, ARN), '/*']),
                ],
                condition={
                    BOOL: {
                        'aws:SecureTransport': False,
                    },
                },
            ),
            PolicyStatement(
                principal={
                    'Service': 'logging.s3.amazonaws.com',
                },
                action='s3:PutObject',
                resource_arn=[Join('', [get_att(ObjectStorageLogBucket, ARN), '/*'])],
                condition={
                    ARN_LIKE: {
                        'aws:SourceArn': get_att(ObjectStorageLogBucket, ARN),
                    },
                    STRING_EQUALS: {
                        'aws:SourceAccount': AWS_ACCOUNT_ID,
                    },
                },
            ),
        ])
