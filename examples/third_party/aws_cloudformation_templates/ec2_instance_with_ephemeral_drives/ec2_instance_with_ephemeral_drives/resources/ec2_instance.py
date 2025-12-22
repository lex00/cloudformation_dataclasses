from __future__ import annotations

"""EC2Instance - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EC2InstanceBlockDeviceMapping:
    resource: BlockDeviceMapping
    device_name = '/dev/sdc'
    virtual_name = 'ephemeral0'


@cloudformation_dataclass
class EC2Instance:
    """AWS::EC2::Instance resource."""

    resource: Instance
    instance_type = ref(InstanceType)
    subnet_id = Select(0, ref(Subnets))
    security_group_ids = [get_att("EC2SecurityGroup", "GroupId")]
    key_name = ref(KeyName)
    image_id = ref(LatestAmiId)
    block_device_mappings = [EC2InstanceBlockDeviceMapping]
