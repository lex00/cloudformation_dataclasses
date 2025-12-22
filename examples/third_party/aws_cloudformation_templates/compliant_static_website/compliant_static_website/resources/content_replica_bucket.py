"""ContentReplicaBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ContentReplicaBucketServerSideEncryptionByDefault:
    resource: s3.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class ContentReplicaBucketServerSideEncryptionRule:
    resource: s3.ServerSideEncryptionRule
    server_side_encryption_by_default = ContentReplicaBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class ContentReplicaBucketBucketEncryption:
    resource: s3.BucketEncryption
    server_side_encryption_configuration = [ContentReplicaBucketServerSideEncryptionRule]


@cloudformation_dataclass
class ContentReplicaBucketPublicAccessBlockConfiguration:
    resource: s3.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class ContentReplicaBucketVersioningConfiguration:
    resource: s3.VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class ContentReplicaBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = ContentReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = ContentReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = ContentReplicaBucketVersioningConfiguration
