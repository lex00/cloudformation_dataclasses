"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EC2SecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'SSH access'
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
    subnet_id = Select(0, ref(Subnets))
    security_group_ids = [get_att(EC2SecurityGroup, "GroupId")]
    key_name = ref(KeyName)
    image_id = ref(LatestAmiId)
    block_device_mappings = [{
        'DeviceName': '/dev/sdc',
        'VirtualName': 'ephemeral0',
    }]
