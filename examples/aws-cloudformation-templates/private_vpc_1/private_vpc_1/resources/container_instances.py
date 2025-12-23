"""ContainerInstances - AWS::EC2::LaunchTemplate resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ContainerInstances:
    """AWS::EC2::LaunchTemplate resource."""

    resource: ec2.LaunchTemplate
    launch_template_data = {
        'ImageId': ref(ECSAMI),
        'SecurityGroupIds': [ref(EcsHostSecurityGroup)],
        'InstanceType': ref(InstanceType),
        'IamInstanceProfile': {
            'Arn': get_att(EC2InstanceProfile, "Arn"),
        },
        'UserData': Base64(Sub("""#!/bin/bash -xe
echo ECS_CLUSTER=${ECSCluster} >> /etc/ecs/ecs.config
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource ECSAutoScalingGroup --region ${AWS::Region}
""")),
    }
