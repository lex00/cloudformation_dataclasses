"""PropertyTypes for AWS::Lightsail::Database."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class RelationalDatabaseParameter(PropertyType):
    APPLY_METHOD = "ApplyMethod"
    IS_MODIFIABLE = "IsModifiable"
    APPLY_TYPE = "ApplyType"
    ALLOWED_VALUES = "AllowedValues"
    DESCRIPTION = "Description"
    PARAMETER_VALUE = "ParameterValue"
    DATA_TYPE = "DataType"
    PARAMETER_NAME = "ParameterName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "apply_method": "ApplyMethod",
        "is_modifiable": "IsModifiable",
        "apply_type": "ApplyType",
        "allowed_values": "AllowedValues",
        "description": "Description",
        "parameter_value": "ParameterValue",
        "data_type": "DataType",
        "parameter_name": "ParameterName",
    }

    apply_method: Optional[Union[str, Ref, GetAtt, Sub]] = None
    is_modifiable: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    apply_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    allowed_values: Optional[Union[str, Ref, GetAtt, Sub]] = None
    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameter_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    data_type: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

