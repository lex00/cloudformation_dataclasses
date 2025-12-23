"""ADSAMLAuthTotalUsageReport - AWS::Logs::QueryDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADSAMLAuthTotalUsageReport:
    """AWS::Logs::QueryDefinition resource."""

    resource: logs.QueryDefinition
    name = Sub('${Folder}/AD or SAML Auth Total Usage Report')
    query_string = """fields @timestamp, `client-vpn-endpoint-id`, `username`, `ingress-bytes`, `egress-bytes`, `connection-start-time`, `connection-end-time`, `connection-duration-seconds` 
| sort @timestamp asc 
| filter `ingress-bytes` > 0 OR `egress-bytes` > 0 
| fields @timestamp, `client-vpn-endpoint-id`, `username`, `ingress-bytes`, `egress-bytes`, `connection-start-time`, `connection-end-time`, `connection-duration-seconds`, (`connection-duration-seconds`/60) as connection_time_minutes 
| sort by `ingress-bytes` desc, `egress-bytes` desc
"""
