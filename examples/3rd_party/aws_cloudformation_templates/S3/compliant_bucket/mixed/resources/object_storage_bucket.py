"""ObjectStorageBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403
from ..config import AppName
from .object_storage_log_bucket import ObjectStorageLogBucket
from .object_storage_replica_bucket import ObjectStorageReplicaBucket
from .object_storage_replication_role import ObjectStorageReplicationRole


@cloudformation_dataclass
class ObjectStorageBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_encryption = {
        BucketEncryption.SERVER_SIDE_ENCRYPTION_CONFIGURATION: [{
            ServerSideEncryptionRule.SERVER_SIDE_ENCRYPTION_BY_DEFAULT: {
                ServerSideEncryptionByDefault.SSE_ALGORITHM: 'AES256',
            },
        }],
    }
    bucket_name = Sub('${AppName}-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = {
        LoggingConfiguration.DESTINATION_BUCKET_NAME: ref(ObjectStorageLogBucket),
    }
    object_lock_enabled = False
    public_access_block_configuration = {
        PublicAccessBlockConfiguration.BLOCK_PUBLIC_ACLS: True,
        PublicAccessBlockConfiguration.BLOCK_PUBLIC_POLICY: True,
        PublicAccessBlockConfiguration.IGNORE_PUBLIC_ACLS: True,
        PublicAccessBlockConfiguration.RESTRICT_PUBLIC_BUCKETS: True,
    }
    replication_configuration = {
        ReplicationConfiguration.ROLE: get_att(ObjectStorageReplicationRole, "Arn"),
        ReplicationConfiguration.RULES: [{
            ReplicationRule.DESTINATION: {
                Region.BUCKET: get_att(ObjectStorageReplicaBucket, "Arn"),
            },
            ReplicationRule.STATUS: 'Enabled',
        }],
    }
    versioning_configuration = {
        DeleteMarkerReplication.STATUS: 'Enabled',
    }
