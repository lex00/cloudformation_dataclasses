"""PropertyTypes for AWS::Config::ConfigurationRecorder."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class ExclusionByResourceTypes(PropertyType):
    RESOURCE_TYPES = "ResourceTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_types": "ResourceTypes",
    }

    resource_types: Optional[Union[list[str], Ref]] = None


@dataclass
class RecordingGroup(PropertyType):
    ALL_SUPPORTED = "AllSupported"
    EXCLUSION_BY_RESOURCE_TYPES = "ExclusionByResourceTypes"
    INCLUDE_GLOBAL_RESOURCE_TYPES = "IncludeGlobalResourceTypes"
    RECORDING_STRATEGY = "RecordingStrategy"
    RESOURCE_TYPES = "ResourceTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "all_supported": "AllSupported",
        "exclusion_by_resource_types": "ExclusionByResourceTypes",
        "include_global_resource_types": "IncludeGlobalResourceTypes",
        "recording_strategy": "RecordingStrategy",
        "resource_types": "ResourceTypes",
    }

    all_supported: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    exclusion_by_resource_types: Optional[ExclusionByResourceTypes] = None
    include_global_resource_types: Optional[Union[bool, Ref, GetAtt, Sub]] = None
    recording_strategy: Optional[RecordingStrategy] = None
    resource_types: Optional[Union[list[str], Ref]] = None


@dataclass
class RecordingMode(PropertyType):
    RECORDING_FREQUENCY = "RecordingFrequency"
    RECORDING_MODE_OVERRIDES = "RecordingModeOverrides"

    _property_mappings: ClassVar[dict[str, str]] = {
        "recording_frequency": "RecordingFrequency",
        "recording_mode_overrides": "RecordingModeOverrides",
    }

    recording_frequency: Optional[Union[str, Ref, GetAtt, Sub]] = None
    recording_mode_overrides: Optional[list[RecordingModeOverride]] = None


@dataclass
class RecordingModeOverride(PropertyType):
    DESCRIPTION = "Description"
    RECORDING_FREQUENCY = "RecordingFrequency"
    RESOURCE_TYPES = "ResourceTypes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "description": "Description",
        "recording_frequency": "RecordingFrequency",
        "resource_types": "ResourceTypes",
    }

    description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    recording_frequency: Optional[Union[str, Ref, GetAtt, Sub]] = None
    resource_types: Optional[Union[list[str], Ref]] = None


@dataclass
class RecordingStrategy(PropertyType):
    USE_ONLY = "UseOnly"

    _property_mappings: ClassVar[dict[str, str]] = {
        "use_only": "UseOnly",
    }

    use_only: Optional[Union[str, Ref, GetAtt, Sub]] = None

