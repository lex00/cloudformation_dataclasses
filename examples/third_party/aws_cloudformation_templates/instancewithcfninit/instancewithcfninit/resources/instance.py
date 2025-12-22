"""Instance - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceEbs:
    resource: ec2.instance.Ebs
    volume_size = 32


@cloudformation_dataclass
class InstanceBlockDeviceMapping:
    resource: ec2.instance.BlockDeviceMapping
    device_name = '/dev/sda1'
    ebs = InstanceEbs


@cloudformation_dataclass
class Instance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    image_id = '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-arm64}}'
    instance_type = 't4g.nano'
    key_name = 'sample'
    block_device_mappings = [InstanceBlockDeviceMapping]
    user_data = Base64(Sub("""#!/bin/bash
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource Instance --region ${AWS::Region}
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource Instance --region ${AWS::Region}"""))
