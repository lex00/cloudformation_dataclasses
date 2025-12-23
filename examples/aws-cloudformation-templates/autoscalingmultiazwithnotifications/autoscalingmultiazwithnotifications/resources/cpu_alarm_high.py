"""CPUAlarmHigh - AWS::CloudWatch::Alarm resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CPUAlarmHigh:
    """AWS::CloudWatch::Alarm resource."""

    # Unknown resource type: AWS::CloudWatch::Alarm
    resource: CloudFormationResource
    alarm_description = 'Scale-up if CPU > 90% for 10 minutes'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = 90
    alarm_actions = [ref(WebServerScaleUpPolicy)]
    dimensions = [{
        'Name': 'AutoScalingGroupName',
        'Value': ref(WebServerGroup),
    }]
    comparison_operator = 'GreaterThanThreshold'
