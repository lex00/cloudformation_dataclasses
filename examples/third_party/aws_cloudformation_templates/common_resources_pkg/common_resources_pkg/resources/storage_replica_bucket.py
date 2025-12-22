"""StorageReplicaBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class StorageReplicaBucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class StorageReplicaBucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = StorageReplicaBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class StorageReplicaBucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [StorageReplicaBucketServerSideEncryptionRule]


@cloudformation_dataclass
class StorageReplicaBucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class StorageReplicaBucketVersioningConfiguration:
    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class StorageReplicaBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_encryption = StorageReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = StorageReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = StorageReplicaBucketVersioningConfiguration
