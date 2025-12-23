"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ResourceFunction:
    """AWS::Serverless::Function resource."""

    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = 'python3.12'
    code_uri = 'lambda'
    handler = 'resource.handler'
    policies = 'CloudWatchFullAccess'


@cloudformation_dataclass
class MacroFunction:
    """AWS::Serverless::Function resource."""

    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = 'python3.12'
    code_uri = 'lambda'
    handler = 'index.handler'


@cloudformation_dataclass
class Macro:
    """AWS::CloudFormation::Macro resource."""

    resource: cloudformation.Macro
    name = 'StackMetrics'
    function_name = get_att(MacroFunction, "Arn")


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
