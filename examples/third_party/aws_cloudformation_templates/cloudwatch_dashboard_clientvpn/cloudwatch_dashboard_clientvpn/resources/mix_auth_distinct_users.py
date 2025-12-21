from __future__ import annotations

"""MixAuthDistinctUsers - AWS::Logs::QueryDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MixAuthDistinctUsers:
    """AWS::Logs::QueryDefinition resource."""

    resource: QueryDefinition
    name = Sub('${Folder}/Mix Auth Distinct Users')
    query_string = """fields @timestamp, `client-vpn-endpoint-id`, `common-name`, `username`
| sort @timestamp asc
| stats count(*) as connection_count,
  latest(`client-vpn-endpoint-id`) as client_vpn_endpoint_id
by `username`, `common-name`
"""
