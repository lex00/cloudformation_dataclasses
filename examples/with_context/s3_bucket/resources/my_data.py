from __future__ import annotations

"""MyData - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403
from ..context import ctx


@cloudformation_dataclass
class MyDataServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class MyDataServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = MyDataServerSideEncryptionByDefault


@cloudformation_dataclass
class MyDataBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [MyDataServerSideEncryptionRule]


@cloudformation_dataclass
class MyDataVersioningConfiguration:
    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class MyDataTag:
    resource: Tag
    key = 'DataClassification'
    value = 'sensitive'


@cloudformation_dataclass
class MyData:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    context = ctx  # Wires up deployment context for naming and tags
    bucket_encryption = MyDataBucketEncryption
    versioning_configuration = MyDataVersioningConfiguration
    tags = [MyDataTag]
