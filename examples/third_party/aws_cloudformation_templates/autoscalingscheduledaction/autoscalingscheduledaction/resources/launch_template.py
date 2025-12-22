from __future__ import annotations

"""LaunchTemplate - AWS::EC2::LaunchTemplate resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LaunchTemplateLaunchTemplateData:
    resource: LaunchTemplateData
    key_name = ref(KeyName)
    image_id = FindInMap("AWSRegionArch2AMI", AWS_REGION, FindInMap("AWSInstanceType2Arch", ref(InstanceType), 'Arch'))
    security_groups = [ref("InstanceSecurityGroup")]
    instance_type = ref(InstanceType)
    user_data = Base64({
    'Fn::Sub': """#!/bin/bash -xe
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource LaunchTemplate  --region ${AWS::Region}
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerGroup --region ${AWS::Region}
""",
})


@cloudformation_dataclass
class LaunchTemplate:
    """AWS::EC2::LaunchTemplate resource."""

    resource: ec2.LaunchTemplate
    launch_template_data = LaunchTemplateLaunchTemplateData
