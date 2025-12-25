"""Storage resources: LoggingBucket, LoggingBucketPolicy."""

from . import *  # noqa: F403


@cloudformation_dataclass
class LoggingBucketOwnershipControlsRule:
    resource: s3.bucket.OwnershipControlsRule
    object_ownership = 'ObjectWriter'


@cloudformation_dataclass
class LoggingBucketOwnershipControls:
    resource: s3.bucket.OwnershipControls
    rules = [LoggingBucketOwnershipControlsRule]


@cloudformation_dataclass
class LoggingBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class LoggingBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    kms_master_key_id = get_att(LoggingBucketKMSKey, "Arn")
    sse_algorithm = ServerSideEncryption.AWS_KMS


@cloudformation_dataclass
class LoggingBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = LoggingBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class LoggingBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [LoggingBucketServerSideEncryptionRule]


@cloudformation_dataclass
class LoggingBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = ref(LoggingBucketVersioning)


@cloudformation_dataclass
class LoggingBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_name = Sub('${AppName}-logging-${Environment}-${AWS::AccountId}-${AWS::Region}')
    ownership_controls = LoggingBucketOwnershipControls
    public_access_block_configuration = LoggingBucketPublicAccessBlockConfiguration
    access_control = 'LogDeliveryWrite'
    bucket_encryption = LoggingBucketBucketEncryption
    versioning_configuration = LoggingBucketDeleteMarkerReplication
    depends_on = ["LoggingBucketKMSKey"]
    deletion_policy = 'Retain'


@cloudformation_dataclass
class LoggingBucketPolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'LoggingBucketPermissions'
    principal = {
        'AWS': Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:root'),
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${LoggingBucket}/AWSLogs/${AWS::AccountId}/*')]


@cloudformation_dataclass
class LoggingBucketPolicyDenyStatement1:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${LoggingBucket}/AWSLogs/${AWS::AccountId}/*')]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class LoggingBucketPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [LoggingBucketPolicyAllowStatement0, LoggingBucketPolicyDenyStatement1]


@cloudformation_dataclass
class LoggingBucketPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(LoggingBucket)
    policy_document = LoggingBucketPolicyPolicyDocument
