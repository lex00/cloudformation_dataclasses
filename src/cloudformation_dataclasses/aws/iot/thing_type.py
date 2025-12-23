"""PropertyTypes for AWS::IoT::ThingType."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Mqtt5Configuration(PropertyType):
    PROPAGATING_ATTRIBUTES = "PropagatingAttributes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "propagating_attributes": "PropagatingAttributes",
    }

    propagating_attributes: Optional[list[PropagatingAttribute]] = None


@dataclass
class PropagatingAttribute(PropertyType):
    USER_PROPERTY_KEY = "UserPropertyKey"
    THING_ATTRIBUTE = "ThingAttribute"
    CONNECTION_ATTRIBUTE = "ConnectionAttribute"

    _property_mappings: ClassVar[dict[str, str]] = {
        "user_property_key": "UserPropertyKey",
        "thing_attribute": "ThingAttribute",
        "connection_attribute": "ConnectionAttribute",
    }

    user_property_key: Optional[Union[str, Ref, GetAtt, Sub]] = None
    thing_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    connection_attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ThingTypeProperties(PropertyType):
    THING_TYPE_DESCRIPTION = "ThingTypeDescription"
    MQTT5_CONFIGURATION = "Mqtt5Configuration"
    SEARCHABLE_ATTRIBUTES = "SearchableAttributes"

    _property_mappings: ClassVar[dict[str, str]] = {
        "thing_type_description": "ThingTypeDescription",
        "mqtt5_configuration": "Mqtt5Configuration",
        "searchable_attributes": "SearchableAttributes",
    }

    thing_type_description: Optional[Union[str, Ref, GetAtt, Sub]] = None
    mqtt5_configuration: Optional[Mqtt5Configuration] = None
    searchable_attributes: Optional[Union[list[str], Ref]] = None

