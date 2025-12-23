"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CloudWatchDashboard:
    """AWS::CloudWatch::Dashboard resource."""

    resource: cloudwatch.Dashboard
    dashboard_name = Sub('${NatGatewayID}-Traffic-Dashboard')
    dashboard_body = Sub("""{
  "widgets": [
    {
      "type": "log",
      "x": 0,
      "y": 0,
      "width": 12,
      "height": 9,
      "properties": {
        "query": "SOURCE '${LogGroupName}' | fields @timestamp, @message | filter (dstAddr like '${NatGatewayPrivateIP}' and isIpv4InSubnet(srcAddr, '${VpcCidr}')) | stats sum(bytes) as bytesTransferred by srcAddr, dstAddr | sort bytesTransferred desc | limit 10",
        "region": "${AWS::Region}",
        "stacked": false,
        "title": "Top 10 - Instances sending most traffic through NAT gateway ${NatGatewayID}", 
        "view": "table"
      }
    },
    {
      "type": "log",
      "x": 12,
      "y": 0,
      "width": 12,
      "height": 9,
      "properties": {
        "query": "SOURCE '${LogGroupName}' | fields @timestamp, @message | filter (dstAddr like '${NatGatewayPrivateIP}' and isIpv4InSubnet(srcAddr, '${VpcCidr}')) or (srcAddr like '${NatGatewayPrivateIP}' and isIpv4InSubnet(dstAddr, '${VpcCidr}'))| stats sum(bytes) as bytesTransferred by srcAddr, dstAddr | sort bytesTransferred desc | limit 10",
        "region": "${AWS::Region}",
        "stacked": false,
        "title": "Top 10 - Traffic To and from NAT gateway ${NatGatewayID}",
        "view": "table"
      }
    },
    {
      "type": "log",
      "x": 0,
      "y": 9,
      "width": 12,
      "height": 9,
      "properties": {
        "query": "SOURCE '${LogGroupName}' | fields @timestamp, @message | filter (srcAddr like '${NatGatewayPrivateIP}' and not isIpv4InSubnet(dstAddr, '${VpcCidr}')) | stats sum(bytes) as bytesTransferred by srcAddr, dstAddr | sort bytesTransferred desc | limit 10",
        "region": "${AWS::Region}",
        "stacked": false,
        "title": "Top 10 - Most often upload communication destinations through NAT Gateway ${NatGatewayID}",
        "view": "table"
      }
    },
    {
      "type": "log",
      "x": 12,
      "y": 9,
      "width": 12,
      "height": 9,
      "properties": {
        "query": "SOURCE '${LogGroupName}' | fields @timestamp, @message | filter (dstAddr like '${NatGatewayPrivateIP}' and not isIpv4InSubnet(srcAddr, '${VpcCidr}')) | stats sum(bytes) as bytesTransferred by srcAddr, dstAddr | sort bytesTransferred desc | limit 10",
        "region": "${AWS::Region}",
        "stacked": false,
        "title": "Top 10 - Most often download communication destinations through NAT Gateway ${NatGatewayID}",
        "view": "table"
      }
    }
  ]
}
""")
