"""ObjectStorageReplicaBucketPolicyPolicy - AWS::S3::BucketPolicy resource."""

from .. import *  # noqa: F403
from ..config import AppName
from .object_storage_replica_bucket import ObjectStorageReplicaBucket


@cloudformation_dataclass
class ObjectStorageReplicaBucketPolicyPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        get_att(ObjectStorageReplicaBucket, ARN),
        Join('', [get_att(ObjectStorageReplicaBucket, ARN), '/*']),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class ObjectStorageReplicaBucketPolicyPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Join('', [get_att(ObjectStorageReplicaBucket, ARN), '/*'])]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': get_att(ObjectStorageReplicaBucket, ARN),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class ObjectStorageReplicaBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ObjectStorageReplicaBucketPolicyPolicyDenyStatement0, ObjectStorageReplicaBucketPolicyPolicyAllowStatement1]


@cloudformation_dataclass
class ObjectStorageReplicaBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: BucketPolicy
    bucket = ref(ObjectStorageReplicaBucket)
    policy_document = ObjectStorageReplicaBucketPolicyPolicyPolicyDocument
