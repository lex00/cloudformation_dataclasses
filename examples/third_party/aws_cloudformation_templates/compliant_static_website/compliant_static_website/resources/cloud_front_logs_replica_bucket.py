"""CloudFrontLogsReplicaBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CloudFrontLogsReplicaBucketServerSideEncryptionByDefault:
    resource: s3.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class CloudFrontLogsReplicaBucketServerSideEncryptionRule:
    resource: s3.ServerSideEncryptionRule
    server_side_encryption_by_default = CloudFrontLogsReplicaBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class CloudFrontLogsReplicaBucketBucketEncryption:
    resource: s3.BucketEncryption
    server_side_encryption_configuration = [CloudFrontLogsReplicaBucketServerSideEncryptionRule]


@cloudformation_dataclass
class CloudFrontLogsReplicaBucketPublicAccessBlockConfiguration:
    resource: s3.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class CloudFrontLogsReplicaBucketVersioningConfiguration:
    resource: s3.VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class CloudFrontLogsReplicaBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = CloudFrontLogsReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = CloudFrontLogsReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = CloudFrontLogsReplicaBucketVersioningConfiguration
