"""PropertyTypes for AWS::Pinpoint::InAppTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class BodyConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "alignment": "Alignment",
        "text_color": "TextColor",
        "body": "Body",
    }

    alignment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    body: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class ButtonConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "web": "Web",
        "default_config": "DefaultConfig",
        "ios": "IOS",
        "android": "Android",
    }

    web: Optional[OverrideButtonConfiguration] = None
    default_config: Optional[DefaultButtonConfiguration] = None
    ios: Optional[OverrideButtonConfiguration] = None
    android: Optional[OverrideButtonConfiguration] = None


@dataclass
class DefaultButtonConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "border_radius": "BorderRadius",
        "button_action": "ButtonAction",
        "text": "Text",
        "text_color": "TextColor",
        "link": "Link",
        "background_color": "BackgroundColor",
    }

    border_radius: Optional[Union[int, Ref, GetAtt, Sub]] = None
    button_action: Optional[Union[str, ButtonAction, Ref, GetAtt, Sub]] = None
    text: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_color: Optional[Union[str, Ref, GetAtt, Sub]] = None
    link: Optional[Union[str, Ref, GetAtt, Sub]] = None
    background_color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HeaderConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "alignment": "Alignment",
        "header": "Header",
        "text_color": "TextColor",
    }

    alignment: Optional[Union[str, Ref, GetAtt, Sub]] = None
    header: Optional[Union[str, Ref, GetAtt, Sub]] = None
    text_color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class InAppMessageContent(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "body_config": "BodyConfig",
        "secondary_btn": "SecondaryBtn",
        "image_url": "ImageUrl",
        "primary_btn": "PrimaryBtn",
        "header_config": "HeaderConfig",
        "background_color": "BackgroundColor",
    }

    body_config: Optional[BodyConfig] = None
    secondary_btn: Optional[ButtonConfig] = None
    image_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    primary_btn: Optional[ButtonConfig] = None
    header_config: Optional[HeaderConfig] = None
    background_color: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class OverrideButtonConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "button_action": "ButtonAction",
        "link": "Link",
    }

    button_action: Optional[Union[str, ButtonAction, Ref, GetAtt, Sub]] = None
    link: Optional[Union[str, Ref, GetAtt, Sub]] = None

