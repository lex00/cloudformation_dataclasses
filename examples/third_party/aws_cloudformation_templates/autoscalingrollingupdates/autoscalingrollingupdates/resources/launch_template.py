from __future__ import annotations

"""LaunchTemplate - AWS::EC2::LaunchTemplate resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LaunchTemplateIamInstanceProfile:
    resource: IamInstanceProfile
    name: Ref[WebServerInstanceProfile] = ref()


@cloudformation_dataclass
class LaunchTemplateLaunchTemplateData:
    resource: LaunchTemplateData
    key_name = ref(KeyName)
    image_id = FindInMap("AWSRegionArch2AMI", AWS_REGION, FindInMap("AWSInstanceType2Arch", ref(InstanceType), 'Arch'))
    instance_type = ref(InstanceType)
    security_groups = [ref("InstanceSecurityGroup")]
    iam_instance_profile = LaunchTemplateIamInstanceProfile
    user_data = Base64({
    'Fn::Sub': """#!/bin/bash -xe
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-init -v --stack ${AWS::StackId} --resource LaunchTemplate --configsets full_install --region ${AWS::Region}
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackId} --resource WebServerGroup --region ${AWS::Region}
""",
})


@cloudformation_dataclass
class LaunchTemplate:
    """AWS::EC2::LaunchTemplate resource."""

    resource: ec2.LaunchTemplate
    launch_template_data = LaunchTemplateLaunchTemplateData
