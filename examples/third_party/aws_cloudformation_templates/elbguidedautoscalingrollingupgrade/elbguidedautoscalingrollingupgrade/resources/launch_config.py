from __future__ import annotations

"""LaunchConfig - AWS::AutoScaling::LaunchConfiguration resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LaunchConfig:
    """AWS::AutoScaling::LaunchConfiguration resource."""

    resource: LaunchConfiguration
    key_name = ref(KeyName)
    image_id = ref(LatestAmiId)
    instance_type = ref(InstanceType)
    security_groups = [ref(InstanceSecurityGroup)]
    iam_instance_profile = ref(WebServerInstanceProfile)
    user_data = Base64(Sub("""#!/bin/bash -xe          
yum update -y aws-cfn-bootstrap 
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} \
         --resource LaunchConfig \
         --configsets full_install \
         --region ${AWS::Region}

/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} \
         --resource WebServerGroup \
         --region ${AWS::Region} 
"""))
