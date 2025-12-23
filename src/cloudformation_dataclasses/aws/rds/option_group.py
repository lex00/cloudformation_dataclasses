"""PropertyTypes for AWS::RDS::OptionGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class OptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "option_version": "OptionVersion",
        "vpc_security_group_memberships": "VpcSecurityGroupMemberships",
        "option_settings": "OptionSettings",
        "port": "Port",
        "option_name": "OptionName",
        "db_security_group_memberships": "DBSecurityGroupMemberships",
    }

    option_version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    vpc_security_group_memberships: Optional[Union[list[str], Ref]] = None
    option_settings: Optional[list[OptionSetting]] = None
    port: Optional[Union[int, Ref, GetAtt, Sub]] = None
    option_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    db_security_group_memberships: Optional[Union[list[str], Ref]] = None


@dataclass
class OptionSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "value": "Value",
        "name": "Name",
    }

    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

