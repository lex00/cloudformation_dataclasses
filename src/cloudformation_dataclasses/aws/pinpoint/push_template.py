"""PropertyTypes for AWS::Pinpoint::PushTemplate."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class APNSPushNotificationTemplate(PropertyType):
    ACTION = "Action"
    MEDIA_URL = "MediaUrl"
    TITLE = "Title"
    SOUND = "Sound"
    BODY = "Body"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "media_url": "MediaUrl",
        "title": "Title",
        "sound": "Sound",
        "body": "Body",
        "url": "Url",
    }

    action: Optional[Union[str, Action, Ref, GetAtt, Sub]] = None
    media_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sound: Optional[Union[str, Ref, GetAtt, Sub]] = None
    body: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class AndroidPushNotificationTemplate(PropertyType):
    ACTION = "Action"
    IMAGE_URL = "ImageUrl"
    SMALL_IMAGE_ICON_URL = "SmallImageIconUrl"
    TITLE = "Title"
    IMAGE_ICON_URL = "ImageIconUrl"
    SOUND = "Sound"
    BODY = "Body"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "image_url": "ImageUrl",
        "small_image_icon_url": "SmallImageIconUrl",
        "title": "Title",
        "image_icon_url": "ImageIconUrl",
        "sound": "Sound",
        "body": "Body",
        "url": "Url",
    }

    action: Optional[Union[str, Action, Ref, GetAtt, Sub]] = None
    image_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    small_image_icon_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    image_icon_url: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sound: Optional[Union[str, Ref, GetAtt, Sub]] = None
    body: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class DefaultPushNotificationTemplate(PropertyType):
    ACTION = "Action"
    TITLE = "Title"
    SOUND = "Sound"
    BODY = "Body"
    URL = "Url"

    _property_mappings: ClassVar[dict[str, str]] = {
        "action": "Action",
        "title": "Title",
        "sound": "Sound",
        "body": "Body",
        "url": "Url",
    }

    action: Optional[Union[str, Action, Ref, GetAtt, Sub]] = None
    title: Optional[Union[str, Ref, GetAtt, Sub]] = None
    sound: Optional[Union[str, Ref, GetAtt, Sub]] = None
    body: Optional[Union[str, Ref, GetAtt, Sub]] = None
    url: Optional[Union[str, Ref, GetAtt, Sub]] = None

