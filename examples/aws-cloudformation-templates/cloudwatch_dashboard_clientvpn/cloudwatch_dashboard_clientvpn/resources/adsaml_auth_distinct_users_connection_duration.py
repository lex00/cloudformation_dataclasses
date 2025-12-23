"""ADSAMLAuthDistinctUsersConnectionDuration - AWS::Logs::QueryDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADSAMLAuthDistinctUsersConnectionDuration:
    """AWS::Logs::QueryDefinition resource."""

    resource: logs.QueryDefinition
    name = Sub('${Folder}/AD or SAML Auth Distinct Users Connection Duration')
    query_string = """fields @timestamp, `client-vpn-endpoint-id`, `username`, `ingress-bytes`, `egress-bytes`, `connection-start-time`, `connection-end-time`, `connection-duration-seconds` 
| sort @timestamp asc 
| filter `ingress-bytes` > 0 OR `egress-bytes` > 0 
| stats count(*) as connection_count, 
  sum(`connection-duration-seconds`/60) as total_connection_time_minutes, 
  sum(`ingress-bytes`) as total_ingress_bytes, 
  sum(`egress-bytes`) as total_egress_bytes, 
  latest(`client-vpn-endpoint-id`) as client_vpn_endpoint_id 
by `username` 
| sort by total_ingress_bytes desc, total_egress_bytes desc
"""
