"""DomainMember3WithSsmAssociationTag - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DomainMember3WithSsmAssociationTagAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = ref(DomainMember3NetBIOSName)


@cloudformation_dataclass
class DomainMember3WithSsmAssociationTagAssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'DomainJoin'
    value = ref(DirectoryName)


@cloudformation_dataclass
class DomainMember3WithSsmAssociationTagEbs:
    resource: ec2.instance.Ebs
    encrypted = True
    volume_type = 'gp3'
    delete_on_termination = True
    volume_size = 100
    kms_key_id = If("EBSKMSKeyCondition", ref(EBSKMSKey), AWS_NO_VALUE)


@cloudformation_dataclass
class DomainMember3WithSsmAssociationTagBlockDeviceMapping:
    resource: ec2.instance.BlockDeviceMapping
    device_name = '/dev/sda1'
    ebs = DomainMember3WithSsmAssociationTagEbs


@cloudformation_dataclass
class DomainMember3WithSsmAssociationTag:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    image_id = ref(WINFULLBASE)
    iam_instance_profile = ref(DomainMembersWindowsInstanceProfile)
    instance_type = ref(DomainMembersInstanceType)
    subnet_id = ref(PrivateSubnet1ID)
    tags = [DomainMember3WithSsmAssociationTagAssociationParameter, DomainMember3WithSsmAssociationTagAssociationParameter1]
    block_device_mappings = [DomainMember3WithSsmAssociationTagBlockDeviceMapping]
    security_group_ids = [ref(DomainMembersSGID)]
    key_name = ref(KeyPairName)
    user_data = Base64(Sub("""<powershell>
$instanceId = "null"
while ($instanceId -NotLike "i-*") {
Start-Sleep -s 3
$instanceId = Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/instance-id
}
Rename-Computer -NewName ${DomainMember3NetBIOSName} -Force
# Set-TimeZone -Name "US Eastern Standard Time"

Install-WindowsFeature -IncludeAllSubFeature RSAT
Restart-Computer -Force
</powershell>
"""))
