"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TestQ:
    """AWS::SQS::Queue resource."""

    resource: sqs.Queue
    queue_name = 'test-events17'


@cloudformation_dataclass
class StorageLogBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class StorageLogBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = StorageLogBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class StorageLogBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [StorageLogBucketServerSideEncryptionRule]


@cloudformation_dataclass
class StorageLogBucketDefaultRetention:
    resource: s3.bucket.DefaultRetention
    mode = ObjectLockRetentionMode.COMPLIANCE
    years = 1


@cloudformation_dataclass
class StorageLogBucketObjectLockRule:
    resource: s3.bucket.ObjectLockRule
    default_retention = StorageLogBucketDefaultRetention


@cloudformation_dataclass
class StorageLogBucketObjectLockConfiguration:
    resource: s3.bucket.ObjectLockConfiguration
    object_lock_enabled = ObjectLockEnabled.ENABLED
    rule = StorageLogBucketObjectLockRule


@cloudformation_dataclass
class StorageLogBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class StorageLogBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class StorageLogBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = StorageLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = StorageLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = StorageLogBucketPublicAccessBlockConfiguration
    versioning_configuration = StorageLogBucketDeleteMarkerReplication


@cloudformation_dataclass
class StorageReplicationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class StorageReplicationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [StorageReplicationRoleAllowStatement0]


@cloudformation_dataclass
class StorageReplicationRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = StorageReplicationRoleAssumeRolePolicyDocument
    path = '/'


@cloudformation_dataclass
class StorageReplicaBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class StorageReplicaBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = StorageReplicaBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class StorageReplicaBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [StorageReplicaBucketServerSideEncryptionRule]


@cloudformation_dataclass
class StorageReplicaBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class StorageReplicaBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class StorageReplicaBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = StorageReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = StorageReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = StorageReplicaBucketDeleteMarkerReplication


@cloudformation_dataclass
class StorageBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class StorageBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = StorageBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class StorageBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [StorageBucketServerSideEncryptionRule]


@cloudformation_dataclass
class StorageBucketLoggingConfiguration:
    resource: s3.bucket.LoggingConfiguration
    destination_bucket_name = ref(StorageLogBucket)


@cloudformation_dataclass
class StorageBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class StorageBucketReplicationDestination:
    resource: s3.bucket.ReplicationDestination
    bucket = get_att(StorageReplicaBucket, "Arn")


@cloudformation_dataclass
class StorageBucketReplicationRule:
    resource: s3.bucket.ReplicationRule
    destination = StorageBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class StorageBucketReplicationConfiguration:
    resource: s3.bucket.ReplicationConfiguration
    role = get_att(StorageReplicationRole, "Arn")
    rules = [StorageBucketReplicationRule]


@cloudformation_dataclass
class StorageBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class StorageBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = StorageBucketBucketEncryption
    bucket_name = Sub('${AppName}-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = StorageBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = StorageBucketPublicAccessBlockConfiguration
    replication_configuration = StorageBucketReplicationConfiguration
    versioning_configuration = StorageBucketDeleteMarkerReplication


@cloudformation_dataclass
class StorageReplicationPolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}')


@cloudformation_dataclass
class StorageReplicationPolicyAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}/*')


@cloudformation_dataclass
class StorageReplicationPolicyAllowStatement2:
    resource: PolicyStatement
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}/*')


@cloudformation_dataclass
class StorageReplicationPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [StorageReplicationPolicyAllowStatement0, StorageReplicationPolicyAllowStatement1, StorageReplicationPolicyAllowStatement2]


@cloudformation_dataclass
class StorageReplicationPolicy:
    """AWS::IAM::RolePolicy resource."""

    resource: iam.RolePolicy
    policy_document = StorageReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = ref(StorageReplicationRole)


@cloudformation_dataclass
class StorageLogBucketPolicyPolicyDenyStatement0:
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
class StorageLogBucketPolicyPolicyAllowStatement1:
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
class StorageLogBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [StorageLogBucketPolicyPolicyDenyStatement0, StorageLogBucketPolicyPolicyAllowStatement1]


@cloudformation_dataclass
class StorageLogBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(StorageLogBucket)
    policy_document = StorageLogBucketPolicyPolicyPolicyDocument


@cloudformation_dataclass
class StorageBucketPolicyPolicyDenyStatement0:
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
class StorageBucketPolicyPolicyAllowStatement1:
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
class StorageBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [StorageBucketPolicyPolicyDenyStatement0, StorageBucketPolicyPolicyAllowStatement1]


@cloudformation_dataclass
class StorageBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(StorageBucket)
    policy_document = StorageBucketPolicyPolicyPolicyDocument


@cloudformation_dataclass
class StorageReplicaBucketPolicyPolicyDenyStatement0:
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
class StorageReplicaBucketPolicyPolicyAllowStatement1:
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
class StorageReplicaBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [StorageReplicaBucketPolicyPolicyDenyStatement0, StorageReplicaBucketPolicyPolicyAllowStatement1]


@cloudformation_dataclass
class StorageReplicaBucketPolicyPolicy:
    """AWS::S3::BucketPolicy resource."""

    resource: s3.BucketPolicy
    bucket = ref(StorageReplicaBucket)
    policy_document = StorageReplicaBucketPolicyPolicyPolicyDocument
