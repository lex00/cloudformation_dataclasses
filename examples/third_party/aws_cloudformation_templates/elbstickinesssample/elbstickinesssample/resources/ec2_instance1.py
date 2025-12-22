"""EC2Instance1 - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EC2Instance1:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    subnet_id = ref(SubnetId)
    security_group_ids = [get_att(InstanceSecurityGroup, "GroupId")]
    key_name = ref(KeyName)
    instance_type = ref(InstanceType)
    image_id = ref(LatestAmiId)
    user_data = Base64(Sub("""#!/bin/bash -xe          
yum update -y aws-cfn-bootstrap 
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} \
         --resource EC2Instance1 \
         --region ${AWS::Region}

/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} \
         --resource EC2Instance1 \
         --region ${AWS::Region} 
"""))
