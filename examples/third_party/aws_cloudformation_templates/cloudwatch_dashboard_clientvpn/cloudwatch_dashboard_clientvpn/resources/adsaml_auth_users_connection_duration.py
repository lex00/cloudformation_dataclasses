from __future__ import annotations

"""ADSAMLAuthUsersConnectionDuration - AWS::Logs::QueryDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADSAMLAuthUsersConnectionDuration:
    """AWS::Logs::QueryDefinition resource."""

    resource: QueryDefinition
    name = Sub('${Folder}/AD or SAML Auth Users Connection Duration')
    query_string = """fields @timestamp, `client-vpn-endpoint-id`, `username`, `ingress-bytes`, `egress-bytes`, `connection-start-time`, `connection-end-time`, `connection-duration-seconds` 
| sort @timestamp asc 
| filter `ingress-bytes` > 0 OR `egress-bytes` > 0 
| stats count(*) as connection_count, 
  sum(`connection-duration-seconds`/60) as total_connection_time_minutes 
by `username` 
| sort by total_connection_time_minutes desc
"""
