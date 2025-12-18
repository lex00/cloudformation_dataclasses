"""
S3 Bucket with Cross-Account Access Policy.

Inspired by AWS's S3/s3-bucket-and-policy-for-caa-v1.yaml template.
Demonstrates:
- S3 Bucket with encryption and versioning
- PublicAccessBlockConfiguration for security
- BucketPolicy with cross-account IAM statements
- Sub intrinsic with AWS::Partition pseudo-parameter
- Policy statements with conditions (deny non-HTTPS)
"""

from . import *  # noqa: F403


# =============================================================================
# Tags
# =============================================================================


@cloudformation_dataclass
class EnvironmentTag:
    """Environment tag."""

    resource: Tag
    key = "Environment"
    value = "Production"


@cloudformation_dataclass
class ManagedByTag:
    """ManagedBy tag."""

    resource: Tag
    key = "ManagedBy"
    value = "cloudformation-dataclasses"


# =============================================================================
# Deployment Context
# =============================================================================


@cloudformation_dataclass
class S3Context:
    """
    Deployment context for S3 cross-account access example.

    Resource naming pattern: {project_name}-{component}-{resource_name}-{stage}
    Example: dataplatform-storage-SharedBucket-prod
    """

    context: DeploymentContext
    project_name = "dataplatform"
    component = "storage"
    stage = "prod"
    region = "us-east-1"
    tags = [EnvironmentTag, ManagedByTag]
    naming_pattern = "{project_name}-{component}-{resource_name}-{stage}"


ctx = S3Context()


# =============================================================================
# Parameters
# =============================================================================


@cloudformation_dataclass
class BucketName:
    """Name of the S3 bucket to create."""

    resource: Parameter
    type = STRING
    description = "The name of the S3 Bucket to create, make this unique"


@cloudformation_dataclass
class PublisherAccountID:
    """AWS account ID to grant cross-account access."""

    resource: Parameter
    type = STRING
    description = "The AWS account ID with whom you are sharing access"


# =============================================================================
# Bucket Configuration
# =============================================================================


@cloudformation_dataclass
class AES256Encryption:
    """AES256 server-side encryption configuration."""

    resource: ServerSideEncryptionByDefault
    sse_algorithm = "AES256"


@cloudformation_dataclass
class EncryptionRule:
    """Server-side encryption rule."""

    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = AES256Encryption


@cloudformation_dataclass
class BucketEncryptionConfig:
    """Bucket encryption configuration."""

    resource: BucketEncryption
    server_side_encryption_configuration = [EncryptionRule]


@cloudformation_dataclass
class VersioningEnabled:
    """Enable versioning on bucket."""

    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class BlockAllPublicAccess:
    """Block all public access to the bucket."""

    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


# =============================================================================
# Resources
# =============================================================================


@cloudformation_dataclass
class SharedBucket:
    """
    S3 bucket with encryption, versioning, and public access blocked.

    This bucket is configured for cross-account access sharing.
    """

    resource: Bucket
    context = ctx
    bucket_name = ref(BucketName)
    bucket_encryption = BucketEncryptionConfig
    versioning_configuration = VersioningEnabled
    public_access_block_configuration = BlockAllPublicAccess


def _bucket_arn() -> dict:
    """Generate bucket ARN using Sub with AWS::Partition."""
    return Sub("arn:${AWS::Partition}:s3:::${Bucket}", {"Bucket": ref(BucketName)}).to_dict()


def _bucket_objects_arn() -> dict:
    """Generate bucket objects ARN using Sub with AWS::Partition."""
    return Sub("arn:${AWS::Partition}:s3:::${Bucket}/*", {"Bucket": ref(BucketName)}).to_dict()


def _cross_account_principal() -> dict:
    """Generate cross-account principal ARN using Sub with AWS::Partition."""
    return Sub(
        "arn:${AWS::Partition}:iam::${AccountId}:root",
        {"AccountId": ref(PublisherAccountID)}
    ).to_dict()


@cloudformation_dataclass
class SharedBucketPolicy:
    """
    Bucket policy enabling cross-account access.

    Grants:
    - s3:ListBucket to the publisher account
    - s3:GetObject to the publisher account
    - Denies all non-HTTPS requests
    """

    resource: BucketPolicy
    bucket = ref(SharedBucket)
    policy_document = {
        "Id": "CrossAccessPolicy",
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "CrossAccListBucket",
                "Effect": "Allow",
                "Action": "s3:ListBucket",
                "Resource": _bucket_arn(),
                "Principal": {"AWS": _cross_account_principal()},
            },
            {
                "Sid": "CrossAccGetObject",
                "Effect": "Allow",
                "Action": "s3:GetObject",
                "Resource": _bucket_objects_arn(),
                "Principal": {"AWS": _cross_account_principal()},
            },
            {
                "Sid": "DenyNonHttps",
                "Effect": "Deny",
                "Action": "s3:*",
                "Resource": [_bucket_arn(), _bucket_objects_arn()],
                "Principal": {"AWS": "*"},
                "Condition": {
                    "Bool": {
                        "aws:SecureTransport": "false"
                    }
                },
            },
        ],
    }


# =============================================================================
# Outputs
# =============================================================================


@cloudformation_dataclass
class BucketOutput:
    """S3 bucket name output."""

    resource: Output
    value = ref(SharedBucket)
    description = "S3 Bucket Name"


@cloudformation_dataclass
class BucketPolicyOutput:
    """S3 bucket policy output."""

    resource: Output
    value = ref(SharedBucketPolicy)
    description = "S3 Bucket Policy Name"


# =============================================================================
# Template
# =============================================================================


@cloudformation_dataclass
class CrossAccountAccessTemplate:
    """
    S3 bucket with cross-account access policy template.

    Demonstrates:
    - Parameters for bucket name and cross-account ID
    - S3 bucket with encryption, versioning, and public access blocking
    - IAM policy with cross-account access and HTTPS enforcement
    """

    resource: Template
    description = (
        "AWS CloudFormation Sample Template: S3 bucket with cross-account access. "
        "Creates an S3 bucket with a bucket policy enabling cross-account access."
    )
    parameters = [BucketName, PublisherAccountID]
    resources = [SharedBucket, SharedBucketPolicy]
    outputs = [BucketOutput, BucketPolicyOutput]


def build_template() -> Template:
    """Build the S3 cross-account access template."""
    return CrossAccountAccessTemplate().resource


if __name__ == "__main__":
    import json

    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))
