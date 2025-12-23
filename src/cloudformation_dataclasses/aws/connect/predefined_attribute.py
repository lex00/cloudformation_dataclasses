"""PropertyTypes for AWS::Connect::PredefinedAttribute."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class AttributeConfiguration(PropertyType):
    ENABLE_VALUE_VALIDATION_ON_ASSOCIATION = "EnableValueValidationOnAssociation"
    IS_READ_ONLY = "IsReadOnly"

    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_value_validation_on_association": "EnableValueValidationOnAssociation",
        "is_read_only": "IsReadOnly",
    }

    enable_value_validation_on_association: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    is_read_only: Optional[Union[bool, Ref, GetAtt, Sub]] = None


@dataclass
class Values(PropertyType):
    STRING_LIST = "StringList"

    _property_mappings: ClassVar[dict[str, str]] = {
        "string_list": "StringList",
    }

    string_list: Optional[Union[list[str], Ref]] = None

