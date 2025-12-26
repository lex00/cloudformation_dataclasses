"""Stack resources."""

from . import *  # noqa: F403


@cloudformation_dataclass
class EnableShapshotTrigger:
    """Custom::Region resource."""

    # Unknown resource type: Custom::Region
    resource: CloudFormationResource
    service_token = get_att(EnableShapshot, "Arn")
    ss_cluster_id = ref(RedisReplicationGroup)
    ss_window = ref(SnapshotWindow)
    ss_retention_limit = ref(SnapshotRetentionLimit)
    depends_on = [EnableShapshot, LambdaExecutePermission, RedisReplicationGroup]
    condition = 'EnableBackups'
