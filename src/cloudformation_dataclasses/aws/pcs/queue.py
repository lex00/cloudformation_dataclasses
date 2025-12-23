"""PropertyTypes for AWS::PCS::Queue."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ComputeNodeGroupConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "compute_node_group_id": "ComputeNodeGroupId",
    }

    compute_node_group_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ErrorInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "message": "Message",
        "code": "Code",
    }

    message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SlurmConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "slurm_custom_settings": "SlurmCustomSettings",
    }

    slurm_custom_settings: Optional[list[SlurmCustomSetting]] = None


@dataclass
class SlurmCustomSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_value": "ParameterValue",
        "parameter_name": "ParameterName",
    }

    parameter_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None

