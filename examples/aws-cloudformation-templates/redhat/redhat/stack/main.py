"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable SSH access via port 22'
    security_group_ingress = [{
        'IpProtocol': 'tcp',
        'FromPort': '22',
        'ToPort': '22',
        'CidrIp': ref(SSHLocation),
    }]


@cloudformation_dataclass
class EC2Instance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    instance_type = ref(InstanceType)
    iam_instance_profile = ref(IAMRole)
    key_name = ref(KeyName)
    image_id = FindInMap("RegionMap", AWS_REGION, ref(RHELVersion))
    subnet_id = ref(SubnetId)
    security_group_ids = [get_att(InstanceSecurityGroup, "GroupId")]
    user_data = Base64(Sub("""#!/bin/bash
rpm -Uvh https://s3.amazonaws.com/amazoncloudwatch-agent/redhat/amd64/latest/amazon-cloudwatch-agent.rpm
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c ssm:${ssmkey} -s
yum update -y
yum install python3 -y
curl -O https://bootstrap.pypa.io/get-pip.py
# Install pip using python3
python3 get-pip.py
export PATH=$PATH:/usr/local/bin
pip3 install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-py3-latest.tar.gz
cfn-init -v --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region} --configsets default
cfn-signal -e $? --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region}
""", {
    'ssmkey': ref(SSMKey),
}))
