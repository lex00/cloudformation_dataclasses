from __future__ import annotations

"""ContainerInstances - AWS::EC2::LaunchTemplate resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ContainerInstancesIamInstanceProfile:
    resource: IamInstanceProfile
    arn: GetAtt[EC2InstanceProfile] = get_att("Arn")


@cloudformation_dataclass
class ContainerInstancesLaunchTemplateData:
    resource: LaunchTemplateData
    image_id = ref(ECSAMI)
    security_group_ids = [ref("EcsHostSecurityGroup")]
    instance_type = ref(InstanceType)
    iam_instance_profile = ContainerInstancesIamInstanceProfile
    user_data = Base64({
    'Fn::Sub': """#!/bin/bash -xe
echo ECS_CLUSTER=${ECSCluster} >> /etc/ecs/ecs.config
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource ECSAutoScalingGroup --region ${AWS::Region}
""",
})


@cloudformation_dataclass
class ContainerInstances:
    """AWS::EC2::LaunchTemplate resource."""

    resource: LaunchTemplate
    launch_template_data = ContainerInstancesLaunchTemplateData
