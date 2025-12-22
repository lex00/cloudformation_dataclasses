"""SimpleAD - AWS::DirectoryService::SimpleAD resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SimpleADVpcSettings:
    resource: directoryservice.microsoft_ad.VpcSettings
    subnet_ids = [Select(0, ref(PrivateSubnet1)), Select(0, ref(PrivateSubnet2))]
    vpc_id = Select(0, ref(VPCID))


@cloudformation_dataclass
class SimpleAD:
    """AWS::DirectoryService::SimpleAD resource."""

    resource: directoryservice.SimpleAD
    create_alias = False
    enable_sso = False
    name = ref(DomainName)
    password = '{{resolve:secretsmanager:simple-ad-pw:SecretString:pasword}}'
    short_name = ref(SimpleADShortName)
    size = ref(Size)
    vpc_settings = SimpleADVpcSettings
