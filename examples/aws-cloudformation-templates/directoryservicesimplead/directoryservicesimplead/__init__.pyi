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
from cloudformation_dataclasses.intrinsics import Equals, Select

from .main import SimpleAD as SimpleAD
from .main import SimpleADVpcSettings as SimpleADVpcSettings
from .outputs import DirectoryAliasOutput as DirectoryAliasOutput
from .outputs import DirectoryIDOutput as DirectoryIDOutput
from .outputs import PrimaryDNSOutput as PrimaryDNSOutput
from .outputs import SecondaryDNSOutput as SecondaryDNSOutput
from .params import AliasCondition as AliasCondition
from .params import CreateAlias as CreateAlias
from .params import DomainName as DomainName
from .params import PrivateSubnet1 as PrivateSubnet1
from .params import PrivateSubnet2 as PrivateSubnet2
from .params import SimpleADShortName as SimpleADShortName
from .params import Size as Size
from .params import VPCID as VPCID

__all__: list[str] = ['AliasCondition', 'CreateAlias', 'DirectoryAliasOutput', 'DirectoryIDOutput', 'DomainName', 'Equals', 'Output', 'Parameter', 'ParameterType', 'PrimaryDNSOutput', 'PrivateSubnet1', 'PrivateSubnet2', 'STRING', 'SecondaryDNSOutput', 'Select', 'SimpleAD', 'SimpleADShortName', 'SimpleADVpcSettings', 'Size', 'Template', 'TemplateCondition', 'VPCID', 'cloudformation_dataclass', 'directoryservice', 'get_att', 'ref', 'setup_resources']
