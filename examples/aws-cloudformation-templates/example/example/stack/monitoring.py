"""Monitoring resources: Dashboard."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Dashboard:
    """AWS::CloudWatch::Dashboard resource."""

    resource: cloudwatch.Dashboard
    dashboard_name = 'CloudFormation-Stacks'
    dashboard_body = """{
    "widgets": [
        {
            "type": "metric",
            "x": 0,
            "y": 0,
            "width": 12,
            "height": 12,
            "properties": {
                "view": "timeSeries",
                "stacked": false,
                "metrics": [
                    [ "CloudFormation", "ResourceCount" ]
                ],
                "region": "eu-west-1",
                "title": "Resources created",
                "period": 300,
                "stat": "Sum"
            }
        },
        {
            "type": "metric",
            "x": 12,
            "y": 0,
            "width": 12,
            "height": 12,
            "properties": {
                "view": "timeSeries",
                "stacked": true,
                "title": "Stack operations",
                "metrics": [
                    [ "CloudFormation", "Create" ],
                    [ ".", "Delete" ],
                    [ ".", "Update" ]
                ],
                "region": "eu-west-1",
                "period": 300,
                "stat": "Sum"
            }
        }
    ]
}
"""
