"""S3 bucket with encryption and versioning configuration."""

from . import *  # noqa: F403
from .context import ctx


@cloudformation_dataclass
class MyServerSideEncryptionByDefault:
    """AES256 encryption configuration."""

    resource: ServerSideEncryptionByDefault
    sse_algorithm = "AES256"


@cloudformation_dataclass
class MyServerSideEncryptionRule:
    """Server-side encryption rule."""

    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = MyServerSideEncryptionByDefault


@cloudformation_dataclass
class MyBucketEncryption:
    """Bucket encryption configuration."""

    resource: BucketEncryption
    server_side_encryption_configuration = [MyServerSideEncryptionRule]


@cloudformation_dataclass
class MyData:
    """
    Production data bucket with encryption and versioning.

    Resource naming:
    - Logical ID: MyData (class name)
    - Resource name: DataPlatform-MyData-prod-001-blue-us-east-1
      (formatted with context pattern: {component}-{resource_name}-{stage}-{deployment_name}-{deployment_group}-{region})
    - deployment_group="blue" enables blue/green deployments

    The naming pattern can be overridden per resource:
        MyData(naming_pattern="{component}-{resource_name}")
        -> "DataPlatform-MyData"
    """

    resource: Bucket
    context = ctx
    tags = [{"Key": "DataClassification", "Value": "sensitive"}]
    bucket_encryption = MyBucketEncryption
    versioning_configuration = {"Status": "Enabled"}
