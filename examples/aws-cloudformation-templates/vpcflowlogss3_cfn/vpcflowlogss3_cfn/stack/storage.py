"""Storage resources: VPCFlowLogsBucket, VPCFlowLogsBucketPolicy."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCFlowLogsBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class VPCFlowLogsBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = If("VPCFlowLogsBucketKMSKeyCondition", 'aws:kms', 'AES256')
    kms_master_key_id = If("VPCFlowLogsBucketKMSKeyCondition", ref(VPCFlowLogsBucketKMSKey), AWS_NO_VALUE)


@cloudformation_dataclass
class VPCFlowLogsBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = VPCFlowLogsBucketServerSideEncryptionByDefault
    bucket_key_enabled = If("VPCFlowLogsBucketKMSKeyCondition", ref(VPCFlowLogsBucketKeyEnabled), AWS_NO_VALUE)


@cloudformation_dataclass
class VPCFlowLogsBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [VPCFlowLogsBucketServerSideEncryptionRule]


@cloudformation_dataclass
class VPCFlowLogsBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class VPCFlowLogsBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_name = Sub('aws-vpcflowlogs-${AWS::AccountId}-${AWS::Region}')
    public_access_block_configuration = VPCFlowLogsBucketPublicAccessBlockConfiguration
    bucket_encryption = VPCFlowLogsBucketBucketEncryption
    logging_configuration = If("S3AccessLogsCondition", {
    LoggingConfiguration.destination_bucket_name: ref(S3AccessLogsBucketName),
}, AWS_NO_VALUE)
    versioning_configuration = VPCFlowLogsBucketDeleteMarkerReplication
    condition = 'VPCFlowLogsNewBucketCondition'


@cloudformation_dataclass
class VPCFlowLogsBucketPolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'AWSLogDeliveryWrite'
    principal = {
        'Service': 'delivery.logs.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${VPCFlowLogsBucket}/*')
    condition = {
        STRING_EQUALS: {
            's3:x-amz-acl': 'bucket-owner-full-control',
        },
    }


@cloudformation_dataclass
class VPCFlowLogsBucketPolicyAllowStatement1:
    resource: PolicyStatement
    sid = 'AWSLogDeliveryAclCheck'
    principal = {
        'Service': 'delivery.logs.amazonaws.com',
    }
    action = 's3:GetBucketAcl'
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${VPCFlowLogsBucket}')


@cloudformation_dataclass
class VPCFlowLogsBucketPolicyDenyStatement2:
    resource: DenyStatement
    sid = 'DenyNonSSLRequests'
    principal = '*'
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${VPCFlowLogsBucket}'),
        Sub('arn:${AWS::Partition}:s3:::${VPCFlowLogsBucket}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class VPCFlowLogsBucketPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [VPCFlowLogsBucketPolicyAllowStatement0, VPCFlowLogsBucketPolicyAllowStatement1, VPCFlowLogsBucketPolicyDenyStatement2]


@cloudformation_dataclass
class VPCFlowLogsBucketPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(VPCFlowLogsBucket)
    policy_document = VPCFlowLogsBucketPolicyPolicyDocument
    condition = 'VPCFlowLogsNewBucketCondition'
