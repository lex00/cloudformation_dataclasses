"""Stack outputs."""

from .. import *  # noqa: F403, F401
from rds import *  # noqa: F403, F401

DbEndpointOutput = Output(
    value=get_att(PostgresInstance, "Endpoint.Address"),
    description="RDS instance endpoint address",
)

DbPortOutput = Output(
    value=get_att(PostgresInstance, "Endpoint.Port"),
    description="RDS instance endpoint port",
)

DbSecretArnOutput = Output(
    value=ref(DbSecret),
    description="ARN of the Secrets Manager secret",
)

DbSecurityGroupIdOutput = Output(
    value=ref(DbSecurityGroup),
    description="Security group ID for RDS",
)
