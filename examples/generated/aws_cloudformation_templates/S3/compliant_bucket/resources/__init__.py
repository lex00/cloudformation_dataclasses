"""Resource definitions - re-exports all resources."""
from .object_storage_log_bucket import ObjectStorageLogBucket
from .object_storage_replication_role import ObjectStorageReplicationRole
from .object_storage_replica_bucket import ObjectStorageReplicaBucket
from .object_storage_bucket import ObjectStorageBucket
from .object_storage_bucket_policy_policy import ObjectStorageBucketPolicyPolicy
from .object_storage_log_bucket_policy_policy import ObjectStorageLogBucketPolicyPolicy
from .object_storage_replica_bucket_policy_policy import ObjectStorageReplicaBucketPolicyPolicy
from .object_storage_replication_policy import ObjectStorageReplicationPolicy

__all__ = [
    "ObjectStorageLogBucket",
    "ObjectStorageReplicationRole",
    "ObjectStorageReplicaBucket",
    "ObjectStorageBucket",
    "ObjectStorageBucketPolicyPolicy",
    "ObjectStorageLogBucketPolicyPolicy",
    "ObjectStorageReplicaBucketPolicyPolicy",
    "ObjectStorageReplicationPolicy",
]
