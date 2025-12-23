"""PropertyTypes for AWS::DataZone::EnvironmentBlueprintConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class LakeFormationConfiguration(PropertyType):
    LOCATION_REGISTRATION_EXCLUDE_S3_LOCATIONS = "LocationRegistrationExcludeS3Locations"
    LOCATION_REGISTRATION_ROLE = "LocationRegistrationRole"

    _property_mappings: ClassVar[dict[str, str]] = {
        "location_registration_exclude_s3_locations": "LocationRegistrationExcludeS3Locations",
        "location_registration_role": "LocationRegistrationRole",
    }

    location_registration_exclude_s3_locations: Optional[Union[list[str], Ref]] = None
    location_registration_role: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ProvisioningConfiguration(PropertyType):
    LAKE_FORMATION_CONFIGURATION = "LakeFormationConfiguration"

    _property_mappings: ClassVar[dict[str, str]] = {
        "lake_formation_configuration": "LakeFormationConfiguration",
    }

    lake_formation_configuration: Optional[LakeFormationConfiguration] = None


@dataclass
class RegionalParameter(PropertyType):
    PARAMETERS = "Parameters"
    REGION = "Region"

    _property_mappings: ClassVar[dict[str, str]] = {
        "parameters": "Parameters",
        "region": "Region",
    }

    parameters: Optional[dict[str, str]] = None
    region: Optional[Union[str, Ref, GetAtt, Sub]] = None

