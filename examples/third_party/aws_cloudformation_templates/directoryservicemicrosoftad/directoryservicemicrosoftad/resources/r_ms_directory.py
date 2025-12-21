from __future__ import annotations

"""rMSDirectory - AWS::DirectoryService::MicrosoftAD resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class rMSDirectoryVpcSettings:
    resource: VpcSettings
    subnet_ids = [ref(pPrivateSubnet1), ref(pPrivateSubnet2)]
    vpc_id = ref(pVPCID)


@cloudformation_dataclass
class rMSDirectory:
    """AWS::DirectoryService::MicrosoftAD resource."""

    resource: MicrosoftAD
    create_alias = ref(pCreateAlias)
    edition = ref(pEdition)
    enable_sso = ref(pEnableSingleSignOn)
    name = ref(pDomainName)
    password = '{{resolve:secretsmanager:microsoft-ad-pw:SecretString:password}}'
    short_name = ref(pMicrosoftADShortName)
    vpc_settings = rMSDirectoryVpcSettings
