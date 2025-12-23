"""LaunchTemplate - AWS::EC2::LaunchTemplate resource."""

from .. import *  # noqa: F403


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
