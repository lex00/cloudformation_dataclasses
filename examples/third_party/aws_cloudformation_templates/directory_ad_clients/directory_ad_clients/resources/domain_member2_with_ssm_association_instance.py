"""DomainMember2WithSsmAssociationInstance - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DomainMember2WithSsmAssociationInstanceAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = ref(DomainMember2NetBIOSName)


@cloudformation_dataclass
class DomainMember2WithSsmAssociationInstanceEbsBlockDevice:
    resource: EbsBlockDevice
    encrypted = True
    volume_type = 'gp3'
    delete_on_termination = True
    volume_size = 100
    # Unknown CF key: KmsKeyId = If("EBSKMSKeyCondition", ref(EBSKMSKey), AWS_NO_VALUE)


@cloudformation_dataclass
class DomainMember2WithSsmAssociationInstanceBlockDeviceMapping:
    resource: BlockDeviceMapping
    device_name = '/dev/sda1'
    ebs = DomainMember2WithSsmAssociationInstanceEbsBlockDevice


@cloudformation_dataclass
class DomainMember2WithSsmAssociationInstance:
    """AWS::EC2::Instance resource."""

    resource: Instance
    image_id = ref(WINFULLBASE)
    iam_instance_profile = ref(DomainMembersWindowsInstanceProfile)
    instance_type = ref(DomainMembersInstanceType)
    subnet_id = ref(PrivateSubnet2ID)
    tags = [DomainMember2WithSsmAssociationInstanceAssociationParameter]
    block_device_mappings = [DomainMember2WithSsmAssociationInstanceBlockDeviceMapping]
    security_group_ids = [ref(DomainMembersSGID)]
    key_name = ref(KeyPairName)
    user_data = Base64(Sub("""<powershell>
$instanceId = "null"
while ($instanceId -NotLike "i-*") {
Start-Sleep -s 3
$instanceId = Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/instance-id
}
Rename-Computer -NewName ${DomainMember2NetBIOSName} -Force
# Set-TimeZone -Name "US Eastern Standard Time"

Install-WindowsFeature -IncludeAllSubFeature RSAT
Restart-Computer -Force
</powershell>
"""))
