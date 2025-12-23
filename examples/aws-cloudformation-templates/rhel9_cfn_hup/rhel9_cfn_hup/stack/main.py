"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceSecurityGroupEgress:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = ref(SSHLocation)


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable SSH access via port 22'
    security_group_ingress = [InstanceSecurityGroupEgress]


@cloudformation_dataclass
class EC2Instance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    instance_type = ref(InstanceType)
    subnet_id = ref(SubnetId)
    security_group_ids = [get_att(InstanceSecurityGroup, "GroupId")]
    key_name = ref(KeyName)
    image_id = FindInMap("AWSRegionArch2AMI", AWS_REGION, FindInMap("AWSInstanceType2Arch", ref(InstanceType), 'Arch'))
    user_data = Base64(Sub("""#!/bin/bash -xe

sudo yum update -y
sudo yum -y install python3-pip
sudo pip3 install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-py3-latest.tar.gz
/usr/local/bin/cfn-init -v --stack ${AWS::StackName} --resource EC2Instance --configsets full_install --region ${AWS::Region} 
/usr/local/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource EC2Instance --region ${AWS::Region}
"""))
