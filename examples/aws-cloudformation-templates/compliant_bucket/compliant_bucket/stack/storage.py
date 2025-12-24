"""Storage resources: ObjectStorageLogBucket, ObjectStorageReplicaBucket, ObjectStorageBucket, ObjectStorageBucketPolicyPolicy, ObjectStorageLogBucketPolicyPolicy, ObjectStorageReplicaBucketPolicyPolicy."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ObjectStorageLogBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class ObjectStorageLogBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = ObjectStorageLogBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class ObjectStorageLogBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [ObjectStorageLogBucketServerSideEncryptionRule]


@cloudformation_dataclass
class ObjectStorageLogBucketDefaultRetention:
    resource: s3.bucket.DefaultRetention
    mode = ObjectLockRetentionMode.COMPLIANCE
    years = 1


@cloudformation_dataclass
class ObjectStorageLogBucketObjectLockRule:
    resource: s3.bucket.ObjectLockRule
    default_retention = ObjectStorageLogBucketDefaultRetention


@cloudformation_dataclass
class ObjectStorageLogBucketObjectLockConfiguration:
    resource: s3.bucket.ObjectLockConfiguration
    object_lock_enabled = ObjectLockEnabled.ENABLED
    rule = ObjectStorageLogBucketObjectLockRule


@cloudformation_dataclass
class ObjectStorageLogBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class ObjectStorageLogBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class ObjectStorageLogBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = ObjectStorageLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = ObjectStorageLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = ObjectStorageLogBucketPublicAccessBlockConfiguration
    versioning_configuration = ObjectStorageLogBucketDeleteMarkerReplication


@cloudformation_dataclass
class ObjectStorageReplicaBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class ObjectStorageReplicaBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = ObjectStorageReplicaBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class ObjectStorageReplicaBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [ObjectStorageReplicaBucketServerSideEncryptionRule]


@cloudformation_dataclass
class ObjectStorageReplicaBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class ObjectStorageReplicaBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class ObjectStorageReplicaBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = ObjectStorageReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = ObjectStorageReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = ObjectStorageReplicaBucketDeleteMarkerReplication


@cloudformation_dataclass
class ObjectStorageBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class ObjectStorageBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = ObjectStorageBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class ObjectStorageBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [ObjectStorageBucketServerSideEncryptionRule]


@cloudformation_dataclass
class ObjectStorageBucketLoggingConfiguration:
    resource: s3.bucket.LoggingConfiguration
    destination_bucket_name = ref(ObjectStorageLogBucket)


@cloudformation_dataclass
class ObjectStorageBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class ObjectStorageBucketReplicationDestination:
    resource: s3.bucket.ReplicationDestination
    bucket = get_att(ObjectStorageReplicaBucket, "Arn")


@cloudformation_dataclass
class ObjectStorageBucketReplicationRule:
    resource: s3.bucket.ReplicationRule
    destination = ObjectStorageBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class ObjectStorageBucketReplicationConfiguration:
    resource: s3.bucket.ReplicationConfiguration
    role = get_att(ObjectStorageReplicationRole, "Arn")
    rules = [ObjectStorageBucketReplicationRule]


@cloudformation_dataclass
class ObjectStorageBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class ObjectStorageBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = ObjectStorageBucketBucketEncryption
    bucket_name = Sub('${AppName}-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = ObjectStorageBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = ObjectStorageBucketPublicAccessBlockConfiguration
    replication_configuration = ObjectStorageBucketReplicationConfiguration
    versioning_configuration = ObjectStorageBucketDeleteMarkerReplication


@cloudformation_dataclass
class ObjectStorageBucketPolicyPolicyDenyStatement0:
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
class ObjectStorageBucketPolicyPolicyAllowStatement1:
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
class ObjectStorageBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ObjectStorageBucketPolicyPolicyDenyStatement0, ObjectStorageBucketPolicyPolicyAllowStatement1]


@cloudformation_dataclass
class ObjectStorageBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(ObjectStorageBucket)
    policy_document = ObjectStorageBucketPolicyPolicyPolicyDocument


@cloudformation_dataclass
class ObjectStorageLogBucketPolicyPolicyDenyStatement0:
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
class ObjectStorageLogBucketPolicyPolicyAllowStatement1:
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
class ObjectStorageLogBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ObjectStorageLogBucketPolicyPolicyDenyStatement0, ObjectStorageLogBucketPolicyPolicyAllowStatement1]


@cloudformation_dataclass
class ObjectStorageLogBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(ObjectStorageLogBucket)
    policy_document = ObjectStorageLogBucketPolicyPolicyPolicyDocument


@cloudformation_dataclass
class ObjectStorageReplicaBucketPolicyPolicyDenyStatement0:
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
class ObjectStorageReplicaBucketPolicyPolicyAllowStatement1:
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
class ObjectStorageReplicaBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ObjectStorageReplicaBucketPolicyPolicyDenyStatement0, ObjectStorageReplicaBucketPolicyPolicyAllowStatement1]


@cloudformation_dataclass
class ObjectStorageReplicaBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(ObjectStorageReplicaBucket)
    policy_document = ObjectStorageReplicaBucketPolicyPolicyPolicyDocument
