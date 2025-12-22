"""PipelineS3Bucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PipelineS3BucketServerSideEncryptionByDefault:
    resource: s3.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class PipelineS3BucketServerSideEncryptionRule:
    resource: s3.ServerSideEncryptionRule
    server_side_encryption_by_default = PipelineS3BucketServerSideEncryptionByDefault


@cloudformation_dataclass
class PipelineS3BucketBucketEncryption:
    resource: s3.BucketEncryption
    server_side_encryption_configuration = [PipelineS3BucketServerSideEncryptionRule]


@cloudformation_dataclass
class PipelineS3BucketPublicAccessBlockConfiguration:
    resource: s3.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class PipelineS3Bucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_name = Sub('${AWS::StackName}-bucket')
    bucket_encryption = PipelineS3BucketBucketEncryption
    public_access_block_configuration = PipelineS3BucketPublicAccessBlockConfiguration
