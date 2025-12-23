"""EC2Instance - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EC2InstanceEbs:
    resource: ec2.instance.Ebs
    volume_size = ref(BootVolSize)
    volume_type = ref(BootVolType)


@cloudformation_dataclass
class EC2InstanceBlockDeviceMapping:
    resource: ec2.instance.BlockDeviceMapping
    device_name = '/dev/sda1'
    ebs = EC2InstanceEbs


@cloudformation_dataclass
class EC2InstanceAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Sub('${AppName}-${Environment}-ec2-instance')


@cloudformation_dataclass
class EC2InstanceAssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Environment'
    value = ref(Environment)


@cloudformation_dataclass
class EC2Instance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    image_id = ref(EC2ImageId)
    instance_type = ref(EC2InstanceType)
    subnet_id = ref(PublicSubnetId1)
    block_device_mappings = [EC2InstanceBlockDeviceMapping]
    security_group_ids = [ref(EC2InstanceSG), ref(ALBExternalAccessSG)]
    key_name = ref(KeyPairName)
    tags = [EC2InstanceAssociationParameter, EC2InstanceAssociationParameter1]
