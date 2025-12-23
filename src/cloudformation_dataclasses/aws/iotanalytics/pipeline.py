"""PropertyTypes for AWS::IoTAnalytics::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Activity(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "select_attributes": "SelectAttributes",
        "datastore": "Datastore",
        "filter": "Filter",
        "add_attributes": "AddAttributes",
        "channel": "Channel",
        "device_shadow_enrich": "DeviceShadowEnrich",
        "math": "Math",
        "lambda_": "Lambda",
        "device_registry_enrich": "DeviceRegistryEnrich",
        "remove_attributes": "RemoveAttributes",
    }

    select_attributes: Optional[SelectAttributes] = None
    datastore: Optional[Datastore] = None
    filter: Optional[Filter] = None
    add_attributes: Optional[AddAttributes] = None
    channel: Optional[Channel] = None
    device_shadow_enrich: Optional[DeviceShadowEnrich] = None
    math: Optional[Math] = None
    lambda_: Optional[Lambda] = None
    device_registry_enrich: Optional[DeviceRegistryEnrich] = None
    remove_attributes: Optional[RemoveAttributes] = None


@dataclass
class AddAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "next": "Next",
        "attributes": "Attributes",
        "name": "Name",
    }

    next: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attributes: Optional[dict[str, str]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Channel(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "channel_name": "ChannelName",
        "next": "Next",
        "name": "Name",
    }

    channel_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    next: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Datastore(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "datastore_name": "DatastoreName",
        "name": "Name",
    }

    datastore_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeviceRegistryEnrich(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute": "Attribute",
        "next": "Next",
        "thing_name": "ThingName",
        "role_arn": "RoleArn",
        "name": "Name",
    }

    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    next: Optional[Union[str, Ref, GetAtt, Sub]] = None
    thing_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DeviceShadowEnrich(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute": "Attribute",
        "next": "Next",
        "thing_name": "ThingName",
        "role_arn": "RoleArn",
        "name": "Name",
    }

    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    next: Optional[Union[str, Ref, GetAtt, Sub]] = None
    thing_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    role_arn: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Filter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "filter": "Filter",
        "next": "Next",
        "name": "Name",
    }

    filter: Optional[Union[str, Ref, GetAtt, Sub]] = None
    next: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Lambda(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "batch_size": "BatchSize",
        "next": "Next",
        "lambda_name": "LambdaName",
        "name": "Name",
    }

    batch_size: Optional[Union[int, Ref, GetAtt, Sub]] = None
    next: Optional[Union[str, Ref, GetAtt, Sub]] = None
    lambda_name: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class Math(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "attribute": "Attribute",
        "next": "Next",
        "math": "Math",
        "name": "Name",
    }

    attribute: Optional[Union[str, Ref, GetAtt, Sub]] = None
    next: Optional[Union[str, Ref, GetAtt, Sub]] = None
    math: Optional[Union[str, Ref, GetAtt, Sub]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class RemoveAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "next": "Next",
        "attributes": "Attributes",
        "name": "Name",
    }

    next: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attributes: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class SelectAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "next": "Next",
        "attributes": "Attributes",
        "name": "Name",
    }

    next: Optional[Union[str, Ref, GetAtt, Sub]] = None
    attributes: Optional[Union[list[str], Ref]] = None
    name: Optional[Union[str, Ref, GetAtt, Sub]] = None

