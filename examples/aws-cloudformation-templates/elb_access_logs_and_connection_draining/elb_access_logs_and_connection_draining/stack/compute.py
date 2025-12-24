"""Compute resources: LaunchConfig, WebServerGroup."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LaunchConfig:
    """AWS::AutoScaling::LaunchConfiguration resource."""

    resource: autoscaling.LaunchConfiguration
    key_name = ref(KeyName)
    image_id = ref(LatestAmiId)
    security_groups = [ref(InstanceSecurityGroup)]
    instance_type = ref(InstanceType)
    user_data = Base64(Sub("""#!/bin/bash -xe          
yum update -y aws-cfn-bootstrap 
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} \
         --resource LaunchConfig \
         --region ${AWS::Region}

/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} \
         --resource WebServerGroup \
         --region ${AWS::Region} 
"""))


@cloudformation_dataclass
class WebServerGroup:
    """AWS::AutoScaling::AutoScalingGroup resource."""

    resource: autoscaling.AutoScalingGroup
    availability_zones = GetAZs()
    launch_configuration_name = ref(LaunchConfig)
    min_size = 2
    max_size = 2
    load_balancer_names = [ref(ElasticLoadBalancer)]
