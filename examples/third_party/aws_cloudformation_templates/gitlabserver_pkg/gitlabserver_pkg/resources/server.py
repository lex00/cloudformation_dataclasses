from __future__ import annotations

"""Server - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ServerEbsBlockDevice:
    resource: EbsBlockDevice
    volume_size = 128


@cloudformation_dataclass
class ServerBlockDeviceMapping:
    resource: BlockDeviceMapping
    device_name = '/dev/xvda'
    ebs = ServerEbsBlockDevice


@cloudformation_dataclass
class ServerAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'gitlab-server'


@cloudformation_dataclass
class Server:
    """AWS::EC2::Instance resource."""

    resource: Instance
    availability_zone = Select(0, GetAZs())
    block_device_mappings = [ServerBlockDeviceMapping]
    iam_instance_profile: Ref[InstanceProfile] = ref()
    image_id = ref(LatestAMI)
    instance_type = ref(InstanceType)
    security_group_ids = [get_att("InstanceSecurityGroup", "GroupId")]
    subnet_id: GetAtt[NetworkPublicSubnet1] = get_att("SubnetId")
    tags = [ServerAssociationParameter]
    user_data = Base64({
    'Fn::Sub': """#!/bin/bash

set -eou pipefail

local_ip=$(ec2-metadata | grep "^local-ipv4: " | cut -d " " -f 2)

# Install cfn-signal
yum install -y aws-cfn-bootstrap

# Install postfix
yum install -y postfix
systemctl enable postfix
systemctl start postfix

# Get the yum repo
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.rpm.sh | sudo bash

# Install gitlab and run it on the local ip
export EXTERNAL_URL="http://$local_ip" 
yum install -y gitlab-ee

# Tell CloudFormation we're ready to go
# This is a variable for the Sub intrisic function, not a bash variable
cfn-signal -s true --stack ${AWS::StackName} --resource Server --region ${AWS::Region}""",
})
    depends_on = ["InstanceRolePolicy", "InstanceRole"]
