from __future__ import annotations

"""LaunchTemplate - AWS::EC2::LaunchTemplate resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LaunchTemplateEbsBlockDevice:
    resource: EbsBlockDevice
    volume_size = 32


@cloudformation_dataclass
class LaunchTemplateBlockDeviceMapping:
    resource: BlockDeviceMapping
    device_name = '/dev/sda1'
    ebs = LaunchTemplateEbsBlockDevice


@cloudformation_dataclass
class LaunchTemplateAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-Instance')


@cloudformation_dataclass
class LaunchTemplateTagSpecification:
    resource: TagSpecification
    resource_type = 'instance'
    tags = [LaunchTemplateAssociationParameter]


@cloudformation_dataclass
class LaunchTemplateLaunchTemplateData:
    resource: LaunchTemplateData
    image_id = ref(LatestAmiId)
    instance_type = ref(InstanceType)
    security_group_ids = ref(SecurityGroups)
    key_name = ref(KeyName)
    block_device_mappings = [LaunchTemplateBlockDeviceMapping]
    user_data = Base64({
    'Fn::Sub': """#!/bin/bash
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource LaunchTemplate --region ${AWS::Region}
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerGroup --region ${AWS::Region}
""",
})
    tag_specifications = [LaunchTemplateTagSpecification]


@cloudformation_dataclass
class LaunchTemplate:
    """AWS::EC2::LaunchTemplate resource."""

    resource: ec2.LaunchTemplate
    launch_template_name = Sub('${AWS::StackName}-LaunchTemplate')
    launch_template_data = LaunchTemplateLaunchTemplateData
