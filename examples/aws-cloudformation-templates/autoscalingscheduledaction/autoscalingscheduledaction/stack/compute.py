"""Compute resources: LaunchTemplate, WebServerGroup, ScheduledActionUp, ScheduledActionDown."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LaunchTemplateSpotFleetLaunchSpecification:
    resource: ec2.spot_fleet.SpotFleetLaunchSpecification
    key_name = ref(KeyName)
    image_id = FindInMap("AWSRegionArch2AMI", AWS_REGION, FindInMap("AWSInstanceType2Arch", ref(InstanceType), 'Arch'))
    security_groups = [ref(InstanceSecurityGroup)]
    instance_type = ref(InstanceType)
    user_data = Base64(Sub("""#!/bin/bash -xe
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource LaunchTemplate  --region ${AWS::Region}
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerGroup --region ${AWS::Region}
"""))


@cloudformation_dataclass
class LaunchTemplate:
    """AWS::EC2::LaunchTemplate resource."""

    resource: ec2.LaunchTemplate
    launch_template_data = LaunchTemplateSpotFleetLaunchSpecification


@cloudformation_dataclass
class WebServerGroupLaunchTemplateSpecification:
    resource: autoscaling.auto_scaling_group.LaunchTemplateSpecification
    launch_template_id = ref(LaunchTemplate)
    version = get_att(LaunchTemplate, "LatestVersionNumber")


@cloudformation_dataclass
class WebServerGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: autoscaling.AutoScalingGroup
    availability_zones = GetAZs()
    launch_template = WebServerGroupLaunchTemplateSpecification
    min_size = 2
    max_size = 5
    load_balancer_names = [ref(ElasticLoadBalancer)]


@cloudformation_dataclass
class ScheduledActionUp:
    """AWS::AutoScaling::ScheduledAction resource."""

    resource: autoscaling.ScheduledAction
    auto_scaling_group_name = ref(WebServerGroup)
    max_size = '10'
    min_size = '5'
    recurrence = '0 7 * * *'


@cloudformation_dataclass
class ScheduledActionDown:
    """AWS::AutoScaling::ScheduledAction resource."""

    resource: autoscaling.ScheduledAction
    auto_scaling_group_name = ref(WebServerGroup)
    max_size = '1'
    min_size = '1'
    recurrence = '0 19 * * *'
