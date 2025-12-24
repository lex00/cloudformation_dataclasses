"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LogInsightsUrlOutput:
    resource: Output
    value = Sub('https://${AWS::Region}.console.aws.amazon.com/cloudwatch/home?region=${AWS::Region}#logsV2:logs-insights')


@cloudformation_dataclass
class DashboardUrlOutput:
    """URL to access the created CloudWatch Dashboard for AWS Client VPN Usage"""

    resource: Output
    value = Sub('https://${AWS::Region}.console.aws.amazon.com/cloudwatch/home?region=${AWS::Region}#dashboards:name=${AWS::Region}-AWS-ClientVPN-Usage-Dashboard')
    description = 'URL to access the created CloudWatch Dashboard for AWS Client VPN Usage'
