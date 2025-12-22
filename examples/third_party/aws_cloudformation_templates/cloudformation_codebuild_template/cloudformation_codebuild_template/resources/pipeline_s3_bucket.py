"""PipelineS3Bucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PipelineS3BucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class PipelineS3BucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = PipelineS3BucketServerSideEncryptionByDefault


@cloudformation_dataclass
class PipelineS3BucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [PipelineS3BucketServerSideEncryptionRule]


@cloudformation_dataclass
class PipelineS3BucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class PipelineS3Bucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_name = Sub('${AWS::StackName}-bucket')
    bucket_encryption = PipelineS3BucketBucketEncryption
    public_access_block_configuration = PipelineS3BucketPublicAccessBlockConfiguration
