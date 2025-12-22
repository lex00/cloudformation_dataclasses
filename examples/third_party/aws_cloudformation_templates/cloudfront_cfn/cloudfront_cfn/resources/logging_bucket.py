"""LoggingBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoggingBucketOwnershipControlsRule:
    resource: OwnershipControlsRule
    object_ownership = 'ObjectWriter'


@cloudformation_dataclass
class LoggingBucketOwnershipControls:
    resource: OwnershipControls
    rules = [LoggingBucketOwnershipControlsRule]


@cloudformation_dataclass
class LoggingBucketPublicAccessBlockConfiguration:
    resource: s3.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class LoggingBucketServerSideEncryptionByDefault:
    resource: s3.ServerSideEncryptionByDefault
    kms_master_key_id = get_att(LoggingBucketKMSKey, "Arn")
    sse_algorithm = ServerSideEncryption.AWS_KMS


@cloudformation_dataclass
class LoggingBucketServerSideEncryptionRule:
    resource: s3.ServerSideEncryptionRule
    server_side_encryption_by_default = LoggingBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class LoggingBucketBucketEncryption:
    resource: s3.BucketEncryption
    server_side_encryption_configuration = [LoggingBucketServerSideEncryptionRule]


@cloudformation_dataclass
class LoggingBucketVersioningConfiguration:
    resource: s3.VersioningConfiguration
    status = ref(LoggingBucketVersioning)


@cloudformation_dataclass
class LoggingBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_name = Sub('${AppName}-logging-${Environment}-${AWS::AccountId}-${AWS::Region}')
    ownership_controls = LoggingBucketOwnershipControls
    public_access_block_configuration = LoggingBucketPublicAccessBlockConfiguration
    access_control = 'LogDeliveryWrite'
    bucket_encryption = LoggingBucketBucketEncryption
    versioning_configuration = LoggingBucketVersioningConfiguration
    depends_on = ["LoggingBucketKMSKey"]
    deletion_policy = 'Retain'
