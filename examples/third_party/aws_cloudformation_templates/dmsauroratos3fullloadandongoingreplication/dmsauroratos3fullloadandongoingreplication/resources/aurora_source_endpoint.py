"""AuroraSourceEndpoint - AWS::DMS::Endpoint resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AuroraSourceEndpoint:
    """AWS::DMS::Endpoint resource."""

    resource: dms.Endpoint
    endpoint_type = 'source'
    engine_name = 'AURORA'
    password = '{{resolve:secretsmanager:aurora-source-enpoint-password:SecretString:password}}'
    port = 3306
    server_name = get_att(AuroraCluster, "Endpoint.Address")
    username = 'admin'
    depends_on = ["DMSReplicationInstance", "AuroraCluster", "AuroraDB"]
