"""CPUAlarmLow - AWS::CloudWatch::Alarm resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CPUAlarmLow:
    """AWS::CloudWatch::Alarm resource."""

    # Unknown resource type: AWS::CloudWatch::Alarm
    resource: CloudFormationResource
    alarm_description = 'Scale-down if CPU < 70% for 10 minutes'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = 70
    alarm_actions = [ref(WebServerScaleDownPolicy)]
    dimensions = [{
        'Name': 'AutoScalingGroupName',
        'Value': ref(WebServerGroup),
    }]
    comparison_operator = 'LessThanThreshold'
