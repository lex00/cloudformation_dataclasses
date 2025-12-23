"""MyData - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MyDataServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class MyDataServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = MyDataServerSideEncryptionByDefault


@cloudformation_dataclass
class MyDataBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [MyDataServerSideEncryptionRule]


@cloudformation_dataclass
class MyDataDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class MyDataTagFilter:
    resource: s3.bucket.TagFilter
    key = 'DataClassification'
    value = 'sensitive'


@cloudformation_dataclass
class MyData:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = MyDataBucketEncryption
    versioning_configuration = MyDataDeleteMarkerReplication
    tags = [MyDataTagFilter]
