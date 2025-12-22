from __future__ import annotations

"""ADSAMLAuthDistinctUsers - AWS::Logs::QueryDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADSAMLAuthDistinctUsers:
    """AWS::Logs::QueryDefinition resource."""

    resource: QueryDefinition
    name = Sub('${Folder}/AD or SAML Auth Distinct Users')
    query_string = """fields @timestamp, `client-vpn-endpoint-id`, `username` 
| sort @timestamp asc 
| stats count(*) as connection_count, 
  latest(`client-vpn-endpoint-id`) as client_vpn_endpoint_id 
by `username`
"""
