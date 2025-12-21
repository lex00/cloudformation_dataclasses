"""ObjectStorageReplicationPolicy - AWS::IAM::RolePolicy resource."""

from .. import *  # noqa: F403
from ..config import AppName
from .object_storage_bucket import ObjectStorageBucket
from .object_storage_replica_bucket import ObjectStorageReplicaBucket
from .object_storage_replication_role import ObjectStorageReplicationRole


@cloudformation_dataclass
class ObjectStorageReplicationPolicy:
    """AWS::IAM::RolePolicy resource."""

    resource: RolePolicy
    policy_document = PolicyDocument(statement=[
            PolicyStatement(action=[
                    's3:GetReplicationConfiguration',
                    's3:ListBucket',
                ], resource_arn=get_att(ObjectStorageBucket, ARN)),
            PolicyStatement(action=[
                    's3:GetObjectVersionForReplication',
                    's3:GetObjectVersionAcl',
                    's3:GetObjectVersionTagging',
                ], resource_arn=Join('', [get_att(ObjectStorageBucket, ARN), '/*'])),
            PolicyStatement(action=[
                    's3:ReplicateObject',
                    's3:ReplicateDelete',
                    's3:ReplicationTags',
                ], resource_arn=Join('', [get_att(ObjectStorageReplicaBucket, ARN), '/*'])),
        ])
    policy_name = 'bucket-replication-policy'
    role_name = ref(ObjectStorageReplicationRole)
