"""MutualAuthDistinctUsers - AWS::Logs::QueryDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MutualAuthDistinctUsers:
    """AWS::Logs::QueryDefinition resource."""

    resource: QueryDefinition
    name = Sub('${Folder}/Mutual Auth Distinct Users')
    query_string = """fields @timestamp, `client-vpn-endpoint-id`, `common-name`
| sort @timestamp asc
| stats count(*) as connection_count, latest(`client-vpn-endpoint-id`) as client_vpn_endpoint_id by `common-name`
"""
