"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    Parameter,
    ParameterType,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.template import Condition as TemplateCondition
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import directoryservice
from cloudformation_dataclasses.aws.directoryservice import MicrosoftAD
from cloudformation_dataclasses.intrinsics import Equals, Select

from .main import rMSDirectory as rMSDirectory
from .main import rMSDirectoryVpcSettings as rMSDirectoryVpcSettings
from .outputs import DirectoryAliasOutput as DirectoryAliasOutput
from .outputs import DirectoryIDOutput as DirectoryIDOutput
from .outputs import PrimaryDNSOutput as PrimaryDNSOutput
from .outputs import SecondaryDNSOutput as SecondaryDNSOutput
from .params import cAliasCondition as cAliasCondition
from .params import pCreateAlias as pCreateAlias
from .params import pDomainName as pDomainName
from .params import pEdition as pEdition
from .params import pEnableSingleSignOn as pEnableSingleSignOn
from .params import pMicrosoftADShortName as pMicrosoftADShortName
from .params import pPrivateSubnet1 as pPrivateSubnet1
from .params import pPrivateSubnet2 as pPrivateSubnet2
from .params import pVPCID as pVPCID

__all__: list[str] = ['DirectoryAliasOutput', 'DirectoryIDOutput', 'Equals', 'MicrosoftAD', 'Output', 'Parameter', 'ParameterType', 'PrimaryDNSOutput', 'STRING', 'SecondaryDNSOutput', 'Select', 'Template', 'TemplateCondition', 'cAliasCondition', 'cloudformation_dataclass', 'directoryservice', 'get_att', 'pCreateAlias', 'pDomainName', 'pEdition', 'pEnableSingleSignOn', 'pMicrosoftADShortName', 'pPrivateSubnet1', 'pPrivateSubnet2', 'pVPCID', 'rMSDirectory', 'rMSDirectoryVpcSettings', 'ref', 'setup_resources']
