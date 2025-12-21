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
class DataClassificationTag:
    """Data classification tag for sensitive data."""

    resource: Tag
    key = "DataClassification"
    value = "sensitive"


@cloudformation_dataclass
class MyData:
    """
    Production data bucket with encryption and versioning.

    Resource naming:
    - Logical ID: MyData (class name)
    - Resource name: analytics-DataPlatform-MyData-prod-001-blue-us-east-1
      (formatted with context pattern: {project_name}-{component}-{resource_name}-{stage}-{deployment_name}-{deployment_group}-{region})
    - deployment_group="blue" enables blue/green deployments
    """

    resource: Bucket
    context = ctx
    bucket_encryption = MyDataBucketEncryption
    versioning_configuration = MyDataVersioningConfiguration
    tags = [DataClassificationTag]
