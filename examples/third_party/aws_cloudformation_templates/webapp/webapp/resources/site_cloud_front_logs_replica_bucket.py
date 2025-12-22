"""SiteCloudFrontLogsReplicaBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteCloudFrontLogsReplicaBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [SiteCloudFrontLogsReplicaBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = SiteCloudFrontLogsReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = SiteCloudFrontLogsReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteCloudFrontLogsReplicaBucketDeleteMarkerReplication
