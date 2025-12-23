"""DomainMember4LinuxWithSsmAssociationInstance - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DomainMember4LinuxWithSsmAssociationInstanceAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = ref(DomainMember4NetBIOSName)


@cloudformation_dataclass
class DomainMember4LinuxWithSsmAssociationInstanceEbs:
    resource: ec2.instance.Ebs
    encrypted = True
    volume_type = 'gp3'
    delete_on_termination = True
    volume_size = 100
    kms_key_id = If("EBSKMSKeyCondition", ref(EBSKMSKey), AWS_NO_VALUE)


@cloudformation_dataclass
class DomainMember4LinuxWithSsmAssociationInstanceBlockDeviceMapping:
    resource: ec2.instance.BlockDeviceMapping
    device_name = '/dev/sda1'
    ebs = DomainMember4LinuxWithSsmAssociationInstanceEbs


@cloudformation_dataclass
class DomainMember4LinuxWithSsmAssociationInstance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    image_id = ref(AMAZONLINUX2)
    iam_instance_profile = ref(DomainMembersLinuxInstanceProfile)
    instance_type = ref(DomainMembersInstanceType)
    subnet_id = ref(PrivateSubnet2ID)
    tags = [DomainMember4LinuxWithSsmAssociationInstanceAssociationParameter]
    block_device_mappings = [DomainMember4LinuxWithSsmAssociationInstanceBlockDeviceMapping]
    security_group_ids = [ref(DomainMembersSGID)]
    key_name = ref(KeyPairName)
    user_data = Base64(Sub("""# Set HostName
LowerEc2Name=$(echo ${DomainMember4NetBIOSName} | tr '[:upper:]' '[:lower:]')
hostnamectl set-hostname $LowerEc2Name
# Set TimeZone
# sed -i 's|^ZONE=.*|ZONE="America/New_York"|' /etc/sysconfig/clock
# ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime
# Patch System Up
yum update -y
# Reboot
reboot
"""))
