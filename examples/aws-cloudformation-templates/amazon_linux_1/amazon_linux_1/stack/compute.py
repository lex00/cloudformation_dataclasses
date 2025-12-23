"""Compute resources: EC2Instance."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EC2Instance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    instance_type = ref(InstanceType)
    iam_instance_profile = ref(IAMRole)
    key_name = ref(KeyName)
    image_id = ref(InstanceAMI)
    subnet_id = ref(SubnetId)
    security_group_ids = [get_att(InstanceSecurityGroup, "GroupId")]
    user_data = Base64(Sub("""#!/bin/bash
rpm -Uvh https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm
/opt/aws/bin/cfn-init -v --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region} --configsets default
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region}
"""))
