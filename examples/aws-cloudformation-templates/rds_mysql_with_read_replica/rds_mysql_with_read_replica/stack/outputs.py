"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DBCredentialSecretNameArnOutput:
    """Name of the secret containing the database credential"""

    resource: Output
    value = ref(DBCredential)
    description = 'Name of the secret containing the database credential'


@cloudformation_dataclass
class EC2PlatformOutput:
    """Platform in which this stack is deployed"""

    resource: Output
    value = If("IsEC2VPC", 'true', 'EC2VPC')
    description = 'Platform in which this stack is deployed'


@cloudformation_dataclass
class JDBCConnectionStringOutput:
    """JDBC connection string for the master database"""

    resource: Output
    value = Join('', [
    'jdbc:mysql://',
    get_att(MainDB, "Endpoint.Address"),
    ':',
    get_att(MainDB, "Endpoint.Port"),
    '/',
    ref(DBName),
])
    description = 'JDBC connection string for the master database'


@cloudformation_dataclass
class ReplicaJDBCConnectionStringOutput:
    """JDBC connection string for the replica database"""

    resource: Output
    value = Join('', [
    'jdbc:mysql://',
    get_att(ReplicaDB, "Endpoint.Address"),
    ':',
    get_att(ReplicaDB, "Endpoint.Port"),
    '/',
    ref(DBName),
])
    description = 'JDBC connection string for the replica database'
    condition = 'EnableReadReplica'
