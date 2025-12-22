"""Dashboard - AWS::CloudWatch::Dashboard resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Dashboard:
    """AWS::CloudWatch::Dashboard resource."""

    resource: cloudwatch.Dashboard
    dashboard_name = Sub('${AWS::Region}-AWS-ClientVPN-Usage-Dashboard')
    dashboard_body = Sub("""{
  "widgets": [
    {
      "type": "log",
      "x": 0,
      "y": 0,
      "width": 24,
      "height": 6,
      "properties": {
        "query": "SOURCE '${ClientVPNLogGroup}' | fields @timestamp, `client-vpn-endpoint-id`, `ingress-bytes`, `egress-bytes`, `connection-duration-seconds`, `username`, `common-name` | sort @timestamp asc | filter `ingress-bytes` > 0 OR `egress-bytes` > 0 | stats count(*) as connection_count, min(@timestamp) as earliest_timestamp, max(@timestamp) as latest_timestamp, sum(`ingress-bytes`)/1048576 as total_ingress_MB, sum(`egress-bytes`)/1048576 as total_egress_MB, sum((`connection-duration-seconds`/60)/60) as total_connection_time_hours, count_distinct(username) as unique_saml_ad_users, count_distinct(`common-name`) as unique_mutual_auth_names by `client-vpn-endpoint-id` | sort by total_ingress_MB desc, total_egress_MB desc",
        "region": "${AWS::Region}",
        "title": "Total Usage per Client VPN Endpoint",
        "view": "table"
      }
    },
    {
      "type": "log",
      "x": 0,
      "y": 6,
      "width": 24,
      "height": 6,
      "properties": {
        "query": "SOURCE '${ClientVPNLogGroup}' | fields @timestamp, `client-vpn-endpoint-id`, `username`, `ingress-bytes`, `egress-bytes`, `connection-start-time`, `connection-end-time`, `connection-duration-seconds` | sort @timestamp asc | filter `ingress-bytes` > 0 OR `egress-bytes` > 0 | fields @timestamp, `client-vpn-endpoint-id`, `username`, `ingress-bytes`, `egress-bytes`, `connection-start-time`, `connection-end-time`, `connection-duration-seconds`, (`connection-duration-seconds`/60) as connection_time_minutes | sort by `ingress-bytes` desc, `egress-bytes` desc",
        "region": "${AWS::Region}",
        "title": "AD or SAML Auth Total Usage Report",
        "view": "table"
      }
    },
    {
      "type": "log",
      "x": 0,
      "y": 12,
      "width": 24,
      "height": 6,
      "properties": {
        "query": "SOURCE '${ClientVPNLogGroup}' | fields @timestamp, `client-vpn-endpoint-id`, `username`, `ingress-bytes`, `egress-bytes`, `connection-start-time`, `connection-end-time`, `connection-duration-seconds` | sort @timestamp asc | filter `ingress-bytes` > 0 OR `egress-bytes` > 0 | stats count(*) as connection_count, sum(`connection-duration-seconds`/60) as total_connection_time_minutes, sum(`ingress-bytes`) as total_ingress_bytes, sum(`egress-bytes`) as total_egress_bytes, latest(`client-vpn-endpoint-id`) as client_vpn_endpoint_id by `username` | sort by total_ingress_bytes desc, total_egress_bytes desc",
        "region": "${AWS::Region}",
        "title": "AD or SAML Auth Distinct Users Connection Duration",
        "view": "table"
      }
    },
    {
      "type": "log",
      "x": 0,
      "y": 18,
      "width": 24,
      "height": 6,
      "properties": {
        "query": "SOURCE '${ClientVPNLogGroup}' | fields @timestamp, `client-vpn-endpoint-id`, `username` | sort @timestamp asc | stats count(*) as connection_count, latest(`client-vpn-endpoint-id`) as client_vpn_endpoint_id by `username`",
        "region": "${AWS::Region}",
        "title": "AD or SAML Auth Distinct Users",
        "view": "table"
      }
    },
    {
      "type": "log",
      "x": 0,
      "y": 24,
      "width": 24,
      "height": 6,
      "properties": {
        "query": "SOURCE '${ClientVPNLogGroup}' | fields @timestamp, `client-vpn-endpoint-id`, `username`, `ingress-bytes`, `egress-bytes`, `connection-start-time`, `connection-end-time`, `connection-duration-seconds` | sort @timestamp asc | filter `ingress-bytes` > 0 OR `egress-bytes` > 0 | stats count(*) as connection_count, sum(`connection-duration-seconds`/60) as total_connection_time_minutes by `username` | sort by total_connection_time_minutes desc",
        "region": "${AWS::Region}",
        "title": "AD or SAML Auth Users Connection Duration",
        "view": "table"
      }
    },
    {
      "type": "log",
      "x": 0,
      "y": 30,
      "width": 24,
      "height": 6,
      "properties": {
        "query": "SOURCE '${ClientVPNLogGroup}' | fields @timestamp, `client-vpn-endpoint-id`, `common-name`, `ingress-bytes`, `egress-bytes`, `connection-start-time`, `connection-end-time`, `connection-duration-seconds` | sort @timestamp asc | filter `ingress-bytes` > 0 OR `egress-bytes` > 0 | fields @timestamp, `client-vpn-endpoint-id`, `common-name`, `ingress-bytes`, `egress-bytes`, `connection-start-time`, `connection-end-time`, `connection-duration-seconds`, (`connection-duration-seconds`/60) as connection_time_minutes | sort by `ingress-bytes` desc, `egress-bytes` desc",
        "region": "${AWS::Region}",
        "title": "Mutual Auth Total Usage Report",
        "view": "table"
      }
    },
    {
      "type": "log",
      "x": 0,
      "y": 36,
      "width": 24,
      "height": 6,
      "properties": {
        "query": "SOURCE '${ClientVPNLogGroup}' | fields @timestamp, `client-vpn-endpoint-id`, `common-name`, `ingress-bytes`, `egress-bytes`, `connection-duration-seconds` | sort @timestamp asc | filter `ingress-bytes` > 0 OR `egress-bytes` > 0 | stats count(*) as connection_count, sum(`connection-duration-seconds`/60) as total_connection_time_minutes, sum(`ingress-bytes`) as total_ingress_bytes, sum(`egress-bytes`) as total_egress_bytes, latest(`client-vpn-endpoint-id`) as client_vpn_endpoint_id by `common-name` | sort by total_ingress_bytes desc, total_egress_bytes desc",
        "region": "${AWS::Region}",
        "title": "Mutual Auth Users Duration",
        "view": "table"
      }
    },
    {
      "type": "log",
      "x": 0,
      "y": 42,
      "width": 24,
      "height": 6,
      "properties": {
        "query": "SOURCE '${ClientVPNLogGroup}' | fields @timestamp, `client-vpn-endpoint-id`, `common-name` | sort @timestamp asc | stats count(*) as connection_count, latest(`client-vpn-endpoint-id`) as client_vpn_endpoint_id by `common-name`",
        "region": "${AWS::Region}",
        "title": "Mutual Auth Distinct Users",
        "view": "table"
      }
    },
    {
      "type": "log",
      "x": 0,
      "y": 48,
      "width": 24,
      "height": 6,
      "properties": {
        "query": "SOURCE '${ClientVPNLogGroup}' | fields @timestamp, `client-vpn-endpoint-id`, `username`, `common-name`, `ingress-bytes`, `egress-bytes`, `connection-start-time`, `connection-end-time`, `connection-duration-seconds` | sort @timestamp asc | filter `ingress-bytes` > 0 OR `egress-bytes` > 0 | fields @timestamp, `client-vpn-endpoint-id`, `username`, `common-name`, `ingress-bytes`, `egress-bytes`, `connection-start-time`, `connection-end-time`, `connection-duration-seconds`, (`connection-duration-seconds`/60) as connection_time_minutes | sort by `ingress-bytes` desc, `egress-bytes` desc",
        "region": "${AWS::Region}",
        "title": "Mix Auth Total Usage Report",
        "view": "table"
      }
    },
    {
      "type": "log",
      "x": 0,
      "y": 54,
      "width": 24,
      "height": 6,
      "properties": {
        "query": "SOURCE '${ClientVPNLogGroup}' | fields @timestamp, `client-vpn-endpoint-id`, `common-name`, `username`, `ingress-bytes`, `egress-bytes`, `connection-start-time`, `connection-end-time`, `connection-duration-seconds` | sort @timestamp asc | filter `ingress-bytes` > 0 OR `egress-bytes` > 0 | stats count(*) as connection_count, sum(`connection-duration-seconds`/60) as total_connection_time_minutes, sum(`ingress-bytes`) as total_ingress_bytes, sum(`egress-bytes`) as total_egress_bytes, latest(`client-vpn-endpoint-id`) as client_vpn_endpoint_id by `common-name`, `username` | sort by total_ingress_bytes desc, total_egress_bytes desc",
        "region": "${AWS::Region}",
        "title": "Mix Auth Distinct Users Connection Duration",
        "view": "table"
      }
    },
    {
      "type": "log",
      "x": 0,
      "y": 60,
      "width": 24,
      "height": 6,
      "properties": {
        "query": "SOURCE '${ClientVPNLogGroup}' | fields @timestamp, `client-vpn-endpoint-id`, `common-name`, `username` | sort @timestamp asc | stats count(*) as connection_count, latest(`client-vpn-endpoint-id`) as client_vpn_endpoint_id by `username`, `common-name`",
        "region": "${AWS::Region}",
        "title": "Mix Auth Distinct Users",
        "view": "table"
      }
    },
    {
      "type": "log",
      "x": 0,
      "y": 66,
      "width": 24,
      "height": 6,
      "properties": {
        "query": "SOURCE '${ClientVPNLogGroup}' | fields @timestamp, `client-vpn-endpoint-id`, `common-name`, `username`, `ingress-bytes`, `egress-bytes`, `connection-start-time`, `connection-end-time`, `connection-duration-seconds` | sort @timestamp asc | filter `ingress-bytes` > 0 OR `egress-bytes` > 0 | stats count(*) as connection_count, sum(`connection-duration-seconds`/60) as total_connection_time_minutes by `username`, `common-name` | sort by total_connection_time_minutes desc",
        "region": "${AWS::Region}",
        "title": "Mix Auth Users Connection Duration",
        "view": "table"
      }
    }
  ]
}
""")
