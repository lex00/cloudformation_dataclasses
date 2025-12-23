"""TotalUsagePerClientVPNEndpoint - AWS::Logs::QueryDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TotalUsagePerClientVPNEndpoint:
    """AWS::Logs::QueryDefinition resource."""

    resource: logs.QueryDefinition
    name = Sub('${Folder}/Total Usage per Client VPN Endpoint')
    query_string = """fields @timestamp, `client-vpn-endpoint-id`, `ingress-bytes`, `egress-bytes`, `connection-duration-seconds`, `username`, `common-name`
| sort @timestamp asc
| filter `ingress-bytes` > 0 OR `egress-bytes` > 0
| stats
    count(*) as connection_count,
    min(@timestamp) as earliest_timestamp,
    max(@timestamp) as latest_timestamp,
    sum(`ingress-bytes`)/1048576 as total_ingress_MB,
    sum(`egress-bytes`)/1048576 as total_egress_MB,
    sum((`connection-duration-seconds`/60)/60) as total_connection_time_hours,
    count_distinct(username) as unique_saml_ad_users,
    count_distinct(`common-name`) as unique_mutual_auth_names
by `client-vpn-endpoint-id`
| sort by total_ingress_MB desc, total_egress_MB desc
"""
