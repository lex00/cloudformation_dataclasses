"""myEC2InstanceSSM - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class myEC2InstanceSSMAssociationParameter:
    resource: AssociationParameter
    key = 'directoryId'
    value = [ref(ADDirectoryId)]


@cloudformation_dataclass
class myEC2InstanceSSMAssociationParameter1:
    resource: AssociationParameter
    key = 'directoryName'
    value = [ref(ADDirectoryName)]


@cloudformation_dataclass
class myEC2InstanceSSMAssociationParameter2:
    resource: AssociationParameter
    key = 'dnsIpAddresses'
    value = [ref(ADDnsIpAddresses1), ref(ADDnsIpAddresses2)]


@cloudformation_dataclass
class myEC2InstanceSSMSsmAssociation:
    resource: SsmAssociation
    document_name = ref(myssmdocument)
    association_parameters = [myEC2InstanceSSMAssociationParameter, myEC2InstanceSSMAssociationParameter1, myEC2InstanceSSMAssociationParameter2]


@cloudformation_dataclass
class myEC2InstanceSSMAssociationParameter3:
    resource: AssociationParameter
    key = 'Name'
    value = 'myEC2InstanceSSM'


@cloudformation_dataclass
class myEC2InstanceSSM:
    """AWS::EC2::Instance resource."""

    resource: Instance
    iam_instance_profile = ref(myInstanceProfile)
    ssm_associations = [myEC2InstanceSSMSsmAssociation]
    key_name = ref(KeyPair)
    image_id = ref(AMI)
    instance_type = ref(InstanceType)
    tags = [myEC2InstanceSSMAssociationParameter3]
    subnet_id = ref(PublicSubnet)
    security_group_ids = [get_att(InstanceSecurityGroup, "GroupId")]
