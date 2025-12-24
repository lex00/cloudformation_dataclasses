"""Parameters, Mappings, and Conditions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class RedisNodeType:
    """elasticache Redis Node Instance Type"""

    resource: Parameter
    type = STRING
    description = 'elasticache Redis Node Instance Type'
    default = 'cache.m3.medium'
    allowed_values = ['cache.m3.medium']
    constraint_description = 'must be an m3.medium - the least costly machine that can use a Replication Group.'


@cloudformation_dataclass
class EnableSnapshotting:
    """elasticache snapshot enable"""

    resource: Parameter
    type = STRING
    description = 'elasticache snapshot enable'
    default = 'True'
    allowed_values = [
    'True',
    'False',
]


@cloudformation_dataclass
class SnapshotRetentionLimit:
    """elasticache Snapshot Retention Limit"""

    resource: Parameter
    type = STRING
    description = 'elasticache Snapshot Retention Limit'
    default = '28'


@cloudformation_dataclass
class SnapshotWindow:
    """Snapshot Window"""

    resource: Parameter
    type = STRING
    description = 'Snapshot Window'
    default = '02:00-03:00'


@cloudformation_dataclass
class AWSRegion2AZMapping:
    resource: Mapping
    map_data = {
        'us-east-1': {
            'A': 'us-east-1b',
            'B': 'us-east-1c',
            'C': 'us-east-1c',
            'D': 'us-east-1d',
        },
        'us-west-1': {
            'A': 'us-west-1b',
            'B': 'us-west-1c',
        },
        'us-west-2': {
            'A': 'us-west-2a',
            'B': 'us-west-2b',
            'C': 'us-west-2c',
        },
    }


@cloudformation_dataclass
class EnableBackupsCondition:
    resource: Condition
    expression = Equals(ref(EnableSnapshotting), 'True')
