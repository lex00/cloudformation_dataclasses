"""Compute resources: LaunchTemplate, WebServerGroup, WebServerScaleUpPolicy, WebServerScaleDownPolicy."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LaunchTemplate:
    """AWS::EC2::LaunchTemplate resource."""

    # Unknown resource type: AWS::EC2::LaunchTemplate
    resource: CloudFormationResource
    launch_template_name = Sub('${AWS::StackName}-LaunchTemplate')
    launch_template_data = {
        'ImageId': ref(LatestAmiId),
        'InstanceType': ref(InstanceType),
        'SecurityGroupIds': ref(SecurityGroups),
        'KeyName': ref(KeyName),
        'BlockDeviceMappings': [{
            'DeviceName': '/dev/sda1',
            'Ebs': {
                'VolumeSize': 32,
            },
        }],
        'UserData': Base64(Sub("""#!/bin/bash
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource LaunchTemplate --region ${AWS::Region}
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerGroup --region ${AWS::Region}
""")),
        'TagSpecifications': [{
            'ResourceType': 'instance',
            'Tags': [{
                'Key': 'Name',
                'Value': Sub('${AWS::StackName}-Instance'),
            }],
        }],
    }


@cloudformation_dataclass
class WebServerGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    # Unknown resource type: AWS::AutoScaling::AutoScalingGroup
    resource: CloudFormationResource
    availability_zones = ref(AZs)
    launch_template = {
        'LaunchTemplateId': ref(LaunchTemplate),
        'Version': get_att(LaunchTemplate, "LatestVersionNumber"),
    }
    min_size = '1'
    max_size = '3'
    target_group_ar_ns = [ref(TargetGroup)]
    notification_configurations = [{
        'TopicARN': ref(NotificationTopic),
        'NotificationTypes': [
            'autoscaling:EC2_INSTANCE_LAUNCH',
            'autoscaling:EC2_INSTANCE_LAUNCH_ERROR',
            'autoscaling:EC2_INSTANCE_TERMINATE',
            'autoscaling:EC2_INSTANCE_TERMINATE_ERROR',
        ],
    }]
    health_check_type = 'ELB'
    vpc_zone_identifier = ref(Subnets)


@cloudformation_dataclass
class WebServerScaleUpPolicy:
    """AWS::AutoScaling::ScalingPolicy resource."""

    # Unknown resource type: AWS::AutoScaling::ScalingPolicy
    resource: CloudFormationResource
    adjustment_type = 'ChangeInCapacity'
    auto_scaling_group_name = ref(WebServerGroup)
    cooldown = '60'
    scaling_adjustment = 1


@cloudformation_dataclass
class WebServerScaleDownPolicy:
    """AWS::AutoScaling::ScalingPolicy resource."""

    # Unknown resource type: AWS::AutoScaling::ScalingPolicy
    resource: CloudFormationResource
    adjustment_type = 'ChangeInCapacity'
    auto_scaling_group_name = ref(WebServerGroup)
    cooldown = '60'
    scaling_adjustment = -1
