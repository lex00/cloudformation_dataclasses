"""Compute resources: EC2Instance."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EC2Instance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    instance_type = ref(InstanceType)
    iam_instance_profile = ref(IAMRole)
    key_name = ref(KeyName)
    image_id = FindInMap("RegionMap", AWS_REGION, ref(CentOSVersion))
    subnet_id = ref(SubnetId)
    security_group_ids = [get_att(InstanceSecurityGroup, "GroupId")]
    user_data = Base64(Sub("""#!/bin/bash
rpm -Uvh https://s3.amazonaws.com/amazoncloudwatch-agent/centos/amd64/latest/amazon-cloudwatch-agent.rpm
yum update -y
yum install python3 -y
curl -O https://bootstrap.pypa.io/get-pip.py
# Install pip using python3
python3 get-pip.py
export PATH=$PATH:/usr/local/bin
pip3 install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-py3-latest.tar.gz
cfn-init -v --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region} --configsets default
cfn-signal -e $? --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region}
"""))
