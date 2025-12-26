"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    ARN_LIKE,
    BOOL,
    DenyStatement,
    Parameter,
    PolicyDocument,
    PolicyStatement,
    STRING,
    STRING_EQUALS,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import iam, s3, sqs
from cloudformation_dataclasses.aws.s3 import (
    ObjectLockEnabled,
    ObjectLockRetentionMode,
    ReplicationRuleStatus,
    ServerSideEncryption,
)
from cloudformation_dataclasses.intrinsics import AWS_ACCOUNT_ID, Sub
from .params import *  # noqa: F403, F401

from .messaging import TestQ as TestQ
from .params import AppName as AppName
from .security import StorageReplicationPolicy as StorageReplicationPolicy
from .security import StorageReplicationPolicyAllowStatement0 as StorageReplicationPolicyAllowStatement0
from .security import StorageReplicationPolicyAllowStatement1 as StorageReplicationPolicyAllowStatement1
from .security import StorageReplicationPolicyAllowStatement2 as StorageReplicationPolicyAllowStatement2
from .security import StorageReplicationPolicyPolicyDocument as StorageReplicationPolicyPolicyDocument
from .security import StorageReplicationRole as StorageReplicationRole
from .security import StorageReplicationRoleAllowStatement0 as StorageReplicationRoleAllowStatement0
from .security import StorageReplicationRoleAssumeRolePolicyDocument as StorageReplicationRoleAssumeRolePolicyDocument
from .storage import StorageBucket as StorageBucket
from .storage import StorageBucketBucketEncryption as StorageBucketBucketEncryption
from .storage import StorageBucketDeleteMarkerReplication as StorageBucketDeleteMarkerReplication
from .storage import StorageBucketLoggingConfiguration as StorageBucketLoggingConfiguration
from .storage import StorageBucketPolicyPolicy as StorageBucketPolicyPolicy
from .storage import StorageBucketPolicyPolicyAllowStatement1 as StorageBucketPolicyPolicyAllowStatement1
from .storage import StorageBucketPolicyPolicyDenyStatement0 as StorageBucketPolicyPolicyDenyStatement0
from .storage import StorageBucketPolicyPolicyPolicyDocument as StorageBucketPolicyPolicyPolicyDocument
from .storage import StorageBucketPublicAccessBlockConfiguration as StorageBucketPublicAccessBlockConfiguration
from .storage import StorageBucketReplicationConfiguration as StorageBucketReplicationConfiguration
from .storage import StorageBucketReplicationDestination as StorageBucketReplicationDestination
from .storage import StorageBucketReplicationRule as StorageBucketReplicationRule
from .storage import StorageBucketServerSideEncryptionByDefault as StorageBucketServerSideEncryptionByDefault
from .storage import StorageBucketServerSideEncryptionRule as StorageBucketServerSideEncryptionRule
from .storage import StorageLogBucket as StorageLogBucket
from .storage import StorageLogBucketBucketEncryption as StorageLogBucketBucketEncryption
from .storage import StorageLogBucketDefaultRetention as StorageLogBucketDefaultRetention
from .storage import StorageLogBucketDeleteMarkerReplication as StorageLogBucketDeleteMarkerReplication
from .storage import StorageLogBucketObjectLockConfiguration as StorageLogBucketObjectLockConfiguration
from .storage import StorageLogBucketObjectLockRule as StorageLogBucketObjectLockRule
from .storage import StorageLogBucketPolicyPolicy as StorageLogBucketPolicyPolicy
from .storage import StorageLogBucketPolicyPolicyAllowStatement1 as StorageLogBucketPolicyPolicyAllowStatement1
from .storage import StorageLogBucketPolicyPolicyDenyStatement0 as StorageLogBucketPolicyPolicyDenyStatement0
from .storage import StorageLogBucketPolicyPolicyPolicyDocument as StorageLogBucketPolicyPolicyPolicyDocument
from .storage import StorageLogBucketPublicAccessBlockConfiguration as StorageLogBucketPublicAccessBlockConfiguration
from .storage import StorageLogBucketServerSideEncryptionByDefault as StorageLogBucketServerSideEncryptionByDefault
from .storage import StorageLogBucketServerSideEncryptionRule as StorageLogBucketServerSideEncryptionRule
from .storage import StorageReplicaBucket as StorageReplicaBucket
from .storage import StorageReplicaBucketBucketEncryption as StorageReplicaBucketBucketEncryption
from .storage import StorageReplicaBucketDeleteMarkerReplication as StorageReplicaBucketDeleteMarkerReplication
from .storage import StorageReplicaBucketPolicyPolicy as StorageReplicaBucketPolicyPolicy
from .storage import StorageReplicaBucketPolicyPolicyAllowStatement1 as StorageReplicaBucketPolicyPolicyAllowStatement1
from .storage import StorageReplicaBucketPolicyPolicyDenyStatement0 as StorageReplicaBucketPolicyPolicyDenyStatement0
from .storage import StorageReplicaBucketPolicyPolicyPolicyDocument as StorageReplicaBucketPolicyPolicyPolicyDocument
from .storage import StorageReplicaBucketPublicAccessBlockConfiguration as StorageReplicaBucketPublicAccessBlockConfiguration
from .storage import StorageReplicaBucketServerSideEncryptionByDefault as StorageReplicaBucketServerSideEncryptionByDefault
from .storage import StorageReplicaBucketServerSideEncryptionRule as StorageReplicaBucketServerSideEncryptionRule

__all__: list[str] = ['ARN_LIKE', 'AWS_ACCOUNT_ID', 'AppName', 'BOOL', 'DenyStatement', 'ObjectLockEnabled', 'ObjectLockRetentionMode', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'ReplicationRuleStatus', 'STRING', 'STRING_EQUALS', 'ServerSideEncryption', 'StorageBucket', 'StorageBucketBucketEncryption', 'StorageBucketDeleteMarkerReplication', 'StorageBucketLoggingConfiguration', 'StorageBucketPolicyPolicy', 'StorageBucketPolicyPolicyAllowStatement1', 'StorageBucketPolicyPolicyDenyStatement0', 'StorageBucketPolicyPolicyPolicyDocument', 'StorageBucketPublicAccessBlockConfiguration', 'StorageBucketReplicationConfiguration', 'StorageBucketReplicationDestination', 'StorageBucketReplicationRule', 'StorageBucketServerSideEncryptionByDefault', 'StorageBucketServerSideEncryptionRule', 'StorageLogBucket', 'StorageLogBucketBucketEncryption', 'StorageLogBucketDefaultRetention', 'StorageLogBucketDeleteMarkerReplication', 'StorageLogBucketObjectLockConfiguration', 'StorageLogBucketObjectLockRule', 'StorageLogBucketPolicyPolicy', 'StorageLogBucketPolicyPolicyAllowStatement1', 'StorageLogBucketPolicyPolicyDenyStatement0', 'StorageLogBucketPolicyPolicyPolicyDocument', 'StorageLogBucketPublicAccessBlockConfiguration', 'StorageLogBucketServerSideEncryptionByDefault', 'StorageLogBucketServerSideEncryptionRule', 'StorageReplicaBucket', 'StorageReplicaBucketBucketEncryption', 'StorageReplicaBucketDeleteMarkerReplication', 'StorageReplicaBucketPolicyPolicy', 'StorageReplicaBucketPolicyPolicyAllowStatement1', 'StorageReplicaBucketPolicyPolicyDenyStatement0', 'StorageReplicaBucketPolicyPolicyPolicyDocument', 'StorageReplicaBucketPublicAccessBlockConfiguration', 'StorageReplicaBucketServerSideEncryptionByDefault', 'StorageReplicaBucketServerSideEncryptionRule', 'StorageReplicationPolicy', 'StorageReplicationPolicyAllowStatement0', 'StorageReplicationPolicyAllowStatement1', 'StorageReplicationPolicyAllowStatement2', 'StorageReplicationPolicyPolicyDocument', 'StorageReplicationRole', 'StorageReplicationRoleAllowStatement0', 'StorageReplicationRoleAssumeRolePolicyDocument', 'Sub', 'Template', 'TestQ', 'cloudformation_dataclass', 'get_att', 'iam', 'ref', 's3', 'setup_resources', 'sqs']
