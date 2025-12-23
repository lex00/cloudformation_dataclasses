"""PropertyTypes for AWS::Lambda::EventInvokeConfig."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class DestinationConfig(PropertyType):
    ON_SUCCESS = "OnSuccess"
    ON_FAILURE = "OnFailure"

    _property_mappings: ClassVar[dict[str, str]] = {
        "on_success": "OnSuccess",
        "on_failure": "OnFailure",
    }

    on_success: Optional[OnSuccess] = None
    on_failure: Optional[OnFailure] = None


@dataclass
class OnFailure(PropertyType):
    DESTINATION = "Destination"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
    }

    destination: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OnSuccess(PropertyType):
    DESTINATION = "Destination"

    _property_mappings: ClassVar[dict[str, str]] = {
        "destination": "Destination",
    }

    destination: Optional[Union[str, Ref, GetAtt, Sub]] = None

