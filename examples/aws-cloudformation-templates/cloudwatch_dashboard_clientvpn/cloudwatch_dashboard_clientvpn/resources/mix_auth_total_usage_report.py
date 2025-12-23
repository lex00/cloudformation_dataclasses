"""MixAuthTotalUsageReport - AWS::Logs::QueryDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MixAuthTotalUsageReport:
    """AWS::Logs::QueryDefinition resource."""

    resource: QueryDefinition
    name = Sub('${Folder}/Mix Auth Total Usage Report')
    query_string = """fields @timestamp, `client-vpn-endpoint-id`, `username`, `common-name`, `ingress-bytes`, `egress-bytes`, `connection-start-time`, `connection-end-time`, `connection-duration-seconds` 
| sort @timestamp asc
| filter `ingress-bytes` > 0 OR `egress-bytes` > 0
| fields @timestamp, `client-vpn-endpoint-id`, `username`, `common-name`, `ingress-bytes`, `egress-bytes`, `connection-start-time`, `connection-end-time`, `connection-duration-seconds`, (`connection-duration-seconds`/60) as connection_time_minutes 
| sort by `ingress-bytes` desc, `egress-bytes` desc
"""
