"""Compute resources: Instance."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Instance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    image_id = '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-arm64}}'
    instance_type = 't4g.nano'
    key_name = 'sample'
    block_device_mappings = [{
        'DeviceName': '/dev/sda1',
        'Ebs': {
            'VolumeSize': 32,
        },
    }]
    user_data = Base64(Sub("""#!/bin/bash
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource Instance --region ${AWS::Region}
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource Instance --region ${AWS::Region}"""))
