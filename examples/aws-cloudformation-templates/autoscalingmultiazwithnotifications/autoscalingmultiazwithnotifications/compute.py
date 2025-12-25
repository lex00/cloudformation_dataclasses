"""Compute resources: LaunchTemplate, WebServerGroup, WebServerScaleUpPolicy, WebServerScaleDownPolicy."""

from . import *  # noqa: F403


@cloudformation_dataclass
class LaunchTemplateEbs:
    resource: ec2.launch_template.Ebs
    volume_size = 32


@cloudformation_dataclass
class LaunchTemplateBlockDeviceMapping:
    resource: ec2.launch_template.BlockDeviceMapping
    device_name = '/dev/sda1'
    ebs = LaunchTemplateEbs


@cloudformation_dataclass
class LaunchTemplateTagSpecification:
    resource: ec2.launch_template.TagSpecification
    resource_type = 'instance'
    tags = [{
        AssociationParameter.key: 'Name',
        AssociationParameter.value: Sub('${AWS::StackName}-Instance'),
    }]


@cloudformation_dataclass
class LaunchTemplateLaunchTemplateData:
    resource: ec2.launch_template.LaunchTemplateData
    image_id = ref(LatestAmiId)
    instance_type = ref(InstanceType)
    security_group_ids = ref(SecurityGroups)
    key_name = ref(KeyName)
    block_device_mappings = [LaunchTemplateBlockDeviceMapping]
    user_data = Base64(Sub("""#!/bin/bash
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource LaunchTemplate --region ${AWS::Region}
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerGroup --region ${AWS::Region}
"""))
    tag_specifications = [LaunchTemplateTagSpecification]


@cloudformation_dataclass
class LaunchTemplate:
    """AWS::EC2::LaunchTemplate resource."""

    resource: ec2.LaunchTemplate
    launch_template_name = Sub('${AWS::StackName}-LaunchTemplate')
    launch_template_data = LaunchTemplateLaunchTemplateData


@cloudformation_dataclass
class WebServerGroupLaunchTemplateSpecification:
    resource: autoscaling.auto_scaling_group.LaunchTemplateSpecification
    launch_template_id = ref(LaunchTemplate)
    version = get_att(LaunchTemplate, "LatestVersionNumber")


@cloudformation_dataclass
class WebServerGroupNotificationConfiguration:
    resource: autoscaling.auto_scaling_group.NotificationConfiguration
    topic_arn = ref(NotificationTopic)
    notification_types = ['autoscaling:EC2_INSTANCE_LAUNCH', 'autoscaling:EC2_INSTANCE_LAUNCH_ERROR', 'autoscaling:EC2_INSTANCE_TERMINATE', 'autoscaling:EC2_INSTANCE_TERMINATE_ERROR']


@cloudformation_dataclass
class WebServerGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: autoscaling.AutoScalingGroup
    availability_zones = ref(AZs)
    launch_template = WebServerGroupLaunchTemplateSpecification
    min_size = '1'
    max_size = '3'
    target_group_ar_ns = [ref(TargetGroup)]
    notification_configurations = [WebServerGroupNotificationConfiguration]
    health_check_type = 'ELB'
    vpc_zone_identifier = ref(Subnets)


@cloudformation_dataclass
class WebServerScaleUpPolicy:
    """AWS::AutoScaling::ScalingPolicy resource."""

    resource: autoscaling.ScalingPolicy
    adjustment_type = 'ChangeInCapacity'
    auto_scaling_group_name = ref(WebServerGroup)
    cooldown = '60'
    scaling_adjustment = 1


@cloudformation_dataclass
class WebServerScaleDownPolicy:
    """AWS::AutoScaling::ScalingPolicy resource."""

    resource: autoscaling.ScalingPolicy
    adjustment_type = 'ChangeInCapacity'
    auto_scaling_group_name = ref(WebServerGroup)
    cooldown = '60'
    scaling_adjustment = -1
