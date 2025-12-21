from __future__ import annotations

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
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class LoggingBucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    kms_master_key_id: GetAtt[LoggingBucketKMSKey] = get_att("Arn")
    sse_algorithm = ServerSideEncryption.AWS_KMS


@cloudformation_dataclass
class LoggingBucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = LoggingBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class LoggingBucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [LoggingBucketServerSideEncryptionRule]


@cloudformation_dataclass
class LoggingBucketVersioningConfiguration:
    resource: VersioningConfiguration
    status = ref(LoggingBucketVersioning)


@cloudformation_dataclass
class LoggingBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_name = Sub('${AppName}-logging-${Environment}-${AWS::AccountId}-${AWS::Region}')
    ownership_controls = LoggingBucketOwnershipControls
    public_access_block_configuration = LoggingBucketPublicAccessBlockConfiguration
    access_control = 'LogDeliveryWrite'
    bucket_encryption = LoggingBucketBucketEncryption
    versioning_configuration = LoggingBucketVersioningConfiguration
    depends_on = ["LoggingBucketKMSKey"]
    deletion_policy = 'Retain'
