"""Database resources: RedisParameterGroup, RedisSubnetGroup, RedisReplicationGroup."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class RedisParameterGroup:
    """AWS::ElastiCache::ParameterGroup resource."""

    resource: elasticache.ParameterGroup
    cache_parameter_group_family = 'redis2.8'
    description = 'RedisParameterGroup'


@cloudformation_dataclass
class RedisSubnetGroup:
    """AWS::ElastiCache::SubnetGroup resource."""

    resource: elasticache.SubnetGroup
    description = 'RedisSubnetGroup'
    subnet_ids = [ref(PublicSubnetA), ref(PublicSubnetB)]


@cloudformation_dataclass
class RedisReplicationGroup:
    """AWS::ElastiCache::ReplicationGroup resource."""

    resource: elasticache.ReplicationGroup
    automatic_failover_enabled = 'true'
    cache_node_type = ref(RedisNodeType)
    cache_parameter_group_name = ref(RedisParameterGroup)
    cache_subnet_group_name = ref(RedisSubnetGroup)
    engine = 'redis'
    engine_version = '2.8.24'
    num_cache_clusters = '2'
    preferred_cache_cluster_a_zs = [FindInMap("AWSRegion2AZ", AWS_REGION, 'A'), FindInMap("AWSRegion2AZ", AWS_REGION, 'B')]
    replication_group_description = 'RedisReplicationGroup'
    security_group_ids = [ref(RedisSecurityGroup)]
