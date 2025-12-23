"""ContainerInstances - AWS::AutoScaling::LaunchConfiguration resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ContainerInstances:
    """AWS::AutoScaling::LaunchConfiguration resource."""

    resource: autoscaling.LaunchConfiguration
    image_id = ref(LatestAmiId)
    security_groups = [ref(EcsSecurityGroup)]
    instance_type = ref(InstanceType)
    iam_instance_profile = ref(EC2InstanceProfile)
    key_name = ref(KeyName)
    user_data = Base64(Sub("""#!/bin/bash -xe
echo ECS_CLUSTER=${ECSCluster} >> /etc/ecs/ecs.config
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} \
    --resource ECSAutoScalingGroup \
    --region ${AWS::Region}
"""))
