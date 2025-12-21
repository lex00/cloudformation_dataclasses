from __future__ import annotations

"""S3BucketDestination - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class S3BucketDestinationServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AWS_KMS
    kms_master_key_id: Ref[KmsKey] = ref()


@cloudformation_dataclass
class S3BucketDestinationServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = S3BucketDestinationServerSideEncryptionByDefault
    bucket_key_enabled = True


@cloudformation_dataclass
class S3BucketDestinationBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [S3BucketDestinationServerSideEncryptionRule]


@cloudformation_dataclass
class S3BucketDestinationPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class S3BucketDestinationVersioningConfiguration:
    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class S3BucketDestination:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_name = Sub('${AWS::StackName}-${AWS::AccountId}-bucket')
    bucket_encryption = S3BucketDestinationBucketEncryption
    public_access_block_configuration = S3BucketDestinationPublicAccessBlockConfiguration
    versioning_configuration = S3BucketDestinationVersioningConfiguration
    deletion_policy = 'Delete'
