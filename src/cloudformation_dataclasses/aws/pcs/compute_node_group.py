"""PropertyTypes for AWS::PCS::ComputeNodeGroup."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class CustomLaunchTemplate(PropertyType):
    VERSION = "Version"
    TEMPLATE_ID = "TemplateId"

    _property_mappings: ClassVar[dict[str, str]] = {
        "version": "Version",
        "template_id": "TemplateId",
    }

    version: Optional[Union[str, Ref, GetAtt, Sub]] = None
    template_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ErrorInfo(PropertyType):
    MESSAGE = "Message"
    CODE = "Code"

    _property_mappings: ClassVar[dict[str, str]] = {
        "message": "Message",
        "code": "Code",
    }

    message: Optional[Union[str, Ref, GetAtt, Sub]] = None
    code: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InstanceConfig(PropertyType):
    INSTANCE_TYPE = "InstanceType"

    _property_mappings: ClassVar[dict[str, str]] = {
        "instance_type": "InstanceType",
    }

    instance_type: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ScalingConfiguration(PropertyType):
    MAX_INSTANCE_COUNT = "MaxInstanceCount"
    MIN_INSTANCE_COUNT = "MinInstanceCount"

    _property_mappings: ClassVar[dict[str, str]] = {
        "max_instance_count": "MaxInstanceCount",
        "min_instance_count": "MinInstanceCount",
    }

    max_instance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None
    min_instance_count: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class SlurmConfiguration(PropertyType):
    SLURM_CUSTOM_SETTINGS = "SlurmCustomSettings"

    _property_mappings: ClassVar[dict[str, str]] = {
        "slurm_custom_settings": "SlurmCustomSettings",
    }

    slurm_custom_settings: Optional[list[SlurmCustomSetting]] = None


@dataclass
class SlurmCustomSetting(PropertyType):
    PARAMETER_VALUE = "ParameterValue"
    PARAMETER_NAME = "ParameterName"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameter_value": "ParameterValue",
        "parameter_name": "ParameterName",
    }

    parameter_value: Optional[Union[str, Ref, GetAtt, Sub]] = None
    parameter_name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SpotOptions(PropertyType):
    ALLOCATION_STRATEGY = "AllocationStrategy"

    _property_mappings: ClassVar[dict[str, str]] = {
        "allocation_strategy": "AllocationStrategy",
    }

    allocation_strategy: Optional[Union[str, Ref, GetAtt, Sub]] = None

