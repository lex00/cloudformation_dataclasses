"""AWSManagedAD - AWS::DirectoryService::MicrosoftAD resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AWSManagedADVpcSettings:
    resource: directoryservice.microsoft_ad.VpcSettings
    subnet_ids = [ref(PrivateSubnet1ID), ref(PrivateSubnet2ID)]
    vpc_id = ref(VPCID)


@cloudformation_dataclass
class AWSManagedAD:
    """AWS::DirectoryService::MicrosoftAD resource."""

    resource: directoryservice.MicrosoftAD
    name = ref(AWSManagedADDomainDNSName)
    short_name = ref(AWSManagedADDomainNetBiosName)
    password = '{{resolve:secretsmanager:AWSManagedADAdminPassword:SecretString:password}}'
    edition = ref(AWSManagedADEdition)
    vpc_settings = AWSManagedADVpcSettings
