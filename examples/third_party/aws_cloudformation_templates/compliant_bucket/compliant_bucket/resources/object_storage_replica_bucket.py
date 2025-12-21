from __future__ import annotations

"""ObjectStorageReplicaBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ObjectStorageReplicaBucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class ObjectStorageReplicaBucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = ObjectStorageReplicaBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class ObjectStorageReplicaBucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [ObjectStorageReplicaBucketServerSideEncryptionRule]


@cloudformation_dataclass
class ObjectStorageReplicaBucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class ObjectStorageReplicaBucketVersioningConfiguration:
    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class ObjectStorageReplicaBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_encryption = ObjectStorageReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = ObjectStorageReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = ObjectStorageReplicaBucketVersioningConfiguration
