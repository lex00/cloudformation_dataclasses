"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class JDBCConnectionStringOutput:
    """JDBC connection string for the database"""

    resource: Output
    value = Join('', [
    'jdbc:mysql://',
    get_att("MyDB", "Endpoint.Address"),
    ':',
    get_att("MyDB", "Endpoint.Port"),
    '/',
    ref(DBName),
])
    description = 'JDBC connection string for the database'
