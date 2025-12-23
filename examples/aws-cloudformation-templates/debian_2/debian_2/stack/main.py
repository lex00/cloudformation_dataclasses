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
    image_id = ref(InstanceAMI)
    subnet_id = ref(SubnetId)
    security_group_ids = [get_att(InstanceSecurityGroup, "GroupId")]
    user_data = Base64(Sub("""#!/bin/bash
wget https://s3.amazonaws.com/amazoncloudwatch-agent/debian/amd64/latest/amazon-cloudwatch-agent.deb -O /tmp/amazon-cloudwatch-agent.deb
sudo dpkg -i /tmp/amazon-cloudwatch-agent.deb
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c ssm:${ssmkey} -s
wget https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-py3-latest.tar.gz -O /tmp/aws-cfn-bootstrap-py3-latest.tar.gz
sudo apt-get update -y
sudo apt-get install -y python3-pip python3-venv

# Create and activate a virtual environment
python3 -m venv /opt/aws/virtualenv
source /opt/aws/virtualenv/bin/activate

# Install the bootstrap package
pip install /tmp/aws-cfn-bootstrap-py3-latest.tar.gz

# Create necessary symlinks
sudo mkdir -p /opt/aws/bin
sudo ln -s /opt/aws/virtualenv/bin/cfn-* /opt/aws/bin/

# Run cfn-init
/opt/aws/bin/cfn-init -v --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region} --configsets default
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region}
""", {
    'ssmkey': ref(SSMKey),
}))
