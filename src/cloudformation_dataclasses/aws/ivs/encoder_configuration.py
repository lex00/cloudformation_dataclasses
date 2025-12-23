"""PropertyTypes for AWS::IVS::EncoderConfiguration."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class Video(PropertyType):
    FRAMERATE = "Framerate"
    HEIGHT = "Height"
    BITRATE = "Bitrate"
    WIDTH = "Width"

    _property_mappings: ClassVar[dict[str, str]] = {
        "framerate": "Framerate",
        "height": "Height",
        "bitrate": "Bitrate",
        "width": "Width",
    }

    framerate: Optional[Union[float, Ref, GetAtt, Sub]] = None
    height: Optional[Union[int, Ref, GetAtt, Sub]] = None
    bitrate: Optional[Union[int, Ref, GetAtt, Sub]] = None
    width: Optional[Union[int, Ref, GetAtt, Sub]] = None

