"""DomainMember1WithInlineSsmAssociation - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DomainMember1WithInlineSsmAssociationAssociationParameter:
    resource: AssociationParameter
    key = 'directoryId'
    value = [ref(DirectoryID)]


@cloudformation_dataclass
class DomainMember1WithInlineSsmAssociationAssociationParameter1:
    resource: AssociationParameter
    key = 'directoryName'
    value = [ref(DirectoryName)]


@cloudformation_dataclass
class DomainMember1WithInlineSsmAssociationSsmAssociation:
    resource: SsmAssociation
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
    resource: AssociationParameter
    key = 'Name'
    value = ref(DomainMember1NetBIOSName)


@cloudformation_dataclass
class DomainMember1WithInlineSsmAssociationEbsBlockDevice:
    resource: EbsBlockDevice
    encrypted = True
    volume_type = 'gp3'
    delete_on_termination = True
    volume_size = 100
    # Unknown CF key: KmsKeyId = If("EBSKMSKeyCondition", ref(EBSKMSKey), AWS_NO_VALUE)


@cloudformation_dataclass
class DomainMember1WithInlineSsmAssociationBlockDeviceMapping:
    resource: BlockDeviceMapping
    device_name = '/dev/sda1'
    ebs = DomainMember1WithInlineSsmAssociationEbsBlockDevice


@cloudformation_dataclass
class DomainMember1WithInlineSsmAssociation:
    """AWS::EC2::Instance resource."""

    resource: Instance
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
