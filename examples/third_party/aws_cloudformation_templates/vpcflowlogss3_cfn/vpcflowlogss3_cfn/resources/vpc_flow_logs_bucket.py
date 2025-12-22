from __future__ import annotations

"""VPCFlowLogsBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCFlowLogsBucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class VPCFlowLogsBucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = If("VPCFlowLogsBucketKMSKeyCondition", 'aws:kms', 'AES256')
    kms_master_key_id = If("VPCFlowLogsBucketKMSKeyCondition", ref(VPCFlowLogsBucketKMSKey), AWS_NO_VALUE)


@cloudformation_dataclass
class VPCFlowLogsBucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = VPCFlowLogsBucketServerSideEncryptionByDefault
    bucket_key_enabled = If("VPCFlowLogsBucketKMSKeyCondition", ref(VPCFlowLogsBucketKeyEnabled), AWS_NO_VALUE)


@cloudformation_dataclass
class VPCFlowLogsBucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [VPCFlowLogsBucketServerSideEncryptionRule]


@cloudformation_dataclass
class VPCFlowLogsBucketVersioningConfiguration:
    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class VPCFlowLogsBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_name = Sub('aws-vpcflowlogs-${AWS::AccountId}-${AWS::Region}')
    public_access_block_configuration = VPCFlowLogsBucketPublicAccessBlockConfiguration
    bucket_encryption = VPCFlowLogsBucketBucketEncryption
    logging_configuration = If("S3AccessLogsCondition", {
    LoggingConfiguration.destination_bucket_name: ref(S3AccessLogsBucketName),
}, AWS_NO_VALUE)
    versioning_configuration = VPCFlowLogsBucketVersioningConfiguration
    condition = 'VPCFlowLogsNewBucketCondition'
