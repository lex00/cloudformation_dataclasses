"""Storage resources: CloudFrontLogsLogBucket, CloudFrontLogsReplicaBucket, CloudFrontLogsBucket, CloudFrontLogsBucketPolicyPolicy, CloudFrontLogsLogBucketPolicyPolicy, CloudFrontLogsReplicaBucketPolicyPolicy, ContentLogBucket, ContentReplicaBucket, ContentBucket, ContentBucketPolicyPolicy, ContentLogBucketPolicyPolicy, ContentReplicaBucketPolicyPolicy."""

from . import *  # noqa: F403

from cloudformation_dataclasses.aws.s3 import BucketVersioningStatus


@cloudformation_dataclass
class CloudFrontLogsLogBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class CloudFrontLogsLogBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = CloudFrontLogsLogBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class CloudFrontLogsLogBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [CloudFrontLogsLogBucketServerSideEncryptionRule]


@cloudformation_dataclass
class CloudFrontLogsLogBucketDefaultRetention:
    resource: s3.bucket.DefaultRetention
    mode = ObjectLockRetentionMode.COMPLIANCE
    years = 1


@cloudformation_dataclass
class CloudFrontLogsLogBucketObjectLockRule:
    resource: s3.bucket.ObjectLockRule
    default_retention = CloudFrontLogsLogBucketDefaultRetention


@cloudformation_dataclass
class CloudFrontLogsLogBucketObjectLockConfiguration:
    resource: s3.bucket.ObjectLockConfiguration
    object_lock_enabled = ObjectLockEnabled.ENABLED
    rule = CloudFrontLogsLogBucketObjectLockRule


@cloudformation_dataclass
class CloudFrontLogsLogBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class CloudFrontLogsLogBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class CloudFrontLogsLogBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = CloudFrontLogsLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = CloudFrontLogsLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = CloudFrontLogsLogBucketPublicAccessBlockConfiguration
    versioning_configuration = CloudFrontLogsLogBucketDeleteMarkerReplication


@cloudformation_dataclass
class CloudFrontLogsReplicaBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class CloudFrontLogsReplicaBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = CloudFrontLogsReplicaBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class CloudFrontLogsReplicaBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [CloudFrontLogsReplicaBucketServerSideEncryptionRule]


@cloudformation_dataclass
class CloudFrontLogsReplicaBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class CloudFrontLogsReplicaBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class CloudFrontLogsReplicaBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = CloudFrontLogsReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = CloudFrontLogsReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = CloudFrontLogsReplicaBucketDeleteMarkerReplication


@cloudformation_dataclass
class CloudFrontLogsBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class CloudFrontLogsBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = CloudFrontLogsBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class CloudFrontLogsBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [CloudFrontLogsBucketServerSideEncryptionRule]


@cloudformation_dataclass
class CloudFrontLogsBucketLoggingConfiguration:
    resource: s3.bucket.LoggingConfiguration
    destination_bucket_name = ref(CloudFrontLogsLogBucket)


@cloudformation_dataclass
class CloudFrontLogsBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class CloudFrontLogsBucketReplicationDestination:
    resource: s3.bucket.ReplicationDestination
    bucket = get_att(CloudFrontLogsReplicaBucket, "Arn")


@cloudformation_dataclass
class CloudFrontLogsBucketReplicationRule:
    resource: s3.bucket.ReplicationRule
    destination = CloudFrontLogsBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class CloudFrontLogsBucketReplicationConfiguration:
    resource: s3.bucket.ReplicationConfiguration
    role = get_att(CloudFrontLogsReplicationRole, "Arn")
    rules = [CloudFrontLogsBucketReplicationRule]


@cloudformation_dataclass
class CloudFrontLogsBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class CloudFrontLogsBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = CloudFrontLogsBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = CloudFrontLogsBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = CloudFrontLogsBucketPublicAccessBlockConfiguration
    replication_configuration = CloudFrontLogsBucketReplicationConfiguration
    versioning_configuration = CloudFrontLogsBucketDeleteMarkerReplication


@cloudformation_dataclass
class CloudFrontLogsBucketPolicyPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class CloudFrontLogsBucketPolicyPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class CloudFrontLogsBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [CloudFrontLogsBucketPolicyPolicyDenyStatement0, CloudFrontLogsBucketPolicyPolicyAllowStatement1]


@cloudformation_dataclass
class CloudFrontLogsBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(CloudFrontLogsBucket)
    policy_document = CloudFrontLogsBucketPolicyPolicyPolicyDocument


@cloudformation_dataclass
class CloudFrontLogsLogBucketPolicyPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class CloudFrontLogsLogBucketPolicyPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class CloudFrontLogsLogBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [CloudFrontLogsLogBucketPolicyPolicyDenyStatement0, CloudFrontLogsLogBucketPolicyPolicyAllowStatement1]


@cloudformation_dataclass
class CloudFrontLogsLogBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(CloudFrontLogsLogBucket)
    policy_document = CloudFrontLogsLogBucketPolicyPolicyPolicyDocument


@cloudformation_dataclass
class CloudFrontLogsReplicaBucketPolicyPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class CloudFrontLogsReplicaBucketPolicyPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class CloudFrontLogsReplicaBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [CloudFrontLogsReplicaBucketPolicyPolicyDenyStatement0, CloudFrontLogsReplicaBucketPolicyPolicyAllowStatement1]


@cloudformation_dataclass
class CloudFrontLogsReplicaBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(CloudFrontLogsReplicaBucket)
    policy_document = CloudFrontLogsReplicaBucketPolicyPolicyPolicyDocument


@cloudformation_dataclass
class ContentLogBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class ContentLogBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = ContentLogBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class ContentLogBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [ContentLogBucketServerSideEncryptionRule]


@cloudformation_dataclass
class ContentLogBucketDefaultRetention:
    resource: s3.bucket.DefaultRetention
    mode = ObjectLockRetentionMode.COMPLIANCE
    years = 1


@cloudformation_dataclass
class ContentLogBucketObjectLockRule:
    resource: s3.bucket.ObjectLockRule
    default_retention = ContentLogBucketDefaultRetention


@cloudformation_dataclass
class ContentLogBucketObjectLockConfiguration:
    resource: s3.bucket.ObjectLockConfiguration
    object_lock_enabled = ObjectLockEnabled.ENABLED
    rule = ContentLogBucketObjectLockRule


@cloudformation_dataclass
class ContentLogBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class ContentLogBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class ContentLogBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = ContentLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = ContentLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = ContentLogBucketPublicAccessBlockConfiguration
    versioning_configuration = ContentLogBucketDeleteMarkerReplication


@cloudformation_dataclass
class ContentReplicaBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class ContentReplicaBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = ContentReplicaBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class ContentReplicaBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [ContentReplicaBucketServerSideEncryptionRule]


@cloudformation_dataclass
class ContentReplicaBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class ContentReplicaBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class ContentReplicaBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = ContentReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = ContentReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = ContentReplicaBucketDeleteMarkerReplication


@cloudformation_dataclass
class ContentBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class ContentBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = ContentBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class ContentBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [ContentBucketServerSideEncryptionRule]


@cloudformation_dataclass
class ContentBucketLoggingConfiguration:
    resource: s3.bucket.LoggingConfiguration
    destination_bucket_name = ref(ContentLogBucket)


@cloudformation_dataclass
class ContentBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class ContentBucketReplicationDestination:
    resource: s3.bucket.ReplicationDestination
    bucket = get_att(ContentReplicaBucket, "Arn")


@cloudformation_dataclass
class ContentBucketReplicationRule:
    resource: s3.bucket.ReplicationRule
    destination = ContentBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class ContentBucketReplicationConfiguration:
    resource: s3.bucket.ReplicationConfiguration
    role = get_att(ContentReplicationRole, "Arn")
    rules = [ContentBucketReplicationRule]


@cloudformation_dataclass
class ContentBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class ContentBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = ContentBucketBucketEncryption
    bucket_name = Sub('${AppName}-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = ContentBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = ContentBucketPublicAccessBlockConfiguration
    replication_configuration = ContentBucketReplicationConfiguration
    versioning_configuration = ContentBucketDeleteMarkerReplication


@cloudformation_dataclass
class ContentBucketPolicyPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class ContentBucketPolicyPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class ContentBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ContentBucketPolicyPolicyDenyStatement0, ContentBucketPolicyPolicyAllowStatement1]


@cloudformation_dataclass
class ContentBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(ContentBucket)
    policy_document = ContentBucketPolicyPolicyPolicyDocument


@cloudformation_dataclass
class ContentLogBucketPolicyPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-logs-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-logs-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class ContentLogBucketPolicyPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-logs-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-logs-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class ContentLogBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ContentLogBucketPolicyPolicyDenyStatement0, ContentLogBucketPolicyPolicyAllowStatement1]


@cloudformation_dataclass
class ContentLogBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(ContentLogBucket)
    policy_document = ContentLogBucketPolicyPolicyPolicyDocument


@cloudformation_dataclass
class ContentReplicaBucketPolicyPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class ContentReplicaBucketPolicyPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class ContentReplicaBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ContentReplicaBucketPolicyPolicyDenyStatement0, ContentReplicaBucketPolicyPolicyAllowStatement1]


@cloudformation_dataclass
class ContentReplicaBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(ContentReplicaBucket)
    policy_document = ContentReplicaBucketPolicyPolicyPolicyDocument
