"""ObjectStorageReplicaBucketPolicyPolicy - AWS::S3::BucketPolicy resource."""

from .. import *  # noqa: F403
from ..config import AppName
from .object_storage_replica_bucket import ObjectStorageReplicaBucket


@cloudformation_dataclass
class ObjectStorageReplicaBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: BucketPolicy
    bucket = ref(ObjectStorageReplicaBucket)
    policy_document = PolicyDocument(statement=[
            PolicyStatement(
                effect='Deny',
                principal={
                    'AWS': '*',
                },
                action='s3:*',
                resource_arn=[
                    get_att(ObjectStorageReplicaBucket, ARN),
                    Join('', [get_att(ObjectStorageReplicaBucket, ARN), '/*']),
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
                resource_arn=[Join('', [get_att(ObjectStorageReplicaBucket, ARN), '/*'])],
                condition={
                    ARN_LIKE: {
                        'aws:SourceArn': get_att(ObjectStorageReplicaBucket, ARN),
                    },
                    STRING_EQUALS: {
                        'aws:SourceAccount': AWS_ACCOUNT_ID,
                    },
                },
            ),
        ])
