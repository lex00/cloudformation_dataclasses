"""Compute resources: DomainMember1WithInlineSsmAssociation, DomainMember2WithSsmAssociationInstance, DomainMember3WithSsmAssociationTag, DomainMember4LinuxWithSsmAssociationInstance."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DomainMember1WithInlineSsmAssociationAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'directoryId'
    value = [ref(DirectoryID)]


@cloudformation_dataclass
class DomainMember1WithInlineSsmAssociationAssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'directoryName'
    value = [ref(DirectoryName)]


@cloudformation_dataclass
class DomainMember1WithInlineSsmAssociationSsmAssociation:
    resource: ec2.instance.SsmAssociation
    document_name = 'AWS-JoinDirectoryServiceDomain'
    association_parameters = [DomainMember1WithInlineSsmAssociationAssociationParameter, DomainMember1WithInlineSsmAssociationAssociationParameter1, If("DomainDNSServersCondition", {
    AssociationParameter.key: 'dnsIpAddresses',
    AssociationParameter.value: [
        If("DomainDNSServer1Condition", ref(DomainDNSServer1), AWS_NO_VALUE),
        If("DomainDNSServer2Condition", ref(DomainDNSServer2), AWS_NO_VALUE),
        If("DomainDNSServer3Condition", ref(DomainDNSServer3), AWS_NO_VALUE),
        If("DomainDNSServer4Condition", ref(DomainDNSServer4), AWS_NO_VALUE),
    ],
}, AWS_NO_VALUE)]


@cloudformation_dataclass
class DomainMember1WithInlineSsmAssociationAssociationParameter2:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = ref(DomainMember1NetBIOSName)


@cloudformation_dataclass
class DomainMember1WithInlineSsmAssociationEbs:
    resource: ec2.instance.Ebs
    encrypted = True
    volume_type = 'gp3'
    delete_on_termination = True
    volume_size = 100
    kms_key_id = If("EBSKMSKeyCondition", ref(EBSKMSKey), AWS_NO_VALUE)


@cloudformation_dataclass
class DomainMember1WithInlineSsmAssociationBlockDeviceMapping:
    resource: ec2.instance.BlockDeviceMapping
    device_name = '/dev/sda1'
    ebs = DomainMember1WithInlineSsmAssociationEbs


@cloudformation_dataclass
class DomainMember1WithInlineSsmAssociation:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    image_id = ref(WINFULLBASE)
    iam_instance_profile = ref(DomainMembersWindowsInstanceProfile)
    ssm_associations = [DomainMember1WithInlineSsmAssociationSsmAssociation]
    instance_type = ref(DomainMembersInstanceType)
    subnet_id = ref(PrivateSubnet1ID)
    tags = [DomainMember1WithInlineSsmAssociationAssociationParameter2]
    block_device_mappings = [DomainMember1WithInlineSsmAssociationBlockDeviceMapping]
    security_group_ids = [ref(DomainMembersSGID)]
    key_name = ref(KeyPairName)
    user_data = Base64(Sub("""<powershell>
$instanceId = "null"
while ($instanceId -NotLike "i-*") {
Start-Sleep -s 3
$instanceId = Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/instance-id
}
Rename-Computer -NewName ${DomainMember1NetBIOSName} -Force
# Set-TimeZone -Name "US Eastern Standard Time"

Install-WindowsFeature -IncludeAllSubFeature RSAT
Restart-Computer -Force
</powershell>
"""))


@cloudformation_dataclass
class DomainMember2WithSsmAssociationInstanceAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = ref(DomainMember2NetBIOSName)


@cloudformation_dataclass
class DomainMember2WithSsmAssociationInstanceEbs:
    resource: ec2.instance.Ebs
    encrypted = True
    volume_type = 'gp3'
    delete_on_termination = True
    volume_size = 100
    kms_key_id = If("EBSKMSKeyCondition", ref(EBSKMSKey), AWS_NO_VALUE)


@cloudformation_dataclass
class DomainMember2WithSsmAssociationInstanceBlockDeviceMapping:
    resource: ec2.instance.BlockDeviceMapping
    device_name = '/dev/sda1'
    ebs = DomainMember2WithSsmAssociationInstanceEbs


@cloudformation_dataclass
class DomainMember2WithSsmAssociationInstance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
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
