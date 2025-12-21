"""ObjectStorageReplicaBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403
from ..config import AppName


@cloudformation_dataclass
class ObjectStorageReplicaBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_encryption = {
        BucketEncryption.SERVER_SIDE_ENCRYPTION_CONFIGURATION: [{
            ServerSideEncryptionRule.SERVER_SIDE_ENCRYPTION_BY_DEFAULT: {
                ServerSideEncryptionByDefault.SSE_ALGORITHM: 'AES256',
            },
        }],
    }
    bucket_name = Sub('${AppName}-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = {
        PublicAccessBlockConfiguration.BLOCK_PUBLIC_ACLS: True,
        PublicAccessBlockConfiguration.BLOCK_PUBLIC_POLICY: True,
        PublicAccessBlockConfiguration.IGNORE_PUBLIC_ACLS: True,
        PublicAccessBlockConfiguration.RESTRICT_PUBLIC_BUCKETS: True,
    }
    versioning_configuration = {
        DeleteMarkerReplication.STATUS: 'Enabled',
    }
