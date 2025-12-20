"""S3 bucket with encryption and versioning configuration."""

from . import *  # noqa: F403
from .context import ctx


# =============================================================================
# Tags
# =============================================================================


@cloudformation_dataclass
class DataClassificationTag:
    """Data classification tag for sensitive data."""

    resource: Tag
    key = "DataClassification"
    value = "sensitive"


# =============================================================================
# Encryption Configuration
# =============================================================================


@cloudformation_dataclass
class MyServerSideEncryptionByDefault:
    """AES256 encryption configuration."""

    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


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


# =============================================================================
# Versioning Configuration
# =============================================================================


@cloudformation_dataclass
class MyVersioningConfiguration:
    """Enable versioning on the bucket."""

    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


# =============================================================================
# Resources
# =============================================================================


@cloudformation_dataclass
class MyData:
    """
    Production data bucket with encryption and versioning.

    Resource naming:
    - Logical ID: MyData (class name)
    - Resource name: analytics-DataPlatform-MyData-prod-001-blue-us-east-1
      (formatted with context pattern: {project_name}-{component}-{resource_name}-{stage}-{deployment_name}-{deployment_group}-{region})
    - deployment_group="blue" enables blue/green deployments

    The naming pattern can be overridden per resource:
        MyData(naming_pattern="{component}-{resource_name}")
        -> "DataPlatform-MyData"
    """

    resource: Bucket
    context = ctx
    tags = [DataClassificationTag]
    bucket_encryption = MyBucketEncryption
    versioning_configuration = MyVersioningConfiguration
