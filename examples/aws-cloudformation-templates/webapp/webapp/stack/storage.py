"""Storage resources: SiteCloudFrontLogsLogBucket, SiteCloudFrontLogsReplicaBucket, SiteCloudFrontLogsBucket, SiteContentLogBucket, SiteContentReplicaBucket, SiteContentBucket, SiteContentLogBucketAccessPolicy, SiteContentBucketAccessPolicy, SiteContentReplicaBucketAccessPolicy, SiteCloudFrontLogsLogBucketAccessPolicy, SiteCloudFrontLogsBucketAccessPolicy, SiteCloudFrontLogsReplicaBucketAccessPolicy."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteCloudFrontLogsLogBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [SiteCloudFrontLogsLogBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketDefaultRetention:
    resource: s3.bucket.DefaultRetention
    mode = ObjectLockRetentionMode.COMPLIANCE
    years = 1


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketObjectLockRule:
    resource: s3.bucket.ObjectLockRule
    default_retention = SiteCloudFrontLogsLogBucketDefaultRetention


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketObjectLockConfiguration:
    resource: s3.bucket.ObjectLockConfiguration
    object_lock_enabled = ObjectLockEnabled.ENABLED
    rule = SiteCloudFrontLogsLogBucketObjectLockRule


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = SiteCloudFrontLogsLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = SiteCloudFrontLogsLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = SiteCloudFrontLogsLogBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteCloudFrontLogsLogBucketDeleteMarkerReplication


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteCloudFrontLogsReplicaBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [SiteCloudFrontLogsReplicaBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = SiteCloudFrontLogsReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = SiteCloudFrontLogsReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteCloudFrontLogsReplicaBucketDeleteMarkerReplication


@cloudformation_dataclass
class SiteCloudFrontLogsBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteCloudFrontLogsBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteCloudFrontLogsBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteCloudFrontLogsBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [SiteCloudFrontLogsBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteCloudFrontLogsBucketLoggingConfiguration:
    resource: s3.bucket.LoggingConfiguration
    destination_bucket_name = ref(SiteCloudFrontLogsLogBucket)


@cloudformation_dataclass
class SiteCloudFrontLogsBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteCloudFrontLogsBucketReplicationDestination:
    resource: s3.bucket.ReplicationDestination
    bucket = get_att(SiteCloudFrontLogsReplicaBucket, "Arn")


@cloudformation_dataclass
class SiteCloudFrontLogsBucketReplicationRule:
    resource: s3.bucket.ReplicationRule
    destination = SiteCloudFrontLogsBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class SiteCloudFrontLogsBucketReplicationConfiguration:
    resource: s3.bucket.ReplicationConfiguration
    role = get_att(SiteCloudFrontLogsReplicationRole, "Arn")
    rules = [SiteCloudFrontLogsBucketReplicationRule]


@cloudformation_dataclass
class SiteCloudFrontLogsBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class SiteCloudFrontLogsBucketOwnershipControlsRule:
    resource: s3.bucket.OwnershipControlsRule
    object_ownership = 'BucketOwnerPreferred'


@cloudformation_dataclass
class SiteCloudFrontLogsBucketOwnershipControls:
    resource: s3.bucket.OwnershipControls
    rules = [SiteCloudFrontLogsBucketOwnershipControlsRule]


@cloudformation_dataclass
class SiteCloudFrontLogsBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = SiteCloudFrontLogsBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = SiteCloudFrontLogsBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = SiteCloudFrontLogsBucketPublicAccessBlockConfiguration
    replication_configuration = SiteCloudFrontLogsBucketReplicationConfiguration
    versioning_configuration = SiteCloudFrontLogsBucketDeleteMarkerReplication
    ownership_controls = SiteCloudFrontLogsBucketOwnershipControls


@cloudformation_dataclass
class SiteContentLogBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteContentLogBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteContentLogBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteContentLogBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [SiteContentLogBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteContentLogBucketDefaultRetention:
    resource: s3.bucket.DefaultRetention
    mode = ObjectLockRetentionMode.COMPLIANCE
    years = 1


@cloudformation_dataclass
class SiteContentLogBucketObjectLockRule:
    resource: s3.bucket.ObjectLockRule
    default_retention = SiteContentLogBucketDefaultRetention


@cloudformation_dataclass
class SiteContentLogBucketObjectLockConfiguration:
    resource: s3.bucket.ObjectLockConfiguration
    object_lock_enabled = ObjectLockEnabled.ENABLED
    rule = SiteContentLogBucketObjectLockRule


@cloudformation_dataclass
class SiteContentLogBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteContentLogBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class SiteContentLogBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = SiteContentLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = SiteContentLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = SiteContentLogBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteContentLogBucketDeleteMarkerReplication


@cloudformation_dataclass
class SiteContentReplicaBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteContentReplicaBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteContentReplicaBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteContentReplicaBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [SiteContentReplicaBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteContentReplicaBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteContentReplicaBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class SiteContentReplicaBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = SiteContentReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = SiteContentReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteContentReplicaBucketDeleteMarkerReplication


@cloudformation_dataclass
class SiteContentBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteContentBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteContentBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteContentBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [SiteContentBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteContentBucketLoggingConfiguration:
    resource: s3.bucket.LoggingConfiguration
    destination_bucket_name = ref(SiteContentLogBucket)


@cloudformation_dataclass
class SiteContentBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteContentBucketReplicationDestination:
    resource: s3.bucket.ReplicationDestination
    bucket = get_att(SiteContentReplicaBucket, "Arn")


@cloudformation_dataclass
class SiteContentBucketReplicationRule:
    resource: s3.bucket.ReplicationRule
    destination = SiteContentBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class SiteContentBucketReplicationConfiguration:
    resource: s3.bucket.ReplicationConfiguration
    role = get_att(SiteContentReplicationRole, "Arn")
    rules = [SiteContentBucketReplicationRule]


@cloudformation_dataclass
class SiteContentBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class SiteContentBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = SiteContentBucketBucketEncryption
    bucket_name = Sub('${AppName}-content-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = SiteContentBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = SiteContentBucketPublicAccessBlockConfiguration
    replication_configuration = SiteContentBucketReplicationConfiguration
    versioning_configuration = SiteContentBucketDeleteMarkerReplication


@cloudformation_dataclass
class SiteContentLogBucketAccessPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class SiteContentLogBucketAccessPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class SiteContentLogBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteContentLogBucketAccessPolicyDenyStatement0, SiteContentLogBucketAccessPolicyAllowStatement1]


@cloudformation_dataclass
class SiteContentLogBucketAccessPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(SiteContentLogBucket)
    policy_document = SiteContentLogBucketAccessPolicyPolicyDocument


@cloudformation_dataclass
class SiteContentBucketAccessPolicyAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'cloudfront.amazonaws.com',
    }
    action = 's3:GetObject'
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*')
    condition = {
        STRING_EQUALS: {
            'AWS:SourceArn': Sub('arn:${AWS::Partition}:cloudfront::${AWS::AccountId}:distribution/${SiteDistribution.Id}'),
        },
    }


@cloudformation_dataclass
class SiteContentBucketAccessPolicyDenyStatement1:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class SiteContentBucketAccessPolicyAllowStatement2:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class SiteContentBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteContentBucketAccessPolicyAllowStatement0, SiteContentBucketAccessPolicyDenyStatement1, SiteContentBucketAccessPolicyAllowStatement2]


@cloudformation_dataclass
class SiteContentBucketAccessPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(SiteContentBucket)
    policy_document = SiteContentBucketAccessPolicyPolicyDocument


@cloudformation_dataclass
class SiteContentReplicaBucketAccessPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


@cloudformation_dataclass
class SiteContentReplicaBucketAccessPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


@cloudformation_dataclass
class SiteContentReplicaBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteContentReplicaBucketAccessPolicyDenyStatement0, SiteContentReplicaBucketAccessPolicyAllowStatement1]


@cloudformation_dataclass
class SiteContentReplicaBucketAccessPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(SiteContentReplicaBucket)
    policy_document = SiteContentReplicaBucketAccessPolicyPolicyDocument


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketAccessPolicyDenyStatement0:
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
class SiteCloudFrontLogsLogBucketAccessPolicyAllowStatement1:
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
class SiteCloudFrontLogsLogBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteCloudFrontLogsLogBucketAccessPolicyDenyStatement0, SiteCloudFrontLogsLogBucketAccessPolicyAllowStatement1]


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketAccessPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(SiteCloudFrontLogsLogBucket)
    policy_document = SiteCloudFrontLogsLogBucketAccessPolicyPolicyDocument


@cloudformation_dataclass
class SiteCloudFrontLogsBucketAccessPolicyDenyStatement0:
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
class SiteCloudFrontLogsBucketAccessPolicyAllowStatement1:
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
class SiteCloudFrontLogsBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteCloudFrontLogsBucketAccessPolicyDenyStatement0, SiteCloudFrontLogsBucketAccessPolicyAllowStatement1]


@cloudformation_dataclass
class SiteCloudFrontLogsBucketAccessPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(SiteCloudFrontLogsBucket)
    policy_document = SiteCloudFrontLogsBucketAccessPolicyPolicyDocument


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketAccessPolicyDenyStatement0:
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
class SiteCloudFrontLogsReplicaBucketAccessPolicyAllowStatement1:
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
class SiteCloudFrontLogsReplicaBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteCloudFrontLogsReplicaBucketAccessPolicyDenyStatement0, SiteCloudFrontLogsReplicaBucketAccessPolicyAllowStatement1]


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketAccessPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(SiteCloudFrontLogsReplicaBucket)
    policy_document = SiteCloudFrontLogsReplicaBucketAccessPolicyPolicyDocument
