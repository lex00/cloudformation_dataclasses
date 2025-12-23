"""PropertyTypes for AWS::ElasticBeanstalk::Environment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class OptionSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_name": "ResourceName",
        "value": "Value",
        "namespace": "Namespace",
        "option_name": "OptionName",
    }

    resource_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    namespace: Optional[Union[str, Ref, GetAtt, Sub]] = None
    option_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Tier(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "Type",
        "version": "Version",
        "name": "Name",
    }

    type_: Optional[Union[str, Ref, GetAtt, Sub]] = None
    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

